print("=" * 45)
print("Keyboard Shortcut")
print("=" * 45)
shortcut = input("Enter the action: ").capitalize()

if shortcut == "Copy":
    print("ctrl + C")
elif shortcut == "Paste":
    print("ctrl + V")
elif shortcut == "Cut":
    print("Ctrl + X")
elif shortcut == "Undo":
    print("Ctrl + Z")
elif shortcut == "Redo":
    print("Ctrl + Y")
elif shortcut == "Select all":
    print("Ctrl + A")
elif shortcut == "Save":
    print("Ctrl + S")
elif shortcut == "Print":
    print("Ctrl + P")
elif shortcut == "Find":
    print("Ctrl + F")
elif shortcut == "Replace":
    print("Ctrl + H")
elif shortcut == "New file / window":
    print("Ctrl + N")
elif shortcut == "Open file":
    print("Ctrl + O")
elif shortcut == "Create new folder":
    print("Ctrl + Shift + N")
elif shortcut == "Rename file":
    print("F2")
elif shortcut == "Permanently delete":
    print("Shift + Delete")
elif shortcut == "Properties":
    print("Alt + Enter")
elif shortcut == "Back":
    print("Alt + Left Arrow")
elif shortcut == "Forward":
    print("Alt + Right Arrow")
elif shortcut == "Parent folder":
    print("Alt + Up Arrow")
elif shortcut == "New tab":
    print("Ctrl + T")
elif shortcut == "Close tab":
    print("Ctrl + W")
elif shortcut == "Reopen closed tab":
    print("Ctrl + Shift + T")
elif shortcut == "Next tab":
    print("Ctrl + Tab")
elif shortcut == "Previous tab":
    print("Ctrl + Shift + Tab")
elif shortcut == "Address bar":
    print("Ctrl + L")
elif shortcut == "Refresh":
    print("Ctrl + R")
elif shortcut == "Bookmark page":
    print("Ctrl + D")
elif shortcut == "Comment/Uncomment":
    print("Ctrl + /")
elif shortcut == "Select multiple lines":
    print("Ctrl + Shift + ↑/↓")
elif shortcut == "Move line up/down":
    print("Alt + ↑/↓")
elif shortcut == "Delete line":
    print("Ctrl + Shift + K")
elif shortcut == "Auto-complete":
    print("Ctrl + Space")
elif shortcut == "Search in project":
    print("Ctrl + Shift + F")

else:
    print("Sorry, couldn't find shortcut")

print("Thank you")