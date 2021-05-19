import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_E():
## Number of Directory and Directory Name ##
  ndir = 1;   dirnam = [[]]*ndir
  dirnam[0] = './DATA'
  
## Computational Condition ##    
  nini = 0     # Initial step number
  dt = 0.00025 # Time step in [ps]
  
## Constant and Array ##  
  stp = np.array([]); etot = np.array([]); epot = np.array([]); 
  base = np.array([0.,0.]); lini = 1; cnt = nini
  
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
        epot = np.append(epot, float(dat[4]))
        if lini == 1: base[0] = dat[4]  
        for i in range(6): dat = fp.readline().split() 
        etot = np.append(etot, float(dat[4]))
        if lini == 1: base[1] = dat[4]; lini = 0  
        cnt += 1
      elif dat[0] == 'Voluntary': break
      else: continue
    fp.close()
    
## Console Output ##  
  print('total number of data: %d' %(len(stp)))
  
## Plot Figure ##
  #plt.plot(stp*dt, etot, label = 'Total energy', linestyle = 'dashed')
  #plt.plot(stp*dt, epot, label = 'Potential energy')
  plt.plot(stp, etot, label = 'Total energy', linestyle = 'dashed')
  plt.plot(stp, epot, label = 'Potential energy')
  plt.legend()
  plt.title('Time Evolution of Energy')
  #plt.xlabel('Time (ps)')
  plt.xlabel('MD step')
  plt.ylabel('Energy (eV)')
  plt.subplots_adjust(left=0.165, right=0.94, bottom=0.12, top=0.92)
  plt.show()
  
plot_E()
