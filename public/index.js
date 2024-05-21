function deleteItem(item_id){
  alert(item_id)
}

async function getAll() {
  try {
    const response = await fetch("/Fallou",{
      method:'GET'
    })
    const data = await response.json();
    const items = data.Data
  
    const ulID = document.getElementById("buddy")
    // Create Items

    for (let i = 0; i < items.length; i++) {
      const el = items[i]

      const li = document.createElement("li");
      var x = document.createElement("BUTTON");
      x.addEventListener("click", deleteAll);

 
      
      li.innerHTML = el.name;
      li.append(x)
   
      ulID.append(li);
    
    }
  } catch (error) {
   console.log(error); 
  }
}

async function deleteAll() {
  console.log("deleteAll")
  try {
    const response = await fetch("/Fallou",{
      method:'DELETE'
    })
    const data = await response.json();
    const items = data.Data

    const ulID = document.getElementById("buddy")

    for (let i = 0; i < items.length; i++) {
      const el = items[i]

      const li = document.createElement("li");

      li.innerHTML = el.name;
      ulID.append(li);

    }
  } catch (error) {
   console.log(error); 
  }
}
getAll()
