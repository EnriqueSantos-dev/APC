var botao_menu = document.getElementById('botao')
        botao_menu.addEventListener('click', toggle_botao)


function toggle_botao() {
    var nav = document.getElementById('navegacao')
        nav.classList.toggle('active');
}
