# Equivalence with the constant and singleton laws

[85 laws](https://github.com/teorth/equational_theories/blob/main/equational_theories/Generated/Constant.lean) have been shown to be equivalent to the constant law ([E46](https://teorth.github.io/equational_theories/implications/?46) $({x \diamond y = z \diamond w})$), and [815 laws](https://github.com/teorth/equational_theories/blob/main/equational_theories/Generated/Singleton.lean) have been shown to be equivalent to the singleton law ([E2](https://teorth.github.io/equational_theories/implications/?2) $({x = y})$).

These are the laws up to 4 operations that follow from diagonalization of [E2](https://teorth.github.io/equational_theories/implications/?2) and [E46](https://teorth.github.io/equational_theories/implications/?46).

To formalize these in Lean, a search was run on the list of equations to discover diagonalizations of these two specific laws: equations of the form $x = R$ where $R$ doesn't include $x$, and equations of the form $x \circ y = R$ where $R$ doesn't include $x$ or $y$.

The proofs themselves all look alike, and correspond exactly to the two steps described in the proof of [Diagonalization](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/general_implications.tex#L67). The Lean proofs were generated semi-manually, using search-and-replace starting from the output of `grep` that found the diagonalized laws.

In the case of the constant law, [E41](https://teorth.github.io/equational_theories/implications/?41) $({x \diamond x = y \diamond z})$ wasn't detected using this method. It was added manually to the file with the existing proof from the sub-graph project.
