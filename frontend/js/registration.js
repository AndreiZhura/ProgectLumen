export function handleRegistration() {
    const btn_registration = document.getElementById('btnregistration');

    if (btn_registration) {
        btn_registration.addEventListener('click', () => {
            window.location.href = "../blockPHP/registration.php";
        });
    } else {
        console.warn("Кнопка #btnregistration не найдена");
    }
}