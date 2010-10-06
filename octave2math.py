import sys
def main():
	f = open(sys.argv[1])
	f.readline()
	name = "" 
	mode = "none"
	matrix = []
	for line in f:
		token = line.split()
		if mode == "matrix":
			if token[0] == "#" and matrix == []:
				continue
			elif token[0] == "#":
				print_matrix(name, matrix)
				matrix = []
				mode = "none"
				name = token[2]
				continue
			row = []
			for i in token:
				row.append(float(i))
			matrix.append(row)
		elif mode == "scalar":
			print '"',name,'"', "=",token[0], "newline"
			mode = "none"
			continue
			
		atrrib = token[1]
		value = token[2]
		if atrrib == "name:":
			name = value
		elif atrrib == "type:":
			mode = value					

def print_matrix(name, matrix):
	print '"',name,'"', "=","left ( matrix{",
	for column in matrix:
		for row in column:
			print	"%.3f"%row, "#",
		print "\b\b##",
	print "\b\b\b} right ) newline"
	
		

if __name__ == "__main__":
	main()
