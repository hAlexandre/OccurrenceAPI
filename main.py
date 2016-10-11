from flask import Flask, request, jsonify
import requests


app = Flask(__name__,  static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/search',  methods=['GET'])
def search():
	if(request.method == 'GET'):
		url =  request.args.get('url')
		palavra = request.args.get('palavra')
		return(crawl(url,palavra))

#tratamento caso não possua http:// na url
def tratarURL(url):
	aux = url	
	match = url.count('http://') + url.count('https://');
	if(match == 0):
		aux = 'http://' + url

	return aux



def crawl(url, palavra):    
	
	url = tratarURL(url)
	
	req = requests.get(url)
	result = []
    
	if(req.status_code != 200):
		return []

	k = req.text.count(palavra)
	return jsonify(numOcorrencias=k)
    

if __name__ == "__main__":
	app.run(debug=True)