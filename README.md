# Kivy + Buildozer Docker workflow

This starter project builds a debug Android APK from a minimal Kivy application.

## Requirements

- Docker Engine or Docker Desktop
- Docker Compose v2

## Build locally

```bash
docker compose build
docker compose run --rm buildozer
```

The APK should be generated in `bin/`.

## Build with Docker directly

```bash
docker build -t my-buildozer:latest .
docker run --rm \
  -v "$PWD:/home/user/hostcwd" \
  -v buildozer-cache:/home/user/.buildozer \
  -w /home/user/hostcwd \
  my-buildozer:latest \
  buildozer android debug
```

## GitHub Actions

Push the project to a GitHub repository on the `main` branch. The workflow in
`.github/workflows/android.yml` builds the APK and uploads it as the
`android-debug-apk` artifact. You can also start it manually from the Actions tab.

## Notes

- The first Android build may take a while while SDK/NDK dependencies are downloaded.
- The base image uses `kivy/buildozer:latest`; for reproducible production builds,
  pin and test a specific image version.
- Release builds require signing configuration; this workflow creates a debug APK.
