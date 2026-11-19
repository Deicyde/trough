---
declaration: theorem
origin: cited
lean: TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff
statement: formalized
proof: formalized
---

# Surjectivity criterion for finite étale morphisms of Huber pairs

A finite étale morphism
`φ : (A, A⁺) → (B, B⁺)` over a complete Hausdorff Tate ring `A` is surjective on adic spectra
exactly when `B` is faithfully flat over `A`.

```lean
TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff.{u_3, u_4} {A : Type u_3}
  {B : Type u_4} [CommRing A] [UniformSpace A] [T2Space A] [CompleteSpace A] [IsTopologicalRing A]
  [IsUniformAddGroup A] [TauCeti.Huber.IsTateRing A] [CommRing B] [TopologicalSpace B]
  [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B] {S : TauCeti.Huber.Pair A}
  {T : TauCeti.Huber.Pair B} {φ : S.Hom T} (hφ : φ.IsFiniteEtale) :
  Function.Surjective φ.spaComap ↔ φ.toRingHom.FaithfullyFlat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.html#TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.html#TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff)
- [Source of `TauCeti.Huber.Pair.Hom.IsFiniteEtale.surjective_spaComap_iff` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Spa/FiniteAlgebra.lean#L198)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
