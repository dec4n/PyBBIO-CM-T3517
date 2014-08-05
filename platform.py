#Method for detect platform
def detect_platform():
  """ Attempt to detect the current platform. Returns : 'Sitara Am35172',
      'BeagleBone >=3.8'. """
  platform = ''
  with open('/proc/cpuinfo', 'rb') as f:
    cpuinfo = f.read().lower() 
  #In this part do it the parameter verification with 'v7l' that
  #represent de ARMv7 architecture (Using the parameter ARMV7 this don't 
  #work) and with 'neon vfpv3' that represent a feature at this processor  
  if ('v7l' in cpuinfo and 
     ('neon vfpv3' in cpuinfo)): 
    platform = 'Sitara'
  #With this we verify that verification in cpuinfo was made
    print 'Entro a cpuinfo'
  import commands
  uname_status, uname = commands.getstatusoutput('uname -a')
  if uname_status > 0:
    exit('uname failed, cannot detect kernel version! uname output:\n %s' % uname)
  if ('3.7.2-cm-t3517' in uname):
    platform += ' 3.7.2'
  #With this we verify that verification inside of uname was made
    print "Entro a uname_a"
    print platform
  else:
    platform += ' >=3.8'
    print platform
    print 'saliendo'
  return platform

#With this We execute the function Locally, withouth complete compilation 
detect_platform()
