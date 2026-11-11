---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed, TauCeti.ClassFieldTheory.tateDualityPairing_perfect
statement: formalized
proof: formalized
---

# Perfect local Tate duality in mixed characteristic

For a characteristic-zero
nonarchimedean local field `F`, every finite smooth discrete `ZMod n`-representation has a perfect
local Tate-duality pairing in complementary degrees.

```lean
TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed (F : Type) [Field F] [CharZero F]
  [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F] (n : ℕ) (hn : n ≠ 0)
  (A : TauCeti.ClassFieldTheory.GalRep n F)
  (tr : ↑(continuousCohomology 2 (TauCeti.ClassFieldTheory.muNRep n F)).toModuleCat ≃+ ZMod n)
  (hA : Finite ↑A) [DiscreteTopology ↑A] [Fact (TauCeti.IsSmoothDiscrete (ZMod n) A)] (i j : ℕ)
  (hij : i + j = 2) :
  (∀ (x : ↑(continuousCohomology i (TauCeti.ClassFieldTheory.tateDual A)).toModuleCat),
      (∀ (y : ↑(continuousCohomology j A).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = 0) →
        x = 0) ∧
    ∀ (φ : ↑(continuousCohomology j A).toModuleCat →+ ZMod n),
      ∃ x,
        ∀ (y : ↑(continuousCohomology j A).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = φ y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Local Tate duality in degree one](local-tate-duality-in-degree-one.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.html#TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed).

## Other forms

**Perfect local Tate duality for the named evaluation pairing.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.tateDualityPairing_perfect`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.html#TauCeti.ClassFieldTheory.tateDualityPairing_perfect).

```lean
TauCeti.ClassFieldTheory.tateDualityPairing_perfect {n : ℕ} {F : Type} [Field F] [ValuativeRel F]
  [TopologicalSpace F] [IsNonarchimedeanLocalField F] (hn : IsUnit ↑n)
  (A : TauCeti.ClassFieldTheory.GalRep n F) [DiscreteTopology ↑A] [Finite ↑A]
  [Fact (TauCeti.IsSmoothDiscrete (ZMod n) A)]
  (tr : ↑(continuousCohomology 2 (TauCeti.ClassFieldTheory.muNRep n F)).toModuleCat ≃+ ZMod n)
  (i j : ℕ) (hij : i + j = 2) :
  (∀ (x : ↑(continuousCohomology i (TauCeti.ClassFieldTheory.tateDual A)).toModuleCat),
      (∀ (y : ↑(continuousCohomology j A).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = 0) →
        x = 0) ∧
    ∀ (φ : ↑(continuousCohomology j A).toModuleCat →+ ZMod n),
      ∃ x,
        ∀ (y : ↑(continuousCohomology j A).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = φ y
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.html#TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed)
- [Source of `TauCeti.ClassFieldTheory.tateDualityPairing_perfect_mixed` in TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.lean#L277)
