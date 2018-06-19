import sys
import os
import re

def get_name(problem_name) :
    problem_number_file, problem_name_file = problem_name.strip().split('.')
    if (len(problem_number_file) < 3 ) :
        problem_number_file = '0' + problem_number_file
        problem_name = '0' + problem_name
    problem_number_file = 'E' + problem_number_file
    problem_name_file = re.sub(r"\s+", "", problem_name_file, flags=re.UNICODE)
    problem_file = problem_number_file + '_' + problem_name_file
    return problem_file
	
is_mac =  os.name == 'posix'
ignored_langs = ["golang", "scala"] if len(sys.argv) > 1 and sys.argv[1] == "basic" else ( sys.argv[1:] or [] )
problem_level = input("input your problem type vals:( e=easy, m=medium, h=hard ) [default=e] :\n") or 'e'
file_name = input("File name ( example = 98. Validate Binary Search Tree ): \n") or sys.exit('Error: File name needed')
file_name = get_name(file_name)

problem_level_dic = {
	'e' : 'easy',
	'm' : 'medium',
	'h' : 'hard'
}

print(os.name)	
if is_mac :
	slash = '/'
	template_path = '/Users/juan.mendoza/extra-git/coding-problems-{1}/{2}mx/grekz/leetcode/{0}/{3}.{4}'
	fileTemplate_path = '/Users/juan.mendoza/extra-git/helper-scripts/templates/'
else: 
	slash = '\\'
	template_path = 'C:\\git\\coding-problems-{1}\\{2}mx\\grekz\\leetcode\\{0}\\{3}.{4}' 
	fileTemplate_path = 'C:\\git\\helper-scripts\\templates\\'
	
problem_level = problem_level_dic[problem_level[0]]

print(ignored_langs)

def read_template(type, *format_vals):
	file = open(fileTemplate_path + type + '.txt', 'r')
	content = file.read().format(*format_vals)
	file.close()
	return content


java_template = read_template("java",problem_level, file_name)
golang_template = read_template("golang", problem_level)
python_template = read_template("python", file_name)
ruby_template = read_template("ruby", file_name)
scala_template = read_template("scala", problem_level,file_name)

languages = [
        ("java", 'src' + slash, "java", java_template),
        ("python", '', "py", python_template),
        ("js", '', "js", ""),
        ("ruby", 'lib' + slash, "rb", ruby_template),
        ("golang", 'src' + slash, "go", golang_template),
        ("scala", 'src' + slash, "scala", scala_template),
    ]
for lang in languages :
	( lang_name, lang_path, file_type, file_template ) = lang
	if not lang_name in ignored_langs: 
		formatted_path = template_path.format(problem_level, lang_name, lang_path, file_name, file_type)
		print(formatted_path)
		try:
			cur_file = open(formatted_path, 'w+')
			cur_file.write(file_template)
			cur_file.close()
		except Exception as e:
			raise e