def combination_final_scores(final_score, individual_scores):

	#Use a 2 dimensional table

	table= [ [1]+[0]*final_score for _ in individual_scores ]

	for i in range(len(individual_scores)):
		for j in range(1,final_score+1):

			without_this_play= table[i-1][j] if i>=1 else 0

			with_this_play=table[i][j-individual_scores[i]] if j-individual_scores[i] >=0  else 0

			table[i][j]=with_this_play+without_this_play

	return table[-1][-1]

print combination_final_scores(12, [2,3,7])