<?php
 $db =mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<html>
<body>
<?php
	if(!isset($_GET['id'])){
		die('No se ha especificado un libro.');
	}
	$libro_id=$_GET['id'];
	$query='SELECT * FROM tLibros where id='.$libro_id;
	$result=mysqli_query($db,$query) or die('Query error');
	$only_row =  mysqli_fetch_array($result);

	echo '<h1>'.$only_row['nombre'].'</h1>';

	echo '<h2><img src="'.$only_row['url_imagen'];
	echo '" width="200" height="200" ></h2>';

	echo '<h2>'.$only_row['anno_publicacion'].'</h2>';

?>
	<h3> Comentarios:</h3>
	<ul>
	<?php
	$query2= 'select * from tComentarios where libro_id='.$libro_id;
	$result2= mysqli_query($db,$query2) or die ('Query error');
	while ($row= mysqli_fetch_array($result2)){
		echo'<li>'.$row['comentario'].'</li>';

	}
	mysqli_close($db);
	?>
	</ul>
	</body>
	</html>
