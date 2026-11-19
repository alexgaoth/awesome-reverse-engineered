FROM python:3.12-slim
# The MCP Registry checks this label against the name in server.json.
LABEL io.modelcontextprotocol.server.name="io.github.alexgaoth/awesome-reverse-engineered" \
      org.opencontainers.image.source="https://github.com/alexgaoth/awesome-reverse-engineered" \
      org.opencontainers.image.description="MCP server for awesome-reverse-engineered: 17,000+ open-source tools built by reverse engineering" \
      org.opencontainers.image.licenses="MIT"
WORKDIR /app
COPY reverse_engineered_mcp.py re_index.py ./
ENTRYPOINT ["python3", "reverse_engineered_mcp.py"]
