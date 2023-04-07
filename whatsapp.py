import tkinter as tk

# Step 1: Open the text file
with open('chat.txt', 'r', encoding='utf-8') as f:
    chatlines = f.readlines()

# Step 2: Extract the chat messages from the text file

chat_data = []
for line in chatlines:
    timestamp, sender_and_message = line.split(' - ')

    sender, message = sender_and_message.split(': ')
    chat_data.append({'timestamp':timestamp, 'sender':sender, 'message':message})
# Step 3: Create a GUI window and chat box widget
root = tk.Tk()
root.title('WhatsApp Chat')
chat_box = tk.Text(root)
chat_box.pack(fill='both', expand=True)

# Step 4: Add each message to the chat box widget
for msg in chat_data:
    chat_box.insert(tk.END, f'{msg["timestamp"]} {msg["sender"]}: {msg["message"]}\n')


root.mainloop()
