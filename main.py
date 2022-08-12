import streamlit as st
import pandas as pd
import backend

import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

class FileDownloader(object):
	# utility class for be able to download the processed file
	
	def __init__(self, data,filename='myfile',file_ext='txt'):
		super(FileDownloader, self).__init__()
		self.data = data
		self.filename = filename
		self.file_ext = file_ext

	def download(self):
		b64 = base64.b64encode(self.data.encode()).decode()
		new_filename = "{}_{}_.{}".format(self.filename,timestr,self.file_ext)
		st.markdown("#### Download File ###")
		href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
		st.markdown(href,unsafe_allow_html=True)



def main():
	st.title("PS Handle")

	# streamlit menu for sidebar selection
	menu = ["excel", "csv"]
	choice = st.sidebar.selectbox("Menu",menu)

	# condition based content
	if choice == "excel":
		st.subheader("excel")
		data_file = st.file_uploader("Upload excel",type=["xlsx"])

		if data_file is not None:
			df = pd.read_excel(data_file)
			convertedData = backend.processExcel(df)
			download = FileDownloader(df.to_csv(), 'converted', file_ext='xlsx').download()
			# st.write(type(data_file))
			# file_details = {"filename":data_file.name, "filetype":data_file.type,
            #                 "filesize":data_file.size}
			# st.write(file_details)
			# df = pd.read_excel(data_file)
			# st.dataframe(df)
			# print(convertedData)

	elif choice == "csv":
		st.subheader("csv")
        

if __name__ == '__main__':
	main()
