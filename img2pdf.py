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
        st.markdown('''
<html>
<head>
  <style>
    .card {
      background-color: #f2f2f2;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      width: 400px;
      margin: 0 auto;
      text-align: center;
    }

    .card-header {
      padding: 20px;
    }

    h1 {
      color: #333;
      font-size: 32px;
      font-family  : fantasy;
      margin: 0;
    }

    p1 {
      color: #777;
      font-size: 18px;
      font-family: cursive;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="card-header">
      <h1>Image to PDF</h1>
      <p1><i>Convert  your  images  to pdf  easily</i></p1>
    </div>
  </div>
</body>
</html>
        ''', unsafe_allow_html=True)
        self.uploads = st.file_uploader("Choose your image  files to convert:",accept_multiple_files = True)
        if  self.uploads !=None:
            try:
                with st.spinner("Processing your files...."):
                    self.images = [Image.open(image) for  image in self.uploads]
                    self.firstimage = self.images[0]
                    self.pdf_path = Path("output.pdf")
                    self.firstimage.save(self.pdf_path.with_suffix('.pdf'), save_all=True, append_images=self.images[1:])
                #with st.spinner("Processing your files"):
                    time.sleep(3)
                st.success("Done")
                with open("output.pdf", "rb")  as  f:
                   # st.write("pdf complete:")
                    st.download_button(label="Download", file_name="output.pdf", data = f)
            except:
                st.info("Choose  the  images  to convert to pdf")

            st.markdown('''
<footer style="background-color: white; padding: 20px; text-align: left;">
    <p style="font-size: 14px; color: #666; margin-bottom: 0; font-family:Chilanka;">Developer: k. wambugu </p>
</footer>
''', unsafe_allow_html = True)


App = Wambugu_Image2Pdf()
App.run()






