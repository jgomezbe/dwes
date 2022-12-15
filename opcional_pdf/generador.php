<?php
$name = $_POST['name'];

$surname = $_POST['surname'];

$date=date('d/m/y');
require('fpdf.php');

class PDF extends FPDF{

    function Header(){          
        $this->Image('logo.png',10,10,30); 
	    $this->SetFont('Arial','B',16);
        $this->cell(120); 
        $this->cell(30,10,'DIPLOMA',1,0,'C');
        $this->cell(80);
        $this->Image('diploma.png',260,10,30); 
        $this->Ln(30);  
    }
    
    function Footer(){
        $this->SetY(-15);
        $this->SetFont('Times','I',10);
        $this->Cell(0,10,utf8_decode('Página ').$this->PageNo().'/{nb}',0,0,'C');
    }

}

$pdf = new PDF();

$pdf->AliasNbPages();
$pdf->AddPage('L');
$pdf->SetFont('Times','B',16);
$pdf->Cell(0,10,'Desarrollador Web en Entorno Servidor ',0,0,'C');

$pdf->Cell(-274,40,'El alumno '.' '.$name.' '.$surname.' se ha graduado en la asignatura de Desarrollo Web en Entorno Servidor',0,0,'C');
$pdf->Cell(-274,60,'a fecha'.' '.date('d/m/Y'),0,1);
$pdf->Cell(274,60,'Firma del alumno ',0,1,'C');
$pdf->SetXY(($pdf->GetPageWidth()/2 )- ($pdf->GetStringWidth($name.' '.$surname)/2),160);
$pdf->Cell($pdf->GetStringWidth($name.' '.$surname),10,$name.' '.$surname,0,1,'C');

$pdf->SetXY(87+$pdf->GetStringWidth($name.' '.$surname),90);
$pdf->Image('firma.png', 135, 140, -300);
$pdf->Output();

?>