from onepoint.katas.mexican import wave
from onepoint.log import init_log, log

if __name__ == "__main__":
    init_log()
    log.info("Hello wave is {}".format(wave("hello")))
