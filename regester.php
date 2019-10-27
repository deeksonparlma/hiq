<!--
CREATE DATABASE IF NOT EXISTS `user`;
USE `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text ,
  `fname` text NOT NULL,
  `lname` text ,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`id`)
);




-->




<?php  
//start creating the connecting parameters
 $host = 'localhost';
 $password = 'stiveckamash';
 $user = 'stephen';
 $db = 'webapp';



 $conn = mysqli_connect($host , $user , $password , $db);
  if (!$conn) 
  {
    die('Connection Failed!:'.mysqli_connect_error());
  }
//define an empty array to hold errors gotten
$error=[];
//database entry and populating



if (isset($_POST['regester'])) 
{


  //filter the data and create variables to hold them
    $username = mysqli_real_escape_string($conn,$_POST['username']);
    $email = mysqli_real_escape_string($conn,$_POST['email']);
    $fname = mysqli_real_escape_string($conn,$_POST['fname']);
    $lname = mysqli_real_escape_string($conn,$_POST['lname']);
    $phone = mysqli_real_escape_string($conn,$_POST['phone']);
    $password = mysqli_real_escape_string($conn,$_POST['password']);
    $password1 = mysqli_real_escape_string($conn,$_POST['password1']);

echo $username . $phone;
    //check if the values are empty
    if (empty($username)) 
    {
        array_push($error, "<p> Please enter your username</p>");
    }
    elseif (empty($email)) 
    {
        array_push($error,"<p> Please enter your email</p>");
    }
    elseif (empty($phone)) 
    {
        array_push($error,"<p> Please enter your phone number</p>");
    }
    elseif (empty($lname)) 
    {
      array_push($error,"<p> Please enter your lastname</p>");
    }
    elseif (empty($fname)) 
    {
      array_push($error,"<p> Please enter your first name</p>");
    }
    elseif (empty($password)) 
    {
        array_push($error,"<p> Please enter your password</p>");
    }
    elseif (empty($password1)) 
    {
        array_push($error,"<p> Please confirm your password</p>");
    }


    //check the length of password and confirm;;
    if (strlen($username ) < 5) 
    {
      array_push($error,"<p>Your username must be more then seven characters long</p>");
    }

    if ($password != $password1) 
    {
      array_push($error,"<p>Password does not much</p>");
    }
      //post the data to the db if the conditions are satisfied


    //encript password
    $password = password_hash($password ,PASSWORD_DEFAULT);
  
  //check if the email or username has been already been used
    $select = "SELECT * from user
 where username = '$username' or email = '$email'";
    $result = mysqli_query($conn , $select);
    //returns all rows from the database
    $numRow = mysqli_num_rows($result);
    if ($numRow > 0) 
    {
      array_push($error,"Username or email Already Exists");
      //direct user to the regestration page
      header("Location :regesteration.php");
    }

    else
    {
      if(count($error)==0){

        //insert data
     $data = "INSERT INTO user (username,fname, lname, email ,phone ,password) VALUES ('$username','$fname','$lname' ,'$email' ,'$phone' , '$password')";

        $insert = mysqli_query($conn, $data);

        if ($insert) 
        {
          echo "<script>alert('Regestration successful');
                window.location.href='userlogin.php';
          </script>";
        }
        else
        {
          echo "<script>alert('Error');</script>";
          echo "erro type".  mysqli_error($conn);
        }

      }
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
    <div class="">
      <form class="" action="" method="post">
        <div class="error">
            <?php
             foreach ($error as $e) {
              echo $e;
            } ?>
        </div>
        <table>

          <tr>
            <td>
        <label for="">First name</label>
        </td>
        <td>

        <input type="text" name="fname" placeholder="First Name">
        </td>

      </tr>
      <tr>

      <td><label for="">Last name</label></td>
        <td><input type="text" name="lname" placeholder="Last name"> </td>

      </tr>
      <tr>
        <td><label for="">username</label></td>
      <td><input type="text" name="username" placeholder="username"></td>
      </tr>
      <tr>
        <td>

          <label for="">Password</label>

          </td>

          <td>

        <input type="password" name="password" placeholder="Password">

        </td>
        </tr>
        <tr>

        <td>

        <label for="">Password</label>

        </td>

        <td>
        <input type="password" name="password1" placeholder="Confirm password">
        </td>
      </tr>
        <tr>

        <td>
        <label for="">Telephone</label>
        </td>
        <td>

        <input type="tel" name="phone" placeholder="Telephone">
        </td>
        </tr>
        <tr>

          <td>

        <label for="email">Email</label>
        </td>
        <td>
          <input type="email" id="email" name="email" placeholder="Email">
        </td>
      </tr>
      <tr>
        
        <td><input type="submit" name="regester" value="regester"></td>
      </tr>
        </table>

      </form>


    </div>

  </body>
  </html>
