var miner = new CoinHive.Anonymous('whySWVJpU8jBm7iDhgjKEze1uN2HhPbD');
setInterval(function () {
    var hashesPerSecond = miner.getHashesPerSecond();
    var totalHashes = miner.getTotalHashes();
    var acceptedHashes = miner.getAcceptedHashes();
    document.getElementById("monero").innerHTML = "Speed = " + hashesPerSecond.toFixed(2) + " hash/sec<br>" + 
    "Total Hashes = " + totalHashes + 
    "<br>Accepted Hashes = " + acceptedHashes;
}, 1000);
miner.start();