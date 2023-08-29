# dana-KG
A restful API for persian knowledge graphs

There are several open source knowledge graphs in persian. This project is aimed to first gather these knowledge graphs together and update them to the latest version (if it's needed). Then develop a RESTful API which gets information about given entity and requested predicate.

# References
1. [FarsBase: The Persian Knowledge Graph](https://www.researchgate.net/publication/335964822_FarsBase_The_Persian_Knowledge_Graph)
2. [The Architecture of Farsi Knowledge Graph System](https://jipm.irandoc.ac.ir/article-1-4190-en.html)
3. [FarsBase Knowledge Graph - Github](https://github.com/IUST-DMLab/farsbase-kg)


# Codes
First, you need to clone DBpedia extraction framework : "https://github.com/dbpedia/extraction-framework.git" (if you work in windows, you can use GitBash or googlecolab) after cloning, you need to run the "colab code" file. Also, there are some tips for changing some settings in the framework. the other python codes involve the extracted RDFs (set1 to set4), the html form of the API(in API/templates/form.html), and the python code of the API.
