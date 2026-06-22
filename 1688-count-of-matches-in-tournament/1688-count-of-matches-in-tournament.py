class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        advance=0
        while n!=1:
            if n%2==0:
                round_matches=n//2
                advance=n//2
                matches+=round_matches    
                n=advance
            else:
                round_matches=n//2
                advance=n//2+1
                matches+=round_matches 
                n=advance
        
        return matches



        