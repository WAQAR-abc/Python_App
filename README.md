# Python_App
This is a simple python app using flask. It runs on port 5000.

**To run this app without Docker, make sure you have python installed then run the following commands:**
> pip install -r requirements.txt

> python app.py

**To run this app with Docker, run the following commands:**
> docker image build -t python_app .

> docker run -d -p 5000:5000 python_app

This will run the app inside container and map's the port 5000 of container with system's port 5000.

Now you can access the app on both <u>http://containerIP:5000</u> & <u>http://systemIP:5000</u>

Also you can see the logs of container to see app logs:
> docker logs containerID

If you want to continously see the logs of container then do:
> watch docker logs containerID
