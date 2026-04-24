from pipeline.image_loader import load_image
from pipeline.object_extractor import detect_objects
from pipeline.face_extractor import detect_faces
from pipeline.scene_describer import describe_scene

def analyze_image(image_path: str):
    image = load_image(image_path)
    objects = detect_objects(image)
    faces = detect_faces(image)
    description = describe_scene(image)

    result = {
        "objects": objects,
        "faces": faces,
        "scene_description": description
    }

    return result