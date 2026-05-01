import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreimport os
from flask import Flask, render_template
from flask_socketio import Socketimport os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
          return render_template('index.html')
      
from flask import request

@socketio.on('chat_message')
def handle_message(data):
          # Foydalanuvchi ID sini olish
          sender_id = request.sid
          print(f'>>> Xabar {sender_id} dan keldi: {data}')
          # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
                  'msg': data,
                  'sender_id': sender_id
    }import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
          return render_template('index.html')

from flask import request

@socketio.on('chat_message')
def handle_message(data):
          # Foydalanuvchi ID sini olish
          sender_id = request.sid
          print(f'>>> Xabar {sender_id} dan keldi: {data}')
          # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
                  'msg': data,
                  'sender_id': sender_id
    })

if __name__ == '__main__':
          cert_path = 'server.crt'
          key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
                  print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
                  socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
                  print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
                  socketio.run(app, host='0.0.0.0', port=5000)
import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
          return render_template('index.html')

from flask import request

@socketio.on('chat_message')
def handle_message(data):
          # Foydalanuvchi ID sini olish
          sender_id = request.sid
          print(f'>>> Xabar {sender_id} dan keldi: {data}')
          # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
                  'msg': data,
                  'sender_id': sender_id
    })

if __name__ == '__main__':
          cert_path = 'server.crt'
          key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
                  print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
                  socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
                  print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
                  socketio.run(app, host='0.0.0.0', port=5000)
      import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
          return render_template('index.html')

from flask import request

@socketio.on('chat_message')
def handle_message(data):
          # Foydalanuvchi ID sini olish
          sender_id = request.sid
          print(f'>>> Xabar {sender_id} dan keldi: {data}')
          # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
                  'msg': data,
                  'sender_id': sender_id
    })

if __name__ == '__main__':
          cert_path = 'server.crt'
          key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
                  print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
                  socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
                  print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
                  socketio.run(app, host='0.0.0.0', port=5000)
          
if __name__ == '__main__':
          cert_path = 'server.crt'
          key_path = 'server.key'
      
    if os.path.exists(cert_path) and os.path.exists(key_path):
                  print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
                  socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
                  print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
                  socketio.run(app, host='0.0.0.0', port=5000)
          , emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*" )

@app.route('/')
def index():
      return render_template('index.html')
  
from flask import request

@socketio.on('chat_message')
def handle_message(data):
      # Foydalanuvchi ID sini olish
      sender_id = request.siimport os
  from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
      return render_template('index.html')

  from flask import request

@socketio.on('chat_message')
def handle_message(data):
      # Foydalanuvchi ID sini olish
      sender_id = request.sid
      print(f'>>> Xabar {sender_id} dan keldi: {data}')
      # Xabar va yuboruvchi ID sini barchaga tarqatish
      socketio.emit('chat_message', {
                'msg': data,
                'sender_id': sender_iimport os
        from flask import Flask, render_template
  from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
      return render_template('index.html')

  from flask import request

@socketio.on('chat_message')
def handle_message(data):
      # Foydalanuvchi ID sini olish
      sender_id = request.sid
      print(f'>>> Xabar {sender_id} dan keldi: {data}')
      # Xabar va yuboruvchi ID sini barchaga tarqatish
      socketio.emit('chat_message', {
                'msg': data,
                'sender_id': sender_iimport os
      from flask import Flask, render_template
  from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
      return render_template('index.html')
  
from flask import request

@socketio.on('chat_message')
def handle_message(data):
      # Foydalanuvchi ID sini olish
      sender_id = request.sid
      print(f'>>> Xabar {sender_id} dan keldi: {data}')
      # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
              'msg': data,
              'sender_id': sender_    })

if __name__ == '__main__':
      cert_path = 'server.crt'
      key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
              print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
              socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
              print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
              socketio.run(app, host='0.0.0.0', port=5000)
      
    })

  if __name__ == '__main__':
        cert_path = 'server.crt'
        key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
              print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
              socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
              print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
              socketio.run(app, host='0.0.0.0', port=5000)
      
      })

  if __name__ == '__main__':
        cert_path = 'server.crt'
        key_path = 'server.key'

    if os.path.exists(cert_path) and os.path.exists(key_path):
              print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
              socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
              print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
              socketio.run(app, host='0.0.0.0', port=5000)
      
      print(f'>>> Xabar {sender_id} dan keldi: {data}')
      # Xabar va yuboruvchi ID sini barchaga tarqatish
    socketio.emit('chat_message', {
              'msg': data,
              'sender_id': sender_id
    })

if __name__ == '__main__':
      cert_path = 'server.crt'
      key_path = 'server.key'
  
    if os.path.exists(cert_path) and os.path.exists(key_path):
              print("HTTPS server 5000-portda ishga tushmoqda (SSL bilan)...")
              socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
    else:
              print("SSL sertifikatlari topilmadi. HTTP rejimida 5000-portda ishga tushmoqda...")
              socketio.run(app, host='0.0.0.0', port=5000)
      !'
socketio = SocketIO(app)

@app.route('/')
def index():import os
  from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
      return render_template('index.html')
  
from flask import request

@socketio.on('chat_message')
def handle_message(data):
      sender_id = request.sid
      socketio.emit('chat_message', {
                'msg': data,
                'sender_id': sender_id
      })
  
if __name__ == '__main__':
      cert_path = 'server.crt'
      key_path = 'server.key'
      if os.path.exists(cert_path) and os.path.exists(key_path):
                socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
      else:
                socketio.run(app, host='0.0.0.0', port=5000)import os
        from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
return render_template('index.html')

from flask import request

@socketio.on('chat_message')
def handle_message(data):
      sender_id = request.sid
      socketio.emit('chat_message', {
          'msg': data,
          'sender_id': sender_id
      })

if __name__ == '__main__':
      cert_path = 'server.crt'
      key_path = 'server.key'
      if os.path.exists(cert_path) and os.path.exists(key_path):
                socketio.run(app, host='0.0.0.0', port=5000, keyfile=key_path, certfile=cert_path)
else:
          socketio.run(app, host='0.0.0.0', port=5000)
  
