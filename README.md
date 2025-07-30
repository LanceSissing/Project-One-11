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

## Technical Improvements & Notes

### Cloudinary Integration for Media Storage
- Configured Django to use Cloudinary for all user-uploaded images, ensuring reliable, scalable, and secure media hosting.
- Credentials are managed via environment variables for security (see `.env` and Heroku Config Vars).
- Local `.env` file and `.gitignore` prevent accidental exposure of sensitive keys.
- All new images uploaded via the deployed app are stored in Cloudinary and displayed reliably.

### Heroku Deployment
- Project is fully configured for deployment on Heroku, including:
  - Automatic database switching (SQLite locally, PostgreSQL on Heroku)
  - Static files collected to `staticfiles/` for production serving
  - Environment-specific settings for debug, allowed hosts, and database engine

### Security Best Practices
- All sensitive credentials (Cloudinary, database, etc.) are stored in environment variables, not in code or version control.
- `.env` is included in `.gitignore` to prevent leaks.

### Data Migration & Testing
- Used Django `dumpdata` and `loaddata` for safe migration of local data to Heroku.
- Ensured UTF-8 encoding for compatibility and error-free imports.
- Manual migration of images recommended for legacy data; new uploads are handled automatically.

### Additional Improvements
- Modular Django app structure (`accounts`, `marketplace`)
- Custom user model for future extensibility
- Clear separation of static and media files
- Step-by-step documentation and troubleshooting for deployment and media issues

---
For more details, see the project planning document or contact the maintainer.
