import subprocess
import os
import sys

problem_url  = input("Input your url: \nexample https://leetcode.com/problems/length-of-last-word/description/\n") or 'https://leetcode.com/problems/'
problem_type = input("input your problem type vals=[easy, medium, hard]( default=easy) :\n") or 'easy'
# problem_file = input("File name ( example = E066_PlusOne ): \n") or sys.exit('Error: File name needed')
problem_name = input("Problem Name ( example = 058. Length of Last Word )\n") or sys.exit('Error: Problem name needed') + ' - Solution.'
problem_number_file, problem_name_file = problem_name.split('.')
if (len(problem_number_file) != 3 ) :
    problem_number_file = '0' + problem_number_file
problem_number_file = 'E' + problem_number_file
problem_name_file = problem_name_file.replace(' ', '')
problem_file = problem_number_file + '_' + problem_name_file

def build_cd(language):
    return "C:\\git\\coding-problems-" + language
def build_problem_language(prefix, language):
    return { 'comment' : prefix + "LCE-" + problem_name, 'language' : language }
def build_command(tup):
    problem = build_problem_language(tup[0], tup[1])
    return [build_cd(problem['language']), ["git add .", 'git commit -am "' + problem['comment'] + '"', "git push -u origin"]]
def do_commits_and_shit():
    languages = [
        ("J", "java"),
        ("P3", "python"),
        ("JS", "js"),
        ("R", "ruby"),
        ("G", "golang"),
        ("S", "scala"),
    ]
    commands  = [ build_command(e) for e in languages ]
    for current_command in commands :
        os.chdir(current_command[0])
        print(current_command[0])
        for inner_command in current_command[1] :
            print(inner_command)
            proc = subprocess.check_output(inner_command)
            print(proc)

    post = '''
<h4><a href='{0}' target='_blank' rel='noopener'>Description</a></h4>
<h4>Solutions:</h4>
<ul>
    <li>
        <a href='https://github.com/Grekz/coding-problems-java/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.java' target='_blank'>Java
        </a>
    </li>
    <li>
        <a href='https://github.com/Grekz/coding-problems-python/blob/working-branch/mx/grekz/leetcode/{1}/{2}.py' target='_blank'>Python
        </a>
    </li>
    <li>
        <a href='https://github.com/Grekz/coding-problems-js/blob/working-branch/mx/grekz/leetcode/{1}/{2}.js' target='_blank'>Javascript
        </a>
    </li>
    <li>
        <a href='https://github.com/Grekz/coding-problems-ruby/blob/working-branch/lib/mx/grekz/leetcode/{1}/{2}.rb' target='_blank'>Ruby</a></li>
    <li>
        <a href='https://github.com/Grekz/coding-problems-golang/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.go' target='_blank'>Golang
        </a>
    </li>
    <li>
        <a href='https://github.com/Grekz/coding-problems-scala/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.scala' target='_blank'>Scala
        </a>
    </li>
</ul>
{3} #leetcode #java #python3 #javascript #ruby #golang #scala #{1}
solution, java, python3, javascript,js, ruby, golang, go, scala, leetcode
    '''
    print(post.format(problem_url, problem_type, problem_file, problem_name))
do_commits_and_shit()
# print(problem_file)