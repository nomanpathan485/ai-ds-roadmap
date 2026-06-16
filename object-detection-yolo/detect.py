from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

results = model.predict(
    "object-detection-yolo/images/manandacar.jpg",
    show=True,
    save=True,
    conf=0.25
)

print("Detection Complete!")
for result in results:
    print(result.boxes)