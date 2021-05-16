from flask import Flask
from app import views
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # this is for cache

app.add_url_rule('/','index',views.index)
app.add_url_rule('/fruits360','fruits360',views.fruits360)
app.add_url_rule('/fruitsyolov3','fruityolov3',views.fruitsyolov3)
app.add_url_rule('/testyolov3','testyolov3',views.testyolov3)
app.add_url_rule('/detect','detect',views.mask_image, methods=['POST'])
#server.add_url_rule('/test','test',views.test, methods=['GET','POST'])

	
#@server.after_request
#def after_request(response):
#    print("log: setting cors" , file = sys.stderr)
#    response.headers.add('Access-Control-Allow-Origin', '*')
#    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#    return response



if __name__ == "__main__":
    app.run(debug=True)
