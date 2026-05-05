import os
import time
import json
from flask import Flask, request, jsonify, send_from_directory, render_template_string

app = Flask(__name__)

# Directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
INFERENCE_FOLDER = os.path.join(BASE_DIR, "inference")
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INFERENCE_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise Vision Platform</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-body: #f1f5f9;
            --bg-card: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --primary: #0284c7;
            --primary-hover: #0369a1;
            --danger: #ef4444;
            --success: #10b981;
            --border: #e2e8f0;
            --sidebar-bg: #ffffff;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }

        body { background-color: var(--bg-body); color: var(--text-main); height: 100vh; overflow: hidden; display: flex; }

        /* Login Screen */
        #login-screen {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            display: flex; justify-content: center; align-items: center; z-index: 1000;
        }

        .login-card {
            background: var(--bg-card); padding: 2.5rem; border-radius: 12px;
            box-shadow: var(--shadow-lg); width: 100%; max-width: 400px;
            text-align: center; border: 1px solid var(--border);
        }

        .login-card h2 { margin-bottom: 0.5rem; color: var(--text-main); font-weight: 600; }
        .login-card p { color: var(--text-muted); margin-bottom: 2rem; font-size: 0.9rem; }
        
        .input-group { margin-bottom: 1.2rem; text-align: left; }
        .input-group label { display: block; font-size: 0.85rem; font-weight: 500; color: var(--text-muted); margin-bottom: 0.4rem; }
        .input-group input { 
            width: 100%; padding: 0.75rem 1rem; border: 1px solid var(--border); border-radius: 6px; 
            font-size: 1rem; color: var(--text-main); outline: none; transition: border-color 0.2s;
        }
        .input-group input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.1); }
        
        .btn { 
            width: 100%; padding: 0.8rem; background: var(--primary); color: #fff; border: none; 
            border-radius: 6px; font-weight: 600; font-size: 1rem; cursor: pointer; transition: background 0.2s;
        }
        .btn:hover { background: var(--primary-hover); }
        .login-error { color: var(--danger); font-size: 0.85rem; margin-top: 1rem; display: none; }

        /* App Layout */
        #app-screen { display: none; width: 100%; height: 100%; flex-direction: row; }

        /* Sidebar */
        .sidebar {
            width: 260px; background: var(--sidebar-bg); border-right: 1px solid var(--border);
            display: flex; flex-direction: column; z-index: 10;
        }

        .brand {
            padding: 1.5rem; border-bottom: 1px solid var(--border);
            display: flex; align-items: center; gap: 0.75rem; font-weight: 700; font-size: 1.2rem; color: var(--primary);
        }

        .nav-menu { padding: 1.5rem 0; flex: 1; }
        .nav-item {
            padding: 0.8rem 1.5rem; display: flex; align-items: center; gap: 1rem;
            color: var(--text-muted); font-weight: 500; cursor: pointer; transition: all 0.2s;
            border-left: 3px solid transparent;
        }
        .nav-item:hover { background: #f8fafc; color: var(--primary); }
        .nav-item.active { background: #f0f9ff; color: var(--primary); border-left-color: var(--primary); }
        .nav-item svg { width: 20px; height: 20px; }

        .sidebar-footer { padding: 1.5rem; border-top: 1px solid var(--border); font-size: 0.85rem; color: var(--text-muted); display: flex; align-items: center; gap: 0.5rem; cursor: pointer;}
        .sidebar-footer:hover { color: var(--danger); }

        /* Main Content */
        .main-wrapper { flex: 1; display: flex; flex-direction: column; overflow: hidden; background: var(--bg-body); }
        
        .topbar {
            height: 70px; background: var(--bg-card); border-bottom: 1px solid var(--border);
            display: flex; align-items: center; justify-content: space-between; padding: 0 2rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }
        .page-title { font-size: 1.25rem; font-weight: 600; }
        .user-info { display: flex; align-items: center; gap: 1rem; font-size: 0.9rem; font-weight: 500; }
        .avatar { width: 36px; height: 36px; border-radius: 50%; background: var(--primary); color: white; display: flex; justify-content: center; align-items: center; font-weight: 600; }

        .content { padding: 2rem; flex: 1; overflow-y: auto; }

        /* Views */
        .view-section { display: none; animation: fadeIn 0.3s ease; }
        .view-section.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Dashboard Overview */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
        .stat-card {
            background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px;
            padding: 1.5rem; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 0.5rem;
        }
        .stat-header { display: flex; justify-content: space-between; align-items: center; color: var(--text-muted); font-size: 0.9rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;}
        .stat-value { font-size: 2rem; font-weight: 700; color: var(--text-main); }
        
        /* Live View */
        .live-container { display: flex; gap: 1.5rem; height: calc(100vh - 180px); }
        .video-panel { flex: 2; background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; box-shadow: var(--shadow); display: flex; flex-direction: column; overflow: hidden; }
        .panel-header { padding: 1rem 1.5rem; border-bottom: 1px solid var(--border); font-weight: 600; display: flex; justify-content: space-between; align-items: center; }
        .video-feed { flex: 1; background: #e2e8f0; display: flex; justify-content: center; align-items: center; position: relative; overflow: hidden; }
        
        /* Vibrating Bounding Box */
        .bounding-box {
            position: absolute;
            border: 3px solid var(--danger);
            background: rgba(239, 68, 68, 0.15);
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.8), inset 0 0 15px rgba(239, 68, 68, 0.5);
            animation: vibrateBox 0.15s linear infinite both;
            pointer-events: none;
            z-index: 10;
        }
        @keyframes vibrateBox {
            0% { transform: translate(0) }
            20% { transform: translate(-2px, 2px) }
            40% { transform: translate(-2px, -2px) }
            60% { transform: translate(2px, 2px) }
            80% { transform: translate(2px, -2px) }
            100% { transform: translate(0) }
        }

        .status-panel { flex: 1; display: flex; flex-direction: column; gap: 1.5rem; }
        .status-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; padding: 1.5rem; box-shadow: var(--shadow); }
        .status-indicator { 
            display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; 
            border-radius: 50px; font-weight: 600; font-size: 0.9rem; margin-top: 1rem;
            transition: all 0.3s ease;
        }
        .status-safe { background: #d1fae5; color: #047857; border: 1px solid #10b981; }
        .status-alert { background: #fee2e2; color: #b91c1c; border: 1px solid #ef4444; animation: pulseRed 2s infinite; }
        @keyframes pulseRed { 0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); } 70% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); } 100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); } }

        /* Logs Table */
        .table-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; box-shadow: var(--shadow); overflow: hidden; }
        table { width: 100%; border-collapse: collapse; }
        th { background: #f8fafc; padding: 1rem 1.5rem; text-align: left; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); border-bottom: 1px solid var(--border); text-transform: uppercase; }
        td { padding: 1rem 1.5rem; border-bottom: 1px solid var(--border); font-size: 0.9rem; }
        tbody tr:hover { background: #f8fafc; }
        
        .badge { padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem; font-weight: 600; }
        .badge-red { background: #fee2e2; color: #b91c1c; }
        .badge-blue { background: #e0f2fe; color: #0369a1; }

    </style>
</head>
<body>

    <!-- Login Screen -->
    <div id="login-screen">
        <div class="login-card">
            <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            </div>
            <h2>Admin Portal</h2>
            <p>Sign in to access the Enterprise Vision IoT Platform</p>
            
            <div class="input-group">
                <label>Administrator ID</label>
                <input type="text" id="username" placeholder="Enter 'admin'">
            </div>
            <div class="input-group">
                <label>Security Key</label>
                <input type="password" id="password" placeholder="Enter 'admin'">
            </div>
            <button class="btn" onclick="attemptLogin()">Secure Login</button>
            <div class="login-error" id="loginError">Invalid credentials. Access Denied.</div>
        </div>
    </div>

    <!-- App Screen -->
    <div id="app-screen">
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="brand">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                Vision IoT
            </div>
            <div class="nav-menu">
                <div class="nav-item active" onclick="switchTab('dashboard', event)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>
                    Overview
                </div>
                <div class="nav-item" onclick="switchTab('live', event)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                    Live Camera Feed
                </div>
                <div class="nav-item" onclick="switchTab('logs', event)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
                    System Logs
                </div>
            </div>
            <div class="sidebar-footer" onclick="logout()">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                Sign Out Admin
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-wrapper">
            <div class="topbar">
                <div class="page-title" id="topbar-title">Dashboard Overview</div>
                <div class="user-info">
                    <div id="sys-time" style="color: var(--text-muted); font-variant-numeric: tabular-nums;">--:--:--</div>
                    <div class="avatar">A</div>
                    <div>Administrator</div>
                </div>
            </div>

            <div class="content">
                
                <!-- Dashboard Tab -->
                <div id="tab-dashboard" class="view-section active">
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-header">
                                Processed Frames
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                            </div>
                            <div class="stat-value" id="dash-total-img">0</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-header">
                                Security Alerts
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--danger)" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                            </div>
                            <div class="stat-value" id="dash-total-alerts">0</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-header">
                                System Status
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--success)" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                            </div>
                            <div class="stat-value" style="color: var(--success); font-size: 1.5rem; margin-top: 8px;">Online & Active</div>
                        </div>
                    </div>
                    
                    <div class="table-card" style="padding: 1.5rem; min-height: 200px;">
                        <h3 style="margin-bottom: 1rem; font-size: 1rem; color: var(--text-muted);">Real-Time Operational Graph</h3>
                        <div style="width: 100%; height: 100px; background: linear-gradient(to right, #f8fafc, #f1f5f9); border-radius: 6px; border: 1px dashed var(--border); display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 0.9rem;">
                            [ Activity Chart Placeholder - Active Monitoring ]
                        </div>
                    </div>
                </div>

                <!-- Live Camera Tab -->
                <div id="tab-live" class="view-section">
                    <div class="live-container">
                        <div class="video-panel">
                            <div class="panel-header">
                                Main Gate ESP32-CAM (Node 01)
                                <span class="badge badge-blue">YOLOv11 Edge</span>
                            </div>
                            <div class="video-feed" id="video-feed-container">
                                <div style="color: var(--text-muted); display: flex; flex-direction: column; align-items: center; gap: 10px;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 16v1a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h2m5.66 0H14a2 2 0 0 1 2 2v3.34l1 1L23 7v10"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
                                    Awaiting Video Signal...
                                </div>
                            </div>
                        </div>
                        <div class="status-panel">
                            <div class="status-card">
                                <h3 style="font-size: 1.1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.8rem; margin-bottom: 1rem;">Threat Detection Status</h3>
                                <p style="color: var(--text-muted); font-size: 0.9rem;">Real-time analysis from restricted zones.</p>
                                
                                <div id="detection-status" class="status-indicator status-safe">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                                    ZONE SECURE - NO PERSON DETECTED
                                </div>
                            </div>
                            
                            <div class="status-card" style="flex: 1;">
                                <h3 style="font-size: 1.1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.8rem; margin-bottom: 1rem;">Node Information</h3>
                                <div style="font-size: 0.9rem; display: flex; flex-direction: column; gap: 0.8rem;">
                                    <div style="display: flex; justify-content: space-between;">
                                        <span style="color: var(--text-muted)">Location:</span> <b>Main Gate Alpha</b>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;">
                                        <span style="color: var(--text-muted)">Network:</span> <b>Connected (WLAN)</b>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;">
                                        <span style="color: var(--text-muted)">Model:</span> <b>YOLOv11n</b>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;">
                                        <span style="color: var(--text-muted)">Current File:</span> <b id="live-filename">N/A</b>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Logs Tab -->
                <div id="tab-logs" class="view-section">
                    <div class="table-card">
                        <table>
                            <thead>
                                <tr>
                                    <th style="width: 200px;">Timestamp</th>
                                    <th style="width: 150px;">Severity</th>
                                    <th>Event Description</th>
                                    <th style="width: 100px;">Node</th>
                                </tr>
                            </thead>
                            <tbody id="logs-table-body">
                                <tr><td colspan="4" style="text-align: center; color: var(--text-muted);">No logs available.</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <script>
        let pollInterval;

        // Authentication
        function attemptLogin() {
            const u = document.getElementById('username').value;
            const p = document.getElementById('password').value;
            if (u === 'admin' && p === 'admin') {
                document.getElementById('login-screen').style.display = 'none';
                document.getElementById('app-screen').style.display = 'flex';
                // Start polling data
                pollInterval = setInterval(fetchData, 1000);
                fetchData();
            } else {
                document.getElementById('loginError').style.display = 'block';
            }
        }

        // Allow Enter key to login
        document.getElementById('password').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') attemptLogin();
        });

        function logout() {
            document.getElementById('app-screen').style.display = 'none';
            document.getElementById('login-screen').style.display = 'flex';
            document.getElementById('password').value = '';
            document.getElementById('loginError').style.display = 'none';
            clearInterval(pollInterval);
        }

        // Navigation
        function switchTab(tabId, event) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.getElementById('tab-' + tabId).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            if(event) event.currentTarget.classList.add('active');

            const titles = {
                'dashboard': 'Dashboard Overview',
                'live': 'Live Camera Feed',
                'logs': 'System Security Logs'
            };
            document.getElementById('topbar-title').innerText = titles[tabId];
        }

        // Clock
        setInterval(() => {
            const now = new Date();
            document.getElementById('sys-time').innerText = now.toLocaleTimeString();
        }, 1000);

        // Data Fetching
        let lastImage = null;

        async function fetchData() {
            try {
                const res = await fetch('/api/data');
                const data = await res.json();

                // Update Overview Stats
                document.getElementById('dash-total-img').innerText = data.total_images.toLocaleString();
                document.getElementById('dash-total-alerts').innerText = data.total_alerts.toLocaleString();

                // Update Camera Feed & Vibrating Box
                if (data.latest_image && data.latest_image !== lastImage) {
                    const container = document.getElementById('video-feed-container');
                    
                    let boxesHtml = '';
                    if (data.inference_meta && data.inference_meta.boxes && data.inference_meta.image === data.latest_image) {
                        const imgWidth = data.inference_meta.width;
                        const imgHeight = data.inference_meta.height;
                        
                        data.inference_meta.boxes.forEach(box => {
                            const left = (box.x1 / imgWidth) * 100;
                            const top = (box.y1 / imgHeight) * 100;
                            const width = ((box.x2 - box.x1) / imgWidth) * 100;
                            const height = ((box.y2 - box.y1) / imgHeight) * 100;
                            
                            boxesHtml += `<div class="bounding-box" style="left: ${left}%; top: ${top}%; width: ${width}%; height: ${height}%;"></div>`;
                        });
                    }
                    
                    container.innerHTML = `
                        <div style="position: relative; display: inline-block; max-width: 100%; max-height: 100%;">
                            <img src="/inference/${data.latest_image}?ts=${Date.now()}" alt="Live Feed" style="max-width:100%; max-height:100%; object-fit:contain; display: block;">
                            ${boxesHtml}
                        </div>
                    `;
                    document.getElementById('live-filename').innerText = data.latest_image;
                    lastImage = data.latest_image;
                }

                // Update Detection Indicator
                const statusEl = document.getElementById('detection-status');
                if (data.person_detected) {
                    statusEl.className = 'status-indicator status-alert';
                    statusEl.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg> ALERT: PERSON DETECTED IN ZONE`;
                } else {
                    statusEl.className = 'status-indicator status-safe';
                    statusEl.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> ZONE SECURE - NO PERSON DETECTED`;
                }

                // Update Logs
                if (data.logs && data.logs.length > 0) {
                    const tbody = document.getElementById('logs-table-body');
                    let html = '';
                    
                    data.logs.slice(0, 15).forEach(logStr => {
                        const isAlert = logStr.includes('[ALERT]');
                        const severity = isAlert ? '<span class="badge badge-red">CRITICAL</span>' : '<span class="badge badge-blue">INFO</span>';
                        
                        const timeMatch = logStr.match(/at (.*)$/);
                        const timeStr = timeMatch ? timeMatch[1] : new Date().toLocaleTimeString();
                        
                        html += `<tr>
                            <td style="color: var(--text-muted); font-family: monospace;">${timeStr}</td>
                            <td>${severity}</td>
                            <td style="font-weight: 500;">${logStr.replace(/at .*$/, '')}</td>
                            <td>Node-01</td>
                        </tr>`;
                    });
                    
                    if (tbody.children.length !== Math.min(data.logs.length, 15) || !tbody.innerHTML.includes(html.substring(0, 50))) {
                        tbody.innerHTML = html;
                    }
                }

            } catch (err) {
                console.error("Data fetch error", err);
            }
        }
    </script>
</body>
</html>
"""

# --- ROUTES ---

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/upload", methods=["POST"])
def upload():
    img_bytes = request.data
    ts = int(time.time())
    filename = os.path.join(UPLOAD_FOLDER, f"cam_{ts}.jpg")
    with open(filename, "wb") as f:
        f.write(img_bytes)
    return "OK\n"

@app.route("/api/data")
def get_data():
    images = []
    if os.path.exists(INFERENCE_FOLDER):
        images = [f for f in os.listdir(INFERENCE_FOLDER) if f.endswith(".jpg")]
        images.sort(key=lambda x: os.path.getmtime(os.path.join(INFERENCE_FOLDER, x)), reverse=True)
    
    latest_image = images[0] if images else None
    
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    
    logs = [log.strip() for log in logs if log.strip()]
    recent_logs = logs[-50:]
    recent_logs.reverse()

    person_detected = False
    if os.path.exists(LOG_FILE):
        mtime = os.path.getmtime(LOG_FILE)
        if time.time() - mtime < 5:
            person_detected = True

    # Read inference metadata for drawing vibrating bounding boxes
    inference_meta = {}
    json_path = os.path.join(BASE_DIR, "latest_inference.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r") as jf:
                inference_meta = json.load(jf)
        except:
            pass

    return jsonify({
        "latest_image": latest_image,
        "total_images": len(images),
        "total_alerts": len(logs),
        "logs": recent_logs,
        "person_detected": person_detected,
        "inference_meta": inference_meta
    })

@app.route("/inference/<path:filename>")
def get_inference_image(filename):
    return send_from_directory(INFERENCE_FOLDER, filename)

if __name__ == "__main__":
    print("Starting Enterprise IoT Master Server on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=False)
