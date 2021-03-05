mkdir -p fdroid
sudo chown 999:999 fdroid

docker run \
    -p 5000:5000 \
    -v "$PWD/fdroid:/data/fdroid:Z" \
    -e LANG_TIMEZONE="America/Chicago" \
    -e DEVICE_CODE=sailfish \
    solidhal/playmaker
