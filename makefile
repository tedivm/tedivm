
readme_grid:
	PROJECT_FORMAT=grid python generator.py > README.md

readme_list:
	PROJECT_FORMAT=list python generator.py > README.md

readme_pdf:
	gh-md-to-html README.md --i imgs --dont-make-images-links false -p RobertsProjects.pdf
