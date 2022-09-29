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
</body>
</html>
