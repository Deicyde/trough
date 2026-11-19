---
declaration: theorem
origin: cited
lean: TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre
statement: formalized
proof: formalized
---

# The fibres of a finite étale morphism of Huber pairs

If `φ : (A, A⁺) → (B, B⁺)` is finite
étale, the points of `Spa(B, B⁺)` over a point `x` of `Spa(A, A⁺)` form a finite set with at most
`rank_x B` elements, the rank of the finite projective `A`-module `B` at the support of `x`.

```lean
TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] [CommRing B]
  [TopologicalSpace B] [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B]
  {S : TauCeti.Huber.Pair A} {T : TauCeti.Huber.Pair B} {φ : S.Hom T} (hφ : φ.IsFiniteEtale)
  (x : ↑(TauCeti.ValuationSpectrum.spa S.plus)) :
  (φ.spaComap ⁻¹' {x}).Finite ∧ Nat.card ↑(φ.spaComap ⁻¹' {x}) ≤ Module.rankAtStalk B (↑x).suppFun
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.html#TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.html#TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre)
- [Source of `TauCeti.Huber.Pair.Hom.IsFiniteEtale.finite_fibre` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.lean#L218)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
