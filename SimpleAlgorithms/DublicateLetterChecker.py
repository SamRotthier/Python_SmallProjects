def main():
    chosen_word: str = input('What is letter combination or word you want to check for its firs dublicate letter? >>')
    seen_letters = []
    for c in chosen_word.lower():
          if c in seen_letters:
                print(f'Found a dubblicate letter: {c}')
                return 
          else:
                seen_letters.append(c)
                print(seen_letters)
    

if __name__ == '__main__':
        main()