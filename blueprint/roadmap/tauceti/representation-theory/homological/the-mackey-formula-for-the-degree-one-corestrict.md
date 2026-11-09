---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.cochainsCor1_mackeyTransversal, TauCeti.ContCohomology.explicitMap2_explicitCor2_eq_sum, TauCeti.ContCohomology.cochainsCor2_mackeyTransversal
statement: formalized
proof: formalized
---

# The Mackey formula for the degree-one corestriction cochain

At the adapted transversal
`Subgroup.mackeyTransversal`, the restriction to `V` of the corestriction of a `1`-cochain `f` on
`U` is, on the nose, the sum over the double cosets `V \ G / U` of the corestrictions, from the
Mackey subgroups to `V` at the canonical transversal, of the conjugates
`y ↦ s • f (s⁻¹ y s)` of `f`.

```lean
TauCeti.ContCohomology.cochainsCor1_mackeyTransversal.{u, v} (G : Type u) [Group G] (M : Type v)
  [AddCommGroup M] [DistribMulAction G M] (U V : Subgroup G) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D) (f : ↥U → M) (k : ↥V) :
  (TauCeti.ContCohomology.cochainsCor1 G M U (U.mackeyTransversal V r hr) ⋯) f ↑k =
    ∑ D,
      (TauCeti.ContCohomology.cochainsCor1 (↥V) M ((TauCeti.mackeySubgroup (r D) U V).subgroupOf V)
          Quotient.out ⋯)
        ((TauCeti.ContCohomology.cochainsMap1 (TauCeti.mackeyToH (r D) U V)
            (DistribSMul.toAddMonoidHom M (r D)))
          f)
        k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mackey double-coset formula in degree one (NSW (1.5.6))](the-mackey-double-coset-formula-in-degree-one-ns.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.cochainsCor1_mackeyTransversal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.cochainsCor1_mackeyTransversal).

## Other forms

**The Mackey formula along a continuous homomorphism (NSW (1.5.6)).** Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitMap2_explicitCor2_eq_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Pullback.html#TauCeti.ContCohomology.explicitMap2_explicitCor2_eq_sum).

```lean
TauCeti.ContCohomology.explicitMap2_explicitCor2_eq_sum.{u, v, w, z} {G : Type u} {H : Type v}
  [Group G] [Group H] [TopologicalSpace G] [TopologicalSpace H] {M : Type w} {N : Type z}
  [AddCommGroup M] [AddCommGroup N] [DistribMulAction G M] [DistribMulAction H N] (φ : H →ₜ* G)
  (f : M →+ N) (hequiv : ∀ (h : H) (m : M), f (φ h • m) = h • f m) (U : Subgroup G)
  [TopologicalSpace M] [IsTopologicalAddGroup M] [ContinuousSMul G M] [TopologicalSpace N]
  [IsTopologicalAddGroup N] [ContinuousSMul H N] [IsTopologicalGroup G] [ContinuousMul H]
  (hf : Continuous ⇑f) [U.FiniteIndex] (hU : IsOpen ↑U)
  (r : DoubleCoset.Quotient ↑(↑φ).range ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑(↑φ).range ↑U), DoubleCoset.mk (↑φ).range U (r D) = D)
  (ψ : DoubleCoset.Quotient ↑(↑φ).range ↑U → H →ₜ* G)
  (hψ : ∀ (D : DoubleCoset.Quotient ↑(↑φ).range ↑U) (h : H), (ψ D) h = (r D)⁻¹ * φ h * r D)
  (x : TauCeti.ContCohomology.H2 (↥U) M) :
  (TauCeti.ContCohomology.explicitMap2 G M H N φ f hf hequiv)
      ((TauCeti.ContCohomology.explicitCor2 G M U hU) x) =
    ∑ D,
      (TauCeti.ContCohomology.explicitCor2 H N (Subgroup.comap (↑(ψ D)) U) ⋯)
        ((TauCeti.ContCohomology.explicitMap2 (↥U) M (↥(Subgroup.comap (↑(ψ D)) U)) N
            ((ψ D).subgroupComap U) (f.comp (DistribSMul.toAddMonoidHom M (r D))) ⋯ ⋯)
          x)
```

**The Mackey formula for the degree-two corestriction cochain.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.cochainsCor2_mackeyTransversal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.cochainsCor2_mackeyTransversal).

```lean
TauCeti.ContCohomology.cochainsCor2_mackeyTransversal.{u, v} (G : Type u) [Group G] (M : Type v)
  [AddCommGroup M] [DistribMulAction G M] (U V : Subgroup G) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D) (f : ↥U × ↥U → M)
  (k l : ↥V) :
  (TauCeti.ContCohomology.cochainsCor2 G M U (U.mackeyTransversal V r hr) ⋯) f (↑k, ↑l) =
    ∑ D,
      (TauCeti.ContCohomology.cochainsCor2 (↥V) M ((TauCeti.mackeySubgroup (r D) U V).subgroupOf V)
          Quotient.out ⋯)
        ((TauCeti.ContCohomology.cochainsMap2 (TauCeti.mackeyToH (r D) U V)
            (DistribSMul.toAddMonoidHom M (r D)))
          f)
        (k, l)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.cochainsCor1_mackeyTransversal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.cochainsCor1_mackeyTransversal)
- [Source of `TauCeti.ContCohomology.cochainsCor1_mackeyTransversal` in TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.lean#L267)
