class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice=0
        bob=0
#         i=0
#         queue=[]
#         while (i<len(piles)):
#             alice=max(piles[i]+alice,alice+piles[-i]
#             bob=max(piles[i+1]+bob,bob+piles[-(i+1)]
#             i+=2
            
#         if alice>bob:
#             return True
#         else:
#             return False
        for i in piles:
            mn=piles.pop(piles.index(max(piles)))
            alice+=mn
            mn2=piles.pop(piles.index(max(piles)))
            bob+=mn2
            
        if alice>bob:
            return True
        else:
            return False