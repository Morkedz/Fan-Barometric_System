import subprocess
import pandas as pd
import io

def export_kern_excel():
    try:
        raw_output = subprocess.check_output(['dmesg', '--reltime']).decode('utf-8')
    except Exception as e:
        print(f"Error grabbing kernel logs: {e}")
        return
    lines = raw_output.strip().split('\n')
    data = []
    
    for line in lines:
        if ']' in line:
            timestamp, message = line.split(']', 1)
            data.append({
                'Timestamp': timestamp.replace('[', '').strip(),
                'Log_Message': message.strip()
            })

    df = pd.DataFrame(data)
    filename = "kernel_log_report.xlsx"
    
    df.to_excel(filename, index=False)
    print(f"Kernel data successfully exported to {filename}")

if __name__ == "__main__":
    export_kern_excel()