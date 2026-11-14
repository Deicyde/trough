---
declaration: proposition
origin: cited
lean: MagicFunction.FourierEigenfunctions.a
statement: formalized
proof: formalized
---

# a-schwartz

$a(x)$ is a Schwartz function.

## Depends on

- [a-definition](def-a-definition.md)
- [phi0-bound](cor-phi0-bound.md)

## Proof depends on

- [smooth-fast-decay-schwartz](../../facts-from-fourier-analysis/thm-smooth-fast-decay-schwartz.md)

## Proof

By Theorem [smooth-fast-decay-schwartz](../../facts-from-fourier-analysis/thm-smooth-fast-decay-schwartz.md), it suffices to show that the function is smooth and decays faster than any polynomial. The smoothness follows from the “differentiation under the integral”, which is already formalized in `mathlib`. The decay follows from Lemmas [bound-I1-I3-I5](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L210) and [bound-I2-I4-I6](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L237), together with Lemma [integral-bound](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L179).

## Lean

Formalized as [`MagicFunction.FourierEigenfunctions.a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.FourierEigenfunctions.a).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 269](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L269)
