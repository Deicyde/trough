---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff, TauCeti.ClassFieldTheory.localEulerCharacteristicK0_eq_localCardNormK0_iff
statement: formalized
proof: formalized
---

# The Euler characteristic formula and `G₀`

Tate's local Euler characteristic formula
`χ_F(X) = φ_F(X)` holds for every finite smooth discrete Galois representation `X` exactly when, for
every open normal subgroup `V` of `G_F`, the descended Euler characteristic and the descended
normalized absolute value of the order agree on the Grothendieck group of `(ZMod n)[G_F ⧸ V]`.

```lean
TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff {n : ℕ} {F : Type}
  [Field F] [NeZero n] [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F] (p : ℕ)
  [Fact (Nat.Prime p)] [TauCeti.FinitePadicExtension F p] (hn : IsUnit ↑n) :
  (∀ (X : TauCeti.ClassFieldTheory.GalRep n F) [inst : Finite ↑X] [DiscreteTopology ↑X]
      [inst_2 : Fact (TauCeti.IsSmoothDiscrete (ZMod n) X)],
      TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯ X =
        TauCeti.ClassFieldTheory.localCardNorm p X) ↔
    ∀ (V : OpenNormalSubgroup (Field.absoluteGaloisGroup F)),
      TauCeti.ClassFieldTheory.localEulerCharacteristicK0 V hn =
        TauCeti.ClassFieldTheory.localCardNormK0 n V p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../../part-01/class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Local Tate duality in degree one](local-tate-duality-in-degree-one.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/GrothendieckGroup.html#TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff).

## Other forms

**The Euler characteristic formula for `V` on `G₀`.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localEulerCharacteristicK0_eq_localCardNormK0_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/GrothendieckGroup.html#TauCeti.ClassFieldTheory.localEulerCharacteristicK0_eq_localCardNormK0_iff).

```lean
TauCeti.ClassFieldTheory.localEulerCharacteristicK0_eq_localCardNormK0_iff {n : ℕ} {F : Type}
  [Field F] (V : OpenNormalSubgroup (Field.absoluteGaloisGroup F)) [NeZero n] [ValuativeRel F]
  [TopologicalSpace F] [IsNonarchimedeanLocalField F] (p : ℕ) [Fact (Nat.Prime p)]
  [TauCeti.FinitePadicExtension F p] (hn : IsUnit ↑n) :
  TauCeti.ClassFieldTheory.localEulerCharacteristicK0 V hn =
      TauCeti.ClassFieldTheory.localCardNormK0 n V p ↔
    ∀ (X : TauCeti.ClassFieldTheory.GalRep n F) [inst : Finite ↑X] [DiscreteTopology ↑X]
      [inst_2 : Fact (TauCeti.IsSmoothDiscrete (ZMod n) X)],
      (∀ g ∈ V, ∀ (x : ↑X), (X.ρ g) x = x) →
        TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯ X =
          TauCeti.ClassFieldTheory.localCardNorm p X
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/GrothendieckGroup.html#TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff)
- [Source of `TauCeti.ClassFieldTheory.forall_localEulerCharacteristic_eq_localCardNorm_iff` in TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/GrothendieckGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/GrothendieckGroup.lean#L195)
