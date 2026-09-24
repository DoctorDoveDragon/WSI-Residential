FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --legacy-peer-deps
COPY . .
RUN npx next build
RUN cp -r .next/static .next/standalone/.next/ && \
    cp -r public .next/standalone/ && \
    cp -r private-docs .next/standalone/ && \
    cp -r data .next/standalone/

FROM node:20-slim AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME=0.0.0.0
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/standalone/.next/static ./.next/static
COPY --from=builder /app/.next/standalone/public ./public
COPY --from=builder /app/.next/standalone/private-docs ./private-docs
COPY --from=builder /app/.next/standalone/data ./data
EXPOSE 3000
CMD ["node", "server.js"]
