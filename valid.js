window.addEventListener("load", init);

function init() {
    //validateForm();
}

function validateForm() {
    let x = document.validTeszt.kNev.value;
    if (x === "") {
        alert("A mező kitöltése kötelező!");
        return false;
    }

    let y = document.validTeszt.jelszo1.value;
    let z = document.validTeszt.jelszo2.value;
    if (y != z) {
        //document.validTeszt.jelszo2.focus();
        alert("Nem egyforma a két jelszó!");       
        return false;
       
    }
}
