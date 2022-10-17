Install pip, python - just google it :-)

Install Requirements:
pip install -r Requirements/requirements.txt

Add your robotframework project into environmental variables:
Go to environment variables > if there is no PYTHONPATH variable, add it. 
Inside PYTHONPATH, add path to your project repository.

Run test suite (cmd command):
robot -d ./Results ./TestSuites/GoogleSearchSuite.robot
