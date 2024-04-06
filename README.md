# Crazy Transcription
A tool which helps you to transcribe normal text to **CRAZY** text
>[!CAUTION]
>
>This project is still in development.
>
>This is neither a encryption tool nor a translator.
## Documentation
### Use its interface
1. Clone the repository
2. Run `python CrazyTranscription.py`(Use `CrazyTranscription.RichUI.py` if you have **Rich** module installed)
3. Enjoy your **CRAZY** transcription!
### Use it as a module
1. Clone the repository
2. Import the module in your code.
```python
from CrazyTranscription import *
```
3. Use the default Transcribers or create your own(See 5.).
```python
DefaultTranscribers=[LatinGreekTranscriber,LatinCyrillicTranscriber,LatinArabicTranscriber,LatinHebrewTranscriber,LatinSanskritTranscriber,LatinTibetanTranscriber]
```
4. Transcribe or Reverse Transcribe your text.
```python
print(LatinGreekTranscriber.Transcribe("Hello World"))
print(LatinGreekTranscriber.ReverseTranscribe("Ηελλο Ωορλδ"))
```
5. Create a `Transcriber` object.(optional)
```python
mapping= {
    'TH': 'Θ', 'Th': 'Θ', 'th': 'θ',
    'A': 'Α', 'a': 'α', 
    'B': 'Β', 'b': 'β', 
    'C': 'Ξ', 'c': 'ξ', 
    'D': 'Δ', 'd': 'δ', 
    'E': 'Ε', 'e': 'ε', 
    'F': 'Φ', 'f': 'φ', 
    'G': 'Γ', 'g': 'γ', 
    'H': 'Η', 'h': 'η', 
    'I': 'Ι', 'i': 'ι', 
    'J': 'Ψ', 'j': 'ψ', 
    'K': 'Κ', 'k': 'κ', 
    'L': 'Λ', 'l': 'λ', 
    'M': 'Μ', 'm': 'μ', 
    'N': 'Ν', 'n': 'ν', 
    'O': 'Ο', 'o': 'ο', 
    'P': 'Π', 'p': 'π', 
    'Q': 'Κ', 'q': 'κ', 
    'R': 'Ρ', 'r': 'ρ', 
    'S': 'Σ', 's': 'σ', 
    'T': 'Τ', 't': 'τ', 
    'U': 'Υ', 'u': 'υ', 
    'V': 'Ν', 'v': 'ν', 
    'W': 'Ω', 'w': 'ω', 
    'X': 'Χ', 'x': 'χ', 
    'Y': 'Υ', 'y': 'υ', 
    'Z': 'Ζ', 'z': 'ζ'
} # Specify your own mapping here
transcriber = Transcriber(mapping)
```
### PyPI Package
Coming soon...
## License
[MIT](https://choosealicense.com/licenses/mit/)

