---
declaration: definition
origin: cited
lean: Hurwitz.starRing
statement: formalized
---

# Hurwitz.starRing

There's a conjugation map (which we'll call "star") from the Hurwitz quaternions to themselves, sending integers to themselves and purely imaginary elements like $2\omega+1$ to minus themselves. It satisfies $(x^*)^*=x$, $(xy)^*=y^*x^*$ and $(x+y)^*=x^*+y^*$. In particular, the Hurwitz quaternions are a "star ring" in the sense of mathlib.

## Depends on

- [Hurwitz.ring](hurwitz-ring.md)

## Lean

Formalized as [`Hurwitz.starRing`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Hurwitz.starRing).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 571](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L571)
