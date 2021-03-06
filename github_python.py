import subprocess
import os
import sys
import re

is_mac =  os.name == 'posix'

problem_level_dic = {
    'e' : 'easy',
    'm' : 'medium',
    'h' : 'hard'
}
def get_name(problem_name) :
    problem_number_file, problem_name_file = problem_name.strip().split('.')
    if (len(problem_number_file) < 3 ) :
        problem_number_file = '0' + problem_number_file
        problem_name = '0' + problem_name
    problem_number_file = 'E' + problem_number_file
    problem_name_file = re.sub(r"[\s-]+", "", problem_name_file, flags=re.UNICODE)
    problem_file = problem_number_file + '_' + problem_name_file
    return problem_file, problem_name

problem_url  = input("Input your url: \nexample https://leetcode.com/problems/length-of-last-word/description/\n") or sys.exit('Error: Problem url needed') 
problem_level = input("input your problem type vals=[easy, medium, hard]( default=easy) :\n") or 'easy'
problem_type = problem_level_dic[problem_level[0]]
problem_title = input("Problem Name ( example = 058. Length of Last Word )\n") or sys.exit('Error: Problem name needed') + ' - Solution.'

problem_file, problem_name = get_name(problem_title)
post_item_ini = '''    <li>
        <a href='https://github.com/Grekz/coding-problems-'''
post_item_end = '''</a>
    </li>
'''
post_ini = '''
<h4><a href='{0}' target='_blank' rel='noopener'>Description</a></h4>
<h4>Solutions:</h4>
<ul>
'''
post_end = '''
</ul>
{3} '''

if is_mac :
    path_git = '/Users/juan.mendoza/extra-git/'
else :
    path_git = 'C:\\git\\'

def build_cd(language):
    return path_git + "coding-problems-" + language
def build_problem_language(prefix, language):
    return { 'comment' : prefix + "LCE-" + problem_name, 'language' : language }
def build_command(tup):
    problem = build_problem_language(tup[0], tup[1])
    return [build_cd(problem['language']), ["git add .", 'git commit -am "' + problem['comment'] + '"', "git push -u origin"], tup[2], tup[1]] #
def do_commits_and_shit():
    languages = [
        ("J", "java", "java/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.java' target='_blank'>Java"),
        ("P3", "python", "python/blob/working-branch/mx/grekz/leetcode/{1}/{2}.py' target='_blank'>Python"),
        ("JS", "js", "js/blob/working-branch/mx/grekz/leetcode/{1}/{2}.js' target='_blank'>Javascript"),
        ("R", "ruby", "ruby/blob/working-branch/lib/mx/grekz/leetcode/{1}/{2}.rb' target='_blank'>Ruby"),
        ("G", "golang", "golang/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.go' target='_blank'>Golang"),
        ("S", "scala", "scala/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.scala' target='_blank'>Scala"),
        ("K", "kotlin", "kotlin/blob/working-branch/src/mx/grekz/leetcode/{1}/{2}.kt' target='_blank'>Kotlin"),
    ]
    commands  = [ build_command(e) for e in languages ]
    hashtags = "#leetcode #{1}"
    post = post_ini
    for current_command in commands :
        # print(current_command)
        os.chdir(current_command[0])
        commit_failed = False
        try:    
            for inner_command in current_command[1] :
                proc = subprocess.check_output(inner_command,shell=True)
                commit_failed = proc == b"On branch working-branch\nYour branch is up to date with 'origin/working-branch'.\n\nnothing to commit, working tree clean\n"                   
        except subprocess.CalledProcessError as e:
            print(e.output)
            commit_failed = True
        if not commit_failed :
            post += post_item_ini + current_command[2] + post_item_end
            hashtags += ' #' + current_command[3]
    post += post_end
    post += hashtags + '\n' + hashtags.replace(" #", ',')[1:]
    print(post.format(problem_url, problem_type, problem_file, problem_name))
do_commits_and_shit()
# print(problem_file)
# print(problem_name)