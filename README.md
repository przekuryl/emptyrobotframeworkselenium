Get webdrivers (like browsers for automated test):
One way is to download them manually and them to PATH
or use webdrivermanager e.g:

pip install webdrivermanager
webdrivermanager firefox chrome --linkpath /usr/local/bin

Requirements:
pip install Requirements/requirements.txt

Run test suite (cmd command):
robot -d ./Results ./TestSuites/TestSuite.robot
