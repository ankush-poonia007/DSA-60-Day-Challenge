class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        # 1. Precompute woman preferences for O(1) comparison
        # woman_ranks[w][m] tells us the preference index of man 'm' for woman 'w'
        woman_ranks = [[0] * n for _ in range(n)]
        for w in range(n):
            for rank, m in enumerate(women[w]):
                woman_ranks[w][m] = rank
        
        # 2. Track matching status
        wife_of_man = [-1] * n       # result[i] = woman matched with man i
        husband_of_woman = [-1] * n  # man currently engaged to woman i
        
        # next_proposal[m] = the index in men[m] list that man 'm' will propose to next
        next_proposal = [0] * n
        
        # List of men who are currently free
        free_men = list(range(n))
        
        # 3. Gale-Shapley Algorithm Loop
        while free_men:
            m = free_men.pop(0)
            
            # The woman man 'm' wants to propose to next
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            # If the woman is free, they become engaged
            if husband_of_woman[w] == -1:
                husband_of_woman[w] = m
                wife_of_man[m] = w
            else:
                # She is already engaged to someone else (current_m)
                current_m = husband_of_woman[w]
                
                # If she prefers 'm' over 'current_m', she switches
                if woman_ranks[w][m] < woman_ranks[w][current_m]:
                    # Current man is dumped and becomes free
                    free_men.append(current_m)
                    wife_of_man[current_m] = -1
                    
                    # New engagement
                    husband_of_woman[w] = m
                    wife_of_man[m] = w
                else:
                    # She rejects 'm', so he stays free to propose again
                    free_men.append(m)
                    
        return wife_of_man

# Example usage:
men = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
women = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
solution = Solution()
print(solution.stableMarriage(men, women))
# Output will be a list where the index represents the man and the value at that index represents the woman he is matched with, e.g., [0, 1, 2] or any other valid stable matching depending on the preferences.
