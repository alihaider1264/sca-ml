import argparse
import LogGenerator.GitDownloader as GitDownloader
import LogGenerator.LogGen as LogGen
import GitLogParser.GitLogParser as GitLogParser
import shutil
import stat
import json
import time
import errno, os, stat, shutil
import subprocess

#https://seart-ghs.si.usi.ch/


#https://stackoverflow.com/questions/1213706/what-user-do-python-scripts-run-as-in-windows
def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

def theLogParserPart(inpath,outpath):
    filesToParse = LogGen.searchFiles(inpath, ".gitlog")
    pathToOutput = "#todo"
    #mimic file structure of initial folder in output folder with an additional folder for each log named after the log.
    for i in filesToParse:
        pathToOutput = outpath + i.split(".gitlog")[0] + "\\"
        print (pathToOutput)
        GitLogParser.mainArgs(pathToOutput,inpath+i)



def interfacer(repo,output,branch,submodules,multibranch,defJSON,usemethods,fileformat,seart,noDupe):
    if noDupe:
        hashes = []
    else:
        hashes = False
    if (seart):
        seartParse(repo,output,branch,submodules,multibranch,defJSON,usemethods,fileformat,seart)
        exit()
    branches = GitDownloader.downloadRepo(repo, output+"\git", branch, multibranch, submodules)
    hashes = LogGen.logGen(fileformat, output+"\git\main", output+"\log\main", defJSON, usemethods,hashes)
    gitpath = output + '\git\\'

    if multibranch is not False:
        for branch in branches:
            if ("->" in branch):
                continue 
            #get current branch TODO maybe
            if (branch == 'master' or branch == 'main'):
                continue 
            print (branch)
            GitDownloader.downloadRepo(repo, output+"\git", branch, False, submodules)
            hashes = LogGen.logGen(fileformat, output+"\git\\"+branch , output+"\log\\"+branch , defJSON, usemethods,hashes)

    theLogParserPart(output+"\log",output+"\parsed")

    process1 = subprocess.run("rmdir "+ gitpath + "/s /q", shell=True)
    hashes = []
    #else:
        #LogGen.main(repo, output, branch, defJSON)


def seartParse(repo,output,branch,submodules,multibranch,defJSON,usemethods,fileformat,seart):
    f = open(repo, encoding="utf8")
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    for i in data['items']:
        gitname = i['name']
        gitrepo = "https://github.com/" + gitname + ".git"
        interfacer(gitrepo,output+"\\"+gitname.split("/")[1],branch,submodules,multibranch,defJSON,usemethods,fileformat,False,True)
        a = open(output+"\\"+gitname.split("/")[1]+"\gitinfo.txt", "w")
        a.write(json.dumps(i))
        a.close()
    f.close()


def main():
    parser = argparse.ArgumentParser(description='The thing that makes LogGen and GitDownloader work together')
    parser.add_argument('-r', '--repo', help='The Repo to generate logs for (Assumes internet repos)', required=True)
    parser.add_argument('-o', '--output', help='The output folder', required=True)
    parser.add_argument('-b', '--branch', help='Specify the branch', required=False)
    parser.add_argument('-s', '--submodules', help='Download submodules', default=False, action="store_true")
    parser.add_argument('-mb', '--multibranch', help='use all avalable branches',  default=False, action="store_true")
    parser.add_argument('-d', '--defJSON', help='the definitions of the file formats', required=False)
    parser.add_argument('-l', '--language', help='the language to generate logs with', required=False)
    parser.add_argument('-se', '--seart', help='use a seart JSON file defined with --repo',  default=False, action="store_true")
    parser.add_argument('-m', '--methods', help='use methods temp text',  default=False, action="store_true")
    parser.add_argument('-p', '--parse', help='parse the Gitlogs into seperate files',  default=False, action="store_true") #new, needs to be implimented!!!
    parser.add_argument('-nd', '--noDupe', help='deletes duplicate files between branches', default=False, action="store_true")




    args = parser.parse_args()
    interfacer(args.repo, args.output, args.branch, args.submodules, args.multibranch, args.defJSON , args.methods, args.language, args.seart , args.noDupe)

main()