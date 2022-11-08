<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
session_start();
$user = 'NULL';
if (!empty($_SESSION['user_id'])) {
	echo '"<a href="/login.php">' . "Login</a>";
} else {
	echo "<h1> Estás logueado </h1>";
}
?>
<html>

<head>
	<style>
		table,
		th {
			border-style: solid;
			border-width: 10px;
			border-color: black;
		}

		td {
			border-style: solid;
			border-width: 10px;
			border-color: black;
			padding: 15px;
			text-align: center;
		}

		img {
			width: 100px;
			height: 200px;
		}

		img:hover {
			width: 95%;
			height: 400px;
			margin: 0 auto;
		}

		.cor:hover {
			width: 20%;
			height: 50px;
			background-color: blue;
		}

		h1:hover {
			width: 100%;
			height: 50px;

			margin: 0 auto;
			text-align: center;
			background: red;
		}

		.tr1:hover {
			background: green;
		}
	</style>
</head>

<body bgcolor="#EEFDEF">
	<a href="/logout.php">Logout</a>
	<a href="/passchange.html">Cambiar su contraseña</a>
	<form action="search.php" method="$_GET">
		<input type="text" name="search" placeholder="Texto de búsqueda">
		<input type=submit>
	</form>
	<?php
    $search = $_GET['search'];
	$query = 'SELECT * FROM tLibros where nombre like "%'.$search.'%" or anno_publicacion like "%'.$search.'%" ';
	$result = mysqli_query($db, $query) or die('Query error');
	//Recorrer el resultado

	echo '<table>
	
	<tr>
	<th class="cor" > ID</th>
	<th class="cor"> Nombre </th>
	<th class="cor"> Portada </th>	
	<th class="cor"> Año de publicación </th>
	</tr>';

	while ($row = mysqli_fetch_array($result)) {
		//tr td
		echo '<tr>';

		echo '<td class="cor"><a href="/detail.php?id=' . $row[0];
		echo '">' . $row[0] . '</a></td>';

		echo '<td class="cor">' . $row[1] . '</td>';

		echo '<td> <img src="' . $row[2];
		echo '"width="200" height="200" >';
		echo '</td>';

		echo '<td class="cor" >' . $row[3] . '</td>';

		echo '</tr>';
	}
	echo "</table>";

	mysqli_close($db);
	?>
	<a href="/main.php">Volver al menú</a>
</body>

</html>
