function superDigit(n, k) {
    let s = n.toString();
    if(s.length === 1){
        return n;
    }
    s = `${s.repeat(k)}`;
    let sum = 0.0;
    for(let x = 0;x<s.length;x++){
        sum+=parseFloat(s[x]);
    }
    return superDigit(sum,1);
    

}
let x = superDigit(9875,4)
console.log(x);