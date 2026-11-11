---
declaration: section
origin: cited
lean: Cslib.Language.IsRegular.singleton_word, Cslib.Language.IsRegular.of_finite, Cslib.Language.IsRegular.of_length_le
statement: formalized
proof: formalized
---

# Finite languages

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages/index.html).

## Single-word languages are regular

For every word $w$ over any alphabet, the language
whose only word is $w$ is regular.

Formalized by `Cslib.Language.IsRegular.singleton_word`, a theorem declared in [CSLibExt/Computability/Languages/Finite.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Finite.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages/index.html#singleton-word).

## Finite languages are regular

Every finite language over any alphabet is regular.

Formalized by `Cslib.Language.IsRegular.of_finite`, a theorem declared in [CSLibExt/Computability/Languages/Finite.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Finite.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages/index.html#of-finite).

## Languages of bounded word length are regular

Over a finite alphabet, if every word of a
language $L$ has length at most $n$, for some natural number $n$, then $L$ is regular.

Formalized by `Cslib.Language.IsRegular.of_length_le`, a theorem declared in [CSLibExt/Computability/Languages/Finite.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Finite.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages/index.html#of-length-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/finite-languages)
