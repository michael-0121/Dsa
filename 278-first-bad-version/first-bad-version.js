var solution = function(isBadVersion) {
    return function(n) {
        let start = 1;
        let end = n;
        
        while (start < end) {
            let mid = Math.floor(start + (end - start) / 2);
            if (isBadVersion(mid)) {
                end = mid; // Move left to find the first bad version
            } else {
                start = mid + 1; // Move right
            }
        }
        
        return start;
    };
};
