# zipline-test

Before running, make sure that you have Python 3.6+ and node 18.x or later installed.

To run locally:

1. Go to the root project and open up 2 termianl windows
2. In the first one, create a virtual Python environment by running the following commands:
```
python3 -m venv .venv
 . .venv/bin/activate
```
3. On that same terminal, with the virutal environment activated, install the dependecies by running the following command:
```
pip install -r requirements.txt
```
4. The last step on the first terminal is to run the following command:
```
flask --app dagData run
```
5. In the second terminal, run `npm install` and then the following command:
```
 http-server -p 8080
 ```
 6. Go to http://localhost:8080/hello to see the app
