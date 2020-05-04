async function set_word() {

    var word = document.getElementById("new_word").value

    eel.set_word(word)

    var get_word = document.getElementById("form_word")
    get_word.style.display = "none"

    guess_ui = document.getElementById("game")
    guess_ui.style.display = "flex"

    hint_word = document.getElementById("hint_word")
    eel.get_hidden_word()(set_hint)

}

function hide_guess() {

    guess_ui = document.getElementById("game")
    guess_ui.style.display = "none"

}

function set_hint(x) {
    hint_word.innerHTML = x
}