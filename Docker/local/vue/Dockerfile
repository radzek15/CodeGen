ARG IMAGE=node:21-bookworm

FROM ${IMAGE} as client-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./client/package*.json ./

RUN npm install

COPY ./client/ ./

CMD ["npm","run","serve"]
