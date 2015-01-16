def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
#Just iterate from the end of the string back to the start, appending
    revd=''
    l=len(s)-1
    while l>=0:
        revd=revd + s[l]
        l=l-1      


    return revd


def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    return s+reverse(s)

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    removed = ''
    
    for l in strng:        
        if l != letter:
            removed = removed+l

    return(removed)



def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """

    #Strip out spaces
    s = remove_letter(' ',s)
    
    #Get the length of the string and decide if its even or odd.
    length=len(s)
    if length % 2 == 0:
        n = length / 2
        front = s[:n]
        back = s[n:]
    else:
        n = (length-1) /2
        front = s[:n]
        back = s[n+1:]

        
    if front == reverse(back):
        return True
    else:
        return False




def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    lsub = len(sub)
    ls = len(s)
    
    # How many iterations do we need?
    # If lsub == ls, only 1
    # If lsub =  ls + 1, 2 iterations...
    n = (ls-lsub) + 1
    count = 0
    i = 0

    while i < n:
        test = s[i:lsub+i] # check a slice lsub long against sub
        
        if test == sub:
            count += 1
        i += 1              # then move the slice along

    return count

def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
      >>> remove('b','boob')
      'oob'
    """

    lsub = len(sub)
    ls = len(s)
    n = (ls-lsub) + 1
    i = 0
    removed = s

    while i < n:
        test = s[i:lsub+i] # check a slice lsub long against sub
        if test == sub:           
            removed = s[:i]+s[(lsub+i):] #splice together bit before sub and bit after
            return removed
        else:
            i += 1
            
    return s #only if no match found

def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    #Just call remove() repeatedly until no change is found
    before = s
    after = remove(sub,s)

    while before != after:
        before = after
        after = remove(sub,before)

    return after

def replace(word, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> replace('Mississippi', 'e', 'I')
      'Mississippi'
      >>> replace('Mississippi', 'ss', 'pp')
      'Mippippippi'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
      >>> replace(s, 'om', 'am')
      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    lsub = len(old)
    n = len(word) - lsub + 1    #the number of possible slices of the word
                            #which are the same length as the substring to be replaced

    #So I went with converting the string to a list and modifying it as I go
    #rather than string.split and string.join
    
    word_as_list = list(word)   #Change the word into a list of chars
    old_as_list = list(old)
    new_as_list = list(new)     

     
    i = 0

    while i < n:
        test = word_as_list[i:lsub + i]     #Check a slice of word lsub long
        if test == old_as_list:
            word_as_list[i:lsub + i] = new_as_list
        i += 1


    replaced = "".join(word_as_list)
    return replaced




    


if __name__ == '__main__':
    import doctest
    doctest.testmod()



dummy_prompt = raw_input('Done? ')

