def rubin_karp(pat, txt, prime_for_hashing, possible_chars): 
    M = len(pat) 
    N = len(txt) 
    pattern_hash = 0   
    txt_hash = 0    
    h = 1
  
    for i in range(M-1): 
        h = (h * possible_chars)% prime_for_hashing 

    for i in range(M): 
        pattern_hash = (possible_chars * pattern_hash + ord(pat[i]))% prime_for_hashing 
        txt_hash = (possible_chars * txt_hash + ord(txt[i]))% prime_for_hashing 
  
    for i in range(N-M + 1): 
        if (pattern_hash == txt_hash): 

            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break

            j+= 1
          
            if (j == M): 
                print ("Pattern found at index " + str(i) )
  
       
        if (i < N-M): 
            t = (possible_chars*(txt_hash-ord(txt[i])*h) + ord(txt[i + M]))% prime_for_hashing 
  
            
            if (t < 0): 
                t = t + prime_for_hashing 
  

txt = "Word is Present. Word!"
pat = "Word"
prime_for_hashing = 32452867 
possible_chars = 256
rubin_karp(pat, txt, prime_for_hashing, possible_chars)