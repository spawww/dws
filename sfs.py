import os
from datetime import datetime 

from bottle import template

REPO_DWS = None
TITLE = None

def scambio(rotta, prefix, infix, infix2, suffix):

    title = TITLE[rotta]
    title = title + " " + prefix + '*' if prefix else title
    title = title + " *" + infix + '*' if infix else title
    title = title + " *" + infix2 + '*' if infix2 else title
    title = title + " *" + suffix  if suffix else title
        
    lrit =  []
    size = 0
    for nf in os.listdir(REPO_DWS[rotta]):
        nfl = nf.lower()
        if nfl.startswith(prefix) and (infix in nfl) and (infix2 in nfl) and nfl.endswith(suffix) and isVisible(REPO_DWS[rotta] + nf):
            dimensione = os.path.getsize(REPO_DWS[rotta] + nf)
            lrit.append({
                         'dataModifica' : convertiTimeStamp(os.path.getmtime(REPO_DWS[rotta] + nf)),
                         'percorsoFile' : rotta + '/' + nf,
                         'nomeFile' : nf,
                         'dimensione' : fileSizeReadable(os.path.getsize(REPO_DWS[rotta] + nf)),
                         })
            size += dimensione
    lrit = sorted(lrit, key = lambda k : k['dataModifica'], reverse=True)
    return template('templates/scambio.tpl', listaFile=lrit, title=title, size=fileSizeReadable(size), rotta=rotta)

def isVisible(nf):
    if (os.path.isfile(nf)):
        if not os.path.isdir(os.path.splitext(nf)[0] + '_files'):
            return True 
    return False

def convertiTimeStamp(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def fileSizeReadable(num):
    for unit in ['b','Kb','Mb']:
        if abs(num) < 1024.0:
            return ("%3.0f %s" % (num, unit)).strip()
        num /= 1024.0
    return ("%.1f %s" % (num, 'Gb')).strip()

def initRepos():
    global REPO_DWS
    global TITLE

    REPO_DWS = {}
    TITLE = {}

def addRepo(rotta, title, folder):
    global REPO_DWS
    global TITLE

    REPO_DWS[rotta] = folder
    TITLE[rotta] = title 

if __name__ == "__main__":
    initRepos()
    addRepo('docs', 'DWS', 'C:/_D_/github/dws/docs/')
    with open('C:/_D_/github/dws/index.html', 'w') as fout:
        fout.write(scambio('docs', '', '', '', ''))

