<?php
  $db = mysqli_connect('172.16.0.2', 'root', '1234', 'repaso') or die('Fail');
$usuario= $_POST['usuario'];
$email=$_POST['email'];
$password=$_POST['password'];
$passwordConfirm=$_POST['passwordConfirm'];

if ($passwordConfirm!=$password) {
    echo '<p>password no valida</p>';
} else {
    $passwordHash=password_hash($password,PASSWORD_DEFAULT);
    $query = $mysqli->prepare ("insert into usuarios values (?,?,?)");
    $query->bind_param("sss",$usuario,$email,$passwordHash); 
    $query->execute();
    $query->close();
    header('Location: login.php');

}
