<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

session_start();
$user = 'NULL';
if (!empty($_SESSION['user_id'])) {
    $user = $_SESSION['user_id'];
}
$pass_enviada = $_POST['password'];
$new_pass = $_POST['new_pass'];
$new_pass_confirm = $_POST['new_pass_confirm'];

echo "Se ha actualizado el usuario con id: ".$user;
$query = "SELECT contraseña FROM tUsuarios WHERE id=".$user;
$result = mysqli_query($db, $query) or die('Query error');

if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);
    if ($only_row[0] == $pass_enviada) {
        if ($new_pass_confirm == $new_pass) {
            echo "<p>La contraseña nueva es: "."$new_pass_confirm</p>"."<br>";

            $query2 = "UPDATE tUsuarios SET contraseña = '".$new_pass."' where id =".$user;
            $result = mysqli_query($db, $query2) or die('Query error');

            echo '<p>La contraseña se ha visto actualizada</p>';
        } else {
            echo '<p>Las nuevas contraseñas no coinciden</p>';
        }
    } else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}
