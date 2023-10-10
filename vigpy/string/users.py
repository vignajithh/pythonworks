tweets="what a game, hats of to both team . welldone @patcummins @benstokes you have bought cricket back to life.Love test cricket @thebarmyarmy @cricketaus @ECB_cricket"
words=tweets.split(" ")
for w in words:
    if w.startswith("@"):
        print(w)
