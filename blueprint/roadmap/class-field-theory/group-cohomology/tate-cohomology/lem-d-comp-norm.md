---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Rep.d_comp_tateNorm
---

# d comp norm

The composition $N_G \circ d_0$ is zero.

## Depends on

- [group homology](../group-cohomology-and-homology/def-group-homology.md)

## Proof

Since the elements $\mathrm{single}(g,m)$ span $C_1(G,M)$, it's sufficient to check that these are all mapped to $0$. We have by [norm comm](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L428)

$$
N_G(d_0 (\mathrm{single}(g,m)))
= N_G( g \bullet m - m)
=	N_G( g \bullet m) - N_G(m)
= 0.
$$

## Lean

Formalized as [`Rep.d_comp_tateNorm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.d_comp_tateNorm).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 465](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L465)
