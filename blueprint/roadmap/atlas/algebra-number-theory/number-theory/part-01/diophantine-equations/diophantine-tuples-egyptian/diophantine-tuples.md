---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.IsDiophantineTuple, MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.Statement, MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.Statement_holds
statement: formalized
---

# Diophantine tuples

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples/index.html).

## Diophantine tuples

A finite set $s$ of natural numbers is a Diophantine tuple when every
element of $s$ is positive and, for all $a, b \in s$ with $a < b$, the number $ab + 1$ is a perfect
square.

## Sources

- OPG-16555 (Diophantine quintuple conjecture) [OpenGarden].

Formalized by `MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.IsDiophantineTuple`, a definition declared in [WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples/index.html#is-diophantine-tuple).

## The statement that no Diophantine quintuple exists

The proposition that no finite set of
natural numbers with exactly five elements is a Diophantine tuple, that is, that there is no
Diophantine quintuple.

## Sources

- OPG-16555 (Diophantine quintuple conjecture) [OpenGarden].

Formalized by `MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.Statement`, a definition declared in [WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples/index.html#statement).

## There is no Diophantine quintuple

The statement that no Diophantine quintuple exists holds:
no finite set of natural numbers with exactly five elements is a Diophantine tuple.

This was an open conjecture, resolved by He, Togbé, and Ziegler.

## Sources

- Bo He, Alain Togbé, and Volker Ziegler, There is no Diophantine quintuple, Transactions of the American Mathematical Society 371 (2019), 6665–6709, https://doi.org/10.1090/tran/7573.

Stated but not proved: `MathlibExt.NumberTheory.DiophantineQuintupleConjectureQuestion1Wanted.Statement_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiophantineQuintupleConjectureQuestion1Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples/index.html#statement-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diophantine tuples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/diophantine-tuples)
