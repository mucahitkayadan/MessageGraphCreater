Telegram and WhatsApp Chat Graph Generator
==========================================

This project lets you generate message count graphs for Telegram and WhatsApp conversations.

Back-Up Your Chat History
-------------------------

Before using this project, you need to back up your Telegram and WhatsApp chat history:

*   Telegram:
    1.  Open the chat you want to back up in Telegram.
    2.  Tap on the three-dot menu icon in the top-right corner.
    3.  Select "Export Chat History" and choose whether to include media.
    4.  Save the exported file as `telegram_chat.json` in the same folder as this script.
*   WhatsApp:
    1.  Open the chat you want to back up in WhatsApp.
    2.  Tap on the three-dot menu icon in the top-right corner.
    3.  Select "More" and then "Export Chat".
    4.  Choose whether to include media and select the export method (via email, etc.).
    5.  Save the exported file as `whatsapp_chat.txt` in the same folder as this script.

Usage
-----

To generate a chat graph, follow these steps:

1.  Make sure you have Python installed on your system.
2.  Download or clone this repository to your computer.
3.  Place the `telegram_chat.json` and `whatsapp_chat.txt` files in the same folder as this script.
4.  Open a terminal or command prompt and navigate to the project folder.
5.  Install the required dependencies (matplotlib) by running the following command:

    $ pip install matplotlib

7.  Run the main script:

    $ python main.py

9.  When prompted, enter the chat type (1 for Telegram, 2 for WhatsApp).
10.  The script will analyze the chat history file and generate a message count graph for the selected chat type.

Contributing
------------

I want you to know that contributions to this project are welcome. If you have any ideas, suggestions, or bug reports, please submit them as GitHub issues or create a pull request.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more details.
