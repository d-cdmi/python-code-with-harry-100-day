from tkinter import *
from tkinter import messagebox
import requests
import json
type = 'game'
apiKey = '022929025e4e4602bc2466dc8ddf1732'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey


class NewsApp:
	global apiKey, type

	def __init__(self, root):
		self.root = root
		self.root.geometry('1350x700+0+0')
		self.root.title("eNewsPaper")

		#====variables========#
		self.newsCatButton = []
		self.newsCat = ["general", "entertainment",
						"business", "sports", "technology", "health"]

		#========title frame===========#
		bg_color = "#404040"
		text_area_bg = "#b8e0c4"
		basic_font_color = "#ccc4c4"
		title = Label(self.root, text="NewsPaper Software", font=("times new roman", 30, "bold"),
					pady=2, bd=12, relief=GROOVE, bg=bg_color, fg=basic_font_color).pack(fill=X)

		F1 = LabelFrame(self.root, text="Category", font=(
			"times new roman", 20, "bold"), bg=bg_color, fg=basic_font_color, bd=10, relief=GROOVE)
		F1.place(x=0, y=80, width=300, relheight=0.88)
		
a = NewsApp(root)
a.__init__()