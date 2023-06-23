import requests
import logging

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("requests.packages.urllib3").setLevel(logging.CRITICAL)

url = f"http://localhost:8000/api/v1"


def register_student(name, regNo, block, password, roomNo):
    """
    Register a new student via API request.
    """
    fURL = url + f"/student/auth/register"

    payload = {
        "name": name,
        "regNo": regNo,
        "block": block,
        "password": password,
        "roomNo": roomNo
    }
    response = requests.request("POST", fURL, json=payload)
    if response.status_code == 200:
        
        return 1

    else:
        print(response.text)


def login_student(regNo, password):
    """
    Login to the system as an existing user with API
    """

    fURL = url + f"/student/auth/login"
    payload = {
        "regNo": regNo,
        "password": password
    }
    response = requests.request("POST", fURL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        student_jwt = result['token']
        return 1, student_jwt
    else:
        return 0, 0


def register_faculty(name, empId, password, isHOD):
    """
    Register a new faculty via API request.
    """
    fURL = url + f"/faculty/auth/register"

    payload = {
        "name": name,
        "empId": empId,
        "password": password,
        "isHOD": isHOD
    }
    response = requests.request("POST", fURL, json=payload)
    if response.status_code == 200:
        return 1
    else:
        return 0


def login_faculty(empId, password):
    """
    Login to the system as an existing user with API
    """

    fURL = url + f"/faculty/auth/login"
    payload = {
        "empId": empId,
        "password": password
    }
    response = requests.request("POST", fURL, json=payload)
    result = response.json()
    faculty_jwt = result['token']
    if response.status_code == 200:
        return 1, faculty_jwt
    else:
        return 0

def myinfo(jwt):
    fURL = url + f"/student/me"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    
def mywarden(jwt):
    fURL = url + f"/student/me/my-warden"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    
def show_leave_request(jwt):
    fURL = url + f"/student/leave"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    
def create_leave_request(jwt,lt,ld,ltime,ldur):
    fURL = url + f"/student/leave"
    header = jwt
    payload = {
        "leaveType": lt,
        "leaveDate": ld,
        "leaveTime": ltime,
        "leaveDuration": ldur
    }
    response = requests.request("POST", fURL, headers=header)
    print(response.json())

    
def delete_leave_request(jwt,lid):
    fURL = url + f"/student/leave"
    header = jwt
    payload = {"leaveID":lid
    }
    response = requests.request("DELETE", fURL, headers=header,json= payload)
    print(response.json())
    
def update_leave_request(jwt,lid,lt,ld,ltime,ldur):
    fURL = url + f"/student/leave"
    header = jwt
    payload = {"leaveID":lid,
        "leaveType": lt,
        "leaveDate": ld,
        "leaveTime": ltime,
        "leaveDuration": ldur
    }
    response = requests.request("PUT", fURL, headers=header,json = payload)
    print(response.json())
      

def show_complaint(jwt):
    fURL = url + f"/student/complaint"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    
    
def create_complaint(jwt,type,date,desc,severity):
    fURL = url + f"/student/complaint"
    header = jwt
    payload = {
        "complaintType": type,
        "complaintDate": date,
        "complaintDescription": desc,
        "complaintSeverity": severity
    }
    response = requests.request("PUT", fURL, headers=header,json = payload)
    print(response.json())
    
def delete_complaint(jwt,cid):
    fURL = url + f"/student/complaint"
    header = jwt
    payload = {"complaintID":cid
    }
    response = requests.request("DELETE", fURL, headers=header,json= payload)
    print(response.json())


def update_complaint(jwt,cid,ct,cd,ctime,csev):
    fURL = url + f"/student/complaint"
    header = jwt
    payload = {"complaintID":cid,
        "complaintType": ct,
        "complaintDate": cd,
        "complaintTime": ctime,
        "complaintDuration": csev
    }
    response = requests.request("PUT", fURL, headers=header,json = payload)
    print(response.json())
     
def room_details(jwt):
    fURL = url + f"/student/room-details"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    
def mess_details(jwt):
    fURL = url + f"/student/mess-details"
    header = jwt
    response = requests.request("GET", fURL, headers=header)
    print(response.json())
    


