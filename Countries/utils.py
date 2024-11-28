import uuid

def generate_guest_id(request):
    guest_id = request.session.get('guest_id')
    if not guest_id:
        guest_id = str(uuid.uuid4()) 
        request.session['guest_id'] = guest_id  
    return guest_id
