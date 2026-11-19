---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg, MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg_eq
statement: formalized
proof: formalized
---

# The Pauli constraints, as a program

A polynomial-time function outputs the Pauli constraints of an edge between two Pauli labels of Lemma [The Pauli basis test as linear constraints](../part-04/lem-intro-pauli-cons.md), from the parameters, the register length in unary and the two labelled questions, at questions of the length the Pauli sampler produces.

## Depends on

- [The Pauli basis test as linear constraints](../part-04/lem-intro-pauli-cons.md)
- [The first hiding edge as linear constraints](../part-04/lem-intro-pauli-hide.md)

## Proof

It routes the pair as the kernel does. Each check is affine in the answer bits, so its constraint vector is its values at the zero answer and at the unit vectors, which the kernel's field programs compute; a field equation gives its $k$ coordinate constraints.

## Lean

Formalized as [`MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg), [`MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliConsProg.pauliConsProg_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2107](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2107)
