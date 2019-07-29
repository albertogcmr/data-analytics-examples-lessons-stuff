# quandl.com

import quandl
import pandas as pd

mydata = quandl.get("FRED/GDP")

print(mydata.head())