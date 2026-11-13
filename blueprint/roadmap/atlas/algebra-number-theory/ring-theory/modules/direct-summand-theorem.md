---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.singleFunctorPlusIsoCompQh, MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.derived_direct_summand, MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.direct_summand
statement: formalized
---

# Direct summand theorem

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/direct-summand-theorem/index.html).

## Single complexes in the bounded-below derived category

For an abelian category $C$ with
a derived category and an integer $n$, the functor sending an object of $C$ to the complex
concentrated in degree $n$, viewed in the bounded-below derived category $D^+(C)$, is naturally
isomorphic to the corresponding single-complex functor into the bounded-below homotopy category
$K^+(C)$ followed by the localization functor $K^+(C) \to D^+(C)$.

Formalized by `MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.singleFunctorPlusIsoCompQh`, a definition declared in [WantedExt/AlgebraicGeometry/DirectSummandWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/DirectSummandWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/direct-summand-theorem/index.html#single-functor-plus-iso-comp-qh).

## Derived direct summand theorem

Let $A$ be a regular commutative ring, let $X$ be a
scheme and let $f \colon X \to \operatorname{Spec} A$ be a proper morphism that is surjective on
underlying points. Let $\varphi \colon A \to \Gamma(X, \mathcal{O}_X)$ be the ring map
corresponding to $f$, and let $R\Gamma$ be the right derived functor, between bounded-below
derived categories, of global sections of sheaves of $\mathcal{O}_X$-modules followed by
restriction of scalars along $\varphi$. If the category of sheaves of $\mathcal{O}_X$-modules
has enough injectives, then the composite of $\varphi$, placed in degree $0$, with the canonical
map from $\Gamma(X, \mathcal{O}_X)$ in degree $0$ to $R\Gamma(\mathcal{O}_X)$ is a split
monomorphism $A \to R\Gamma(\mathcal{O}_X)$ in the bounded-below derived category of
$A$-modules.

## Sources

-. Problem `direct_summand` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.derived_direct_summand` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/DirectSummandWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/DirectSummandWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/direct-summand-theorem/index.html#derived-direct-summand).

## Direct summand theorem

Let $A$ be a regular commutative ring and let $B$ be a commutative
$A$-algebra that is finitely generated as an $A$-module and on which $A$ acts faithfully
(equivalently, the structure map $A \to B$ is injective). Then there is an $A$-linear map
$\pi \colon B \to A$ with $\pi(a \cdot 1) = a$ for every $a \in A$; that is, $A$ is a direct
summand of $B$ as an $A$-module.

## Sources

-. Problem `direct_summand` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.DirectSummandWanted.AlgebraicGeometry.DirectSummand.direct_summand` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/DirectSummandWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/DirectSummandWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/direct-summand-theorem/index.html#direct-summand).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Direct summand theorem](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/direct-summand-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/modules/direct-summand-theorem)
