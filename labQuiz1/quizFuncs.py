#Name: Chanelle Mosquera
#Section: CPE 101 - 016

def multiply_List(l_int, num):
	mult_l = []
	for i in range(len(l_int)):
		if i == 1:
			sub_l = []
			for n in range(len(l_int[i])):
				sub_l.append(l_int[i][n] * num)
			mult_l.append(sub_l)
		else:
			mult_l.append(l_int[i] * num)
			
	return mult_l

def average_List(l_int):
	cnt = 0
	suml = 0.0
	for i in l_int:
		suml += i
		cnt += 1
	avg = float(suml/cnt)
	list_avg_cnt = [avg,cnt]
	return list_avg_cnt

def studntGrade(l1,l2,l3):
	student_avg = []
	for student in range(9):
		grade_avg = (l1[student] + l2[student] + l3[student]) / 3.0
		student_avg.append(grade_avg)
	total_sum = 0
	for grade in student_avg:
			total_sum += grade
	main_avg = total_sum/9
	return student_avg, main_avg


