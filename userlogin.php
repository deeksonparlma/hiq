<?php
session_start();
$host = 'localhost';
$password = 'stiveckamash';
$user = 'stephen';
$db = 'webapp';



$conn = mysqli_connect($host , $user , $password , $db);
 if (!$conn) 
 {
  die('Connection Failed!:'.mysqli_connect_error());
 }


 if (isset($_POST['login'])) 
 {
       $email = mysqli_real_escape_string($conn,$_POST['email']);
       $pass = mysqli_real_escape_string($conn,$_POST['password']);

      //check if username is found

       $check = "SELECT * from user  where email = '$email' ";

       //query the results
       $results = mysqli_query($conn , $check);

       //create the record rows
       $row =mysqli_num_rows($results);


       //check number of rows to be one
       if ($row == 1) 
       {

        //return the row
        //the fetch returns rows in array form
        $found = mysqli_fetch_array($results);

        //get password from the array
        $dbpass = $found['password'];

        //verify password with the username in the row

        if ($pass == $dbpass) 
        { 
                  //create a super global variable to be assigned to the loggen in user
                  $_SESSION['name']=$email;
           echo "<script>alert('Login  successful')
                  window.location.href='index.php';
                 </script>";

        }
        else
        {
          echo "<script>alert('Wrong Password')
          window.location.href='userlogin.php'</script>";
        }

       }

       else
       {
          echo "<script>alert('No username Found')
          window.location.href='regesteration.php</script>";
       }



 }

?>


<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
<form class="" action="login.php" method="post">
  <table>
    <tr>
      <td><label for="">Email</label></td>
     <td> <input type="email" name="email" placeholder="email address"></td>
    </tr>
    <tr>
      <td><label for="">Password</label> </td>
      <td><input type="password" name="password" placeholder="Password"></td>
    </tr>
    <tr>
    <td><input type="submit" name="login" value="login"></td>
    </tr>
  </table>
</form>
  </body>
</html>
