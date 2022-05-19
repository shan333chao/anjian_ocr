FROM python:3.7-slim-bullseye
COPY . ./TrWebOCR_anjian
chmod +x ./TrWebOCR_anjian/docker_run.sh
RUN ./TrWebOCR_anjian/docker_run.sh
EXPOSE 8989
CMD ["supervisord","-c","/TrWebOCR_anjian/supervisord.conf"]
