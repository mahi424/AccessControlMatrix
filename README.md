# AccessControlMatrix
Create Access Control Matrix from the output of ls -la

The command ls -la is used to list the content of directory. The output provides illustrative details about file and directories present in it.
Some of the details are owner, group, permissions etc.

    ls -la
    total 48
    drwxr-xr-x 4 user1 Users 4096 Jul  7 13:31 .
    drwx------ 6 user2 Users 4096 Jun  4 17:26 ..
    -rwxr-xr-x 1 user3 Prof  167 Jul  5 12:27 file1
    -rwxrwxrwx 1 user4 tech  425 Jul  5 12:27 file2
    dr--r-xrwx 2 user5 admin 4096 Jul  5 22:26 file3
    
This program uses a saved version of the above output to construct a Access Control Matrix

                     .                       ..                      file1                    file2                    file3          
              ==================================================================================================================================
    user4           r-x                      ---                      r-x                      rwx                      rwx           
    user5           r-x                      ---                      r-x                      rwx                      r--           
    user2           r-x                      rwx                      r-x                      rwx                      rwx           
    user3           r-x                      ---                      rwx                      rwx                      rwx           
    user1           rwx                      ---                      r-x                      rwx                      rwx    
    
 Below is the images of Code in action
 
 
 ![Input File Image](ScreenshotOfInput.png?raw=true "Image of input file used")
 
 ![Output File Image](ScreenshotOfOutput.png?raw=true "Image of output file")