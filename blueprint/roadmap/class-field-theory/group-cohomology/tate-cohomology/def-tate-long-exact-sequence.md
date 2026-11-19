---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: TateCohomology.preservesFiniteLimits_tateComplexFunctor, TateCohomology.preservesFiniteColimits_tateComplexFunctor, TateCohomology.δ
---

# Tate long exact sequence

Since the functors $C^\bullet(G,-)$ and $C_\bullet(G,-)$ are both exact, it follows that $C^\bullet_{\mathrm{Tate}}(G,-)$ is an exact functor. Hence, given any short exact sequence in $\mathbf{Rep}(R,G)$:

$$
0 \to A \to B \to C \to 0,
$$

we obtain a short exact sequence of Tate complexes and therefore connecting homomorphisms $\delta : H^n_{\mathrm{Tate}}(G,C) \to H^{n+1}_{\mathrm{Tate}}(G,A)$ such that the following is a long exact sequence (for $n \in {\mathbb Z}$):

$$
\cdots \to H^n_{\mathrm{Tate}}(G,A) \to H^n_{\mathrm{Tate}}(G,B) \to H^n_{\mathrm{Tate}}(G,C)
\to H^{n+1}_{\mathrm{Tate}}(G,A) \to H^{n+1}_{\mathrm{Tate}}(G,B) \to \cdots
$$

The exactness statements are in Mathlib in the namespace `HomologicalComplex.HomologySequence`. The connecting maps $\delta : H^n_{\mathrm{Tate}}(G,C) \to H^{n+1}_{\mathrm{Tate}}(G,A)$ coincide with those for cohomology for $n \ge 1$ and with those for homology for $n \le -3$.

## Depends on

- [Tate cohomology](def-tate-cohomology.md)
- [cochainsFunctor exact](../group-cohomology-and-homology/lem-cochainsfunctor-exact.md)

## Lean

Formalized as [`TateCohomology.preservesFiniteLimits_tateComplexFunctor`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/TateCohomology.preservesFiniteLimits_tateComplexFunctor), [`TateCohomology.preservesFiniteColimits_tateComplexFunctor`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/TateCohomology.preservesFiniteColimits_tateComplexFunctor), [`TateCohomology.δ`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/TateCohomology.δ).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 596](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L596)
