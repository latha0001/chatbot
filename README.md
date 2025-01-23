# Django Chat Application

## Features

1. **User Authentication**:
   - Users can sign up and log in to the application.

2. **User List**:
   - A collapsible left menu displays all registered users.

3. **Chat Functionality**:
   - Logged-in users can select any user from the menu to initiate a chat.
   - Messages are stored in the database and retrieved for display.

4. **Real-Time Messaging**:
   - WebSocket technology is used to enable real-time communication.

5. **User-Friendly Interface**:
   - The chat interface is intuitive and functional.

## Prerequisites

- Python 3.8 or above
- Django 4.0 or above
- Django Channels
- Redis (for WebSocket handling)
- A web browser for testing

## Setup Instructions

### Configure the Database

1. Open `settings.py` and update the `DATABASES` setting to match your preferred database.
2. Run migrations:
   ```bash
   python manage.py migrate
   ```

### Configure Redis

1. Install Redis on your system or use a cloud-based Redis service.
2. Update the `CHANNEL_LAYERS` configuration in `settings.py` to point to your Redis server.

### Run the Development Server

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Access the Application

Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Sign Up/Login**:
   - Create a new account or log in using existing credentials.
2. **Initiate a Chat**:
   - Select a user from the collapsible menu to start chatting.
3. **Real-Time Messaging**:
   - Send and receive messages instantly using WebSocket technology.
4. **View Chat History**:
   - Old messages are displayed when a chat is opened.
