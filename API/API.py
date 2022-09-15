from flask import Flask
from flask import request 
from flask import render_template
from rdflib import Graph
from rdflib import URIRef



app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("form.html")

@app.route("/", methods =["GET", "POST"])
def my_form_post():
    #with app.test_request_context():
    if request.method == "POST":
       # getting input with name = word in HTML form
       Word = request.form.get("word")
       node = URIRef("http://fa.dbpedia.org/resource/" + Word) 
       g = Graph()
       g.parse("set4.xml")
       g.parse("set3.xml")
       g.parse("set2.xml")
       g.parse("set1.xml")
       #print(len(g))
       #count = 0
       result = ""
       string_set = {"http://fa.dbpedia.org/property/", "http://purl.org/dc/terms/subject:http://fa.dbpedia.org/resource/",
                     "http://fa.dbpedia.org/property/wikiPageUsesTemplate:http://fa.dbpedia.org/resource/", "http://fa.dbpedia.org/resource/", "http://purl.org/dc/terms/subject",
                     "http://purl.org/dc/terms/subject", "wikiPageUsesTemplate"} 
       for s, p, o in g:
          if(s, p, o) in g.triples((node, None, None)):
              for sample in string_set:
                  if p.find(sample) != -1:
                      p = p.replace(sample, "")
                  if o.find(sample) != -1:
                      o = o.replace(sample, "")
              #count = count + 1
              if o.find(":") != -1 or p.find(":") != -1:
                  result = result + p + o + "<br/>" + "<br/>"
              else:
                  result = result + p + ":" + o + "<br/>" + "<br/>"
       if result == "":
           result = "Noting found!"
       return result
       
     



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)