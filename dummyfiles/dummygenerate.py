#!/usr/bin/env python3
"""
Dummy Generate
Creates Large numbers of files for test data
"""

"""
Libraries

sys
argparse
os
"""
import sys
import argparse
import os
import logging
import subprocess
import datasize

"""
Global Variables
"""
__version__='0.1.1'

class ColorizingStreamHandler(logging.StreamHandler):

    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BROWN = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    GREY = '\033[0;37m'

    DARK_GREY = '\033[1;30m'
    LIGHT_RED = '\033[1;31m'
    LIGHT_GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    LIGHT_BLUE = '\033[1;34m'
    LIGHT_PURPLE = '\033[1;35m'
    LIGHT_CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'

    RESET = "\033[0m"

    def __init__(self, *args, **kwargs):
        self._colors = {logging.DEBUG: self.GREEN,
                        logging.INFO: self.RESET,
                        logging.WARNING: self.BROWN,
                        logging.ERROR: self.LIGHT_RED,
                        logging.CRITICAL: self.RED}
        super(ColorizingStreamHandler, self).__init__(*args, **kwargs)

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream
            if not self.is_tty:
                stream.write(message)
            else:
                message = self._colors[record.levelno] + message + self.RESET
                stream.write(message)
            stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def setLevelColor(self, logging_level, escaped_ansi_code):
        self._colors[logging_level] = escaped_ansi_code


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = ColorizingStreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def generatefiles(mainDirNum,subDirNum,filesPerSubDir,fileSize,numBase,mainDirOffset,directory):
    userHome = os.path.expanduser("~")
    dummyDir=userHome + "/" + directory

    mainLen = namelen(mainDirNum,numBase)
    subLen = namelen(subDirNum,numBase)
    fileLen = namelen(filesPerSubDir,numBase)
    mainMax=mainDirNum + mainDirOffset
    i = mainDirOffset
    while i < mainMax:
        j = 0
        mainDirName = generatename(i,numBase,mainLen)
        while j < subDirNum:
            subDirName = generatename(j,numBase,subLen)
            k = 0            
            while k < filesPerSubDir:
                fileName = generatename(k,numBase,fileLen)
                dirName = dummyDir + "/" +mainDirName + "/" + subDirName + "/"
                os.makedirs(dirName,exist_ok=True)
                f = open(dirName + fileName,"wb")
                f.write(os.urandom(fileSize))
                f.close
                k = k + 1
            j = j + 1
        i = i + 1

    return 0

def namelen(maxNum,numBase):
    if numBase == "hexlower" or numBase == "hexupper":
        baseNum = hex(maxNum)
    elif numBase == "oct":
        baseNum = oct(maxNum)
    else:
        baseNum = maxNum

    strName = str(baseNum)
    truncName = strName[2:]

    nameLen = len(truncName)
    return nameLen
    
        
def generatename(name,numBase,nameLen):
    if numBase == "hexlower":
        baseName = hex(name)[2:]
    elif numBase == "hexupper":
        baseName = hex(name).upper()[2:]
    elif numBase == "oct":
        baseName = oct(name)[2:]
    else:
        baseName = name

    newName = str(baseName).rjust(nameLen,'0')
    return newName

def calctotalfilesize(fileSize,totalSize,mainDirNum,subDirNum):
    logger.debug("Entered function calctotalfilesize")
    logger.debug("fileSize:   " + fileSize)
    logger.debug("totalSize:  " + totalSize)
    logger.debug("mainDirNum: " + str(mainDirNum))
    logger.debug("subDirNum:  " + str(subDirNum))

    # dirty hack,
    # there has got to be a way to accurately hetermine ttis
    dirSize = datasize.DataSize("8ki")
    byteTotalSize = datasize.DataSize(totalSize)

    # Calculate space used by ddrectories
    totalDirSize = dirSize * mainDirNum * subDirNum

    # Calculate space used by files
    totalFileSize = byteTotalSize - totalDirSize
        
    return totalFileSize

def calcnumfiles (totalFileSize, fileSize):
    byteFileSize = datasize.DataSize(fileSize)
    numFiles = totalFileSize / byteFileSize
    return numFiles

def adjdirnum (numFiles, dirNum):
    # to maximize the total number of files:
    zeroCheck = numFiles % dirNum
    logger.debug("zeroCheck: " + str(zeroCheck))
    if zeroCheck != 0:
        logger.debug("zeroCheck is not Zero(0)")
        dirNum = adjdirnum(numFiles, dirNum - 1)
    else:
        logger.debug("dirNum: " + str(dirNum))
        
    return dirNum

    
def calcfilespermaindir (numFiles, mainDirNum):
    return numFiles / mainDirNum

def calcfilespersubdir (filesPerMainDir,subDirNum):
    return filesPerMainDir / subDirNum


def main():
    parser = argparse.ArgumentParser(description="Process parameters")
    parser.add_argument("-8","--base_eight",
                        action="store_true",
                        help="Set number system to base 8")
    parser.add_argument("-d","--directory",
                        default="dummyfiles",
                        help="Set Directory")
    parser.add_argument("-f","--file_size",
                        default="4ki",
                        #choices=["*k", "#ki"],
                        help="Set the size of the files to create")
    parser.add_argument("-hl","--hex_lower",
                        action="store_true",
                        help="Set number system to base 16 with lower case letters")
    parser.add_argument("-hu","--hex_upper",
                        action="store_true",
                        help="Set number system to base 16 with upper case letters")
    parser.add_argument("-m","--main_dir_num",
                        default=100,
                        type=int,
                        help="Set the number of directories to exist in the main directory")
    parser.add_argument("-n","--number_of_files",
                        default=100,
                        help="Set the total number of files to generate")
    parser.add_argument("-o","--main_dir_offset",
                        default=2000,
                        type=int,
                        help="Dirty hack")
    parser.add_argument("-s","--sub_dir_num",
                        default=12,
                        type=int,
                        help="Set the number of directories to exist in the main directory")
    parser.add_argument("-t","--total_size",                        
                        default="100Mi",
                        help="Set the total space allowed")
    parser.add_argument("--log",
                        help="Set minimum logging level",
                        choices=["debug","info","warning","error","critical","DEBUG","INFO","WARNING","ERROR","CRITICAL"])
    parser.add_argument("-V", "--version",
                        help="Print version information and exit",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("--debug",
                        help="Enable Debugging",
                        action="store_true")
    args = parser.parse_args()


    # Configure Application based on the arguments recieved
    if args.debug:
        logging.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    else:
        if args.log:
            # Bind loglevel to the string value obtained from the command line argument
            argloglevel=args.log
            # Convert to upper case to allow the user to specify --log=DEBUG or --log=debug
            loglevel = argloglevel.upper()
            logging.setLevel(loglevel)
            ch.setLevel(loglevel)


    # If debugging enabled, log the arguments passed to the program
    logger.debug("Arguments Processed")
    

    totalFileSize = calctotalfilesize(args.file_size,args.total_size,args.main_dir_num,args.sub_dir_num)
    fileSize = datasize.DataSize(args.file_size)

    numFiles = totalFileSize / fileSize

    mainDirNum = adjdirnum(numFiles,args.main_dir_num)
    filesPerMainDir = calcfilespermaindir(numFiles,mainDirNum)
    logger.debug("Calc Sub Dir Num")
    subDirNum = adjdirnum(filesPerMainDir,args.sub_dir_num)

    filesPerSubDir = calcfilespersubdir(filesPerMainDir,subDirNum)

    logger.debug("totalFileSize:   " + str(totalFileSize))
    logger.debug("mainDirNum: " + str(mainDirNum))
    logger.debug("filesPerMainDir: " + str(filesPerMainDir))
    logger.debug("subDirNum:  " + str(subDirNum))
    logger.debug("filesPerSubDir:  " + str(filesPerSubDir))

    if filesPerSubDir == 0:
        logger.critical("Total Spcae allowed is too small for the number of directories desired")
    else:
        if args.hex_lower:
            numBase="hexlower"
        elif args.hex_upper:
            numBase="hexupper"
        elif args.base_eight:
            numBase="oct"
        else:
            numBase="dec"

        logger.debug("numBase: " + str(numBase))

        generatefiles(int(mainDirNum),int(subDirNum),int(filesPerSubDir),fileSize,numBase,args.main_dir_offset,args.directory)
            
    return 0

main()
