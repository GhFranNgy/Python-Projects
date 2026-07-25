import os

script_dir = os.path.dirname(__file__)
log_dir = os.path.join(script_dir, "server.log")
info_dir = os.path.join(script_dir, "info.txt")
err_dir = os.path.join(script_dir, "error.txt")
warn_dir = os.path.join(script_dir, "warning.txt")

info_counter = 0
error_counter = 0
warning_counter = 0

def read_file():
    global info_counter, error_counter, warning_counter
    with open(log_dir, "r") as server_log:
        lines = server_log.readlines()
        for line in lines:
            if "INFO" in line:
                info_counter += 1
                add_info_Msg(line)
            elif "ERROR" in line:
                error_counter += 1
                add_err_Msg(line)
            elif "WARNING" in line:
                warning_counter +=1
                add_warn_Msg(line)

def add_info_Msg(line):
    with open (info_dir, "a") as file:
        file.write(line)

def add_err_Msg(line):
    with open (err_dir, "a") as file:
        file.write(line)

def add_warn_Msg(line):
    with open (warn_dir, "a") as file:
        file.write(line)

def output():
    print(f"Errors: {error_counter} Infos: {info_counter} Warnings: {warning_counter}")

read_file()
output()