<?php

    if(isset($_POST['input1']) && isset($_POST['input2'])){
        
        if($_POST['input1'] == "admin" && $_POST['input2'] == "hahaha"){
            echo "BERHASIL BRUTE FORCE!!!";
        } else {
            echo "Something wrong";
        }
    } else {
        echo "parameter tidak masuk";
    }













?>