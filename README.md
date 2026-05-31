# Chat Bot Direct Sales

A simple, interactive chatbot designed to assist with direct sales. It can answer product questions, provide pricing, and simulate placing orders. Built with Python, it's easy to extend for real-world use (e.g., integrating with a database or API).

## Features

- Responds to common sales inquiries (products, prices, shipping).
- Simulates order placement.
- Easy to customize product catalog.
- Command-line interface (can be adapted to web or messaging apps).

## Requirements

- Python 3.6+

No external libraries required (uses only standard library).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nate88811/chatBot-Direct-Sales.git
   cd chatbot-direct-sales
   ```
Usage 

1. Start the chatbot.

2. Type your message (e.g., "What products do you have?", "Price of widget", "I want to buy 2 gadgets").
 
 
3. The bot will respond with product info, pricing, or order confirmation.

 4. Type exit or quit to stop.
 
  Customization

 Edit the products dictionary in chatbot.py to change the product catalog.

 Modify the responses dictionary to change bot replies.

 Add more intents (e.g., discount codes, returns) by extending the get_response() function.
