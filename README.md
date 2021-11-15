# Automated-Result-Scanner
An automated program which surveys the University result page every 5mins and alerts the user when the Examination grades are released.<br/><br/>
Used selenium to automate accessing and viewing the results page with a given student's registration number.
<br/><br/>
Scanned the home page and entered the relevant details to open the Examination grades page and capture an image of the image.
<br/><br/>
Compared the captured image with the original Examination grades page(which does not have the grades released). Calculated the difference in similarity between both images and determined whether the Grades were released. Did this process of comparison using OpenCV Tesseract.
<br/><br/>
If the program determine the grades were available it would ring an alarm to notify the user, if the grades were unavailable it would check again after a certain period of time
