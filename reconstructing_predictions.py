 # reconstruct by getting the first overlapped/2 items from the first part and second overlapped/2 items from second part
def reconstruct_overlapped(lst,overlap):
  final_lst = []
  overlap_by2= int(overlap/2)
  final_lst += lst[0][:-overlap_by2]
  for i in range(len(lst)-2):
    final_lst += lst[i+1][overlap_by2:-overlap_by2]
  final_lst +=lst[-1][overlap_by2:]
  return final_lst


# combine overlaps of one example into a list
# shape: (n_examples, different_n_of_overlaps_for_each_example)
current_ind = indecies[0][:-2] #only works if the last part is a single digit (no more than 10 overlapping passages for a single training sentence)
ovr_preds = []
single_ovr_pred =[]
for lst_preds,index in zip(preds_list,indecies):
  # done with the overlapses of one sentence and checking a new one
  if(current_ind != index[:-2]): #only works if the last part is a single digit
    ovr_preds.append(single_ovr_pred)
    single_ovr_pred =[]
    current_ind = index[:-2]
  single_ovr_pred.append(lst_preds)
ovr_preds.append(single_ovr_pred)

# reconstruct the original examples 
special_preds = []
for lst in ovr_preds:
  special_preds.append(reconstruct_overlapped(lst,overlap=30))

# replace the old special examples predictions (not fully processed ones) with the new ones (after performing overlapping) 
# in the original predictions list (preds_list) so we can calculate a score for all examples
# replace the prediction of the special one and calc the total score
for i in range(len(special_preds)):
  preds_list[long_sequences[i]] = special_preds[i]
  