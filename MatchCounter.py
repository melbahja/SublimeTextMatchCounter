import sublime
import sublime_plugin

'''
    Author: Mohamed Elbahja
    Sublime Version: 3.x
'''

class MatchCounter(sublime_plugin.EventListener):

	def on_selection_modified_async(self, view):
		
		selected = view.sel()
		words = []

		for x in selected:
			
			x = view.substr(x)

			if x and x not in words:
				words.append(x)
			


		if (len(set(words)) == 1):

			words = len(view.find_all(words[0]))
			match = 'match' if words <= 1 else 'matches'
			self.status(view, "{0} {1}".format(words, match))
		
		else:

			self.status(view, '')


	def status(self, view, val):
		return view.set_status('matchCounter', val)

