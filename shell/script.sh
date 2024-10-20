# in one step, create a new file and pass the print function into the file
echo "print('This is my first Python script')" >> my_first_python_script.py

# check file location 
ls

# check file content 
cat my_first_python_script.py

# execute Python script file directly from command line  
python my_first_python_script.py



# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt

# Install the required dependencies
pip install -r requirements.txt

# Verify that Scikit-Learn is now installed
pip list




# Re-install requirements
pip install -r requirements.txt

# Preview Python model script for import dependencies
cat create_model.py

# Verify that dependencies are installed
pip list

# Execute Python model script, which outputs a pkl file
python create_model.py

# Verify that the model.pkl file has been created 
ls

