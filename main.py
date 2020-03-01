import genanki
import os

from model import modelTemplate
from notes import NoteTemplate
from random import randint, choice

my_deck = genanki.Deck(
  2059400110,
  'Mathematic Equations')

for num in range(0, 10000):
  data = NoteTemplate(randint(10, 100), randint(10, 100), choice(["add", "subtract"]))
  note = genanki.Note(
    model = modelTemplate,
    fields = [data.equation, str(data.result)]
  )
  my_deck.add_note(note)

path = os.getcwd()

try:
  os.mkdir(path + "/build")
except OSError:
    print ("Creation of the directory %s failed" % path)

genanki.Package(my_deck).write_to_file('build/mathequation.apkg')

print ("Successfully generated apkg file!")