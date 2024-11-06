#command to run before starting:
# pip install qrcode
# pip install Pillow

#You can make multiple virtual environments in 1 project (venv)
#This is done by (going to the right directory and) running the following code:
# python -m venv venv1   
# source venv1/bin/activate  

# You can stop using it with the following command:
# deactivate

#Later you can use the following command to run the code:
# d:/Projects/Python/Python_SmallProjects/Util/QRCodeGenerator/venv1/Scripts/python.exe d:/Projects/Python/Python_SmallProjects/Util/QRCodeGenerator/QRCodeGenerator.py


import qrcode

class MyQR:
    """A class that simplifies the creation of QR Codes"""

    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        """
        Creates a qr code with some user customization

        :param file_name: The name/path of your qr code
        :param fg: The foreground colour
        :param bg: The background colour
        :return: None
        """
        # Get the user input
        user_input: str = input ('Enter text: ')

        try:
            # Add the user input to the qr code and create it
            self.qr.add_data(user_input)
            qr_image=self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            # Display that it was successfully done
            print(f'Successfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')

def main_QRCodeGen():
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr('sample.png', fg='black',bg='white')

if __name__ == '__main__':
    main_QRCodeGen()

# Improvements:
#   - Save the qr code with a user chosen name