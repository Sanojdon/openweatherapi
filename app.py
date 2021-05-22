from flask import Flask, render_template, request
import wrapper
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/collect")
def api_collect():
	result = model.view_city()
	for city in result:
		data = wrapper.get_api_data(city.ct_latitude, city.ct_longitude)
		model.add_city_records(city.ct_name, data["timezone"], data["current"]["dt"], \
			data["current"]["sunrise"], data["current"]["sunset"], data["current"]["temp"],\
			data["current"]["feels_like"], data["current"]["pressure"], data["current"]["humidity"], data["current"]["weather"][0]["main"],\
			data["current"]["weather"][0]["description"])
	return render_template("api_collect.html", cities=result)

@app.route("/api/similar")
def api_similar():
	return render_template("api_similar.html")

@app.route("/addcity", methods=["POST","GET"])
def add_city():
	if request.method == "POST":
		result = request.form
		model.add_city(result["txt_city"], float(result["txt_lat"]), float(result["txt_lon"]))
		return render_template("index.html")
	return render_template("add_city.html")

if __name__ == "__main__":
	app.run()