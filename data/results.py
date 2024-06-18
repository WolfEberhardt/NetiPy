import command_runner

def activ_interface():
    result = command_runner.command_runner(command="netsh interface show interface")
    activ = result
    return activ