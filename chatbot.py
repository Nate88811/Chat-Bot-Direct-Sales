"""
chatbot
A simple command-line chatbot for handling sales inquiries and orders.
"""

import re

# Product catalog: product_name -> price
products = {
    "widget": 10.00,
    "gadget": 25.00,
    "doohickey": 15.50,
    "thingamajig": 40.00
}

# Basic responses for common intents
responses = {
    "greeting": "Welcome to chatbot! I can help you with products, prices, and orders. Ask me anything!",
    "products": "We have: " + ", ".join([f"{name} (${price:.2f})" for name, price in products.items()]),
    "unknown": "I'm sorry, I didn't understand that. Try asking about products, prices, or placing an order.",
    "exit": "Goodbye!"
}

def get_product_price(product_name):
    """Return the price of a product, or None if not found."""
    product_name = product_name.lower().strip()
    return products.get(product_name)


def handle_order(text):
    """
    Try to parse an order from user input.
    Expected format: "buy N product" or "order N product" or "I want N product"
    Returns a tuple (product_name, quantity) or None.
    """
    # Patterns: "buy 2 widgets", "order 3 gadgets", "I want 1 doohickey"
    patterns = [
        r"(?:buy|order|purchase)\s+(\d+)\s+(.+)",
        r"(?:i want|i'd like|give me)\s+(\d+)\s+(.+)",
        r"(\d+)\s+(.+)"  # fallback: "2 widgets"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            quantity = int(match.group(1))
            product_name = match.group(2).strip().lower()
            # Remove trailing punctuation/words
            product_name = re.sub(r'[^a-z\s]', '', product_name).strip()
            # Check if product exists (exact match or first word)
            if product_name in products:
                return product_name, quantity
            # Try first word only (e.g., "widgets" -> "widget")
            first_word = product_name.split()[0]
            if first_word in products:
                return first_word, quantity
    return None


def get_response(user_input):
    """Main logic: determine intent and return appropriate response."""
    text = user_input.lower().strip()

    # Exit commands
    if text in ["exit", "quit", "bye", "goodbye"]:
        return responses["exit"], True  # (response, should_exit)

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "greetings"]):
        return responses["greeting"], False

    # Product listing
    if any(word in text for word in ["product", "catalog", "what do you have", "items"]):
        return responses["products"], False

    # Price inquiry
    if "price" in text or "cost" in text or "how much" in text:
        # Try to find a product name in the text
        for product_name in products:
            if product_name in text:
                price = products[product_name]
                return f"{product_name.capitalize()} costs ${price:.2f}", False
        # If no specific product found, list all prices
        return responses["products"], False

    # Order placement
    order = handle_order(text)
    if order:
        product_name, quantity = order
        price = products[product_name]
        total = price * quantity
        return f"Order placed: {quantity} x {product_name} = ${total:.2f}. Thank you for your purchase!", False

    # Fallback
    return responses["unknown"], False


def main():
    print("🤖 chatbot")
    print("Type 'exit' to quit.\n")

    # Initial greeting
    print(responses["greeting"]) 

    while True:
        user_input = input("\nYou: ")
        response, should_exit = get_response(user_input)
        print(f"Bot: {response}")
        if should_exit:
            break


if __name__ == "__main__":
    main()
