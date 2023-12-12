function showCustomAlert() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('custom-alert').style.display = 'block';
}

function closeCustomAlert(url) {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('custom-alert').style.display = 'none';
    window.location.href = url;

}

function createNewDatabase() {
    showCustomAlert()
}
