import subprocess
import time

def run_sniffer():
    # Running sniffer.py directly in the same terminal
    print("Running sniffer.py for 30 seconds...")
    
    # Start sniffer.py and wait for 30 seconds
    sniffer_process = subprocess.Popen(['python3', 'sniffer.py'])
    
    # Wait for 30 seconds (sniffer.py should be running during this time)
    time.sleep(30)  # This will block for 30 seconds to simulate sniffer running
    
    # After the 30 seconds, terminate the sniffer process if it's still running
    sniffer_process.terminate()
    sniffer_process.wait()  # Wait for the process to actually terminate

    print("sniffer.py has completed.")

def run_convert_logs():
    # Run the convert_logs_csv.py script after sniffer.py has finished
    print("Running convert_logs_csv.py...")
    convert_logs_process = subprocess.run(['python3', 'convert_logs_to_csv.py'])

    # Wait for convert_logs_csv.py to finish (this is synchronous)
    convert_logs_process.check_returncode()

def run_generate_report():
    # Run the generate_report.py script after convert_logs_csv.py has finished
    print("Running generate_report.py...")
    generate_report_process = subprocess.run(['python3', 'generate_report.py'])

    # Wait for generate_report.py to finish (this is synchronous)
    generate_report_process.check_returncode()

def main():
    # Run the sniffer for 30 seconds and wait for it to finish
    run_sniffer()

    # Proceed with the rest of the process only after sniffer.py is finished
    run_convert_logs()
    run_generate_report()

if __name__ == "__main__":
    main()
