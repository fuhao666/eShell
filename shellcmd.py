import os, traceback

password = '137871'


class shellcmd:

    def sudo_cmd(cmd):
        try:
            strs = os.system('echo %s | sudo -S %s' % (password, cmd))
        except:
            strtest = traceback.format_exc()
            print(strtest)

    def cmd(cmd):
        try:
            strs = os.system('%s' % cmd)
        except:
            strtest = traceback.format_exc()
            print(strtest)

