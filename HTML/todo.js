let todoList = [
  {item:'Buy Milk', dueDate:'4/10/2023'},
  {item:'Go to College', dueDate:'4/10/2023'}
];
displayItems();

function addTodo(){
  let inputElement = document.querySelector('#todo-input');
  // aap isse use karke kisi bhi chiz ke andar ki chez nikal sakte hain
  let dateElements = document.querySelector('#todo-date');
  let todoItem = inputElement.value; // isse aap andar ki value nikal sakte hain
  let todoDate = dateElements.value;
  todoList.push({item:todoItem, dueDate:todoDate});
  //console.log(todoList);
  inputElement.value = '';
  dateElements.value = '';
  displayItems();
}

function displayItems(){
  let containerElements = document.querySelector('.todo-container');
  // yaha par humne div ke andar ke elements ko access kar liya 
  let newHtml = '';
 // displayElements.innerText = '';
  for(let i =0; i<todoList.length; i++){
    let{item,dueDate} = todoList[i];
    newHtml += `
    <span>${item}</span>
    <span>${dueDate}</span>
    <button class ="btn-delete"onclick="todoList.splice(${i},1); displayItems();">Delete</button>
    `
    //displayElements.innerText = displayElements.innerText + "\n"+ todoList[i];
  }
  containerElements.innerHTML = newHtml; // replacing old HTML with new HTML
}