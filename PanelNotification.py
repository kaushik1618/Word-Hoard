#!/usr/bin/env python

def showPanelNotification(title="Not set", text="Not set", initText="Not set"):
    try:
        import gtk, pygtk, sys, os, os.path, pynotify
        pygtk.require('2.0')
    except:
        print "Error: need python-notify, python-gtk2 and gtk"
    if not pynotify.init(initText):
        print "pynotify.init() failed"
        sys.exit(1)
    n = pynotify.Notification(title, text)
    n.set_urgency(pynotify.URGENCY_LOW)
    """helper = gtk.Button()
    icon = helper.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
    n.set_icon_from_pixbuf(icon)"""
    if not n.show():
        print "Failed to send notification"
        sys.exit(1)
    return

if __name__ == '__main__':
    showPanelNotification()
