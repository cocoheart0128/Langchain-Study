colima start --arch aarch64 --cpu 4 --memory 8 --disk 60

echo "🔧 Building Docker images..."
docker-compose -f cicd/docker-compose.yaml build --no-cache
echo "🚀 Starting LangChain services..."
docker-compose -f cicd/docker-compose.yaml up -d

echo "✅ All services started!"
echo "📌 Jupyter → http://localhost:8888"
