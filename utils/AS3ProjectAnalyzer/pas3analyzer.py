import os
import os.path
import re


# ---------------------------- classes ---------------------------------
class ASClass:
    def __init__(self, fileName, filePath):
        self.fileName = fileName
        self.filePath = filePath
        self.className = fileName[:fileName.index('.')]

        self.innerClasses = []
        self.innerMethods = []

    def __repr__(self):
        return self.className

    def getInnerClasses(self):
        return self.innerClasses

# -----------------------------------------------------------------------

print("------------- AS3 project analyzer --------------")

# rootClassName = 'Main'
# folders = ['prj']
rootClassName = 'GameBase'
folders = ['puppy']

prjClassesList = []
prjClassesDict = {}
classesLinkedWithRoot = []

print('\n...gathering all classes...')
while len(folders):
    fileNode = folders.pop(0)
    # debug:
    # print(fileNode)
    fdir = os.listdir(fileNode)
    for childFile in fdir:
        childPath = fileNode + "\\" + childFile
        if os.path.isdir(childPath):
            folders.append(childPath)
        else:
            asclass = ASClass(childFile, childPath)
            prjClassesList.append(asclass)
            prjClassesDict[asclass.className] = asclass
        # debug:
        # print(childPath)

# set root class as first in list
for c in prjClassesList:
    if c.className == rootClassName:
        idx = prjClassesList.index(c)
        rootClassObj = prjClassesList.pop(idx)
        prjClassesList.insert(0, rootClassObj)

    pass

print('\n--- gathered classes:', prjClassesList)

print('\n...collecting class references per every class...')
for c in prjClassesList:
    print("[..................CLASS...................:]" + c.className)
    with open(c.filePath, 'r', encoding='utf-8') as f:
        codeLines = f.readlines()
        longCommentEncountered = False
        for line in codeLines[:]:
            line = line.strip()
            # print('[<-  ]' + line)

            # --------------- ignore some lines because of emptyness, comments ...etc -------------------
            # empty line
            if len(line) == 0:
                continue

            # short comment
            if line.find('//') != -1:
                continue

            # curly braces
            if len(line) == 1 and line.find('{') != -1:
                continue
            if len(line) == 1 and line.find('}') != -1:
                continue

            # long comment in one line
            if line.find('/*') != -1 and line.find('*/') != -1:
                continue

            # long comment
            if line.find('/*') != -1:
                longCommentEncountered = True
                continue

            if line.find('*/') != -1 and longCommentEncountered:
                longCommentEncountered = False
                continue

            if longCommentEncountered:
                continue

            # skip all imports
            if line.find('import') != -1:
                continue

            # skip all packages
            if line.find('package') != -1:
                continue

            # ------------------- gathering classes --------------------
            # print('[  ->]' + line)
            if line.find('extends') != -1:
                match = re.search('(extends\s+)(?P<clazz>\w+)', line)
                c.innerClasses.append(match['clazz'])
                # print('[clz add->]' + match['clazz'])
                continue

            # class from declarations and as returned values
            if line.find(':') != -1:
                match = re.search(':\s*(?P<clazz>\w+)', line)
                if match is not  None:
                    c.innerClasses.append(match['clazz'])
                    # print('[clz add->]' + match['clazz'])

            if line.find('new') != -1:
                match = re.search('new\s+(?P<clazz>\w+)', line)
                if match is not  None:
                    c.innerClasses.append(match['clazz'])
                    # print('[clz add->]' + match['clazz'])
            # assignment class to var
            if line.find('=') != -1:
                match = re.search('=\s*(?P<clazz>\w+)\W*', line)
                if match is not  None:
                    c.innerClasses.append(match['clazz'])
                    # print('[clz add->]' + match['clazz'])

            # getting static classes
            if line.find('.') != -1:
                matches = re.findall('(\w+)\.', line)
                if len(matches) > 0:
                    for m in matches:
                        c.innerClasses.append(m)
                        # print('[clz add->]' + m)

            #------------------- gathering methods -------------------
            '''
            if line.find('function') != -1:
                match = re.search('function\s+(?P<method>\w+)', line)
                if match is not  None:
                    c.innerMethods.append(match['method'])
                    print('[mTd add->]' + match['method'])
            '''



print('\n...postprocessing collected classes...')
print('\n--- Classes and thier inner classes:')
for c in prjClassesList:
    # make unique
    c.innerClasses = list(set(c.innerClasses))
    # fill innerClasses with real class objects
    # and also automatically filtering of built-in classes like Sprite or MovieClip
    c.innerClasses = [prjClassesDict[ic] for ic in c.innerClasses if ic in prjClassesDict]
    classesLinkedWithRoot += c.innerClasses
    # print('class:' + str(c))
    # print(' -> inner refs:' + str(c.innerClasses))

classesLinkedWithRootSet = set(classesLinkedWithRoot)

isolatedClasses = set(prjClassesList) - classesLinkedWithRootSet
print("\n--- isolated classes:" + str(isolatedClasses))

classesLinkedWithRoot = list(classesLinkedWithRootSet)
print("\n--- linked with ROOT classes:" + str(classesLinkedWithRoot))

# +1 because of root class
print("\n--- Number of actual classes:" + str(len(classesLinkedWithRoot) + 1))

#--------------------- processing methods --------------------------------