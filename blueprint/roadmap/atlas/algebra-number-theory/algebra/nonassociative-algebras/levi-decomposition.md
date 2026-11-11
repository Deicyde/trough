---
declaration: section
origin: cited
lean: LieModule.exists_isCompl_of_isSemisimple, MathlibExt.Algebra.Lie.LandmarkWanted.levi_decomposition
statement: formalized
proof: formalized
---

# Levi decomposition

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/levi-decomposition/index.html).

## Weyl's complete reducibility theorem

Let $L$ be a finite-dimensional semisimple Lie
algebra over a field $K$ of characteristic zero, and let $M$ be a finite-dimensional Lie module
over $L$ and $K$. Then every Lie submodule $W$ of $M$ has a complement: there is a Lie submodule
$U$ of $M$ with $W \cap U = 0$ and $W + U = M$.

Formalized by `LieModule.exists_isCompl_of_isSemisimple`, a theorem declared in [MathlibExt/Algebra/Lie/LeviDecomposition.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Lie/LeviDecomposition.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/levi-decomposition/index.html#exists-is-compl-of-is-semisimple).

## Levi decomposition

Let $L$ be a finite-dimensional Lie algebra over a field $K$ of
characteristic zero, and let $\operatorname{rad}(L)$ be its radical, the largest solvable ideal
of $L$. Then there is a semisimple Lie subalgebra $S$ of $L$ (a Levi factor) such that
$L = \operatorname{rad}(L) \oplus S$ as $K$-vector spaces, that is,
$\operatorname{rad}(L) + S = L$ and $\operatorname{rad}(L) \cap S = 0$.

Proof: Weyl's complete reducibility theorem is proved with the trace-form Casimir operator. The
Levi factor is then constructed for an abelian radical and the general case follows by induction
through the derived ideal of the radical.

## Sources

- E. E. Levi, Atti Accad. Sci. Torino 1905 and A. I. Malcev, Izv. Akad. Nauk SSSR 1945; Bourbaki, Lie I; Lean states K-module direct sum form over char-zero fields.

Formalized by `MathlibExt.Algebra.Lie.LandmarkWanted.levi_decomposition`, a theorem declared in [MathlibExt/Algebra/Lie/LeviDecomposition.lean, line 1713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Lie/LeviDecomposition.lean#L1713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/levi-decomposition/index.html#levi-decomposition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Levi decomposition](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/levi-decomposition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/nonassociative-algebras/levi-decomposition)
