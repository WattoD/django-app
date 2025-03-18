document.addEventListener('DOMContentLoaded', function() {
    const languageNameInput = document.querySelector('#id_name');
    if (languageNameInput) {
        languageNameInput.addEventListener('input', function () {
            const value = languageNameInput.value;
            const regex = /^[a-zA-Zа-яА-ЯёЁ\s]*$/;
            if (!regex.test(value)) {
                alert('Назва мови може складатися лише з літер!');
                languageNameInput.value = value.slice(0, -1);
            }
        });
    }
});