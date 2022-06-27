# importons les librairies a utiliser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

# création d'une classe de fenêtre principale
class MainWindow(QMainWindow):

	# definir un constructeur
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)


		# création d'un QWebEngineView
		self.browser = QWebEngineView()

		# réglons l'url par defaut 
		self.browser.setUrl(QUrl("https://christiandev.pythonanywhere.com/"))

		# ajouter une action lorsque l'URL est modifiée
		self.browser.urlChanged.connect(self.update_urlbar)

		# ajout d'une action lorsque le chargement est terminé
		self.browser.loadFinished.connect(self.update_title)

		# définir ce navigateur comme widget central ou fenêtre principale
		self.setCentralWidget(self.browser)

		# création d'un objet barre d'état
		self.status = QStatusBar()

		# ajout de la barre d'état à la fenêtre principale
		self.setStatusBar(self.status)

		# création de QToolBar pour la navigation
		navtb = QToolBar("Navigation")

		# ajouter cette barre d'outils à la fenêtre principale
		self.addToolBar(navtb)

		# ajouter des actions à la barre d'outils
		# création d'une action pour le dos
		back_btn = QAction("Back", self)

		# conseil d'état de réglage
		back_btn.setStatusTip("Back to previous page")

		# ajouter une action au bouton de retour
		# faire revenir le navigateur en arrière
		back_btn.triggered.connect(self.browser.back)

		# ajouter cette action à la barre d'outils
		navtb.addAction(back_btn)

		# de même pour l'action vers l'avant
		next_btn = QAction("Forward", self)
		next_btn.setStatusTip("Forward to next page")

		# ajouter une action au bouton suivant
		# faire avancer le navigateur
		next_btn.triggered.connect(self.browser.forward)
		navtb.addAction(next_btn)

		# de même pour l'action de rechargement
		reload_btn = QAction("Reload", self)
		reload_btn.setStatusTip("Reload page")

		# ajouter une action au bouton de rechargement
		# faire recharger le navigateur
		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)

		# de même pour l'action à domicile
		home_btn = QAction("Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		# ajouter un séparateur dans la barre d'outils
		navtb.addSeparator()

		# créer une ligne d'édition pour l'url
		self.urlbar = QLineEdit()

		# ajouter une action lorsque la touche de retour est enfoncée
		self.urlbar.returnPressed.connect(self.navigate_to_url)

		# ajouter ceci à la barre d'outils
		navtb.addWidget(self.urlbar)

		# ajout d'une action d'arrêt à la barre d'outils
		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")

		# ajouter une action au bouton d'arrêt
		# faire en sorte que le navigateur s'arrête
		stop_btn.triggered.connect(self.browser.stop)
		navtb.addAction(stop_btn)

		# montrant tous les composants
		self.show()


	# methode pour mettre a jour le titre de la fenetre
	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle("% s - Master Lipakumu Browser" % title)


	# methode d'appel d'action du home
	def navigate_home(self):

		# ouvrir l'url
		self.browser.setUrl(QUrl("https://christiandev.pythonanywhere.com/"))

	# méthode appelée par la ligne edit lorsque la touche retour est enfoncée
	def navigate_to_url(self):

		# obtenir l'URL et la convertir en objet QUrl
		q = QUrl(self.urlbar.text())

		# si l'url est le schéma est vide
		if q.scheme() == "":
			# définir le schéma d'url sur html
			q.setScheme("http")

		# définir l'URL du navigateur
		self.browser.setUrl(q)

	# méthode de mise à jour de l'url
	# cette méthode est appelée par l'objet QWebEngineView
	def update_urlbar(self, q):

		# mettre du texte dans la barre d'url
		self.urlbar.setText(q.toString())

		# réglage de la position du curseur de la barre d'URL
		self.urlbar.setCursorPosition(0)


# creation de l'application pyqt5
app = QApplication(sys.argv)

# reglage du nom de l'application
app.setApplicationName("Master Lipakumu Browser")

# création d'un objet fenêtre principale
window = MainWindow()

# boucle
app.exec_()
