---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm, TauCeti.ClassFieldTheory.natCard_H1_eq_mul, TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_index_coprime
statement: formalized
proof: formalized
---

# Tate's local Euler characteristic formula

The Euler characteristic of a finite smooth
discrete Galois module equals the normalized absolute value of its order.

```lean
TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm (p : ℕ) [Fact (Nat.Prime p)]
  (F : Type) [Field F] [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F]
  [TauCeti.FinitePadicExtension F p] (n : ℕ) [NeZero n] (A : TauCeti.ClassFieldTheory.GalRep n F)
  [Finite ↑A] [Fact (TauCeti.IsSmoothDiscrete (ZMod n) A)] :
  TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯ A = TauCeti.ClassFieldTheory.localCardNorm p A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Local Tate duality in degree one](local-tate-duality-in-degree-one.md)
- [The logarithm is Galois-equivariant](../../part-01/local-fields-and-ramification/the-logarithm-is-galois-equivariant.md)
- [Modular-Artin reduction of the local Euler characteristic formula](modular-artin-reduction-of-the-local-euler-chara.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Perfect local Tate duality in mixed characteristic](perfect-local-tate-duality-in-mixed-characterist.md)
- [Shapiro's lemma for the normalized order](shapiros-lemma-for-the-normalized-order.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Theorem.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm).

## Other forms

**Tate's local Euler characteristic formula for explicit cohomology.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.natCard_H1_eq_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Theorem.html#TauCeti.ClassFieldTheory.natCard_H1_eq_mul).

```lean
TauCeti.ClassFieldTheory.natCard_H1_eq_mul (p : ℕ) [Fact (Nat.Prime p)] (F : Type) [Field F]
  [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F]
  [TauCeti.FinitePadicExtension F p] (M : Type) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction (TauCeti.AbsoluteGaloisGroup F) M]
  [ContinuousSMul (TauCeti.AbsoluteGaloisGroup F) M] [Finite M] :
  Nat.card (TauCeti.ContCohomology.H1 (TauCeti.AbsoluteGaloisGroup F) M) =
    Nat.card ↥(TauCeti.ContCohomology.H0 (TauCeti.AbsoluteGaloisGroup F) M) *
        Nat.card (TauCeti.ContCohomology.H2 (TauCeti.AbsoluteGaloisGroup F) M) *
      p ^ (Module.finrank ℚ_[p] F * padicValNat p (Nat.card M))
```

**Tate's local Euler characteristic formula, prime-to-`ℓ` case.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_index_coprime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Coprime.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_index_coprime).

```lean
TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_index_coprime (p : ℕ)
  [Fact (Nat.Prime p)] {F : Type} [Field F] [CharZero F] [ValuativeRel F] [TopologicalSpace F]
  [IsNonarchimedeanLocalField F] [TauCeti.FinitePadicExtension F p] {ℓ : ℕ} [Fact (Nat.Prime ℓ)]
  (A : TauCeti.ClassFieldTheory.GalRep ℓ F) [Finite ↑A] [Fact (TauCeti.IsSmoothDiscrete (ZMod ℓ) A)]
  (N : OpenNormalSubgroup (Field.absoluteGaloisGroup F)) (hN : (↑N.toOpenSubgroup).index.Coprime ℓ)
  (hA : ∀ g ∈ N, ∀ (x : ↑A), (A.ρ g) x = x) :
  TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯ A = TauCeti.ClassFieldTheory.localCardNorm p A
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Theorem.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm)
- [Source of `TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm` in TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Theorem.lean#L44)
