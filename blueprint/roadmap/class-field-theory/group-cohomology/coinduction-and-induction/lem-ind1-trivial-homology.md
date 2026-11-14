---
declaration: lemma
origin: cited
lean: Rep.trivialHomology_ind₁
statement: formalized
proof: formalized
---

# ind₁ trivial homology

The representation $\mathrm{ind}_1(G,A)$ has trivial homology.

## Depends on

- [induced](def-induced.md)
- [trivial cohomology](def-trivial-cohomology.md)
- [Shapiro's Lemma](lem-shapiro.md)

## Proof

The restriction of $\mathrm{ind}_1(G,A)$ to a subgroup $S$ is isomorphic to $\mathrm{ind}_1(S, C \to_0 A)$, where $C$ is a set of coset representatives for the cosets $cS$ of $S$ in $G$. Hence by [Shapiro's Lemma](lem-shapiro.md) we have

$$
H_n(S,\mathrm{ind}_1(G,A)) \cong H_n(S,\mathrm{ind}_1(S,C\to_0 A)\cong H_n(1,C \to_0 A).
$$

The result now follows from [homology unit](../group-cohomology-and-homology/README.md).

## Lean

Formalized as [`Rep.trivialHomology_ind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.trivialHomology_ind₁).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 833](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L833)
