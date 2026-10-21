FROM kivy/buildozer:latest

WORKDIR /home/user/hostcwd

ENV BUILDOZER_WARN_ON_ROOT=0

CMD ["buildozer", "android", "debug"]
