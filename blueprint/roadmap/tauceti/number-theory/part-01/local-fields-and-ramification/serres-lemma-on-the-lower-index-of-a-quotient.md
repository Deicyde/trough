---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one, TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum_card
statement: formalized
proof: formalized
---

# Serre's lemma on the lower index of a quotient

If `σ` has the largest lower index in its
coset `σ H`, and `i_G(σ) = j` is finite, then `φ_{M/L}(j - 1) = i_{G/H}(σ|_L) - 1`.

```lean
TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one.{u_1, u_2, u_3} {K : Type u_1}
  {L : Type u_2} {M : Type u_3} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Normal K L] [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [IsGalois L M]
  [Algebra K M] [ValuativeExtension K M] [Module.Finite K M] [IsScalarTower K L M] (σ : Gal(M/K))
  {j : ℕ} (hj : TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer) σ = ↑j)
  (hσ :
    ∀ (τ : Gal(M/L)),
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer)
          (σ * AlgEquiv.restrictScalars K τ) ≤
        TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer) σ) :
  ↑(TauCeti.LocalFieldsRamification.herbrand L M ⟨↑j - 1, ⋯⟩) =
    ↑(TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation L).integer)
            (σ.restrictNormal L)).toNat -
      1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's quotient formula for the lower index](serres-quotient-formula-for-the-lower-index.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/Quotient.html#TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one).

## Other forms

**Serre's lemma on the lower index of a quotient, in counting form.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/Quotient.html#TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum_card).

```lean
TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum_card.{u_1,
    u_2, u_3}
  {K : Type u_1} {L : Type u_2} {M : Type u_3} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Normal K L] [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [IsGalois L M]
  [Algebra K M] [ValuativeExtension K M] [Module.Finite K M] [IsScalarTower K L M] (σ : Gal(M/K))
  {j : ℕ} (hj : TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer) σ = ↑j)
  (hσ :
    ∀ (τ : Gal(M/L)),
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer)
          (σ * AlgEquiv.restrictScalars K τ) ≤
        TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer) σ) :
  ↑(TauCeti.ramificationIndex L M) *
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation L).integer) (σ.restrictNormal L) =
    ∑ k ∈ Finset.range j,
      ↑(Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup L M ↑k))
```

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/Quotient.html#TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one)
- [Source of `TauCeti.LocalFieldsRamification.coe_herbrand_lowerIndex_sub_one` in TauCeti/NumberTheory/LocalField/Herbrand/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Herbrand/Quotient.lean#L120)
