let modal = document.getElementById("MyModal");
let flex = document.getElementById("flex");
let abrir = document.getElementById("agg-poster");
let cerrar = document.getElementById("close");

abrir.addEventListener("click", function () {
    modal.style.display = "block";
});

cerrar.addEventListener("click", function () {
    modal.style.display = "none";
});

window.addEventListener("click", function (e) {
    if (e.target == flex) {
        modal.style.display = "none";
    }
});

$("#upload").click(function () {
    $("#add-img").click();
});

$("#add-img").change(function () {
    var files = this.files;
    var supportedImg = ["image/png", "image/jpg", "image/jpeg"];
    var element_not_validos = false;
    if (supportedImg.indexOf(files[0].type) != -1) {
        createPreview(files[0]);
    } else {
        element_not_validos = true;
    }
});

function createPreview(element) {
    document
        .getElementById("photo")
        .setAttribute("src", URL.createObjectURL(element));
}

function modalClick(id, descripccion, direccion, imagen) {
    let ModalEdit = document.getElementById("MyModalEdit");
    let flexEdit = document.getElementById("flexEdit");
    let cerrar = document.getElementById("closeEdit");

    $("#idEdit").val(id);
    $("#direccionEdit").val(direccion);
    $("#descripcionEdit").val(descripccion);
    $("#photoEdit").attr("src", imagen);

    ModalEdit.style.display = "block";

    cerrar.addEventListener("click", function () {
        ModalEdit.style.display = "none";
    });

    window.addEventListener("click", function (e) {
        if (e.target == flexEdit) {
            ModalEdit.style.display = "none";
        }
    });
}
