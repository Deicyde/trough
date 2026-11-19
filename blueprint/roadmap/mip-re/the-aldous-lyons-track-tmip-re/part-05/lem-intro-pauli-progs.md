---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg, MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg, MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg_eq, MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg_eq, MIPRE.Tailored.Intro.PauliConsProg.zGuardProg, MIPRE.Tailored.Intro.PauliConsProg.zGuardProg_eq
statement: formalized
proof: formalized
---

# The Pauli constraints of the first hiding edge, as programs

Polynomial-time functions output the constraints of the first hiding edge in either order, from the parameters, the first factor as a mask and the kernel generators; and decide whether the $Z$-basis answer projects to a given register.

## Depends on

- [The first hiding edge as linear constraints](../part-04/lem-intro-pauli-hide.md)

## Proof

Every coefficient is an inner product of the generator, restricted to the factor, with a column of the self-dual coordinate map, or a unit vector.

## Lean

Formalized as [`MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg), [`MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg), [`MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHideProg.pauliHideProg_eq), [`MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHideProg.pauliHideRevProg_eq), [`MIPRE.Tailored.Intro.PauliConsProg.zGuardProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliConsProg.zGuardProg), [`MIPRE.Tailored.Intro.PauliConsProg.zGuardProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliConsProg.zGuardProg_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2087](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2087)
