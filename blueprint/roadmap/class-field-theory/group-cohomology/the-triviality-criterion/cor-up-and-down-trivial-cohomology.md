---
declaration: corollary
origin: cited
lean: Rep.dimensionShift.up_trivialCohomology, Rep.dimensionShift.down_trivialCohomology
statement: formalized
---

# up and down trivial cohomology

If $M$ is a representation of a finite group $G$ and $M$ has trivial cohomology then $\mathrm{up}(M)$ and $\mathrm{down}(M)$ have trivial cohomology.

## Depends on

- [triviality criterion](thm-triviality-criterion.md)

## Proof

For each subgroup $S$ of $G$ we have

$$
H^1(S,\mathrm{up}(M)) \cong H^2(S,M) \cong 0,
\qquad
H^2(S,\mathrm{up}(M)) \cong H^3(S,M) \cong 0.
$$

By [triviality criterion](thm-triviality-criterion.md) $\mathrm{up}(M)$ has trivial cohomology. Similarly

$$
H^2(S,\mathrm{down}(M)) \cong H^1(S,M) \cong 0,
\qquad
H^3(S,\mathrm{down}(M)) \cong H^2(S,M) \cong 0,
$$

so $\mathrm{down}(M)$ has trivial cohomology.

## Lean

Stated as [`Rep.dimensionShift.up_trivialCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.up_trivialCohomology), [`Rep.dimensionShift.down_trivialCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.down_trivialCohomology); the blueprint marks no proof of it as formalized.

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1833](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1833)
