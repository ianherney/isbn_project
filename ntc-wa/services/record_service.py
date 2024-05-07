from consumers.ag.record_consumer import *

class RecordService:
    
    @staticmethod
    def create_record(user_company, user_line, capac_id, capac_line, capac_date, capac_time, capac_capacity):

        data = {
            "user_company": user_company,
            "user_line": user_line,
            "capac_id": capac_id,
            "capac_line": capac_line,
            "capac_date": capac_date,
            "capac_time": capac_time,
            "capac_capacity": capac_capacity,
        }

        return create_record(data)