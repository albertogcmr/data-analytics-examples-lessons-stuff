import os
from dotenv import load_dotenv

if __name__ == '__main__': 
    # load_dotenv()
    load_dotenv(dotenv_path='.env')


    key_1 = os.getenv('KEY1', 'No value found')
    print(key_1) 

    key_2 = os.getenv('KEY2', 'No value found')
    print(key_2)  
      
    key_3 = os.getenv('KEY3', 'No value found')
    print(key_3)