#!/usr/bin/env python

def showPanelNotification(title="Not set", text="Not set", timeoutInSecs=5, initText="Not set"):

    try:
        import gtk, pygtk, sys, os, os.path, pynotify
        pygtk.require('2.0')
    except:
        print "Error: need python-notify, python-gtk2 and gtk"

    if not pynotify.init(initText):
        print "pynotify.init() failed"
        sys.exit(1)

    n = pynotify.Notification(title, text)
    #n = pynotify.Notification("Moo title", "test", "file:///path/to/icon.png")

#options: URGENCY_LOW, URGENCY_NORMAL, URGENCY_CRITICAL

    n.set_urgency(pynotify.URGENCY_LOW)
    n.set_timeout(1000*timeoutInSecs)
    #n.set_category("device")

    helper = gtk.Button()
    icon = helper.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
    n.set_icon_from_pixbuf(icon)

    if not n.show():
        print "Failed to send notification"
        sys.exit(1)

if __name__ == '__main__':
    showPanelNotification()
