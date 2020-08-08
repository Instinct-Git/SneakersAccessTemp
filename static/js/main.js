function settingsToggle() {
    let settings = document.getElementById('settings')
    console.log(settings.style.display)
    if (settings.style.display == '' || settings.style.display == 'none')
        settings.style.display = 'block'
    else
        settings.style.display = 'none'
}

/*
document.addEventListener('DOMContentLoaded', function() {

    var url = 'http://127.0.0.1:5001/GUI-is-still-open'; 
    fetch(url, { mode: 'no-cors'});
    setInterval(function(){ fetch(url, { mode: 'no-cors'});}, 5000)();

});
*/