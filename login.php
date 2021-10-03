<?php 
$user=$_POST["user"];
$pass=$_POST["pass"]; 
?>
<?php 
if ($user=="sina" && $pass=="majidi"){
  echo "ok";
} else {
  echo "not";
}
?>

