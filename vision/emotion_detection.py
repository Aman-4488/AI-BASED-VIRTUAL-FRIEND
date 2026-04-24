import cv2
from deepface import DeepFace
from backend.suggestion_engine import get_suggestion

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    try:
        # Detect emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Get suggestions
        data = get_suggestion(emotion)

        # Display emotion on screen
        cv2.putText(frame, f'Emotion: {emotion}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Print in terminal
        print("\nEmotion:", emotion)
        print("Message:", data["message"])
        print("Suggestions:", data["suggestions"])

    except Exception as e:
        print("Error:", e)

    # Show webcam
    cv2.imshow("AI Virtual Friend - Emotion Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()