window.onload = function() {
    document.getElementById("modalClose").addEventListener("click", (event) => {
        resetForm();
    });
}

async function getUserDetails(id) {
    return fetch("/user/" + id).then(
        response => response.json()
    ).then(
        responseJSON => {return responseJSON}
    )
}

async function fillUserEditModal(id) {
    let nameInput = document.getElementById("name");
    let userInput = document.getElementById("username");
    let emailInput = document.getElementById("email");
    let modalEdit = document.getElementById("modalEdit");
    let modalTitle = document.getElementById("exampleModalLabel");
    let data = await getUserDetails(id);
    modalEdit.removeAttribute("hidden");
    modalTitle.innerHTML = "Editar usuario";
    nameInput.value = data["name"];
    emailInput.value = data["email"];
    userInput.value = data["username"];
}

async function addUser() {
    let modalTitle = document.getElementById("exampleModalLabel");
    let modalSave = document.getElementById("modalSave");
    let nameInput = document.getElementById("name");
    let userInput = document.getElementById("username");
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");
    let privilegesInput = document.getElementById("privileges");

    modalTitle.innerHTML = "Agregar usuario";
    modalSave.removeAttribute("hidden");

    let userData = {
        "name": nameInput.value,
        "username": userInput.value,
        "email": emailInput.value,
        "password": passwordInput.value,
        "privileges": privilegesInput.value
    }

    const response = await fetch("/user/create", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });

      if (response.ok) {
          document.getElementById("modalClose").click();
          resetForm();
      }
    
    return response.json();
}

async function updateUser(id) {
    resetForm();
}

function resetForm() {
    let modalTitle = document.getElementById("exampleModalLabel");
    let modalForm = document.getElementById("modalForm");
    let modalSave = document.getElementById("modalSave");
    let modalEdit = document.getElementById("modalEdit");
    let nameInput = document.getElementById("name");
    let userInput = document.getElementById("username");
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");
    let privilegesInput = document.getElementById("privileges");

    modalTitle.innerHTML = "Agregar usuario";
    modalSave.setAttribute("hidden", "true");
    modalEdit.setAttribute("hidden", "true");
    modalForm.reset();

}

function toggleAdd() {
    resetForm();
    document.getElementById("modalSave").removeAttribute("hidden");
}