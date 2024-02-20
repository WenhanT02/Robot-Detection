import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("Untitled video.mp4")

# Read frame1 of the video, ret boolean make sure the read is "True" (successfully)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
center_point = []

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate the time threshold
time_threshold = 40  # 40sec
frame_threshold = int(time_threshold * fps)
frame_count = 0

# Create a new figure for plotting circles
plt.figure()
plt.ion()
circle_plot = plt.gca()
plt.title('Detected Motion Centers')

while cap.isOpened():  # check if the video is open with "ret", if not "True" stop
    if not ret:
        break

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = None
    max_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area < 2500:
            continue

        if area > max_area:  # Detect only one object per frame
            max_area = area
            largest_contour = contour
            if largest_contour is not None:  # No use, but if works
                (x, y, w, h) = cv2.boundingRect(largest_contour)  # Calculate center point
                # print("w:", w, "h:", h)

                if frame_count <= frame_threshold:  # for the first 40sec of the video do this
                    # print('frame_count',frame_count, "frame_threshold", frame_threshold)

                    if (w / h) <= 1.0 / 1.63:  # If detect the shadow then modify the center location of the robot
                        cx = int(x + w / 2)
                        cy = int(y + h * (2 / 3))
                        # print('2/3')
                    else:  # else just put in the center
                        cx = int(x + w / 2)
                        cy = int(y + h / 2)
                        # print('Normal')
                else:
                    cx = int(x + w / 2)
                    cy = int(y + h / 2)

                center_point.append((cx, cy))

                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle on frame1, reference top left point, bottom right point, green rectangle, 2 thickness
                cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)  # add text

    # Display the frame with rectangle in OpenCV window
    cv2.imshow("feed", frame1)

    # Plot circles in the separate graph window
    circle_plot.clear()
    circle_plot.set_aspect('equal', adjustable='box')
    circle_plot.set_xlim(0, frame1.shape[1])
    circle_plot.set_ylim(0, frame1.shape[0])
    for pt in center_point:
        circle_plot.add_patch(plt.Circle((pt[0], pt[1]), 2, color='r'))
    plt.draw()
    plt.pause(0.001)

    frame1 = frame2
    ret, frame2 = cap.read()
    frame_count += 1

    if cv2.waitKey(40) & 0xFF == 27:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
