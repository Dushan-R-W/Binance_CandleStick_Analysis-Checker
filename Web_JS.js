// import fs from 'node:fs/promises';


function signal(signalNumber, entryprice, date, leverage, tp1, tp2, tp3, tradetype, coin){
    this.make = signalNumber;
    this.make = entryprice;
    this.make = date;
    this.make = leverage
    this.make = tp1
    this.make = tp2
    this.make = tp3
    this.make = tradetype
    this.make = coin
}

const signal1 = new signal();
const signal2 = new signal();
const signal3 = new signal();
const signal4 = new signal();
const signal5 = new signal();
const signal6 = new signal();

document.getElementById("button1").addEventListener("click", getInputs1);
document.getElementById("button2").addEventListener("click", getInputs2);
document.getElementById("button3").addEventListener("click", getInputs3);
document.getElementById("button4").addEventListener("click", getInputs4);
document.getElementById("button5").addEventListener("click", getInputs5);
document.getElementById("button6").addEventListener("click", getInputs6);

function getInputs1(){
    var signalnumber = 1;
    var entryprice = document.getElementById("entryPrice1").value;
    var date = document.getElementById("datetime1").value;
    var leverage = document.getElementById("leverage1").value;
    var tp1 = document.getElementById("Target1_1").value;
    var tp2 = document.getElementById("Target2_1").value;
    var tp3 = document.getElementById("Target3_1").value;
    var tradetype = document.getElementById("tradeType1").value;
    var coin = document.getElementById("CoinName1").value;
    if (coin != "") {
        signal1.signal = signalnumber
        signal1.entryprice = entryprice
        signal1.date = date
        signal1.leverage = leverage
        signal1.tp1 = tp1
        signal1.tp2 = tp2
        signal1.tp3 = tp3
        signal1.tradetype = tradetype
        signal1.coin = coin
    }
}

function getInputs2(){
    var signalnumber = 2;
    var entryprice = document.getElementById("entryPrice2").value;
    var date = document.getElementById("datetime2").value;
    var leverage = document.getElementById("leverage2").value;
    var tp1 = document.getElementById("Target1_2").value;
    var tp2 = document.getElementById("Target2_2").value;
    var tp3 = document.getElementById("Target3_2").value;
    var tradetype = document.getElementById("tradeType2").value;
    var coin = document.getElementById("CoinName2").value;
    if (coin != "") {
        signal2.signal = signalnumber
        signal2.entryprice = entryprice
        signal2.date = date
        signal2.leverage = leverage
        signal2.tp1 = tp1
        signal2.tp2 = tp2
        signal2.tp3 = tp3
        signal2.tradetype = tradetype
        signal2.coin = coin
    }
}

function getInputs3(){
    var signalnumber = 3;
    var entryprice = document.getElementById("entryPrice3").value;
    var date = document.getElementById("datetime3").value;
    var leverage = document.getElementById("leverage3").value;
    var tp1 = document.getElementById("Target1_3").value;
    var tp2 = document.getElementById("Target2_3").value;
    var tp3 = document.getElementById("Target3_3").value;
    var tradetype = document.getElementById("tradeType3").value;
    var coin = document.getElementById("CoinName3").value;
    if (coin != "") {
        signal3.signal = signalnumber
        signal3.entryprice = entryprice
        signal3.date = date
        signal3.leverage = leverage
        signal3.tp1 = tp1
        signal3.tp2 = tp2
        signal3.tp3 = tp3
        signal3.tradetype = tradetype
        signal3.coin = coin
    }
}

function getInputs4(){
    var signalnumber = 4;
    var entryprice = document.getElementById("entryPrice4").value;
    var date = document.getElementById("datetime4").value;
    var leverage = document.getElementById("leverage4").value;
    var tp1 = document.getElementById("Target1_4").value;
    var tp2 = document.getElementById("Target2_4").value;
    var tp3 = document.getElementById("Target3_4").value;
    var tradetype = document.getElementById("tradeType4").value;
    var coin = document.getElementById("CoinName4").value;
    if (coin != "") {
        signal4.signal = signalnumber
        signal4.entryprice = entryprice
        signal4.date = date
        signal4.leverage = leverage
        signal4.tp1 = tp1
        signal4.tp2 = tp2
        signal4.tp3 = tp3
        signal4.tradetype = tradetype
        signal4.coin = coin
    }
}

function getInputs5(){
    var signalnumber = 5;
    var entryprice = document.getElementById("entryPrice5").value;
    var date = document.getElementById("datetime5").value;
    var leverage = document.getElementById("leverage5").value;
    var tp1 = document.getElementById("Target1_5").value;
    var tp2 = document.getElementById("Target2_5").value;
    var tp3 = document.getElementById("Target3_5").value;
    var tradetype = document.getElementById("tradeType5").value;
    var coin = document.getElementById("CoinName5").value;
    if (coin != "") {
        signal5.signal = signalnumber
        signal5.entryprice = entryprice
        signal5.date = date
        signal5.leverage = leverage
        signal5.tp1 = tp1
        signal5.tp2 = tp2
        signal5.tp3 = tp3
        signal5.tradetype = tradetype
        signal5.coin = coin
    }
}


function getInputs6(){
    var signalnumber = 6;
    var entryprice = document.getElementById("entryPrice6").value;
    var date = document.getElementById("datetime6").value;
    var leverage = document.getElementById("leverage6").value;
    var tp1 = document.getElementById("Target1_6").value;
    var tp2 = document.getElementById("Target2_6").value;
    var tp3 = document.getElementById("Target3_6").value;
    var tradetype = document.getElementById("tradeType6").value;
    var coin = document.getElementById("CoinName6").value;
    if (coin != "") {
        signal6.signal = signalnumber
        signal6.entryprice = entryprice
        signal6.date = date
        signal6.leverage = leverage
        signal6.tp1 = tp1
        signal6.tp2 = tp2
        signal6.tp3 = tp3
        signal6.tradetype = tradetype
        signal6.coin = coin
    }
}

document.getElementById("saveSig1").addEventListener("click", () => {
    saveSignalData("1");
});
document.getElementById("saveSig2").addEventListener("click", () => {
    saveSignalData("2");
});
document.getElementById("saveSig3").addEventListener("click", () => {
    saveSignalData("3");
});
document.getElementById("saveSig4").addEventListener("click", () => {
    saveSignalData("4");
});
document.getElementById("saveSig5").addEventListener("click", () => {
    saveSignalData("5");
});
document.getElementById("saveSig6").addEventListener("click", () => {
    saveSignalData("6");
});


function saveSignalData(signalNum){
    console.log(signalNum)
    var name = "signal"+signalNum;
    console.log(name)

    const fs = require('fs');
    // Data which will write in a file. 
    let data = name
    // Write data in 'Output.txt' . 
    fs.writeFile('Output.txt', data, (err) => { 
        if (err) throw err; 
    }) 
}

