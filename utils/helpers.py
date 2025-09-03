def is_admin(user_id, db):
    # Example check
    admin = db.admins.find_one({"user_id": user_id})
    return bool(admin)