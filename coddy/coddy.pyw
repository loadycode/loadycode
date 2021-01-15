import tkinter as tk;import tkinter.filedialog as fd
try:from ctypes import windll
except ImportError:pass
filetypes=[("all filetypes","*"),("plain text (.txt)","*.txt"),("markdown (.md)","*.md"),("xml (.xml)","*.xml"),("json (.json)","*.json"),("python (.py)","*.py"),("html (.html)","*.html"),("javascript (.js)","*.js"),("java (.java)","*.java"),("php (.php)","*.php"),("c language (.c)","*.c"),("c++ (.cpp)","*.cpp"),("c/c++ headers (.h)","*.h")];edited=False;openfile=None
def editevent(event):
	global edited,linesLabel,lines;edited=True;lines=textbox.get("1.0","end").split("\n")
	if lines.index("")==1:linesLabel["text"]="1 line"
	else:linesLabel["text"]=str(lines.index(""))+" lines"
	if openfile==None:tilelabel["text"]="# untitled "+str(separator)+" coddy"
	elif openfile!=None:tilelabel["text"]="# "+str(openfile)+" "+str(separator)+" coddy"
def newfile(event):
	global edited;global openfile
	def oldsave(event):
		global filetypes,openfile,edited;edited=False
		if openfile!=None:open(openfile,"wt").write(textbox.get("1.0","end"))
		elif openfile=="coddyconf":open("coddyconf","wt").write(textbox.get("1.0","end"))
		else:
			openfile=fd.SaveAs(window,filetypes=filetypes).show()
			if openfile=="":return
			open(openfile,"wt").write(textbox.get("1.0","end"))
		checkconf();textbox.delete("1.0","end");tilelabel["text"]="untitled "+str(separator)+" coddy";dialog.destroy();linesLabel["text"]="1 line";openfile=None
	def oldclose(event):
		global edited;edited=False
		textbox.delete("1.0","end");tilelabel["text"]="untitled "+str(separator)+" coddy";dialog.destroy();linesLabel["text"]="1 line";openfile=None
	if edited==True:
		dialog=tk.Frame(window,bg="white",height=20);dialog.pack(side="bottom",fill="x")
		if openfile!=None:dialoglabel=tk.Label(dialog,bg="white",text=openfile+" had unsaved changes").pack(side="left")
		else:dialoglabel=tk.Label(dialog,bg="white",text="untitled file had unsaved changes").pack(side="left")
		savebtn=tk.Label(dialog,text="save",bg="white");dontsavebtn=tk.Label(dialog,text="don't save",bg="white");savebtn.bind("<Button-1>",oldsave);dontsavebtn.bind("<Button-1>",oldclose);savebtn.pack(side="right",padx=10);dontsavebtn.pack(side="right",padx=10)
	else:textbox.delete("1.0","end");tilelabel["text"]="untitled "+str(separator)+" coddy";openfile=None
def openfunc(event):
	global filetypes,openfile,edited;openfile=fd.Open(window,filetypes=filetypes).show()
	if openfile=="":return
	textbox.delete("1.0","end");textbox.insert("1.0",open(openfile).read());tilelabel["text"]=str(openfile)+" "+str(separator)+" coddy";lines=textbox.get("1.0","end").split("\n")
	if lines.index("")==1:linesLabel["text"]="1 line"
	else:linesLabel["text"]=str(lines.index(""))+" lines"
def savefunc(event):
	global filetypes,openfile,edited
	if openfile!=None:open(openfile,"wt").write(textbox.get("1.0","end"));tilelabel["text"]=openfile+" "+separator+" coddy"
	elif openfile=="coddyconf":open("coddyconf","wt").write(textbox.get("1.0","end"));tilelabel["text"]=openfile+" "+separator+" coddy"
	else:
		openfile=fd.SaveAs(window,filetypes=filetypes).show()
		if openfile=="":return
		open(openfile,"wt").write(textbox.get("1.0","end"));tilelabel["text"]=openfile+" "+separator+" coddy"
	lines=textbox.get("1.0","end").split("\n");edited=False
	if lines.index("")==1:linesLabel["text"]="1 line"
	else:linesLabel["text"]=str(lines.index(""))+" lines"
def saveasfunc(event):
	global filetypes,openfile,edited;openfile=fd.SaveAs(window,filetypes=filetypes).show()
	if openfile=="":return
	open(openfile,"wt").write(textbox.get("1.0","end"));tilelabel["text"]=openfile+" "+separator+" coddy";edited=False
def exitfunc(event):window.destroy()
default_bg="#444444";default_fg="white";default_panel="silver";default_cursor="orange";default_font="Consolas 10";default_side="silver";default_side_fg="black";default_panel_fg="black";separator="-";icon="icon.ico";sideshow="False";panelshow="True"
def settings(event):global window,openfile;openfile="coddyconf";textbox.delete("1.0","end");textbox.insert("1.0",open("coddyconf").read());tilelabel["text"]=openfile+" "+separator+" coddy"
def checkconf():
	global textbox,panel,side,separator,icon,sideshow,panelshow;conf=open("coddyconf").read();confarray=conf.split("\n");textbox["bg"]=confarray[1];textbox["fg"]=confarray[3];panel["bg"]=confarray[5];textbox["insertbackground"]=confarray[7];textbox["font"]=confarray[9];side["bg"]=confarray[11];side["fg"]=confarray[13];openbtn["fg"]=confarray[15];savebtn["fg"]=confarray[15];saveasbtn["fg"]=confarray[15];settingsbtn["fg"]=confarray[15];linesLabel["fg"]=confarray[15];separator=confarray[17];icon=confarray[19];sideshow=confarray[21];panelshow=confarray[23]
	if sideshow=="False":side.destroy()
	if panelshow=="False":panel.destroy()
def set_appwindow(window):GWL_EXSTYLE=-20;WS_EX_APPWINDOW=0x00040000;WS_EX_TOOLWINDOW=0x00000080;hwnd=windll.user32.GetParent(window.winfo_id());stylew=windll.user32.GetWindowLongW(hwnd,GWL_EXSTYLE);stylew=stylew&~WS_EX_TOOLWINDOW;stylew=stylew|WS_EX_APPWINDOW;res=windll.user32.SetWindowLongW(hwnd,GWL_EXSTYLE,stylew);window.wm_withdraw();window.after(10,lambda:window.wm_deiconify())
def mapped(event):
	global isMapped;window.overrideredirect(True);window.call("wm","iconphoto",window._w,iconimg);window.iconphoto(True,iconimg)
	if isMapped==1:set_appwindow(window);isMapped=0
isMapped=0;isMaximised=False;window=tk.Tk();window.title("coddy");window.bind("<Map>",mapped);window.overrideredirect(True);screenwidth=window.winfo_screenwidth();screenheight=window.winfo_screenheight();xcoor=(screenwidth/2)-(600/2);ycoor=(screenheight/2)-(400/2);window.minsize(width=600,height=450)
def close(event):window.destroy()
def minimise(event):global isMapped;window.state('withdrawn');window.overrideredirect(False);window.state('iconic');isMapped=1
def maximise(event):
	global isMaximised
	if isMaximised==False:window.geometry("{}x{}+{}+{}".format(window.winfo_screenwidth(),window.winfo_screenheight(),0,0));isMaximised=True
	else:window.geometry("{}x{}+{}+{}".format(600,400,int(xcoor),int(ycoor)));isMaximised=False	
def clickpos(event):global clickx,clicky;clickx=event.x;clicky=event.y
def moving(event):x,y=event.x-clickx+window.winfo_x(),event.y-clicky+window.winfo_y();window.geometry("+%s+%s"%(x,y))
tile=tk.Frame(window,height=40,bg="white");tile.bind("<B1-Motion>",moving);tile.bind("<Button-1>",clickpos);tile.pack(side="top",fill="x");iconimg=tk.PhotoImage(file="icons/logo.png");icon=tk.Button(tile,image=iconimg,relief="flat",width=23,height=23,borderwidth=0);icon.pack(side="left");tilelabel=tk.Label(tile,text="coddy",justify="center",bg="white",font="Consolas 10");tilelabel.bind("<B1-Motion>",moving);tilelabel.bind("<Button-1>",clickpos);tilelabel.pack(side="left");tileclose=tk.Frame(tile,height=25,width=25,bg="red");tileclose.bind("<Button-1>",close);tileclose.pack(side="right");tilemax=tk.Frame(tile,height=25,width=25,bg="green");tilemax.bind("<Button-1>",maximise);tilemax.pack(side="right");tilemin=tk.Frame(tile,height=25,width=25,bg="blue");tilemin.bind("<Button-1>",minimise);tilemin.pack(side="right");side=tk.Label(window,bg="white",fg=default_side_fg,anchor="n",font=default_font);side.pack(side="left",fill="y")
for x in range(1,40):side["text"]+=str(x)+"\n"
verScroll=tk.Scrollbar(window,relief="flat",width=25);verScroll.pack(side="right",fill="y");horScroll=tk.Scrollbar(window,relief="flat",orient="horizontal");horScroll.pack(side="bottom",fill="x");textbox=tk.Text(window,undo=True,relief="flat",wrap="none",bg=default_bg,fg=default_fg,font=default_font,insertbackground=default_cursor);textbox["yscrollcommand"]=verScroll.set;textbox["xscrollcommand"]=horScroll.set;verScroll["command"]=textbox.yview;horScroll["command"]=textbox.xview;textbox.pack(side="top",fill="both",expand=1);panel=tk.Frame(window,bg=default_panel,height=50);panel.pack(side="bottom",fill="x");openbtn=tk.Label(panel,bg=default_panel,fg=default_panel_fg,text="open");openbtn.pack(side="left",padx=2);openbtn.bind("<Button-1>",openfunc);savebtn=tk.Label(panel,bg=default_panel,fg=default_panel_fg,text="save");savebtn.pack(side="left",padx=2);savebtn.bind("<Button-1>",savefunc);saveasbtn=tk.Label(panel,bg=default_panel,fg=default_panel_fg,text="save as");saveasbtn.pack(side="left",padx=2);saveasbtn.bind("<Button-1>",saveasfunc);settingsbtn=tk.Label(panel,bg=default_panel,fg=default_panel_fg,text="settings");settingsbtn.bind("<Button-1>",settings);settingsbtn.pack(side="left",padx=2);linesLabel=tk.Label(panel,bg=default_panel,fg=default_panel_fg,text="start page");linesLabel.pack(side="right",padx=2);window.bind("<Control-n>",newfile);window.bind("<Control-o>",openfunc);window.bind("<Control-s>",savefunc);window.bind("<Control-Alt-s>",saveasfunc);window.bind("<Control-p>",settings);window.bind("<Control-q>",exitfunc);bindnum=0
while(bindnum!=36):chars=["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"];window.bind(chars[bindnum],editevent);bindnum+=1
checkconf();textbox.insert("1.0",open("launch").read());minimise(1);window.geometry("{}x{}+{}+{}".format(600,400,int(xcoor),int(ycoor)));mapped(1);window.mainloop()