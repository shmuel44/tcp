import socket



def menu():
 								#Menu function
    print ("[1] for UPLOAD  prees 1")
    print ("[2] for DOWNLOAD prees 2 ")
    print ("[3] for LIST prees 3")
    print ("[4] for exit prees 4")
    choice= int (input(">>"))
    while (choice < 1) or ( 4< choice):				#Check if the number entered is valid
        choice = int (input ("error, pless enter Correct number \n>>" ))
        if(1 <= choice <=4 ):
            return choice
    
    return choice


def exit_or_menu():

    tmp_choice =str( input ("for to back to the menu  frees m, for exit prees any key \n>>" ))
    choice =tmp_choice.lower()					#Adding an option that even a capital letter (M) will return to the main menu
    thanks = ("I hope this was helpful to you")
    if (choice == 'm' ):
	    main()
    else:
	    print  (thanks)
            



def upload(file_name):
    
    print("upload.....\n")          
    server.send (b'upload')                                 #send the commend to the server
    server.send(file_name.encode())                         #send the file name in binary to the server
    try:
        with open(file_name , 'rb') as file_up:	            #open the file taht we want to send and reading him
            data = file_up.read(1024)                       #read only the size we can send  
            while data:                                     #As long as the entire file has not been sent
                server.send(data)                           #send data to the server
                data = file_up.read(1024)                   #Sends the rest of the file in the allowed amount
        print(f"Upload file: {file_name} successfully!")
    except:
        print(f"the file: {file_name} not exist, please check the name again!")
	        
                
def download(file_name):
  
    print("download")
    server.send(b'download')                                #send the commend to the server
    server.send(file_name.encode())                         #send the file name in binary to the server
    
    with open(file_name , 'wb') as file_dwn:                #open new file 
        while True:
            data = server.recv(1024)                        #get the data fro the server
            if data:                                        #if we have data...
                file_dwn.write(data)                        #write the data in the new file
            else:                                           #when the all data finish to send to me .....Break
                break
    print(f"download file: {file_name} seccessful")
    
        


def list_of_all_files():
    print ("printing....")
    server.send(b'list')                 #send the commend to the server

def main():
				#main
	
    choice = menu()
    if (choice == 1):		    
        path=input("Please enter full file patch\n>>") 
        upload(path)
        exit_or_menu()
    elif (choice == 2):
        download(file_name)
        exit_or_menu()
    elif(choice == 3):
        list_of_all_files()
        exit_or_menu()
    elif(choice == 5):
        print("see you later")

if __name__ == "__main__":
 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = input('\nplease enter IP address of the server:\n>> ')
    PORT = 12345
    server.connect((HOST, PORT))
    
    main()
