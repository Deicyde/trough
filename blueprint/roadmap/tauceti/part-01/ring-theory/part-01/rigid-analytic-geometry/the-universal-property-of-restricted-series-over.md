---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring
statement: formalized
proof: formalized
---

# The universal property of restricted series over an affinoid algebra

Let `A` and `B` be
affinoid algebras with complete ultrametric algebra norms. A `K`-algebra map `φ : A → B` and
power-bounded `b₁, …, bₖ ∈ B` extend to exactly one `K`-algebra map `A⟨X₁, …, Xₖ⟩ → B` sending
each `Xᵢ` to `bᵢ`, namely `TauCeti.IsAffinoidAlgebra.restrictedLift`. It is continuous, as is every
algebra map between such algebras (`TauCeti.IsAffinoidAlgebra.continuous_algHom`).

```lean
TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A] {k : ℕ}
  (hA : TauCeti.IsAffinoidAlgebra K A) {B : Type u_3} [NormedCommRing B] [NormedAlgebra K B]
  [IsUltrametricDist B] [CompleteSpace B] (hB : TauCeti.IsAffinoidAlgebra K B) (φ : A →ₐ[K] B)
  {b : Fin k → B} (hb : ∀ (i : Fin k), TauCeti.Huber.IsPowerBounded (b i)) :
  ∃! ψ,
    (∀ (a : A), ψ ((algebraMap A ↥(MvPowerSeries.IsRestricted.subring fun x => 1)) a) = φ a) ∧
      ∀ (i : Fin k), ψ ⟨MvPowerSeries.X i, ⋯⟩ = b i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Restricted series over an affinoid algebra form an affinoid algebra](restricted-series-over-an-affinoid-algebra-form.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring)
- [Source of `TauCeti.IsAffinoidAlgebra.existsUnique_algHom_isRestricted_subring` in TauCeti/RingTheory/Affinoid/Restricted.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/Restricted.lean#L166)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
