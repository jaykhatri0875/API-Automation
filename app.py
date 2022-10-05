# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import git
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


#######################################################
# this is webhook for CD -- do not change

@app.route('/update-server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./API-Automation')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
#######################################################

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):

		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201

# another resource to calculate the square of a number
class Square(Resource):
	def get(self, num):
		return jsonify({'square': num**2})

class cube(Resource):
	def get(self, num):
		return jsonify({'Cube of number': num**3})
class meta(Resource):
	def get(self,num):
		return jsonify({
			'this is number you typed':num
		})

# is this even working fine ?
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(cube,'/cube/<int:num>')
api.add_resource(meta,'/meta/<int:num>') # this was wrong earlier, should be directly parameter name in case of string
# driver function
# i dont think this is required anymore
'''
if __name__ == '__main__':
	app.run(debug = True)
'''
