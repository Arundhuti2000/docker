# This is a comment

# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# COPY source destination
COPY docker /bin/goserver
ENV PORT=8991
# execute the 'echo "hello world"'
# command when the container runs
# CMD ["echo", "hello world"]

CMD ["/bin/goserver"]