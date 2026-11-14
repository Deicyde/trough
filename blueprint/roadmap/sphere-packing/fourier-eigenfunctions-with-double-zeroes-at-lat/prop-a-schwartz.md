---
declaration: proposition
origin: cited
lean: MagicFunction.FourierEigenfunctions.a
statement: formalized
---

# a-schwartz

$a(x)$ is a Schwartz function.

## Depends on

- [a-definition](def-a-definition.md)

## Proof

By Theorem [smooth-fast-decay-schwartz](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/fourier-analysis.tex#L101), it suffices to show that the function is smooth and decays faster than any polynomial. The smoothness follows from the “differentiation under the integral”, which is already formalized in `mathlib`. The decay follows from Lemmas [bound-I1-I3-I5](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L206) and [bound-I2-I4-I6](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L233), together with Lemma [integral-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L175).

## Lean

Stated as [`MagicFunction.FourierEigenfunctions.a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.FourierEigenfunctions.a); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 265](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L265)
