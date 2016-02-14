def deep_lst_sum(n):
  if n[1] == None:
     return n[0]
  if is_int(n[0]):
     return n + deep_lst_sum(n[1:])
  elif is_list(n[0]):
     return n[0] + deep_lst_sum(n[1:])