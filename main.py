import psutil, time, easygui, sys, os, ctypes

def file_exists(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

def psdbox(msg):
    return str(easygui.passwordbox(msg=msg, title='反网课检测系统，by suai哥郭某人'))
    
def msgbox(msg):
    easygui.msgbox(msg=msg, title="反网课检测系统，by suai哥郭某人")

def enterbox(msg):
    return easygui.enterbox(msg=msg, title='反网课检测系统，by suai哥郭某人')

def running(psd, program_name):

    msgbox('反网课系统已开启！')

    while True:
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                if process_name == program_name:
                    proc.kill()

                    psd = psdbox(msg='请输入密码！')
                    try:
                        psd = int(psd)
                    except ValueError:
                            msgbox('请不要输入字母及符号！')
                    else:
                        if int(psd) == int(password):
                            msgbox('反网课系统已关闭！')
                            sys.exit()

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        time.sleep(1)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        file = open('C:/AppData/No-Classes/configuration-file.ini', 'r',  encoding='utf8')
        tmp = file.readlines()
        file.close()

        password = tmp[0]
        program_name = tmp[1]

        running(password, program_name)

    except FileNotFoundError:
        msgbox('检测到您是第一次使用软件，请先生成配置文件！')
        
        path = 'C:/AppData/No-Classes'

        file_exists(path)

        file = open(path + '/configuration-file.ini', 'w',  encoding='utf8')

        ok = True
        while ok:
            ok1 = True
            psd1 = 0
            psd2 = 0
            while ok1:
                psd1 = easygui.passwordbox(msg='请输入密码！', title='反网课检测系统，by suai哥郭某人')
                try:
                    psd1 = int(psd1)
                except ValueError:
                    msgbox('密码只支持数字，请不要输入字母及符号！')
                else:
                    ok1 = False
            
            ok2 = True
            while ok2:
                psd2 = easygui.passwordbox(msg='请再次输入密码！', title='反网课检测系统，by suai哥郭某人')
                try:
                    psd2 = int(psd2)
                except ValueError:
                    msgbox('密码只支持数字，请不要输入字母及符号！')
                else:
                    ok2 = False

            if psd1 == psd2:
                ok = False
                file.write(str(psd1) + '\n')
            else:
                msgbox('密码输入不匹配，请重新输入！')

        file.write(easygui.enterbox('请输入要关闭的程序名称！（默认为ClassIn）',  default='ClassIn.exe', title='反网课检测系统，by suai哥郭某人'))
        file.close()
        msgbox('配置文件已生成，点击OK后程序会自动重启。')
        os.execl(sys.executable,sys.executable,*sys.argv)
else:
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


