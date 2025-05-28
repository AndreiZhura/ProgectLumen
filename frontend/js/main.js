import {handleRegistration} from './registration';
import { handleLogin } from './login';

document.addEventListener('DOMContentLoaded', () => {
    handleRegistration();
    handleLogin();
});