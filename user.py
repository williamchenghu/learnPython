class User:
    def __init__(self, usr_name, usr_email, usr_pwd, usr_job):
        self.name = usr_name
        self.email = usr_email
        self.password = usr_pwd
        self.current_job_title = usr_job

    def change_password(self, new_pwd):
        self.password = new_pwd

    def change_job_title(self, new_job):
        self.current_job_title = new_job

    def get_user_info(self):
        print(f"Hey, {self.name} is currently working as a {self.current_job_title}, reach to them at {self.email}!")
