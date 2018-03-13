import sys

problem_level = input("input your problem type vals=[easy, medium, hard]( default=easy) :\n") or 'easy'
file_name = input("File name ( example = E066_PlusOne ): \n") or sys.exit('Error: File name needed')

def read_template(type, *format_vals):
	file = open('C:\\git\\helper-scripts\\templates\\' + type + '.txt', 'r')
	content = file.read().format(*format_vals)
	file.close()
	return content


java_template = read_template("java",problem_level, file_name)
golang_template = read_template("golang", problem_level)
python_template = read_template("python", file_name)
ruby_template = read_template("ruby", file_name)
scala_template = read_template("scala", problem_level,file_name)

languages = [
        ("java", 'src\\', "java", java_template),
        ("python", '', "py", python_template),
        ("js", '', "js", ""),
        ("ruby", 'lib\\', "rb", ruby_template),
        ("golang", 'src\\', "go", golang_template),
        ("scala", 'src\\', "scala", scala_template),
    ]
for lang in languages :
	( lang_name, lang_path, file_type, file_template ) = lang
	formatted_path = 'C:\\git\\coding-problems-{1}\\{2}mx\\grekz\\leetcode\\{0}\\{3}.{4}'.format(problem_level, lang_name, lang_path, file_name, file_type)
	# print(lang)
	print(formatted_path)
	cur_file = open(formatted_path, 'w+')
	cur_file.write(file_template)
	cur_file.close()