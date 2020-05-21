docker kill sut1 sut2 sut3 master_container testit_container > /dev/null 2>&1
x-terminal-emulator -e "roslaunch testit_patrol testit_patrol.launch"
sleep 2
rosrun testit testit_command.py bringup
sleep 2
rosrun testit testit_command.py "$1" "$2"
