export function handleLogin(){
    const btn_login = document.getElementById('btnlogin')
    btn_login.addEventListener("click",()=>{
         window.location.href = "../blockPHP/login.php"
    })
}