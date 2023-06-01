# Task1
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        buy_amount = prices[i]
        for j in range(i+1, len(prices)):
            sell_amount = prices[j]
            profit = sell_amount-buy_amount
            if profit>max_profit:
                max_profit = profit
    return max_profit
        

prices = [7,1,5,3,6,4]
print("Max Profit is : ",maxProfit(prices))


prices = [7,6,4,3,1]
print("Max Profit is : ",maxProfit(prices))



# Task2

def return90DegressMatrix(matrix):
    output_matrix = []


    for i in range(len(matrix)):
        inner_output = []
        # itterate over the inner array
        for j in range(len(matrix[0])):
            # insert the j-column and i-row on top always otherwise we will get exact transpose.
            inner_output.insert(0, matrix[j][i])
        output_matrix.append(inner_output)

    return output_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Output: ",return90DegressMatrix(matrix))

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("Output: ",return90DegressMatrix(matrix))


# Task3
class Solution(object):
    def solve(self,i,j,matrix):
        if self.dp[i][j]:
            return self.dp[i][j]
        self.dp[i][j] = 1
        temp = 0
        for r in range(i-1,i+2):
            for c in range(j-1,j+2):
                if r==i and c==j or (abs(r-i)==1 and abs(c-j)==1):
                    continue
                if c>=0 and r>=0 and r<len(matrix) and c<len(matrix[0]) and matrix[r][c]>matrix[i][j]:
                    temp = max(temp,self.solve(r,c,matrix))
        self.dp[i][j]+=temp
        return self.dp[i][j]
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        self.dp = [ [0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        self.ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dp[i][j]==0:
                    self.solve(i,j,matrix)
                self.ans = max(self.ans,self.dp[i][j])
        return self.ans

ob = Solution()
print(ob.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))