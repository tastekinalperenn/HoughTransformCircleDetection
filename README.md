# HoughTransformCircleDetection

#Overview
With this homework, we will learn the Hough Transform method, which is used to detect geometric
shapes such as lines and circles. We will try to detect circles on images using Hough Transform. We
will implement the steps of the algorithm from start to finish. We will compare the circles we detect
with the given ground truth values and test how well the algorithm works. We will draw the circles
that we find with using Hough Transform on the pictures.


#Edge Detection
I used the Canny edge detection method for edge detection. The algorithm basically consists of 5
steps. Since edge detection is sensitive to noise, the image is blurred with Gaussian first. Then the
gradient is calculated and the density and direction of the edges are determined. Thanks to non max
suppression, the width of one edge is reduced, overlapping edges are neglected. Finally, we give the
function a minimum and a maximum threshold value. The function detects the edges between these
threshold values. The optimum threshold values are different for each image. For this reason, two
generally accepted values are determined. For maximum efficiency, each image should be tested
separately. Keeping this gap too wide can increase the program’s run time and allow it to find extra
edges, while making it too narrow can cause the loss of edges to indicate circles.
