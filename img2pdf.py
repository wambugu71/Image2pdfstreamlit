import  streamlit as  st
from PIL  import Image
from pathlib import  Path
import  time

class  Wambugu_Image2Pdf(object):
    def  __init__(self,*args,**kwargs):
        super(Wambugu_Image2Pdf, self).__init__()
        self.uploads = None
        self.images = None
        self.filename = None
        self.firstimage = None
        self.myimages = None
        self.pdf_path = None

    def  run(self):
        self.uploads = st.file_uploader("Choose your image  files to convert:",accept_multiple_files = True)
        if  self.uploads !=None:
            try:
                self.images = [Image.open(image) for  image in self.uploads]
                self.firstimage = self.images[0]
                self.pdf_path = Path("output.pdf")
                self.firstimage.save(self.pdf_path.with_suffix('.pdf'), save_all=True, append_images=self.images[1:])
                time.sleep(3)
                with open("output.pdf", "rb")  as  f:
                    st.write("pdf complete:")
                    st.download_button(label="Download", file_name="output.pdf", data = f)
            except:
                st.info("Choose  the  images  to convert to pdf")


App = Wambugu_Image2Pdf()
App.run()






