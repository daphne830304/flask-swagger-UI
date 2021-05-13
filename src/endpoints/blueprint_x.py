from flask import Blueprint, jsonify, request
import crud.py
import json
blueprint_x = Blueprint(name="blueprint_x", import_name=__name__)
results_dict = json.loads('result.json')
x = 5

@blueprint_x.route('/test', methods=['GET',"POST"])
def test():
    """
    ---
    get:
      description: test endpoint
      parameters:
          - in: query
            name: name
            schema:
              type: string
            description: enter your name
          - in: query
            name: gender
            schema:
              type: string
            description: enter "female" or "male"
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing

          
    """
    name = request.args.get('name')
    gender = request.args.get('gender')
    # constellation = request.args.get('constellation')
    sums = 0
    ascii_list = []
    if name:
        for i in name:
            if i:
                ascii_list.append(ord(i))
            sums += ord(i)

    first = crud.find_first(sums,name,ascii_list,gender)

    output = {"name": name,
              "gender":gender,
              "result":results_dict[first]
              }
    return jsonify(output)
@blueprint_x.route('/test1', methods=['GET'])
def test1():
    """
    ---
    get:
      description: test endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing

          
    """


    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)

@blueprint_x.route('/plus', methods=['POST'])
def plus_x():
    """
    ---
    post:
      description: increments the input by x
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - calculation
    """
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and return as JSON
    result = in_val + x
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)


