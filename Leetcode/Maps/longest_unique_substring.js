var lengthOfLongestSubstring = function(s) {

    let longest = 0;
    //naive solution with double pointers
    for(let x = 0;x<s.length;x++){
        const temp = new Set(s[x]);
        for(let f = x+1;f<s.length;f++){
            if(!temp.has(s[f])){
                temp.add(s[f])
            }
            else{
                if(temp.size>longest){
                    longest = temp.size
                }
                temp.clear()
                break;
            }
        }
        if(temp.size>longest){
            longest = temp.size
        }
    }
    return longest;

};

console.log(lengthOfLongestSubstring("xxzqi"));