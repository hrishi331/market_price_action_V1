# Import packages
import nsepython as nse
import time
import pandas as pd
l = []
for i in range(10):
    l.append(nse.index_info('NIFTY 50'))
    print(f'reading {i} taken!')
    print('-'*50)
    time.sleep(5)

print(pd.DataFrame(l))
    


