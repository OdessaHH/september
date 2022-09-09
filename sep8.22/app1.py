import sys
fast_mode=False
#user_input = input()
#help_var =sys.argv[1]
#fast_var = sys.argv[2]
for i in sys.argv[1:]:
    if sys.argv[1]== "--help":
        print("slow mode enabled my default, you can activate fast mode with --fast")
    elif sys.argv[1]== "--fast" or sys.argv[2] =="--fast":
        fast_mode=True

if fast_mode == True:
    print("Fast mode enabled")
else:
     print("slow mode enabled")