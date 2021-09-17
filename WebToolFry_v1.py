#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import mechanize
import wx
import wx.html as html

def tips():
	#provider = wx.CreateFileTipProvider("tips.txt", 0)
	#wx.ShowTip(None, provider, True)
	pass

def AyudaDef(event):
	description = """Software Libre diseniado Para
	tareas de Pentesting.
	"""
	licence = """
	GPL
	"""
	info = wx.AboutDialogInfo()
	info.SetIcon(wx.Icon('friky.png', wx.BITMAP_TYPE_PNG))
	info.SetName('WebToolFry')
	info.SetVersion('v1.0.0')
	info.SetDescription(description)
	info.SetCopyright('(C) FryProject 2015 Miguel Angel M.F. (Friky-X13)')
	#info.SetWebSite('')
	info.SetLicence(licence)
	info.AddDeveloper('FryProject(Miguel Angel M.F. (Friky-X13))')
	info.AddDocWriter("")	
	info.AddArtist('Miguel Angel M.F. (Friky-X13)')
	info.AddTranslator('Miguel Angel M.F. (Friky-X13)')
	wx.AboutBox(info)


class MostrarResultado(wx.Frame):
	def __init__(self,pagmoo):
		wx.Frame.__init__(self,None,-1,title=str(pagmoo.geturl()),pos=wx.Point(80,10),size=wx.Size(800, 500))
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		Guardarsm = wx.Menu()

		fileMenu.AppendSeparator()
		fileMenu2 = wx.Menu()
		fitema = fileMenu2.Append(1,'About')

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)


		fitem = fileMenu.Append(14,'Nuevo')
		fitem = fileMenu.Append(13,'Abrir pagina con WebCrawFry')
		fitem = fileMenu.Append(15,'Abrir pagina con FormFry')
		fileMenu.AppendSeparator()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)
		panel = wx.ScrolledWindow(self, -1)
		panel.SetScrollbars(1, 1, 900, 1000)

		htmlwin = html.HtmlWindow(panel, -1,size=wx.Size(900,1000),pos=wx.Point(0,0), style=wx.NO_BORDER)
		htmlwin.SetBackgroundColour(wx.RED)
		htmlwin.SetStandardFonts()
		htmlwin.SetPage(pagmoo.read())
		self.pagmoo = pagmoo.geturl()
		self.Show(True)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.Bind(wx.EVT_MENU,self.WCF , id=13)
		self.Bind(wx.EVT_MENU,self.FF , id=15)
		self.Bind(wx.EVT_MENU,self.Nuevo , id=14)
	def FF(self,event):FormFry1(self.pagmoo)
	def WCF(self,event):escanear(self.pagmoo)
	def Nuevo(self,event):
		entra = entrada()
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass

class FormFry1(wx.Frame):
	
	def __init__(self,page):
		wx.Frame.__init__(self,None,-1,title="FormFry GUI V1 Pag: ",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10))
		self.SetSize(wx.Size(500,700))
		panel = wx.ScrolledWindow(self, -1)
		panel.SetScrollbars(1, 1, 1500, 500)

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		Guardarsm = wx.Menu()

		fileMenu.AppendSeparator()
		fileMenu2 = wx.Menu()
		fitema = fileMenu2.Append(1,'About')

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)


		fitem = fileMenu.Append(14,'Nuevo')
		fitem = fileMenu.Append(13,'Reiniciar')
		fileMenu.AppendSeparator()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)


		self.metodos = []
		self.actions = []
		self.variables = []
		self.types = []
		self.valores = []
		self.activa = []
		i = 0
		punto = 50
		pag = urllib.request(page,"r")
		pagb = BeautifulSoup(pag,"html")
		br = mechanize.Browser()
		response = br.open(page)
		for form in br.forms():
			br.select_form(nr=i)
			self.variables.append([])
			self.types.append([])
			self.valores.append({})
			self.activa.append({})
			self.metodos.append(br.form.method)
			self.actions.append(br.form.action)
			i2 = 0
			wx.StaticText(panel, label="Formulario numero:"+str(i),pos=wx.Point(150,punto),size=wx.Size(200,40))
			punto+=50
			wx.StaticText(panel, label="Tipo:",pos=wx.Point(100,punto),size=wx.Size(100,40))
			wx.StaticText(panel, label="Nombre:",pos=wx.Point(200,punto),size=wx.Size(100,40))
			wx.StaticText(panel, label="Valor:",pos=wx.Point(300,punto),size=wx.Size(100,40))
			punto+=50
			
			for control in br.controls:

				self.variables[i].append(control.name)
				self.types[i].append(control.type)

				wx.StaticText(panel, label=str(control.type),pos=wx.Point(100,punto),size=wx.Size(100,40))
				wx.StaticText(panel, label=str(control.name),pos=wx.Point(200,punto),size=wx.Size(100,40))
				if "RadioControl" in str(control):
					listas = str(control).split("=[")
					listt = listas[-1].split("])>")
					listt = listt[0].split(", ")
					self.valores[i][control.name] = wx.ComboBox(panel, 26, pos=wx.Point(300,punto), size=wx.Size(100, 25), choices=listt)
				elif "CheckboxControl" in str(control):
					listas = str(control).split("=[")
					listt = listas[-1].split("])>")
					listt = listt[0].split(", ")
	#				print listt
					self.valores[i][control.name] = wx.ComboBox(panel, 26, pos=wx.Point(300,punto), size=wx.Size(100, 25), choices=listt)
				elif "SelectControl" in str(control):
#					print control
					listas = str(control).replace("*","").split("=[")
					listt = listas[-1].split("])>")
					listt = listt[0].split(", ")
					self.valores[i][control.name] = wx.ComboBox(panel, 26, pos=wx.Point(300,punto), size=wx.Size(100, 25), choices=listt)
				elif "HidenControl" in str(control):
					listas = str(control).split("=[")
					listt = listas[-1].split("])>")
					listt = listt[0].split(", ")
					self.valores[i][control.name] = wx.ComboBox(panel, 26, pos=wx.Point(300,punto), size=wx.Size(100, 25), choices=listt)
				elif "FileControl" in str(control):
					self.valores[i][control.name] =  wx.TextCtrl(panel,pos=wx.Point(300,punto),size=wx.Size(100,25))
					self.valores[i][control.name].SetValue(str(control.value))
				else:
					self.valores[i][control.name] =  wx.TextCtrl(panel,pos=wx.Point(300,punto),size=wx.Size(100,25))
					self.valores[i][control.name].SetValue(str(control.value))
				self.activa[i][control.name] = wx.CheckBox(panel, -1, 'Activar '+control.name, pos=wx.Point(409, punto))
				self.activa[i][control.name].SetValue(True)


				punto +=45

			punto+=10
			self.boton = wx.Button(panel,id= i,label="Enviar Variables",pos=wx.Point(200,punto),size=wx.Size(100,30))
			self.boton.Bind(wx.EVT_BUTTON,self.enviar, id=i)

			punto+=50
			i+=1

		panel.SetScrollbars(1, 1, 600, punto+200)
	
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.Bind(wx.EVT_MENU,self.Reiniciar , id=13)
		self.Bind(wx.EVT_MENU,self.Nuevo , id=14)
		self.Show(True)


	def enviar(self,event):
		
		#self.metodos.append(br.form.method)
		#self.actions.
		if self.metodos[event.GetId()]=="POST":
			cadena = {}
			for vari in self.variables[event.GetId()]:
				if self.activa[event.GetId()][vari].GetValue() == True:
					cadena[vari] = self.valores[event.GetId()][vari].GetValue()

			campos = urllib.urlencode(cadena)
			sitio = urllib.urlopen(self.actions[event.GetId()], campos)
			pagmoo = sitio
			MostrarResultado(pagmoo)

		elif self.metodos[event.GetId()]=="GET":
			cadena = u"?"
			for vari in self.variables[event.GetId()]:
				if self.activa[event.GetId()][vari].GetValue() == True:
					if cadena == "?":
						cadena += vari+"="+self.valores[event.GetId()][vari].GetValue().replace(" ","+")
					else:
						cadena += "&"+vari+"="+self.valores[event.GetId()][vari].GetValue().replace(" ","+")
			sitio = urllib.urlopen(self.actions[event.GetId()]+ cadena)
	#		print self.actions[event.GetId()]+ cadena
			
			pagmoo = sitio
			MostrarResultado(pagmoo)
			
		else:pass

	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass
	def Reiniciar(self,evt):
		dial = wx.MessageDialog(None, '¿Estas seguro de reiniciar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			entra = entrada()
			self.Destroy()
		else:
			pass
		
	def Nuevo(self,event):
		entra = entrada()

class vista1(wx.Frame):
	
	def __init__(self,paginaweb,enlaces,formsl,coments,enlacest,correl,numerot):
		self.paginaweb = paginaweb
		self.enlaces = enlaces
		self.formsl = formsl
		self.coments = coments
		self.enlacest = enlacest
		self.correl = correl
		self.numerot = numerot
		self.enlacestn = []
		girar = 0
		for enlare in self.enlaces:	
			self.enlacestn.append(enlacest[girar]+": "+enlare)
			
			girar +=1


		self.enlacesm = {}
		numc = 0
		for clave in self.enlacest:
			resul = str(self.enlaces[numc])	
			self.enlacesm[clave] = resul

			numc += 1


		wx.Frame.__init__(self,None,-1,title="WebCrawFry GUI V3.01 Pag: "+self.paginaweb,style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(1000,500))
	
		panel = wx.ScrolledWindow(self, -1)
		panel.SetScrollbars(1, 1, 1500, 500)

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		Guardarsm = wx.Menu()

		gcfi = Guardarsm.Append(2, 'Codigo Fuente')
		gcei = Guardarsm.Append(3, 'Comentarios Encontrados')
		gfei = Guardarsm.Append(4, 'Formularios Encontrados')
		gcoei = Guardarsm.Append(5, 'Correos Encontrados')
		gnei = Guardarsm.Append(6, 'Num. Tel. Encontrados')

		fim = fileMenu.AppendMenu(wx.ID_ANY, 'Guardar ...', Guardarsm)

		fileMenu.AppendSeparator()
		fileMenu2 = wx.Menu()
		fitema = fileMenu2.Append(1,'About')

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)
		self.Bind(wx.EVT_MENU,self.guardart , id=2)
		self.Bind(wx.EVT_MENU,self.guardart , id=3)
		self.Bind(wx.EVT_MENU,self.guardart , id=4)
		self.Bind(wx.EVT_MENU,self.guardart , id=5)
		self.Bind(wx.EVT_MENU,self.guardart , id=6)

		fitem = fileMenu.Append(14,'Nuevo')
		fitem = fileMenu.Append(13,'Reiniciar')
		fileMenu.AppendSeparator()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.Bind(wx.EVT_MENU,self.Reiniciar , id=13)
		self.Bind(wx.EVT_MENU,self.Nuevo , id=14)


		enlayvil = wx.StaticText(panel, label="Enlaces y Vistas: ",pos=wx.Point(70,100),size=wx.Size(150,30))
		self.enlacesmostrar = wx.ListBox(panel, 26, (50,150), (170, 130), self.enlacest, wx.LB_SINGLE)
		self.botonf = wx.Button(panel,id= -1,label="Abrir pagina en FormFry",pos=wx.Point(60,300),size=wx.Size(150,30))
		self.botonf.Bind(wx.EVT_BUTTON, self.fbus)

		coful = wx.StaticText(panel, label="Codigo Fuente: ",pos=wx.Point(400,50),size=wx.Size(150,30))
		self.cofu = wx.TextCtrl(panel, style=wx.TE_MULTILINE,pos=wx.Point(250,100),size=wx.Size(400,300))

		comel = wx.StaticText(panel, label="Comentarios encontrados: ",pos=wx.Point(700,50),size=wx.Size(200,30))
		self.come = wx.TextCtrl(panel, style=wx.TE_MULTILINE,pos=wx.Point(700,80),size=wx.Size(200,100))

		formsla = wx.StaticText(panel, label="Formularios encontrados: ",pos=wx.Point(700,200),size=wx.Size(200,30))
		self.formsp = wx.TextCtrl(panel, style=wx.TE_MULTILINE,pos=wx.Point(700,230),size=wx.Size(200,200))

		corr = wx.StaticText(panel, label="Correos encontrados:",pos=wx.Point(1000,50),size=wx.Size(300,30))
		self.corr = wx.TextCtrl(panel, style=wx.TE_MULTILINE,pos=wx.Point(930,80),size=wx.Size(300,100))

		nut = wx.StaticText(panel, label="Posibles numeros telefonicos encontrados:",pos=wx.Point(930,190),size=wx.Size(150,40))
		self.nut = wx.TextCtrl(panel, style=wx.TE_MULTILINE,pos=wx.Point(930,230),size=wx.Size(150,200))

		self.Show(True)
		self.Bind(wx.EVT_LISTBOX,self.MostrarCF)
		self.Bind(wx.EVT_CLOSE, self.SalirExit)
	def fbus(self,event):
		if "WebCrawFry" in str(self.GetTitle()): pass
		else: 
			pag = str(self.GetTitle()).replace("Enlace: ","")
			FormFry1(pag)
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass
	def guardart(self,event):

		openFileDialog = wx.FileDialog(self, "Guardar", "", "","Todos los Archivos (*)|*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		openFileDialog.ShowModal()
		archig = str(openFileDialog.GetPath())
		

		texts=""
		if event.GetId() == 2:
			textu = self.cofu.GetValue()
			texts=textu.encode("utf-8")
		elif event.GetId() == 3:
			textu = self.come.GetValue()
			texts=textu.encode("utf-8")
		elif event.GetId() == 4:
			textu = self.formsp.GetValue()
			texts=textu.encode("utf-8")
		elif event.GetId() == 5:
			textu = self.corr.GetValue()
			texts=textu.encode("utf-8")
		elif event.GetId() == 6:
			textu = self.nut.GetValue()
			texts=textu.encode("utf-8")

		archige = open(archig,"w")
		archige.writelines("<!--\t"+str(self.GetTitle())+"\t-->")
		archige.writelines("\n\n\n\n"+texts)
		archige.close()
		wx.MessageBox("Se a guardo con exito","Guardado",wx.YES_DEFAULT)

	def Reiniciar(self,evt):
		dial = wx.MessageDialog(None, '¿Estas seguro de reiniciar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			entra = entrada()
			self.Destroy()
		else:
			pass
		
	def Nuevo(self,event):
		entra = entrada()

	def MostrarCF(self,event):
		selec = event.GetSelection()
		pags = self.enlacest[selec]
		pags2 = self.enlacesm[pags]
		self.cofu.SetValue("")
		self.come.SetValue("")
		self.formsp.SetValue("")
		self.corr.SetValue("")
		self.nut.SetValue("")
		try:
			pagur = urllib.urlopen(pags2,"r")
			pagbb = str(BeautifulSoup(pagur,"html"))
			self.cofu.SetValue(pagbb)
			comag=""
			formag = ""
			comac = ""
			coman = ""
			for coml in self.coments[selec]:
				comag += "<!--"+coml+"-->\n"
			self.come.SetValue(comag)

			for correi in self.correl[selec]:
				comac += correi+"\n"
			self.corr.SetValue(comac)

			for nutt in self.numerot[selec]:
				coman += str(nutt)+"\n"
			self.nut.SetValue(coman)

			for forl in self.formsl[selec]:
				formag += forl+"\n\n\n"
			self.formsp.SetValue(formag)
			
			enlarer = self.enlaces[selec]
			
			self.SetTitle("Enlace: "+enlarer)

		except:
			pass
			#print "No"
			#print e
			wx.MessageBox("No se pudo abrir el enlace","ERROR",wx.YES_DEFAULT)

class escanear():
	enlaces = []
	formsl =  []
	coments = []
	enlacest =[]
	numeros = []
	correos = []
	imagess = []
	def buscoment(self,page,enlurl,nume,enlaces,formsl,coments):
		pag = urllib.request.urlopen(page,"r")
		pagb = BeautifulSoup(pag,"html")

		pagbs = str(pagb)

		pal=pagbs.split("<!--")
		for palo in pal:
			if "-->"in palo:
				pall = palo.split("-->")

				num = enlaces.index(enlurl)

				coments[num].append(str(pall[0]))
				
	def busform(self,page,enlurl,enlaces,formsl,coments):
		pag = urllib.request.urlopen(page,"r")
		pagb = BeautifulSoup(pag,"html")

		formus = pagb.find_all("form")
		for formc in formus:
			num = enlaces.index(enlurl)

			formsl[num].append(str(formc))


	def busmail(self,page,enlurl,nume,enlaces,formsl,coments,correl):
		pag = urllib.request.urlopen(page,"r")
		pagb = BeautifulSoup(pag,"html")

		pagbs = str(pagb)

		pal=pagbs.split(" ")
		for palo in pal:
			if "@"in palo:
				pat = palo.split("\n")
				for to in pat:
					if "@"in to:
						num = enlaces.index(enlurl)

						correl[num].append(to)

	def busima(self,page,enlurl,nume,enlaces,formsl,coments,imagess):
		pag = urllib.request.urlopen(page,"r")
		pagb = BeautifulSoup(pag,"html")
		img = pagb.find_all("img")
		for ima in img:
			num = enlaces.index(enlurl)
			imagess[num].append(ima)

	def busnume(self,page,enlurl,nume,enlaces,formsl,coments,correl,numerot):
		pag = urllib.request.urlopen(page,"r")
		pagb = BeautifulSoup(pag,"html")

		pagbs = str(pagb)

		pal=pagbs.split(" ")
		for palo in pal:
			pat = palo.split("\n")
			for pato in pat:
				if ("+51"in pato) or ("088"in pato) or ("+52"in pato) or ("55"in pato) or ("044"in pato):
					al = len(pato)
					if (al>7) and (al<15):
						try:
							patol = pato.replace("+","")
							numee = int(patol)
							num = enlaces.index(enlurl)
							numerot[num].append(pato)

						except :
							"""print "no se pudo"
							print e"""
							pass


	def buslink(self,page,enlaces,formsl,coments,enlacest):
		
		try:
			pag = urllib.urlopen(page,"r")
			pagb = BeautifulSoup(pag,"html")
			
			pagm=mechanize.Browser()
			pagmo = pagm.open(page)
			pagmo.read()
			for enlaces1 in pagm.links():
				
				for listar in enlaces:

					enlurl = enlaces1.url
					request = pagm.click_link(enlaces1)
					response=pagm.follow_link(enlaces1)

					if response.geturl() in enlaces:
						pass

					else:
						
						
						enlaces.append(response.geturl())
						enlacest.append(enlaces1.text)
						pagm.back()
					break
		
		except :
			#print e
			pass
	def __init__(self, paginaweb):
		
		enlaces =[]
		formsl = []
		coments =[]
		enlacest=[]
		enlacesy=[]
		numerot =[]
		correl = []
		imagess =[]

		
		paginaweb = paginaweb	
		enlaces.append(paginaweb)
		enlacest.append(paginaweb)
		seguir = True

		while seguir == True:
			page = paginaweb
			
			for lola in enlaces:
				
				page = lola
				self.buslink(page,enlaces,formsl,coments,enlacest)
									

			seguir = False

		nume = 0

		for enli in enlaces:
			page = enli
			formsl.append([])
			coments.append([])
			numerot.append([])
			correl.append([])
			imagess.append([])

			self.busform(page,enli,enlaces,formsl,coments)
			self.buscoment(page,enli,nume,enlaces,formsl,coments)
			self.busmail(page,enli,nume,enlaces,formsl,coments,correl)
			self.busnume(page,enli,nume,enlaces,formsl,coments,correl,numerot)
			self.busima(page,enli,nume,enlaces,formsl,coments,imagess)
			nume +=1
				
		vista1(paginaweb,enlaces,formsl,coments,enlacest,correl,numerot)

class fryin(wx.Frame):
	def __init__(self,st,st1):
		wx.Frame.__init__(self,None,-1,title="FryInclusion V1",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(850,500))
		pweb = str(st1)
		listab = str(st)
		abl = open(listab,"r").readlines()
		self.existee=[]
		self.noexist=[]
		self.existpr=[]
		self.ida = -10000000000
		panel = wx.ScrolledWindow(self, -1)
		panel.SetScrollbars(1, 1, 900, 500)
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		Guardarsm = wx.Menu()

		gcfi = Guardarsm.Append(200, 'Paginas Existentes')
		gcei = Guardarsm.Append(300, 'Paginas No Existentes')
		gfei = Guardarsm.Append(400, 'Paginas Redireccionadas')

		self.Bind(wx.EVT_MENU,self.guardart , id=200)
		self.Bind(wx.EVT_MENU,self.guardart , id=300)
		self.Bind(wx.EVT_MENU,self.guardart , id=400)

		fim = fileMenu.AppendMenu(wx.ID_ANY, 'Guardar ...', Guardarsm)

		fileMenu.AppendSeparator()
		fileMenu2 = wx.Menu()
		fitema = fileMenu2.Append(1,'About')

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)

		fitem = fileMenu.Append(14,'Nuevo')
		fitem = fileMenu.Append(13,'Reiniciar')
		fileMenu.AppendSeparator()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.Bind(wx.EVT_MENU,self.Reiniciar, id=13)
		self.Bind(wx.EVT_MENU,self.Nuevo , id=14)
		for palabra in abl:
			page = pweb.replace("#fry#",palabra).replace("\n","").replace("\t","")
			
			try:
				pagm=mechanize.Browser()
				pagmo = pagm.open(page)
				pagmo.read()
				if str(pagmo.geturl()) == page:
					self.existee.append("[+] Si existe "+page)
				else:
					self.existpr.append("[*] Pagina: "+page+", Redireccionada a: "+str(pagmo.geturl()))
			except:
				if("404" in str(e)):
					self.noexist.append("[-] No existe: "+page+" error:404")
				elif("not viewing" in str(e)):
					self.noexist.append("[-] No existe: "+page+" url incorrecto")
				else:
					self.noexist.append("[-] No existe: "+page+" error desconocido")

		self.pagmos = wx.StaticText(panel, label=" ",pos=wx.Point(300,50),size=wx.Size(300,40))
		

		nut = wx.StaticText(panel, label="[+] Paginas Existentes:",pos=wx.Point(80,100),size=wx.Size(150,40))
		self.enlacesmostrar = wx.ListBox(panel, 10, (50,150), (200, 130), self.existee, wx.LB_SINGLE)

		nut = wx.StaticText(panel, label="[*] Paginas Redireccionadas:",pos=wx.Point(320,100),size=wx.Size(150,40))
		self.enlacesmostrar = wx.ListBox(panel, 11, (300,150), (200, 130), self.existpr, wx.LB_SINGLE)

		nut = wx.StaticText(panel, label="[-] Paginas No Existentes:",pos=wx.Point(570,100),size=wx.Size(150,40))
		self.enlacesmostrar = wx.ListBox(panel, 26, (550,150), (200, 130), self.noexist, wx.LB_SINGLE)

		self.botona = wx.Button(panel,id= -1,label="Abrir en WebCrawFry la pagina seleccionada",pos=wx.Point(100,300),size=wx.Size(300,100))
		self.botonf = wx.Button(panel,id= -1,label="Abrir pagina en FormFry",pos=wx.Point(400,300),size=wx.Size(300,100))
		
		self.Show(True)
		self.botonf.Bind(wx.EVT_BUTTON, self.fbus)
		self.Bind(wx.EVT_CLOSE, self.SalirExit)
		self.botona.Bind(wx.EVT_BUTTON, self.AbPa)
		self.Bind(wx.EVT_LISTBOX,self.AbFr,id=10)
		self.Bind(wx.EVT_LISTBOX,self.AbRe,id=11)
		self.Bind(wx.EVT_LISTBOX,self.mostrarpag,id=26)

	def mostrarpag(self,event):
		selec = event.GetSelection()
		self.pagmos.SetLabel(self.noexist[selec])
		
	def guardart(self,event):
		root = Tk()
		root.geometry("00x00")
		root.state(newstate='withdraw')
		filename=asksaveasfilename(initialdir='c:\\',filetypes=[('Todos los archivos', '*')])
		archig=str(filename)
		texts=""
		if event.GetId() == 200:
			for textu in self.existee:
				texts+=textu.encode("utf-8")+"\n"

		elif event.GetId() == 400:
			for textu in self.existpr:
				texts+=textu.encode("utf-8")+"\n"

		elif event.GetId() == 300:
			for textu in self.noexist:
				texts+=textu.encode("utf-8")+"\n"

		archige = open(archig,"w")
		archige.writelines("<!--\t"+str(self.GetTitle())+"\t-->")
		archige.writelines("\n\n\n\n"+texts)
		archige.close()
		wx.MessageBox("Se a guardo con exito","Guardado",wx.YES_DEFAULT)
	
	def fbus(self,event):
		if (self.ida != -10000000000):
			selec = self.existee[self.ida]
			if "[+] Si existe " in selec:
				FormFry1(selec.replace("[+] Si existe ",""))
			elif "[*] Redireccionada " in selec:
				lol = selec.split("Redireccionada a: ")
				FormFry1(lol[1])

	def AbPa(self,event):
		if (self.ida != -10000000000):
			selec = self.existee[self.ida]
			if "[+] Si existe " in selec:
				escanear(selec.replace("[+] Si existe ",""))
			elif "[*] Redireccionada " in selec:
				lol = selec.split("Redireccionada a: ")
				escanear(lol[1])
		else:
			wx.MessageBox("Por favor selecciona un elemento de la lista de paginas existentes o de paginas redireccionadas.","ERROR",wx.YES_DEFAULT)
	def AbRe(self,event):
		selec = event.GetSelection()
		self.ida = selec
		self.pagmos.SetLabel(self.existpr[selec])
	def AbFr(self,event):
		selec = event.GetSelection()
		self.ida = selec
		self.pagmos.SetLabel(self.existee[selec])
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass
	def Reiniciar(self,evt):
		dial = wx.MessageDialog(None, '¿Estas seguro de reiniciar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			entra = entrada()
			self.Destroy()
		else:
			pass
		
	def Nuevo(self,event):
		entra = entrada()

class entrada(wx.Frame):
	def __init__(self):	

		wx.Frame.__init__(self,None,-1,title="WebToolFry GUI V1.0",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(500,300))
		self.cab = 0
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileMenu2 = wx.Menu()
		fileMenu3 = wx.Menu()
		
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		menubar.Append(fileMenu, '&Archivo')
		fileMenu3.Append(4,'FormFry')
		fileMenu3.Append(2, 'FryInclusion')
		menubar.Append(fileMenu3, "Herramientas")
		fitema = fileMenu2.Append(1,'About')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)
		self.Bind(wx.EVT_MENU,self.finc , id=2)
		self.Bind(wx.EVT_MENU,self.wcf , id=3)
		self.Bind(wx.EVT_MENU,self.formf , id=4)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.scroll = wx.ScrolledWindow(self, -1)
		self.scroll.SetScrollbars(1, 1, 600, 400)

		self.pagl = wx.StaticText(self.scroll, label="Pagina Web: ",pos=wx.Point(50,60),size=wx.Size(100,30))
		self.tc3 = wx.TextCtrl(self.scroll,pos=wx.Point(150,60),size=wx.Size(100,20))

		self.botone = wx.Button(self.scroll,id= -1,label="Escanear",
		pos=wx.Point(150,118),size=wx.Size(70,30))
		self.botone.Bind(wx.EVT_BUTTON, self.OnEs)
		self.Show(True)

	def formf(self,event):
		pga = self.tc3.GetValue()
		formfryc(pga)
		self.Destroy()
	def finc(self,event):
		pga = self.tc3.GetValue()
		fryinc(pga)
		self.Destroy()
	def wcf(self,event):
		pga = self.tc3.GetValue()
		webcrawc(pga)
		self.Destroy()

	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass
	
	def OnEs(self,event):
		st = str(self.tc3.GetValue())
		if ((st==None)|(st=="\n")|(st==" ")|(st=="\t")|(st=="\n\n")|(st=="\n\n\n")|(st=="")):
			
			wx.MessageBox("Por favor llena el campo","ERROR",wx.YES_DEFAULT)
		else:
			paginaweb = st
			escanear(paginaweb)
			self.Close()

class formfryc(wx.Frame):
	def __init__(self,pga):	

		wx.Frame.__init__(self,None,-1,title="FormFry",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(500,300))
		self.cab = 0
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileMenu2 = wx.Menu()
		fileMenu3 = wx.Menu()
		
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		menubar.Append(fileMenu, '&Archivo')
		fileMenu3.Append(3,'WebCrawFry')
		fileMenu3.Append(2, 'FryInclusion')
		menubar.Append(fileMenu3, "Herramientas")
		fitema = fileMenu2.Append(1,'About')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)
		self.Bind(wx.EVT_MENU,self.finc , id=2)
		self.Bind(wx.EVT_MENU,self.wcf , id=3)
		self.Bind(wx.EVT_MENU,self.formf , id=4)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.scroll = wx.ScrolledWindow(self, -1)
		self.scroll.SetScrollbars(1, 1, 600, 400)

		self.pagl = wx.StaticText(self.scroll, label="Pagina Web: ",pos=wx.Point(50,60),size=wx.Size(100,30))
		self.botont = wx.Button(self.scroll,id= -1,label="Buscar",pos=wx.Point(150,118),size=wx.Size(70,30))
		self.tc3 = wx.TextCtrl(self.scroll,pos=wx.Point(150,60),size=wx.Size(100,20))
		self.tc3.SetValue(pga)
		self.botont.Bind(wx.EVT_BUTTON, self.FryForm)
		self.Show(True)

	def formf(self,event):
		pga = self.tc3.GetValue()
		formfryc(pga)
		self.Destroy()
	def finc(self,event):
		pga = self.tc3.GetValue()
		fryinc(pga)
		self.Destroy()
	def wcf(self,event):
		pga = self.tc3.GetValue()
		webcrawc(pga)
		self.Destroy()


	def FryForm(self,event):
		pg = self.tc3.GetValue()
		if (pg == ""):
			wx.MessageBox("Por favor llena el campo de la pag web","ERROR",wx.YES_DEFAULT)
		else:
			self.Destroy()
			FormFry1(pg)
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass

class fryinc(wx.Frame):
	def __init__(self,pga):	

		wx.Frame.__init__(self,None,-1,title="FryInclusion",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(500,300))
		self.cab = 0
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileMenu2 = wx.Menu()
		fileMenu3 = wx.Menu()
		
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		menubar.Append(fileMenu, '&Archivo')
		fileMenu3.Append(3,'WebCrawFry')
		fileMenu3.Append(4, 'FormFry')
		menubar.Append(fileMenu3, "Herramientas")
		fitema = fileMenu2.Append(1,'About')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)
		self.Bind(wx.EVT_MENU,self.finc , id=2)
		self.Bind(wx.EVT_MENU,self.wcf , id=3)
		self.Bind(wx.EVT_MENU,self.formf , id=4)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.scroll = wx.ScrolledWindow(self, -1)
		self.scroll.SetScrollbars(1, 1, 600, 400)
		
		self.pagl = wx.StaticText(self.scroll, label="Pagina Web: ",pos=wx.Point(50,60),size=wx.Size(100,30))
		self.tc3 = wx.TextCtrl(self.scroll,pos=wx.Point(150,60),size=wx.Size(100,20))
		self.pagt = wx.StaticText(self.scroll, label="Lista:",pos=wx.Point(50,100),size=wx.Size(100,30))
		self.listaa = wx.TextCtrl(self.scroll,pos=wx.Point(150,100),size=wx.Size(100,20))
		self.botona = wx.Button(self.scroll,id= -1,label="...",pos=wx.Point(250,100),size=wx.Size(20,20))
		self.botonf = wx.Button(self.scroll,id= -1,label="Buscar",pos=wx.Point(150,140),size=wx.Size(70,30))
		self.tc3.SetValue(pga)
		
		self.botona.Bind(wx.EVT_BUTTON, self.abrir)
		self.botonf.Bind(wx.EVT_BUTTON, self.fiin)
		self.Show(True)


	def formf(self,event):
		pga = self.tc3.GetValue()
		formfryc(pga)
		self.Destroy()
	def finc(self,event):
		pga = self.tc3.GetValue()
		fryinc(pga)
		self.Destroy()
	def wcf(self,event):
		pga = self.tc3.GetValue()
		webcrawc(pga)
		self.Destroy()
	def abrir(self,event):
		openFileDialog = wx.FileDialog(self, "Abrir", "", "","Todos los archivos (*)|*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()
		archivoa = str(openFileDialog.GetPath())
		self.listaa.SetValue(archivoa)


	def fiin(self,event):
			st = self.listaa.GetValue()
			st1 = self.tc3.GetValue()
			if  ((st==None)|(st=="\n")|(st==" ")|(st=="\t")|(st=="\n\n")|(st=="\n\n\n")|(st=="")):
				wx.MessageBox("Por favor llena el campo de la lista","ERROR",wx.YES_DEFAULT)
			elif  ((st1==None)|(st1=="\n")|(st1==" ")|(st1=="\t")|(st1=="\n\n")|(st1=="\n\n\n")|(st1=="")):
				wx.MessageBox("Por favor llena el campo de la pag web","ERROR",wx.YES_DEFAULT)
			else:
				if("#fry#" not in st1):
					wx.MessageBox("Por favor especifica la o las partes que incluiran la palabra con un #fry#","ERROR",wx.YES_DEFAULT)
				else:
					self.Destroy()
					fryin(st,st1)
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass

class webcrawc(wx.Frame):
	def __init__(self,pga):	

		wx.Frame.__init__(self,None,-1,title="WebCrawFry",style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER 
			| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,pos=wx.Point(80,10),size=wx.Size(500,300))
		self.cab = 0
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileMenu2 = wx.Menu()
		fileMenu3 = wx.Menu()
		
		fitem = fileMenu.Append(wx.ID_EXIT, 'Salir')
		menubar.Append(fileMenu, '&Archivo')
		fileMenu3.Append(4,'FormFry')
		fileMenu3.Append(2, 'FryInclusion')
		menubar.Append(fileMenu3, "Herramientas")
		fitema = fileMenu2.Append(1,'About')
		menubar.Append(fileMenu2, 'Ayuda')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU,AyudaDef , id=1)
		self.Bind(wx.EVT_MENU,self.finc , id=2)
		self.Bind(wx.EVT_MENU,self.wcf , id=3)
		self.Bind(wx.EVT_MENU,self.formf , id=4)
		self.Bind(wx.EVT_MENU,self.SalirExit , id=wx.ID_EXIT)
		self.scroll = wx.ScrolledWindow(self, -1)
		self.scroll.SetScrollbars(1, 1, 600, 400)
		
		self.pagl = wx.StaticText(self.scroll, label="Pagina Web: ",pos=wx.Point(50,60),size=wx.Size(100,30))
		self.tc3 = wx.TextCtrl(self.scroll,pos=wx.Point(150,60),size=wx.Size(100,20))
		self.botone = wx.Button(self.scroll,id= -1,label="Escanear",pos=wx.Point(150,118),size=wx.Size(70,30))
		self.tc3.SetValue(pga)
		
		self.botone.Bind(wx.EVT_BUTTON, self.OnEs)
		self.Show(True)

	def formf(self,event):
		pga = self.tc3.GetValue()
		formfryc(pga)
		self.Destroy()
	def finc(self,event):
		pga = self.tc3.GetValue()
		fryinc(pga)
		self.Destroy()
	def wcf(self,event):
		pga = self.tc3.GetValue()
		webcrawc(pga)
		self.Destroy()

	def OnEs(self,event):
		st = str(self.tc3.GetValue())
		if ((st==None)|(st=="\n")|(st==" ")|(st=="\t")|(st=="\n\n")|(st=="\n\n\n")|(st=="")):
			
			wx.MessageBox("Por favor llena el campo","ERROR",wx.YES_DEFAULT)
		else:
			paginaweb = st
			escanear(paginaweb)
			self.Close()
	def SalirExit(self,event):
		dial = wx.MessageDialog(None, '¿Estas seguro de cerrar el programa?', 'salir',
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			pass


app = wx.App()
entra = entrada()
tips()
app.MainLoop()