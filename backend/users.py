from flask import current_app as app

class User():
    def __init__(self, phone, time, do_quote, do_meme, do_msg):
        self.phone = phone
        self.time = time
        self.do_quote = do_quote
        self.do_meme = do_meme
        self.do_msg = do_msg
    
    @staticmethod
    def get(phone):
        rows = app.db.execute("""
        SELECT phone, time, do_quote, do_meme, do_msg
        FROM Users
        WHERE phone = :phone
        """, phone=phone)

        if not rows:
            return None
        else:
            return User(*(rows[0]))
    
    @staticmethod
    def register(phone, time, do_quote, do_meme, do_msg):
        try:
            rows = app.db.execute("""
            INSERT INTO Users(phone, time, do_quote, do_meme, do_msg)
            VALUES(:phone, :time, :do_quote, :do_meme, :do_msg)
            ON CONFLICT(phone) DO UPDATE SET time = :time, do_quote = :do_quote, do_meme = :do_meme, do_msg = :do_msg
            RETURNING phone
            """, phone=phone, time=time, do_quote=do_quote,
            do_meme=do_meme, do_msg=do_msg)
            
            phone = rows[0][0]
            return User.get(phone)
        except Exception as e:
            print(str(e))
            return None
    
    @staticmethod
    def cancel(phone):
        try:
            app.db.execute("""
            DELETE FROM Users
            WHERE phone = :phone
            """, phone=phone)
            return True
        except Exception as e:
            print(str(e))
            return False
        