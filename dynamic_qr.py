import qrcode

from flask import Flask, redirect
import sqlite3
from datetime import datetime

from flask import url_for

app = Flask(__name__)


qr_id = 26
dynamic_url = f"http://localhost:8000/q/{qr_id}"
# dynamic_url = "https://ramadan-nice-kareem-2.netlify.app/"
# http://192.168.1.5:8080/q/

@app.route("/q/<int:qr_id>")
def redirect_qr(qr_id):

    conn = sqlite3.connect("qr.db")
    c = conn.cursor()
    
    # c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    c.execute("SELECT * FROM qr_codes")
    print(c.fetchall())

    c.execute("SELECT destination FROM qr_codes WHERE id=?",(qr_id,))
    result = c.fetchone()
    print(c.fetchone())
    print(result[0])
    if result:
        url = result[0]

        print(redirect(url))
        # save visit
        c.execute(
            "INSERT INTO visits(qr_id, time) VALUES (?, ?)",
            (qr_id, datetime.now())
        )
# url = url_for("qr_redirect", code="test123", _external=True)
        conn.commit()
        conn.close()
        # url = url_for("qr_redirect", code="test123", _external=True)
        return redirect(url)
    # .headers["Location"]

    return "QR not found"


# @app.route("/create")
# def create():

#     # code = "test123"
#     code = qr_id

#     qr_link = url_for("qr_redirect", code=code, _external=True)

#     print(qr_link,"mostafa")

#     return qr_link
# url = url_for("qr_redirect", code=qr_id, _external=True)
# print(url)
# create()




# INSERT INTO qr_codes(id,url)
# VALUES(25,'https://gym-offer.com');
redirect_qr(qr_id)
# print(dynamic_url.headers["Location"])
print(dynamic_url,"moomk")
# .headers["Location"]

qr = qrcode.make("http://192.168.1.5:8080/q/26")

qr.save("static/qr/dynamic_qr2.png")





if __name__ == "__main__":
    app.run(port=8000, debug=True)

print("Running file:", __name__)

# @app.route("/")
# def home():
#     return "QR Server Running"
# home()