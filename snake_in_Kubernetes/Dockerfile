# Use a lightweight stable Python image
FROM python:3.11-slim

# Install Kerberos, Xvfb, Tkinter, and a VNC server
RUN apt-get update && apt-get install -y \
    krb5-user \
    xvfb \
    python3-tk \
    x11vnc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY main.py snake.py food.py scoreboard.py ./

ENV KRB5_CONFIG=/etc/krb5.conf
ENV KRB5CCNAME=/tmp/krb5cc_snake

# Start Xvfb, wait for it to spin up, start x11vnc on port 5900, then execute the game loop
CMD ["sh", "-c", "Xvfb :99 -screen 0 600x600x16 & sleep 2 && x11vnc -display :99 -nopw -forever -bg -rfbport 5900 && DISPLAY=:99 python main.py"]
