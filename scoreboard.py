import os
import constants as cons

def load_highscore():
    """Loads highscore from the file"""
    if not os.path.exists(cons.HIGHSCORE_PATH):
        save_highscore(0,"")
    
    with open(cons.HIGHSCORE_PATH,"r") as f:
       file_content = f.read().strip()
       if file_content != "":
            score_str,player_name = file_content.split(",",1)
            return (int(score_str),player_name)
       return (0,"")
            
    
    

def save_highscore(new_high_score,player_name):
    """Saves new highscore"""
    with open(cons.HIGHSCORE_PATH,"w") as f:
        f.write(f"{new_high_score},{player_name}")