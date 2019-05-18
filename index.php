
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<?php 
		if(isset($_POST['submit'])){
			$user = $_POST['username'];
			$pass = $_POST['password'];

			if($user == "user" && $pass == "naruto"){
				header("Location: congrats.php");
			}else{
				echo "Something wrong";
			}
		}
	?>

	<form action="" method="POST">
		<input type="text" name="username" id="username" placeholder="Username...">
		<input type="password" name="password" id="password" placeholder="Password...">
		<input type="submit" name="submit" id="submit" value="LOGIN">
	</form>
</body>
</html>