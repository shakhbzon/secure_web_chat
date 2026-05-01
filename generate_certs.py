import os
import subprocess

def generate():
      passimport os
import subprocess

def generate_self_signed_cert():
      cmd = [
                "openssl", "req", "-x509", "-newkey", "rsa:4096", "-keyout", "server.key", 
                "-out", "server.crt", "-days", "365", "-nodes",
                "-subj", "/C=UZ/ST=Tashkent/L=Tashkent/O=SecureChat/OU=IT/CN=localhost"
      ]
      try:
                subprocess.run(cmd, check=True)
except Exception as e:
        print(f"Xato: {e}")

if __name__ == "__main__":
      generate_self_signed_cert()
  
