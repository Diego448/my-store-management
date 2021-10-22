async function getUserDetails(id) {
    return fetch("/user/" + id).then(
        response => response.json()
    ).then(
        responseJSON => {return responseJSON}
    )
}

async function fillUserEditModal(id) {
    let nameInput = document.getElementById("name");
    let modalTitle = document.getElementById("exampleModalLabel");
    let data = await getUserDetails(id);
    modalTitle.innerHTML = "Editar usuario";
    nameInput.value = data["name"];
}

async function addUser() {
    let modalTitle = document.getElementById("exampleModalLabel");
    let nameInput = document.getElementById("name");
    let userInput = document.getElementById("username");
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");
    let privilegesInput = document.getElementById("privileges");

    modalTitle.innerHTML = "Agregar usuario";

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
      }

    return response.json();
}

function resetForm() {
    let modalTitle = document.getElementById("exampleModalLabel");
    let modalForm = document.getElementById("modalForm");
    let nameInput = document.getElementById("name");
    let userInput = document.getElementById("username");
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");
    let privilegesInput = document.getElementById("privileges");

    modalTitle.innerHTML("Agregar usuario");
    modalForm.resetForm();

}