'''
Created on Sep 8, 2018
@author: ishank
'''

def differentTeams(skills):
    
    subjects = {'p': 0, 'c': 0, 'm': 0, 'b': 0, 'z': 0 }
    
    for skill in skills.lower(): 
        subjects[skill] = subjects.get(skill, 0) + 1
    
    return min(subjects.values())

print(differentTeams("pppccmmbbzzz"))
    
