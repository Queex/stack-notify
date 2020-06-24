# Stacking Notifications for Renpy
This stand-alone file implements a stacking notification widget for renpy, which can replace the default notification window.

## Behaviour
Whenever a new notification is generated, it is added to the list of current notifications and this screen is shown. The screen fades in, remains, then fades out. If a new notification is generated while the screen is displayed, then it is added to the vertical stack of notifications and the display time is restarted. Once the screen has faded out completely, then the list of notifications is cleared and new ones won't reshow the old ones. The screen uses the standard 'notify' style, which you can alter as usual.

## Usage
Simply drop this script into your game directory to use it.
The script contains the line:

`define config.notify = add_notify_message`

which means this sytem will replace the standard renpy notification; if you want to have both then comment out this line.

## Parameters
There are several tweaks you can make to how the system works:
- `notify_duration=4.0`: the total display time of the most recent notification.
- `notify_fade_in=0.25`: how long the notification takes to fade in.
- `notify_fade_out=0.5`: how long the notification takes to fade out.
- `recent_notify_at_top=True`: when `True` new notifications are put at the top of the stack, when 'False' they are put ta the bottom.

## Advanced Customisation
You can fine-tune or extend behaviour in the following ways:

### add_notify_messages(msg)
This is called when a new notification is generated.

### finish_notify()
This is called every time an individual message has been shown for the requisite amount of time. The `if` clause checks to make sure there are no more recent notifications keeping the screen alive, and hides the screen if not.

### clear_notify(trans, st ,at):
This is called after the screen has faded out completely, to empty the list of messages.

### stack_notify_appear
This transform is used for the enclosing frame for all the notifications.
