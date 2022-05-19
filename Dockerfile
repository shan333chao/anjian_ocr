FROM python:3.7-slim
COPY . ./TrWebOCR_anjian
RUN chmod +x ./TrWebOCR_anjian/docker_run.sh
RUN ./TrWebOCR_anjian/docker_run.sh
EXPOSE 8989
CMD ["supervisord","-c","/TrWebOCR_anjian/supervisord.conf"]