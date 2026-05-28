cd "C:/Users/m.pavani/Desktop/fitness 2/server"
npm install
# copy env example
cp .env.example .env   # PowerShell: Copy-Item .env.example .env
# edit .env to set MONGO_URI and JWT_SECRET (e.g. `notepad .env`)
npm run dev
