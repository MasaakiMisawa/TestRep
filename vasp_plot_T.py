import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_T():
## Number of Directory and Directory Name ##
  ndir = 1;   dirnam = [[]]*ndir
  dirnam[0] = './DATA'
  
## Computational Condition ##    
  nini = 0     # Initial step number
  dt = 0.00025 # Time step in [ps]
  
## Constant and Array ##  
  stp = np.array([]); temp = np.array([]); cnt = nini
  
## Read Data ##
  for n in range(ndir):
    filnam = '%s/OUTCAR' %(dirnam[n])
    fp = open(filnam, 'r')
    print('open: %s' %(filnam))
    while True:
      dat = fp.readline().split()   
      if dat == []: continue
      elif dat[0] == '%':
        stp = np.append(stp, cnt)
        for i in range(2): dat = fp.readline().split() 
        temp = np.append(temp, float(dat[5]))
        cnt += 1
      elif dat[0] == 'Voluntary': break
      else: continue
    fp.close()
    
## Console Output ##  
  print('total number of data: %d' %(len(stp)))
  
## Plot Figure ##
  plt.plot(stp, temp)
  plt.title('Time Evolution of Temperature')
  #plt.xlabel('Time (ps)')
  plt.xlabel('MD step')
  plt.ylabel('Temperature (K)')
  plt.subplots_adjust(left=0.165, right=0.94, bottom=0.12, top=0.92)
  plt.show()
  
plot_T()
