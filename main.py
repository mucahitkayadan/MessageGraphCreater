import json
import matplotlib.pyplot as plt
from datetime import datetime
import re

def parse_telegram_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        message_counts = {}
        person_names = set()  # Store unique person names
        
        for message in data['messages']:
            date_str = message['date'].split('T')[0]
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            ##sender = message['from']
            if 'from' in message:
                sender = message['from']
            else:
                print("Sender and receiver could not found in Json file!")
            person_names.add(sender)  # Collect unique person IDs
            
            if date in message_counts:
                message_counts[date] += 1
            else:
                message_counts[date] = 1
        
        sorted_counts = sorted(message_counts.items(), key=lambda x: x[0])
        
        dates = [str(date) for date, count in sorted_counts]
        counts = [count for date, count in sorted_counts]
        
        person_names_str = ' and '.join(person_names)
        
        return dates, counts, person_names_str

def parse_telegram_chat_iphone(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        message_counts = {}
        person_names = set()  # Store unique person IDs
        
        for message in data['messages']:
            date_str = message['date'].split('T')[0]
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            if 'from' in message:
                sender = message['from']
            elif 'actor' in message:
                sender = message['actor']
            else:
                print("Sender could not be found in JSON file!")
                continue
            
            person_names.add(sender)  # Collect unique person IDs
            
            if date in message_counts:
                message_counts[date] += 1
            else:
                message_counts[date] = 1
        
        sorted_counts = sorted(message_counts.items(), key=lambda x: x[0])
        
        dates = [str(date) for date, count in sorted_counts]
        counts = [count for date, count in sorted_counts]
        
        person_names_str = ' and '.join(person_names)
        
        return dates, counts, person_names_str

def parse_whatsapp_chat(file_path):
    pattern = r'^(\d{1,2}/\d{1,2}/\d{2}), (\d{2}:\d{2}) - (.+?): (.+)$'
    message_counts = {}
    person_names = set()  # Store unique person names
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line)
            
            if match:
                date_str = match.group(1)
                time_str = match.group(2)
                sender = match.group(3)
                message = match.group(4)
                
                person_names.add(sender)  # Collect unique person names
                
                datetime_str = f'{date_str} {time_str}'
                date = datetime.strptime(datetime_str, '%m/%d/%y %H:%M').date()
                
                if date in message_counts:
                    message_counts[date] += 1
                else:
                    message_counts[date] = 1
    
    sorted_counts = sorted(message_counts.items(), key=lambda x: x[0])
    
    dates = [str(date) for date, count in sorted_counts]
    counts = [count for date, count in sorted_counts]
    
    person_names_str = ' and '.join(person_names)
    
    return dates, counts, person_names_str

def parse_whatsapp_chat_iphone(file_path):
    pattern = r'\[(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2})\] (.+?): (.+)'
    message_counts = {}
    person_names = set()  # Store unique person names
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line)
            
            if match:
                date_str = match.group(1)
                time_str = match.group(2)
                sender = match.group(3)
                message = match.group(4)
                
                person_names.add(sender)  # Collect unique person names
                
                datetime_str = f'{date_str} {time_str}'
                date = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S').date()
                
                if date in message_counts:
                    message_counts[date] += 1
                else:
                    message_counts[date] = 1
    
    sorted_counts = sorted(message_counts.items(), key=lambda x: x[0])
    
    dates = [str(date) for date, count in sorted_counts]
    counts = [count for date, count in sorted_counts]
    
    person_names_str = ' and '.join(person_names)
    
    return dates, counts, person_names_str

# Get the message counts for the chosen chat type
def get_message_counts(chat_type, iphone_or_not):
    if chat_type == 1:  # Telegram
        if iphone_or_not ==1:
            return parse_telegram_chat_iphone('telegram_chat.json')
        elif iphone_or_not ==2:
            return parse_telegram_chat('telegram_chat.json')
        else:
            raise ValueError('Invalid phone type')
    elif chat_type == 2:  # WhatsApp
        if iphone_or_not ==1:
            return parse_whatsapp_chat_iphone('whatsapp_chat.txt')
        elif iphone_or_not ==2:
            return parse_whatsapp_chat('whatsapp_chat.txt')
        else:
            raise ValueError('Invalid phone type')
    else:
        raise ValueError('Invalid chat type')

# Get the user's input for chat type
def get_user_input():
    chat_type = int(input('Enter chat type (1 for Telegram, 2 for WhatsApp): '))
    iphone_or_not=int(input('Is your phone Iphone ? (1 for Yes , 2 for No): '))
    return chat_type, iphone_or_not

# Main function
def main():
    (chat_type, iphone_or_not) = get_user_input()
    
    try:
        dates, counts, person_names_str = get_message_counts(chat_type, iphone_or_not)
        
        plt.figure(figsize=(10, 6))
        plt.plot(dates, counts, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Number of Messages')
        plt.title('Chat Graph of ' + person_names_str)

        # Set the x-axis ticks to display only the first and last dates
        plt.xticks([dates[0], dates[-1]])

        plt.tight_layout()
        plt.show()
    except ValueError as e:
        print(str(e))

# Run the main function
if __name__ == '__main__':
    main()
