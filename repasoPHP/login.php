<?php
$db = mysqli_connect('localhost', 'root', '1234', 'repaso') or die('Fail');

$usuario= $_POST['usuario'];
$password= $_POST['contraseña'];

$query = "SELECT id, contraseña FROM tusuarios WHERE nombre = '" . $usuario . "'";;
$result = mysqli_query($db, $query) or die('Query error');
$passwordHash=password_hash($password,PASSWORD_DEFAULT);

if (password_verify($password, $only_row[1])) {
    session_start();
    $_SESSION['user_id'] = $only_row[0];
    header('Location: main.php');

}else{
    echo '<p>Contraseña no coincide</p>';
}
?>
