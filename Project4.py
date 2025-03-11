'''Annabel Huber
CS375
Project 4
Prof. Eric Aaron
December 2022'''

edit_dist = []

def edit_dist_recursive(S, T):
	#uses recursion to calculate the edit distance 
	#transforming string S into string T
	m = len(S)
	n = len(T) 
	if m == 0 or n == 0:
		#base case, if S or T is empty
		return max(m, n)
		#returns the length of the non-empty string
		#if both are empty, returns 0

	else:
		#recursive cases
		if S[-1] == T[-1]:
			#if the last characters are the same
			edit_dist_recursive(S[:-1], T[:-1])
			#recursively call on all but the last character
		else:
			#if the last characters aren't the same
			if n == m:
				#if they're the same length
				edit_dist.append(1)
				S.replace(S[-1], T[-1])
				edit_dist_recursive(S[:-1], T[:-1])
			elif m > n:
				#if S is longer than T
				edit_dist.append(1)
				S = S[:-1]
				edit_dist_recursive(S[:-1], T[:-1])
			else:
				#if T is longer than S
				edit_dist.append(1)
				S = S + T[-1]
				edit_dist_recursive(S[:-1], T[:-1])
		return len(edit_dist)

		


# def edit_dist_iterative(S, T):
# 	#iteratively returns the edit distance from string S to string T
# 	m = len(S)
# 	n = len(T)

# 	edit_dist = 0
# 	#default edit distance

# 	if m == 0 or n == 0:
# 		#if S is empty
# 		S = T
# 		edit_dist += max(m,n)
# 		#edit distance is now the length of the non empty string
			
# 	for i in range(0, n):
# 		#loop through the length of T
# 		m = len(S)
# 		n = len(T)
# 		#reset the length variables

# 		if len(S[i:]) == 0:
# 			S = S[:i] + T[i] + S[i:]
# 			edit_dist += 1

# 		while S[i] != T[i]:
# 			#while the ith letter in S isn't the ith letter in T
# 			#if they're the same letter, moves onto the next
			
# 			m = len(S)
# 			n = len(T)
# 			#reset the length variables

# 			if m > n:
# 				#if S is longer, remove the ith letter
# 				S = S[:i] + S[i + 1:]
# 				edit_dist += 1

# 			elif n > m:
# 				#if T is longer, insert the ith letter in T
# 				S = S[:i] + T[i] + S[i:]
# 				edit_dist += 1

# 			else:
# 				#if they're the same length
# 				#replace S[i] with T[i]
# 				S = S[:i] + T[i] + S[i+1:]
# 				edit_dist += 1
# 	m = len(S)
# 	n = len(T)
# 	if S != T:
# 		S = T
# 		edit_dist += (m-n)

# 	return edit_dist, S, T




def edit_dist_iterative(S, T):
	#iteratively returns the edit distance from string S to string T
	m = len(S)
	n = len(T)

	edit_dist = 0
	#default edit distance

	if S != T:
		#if S and T aren't already the same word

		for i in range(0, max(m,n)):
			#iterate through the larger string
			m = len(S)
			n = len(T)
			#reset the length variables

			if i >= len(S):
				#if it has reached the end of string S
				edit_dist += abs(m-n)
				S = S[:i] + T[i:]
				#string S is the first i characters (already converted to the same as T[:i])
				#plus the last i characters of T
				#edit distance is the number of remaining characters in T to add
				return edit_dist


			elif i >= len(T):
				#if it has reached the end of string T
				edit_dist += abs(n-m)
				S = S[:i]
				#string S is the first i characters of S
				#edit distance is the last i characters of T to remove
				return edit_dist


			else:
				#if it hasn't reached the end of either string yet
				while S[i] != T[i]:
					#while characters i is not the same between the two strings

					if len(S) > len(T):
						#if S is longer
						S = S[:i] + S[i + 1:]
						#remove the ith character of S
						edit_dist += 1

					elif len(T) > len(S):
						#if T is longer
						S = S[:i] + T[i] + S[i:]
						#insert the ith character of T
						edit_dist += 1

					else:
						#if they're the same length
						S = S[:i] + T[i] + S[i+1:]
						#replace S[i] with T[i]
						edit_dist += 1

	return edit_dist









def spell_check(T, D):
	#for every mispelled word in T, returns 5 options with smallest edit dist from W
	suggestions = []
	#create an empty list to put the suggestions in
	T = T.split(" ")
	D = open(D).read().split()
	#split and open both T and D
	for i in range(0, len(T)):
		#run through each word in T

		temp_suggestions = []
		#tempoarary variable to hold the suggestions for each word

		if T[i] not in D:
			#if the word is mispelled i.e. not in the dictionary

			temp_min = edit_dist_iterative(T[i], D[0])
			#set a temp variable as the edit distance from the given word to the first word in the dictionary

			for j in range(0, len(D)):
				#run through the dictionary and find the minimum edit distance

				if temp_min > edit_dist_iterative(T[i], D[j]):
					temp_min = edit_dist_iterative(T[i], D[j])

			for q in range(0, 4):
				#run through 5 times, for the 5 suggested words
				
				for m in range(0, len(D)):
					#run through the dictionary again

					if len(temp_suggestions) < 5:
						#if there aren't already 5 words in suggested

						if edit_dist_iterative(T[i], D[m]) <= temp_min + q and D[m] not in temp_suggestions:
							#if the edit distance is the minimum + q
							#(first finds the words with minimum edit distance, if there arent 5
							#then find the next words with edit distance of minimum + 1 and so on)
							print(D[m], q)

							temp_suggestions.append(D[m])
							#append the suggested word to the temp variable

			suggestions.append(temp_suggestions)
			#append the list 5 of per word to the total list which will be returned

	return suggestions



t = "wandereed alogn wiithout"

#print(spell_check(t, "en_US-large.txt"))

























