run:
	python gen_wall.py "bg.png" "logos/nixos-pure.png"
	# python gen_wall.py <bg-color|bg-img> <logo-img> ?<logo-color>
	sxiv out.png
transform:
	python transform_logo.py
	sxiv transformed.png
