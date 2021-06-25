import numpy as np

def make_PDB():
## Number of Directory and Directory Name ##
  ndir = 1;   dirnam = [[]]*ndir
  dirnam[0] = './DATA'
  
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
      fac = float(fp.readline().split()[0])
      cel = np.array([])
      for i in range(3): cel = np.append(cel, np.array(fp.readline().split(), dtype='float'))
      cel = cel.reshape(3,3)*fac
      pdb.write('CRYST1%9.3f%9.3f%9.3f' %(np.linalg.norm(cel[:,0]),np.linalg.norm(cel[:,1]),np.linalg.norm(cel[:,2])))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,1],cel[:,2])/np.linalg.norm(cel[:,1])*np.linalg.norm(cel[:,2]))*rtd))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,0],cel[:,2])/np.linalg.norm(cel[:,0])*np.linalg.norm(cel[:,2]))*rtd))
      pdb.write('%7.2f' %(np.arccos(np.dot(cel[:,1],cel[:,0])/np.linalg.norm(cel[:,1])*np.linalg.norm(cel[:,0]))*rtd))
      typ = fp.readline().split()
      nat = np.array(fp.readline().split(), dtype='int')
      pdb.write('%16d\n' %(sum(nat)))
      if lini == 1:
        it = []; lini = 0 
        for i in range(len(typ)):
          for j in range(nat[i]): it.append(typ[i])
      xyz = np.zeros([sum(nat), 3]) 
      dat = fp.readline().split()
      #if dat[0] == 'Direct': fac2 = float(dat[3])
      #elif dat[0] == 'Cartesian': fac2 = float(dat[3])
      for i in range(sum(nat)):
        xyz[i,:] = np.array(fp.readline().split(), dtype='float')
        xyz[i,:] = (np.matrix(cel)*np.matrix(xyz[i,:]).T).T
        pdb.write('HETATM%5d%2s%13d%12.3f%8.3f%8.3f%24s\n' %(i, it[i], i, xyz[i,0], xyz[i,1], xyz[i,2], it[i]))
      pdb.write('END\n')
    fp.close()
  pdb.close()
 
make_PDB()
