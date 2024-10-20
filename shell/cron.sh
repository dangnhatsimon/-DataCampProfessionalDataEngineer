# Verify that there are no CRON jobs currently scheduled
crontab -l 

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file 
cat hello_world.py

# Add as job that runs every minute on the minute to crontab
echo "* * * * * python hello_world.py" | crontab

# Verify that the CRON job has been added
crontab -l





# Preview both Python script and requirements text file
cat create_model.py
cat requirements.txt

# Pip install Python dependencies in requirements file
pip install -r requirements.txt

# Run Python script on command line
python create_model.py

# Add CRON job that runs create_model.py every minute
echo "* * * * * python create_model.py" | crontab

# Verify that the CRON job has been scheduled via CRONTAB
crontab -l