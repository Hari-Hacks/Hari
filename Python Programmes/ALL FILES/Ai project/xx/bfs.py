import tkinter as tk
from collections import deque

# ── Constants ──────────────────────────────────────────────────────────────────
GRID_SIZE  = 9
CELL_SIZE  = 64
PAD        = 24
PANEL_W    = 230
ANIM_MS    = 220          # ms per bot step (adjustable via slider)

# Palette — dark terminal aesthetic
BG         = "#0a0e14"
GRID_BG    = "#0d1219"
GRID_LINE  = "#1e2a38"
C_UNKNOWN  = "#111820"    # fog-of-war (unexplored, hidden)
C_EMPTY    = "#1a2636"    # explored, passable
C_OBS      = "#8b1a1a"    # obstacle (placed by user, revealed when bot steps near)
C_FRONTIER = "#0e4a6e"    # BFS frontier (queued)
C_VISITED  = "#1e3a52"    # visited by bot
C_BOT      = "#00d4ff"    # bot current position
C_START    = "#00c97a"    # start marker
C_HOVER    = "#1f3048"
TEXT_PRI   = "#cdd9e5"
TEXT_SEC   = "#546e7a"
TEXT_ACC   = "#00d4ff"
TEXT_WARN  = "#f0a500"
BTN_GO     = "#0d5c2e"
BTN_STOP   = "#6b1212"
BTN_RST    = "#1c2230"
BTN_FG     = "#cdd9e5"
DIRS       = [(-1,0),(0,1),(1,0),(0,-1)]   # N E S W


class BFSExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BFS Unknown-Environment Explorer  ·  9×9")
        self.resizable(False, False)
        self.configure(bg=BG)

        cw = GRID_SIZE * CELL_SIZE + PAD * 2
        ch = GRID_SIZE * CELL_SIZE + PAD * 2

        # ── State ──────────────────────────────────────────────────────────────
        self.mode        = tk.StringVar(value="obstacle")
        self.obstacles   = set()          # cells permanently blocked
        self.start       = None           # (r,c)

        # Runtime
        self.known       = set()          # cells bot has "seen" (adjacent or visited)
        self.visited     = set()          # cells bot physically stepped on
        self.frontier    = deque()        # BFS queue  [(r,c), …]
        self.frontier_set= set()          # for O(1) lookup
        self.bot_pos     = None
        self.running     = False
        self.done        = False
        self.after_id    = None
        self.step_count  = 0

        self.speed_ms    = tk.IntVar(value=ANIM_MS)

        # ── Widgets ────────────────────────────────────────────────────────────
        self.canvas = tk.Canvas(self, width=cw, height=ch,
                                bg=GRID_BG, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=(PAD,0), pady=PAD)

        panel = tk.Frame(self, bg=BG, width=PANEL_W)
        panel.grid(row=0, column=1, sticky="nsew", padx=PAD, pady=PAD)
        panel.grid_propagate(False)

        self._build_panel(panel)
        self.rects = {}
        self._draw_base_grid()
        self._bind()

    # ── Panel ──────────────────────────────────────────────────────────────────
    def _build_panel(self, p):
        def lbl(txt, size=10, fg=TEXT_PRI, pady=0, bold=False):
            f = ("Courier", size, "bold") if bold else ("Courier", size)
            tk.Label(p, text=txt, font=f, bg=BG, fg=fg)\
              .pack(anchor="w", pady=(pady,0))

        def sep():
            tk.Frame(p, bg=GRID_LINE, height=1).pack(fill="x", pady=8)

        def btn(txt, cmd, bg=BTN_RST, fg=BTN_FG, pady=3):
            b = tk.Button(p, text=txt, command=cmd, font=("Courier",10,"bold"),
                          bg=bg, fg=fg, activebackground=bg, activeforeground=fg,
                          relief="flat", cursor="hand2", padx=6, pady=7,
                          highlightbackground=GRID_LINE, bd=1)
            b.pack(fill="x", pady=(pady,0))
            return b

        lbl("BFS  EXPLORER", 14, TEXT_ACC, 2, bold=True)
        lbl("Unknown Environment  ·  9×9", 9, TEXT_SEC)
        sep()

        lbl("PLACE MODE", 9, TEXT_SEC)
        for val, txt in [("obstacle","⬛  Obstacle (drag to paint)"),
                         ("start",   "🔵  Start position")]:
            tk.Radiobutton(p, text=txt, variable=self.mode, value=val,
                           font=("Courier",10), bg=BG, fg=TEXT_PRI,
                           selectcolor="#16202e", activebackground=BG,
                           activeforeground=TEXT_ACC,
                           cursor="hand2").pack(anchor="w", pady=2)

        sep()

        lbl("LEGEND", 9, TEXT_SEC)
        for clr, txt in [
            (C_UNKNOWN,  "Fog of war (unseen)"),
            (C_START,    "Start cell"),
            (C_BOT,      "Bot (current)"),
            (C_FRONTIER, "BFS frontier"),
            (C_VISITED,  "Explored path"),
            (C_EMPTY,    "Mapped (passable)"),
            (C_OBS,      "Obstacle"),
        ]:
            row = tk.Frame(p, bg=BG); row.pack(anchor="w", pady=1)
            tk.Frame(row, bg=clr, width=13, height=13).pack(side="left")
            tk.Label(row, text=f"  {txt}", font=("Courier",9),
                     bg=BG, fg=TEXT_SEC).pack(side="left")

        sep()

        # Speed slider
        lbl("SPEED", 9, TEXT_SEC)
        spd_row = tk.Frame(p, bg=BG); spd_row.pack(fill="x")
        tk.Label(spd_row, text="Fast", font=("Courier",8), bg=BG,
                 fg=TEXT_SEC).pack(side="left")
        tk.Scale(spd_row, from_=50, to=600, orient="horizontal",
                 variable=self.speed_ms, bg=BG, fg=TEXT_PRI,
                 troughcolor=GRID_LINE, highlightthickness=0,
                 showvalue=False, length=110).pack(side="left", padx=4)
        tk.Label(spd_row, text="Slow", font=("Courier",8), bg=BG,
                 fg=TEXT_SEC).pack(side="left")

        sep()

        self.go_btn   = btn("▶  Start Exploring", self._start_explore, BTN_GO)
        self.stop_btn = btn("⏸  Pause / Resume",  self._toggle_pause,  BTN_RST)
        btn("🔄  Reset", self._reset, BTN_STOP, "#ffaaaa", pady=6)

        sep()

        self.stat_var = tk.StringVar(value="Place Start, then explore.")
        tk.Label(p, textvariable=self.stat_var, font=("Courier",9),
                 bg=BG, fg=TEXT_SEC, wraplength=PANEL_W-12,
                 justify="left").pack(anchor="w")

        self.info_var = tk.StringVar(value="")
        tk.Label(p, textvariable=self.info_var, font=("Courier",9,"bold"),
                 bg=BG, fg=TEXT_ACC, wraplength=PANEL_W-12,
                 justify="left").pack(anchor="w", pady=(3,0))

    # ── Grid drawing ───────────────────────────────────────────────────────────
    def _draw_base_grid(self):
        self.canvas.delete("all")
        self.rects.clear()

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x1 = PAD + c*CELL_SIZE
                y1 = PAD + r*CELL_SIZE
                rid = self.canvas.create_rectangle(
                    x1+1, y1+1, x1+CELL_SIZE-1, y1+CELL_SIZE-1,
                    fill=C_UNKNOWN, outline="")
                self.rects[(r,c)] = rid
                # axis labels
                if c == 0:
                    self.canvas.create_text(x1-7, y1+CELL_SIZE//2,
                        text=str(r), font=("Courier",8), fill=GRID_LINE, anchor="e")
                if r == 0:
                    self.canvas.create_text(x1+CELL_SIZE//2, y1-7,
                        text=str(c), font=("Courier",8), fill=GRID_LINE, anchor="s")

        # grid lines
        for i in range(GRID_SIZE+1):
            x = PAD + i*CELL_SIZE
            y = PAD + i*CELL_SIZE
            self.canvas.create_line(PAD, y, PAD+GRID_SIZE*CELL_SIZE, y,
                                    fill=GRID_LINE)
            self.canvas.create_line(x, PAD, x, PAD+GRID_SIZE*CELL_SIZE,
                                    fill=GRID_LINE)

        self.bot_oval = None
        self._refresh()

    def _cell_color(self, r, c):
        if self.bot_pos == (r,c):
            return C_BOT
        if (r,c) == self.start:
            # show start distinctly even after visited
            return C_START
        if (r,c) in self.known:
            if (r,c) in self.obstacles:
                return C_OBS
            if (r,c) in self.frontier_set:
                return C_FRONTIER
            if (r,c) in self.visited:
                return C_VISITED
            return C_EMPTY
        return C_UNKNOWN

    def _paint(self, r, c):
        self.canvas.itemconfig(self.rects[(r,c)], fill=self._cell_color(r,c))

    def _refresh(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                self._paint(r, c)
        self._redraw_bot()

    def _redraw_bot(self):
        if self.bot_oval:
            self.canvas.delete(self.bot_oval)
            self.canvas.delete("botlabel")
            self.bot_oval = None
        if self.bot_pos:
            r, c = self.bot_pos
            x = PAD + c*CELL_SIZE + CELL_SIZE//2
            y = PAD + r*CELL_SIZE + CELL_SIZE//2
            rad = CELL_SIZE//2 - 7
            self.bot_oval = self.canvas.create_oval(
                x-rad, y-rad, x+rad, y+rad,
                fill=C_BOT, outline="#ffffff", width=2)
            self.canvas.create_text(x, y, text="🤖",
                font=("",16), tags="botlabel")

    # ── Events ─────────────────────────────────────────────────────────────────
    def _bind(self):
        self.canvas.bind("<Button-1>",  self._click)
        self.canvas.bind("<B1-Motion>", self._drag)
        self.canvas.bind("<Motion>",    self._hover)
        self.canvas.bind("<Leave>",     self._leave)
        self._hov = None

    def _cell_at(self, e):
        c = (e.x - PAD) // CELL_SIZE
        r = (e.y - PAD) // CELL_SIZE
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            return r, c
        return None

    def _hover(self, e):
        cell = self._cell_at(e)
        if cell == self._hov: return
        if self._hov: self._paint(*self._hov)
        self._hov = cell
        if cell and not self.running:
            self.canvas.itemconfig(self.rects[cell], fill=C_HOVER)

    def _leave(self, _):
        if self._hov: self._paint(*self._hov)
        self._hov = None

    def _click(self, e):
        cell = self._cell_at(e)
        if cell and not self.running:
            self._place(cell)

    def _drag(self, e):
        cell = self._cell_at(e)
        if cell and not self.running and self.mode.get() == "obstacle":
            self._place(cell)

    def _place(self, cell):
        r, c = cell
        if self.mode.get() == "obstacle":
            if (r,c) == self.start: return
            if (r,c) in self.obstacles:
                self.obstacles.discard((r,c))
            else:
                self.obstacles.add((r,c))
        else:  # start
            self.start   = (r,c)
            self.bot_pos = (r,c)
            self.obstacles.discard((r,c))
        self.stat_var.set(f"Placed {self.mode.get()} at ({r},{c}).")
        self._paint(r, c)
        if self.start and self.start == (r,c):
            # Show start immediately
            self.canvas.itemconfig(self.rects[(r,c)], fill=C_START)
        self._redraw_bot()

    # ── BFS exploration logic ──────────────────────────────────────────────────
    def _reveal_adjacent(self, r, c):
        """Mark cells adjacent to (r,c) as known (fog lifted)."""
        for dr, dc in DIRS + [(0,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                self.known.add((nr,nc))

    def _enqueue_passable_neighbors(self, r, c):
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if (0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE
                    and (nr,nc) not in self.visited
                    and (nr,nc) not in self.obstacles
                    and (nr,nc) not in self.frontier_set):
                self.frontier.append((nr,nc))
                self.frontier_set.add((nr,nc))

    def _start_explore(self):
        if self.running: return
        if not self.start:
            self.stat_var.set("⚠  Place a Start cell first!")
            return

        # Init BFS from start
        self.known.clear()
        self.visited.clear()
        self.frontier.clear()
        self.frontier_set.clear()
        self.bot_pos   = self.start
        self.step_count = 0
        self.done      = False
        self.running   = True

        self._reveal_adjacent(*self.start)
        self.visited.add(self.start)
        self._enqueue_passable_neighbors(*self.start)

        self._refresh()
        self.stat_var.set("Exploring…")
        self._step()

    def _step(self):
        if not self.running: return

        if not self.frontier:
            # Fully explored!
            self.running = False
            self.done    = True
            cells_mapped = len([c for c in self.known if c not in self.obstacles])
            self.stat_var.set(f"✅  Full map complete!")
            self.info_var.set(f"Steps: {self.step_count}  |  "
                              f"Cells mapped: {cells_mapped}")
            return

        # Pop next cell from BFS queue
        next_cell = self.frontier.popleft()
        self.frontier_set.discard(next_cell)

        # If it turned out to be an obstacle (placed after enqueue) — skip
        if next_cell in self.obstacles:
            self.after_id = self.after(1, self._step)
            return

        prev = self.bot_pos
        self.bot_pos = next_cell
        self.step_count += 1

        self.visited.add(next_cell)
        self._reveal_adjacent(*next_cell)
        self._enqueue_passable_neighbors(*next_cell)

        # Repaint affected cells
        if prev: self._paint(*prev)
        self._paint(*next_cell)
        for dr, dc in DIRS + [(0,0)]:
            nr, nc = next_cell[0]+dr, next_cell[1]+dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                self._paint(nr, nc)
        self._redraw_bot()

        self.info_var.set(f"Step: {self.step_count}  |  "
                          f"Frontier: {len(self.frontier)}  |  "
                          f"Mapped: {len(self.visited)}")

        self.after_id = self.after(self.speed_ms.get(), self._step)

    def _toggle_pause(self):
        if self.done: return
        if self.running:
            self.running = False
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
            self.stat_var.set("⏸  Paused. Resume to continue.")
        else:
            if self.bot_pos and not self.done:
                self.running = True
                self.stat_var.set("Exploring…")
                self._step()

    def _reset(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        self.running     = False
        self.done        = False
        self.start       = None
        self.bot_pos     = None
        self.obstacles.clear()
        self.known.clear()
        self.visited.clear()
        self.frontier.clear()
        self.frontier_set.clear()
        self.step_count  = 0
        self.stat_var.set("Place Start, then explore.")
        self.info_var.set("")
        self._draw_base_grid()


if __name__ == "__main__":
    BFSExplorer().mainloop()