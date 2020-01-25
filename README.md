# PRESENTATION_zyxelControl

Sometimes Zyxel routers for some reason do not have a “reboot” button on the web interface. This means that if you need to reboot it remotely, you will have to connect to this router via SSH to register the "reboot" command. Anyway, sometimes you may need to quickly connect to some routers through the terminal. There is a program called 'PuTTY' that solves this problem, but I still wanted to do something for a faster and more convenient connection.


For this, this program was developed.
I have it 4th in a row (I didn’t post the 3rd, because there it’s just converting links from one format to another, nothing interesting)
By this moment, I already understood the tkinter module much better, so writing it did not make me any trouble and took quite a bit of time.

Features:
  switching between fields by pressing TAB,
  when pressing ENTER anywhere - a new terminal opens with a connection
 
Used modules:
  os,
  tkinter

In fact, this is a simple GUI for the program 'plink.exe'
