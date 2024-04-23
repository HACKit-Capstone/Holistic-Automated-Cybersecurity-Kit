import dns.resolver
import sys

def check_subdomain_takeover(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        for rdata in answers:
            cname = rdata.target.to_text()
            if cname.endswith("s3.amazonaws.com"):
                return f"Subdomain {subdomain} is vulnerable to S3 bucket takeover."
            elif cname.endswith("azurewebsites.net"):
                return f"Subdomain {subdomain} is vulnerable to Azure App Service takeover."
            elif cname.endswith("herokuapp.com"):
                return f"Subdomain {subdomain} is vulnerable to Heroku app takeover."
            else:
                return f"Subdomain {subdomain} points to {cname}, which may be vulnerable to takeover."
    except dns.resolver.NoAnswer:
        return f"No CNAME records found for {subdomain}."
    except dns.resolver.NXDOMAIN:
        return None

def read_subdomains(filename):
    with open(filename, 'r') as file:
        subdomains = [line.strip() for line in file.readlines() if line.strip()]
    return subdomains

def save_to_file(filename, messages):
    with open(filename, 'w') as file:
        for message in messages:
            file.write(message + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subdom-tk.py <input_filename.txt>")
        sys.exit(1)

    msg = sys.argv[1]
    input_filename = f"{msg}.txt"
    output_filename = f"{msg}subtk.txt"

    subdomains = read_subdomains(input_filename)
    vulnerable_subdomains = [check_subdomain_takeover(subdomain) for subdomain in subdomains if subdomain]

    save_to_file(output_filename, filter(None, vulnerable_subdomains))
    print(f"Subdomain takeover results saved to: {output_filename}")
