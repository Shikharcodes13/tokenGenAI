import tiktoken
english_letters = []
for i in range(ord('a'), ord('z') + 1):
    english_letters.append(chr(i))

hindi_varnamala = [
    
    'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः',

    'क', 'ख', 'ग', 'घ', 'ङ',
    'च', 'छ', 'ज', 'झ', 'ञ',
    'ट', 'ठ', 'ड', 'ढ', 'ण',
    'त', 'थ', 'द', 'ध', 'न',
    'प', 'फ', 'ब', 'भ', 'म',
    'य', 'र', 'ल', 'व',
    'श', 'ष', 'स', 'ह',
]

vocab = []
for char in english_letters:
    vocab.append(char)
for char in hindi_varnamala:
    vocab.append(char)
encoder = tiktoken.encoding_for_model('gpt-4o')
text="How are you doing?"
tokens = encoder.encode(text)
print("Tokens",tokens)
my_tokens=[5299, 553, 481, 5306, 30]
decoder=encoder.decode(my_tokens)
print("Decoded text",decoder)
