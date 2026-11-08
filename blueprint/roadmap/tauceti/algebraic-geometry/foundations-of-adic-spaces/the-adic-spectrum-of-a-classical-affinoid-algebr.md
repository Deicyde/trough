---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra
statement: formalized
proof: formalized
---

# The adic spectrum of a classical affinoid algebra is an affinoid adic space

Let `K` be a
complete nonarchimedean field with a nontrivial absolute value and `B` a quotient of a Tate algebra
`K⟨X₁, …, Xₙ⟩`, carrying a complete ultrametric algebra norm, for instance the quotient Gauss norm.
Then for any pair of definition `P` of `B` and any plus ring `B⁺` of power-bounded elements
containing its ring of definition, such as `B°`, `Spa(B, B⁺)` is an affinoid adic space.

```lean
TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra.{u, u_1}
  {K : Type u_1} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {B : Type u}
  [NormedCommRing B] [NormedAlgebra K B] [IsUltrametricDist B] [CompleteSpace B]
  (P : TauCeti.Huber.PairOfDefinition B) {Bplus : Subring B} (hB : TauCeti.IsAffinoidAlgebra K B)
  (hP : P.ringOfDefinition ≤ Bplus)
  (hBplus : ∀ ⦃b : B⦄, b ∈ Bplus → TauCeti.Huber.IsPowerBounded b) :
  (TauCeti.ValuationSpectrum.presentationLimitPreAdicSpace P Bplus hBplus hP).isAdic
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](adic-spaces-wedhorn-definition-8-22.md)

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Henkel's open mapping theorem](../../topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Henkel's theorem in quotient form](../../topology/algebra/part-01/henkels-theorem-in-quotient-form.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../../ring-theory/part-01/mv-power-series/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](../../ring-theory/part-02/other-results/part-02/the-open-mapping-theorem-over-a-tate-ring.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](../../ring-theory/part-01/rigid-analytic-geometry/tauceti-isaffinoidalgebra-continuous-alghom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.html#TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.html#TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra)
- [Source of `TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.lean#L110)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
