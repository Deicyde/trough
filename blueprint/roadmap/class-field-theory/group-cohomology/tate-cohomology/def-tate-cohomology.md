---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: tateComplex, tateComplexFunctor, tateCohomology
---

# Tate cohomology

Recall that we have a cochain complex $C^n(G,M)$, indexed by $n \in {\mathbb N}$, whose zeroth term may be identified with $M$. We also have a chain complex $C_n(G,M)$ whose zeroth term may be identified with $M$. By [norm comp d](lem-norm-comp-d.md) and [d comp norm](lem-d-comp-norm.md), we may glue these together with the map $N_G : M \to M$ to obtain a cochain complex indexed by ${\mathbb Z}$:

$$
\cdots \to C_2(G,M) \to C_1(G,M) \stackrel{d_0}\to C_0(G,M)
\stackrel{N_G}\to C^0(G,M) \stackrel{d^0}\to C^1(G,M) \to C^2(G,M) \to \cdots
$$

We shall write $C^n_{\mathrm{Tate}}(G,M)$ for this cochain complex, and we normalize the indices so that for natural numbers $n$ we have $C^n_{\mathrm{Tate}}(G,M) = C^n(G,M)$. This implies $C^{-n-1}_{\mathrm{Tate}}(G,M) = C_n(G,M)$. It follows from [norm naturality](lem-norm-naturality.md) that $C^\bullet_{\mathrm{Tate}}(G,M)$ is functorial in $M$.

For an integer $n$, we shall write $H^n_{\mathrm{Tate}}(G,M)$ for the $n$-th cohomology of the complex $C^n_{\mathrm{Tate}}(G,M)$; this is called the $n$-th Tate cohomology of $M$, and is often written $\hat H^n(G,M)$ or (confusingly) just $H^n(G,M)$ in the literature. We stress that Tate cohomology exists only in the case that $G$ is a finite group.

## Depends on

- [norm comp d](lem-norm-comp-d.md)
- [d comp norm](lem-d-comp-norm.md)
- [norm naturality](lem-norm-naturality.md)

## Lean

Formalized as [`tateComplex`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/tateComplex), [`tateComplexFunctor`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/tateComplexFunctor), [`tateCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/tateCohomology).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 514](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L514)
