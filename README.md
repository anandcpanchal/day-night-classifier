# day-night-classifier
Simple day-night classifier

Requirement:
python3
opencv2
numpy
matplotlib

Note:
1. Use --debug True to display image and computed hsv average
2. Defualt hsv threshold is randomly set to 100. Use --threshold <value> to modify it.

Usage:
1. Simple
command : python simple_day_night_classifier.py -i <path_to_input_image>
output  : Day image / Night image

2. Advance
command : python simple_day_night_classifier.py -i <path_to_input_image> [ --threshold <threshold_value_for_hsv_avg_brightness> ] [ --debug <True> ]
