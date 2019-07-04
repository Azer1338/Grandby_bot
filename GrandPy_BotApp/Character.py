# -*- coding: utf-8 -*-

class Character():
		""" Manage bubble discussion
		"""
		
		def __init__(self, kind_of):
			"""Initialize some variables or objects.
			"""
			
			# Variable
			self.Name = kind_of
			self.Class_name = "row"
			
			# Define the right DOM for display
			self.DOM_definition()
			
		def DOM_definition(self):
			""" Define the bubble discussion orientation
			for display purpose
			"""
			if self.Name == 'System':
				self.Class_name = "row bubble bubble_right"
			elif self.Name == 'User':
				self.Class_name = "row bubble bubble_left"
			else :
				print('DOM not defined. Character definition not known')
				
		def creation_DOM(self):
			""" Create a bubble into the discussion area.
			

			# Create a bubble for discussion
			var bubbleElt = document.createElement("div");
			bubbleElt.setAttribute("class",this.className);
			
			"""
		
		def text_intro(self):
			""" Introduction text.
			"""
			
			txt = "Ou veux tu aller?"
			
			return txt
				
		def display_text(self,txt_to_display):
			"""
			
			this.CreationDOM();

			// DOM element content
			var textElt = document.createElement("p");
			textElt.textContent = textToDisplay;
			bubbleElt.appendChild(textElt);
			"""
		
		def display_form(self):
			"""
			
			this.CreationDOM();

			// Input
			var inputElt = document.createElement("input");
			inputElt.id = "User_destination";
			inputElt.setAttribute("placeholder","Tape ton adresse ici!");
			inputElt.setAttribute("maxlength","45");
			bubbleElt.appendChild(inputElt);

			// Button
			var ButtonElt = document.createElement("button");
			ButtonElt.id = "Destination_btn";
			ButtonElt.setAttribute("class","btn btn-primary");
			ButtonElt.setAttribute("type","button");
			ButtonElt.setAttribute("required", "true");
			ButtonElt.appendChild(document.createTextNode("Envoi"));
			bubbleElt.appendChild(ButtonElt);
			"""
			
		def display_map(self, place_to_display):
			""" Display a map embeded.
			
			"""
			
		def display_story(self, place_relative_to_story):
			""" Display a story relative to a place.
			
			"""
		def parse_fr_method(self,sentence_to_parse):
			""" Shrink sentence based on parse method.
			Sentence chain is converted as a list.
			Minor words (light weight) are removed.
			List is convert as a chain.
			Only major words are kept.
			"""
			
			return major_word_chain
