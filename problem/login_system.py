class database:
    
    def store_data(self):
        name="saurabh"
        email="raghav"  
        return name , email
class login_system(database):
    def login(self,name,email):
        db_name, db_email = self.store_data()
        if name==db_name and email==db_email:
            print("login successful")
            def website():
                print("welcome to website")
            website()
        else:
            print("login failed")
            def register():
                print("please register")
            register()
obj=login_system()
obj.login("saurabh","raghav")                