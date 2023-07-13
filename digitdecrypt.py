class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            if num == 0:
                return 0
            identification = (num%10) + (num - num%10)/10
            return identification%9
            #TODO: Write code below to returnn an int with the solution to the prompt.
            pass
 
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()
