# OnboardAI

This is Employee Assistant built at AgiHouse hackathon 
# Install Backend
1. Set the secrets:
```
export LIVEKIT_API_KEY=
export LIVEKIT_API_SECRET=
export LIVEKIT_API_URL=https://x.livekit.cloud
export LIVEKIT_URL=https://x.livekit.cloud
export ROOM_TOKEN=x 
export TUNE_API_KEY=x
```
2. Run agent:
```
python3 agent.py start
```

# Install Frontend

Set the secrets:
1. Set the credentials for Livekit:
```
NEXT_PUBLIC_LIVEKIT_URL=wss://x.livekit.cloud
LIVEKIT_API_KEY=xx             
LIVEKIT_API_SECRET=xx
```

2. Run ui locally:
```
cd ui
yarn install
yarn dev
```