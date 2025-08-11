# Project-One-11

## Overview
Project-One-11 is a scalable full-stack web application for buying and selling motorcycle parts. Users can create accounts, post items for sale, and correspond with prospective buyers. The platform aims to provide a frustration-free, value-driven experience for both buyers and sellers, with future plans for commission-based revenue.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [User Experience Design](#user-experience-design)
- [Project Planning](#project-planning)
  - [MOSCOW Prioritisation](#moscow-prioritisation)
  - [Wireframes](#wireframes)
- [User Stories](#user-stories)
- [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
- [Security](#security)
- [Future Features](#future-features)
- [Technologies and Languages Used](#technologies-and-languages-used)
- [Libraries and Frameworks](#libraries-and-frameworks)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Agile](#agile)
- [AI Implementation](#ai-implementation)
- [Assessment/Admin Access](#assessmentadmin-access)

## Key Features
- User registration and account management
- Post and browse motorcycle parts for sale
- Search by machine, part category, brand, and type
- Messaging between buyers and sellers
- Transparent, regulated environment
- (Future) Business accounts and database integration

## User Experience Design
The application is designed for clarity and ease of use, with a responsive layout and intuitive navigation. Key user flows (registration, listing items, messaging) are streamlined. Accessibility is considered, with semantic HTML and ARIA labels. User feedback and error messages are clear and actionable.

## Project Planning

### MOSCOW Prioritisation
- **Must Have:** User registration/login, item listing, messaging, search/filter, secure media storage, responsive design.
- **Should Have:** Business accounts, account editing, image gallery modal, semantic HTML for accessibility.
- **Could Have:** Advanced search, user ratings, saved searches, notifications.
- **Won’t Have (for now):** Integrated payment processing (see Future Features).

### Wireframes
*Add wireframe images or links here to illustrate key pages and user flows.*

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

## Entity Relationship Diagram (ERD)
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

## Security

- All sensitive credentials (Cloudinary, database, etc.) are stored in environment variables, not in code or version control.
- `.env` is included in `.gitignore` to prevent leaks.
- User authentication and permissions are enforced throughout the app.
- Data validation and form sanitization are implemented to prevent common vulnerabilities.

## Future Features

- **Payment Integration:** Add secure payment methods (e.g., Stripe, PayPal) for in-app transactions.
- **User Ratings & Reviews:** Allow buyers and sellers to rate each other.
- **Notifications:** Email or in-app notifications for new messages and offers.
- **Mobile App:** Native or PWA version for mobile users.

## Technologies and Languages Used

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (for interactivity)
- **Database:** SQLite (local), PostgreSQL (production/Heroku)
- **Media Storage:** Cloudinary

## Libraries and Frameworks

- Django (core framework)
- Bootstrap (styling and layout)
- Cloudinary (media storage)
- psycopg2 (PostgreSQL integration)
- gunicorn (production server)
- django-environ (environment variable management)

## Testing

- Manual testing of all user flows (registration, login, listing, messaging, editing).
- Automated tests for models and forms (add screenshots here).
- Lighthouse and WAVE used for accessibility and performance checks.
- Example screenshot:
  ![Lighthouse Accessibility Score](screenshots/lighthouse-accessibility.png)

## Deployment

- Deployed on Heroku with automatic database switching (SQLite locally, PostgreSQL on Heroku).
- Static files collected and served from `/staticfiles/`.
- Media files stored on Cloudinary.
- Environment-specific settings for debug, allowed hosts, and database engine.
- Data migrated using Django `dumpdata` and `loaddata`.

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

### Data Migration & Testing
- Used Django `dumpdata` and `loaddata` for safe migration of local data to Heroku.
- Ensured UTF-8 encoding for compatibility and error-free imports.
- Manual migration of images recommended for legacy data; new uploads are handled automatically.

### Additional Improvements
- Modular Django app structure (`accounts`, `marketplace`)
- Custom user model for future extensibility
- Clear separation of static and media files
- Step-by-step documentation and troubleshooting for deployment and media issues

## Credits

- Project developed by [Your Name].
- Thanks to the Django, Bootstrap, and Cloudinary communities for open-source tools and documentation.
- [List any other contributors, mentors, or resources here.]

## Agile

- Project managed using agile principles: iterative development, regular review, and adaptation.
- User stories and MOSCOW prioritisation guided feature development.
- Kanban board (Trello/Jira/other) used for task tracking.

## AI Implementation

- GitHub Copilot and other AI tools were used for code suggestions, semantic HTML improvements, and troubleshooting.
- AI-assisted accessibility and performance checks (Lighthouse, WAVE).

## Admin Access

To access the Django admin panel for assessment:

- **Admin URL:** https://project-one-11-4a3af24a0591.herokuapp.com/admin/
- **Username:** Admin-one-11
- **Password:** Comp-12_8hg*!

---

For more details, see the project planning document or contact the maintainer.
