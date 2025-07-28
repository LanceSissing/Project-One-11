C:/Users/No-one/Documents/vscode-projects/PROJECT-ONE-11/.venv/Scripts/python.exe manage.py migrate
# Project-One-11

## Overview
Project-One-11 is a scalable full-stack web application for buying and selling motorcycle parts. Users can create accounts, post items for sale, and correspond with prospective buyers. The platform aims to provide a frustration-free, value-driven experience for both buyers and sellers, with future plans for commission-based revenue.

## Key Features
- User registration and account management
- Post and browse motorcycle parts for sale
- Search by machine, part category, brand, and type
- Messaging between buyers and sellers
- Transparent, regulated environment
- (Future) Business accounts and database integration

## User Stories
**Individual Buyer:**
- Find items that fit their motorcycle easily
- Buy at market-leading prices with confidence

**Individual Seller:**
- Sell parts with minimal fuss and low fees
- Avoid excessive charges or commissions

**Business User:**
- Add products and manage inventory
- Reach a targeted audience with minimal setup cost

## Entity Relationship Diagram (ERD) Outline
```
User (Buyer/Seller/Business)
  |--< Item (Product)
  |--< Transaction
  |--< Message

Item
  |--< Transaction

Transaction
  |-- Buyer (User)
  |-- Seller (User)
  |-- Item
```

*Note: This is a simplified ERD. More fields and relationships will be added as the project develops.*

## Getting Started
1. Clone the repository
2. Set up a Python virtual environment
3. Install dependencies (`pip install -r requirements.txt`)
4. Run migrations and start the development server

---
For more details, see the project planning document or contact the maintainer.
