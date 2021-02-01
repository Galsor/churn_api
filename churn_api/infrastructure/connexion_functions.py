import subprocess

def get_host(service_name):
    bash_cmd = "kubectl get services {0} | grep {0}".format(service_name)+ "| awk '{print $4}'"
    host = subprocess.check_output(bash_cmd, shell=True, text=True)[:-1]
    return host


def get_port(service_name):
    bash_cmd = "kubectl get services {0} | grep {0}".format(service_name)+ "| awk '{print $5}'"
    port = subprocess.check_output(bash_cmd, shell=True, text=True).split(':')[0]
    return port
