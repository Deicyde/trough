---
declaration: definition
origin: cited
lean: Rep.TrivialCohomology, Rep.TrivialHomology, Rep.TrivialTateCohomology
statement: formalized
---

# trivial cohomology

Let $M$ be a representation of $G$ over a ring $R$.

- $M$ is said to have *trivial cohomology* if for every subgroup $S \le G$ and every $n > 0$, $H^n(S,M) \cong 0$.
- $M$ is said to have *trivial homology* if for every subgroup $S \le G$ and every $n > 0$, $H_n(S,M) \cong 0$.
- Suppose the group $G$ is finite. Then $M$ is said to have *trivial Tate cohomology* if for every subgroup $S \le G$ and every $n \in {\mathbb Z}$, $H^n_{\mathrm{Tate}}(S,M) \cong 0$.

(We will later see that for a finite group $G$, the three concepts are equivalent.)

## Depends on

- [group homology](../group-cohomology-and-homology/def-group-homology.md)
- [inflation restriction functors](../group-cohomology-and-homology/def-inflation-restriction-functors.md)

## Lean

Formalized as [`Rep.TrivialCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.TrivialCohomology), [`Rep.TrivialHomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.TrivialHomology), [`Rep.TrivialTateCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.TrivialTateCohomology).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 630](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L630)
