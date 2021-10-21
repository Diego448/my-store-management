function editUser(id) {
    const response = fetch("/user/" + id).then(
        response => response.json()
    ).then(
        response => console.log(response)
    )
}

function fillUserEditModal(data) {
    let nameInput = document.getElementById("name");
    nameInput.value = data.name;
}
