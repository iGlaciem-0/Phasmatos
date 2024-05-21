from flask import Flask, render_template, request, jsonify


app = Flask(
  __name__ ,
  template_folder='templates', 
  static_folder='public'
)

Sarugami = [{
  "id": 1,
    "name": "Leo",
}]

def find_item_by_id(array, target_id):
  for item in array:
    if item.get("id") == target_id:
      return item
  return None


@app.route('/')
def index():
  return render_template('index.html')

# Get all items
@app.route('/Fallou')
def getall():
  return jsonify(
    {
      "Data": Sarugami 
    }
  )
  

# Get 1 item
@app.route('/<int:item_id>', methods=["GET"])
def item_detail(item_id):
    item = find_item_by_id(Sarugami, item_id)
    if item:
        return render_template('item_detail.html', item=item)
    else:
        return "Item not found", 404
      
# Create an item
@app.route('/Saru', methods=["POST"])
def Espada3():

  label = request.form.get("fname")
  # Get the length of the array then add 1
  X = len(Sarugami)
  X = X + 1
  Cars = {
      "id": X,
      "name": label,
    }
  Sarugami.append(Cars)

  return render_template('index.html', AlternateUniverse = Sarugami)


@app.route('/<int:item_id>', methods=["DELETE"])
def delete_item(item_id):
  print("nnpkokon")
  print(item_id)

# Search array by ID
  # Delete that item
  for i in Sarugami:
    if i["id"] == item_id:
        Sarugami.remove(i)

    return jsonify({
      "message": "Item deleted successfully",
      "items": AlternateUniverse
    }), 200
     

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)