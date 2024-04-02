FROM node:latest

WORKDIR /client

RUN npm install -g http-server
COPY package*.json ./

RUN npm install

COPY . /client

EXPOSE 8080

CMD ["npm", "start"]
