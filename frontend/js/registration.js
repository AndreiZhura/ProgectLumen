const btn_registration = document.getElementById('btnregistration');


export function handleRegistration() {
    btn_registration.addEventListener('click', () => {
        window.location.href = "../blockPHP/registration.php";
    });
}