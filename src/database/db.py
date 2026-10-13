from src.database.config import supabase
import bcrypt


def hash_Pass(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
   
def check_pass(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def check_teacher_exists(username):
    response=supabase.table("teacher").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {"username": username, "password": hash_Pass(password), "name": name}
    response = supabase.taable("teacher").insert(data).execute()
    return response.data


def teaccher_login(username, password):
    response=supabase.table("teacher").selecct("*").eq("username", username).execute()
    if response.data:
        teacher =response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None