---
declaration: section
origin: cited
lean: Cslib.Automata.PDA.IsDeterministic, Cslib.Language.endMarkerEncode, Cslib.Language.endMarkerErase, Cslib.Language.encodedWords, Cslib.Language.endMarkerErase_endMarkerEncode, Cslib.Language.endMarkerEncode_injective, Cslib.Language.endMarkerDFA, Cslib.Language.endMarkerDFA_evalFrom_dead
statement: formalized
proof: formalized
---

# Deterministic context-free languages

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html).

## Automata

## Deterministic pushdown automaton

A pushdown automaton is deterministic when every transition set
has at most one element, and an available `ε`-transition precludes
every consuming transition from the same state and stack symbol.

## Sources

- Sipser, Introduction to the Theory of Computation, 3rd ed., Chapter 2 (deterministic pushdown automata); Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Automata.PDA.IsDeterministic`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#is-deterministic).

## End-marker encoding of a word

Encode a word by copying it to the left summand and appending the
end marker `Sum.inr ()`.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3 (deterministic pushdown automata, acceptance by empty stack with an end marker).

Formalized by `Cslib.Language.endMarkerEncode`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-encode).

## End-marker erasure

Erase the end marker: a left letter maps to its one-letter word,
the end marker maps to the empty word.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3 (deterministic pushdown automata, acceptance by empty stack with an end marker).

Formalized by `Cslib.Language.endMarkerErase`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-erase).

## Language of end-marker encoded words

The encodings of words over `T`: the words over `T ⊕ Unit`
consisting of left letters followed by a single end marker.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3 (deterministic pushdown automata, acceptance by empty stack with an end marker).

Formalized by `Cslib.Language.encodedWords`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#encoded-words).

## Erasing the end-marker encoding recovers the word

Erasing an encoding recovers the word.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerErase_endMarkerEncode`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-erase-end-marker-encode).

## Injectivity of the end-marker encoding

Encoding is injective.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerEncode_injective`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-encode-injective).

## DFA recognizing end-marker encodings

The DFA for the encodings: state `inl false` while reading left
letters, `inl true` after the end marker (the accepting state), and
`inr ()` dead once anything follows the end marker.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerDFA`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-dfa).

## Dead state of the encoding DFA is absorbing

The dead state of the encoding DFA stays dead.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerDFA_evalFrom_dead`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-dfa-eval-from-dead).

## Encoding DFA stays in its start state on left letters

The encoding DFA stays in its start state while reading left
letters.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerDFA_evalFrom_inl`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-dfa-eval-from-inl).

## Encoding DFA after the end marker accepts only the empty input

After the end marker, the encoding DFA can only be in its
accepting state on empty input.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerDFA_evalFrom_afterMarker`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-dfa-eval-from-after-marker).

## Encoding DFA accepts every end-marker encoding

The encoding DFA accepts exactly the encodings: it reaches the
accepting state on an encoding.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.endMarkerDFA_evalFrom_encode`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#end-marker-dfa-eval-from-encode).

## Encoding DFA accepts only end-marker encodings

The encoding DFA reaches the accepting state only on encodings.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.exists_endMarkerEncode_of_endMarkerDFA_evalFrom`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#exists-end-marker-encode-of-end-marker-d).

## End-marker encodings form a regular language

The encodings of words form a regular language.

## Sources

- Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.isRegular_encodedWords`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#is-regular-encoded-words).

## Deterministic context-free language

A language is deterministic context-free when some deterministic
pushdown automaton with finite state and stack alphabets, whose
transitions consume letters from a finite set, accepts by empty stack
exactly the end-marker encodings of its words.

## Sources

- Ginsburg and Greibach, "Deterministic context free languages", Information and Control 9 (1966), 620-648; Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.IsDeterministicContextFree`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#is-deterministic-context-free).

## Deterministic context-free languages are context-free

Every deterministic context-free language is context-free: the
encoded language is accepted by a pushdown automaton, hence
context-free; intersecting with the regular language of encodings and
erasing the end marker recovers the original language.

## Sources

- Ginsburg and Greibach, "Deterministic context free languages", Information and Control 9 (1966), 620-648; Hopcroft, Motwani, and Ullman, Introduction to Automata Theory, Languages, and Computation, 3rd ed., Section 10.3.

Formalized by `Cslib.Language.IsDeterministicContextFree.isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Deterministic.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Deterministic.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html#is-context-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deterministic context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/deterministic-context-free-languages)
