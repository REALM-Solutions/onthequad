
class UserHelper:
    def createUserName (email):
        emailArray = email.split("@")
        userName = emailArray[0]
        return userName
