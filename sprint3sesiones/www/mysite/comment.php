<?php
	$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
	<body>
	<?php
		
	session_start();
	$user_id_a_insertar = 'NULL';
	if (!empty($_SESSION['user_id'])) {
	$user_id_a_insertar = $_SESSION['user_id'];
	}
	 $libro_id = $_POST['libro_id'];
	 $comentario = $_POST['new_comment'];

	$query = "INSERT INTO tComentarios (comentario, libro_id, usuario_id, fecha_comentario) values ('".$comentario."',".$libro_id.",".$user_id_a_insertar.",now())";	
	mysqli_query($db, $query) or die ('Error');
	
	echo "<p>Nuevo comentario ";
	echo mysqli_insert_id($db);
	echo " añadido</p>";

	echo "<a href='/detail.php?id=".$libro_id."'>Volver</a>";
	mysqli_close($db);
	?>
	</body>
</html>
