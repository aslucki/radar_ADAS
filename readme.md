# Radar demo
Sample usage of a [Grove Doppler Radar](https://wiki.seeedstudio.com/Grove-Doppler-Radar/) showing a basic ADAS utility - the radar warns about objects approaching towards ego vehicle. 

It's for a demo purpose only, it would require more work or possible different radar to become a practical solution for this use case. 

Supports only Python3

## Installation
1. Clone repo to your catkin workspace
2. From the repo's main directory run:  
   `pip3 install ./src/lib/grove-doppler-radar`
   
3. Navigate to your catkin workspace and run:  
`catkin_make`
   
## Usage
1. Start ros master.

2. Execute the script:
`python3 ./src/radar_adas_demo.py`
   
The node will publish to /cmd_vel topic. It will stop the vehicle for a few seconds when the radar detects objects approaching with a given speed.

## Other
1. Robot used for the testing: https://github.com/tooploox/autonomous_car_model
2. Radar library: https://github.com/tooploox/grove-doppler-radar