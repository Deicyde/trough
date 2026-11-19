---
declaration: lemma
origin: cited
lean: Rep.trivialCohomology_coind₁
statement: formalized
proof: formalized
---

# coind₁ trivial cohomology

The representation $\mathrm{coind}_1(G,A)$ has trivial cohomology.

## Depends on

- [trivial cohomology](def-trivial-cohomology.md)
- [induced](def-induced.md)
- [Shapiro's Lemma](lem-shapiro.md)
- [Hn unit](../group-cohomology-and-homology/lem-hn-unit.md)

## Proof

Let $S$ be a subgroup of $G$ and let $C$ be a set of representatives for the cosets $cS$ of $S$ in $G$. There is an isomorphism of $S$-representations

$$
\mathrm{coind}_1(G,M) \downarrow S
\cong
\mathrm{coind}_1(S,C \to M).
$$

This isomorphism takes a function $f : G \to M$ to function $S \to (C \to M)$ defined by $s \mapsto (c \mapsto f(cs))$.

The isomorphism, together with [Shapiro's Lemma](lem-shapiro.md) and [Hn unit](../group-cohomology-and-homology/lem-hn-unit.md) implies for $n >0$:

$$
H^n(S,\mathrm{coind}_1(G,M)) \cong
H^n(S,\mathrm{coind}_1(S,C \to M)) \cong
H^n(1,C \to M) \cong 0.
$$

## Lean

Formalized as [`Rep.trivialCohomology_coind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.trivialCohomology_coind₁).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 739](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L739)
