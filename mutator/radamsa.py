import subprocess

class RadamsaMutator:
    __mutator_name__ = "RadamsaMutator"

    def __init__(self):
        pass

    def mutate(self, input, output):
        command = "./radamsa {} -o {}".format(input, output)
        p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
        p.wait()
