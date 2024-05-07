from consumers.users_ms.user_consumer import *
from consumers.tasks_ms.task_consumer import *

class RecordService:
    
    @staticmethod
    def create_record_service(data):

        user_data = {
            "company": data['user_company'],
            "line": data['user_line']
        }

        user = create_user(user_data)

        if user.status_code == 201:

            task_data = {
                "id": data['capac_id'],
                "details":{
                    "line": data['capac_line'],
                    "date": data['capac_date'],
                    "time": data['capac_time'],
                    "capacity": data['capac_capacity'],
                    "user_id": "1"
                }
            }
            task = create_task(task_data)

            if task.status_code == 201:

                return True

        return False