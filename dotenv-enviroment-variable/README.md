### Info
https://pypi.org/project/python-dotenv/

### Files
main.py
```
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
```
.env
```
# tokens

KEY1=clave1
KEY2=key2
KEY3=top-secret
```
.gitignore
```
.env
```

### Outputs

```
$ python3 main.py

[output] >>> 
    clave1
    key2
    top-secret
```
