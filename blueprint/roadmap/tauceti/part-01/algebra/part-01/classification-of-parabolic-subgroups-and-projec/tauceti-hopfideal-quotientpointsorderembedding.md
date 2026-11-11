---
declaration: def
origin: cited
lean: TauCeti.HopfIdeal.quotientPointsOrderEmbedding
statement: formalized
---

# TauCeti.HopfIdeal.quotientPointsOrderEmbedding

Reduced finite-type closed subgroups embed, with their geometric inclusion order,
into the subgroups of geometric points. The order dual reverses the order on defining
Hopf ideals. The algebraically closed extension need not be algebraic over the base field.

```lean
TauCeti.HopfIdeal.quotientPointsOrderEmbedding.{u, v, w} {k : Type u} [Field k] (K : Type w)
  [Field K] [Algebra k K] [IsAlgClosed K] (H : CommHopfAlgCat k) :
  { I // Algebra.FiniteType k ↑(H.quotient I) ∧ IsReduced ↑(H.quotient I) }ᵒᵈ ↪o
    Subgroup ↑(TauCeti.HopfAlgebra.points ↧K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.quotientPointsOrderEmbedding`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Points/Embedding.html#TauCeti.HopfIdeal.quotientPointsOrderEmbedding).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.quotientPointsOrderEmbedding`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Points/Embedding.html#TauCeti.HopfIdeal.quotientPointsOrderEmbedding)
- [Source of `TauCeti.HopfIdeal.quotientPointsOrderEmbedding` in TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Points/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Points/Embedding.lean#L50)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
