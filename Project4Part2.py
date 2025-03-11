'''Annabel Huber
CS375
Project 4
Prof. Eric Aaron
December 2022'''

import time
#to time the functions

edit_dist = 0

def edit_dist_recursive(S, T):
	#uses recursion to calculate the edit distance 
	#transforming string S into string T
	global edit_dist

	S = S.lower()
	T = T.lower()
	#lowercase both strings
	m = len(S)
	n = len(T) 
	#define m and n
	if m == 0 or n == 0:
		#base case, if S or T is empty
		edit_dist += (max(m, n))
		return edit_dist
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
				edit_dist += 1
				#replace
				S = S[:-1] + T[-1]
				edit_dist_recursive(S[:-1], T[:-1])
			elif m > n:
				#if S is longer than T
				edit_dist += 1
				#delete
				S = S[:-1]
				edit_dist_recursive(S[:-1], T[:-1])
			else:
				#if T is longer than S
				edit_dist += 1
				#insert
				S = S + T[-1]
				edit_dist_recursive(S[:-1], T[:-1])
		return edit_dist

		




def edit_dist_iterative(S, T):
	#iteratively returns the edit distance from string S to string T
	S = S.lower()
	T = T.lower()
	m = len(S)
	n = len(T)

	edit_dist = 0
	#default edit distance

	if S != T:
		#if S and T aren't already the same word

		for i in range(0, max(m,n)):
			#iterate through the larger string
			#reset the length variables

			if i >= min(m,n):
				#if it has reached the end of the shorter string
				edit_dist += abs(len(S)-len(T))
				#the edit distance is the difference in characters between the two
				return edit_dist


			else:
				#if it hasn't reached the end of either string yet
				while S[i] != T[i]:
					#while characters i is not the same between the two string

					if m > n:
						#if S is longer
						m = m - 1
						S = S[:i] + S[i + 1:]
						#remove the ith character of S
						edit_dist += 1

					elif n > m:
						#if T is longer
						m = m + 1
						S = S[:i] + T[i] + S[i:]
						#insert the ith character of T
						edit_dist += 1

					else:
						#if they're the same length
						S = S[:i] + T[i] + S[i+1:]
						#S[i] = T[i]
						#replace S[i] with T[i]
						edit_dist += 1

	return edit_dist



def spell_check(T, D):
	#for every mispelled word in T, returns 5 options with smallest edit dist from W
	suggestions = []
	#create an empty list to put the suggestions in


	D = open(D).read().split()
	#split and open D 


	for b in T:
			#remove special characters and exclude numbers
		if b.isalpha() == False:
				#if character b in T[i] is a special character or number
			if b == "'":
				b = b
				#except apostraphies, which are included in the dictionary
			else:
				T = T.replace(b, " ")
				#remove it

	T = T.split()

	for i in range(0, len(T)):
		#run through each word in T

		if len(T[i]) > 0:
			#if T[i] contains characters after having special characters and numbers removed

			temp_min = edit_dist_iterative(T[i], D[0])
			#temporary variable for the minimum edit distance

			for j in range(0, len(D)):

				#D[j] = D[j].lower()
				#run through the dictionary
				#if temp_min != 0:

				if temp_min > edit_dist_iterative(T[i], D[j]):
					temp_min = edit_dist_iterative(T[i], D[j])
					#if temp distance is zero break the loop
						#redefine the edit distance for the minimum
				if temp_min == 0:
					#print("breaking")
					break
	

			if temp_min > 0:
					#if the word is not in D
				print("misspelled", T[i])

				temp_suggestions = []
				#empty list to hold suggestions for T[i]

				for q in range(0, 4):
					#5 loops for 5 suggestions

					if len(temp_suggestions) < 5:
						#if there aren't 5 suggestions already added

						for m in range(0, len(D)):
							#loop through the dictionary

							#D[m] = D[m].lower()

							if edit_dist_iterative(T[i], D[m]) == temp_min + q and D[m].lower() not in suggestions and len(temp_suggestions) < 5:
								#if the edit dist is the minimum + q and the word is not already in suggestions
								temp_suggestions.append(D[m])

				suggestions.append(temp_suggestions)

	return suggestions

#part 2

def make_dictionary375(D):
	#makes the CS375 specific dictionary using the given text file 
	CS375_dictionary = []

	D = open(D).read()

	for b in D:
		#remove special characters and exclude numbers
		if b.isalpha() == False:
			#if character b in T[i] is a special character or number
			if b == "'":
				b = b
			#except apostraphies, which are included in the dictionary
			else:
				D = D.replace(b, " ")

	D = D.split()

	for i in range(len(D)):
		#loop through the text file
		if D[i] not in CS375_dictionary:
			#if this is the first occurence of the word
			 CS375_dictionary.append(D[i])
			 #append it
			 #doesn't append repeats

	return CS375_dictionary




def spell_check375(T, D):
	#spell check using regular dictionary and the CS375 specific dictionary 
	#for every mispelled word in T, returns 5 options with smallest edit dist 
	D_375 = make_dictionary375("dictionary.txt")
	#make the CS375 specific dictionary
	suggestions = []
	#create an empty list to put the suggestions in

	for b in T:
			#remove special characters and exclude numbers
		if b.isalpha() == False:
				#if character b in T[i] is a special character or number
			if b == "'":
				b = b
				#except apostraphies, which are included in the dictionary
			else:
				T = T.replace(b, " ")
				#remove it

	T = T.split()

	D = open(D).read().split()
	#split and open D
	for i in range(0, len(T)):
		#run through each word in T

		temp_min = edit_dist_iterative(T[i], D[0])
		#temporary variable for minimum edit distance

		for p in range(0, len(D)):
			#loop through dictionary D
			#lowercase every character
			#stop the loop if temp min is 0

			if temp_min > edit_dist_iterative(T[i], D[p]):
					temp_min = edit_dist_iterative(T[i], D[p])
					#find the minimum edit distance

			if temp_min == 0:
					#print("breaking")
				break

		if temp_min != 0:

			for w in range(0, len(D_375)):
			#run through CS375 specific dictionary

				if temp_min > edit_dist_iterative(T[i], D_375[w]):
					temp_min = edit_dist_iterative(T[i], D_375[w])

				if temp_min == 0:
					#print("breaking")
					break

		#edit distance is the minimum between the two dictionaries

		if temp_min > 0:
			#if the word is mispelled
			print("misspelled", T[i])

			temp_suggestions = []
			#tempoarary variable to hold the suggestions for each word

			for q in range(0, 4):
				#run through 5 times, for the 5 suggested words

				if len(temp_suggestions) < 5:
					#if there aren't already 5 words in suggested

					for m in range(0, len(D_375)):
						#run through the CS375 dictionary again

						if edit_dist_iterative(T[i], D_375[m]) == temp_min + q and len(temp_suggestions) < 5:
							#if the edit distance is the minimum + q
								#(first finds the words with minimum edit distance, if there arent 5
								#then find the next words with edit distance of minimum + 1 and so on)
							if D_375[m].lower() not in temp_suggestions:
								#if the word isn't already suggested

								temp_suggestions.append(D_375[m])
									#append the suggested word to the temp variable
							
					for j in range(0, len(D)):
						#run through the dictionary again

						if edit_dist_iterative(T[i], D[j]) <= temp_min + q and len(temp_suggestions) < 5:
							#same process as above 

							if D[j].lower() not in temp_suggestions:

								temp_suggestions.append(D[j])
									#append the suggested word to the temp variable

			suggestions.append(temp_suggestions)
			#append the list 5 of per word to the total list which will be returned

	return suggestions

#part 3


def make_dictionary375_improve(D):
	#creates the CS375 dictionary as the dictionary varaible-type
	D_375 = {}
	#empty dictionary
	D = open(D).read()

	for b in D:
		#remove special characters and exclude numbers
		if b.isalpha() == False:
			#if character b in T[i] is a special character or number
			if b == "'":
				b = b
			#except apostraphies, which are included in the dictionary
			else:
				D = D.replace(b, " ")

	D = D.split()

	for i in range(0, len(D)):

		if D[i] not in D_375:
			#if the word isn't already in D_375
			#create a dictionary with value 1
			D_375[D[i]] = 1
		else:
			#if the word is already in D_375
			#add one to the value
			D_375[D[i]] += 1

	return D_375


def make_dictionary(D, D375):
	dictionary = {}
	dictionary375 = make_dictionary375_improve(D375)

	D = open(D).read().split()

	for i in range(0, len(D)):
		#add a value of 1 to each word in the regular dictionary
		#make them all lowercase

		dictionary[D[i]] = 1

	#combine the dictionaries into one

	for j in dictionary375:
		#run through the CS375 dictionary
		if j in dictionary:
			#if the word is in the dictionary
			dictionary[j] = dictionary375[j] + 1
			#add one to the value from CS375
		else:
			dictionary[j] = dictionary375[j]
			#otherwise append it with the value from CS375 dictionary

	return dictionary








def spell_check375_improve(T, D, D375):
	#uses dictionary-type data structures to return better suggestions based on the number of times they appear
	#in CS375 dictionary + regualr dictionary
	#for every mispelled word in T, returns 5 options with smallest edit dist
	#make the CS375 specific dictionary
	D = make_dictionary(D, D375)
	#make the regualar dictionary (from a list to a dictionary data type)
	
	suggestions = []
	#create an empty list to put the suggestions in

	for b in T:
			#remove special characters and exclude numbers
		if b.isalpha() == False:
				#if character b in T[i] is a special character or number
			if b == "'":
				b = b
				#except apostraphies, which are included in the dictionary
			else:
				T = T.replace(b, " ")
				#remove it

	T = T.split()

	D_keys = list(D.keys())
	#make a list of just the keys of D
	for i in range(0, len(T)):
		#run through each word in T

		temp_min = edit_dist_iterative(T[i], D_keys[0])
		#temporary variable for minimum edit distance

		for p in range(0, len(D_keys)):
			#loop through dictionary D

			if temp_min > edit_dist_iterative(T[i], D_keys[p]):
					#reassign the temp variable if it's lower
					temp_min = edit_dist_iterative(T[i], D_keys[p])
			if temp_min == 0:
					#print("breaking")
				break


		if temp_min > 0:
		#if the word is mispelled
			print("misspelled", T[i])

			temp_suggestions = []
			#tempoarary variable to hold the suggestions for each word

			for q in range(0, 4):
				#run through 5 times, for the 5 suggested words
				if len(temp_suggestions) < 5:

					for m in range(0, len(D_keys)):
							#run through the dictionary again

						if edit_dist_iterative(T[i], D_keys[m]) == temp_min + q:

							if D_keys[m].lower() not in temp_suggestions:
									#if the edit distance is the minimum + q
									#(first finds the words with minimum edit distance, if there arent 5
									#then find the next words with edit distance of minimum + 1 and so on)
								temp_suggestions.append(D_keys[m])
									#append the suggested word to the temp variable

				if len(temp_suggestions) >= 5:
					#if there are more than 5 words with equal edit distances

					keys_values = {}
					#make an empty dictionary

					for k in range(len(temp_suggestions)):
						#make a dictionary of each suggested word and its value
				
						keys_values[temp_suggestions[k]] =  D[temp_suggestions[k]]
				
					#temp suggestions now contains both the keys and values

					temp_suggestions = sorted(keys_values.items(), key = lambda item: item[1])
					#sort in ascending order based on their value

					for j in range(1, 6):
						#append the 5 words with the highest 
					
						suggestions.append(temp_suggestions[-j])
					break


	return suggestions


#to test the spells check on Project 4, uncomment the lines below -- dictionary.txt and CS375Project4.txt are in submitted work
# t = open("CS375Project4.txt").read()

# print(spell_check(t, "en_US-large.txt"))
# print(spell_check375(t, "en_US-large.txt"))
# print(spell_check375_improve(t, "en_US-large.txt", "dictionary.txt"))

#to compare the three spell checks, uncomment the code below:

# t = "I wrote my algorithm in psudoscode to make more simple subproblems"

# print(t)
# print("regular:", spell_check(t, "en_US-large.txt"))
# print("domain-specific:", spell_check375(t, "en_US-large.txt"))
# print("improved:", spell_check375_improve(t, "en_US-large.txt", "dictionary.txt"))

















