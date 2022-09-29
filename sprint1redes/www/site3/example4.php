<html>
<body>
<h1>Jubilación</h1>
<?php
	function edad_en_5_años($edad){
	return $edad + 5;
}
if (edad_en_5_años($_GET[edad])>65){
	echo "En 5 años tendrás edad de jubilación";
	}else {
	echo "¡Disfruta de tu tiempo!";
	}
?>
<table>
<tr>
<th>Edad</th>
<th>Info</th>
</tr>
<?php
	$lista =array(64,65,61,59,53);
foreach($lista as $valor){
	echo "<tr>";
	echo "<td>".$valor."</td>";
	echo "<td".mensaje($valor)."</td>";
	echo "</tr>";
	}
?>
</table>
</body>
</html>
