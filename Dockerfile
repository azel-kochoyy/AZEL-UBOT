# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# ramubot minta wkwk
# Geez-UserBot
#
RUN git clone -b RAM-UBOT https://github.com/azel-kochoyy/AZEL-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/azel-kochoyy/AZEL-UBOT/AZEL-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
