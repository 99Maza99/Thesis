import cv2
from pyzbar.pyzbar import decode
import threading

class Scanner:
    def __init__(self, widgets=None, operation="Standby"):
        self.widgets = widgets if widgets else []
        self.operation = operation
        self.running = False
        self.camera_index = 0  # default to the first available camera

    def read_codes(self, frame):
        codes = decode(frame)
        for barcode in codes:
            code_data = barcode.data.decode('utf-8')
            data_type = barcode.type
            print("Scanned Data:", code_data)
            print("Data Type:", data_type)

            if self.operation == "entry":
                entrywidgets   = self.widgets[0:3]
                personelwidgets = self.widgets[4:]

                if data_type == "EAN13" and entrywidgets[0].get() == "":
                    print("1")
                    entrywidgets[0].insert(0,code_data)
                    
                
                if data_type == "QRCODE" and personelwidgets[0].get() =="":
                    print("2")
                    personelwidgets[0].insert(0,code_data)


    def start_scanning(self):
        camera = cv2.VideoCapture(self.camera_index)
        if not camera.isOpened():
            print(f"Failed to open camera index {self.camera_index}")
            return

        while self.running:
            ret, frame = camera.read()
            if ret:
                self.read_codes(frame)
            else:
                print("Failed to capture frame from camera.")
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on pressing 'q'
                break

        camera.release()
        cv2.destroyAllWindows()

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.start_scanning)
            self.thread.daemon = True
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()

    def update(self, widgets=None, operation=None):
        if widgets is not None:
            self.widgets = widgets
        if operation is not None:
            self.operation = operation

    def check_available_cameras(self):
        # This method checks all available cameras and returns the index of the first one that works
        index = 0
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.isOpened():
                cap.release()
                break
            cap.release()
            index += 1
        self.camera_index = index - 1 if index > 0 else 0
        print(f"Using camera index: {self.camera_index}")

