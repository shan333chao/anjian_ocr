FROM python:3.7-slim-bullseye
COPY . ./TrWebOCR_anjian
EXPOSE 8989
ENTRYPOINT ["./TrWebOCR_anjian/docker_run.sh"]
CMD ["supervisord","-c","/TrWebOCR_anjian/supervisord.conf"]
