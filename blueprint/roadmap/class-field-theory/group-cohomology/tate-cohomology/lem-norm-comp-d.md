---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Rep.tateNorm_comp_d
---

# norm comp d

The composition $d^0 \circ N_G$ is zero.

## Depends on

Its statement uses no other node that has an article here.

## Proof

The map $d^0 : M \to (G \to M)$ is given by $(d^0 m)(g) = m - g\bullet m$. Using this formula, we obtain (by Lemma [norm comm](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L428)) $d^0 (N_G m) (g) = g \bullet N_G m - N_G m = 0$.

## Lean

Formalized as [`Rep.tateNorm_comp_d`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.tateNorm_comp_d).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 449](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L449)
