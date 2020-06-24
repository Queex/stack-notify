default notify_messages=[]
default notify_last_addition=None

# Adjust these as you like
default notify_duration=4.0
default notify_fade_in=0.25
default notify_fade_out=0.5
default recent_notify_at_top=True

# This means that the stack notify will replace the usual notify
# If you want to have 2 separate systems, comment this out and
# call add_notify_message directly.
define config.notify = add_notify_message

init -1 python:

    def add_notify_message(msg):
        import time
        global notify_messages
        global notify_last_addition
        if recent_notify_at_top:
            notify_messages.prepend(msg)
        else:
            notify_messages.append(msg)
        notify_last_addition=time.time()
        renpy.show_screen("stack_notify")
        renpy.restart_interaction()

    def finish_notify():
        import time
        if time.time() > notify_last_addition + notify_duration-notify_fade_out:
            renpy.hide_screen("stack_notify")
            renpy.restart_interaction()

    def clear_notify(trans, st, at):
        global notify_messages
        notify_messages=[]

screen stack_notify_item(msg):
    style_prefix "notify"
    text "[msg!tq]"
    timer notify_duration-notify_fade_out action Function(finish_notify)

screen stack_notify():
    tag stack_notify
    zorder 100
    style_prefix "notify"

    frame at stack_notify_appear:
        has vbox
        for msg in notify_messages:
            use stack_notify_item(msg)

transform stack_notify_appear:
    on show:
        alpha 0
        linear notify_fade_in alpha 1.0
    on hide:
        linear notify_fade_out alpha 0.0
        function clear_notify
