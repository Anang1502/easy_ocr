from locust import HttpUser, TaskSet, task, between
import PyPDF2


# class UserBehavior(HttpUser):
#     wait_time = between(1, 5)
#
#     @task(1)
#     def model(self):
#         # self.client.get('http://192.168.10.3:5000/are_dinosaurs_real')        url = "http://192.168.10.3:5000/api/v1/getText"        document = "D:/SF-ocr/A-Z-Alphabet-Book-and-1-10.pdf"
#         files = {'file': open(document, 'rb')}
#         # params = {"Language": "eng", "ProcessImage": "true"}
#         self.client.post(url, files=files, data=params)
#
#         # self.client.post('http://192.168.10.3:5000/api/v1/getText', 'C:/Users/Tejaswini/Downloads/file-sample_100kB')        #self.client.post('http://192.168.10.3:5000/api/v1/keywords', '/D:/SF-ocr/A-Z-Alphabet-Book-and-1-10.pdf')        #self.client.post('http://192.168.10.3:5000/api/v1/upload', 'D:/SF-ocr/Untitled')        #C:/Users/Tejaswini/Downloads/170932_Kjøpekontrakt (1)
#         # C:/Users/Tejaswini/Downloads/file-sample_100kB

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def model(self):
        url1 = "http://localhost:5006/apidocs/#/Process_File/post_api_v1_process_file"
        # url = "http://192.168.0.48:5000/api/v1/upload"
        # document = "D:/cl_test/2019-06-12 Pristilbud Grenland Hage og Landskap.pdf"
        document1 = "C:/Users/Anang Raj/Downloads/pdfs/Nevigate_data/Nevigate_data/purchase_order/HK-PO217026_DellHK-HK-PO217026"
        files = {'file': open(document1, 'rb')}
        params = {"CustomerId": "988D5BD4-1B98-46C6-B00D-38868B42E218", "BotId": "178F295C-E115-4788-91F2-DDD0ECEC0B50"}
        self.client.post(url1, files=files, data=params)
