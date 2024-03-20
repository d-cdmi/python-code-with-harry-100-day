from notifypy import Notify


def notiyi(NowTime,MyWork):
    notification = Notify()
    notification.title = f"Now Time is {NowTime}"
    notification.message = f"This Time is {MyWork}"
    # notification.icon = "path/to/icon.png"
    notification.send()
