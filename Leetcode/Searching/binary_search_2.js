function testing(n) {
    let start = 1;
    let end = n;
    while(start<=end){
        let mid = start + (end-start)/2;
        if(isBadVersion(mid)){
            end = mid;
        }
        else{
            start = mid+1 ;
        }
    }
    
    return end;
    }

    function isBadVersion(n)