import numpy as np

def make_PDB():
## Number of Directory and Directory Name ##
  ndir = 1;   dirnam = [[]]*ndir
  dirnam[0] = './test'
  
## Constant ##
  rtd = 180/np.arccos(-1)

## Read Data and Make PDB File ##
  lini = 1
  pdb = open('config.pdb', 'w')
  for n in range(ndir):
    filnam = '%s/XDATCAR' %(dirnam[n])
    fp = open(filnam, 'r')
    print('open: %s' %(filnam))
    while True:
      dat = fp.readline().split(); 
      if len(dat) == 0: break 
      if lini == 1:
        fac = float(fp.readline().split()[0])
        cel = np.array([])
        for i in range(3): cel = np.append(cel, np.array(fp.readline().split(), dtype='float'))
        cel = cel.reshape(3,3)*fac
        typ = fp.readline().split()
        nat = np.array(fp.readline().split(), dtype='int')
        it = []; lini = 0 
        for i in range(len(typ)):
          for j in range(nat[i]): it.append(typ[i])
        dat = fp.readline().split()
      pdb.write('CRYST1%9.3f%9.3f%9.3f' %(np.linalg.norm(cel[:,0]),np.linalg.norm(cel[:,1]),np.linalg.norm(cel[:,2])))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,1],cel[:,2])/np.linalg.norm(cel[:,1])*np.linalg.norm(cel[:,2]))*rtd))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,0],cel[:,2])/np.linalg.norm(cel[:,0])*np.linalg.norm(cel[:,2]))*rtd))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,1],cel[:,0])/np.linalg.norm(cel[:,1])*np.linalg.norm(cel[:,0]))*rtd))
      pdb.write('%16d\n' %(sum(nat)))
      xyz = np.zeros([sum(nat), 3]) 
      for i in range(sum(nat)):
        xyz[i,:] = np.array(fp.readline().split(), dtype='float')
        xyz[i,:] = (np.matrix(cel)*np.matrix(xyz[i,:]).T).T
        pdb.write('HETATM%5d%3s%24.3f%8.3f%8.3f%24s\n' %(i, it[i], xyz[i,0], xyz[i,1], xyz[i,2], it[i]))
      pdb.write('END\n')
    fp.close()
  pdb.close()
 
make_PDB()
