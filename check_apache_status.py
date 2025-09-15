import subprocess

def check_apache_status():
    # Try both common Apache service names
    for service_name in ["apache2", "httpd"]:
        try:
            result = subprocess.run(["systemctl", "is-active", service_name],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            status = result.stdout.strip()
            if status == "active":
                print(f"✅ Apache service '{service_name}' is running.")
                return
            elif status == "inactive" or status == "failed":
                print(f"❌ Apache service '{service_name}' is not running. Status: {status}")
                return
        except Exception as e:
            continue  # Try next service name

    print("⚠️ Apache service not found (tried 'apache2' and 'httpd').")

# Run the check
check_apache_status()
