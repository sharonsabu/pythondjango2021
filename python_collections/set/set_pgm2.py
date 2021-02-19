st={10,11,12,13}
st1={10,11,300}

#union of both the sets
union_set=st.union(st1)
print(union_set)

#intersection of elements
intersection_set=st.intersection(st1)
print(intersection_set)

#difference between two sets
diff_set=st.difference(st1)  #or st-st1
print(diff_set)