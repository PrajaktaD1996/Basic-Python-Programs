import keyboard
#________________________#
#list of keys in usage
#------------------------
#enter  =>Enter
#space  =>Start timer
#larrow =>prev
#rarrow =>next
#ctrl+r =>redo/retry
#ctrl+u =>undo
#ctrl+s =>save
#
#________________________#
##isuue in combiantional logic
while True:
    if(keyboard.read_key()=="enter"):
        print("enter is pressed")
    if(keyboard.is_pressed('space')): 
        print("space is pressed")
    if(keyboard.is_pressed("left arrow")): 
        print("left-arrow key pressed")
    if(keyboard.is_pressed("right arrow")): 
        print("right")
    if(keyboard.is_pressed("down arrow")):
        print("down")
    if(keyboard.is_pressed("up arrow")):
        print("up")
    if( keyboard.is_pressed('r')):  ##detecting single time for ctrl+s
        print("retry")
    if( keyboard.is_pressed('u')):  ##detecting single time for ctrl+s
        print("undo")
    if(keyboard.is_pressed('s')):
        print("save")






    
  
