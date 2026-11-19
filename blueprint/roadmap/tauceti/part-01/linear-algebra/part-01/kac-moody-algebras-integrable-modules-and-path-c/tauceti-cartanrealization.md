---
declaration: structure
origin: cited
lean: TauCeti.CartanRealization
statement: formalized
---

# TauCeti.CartanRealization

A realization of a matrix, with independent roots and coroots in the full ambient space.
For an integral Cartan matrix over a characteristic-zero field, use its entrywise cast.
Neither family is required to span the ambient space, and its dimension is unconstrained.
This generalizes Kac's notion: in his setting, his realizations are exactly the minimal ones,
attaining `CartanRealization.two_mul_card_le_rank_add_finrank` with equality.

```lean
TauCeti.CartanRealization.{u_1, u_2, u_3} {I : Type u_1} {K : Type u_2} [Field K] (A : Matrix I I K)
  (H : Type u_3) [AddCommGroup H] [_root_.Module K H] : Type (max (max u_1 u_2) u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CartanRealization`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization).

## Sources

- [Tau Ceti documentation: `TauCeti.CartanRealization`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization)
- [Source of `TauCeti.CartanRealization` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L39)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KacMoody/STATUS.md)
