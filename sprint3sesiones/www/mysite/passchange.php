 <?php
session_start();

        $email = $_POST['email'];
        $password = $_POST['contraseña'];
        $newpassword = $_POST['newpassword'];
        $confirmnewpassword = $_POST['confirmnewpassword'];
        $result = mysql_query("SELECT contraseña FROM tUsuarios WHERE 
email='$email'");
        if(!$result)
        {
        echo "El usuario que has introducido no existe";
        }
        else if($password!= mysql_result($result, 0))
        {
        echo "Has introducido una contraseña incorrecta";
        }
    else{
        if($newpassword==$confirmnewpassword)
        $sql=mysql_query("UPDATE tUsuarios SET contraseña='$newpassword' where 

 usuario_id='$username'");
        if($sql)
        {
        echo "Felicidades, has cambiado tu contraseña correctamente.";
        }
       else
        {
       echo "Las contraseñas no coinciden";
       }
    }
      ?>
