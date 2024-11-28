# utils.py (in your app directory)
import uuid

def generate_guest_id(request):
    # Check if the user already has a guest ID stored in their session
    guest_id = request.session.get('guest_id')
    if not guest_id:
        # If not, create a new UUID
        guest_id = str(uuid.uuid4())  # Generate a new unique identifier
        request.session['guest_id'] = guest_id  # Store the UUID in the session
    return guest_id
