<?php
	$db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<html>
<head>
<style>
table,td,th{
	border-style:solid;
	border-width10px;
	border-color:black;
}
td{
	text-align:center;
}
</style>
</head>

<body bgcolor="#EEFDEF">
<h1> Conexión establecida</h1>
<?php
	//Lanzar una query
	$query = 'SELECT * FROM tLibros';
	$result = mysqli_query($db,$query) or die ('Query error');
	//Recorrer el resultado

	echo'<table>
	
	<tr>
	<th> ID</th>
	<th> Nombre </th>
	<th> Portada </th>	
	<th> Año de publicación </th>
	</tr>';

	while ($row =mysqli_fetch_array($result)) {
	//tr td
	echo '<tr>';

	echo '<td><a href="/detail.php?id='.$row[0];
	echo '">'.$row[0].'</a></td>';

	echo '<td>'.$row[1].'</td>';

	echo '<td> <img src="'.$row[2];
	echo '"width="200" height="200" >';
	echo '</td>';

	echo '<td>'.$row[3].'</td>';

	echo '</tr>';
	}
	echo "</table>";

	mysqli_close($db);
?>
</body>
</html>
