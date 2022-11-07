# HoughTransformCircleDetection

**Overview**
With this homework, we will learn the Hough Transform method, which is used to detect geometric
shapes such as lines and circles. We will try to detect circles on images using Hough Transform. We
will implement the steps of the algorithm from start to finish. We will compare the circles we detect
with the given ground truth values and test how well the algorithm works. We will draw the circles
that we find with using Hough Transform on the pictures.

**Edge Detection**
I used the Canny edge detection method for edge detection. The algorithm basically consists of 5
steps. Since edge detection is sensitive to noise, the image is blurred with Gaussian first. Then the
gradient is calculated and the density and direction of the edges are determined. Thanks to non max
suppression, the width of one edge is reduced, overlapping edges are neglected. Finally, we give the
function a minimum and a maximum threshold value. The function detects the edges between these
threshold values. The optimum threshold values are different for each image. For this reason, two
generally accepted values are determined. For maximum efficiency, each image should be tested
separately. Keeping this gap too wide can increase the program’s run time and allow it to find extra
edges, while making it too narrow can cause the loss of edges to indicate circles.As can be seen in the code, 
although Canny uses Gaussian in itself, it is more useful to blur the picture beforehand.
Maybe some morphological transformations can be done in this part.
After detecting the edge, I convert the picture to matrix format for other operations and return it.


**Hough Transform Implementation**
A circle equation with center (a,b) and radius r in the x-y coordinate plane is expressed as (x-a)^2
+ (y-b)^2 = r^2. Each point (x,y) on the circle indicates a circle with the formula (a-x)^2 +
(b-y)^2 = r^2 in the a-b coordinate plane. What we’re trying to do with the Hough transform is to
find all the points of the corresponding circle in the a-b coordinate plane for each pixel of an image
whose edges we have removed (here we used Canny). When this operation is done for all pixels,
the coordinate where all these circles intersect in the a-b coordinate plane (or the most voted pixel
coordinate) gives us the center of the circle in the x-y plane. We try to find the relevant circles by
repeating this process as many times as the number of circles specified in the ground truth file. In
addition, instead of taking all the points of the circle in the a-b plane, we skip the angle values 5 by 5
for the program to run fast. For this reason, we sometimes miss the points that need the most votes,
and points that are not the center of the circle can be voted too many times. In this case, I choose a
certain number of the most voted points and choose the one closest to the central ground truth value.
We draw the circles determined in the last step on the input picture. We save the output image in the
format Output(inputfilename).jpg.





**Failed Scenarios**
There may be several reasons why the algorithms is not detecting the correct circles. The first of
these concerns the detection of edges. Lost or extra noise details during edge detection may cause the
program to find or not find circles in different places. This problem can be solved by changing the
threshold values entered while detecting edges with Canny. Another problem may be that while there
are points on the circle in the a-b coordinate plane, the angle values are skipped 5 by 5 and some
points are not processed in order for the program to run faster

