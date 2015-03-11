<?php
$Prog_name=$argv[0]."\n";	$Task_no = $argv[1]."\n";	$input = $argv[2]."\n";		$output = $argv[3]."\n";	// Retriving argument from command line											//First Argument
$map = array('B' => 's','d' => 'k','e' => 'y','f' => 'g','g' => 'F','a' => 'q',
'h' => 't','i' => 'r','J' => 'd','c' => 'z','k' => 'u','l' => 'p','A' => 'c');												// Associative array for cypher program
$flag = 0;																										// Flag for validation of input arguments
		if(count($argv)!= 4)	
		{
			echo "You have entered more or less argument than 4\n";
		}
		elseif(count($argv) == 4)
		{
			if(preg_match('/^([1-2])$/',$argv[1]) & ($Task_no == 1 | $Task_no == 2))									//Check the format of arguments and number of argument
			{
				$flag++;
	    	}
			else echo "Please give valid Task Number.It should be 1 or 2\n"; 
		
			if(preg_match('/.txt$/',$argv[2]) & file_exists($input="./$argv[2]"))
			{
				$flag++;
	    	}
			else echo "Please give valid text file name(.txt format) for input or File doesn't exists.\n"; 

			if(preg_match('/.txt$/',$argv[3]))
			{
				$flag++;
				if($flag == 3)
				{  
					if($Task_no == 1)																			// Ascii conversion program and respective characte translation
	    			{ 
						$String = file_get_contents('./'.trim($input),FILE_USE_INCLUDE_PATH);					// read the file and store it into array of string
						$array = str_split($String,1);															// Breaking up string into size of 1

						for($i = 0; $i != strlen($String); $i++) 
	    				{
	    					$ascii[$i] += ord($array[$i]); 														// conversion of character to ascii
	    					if($ascii[$i]>=65 & $ascii[$i]<=90)
	    					{
	    		    			if($ascii[$i]>=65 & $ascii[$i]<=77)												//logic for program 1 for BLOCK Letters
	    		    			{
	    		        			$Newascii[$i] = $ascii[$i] + 13;
	    		        			$NewChar .= chr($Newascii[$i]);
	    		    			}
	    		    			else
	    		    			{
	    		    				$Newascii[$i] = $ascii[$i] - 13;
	    		    				$NewChar .= chr($Newascii[$i]);
	    		    			}
	    					}
	    		  			elseif($ascii[$i] >= 97 & $ascii[$i] <= 122)										// logic for small letters
	    		  			{
	    		  				if($ascii[$i]>=97 & $ascii[$i]<=109)
	    		  				{
	    		        			$Newascii[$i] = $ascii[$i] + 13;
	    		        			$NewChar .= chr($Newascii[$i]);
	    		    			}
	    		    			else
	    		    			{
	    		    				$Newascii[$i] = $ascii[$i] - 13;
	    		    				$NewChar .= chr($Newascii[$i]);
	    		    			}
	    		 		 	}
	    		  			elseif($ascii[$i]>=48 & $ascii[$i]<=57)												// Here it is for numbers
	    		  			{
	    		  				if($ascii[$i]>=48 & $ascii[$i]<=52)
	    		  				{		    		  			    
	    		        			$Newascii[$i] = $ascii[$i] + 5;
	    		        			$NewChar .= chr($Newascii[$i]);	    		      
	    		    			}
	    		    			else
	    		    			{
	    		    				$Newascii[$i] = $ascii[$i] - 5;
	    		    				$NewChar .= chr($Newascii[$i]);	    		   
	    		    			}
	    		  			}
	    		  			else
	    		  			{
	    		      			$Newascii[$i] = $ascii[$i];
	    		        		$NewChar .= chr($Newascii[$i]);
	    		  	    	}
	   				 	}
	    				$output = "./$argv[3]";																	// store into output file
	    				if(file_exists($output))																// Checking output file exists or not?
	    				{
	    					file_put_contents("./$output",$NewChar);
	    				}
	    				else file_put_contents("./$output",$NewChar);       									// If doesn't exists then creating the one which the name given at commandline
		  			}
		  			else																						// Starting of Second Program
				  	{
				  		$String = file_get_contents('./'.trim($input),FILE_USE_INCLUDE_PATH);					//read the file and store it into array of string
						$array = str_split($String,1);															// Split the string into size of 1
		
							for($i = 0; $i != strlen($String); $i++) 
			    			{
			    				if(in_array($array[$i],array_keys($map)))										// check the given key and value Exists in associative array
			    				{
			    		    		$Encrypt .= $map[$array[$i]];												// If exists then assign a value of respective key
			    				}	
			    				else
			    				{
			    		    	$Encrypt .= $array[$i];															// esle give the same value as input
			    				}
			    			}
			    	$Encryption_f = "./$argv[3]";
			    		if(file_exists($Encryption_f))
			    		{
			    			file_put_contents("./$Encryption_f",$Encrypt);										// writing the output into the file
			    		}
			    		else
			    		{
			 				file_put_contents("./$Encryption_f",$Encrypt);       
						}
				  	}
				}	else echo "Please give valid arguments for input file.";
			} else echo "Please give valid text file name(.txt format) for output.\n";
	}
	else echo "Please give required Areguments. It should be 4 in total";
?>