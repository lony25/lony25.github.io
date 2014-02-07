import subprocess

class git:
    def __init__(self):
        self.git_command = 'git %s'
        print 'class git initialized'
        
    def init(self):
        #p = subprocess.Popen(self.git_command % ' '.join(['init']), stdout=subprocess.PIPE, shell=True)
        #output, err = p.communicate()
        print "Hello"

    def status(self):
        p = subprocess.Popen(self.git_command % ' '.join(['status']), stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        print output

    def printC(self):
        print self.git_command % ' '.join(['status'])

    def commit(self):
        p = subprocess.Popen(self.git_command % ' '.join(['commit','-am','\"First check for the git lib\"']), stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        print output
    
    def add(self):
        p = subprocess.Popen(self.git_command % ' '.join(['add', '.']), stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        
    def push(self):
        p = subprocess.Popen(self.git_command % ' '.join(['push']), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        output, err = p.communicate(input='lony25')
                             

if __name__=='__main__':
    repo = git()
    repo.status()
    repo.init()
    repo.add()
    repo.commit()
    repo.push()

