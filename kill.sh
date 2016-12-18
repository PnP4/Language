alias kill8080="fuser -k -n tcp 8080"
kill -9 $(lsof -i:8080 -t)
