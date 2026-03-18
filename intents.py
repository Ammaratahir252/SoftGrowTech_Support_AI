# ================================================================
#  intents.py — Customer Support Knowledge Base
#  All chatbot intents, patterns and responses are defined here.
#  Add your own intents by following the same structure.
# ================================================================

INTENTS = [
    # ── Greetings ────────────────────────────────────────────────
    {
        "tag": "greeting",
        "patterns": [
            "hello", "hi", "hey", "good morning", "good afternoon",
            "good evening", "howdy", "what's up", "hi there", "greetings",
            "sup", "yo", "hiya"
        ],
        "responses": [
            "Hello! Welcome to our support center. How can I help you today?",
            "Hi there! I'm here to help. What can I assist you with?",
            "Hey! Great to hear from you. What do you need help with?",
            "Hello! How can I assist you today?"
        ]
    },

    # ── Goodbye ──────────────────────────────────────────────────
    {
        "tag": "goodbye",
        "patterns": [
            "bye", "goodbye", "see you", "see ya", "take care",
            "later", "quit", "exit", "done", "that's all", "thanks bye",
            "thank you bye", "i'm done", "nothing else"
        ],
        "responses": [
            "Goodbye! Have a wonderful day. Feel free to come back anytime!",
            "Take care! Don't hesitate to reach out if you need anything.",
            "Bye! It was great helping you today. Have a great day!",
            "See you later! Stay well and reach out if you need us."
        ]
    },

    # ── Thanks ───────────────────────────────────────────────────
    {
        "tag": "thanks",
        "patterns": [
            "thank you", "thanks", "thank you so much", "thanks a lot",
            "appreciate it", "that helped", "great thanks", "cheers",
            "many thanks", "thx", "ty"
        ],
        "responses": [
            "You're welcome! Is there anything else I can help you with?",
            "Happy to help! Let me know if you need anything else.",
            "Glad I could assist! Anything else on your mind?",
            "Anytime! Feel free to ask if you have more questions."
        ]
    },

    # ── Order Status ─────────────────────────────────────────────
    {
        "tag": "order_status",
        "patterns": [
            "where is my order", "track my order", "order status",
            "when will my order arrive", "order tracking", "my order",
            "check order", "order not received", "order update",
            "where is my package", "track package", "delivery status",
            "has my order shipped", "order confirmation", "order number"
        ],
        "responses": [
            "To track your order, please visit our website and go to 'My Orders' section. You'll need your order number and email address. If you can't find it, share your order number and I'll look into it.",
            "You can check your order status by logging into your account and clicking 'Track Order'. Orders typically ship within 1-2 business days. Need help finding your order number?",
            "For order tracking, head to our Orders page or check your email for a shipping confirmation with a tracking link. What's your order number so I can assist further?"
        ]
    },

    # ── Returns & Refunds ────────────────────────────────────────
    {
        "tag": "returns",
        "patterns": [
            "return policy", "how to return", "return an item", "refund",
            "get my money back", "return product", "exchange", "damaged item",
            "wrong item", "defective product", "return request",
            "how do i return", "refund policy", "return window",
            "can i return", "want to return", "send back"
        ],
        "responses": [
            "Our return policy allows returns within 30 days of purchase. Items must be in original condition. To start a return: go to My Orders → Select the item → Click 'Return'. Refunds are processed within 5-7 business days.",
            "You can return most items within 30 days. Simply log in, go to your orders, and select 'Return Item'. Once we receive it, your refund will be issued within 5-7 business days to your original payment method.",
            "Returns are easy! Visit My Account → My Orders → Return Item. We accept returns within 30 days of delivery. Damaged or defective items can be returned for free — just mention the issue when submitting."
        ]
    },

    # ── Payment ──────────────────────────────────────────────────
    {
        "tag": "payment",
        "patterns": [
            "payment methods", "how to pay", "accepted payments",
            "credit card", "debit card", "paypal", "payment failed",
            "payment issue", "can i pay with", "billing", "invoice",
            "payment not working", "charge", "pay online", "payment options",
            "do you accept", "apple pay", "google pay"
        ],
        "responses": [
            "We accept Visa, Mastercard, American Express, PayPal, Apple Pay and Google Pay. All payments are secured with SSL encryption. If your payment failed, please check your card details or try a different payment method.",
            "Payment options include all major credit/debit cards, PayPal, Apple Pay and Google Pay. Having trouble with payment? Try clearing your browser cache or using a different browser.",
            "We support all major credit cards, PayPal and digital wallets. If you're experiencing a payment issue, ensure your billing address matches your card records or contact your bank to check if the transaction was blocked."
        ]
    },

    # ── Shipping ─────────────────────────────────────────────────
    {
        "tag": "shipping",
        "patterns": [
            "shipping cost", "how long does shipping take", "delivery time",
            "free shipping", "express delivery", "overnight shipping",
            "international shipping", "shipping options", "estimated delivery",
            "how fast", "when will it arrive", "shipping fee",
            "do you ship to", "standard shipping", "fast delivery"
        ],
        "responses": [
            "Shipping options: Standard (5-7 days, free over $50), Express (2-3 days, $9.99), Overnight ($24.99). International shipping available to 50+ countries. Orders placed before 2 PM ship same day!",
            "We offer free standard shipping on orders over $50. Express delivery (2-3 business days) is $9.99, and overnight is $24.99. Most orders ship within 1 business day.",
            "Standard shipping takes 5-7 business days and is free for orders over $50. Need it faster? Choose express (2-3 days) or overnight at checkout. We ship internationally to over 50 countries!"
        ]
    },

    # ── Account ──────────────────────────────────────────────────
    {
        "tag": "account",
        "patterns": [
            "forgot password", "reset password", "can't login", "login issue",
            "account locked", "create account", "sign up", "register",
            "change email", "update profile", "delete account",
            "account problem", "can't access account", "my account",
            "password reset", "username", "account help"
        ],
        "responses": [
            "For password reset: click 'Forgot Password' on the login page and enter your email. You'll receive a reset link within 2 minutes. Check your spam folder if you don't see it.",
            "Account issues? Here's help: Reset password via 'Forgot Password' on login page. If account is locked, wait 15 minutes or contact support. To update profile, go to Account Settings.",
            "To reset your password, visit the login page and click 'Forgot Password'. Enter your registered email and follow the instructions. Still having trouble? I can escalate this to our account team."
        ]
    },

    # ── Product Info ─────────────────────────────────────────────
    {
        "tag": "product",
        "patterns": [
            "product information", "tell me about", "product details",
            "is it available", "in stock", "out of stock", "product specs",
            "features", "how does it work", "product review",
            "best product", "recommend", "which product", "size guide",
            "color options", "product quality"
        ],
        "responses": [
            "For detailed product information including specs, reviews and availability, please visit the product page on our website. You can also use the search bar to find exactly what you're looking for. Need help with a specific product?",
            "I'd be happy to help with product info! For the most accurate and up-to-date details, check the product listing on our site. You can filter by size, color and availability. What product are you interested in?",
            "Product details, specs, and availability are all on our website. Each listing includes customer reviews, size guides, and stock status. Is there a specific item I can help you find?"
        ]
    },

    # ── Discount & Promo ─────────────────────────────────────────
    {
        "tag": "discount",
        "patterns": [
            "discount", "promo code", "coupon", "sale", "offer",
            "deal", "promo", "voucher", "get discount", "any offers",
            "save money", "cheaper", "best price", "price match",
            "student discount", "first order discount", "referral"
        ],
        "responses": [
            "Sign up for our newsletter to receive a 10% welcome discount! We also run seasonal sales. Check our Offers page for current deals. Have a promo code? Enter it at checkout.",
            "Current promotions: 10% off first order with code WELCOME10, free shipping on orders over $50, and 20% off select items in our sale section. Newsletter subscribers get exclusive deals first!",
            "Great news! New customers get 10% off with code WELCOME10. We also have a referral program — share your link and earn store credit. Check our Deals page for the latest offers!"
        ]
    },

    # ── Contact / Human Agent ────────────────────────────────────
    {
        "tag": "contact",
        "patterns": [
            "speak to human", "talk to agent", "human support",
            "contact support", "call customer service", "email support",
            "live chat", "phone number", "customer service number",
            "real person", "escalate", "complaint", "not helpful",
            "speak to someone", "contact us", "support team", "help desk"
        ],
        "responses": [
            "To reach our support team: Email: support@company.com | Phone: 1-800-SUPPORT (Mon-Fri 9AM-6PM) | Live Chat: Available on our website. For urgent issues, phone is fastest. Would you like me to try helping first?",
            "Our human support team is available via: 📧 Email: support@company.com | 📞 Phone: 1-800-SUPPORT | 💬 Live Chat on our website. Hours: Monday-Friday 9AM-6PM EST. What's the issue you'd like to escalate?",
            "I can connect you with our team! Contact options: Phone (1-800-SUPPORT), Email (support@company.com), or Live Chat on our website. Available weekdays 9AM-6PM. Is there anything I can resolve for you first?"
        ]
    },

    # ── Warranty ─────────────────────────────────────────────────
    {
        "tag": "warranty",
        "patterns": [
            "warranty", "guarantee", "product warranty", "warranty claim",
            "broken product", "defective", "not working", "faulty",
            "repair", "replacement", "how long is warranty",
            "warranty period", "manufacturer warranty"
        ],
        "responses": [
            "All products come with a 1-year manufacturer warranty covering defects. To make a warranty claim, go to My Orders, select the item, and click 'Warranty Claim'. Include photos of the defect. Most claims are resolved within 7 business days.",
            "Our products carry a 1-year warranty against manufacturing defects. If your product is faulty, please contact us with your order number and photos of the issue. We'll arrange a repair or replacement at no cost to you.",
            "Warranty coverage: 1 year on all products for manufacturing defects. Physical damage is not covered. To file a claim: My Account → Orders → Warranty Claim. You'll hear from our team within 2 business days."
        ]
    },

    # ── Fallback ─────────────────────────────────────────────────
    {
        "tag": "fallback",
        "patterns": [],
        "responses": [
            "I'm not sure I understood that. Could you rephrase your question? I can help with orders, returns, payments, shipping, account issues, and more.",
            "Hmm, I didn't quite catch that. Try asking about order tracking, returns, shipping, payments, or account help. Or type 'contact' to reach a human agent.",
            "I'm still learning! I didn't understand that question. You can ask me about: orders, returns, refunds, shipping, payments, accounts, products, or discounts.",
            "That's outside my current knowledge. For complex issues, type 'contact support' to reach our team. Otherwise, try rephrasing — I'm here to help!"
        ]
    }
]
