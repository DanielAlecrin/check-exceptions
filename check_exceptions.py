import glob

directory = "/home/dalecrin/Documentos/Workspace/Agendamento/SL-AgendamentoCore/src/main/"
resourceDirectoryPortuguese = directory + "resources/i18n/exception/messages_pt.properties"
resourceDirectoryEnglish = directory + "resources/i18n/exception/messages_en.properties"
resourceDirectorySpanish = directory + "resources/i18n/exception/messages_es.properties"

def inspect_exception_literals(resourceDirectory):
    incorrectExceptions = []

    f = open(resourceDirectory, "r")
    if f.mode == "r":
        contents = f.read()
        lines = contents.splitlines()

        for exception in all_exceptions:
            isCorrect = False
            messageAndDetail = 0
            for line in lines:
                if exception in line:
                    messageAndDetail += 1
                
                if messageAndDetail == 2:
                    isCorrect = True
                    break
            
            if isCorrect == False:
                incorrectExceptions.append(exception)
    
    return incorrectExceptions

all_exceptions = []
for filename in glob.iglob(directory + "**/*Exception.java", recursive=True):
    fileNameSplittedByDot = filename.split(".")
    fileNameSplittedByBar = fileNameSplittedByDot[0].split("/")

    exceptionName = fileNameSplittedByBar[len(fileNameSplittedByBar) - 1]

    all_exceptions.append(exceptionName)

print("#####################\n")
print("#####################\n")
print("ABAIXO ESTÃO AS EXCEPTIONS QUE ESTÃO SEM AS LITERAIS NOS ARQUIVOS\n")
print("#####################\n")
print("#####################\n")

## Português
wrong_exceptions_pt = inspect_exception_literals(resourceDirectoryPortuguese)

print("Exceptions incorretas em Portugues: "  + str(len(wrong_exceptions_pt)))
for wrongExcpt in wrong_exceptions_pt:
    print(wrongExcpt)

print("\n")

## Espanhol
wrong_exceptions_es = inspect_exception_literals(resourceDirectorySpanish)

print("Exceptions incorretas em Espanhol: "  + str(len(wrong_exceptions_es)))
for wrongExcpt in wrong_exceptions_es:
    print(wrongExcpt)

print("\n")

## Inglês
wrong_exceptions_en = inspect_exception_literals(resourceDirectoryEnglish)

print("Exceptions incorretas em Ingles: "  + str(len(wrong_exceptions_en)))
for wrongExcpt in wrong_exceptions_en:
    print(wrongExcpt)

print("\n")


################################################
def inspect_not_unused_literals(resourceDirectory):
    notUnusedExceptions = []

    f = open(resourceDirectory, "r")
    if f.mode == "r":
        contents = f.read()
        lines = contents.splitlines()

        for line in lines:

            if len(line.strip()) == 0:
                continue

            hasExcept = False
            splittedLine = line.split("=")[0].split(".")

            lineExcep = splittedLine[0]
            if len(splittedLine) < 3:
                for exception in all_exceptions:

                    if lineExcep == exception:
                        hasExcept = True
                        break
                
                if hasExcept == False:
                    notUnusedExceptions.append(lineExcep)

    # return notUnusedExceptions
    return list(dict.fromkeys(notUnusedExceptions))    

        # for exception in all_exceptions:
        #     isCorrect = False
        #     messageAndDetail = 0
        #     for line in lines:
        #         if exception in line:
        #             messageAndDetail += 1
                
        #         if messageAndDetail == 2:
        #             isCorrect = True
            
        #     if isCorrect == False:
        #         incorrectExceptions.append(exception)


not_unused_except = inspect_not_unused_literals(resourceDirectoryPortuguese)

print("#####################\n")
print("#####################\n")
print("ABAIXO ESTÃO AS LITERAIS NÃO UTILIZADAS E QUE ESTÃO NOS ARQUIVOS\n")
print("#####################\n")
print("#####################\n")
print("Literais não utilizadas - Português:")
for excp in not_unused_except:
    print(excp)


not_unused_except = inspect_not_unused_literals(resourceDirectorySpanish)

print("#####################\n")
print("Literais não utilizadas - Espanhol:")
for excp in not_unused_except:
    print(excp)

not_unused_except = inspect_not_unused_literals(resourceDirectoryEnglish)

print("#####################\n")
print("Literais não utilizadas - Ingles:")
for excp in not_unused_except:
    print(excp)