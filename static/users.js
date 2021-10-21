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
