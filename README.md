# Bulk_email_sender
Bulk_email_sender is just an another python script with very basic programming concepts. This script helps you to send emails only with text message with your specified email addresses in the script.
As I mentioned this very basic unsanitized script so don't try to play with it.

**Use it for only educational purposes only**

#### Only works when targeted email provider allows you to send as many emails as per your need here i am using Gmail account for which you have to enable the Less secure apps(LSA) permission ON which basically means that now we can connect to Gmail account with username and password specified from our script.


## USAGE
This image helps you to understand how it works.


![](/usage.png)


- First argument it takes is file name "-file" as shown in image
    > -file /path to your file
    
Specify your answer 
- Secondly if you did't want to send email to many target then you may use --targat to target one person
    > --target example.gmail.com
    
- And then specify the email server name like here i mentioned gmail.server
    > -server smtp.gmail.com
    
- At last specify the sender name
    > -sender example
  
> At last if the script executed successfully then you see ***send..***
