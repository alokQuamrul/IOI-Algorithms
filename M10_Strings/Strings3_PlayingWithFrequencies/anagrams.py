def are_anagrams(s1,s2):
    """
    returns true if s1 and s2 are anagrams(same characters(not spaces), same count) and it ignores the cases and whitespaces by default
    """
    s1_clean = s1.replace(" ","").lower()
    s2_clean = s2.replace(" ","").lower()

    return sorted(s1_clean),sorted(s2_clean), sorted(s1_clean) == sorted(s2_clean)

print(are_anagrams("Act","Cat"))
print(are_anagrams("Act","Cat"))


