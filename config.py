import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "4410228")

API_HASH = os.environ.get("API_HASH", "e73c6f2e8842acdeb8bf8c18628bb772")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6140023675:AAEujcvWz-GDZOezpWCr5jKtwYS7ITazUDA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "ultroidofficial") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Cluster0:Cluster0@cluster0.c07xkuf.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
