import subprocess


def run_command(command_list):
    output = subprocess.check_output(command_list)
    return output
