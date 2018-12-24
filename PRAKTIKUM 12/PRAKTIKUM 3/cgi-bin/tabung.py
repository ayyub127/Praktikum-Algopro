def tabung():
	volume = 22/7*5*5*5
	return volume
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Tabung</title>
	</head>
	<body>
		<form>
			<table>
				<tr>
					<td rowspan='8'>
					<img src='../tabung.png' width='160' height='160'>
					</td>
					<td>
						<p><b><font size='5'>Bangun Geometri</font></b></p>
					</td>
				</tr>
				
				<tr>
					<td>Nama Bangun</td>
					<td>:</td>
					<td>Tabung</td>
				</tr>
				
				<tr>
					<td>Dimensi</td>
					<td>:</td>
					<td>2D</td>
				</tr>
				
				<tr>
					<td>Rumus Volume</td>
					<td>:</td>
					<td>22/7 * r * r * t</td>
				</tr>
				
				<tr>
					<td>pi</td>
					<td>:</td>
					<td>
					22/7
					</td>
				</tr>
				<tr>
					<td>r</td>
					<td>:</td>
					<td>
					5
					</td>
				</tr>
				<tr>
					<td>t</td>
					<td>:</td>
					<td>
					5
					</td>
				</tr>
    
				<tr>
					<td>Volume</td>
					<td>:</td>
					<td>"""
print tabung()
print"""</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""
