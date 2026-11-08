---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum, TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum
statement: formalized
proof: formalized
---

# Serre's quotient formula for the lower index

For an intermediate field `L` of `M/K`
normal over `K` and `σ' : Gal(L/K)`, `e(M/L) · i_{L/K}(σ') = ∑_{σ|_L = σ'} i_{M/K}(σ)`, the sum
running over the automorphisms of `M/K` restricting to `σ'`.

```lean
TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum.{u_1, u_2, u_3}
  {K : Type u_1} {L : Type u_2} {M : Type u_3} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Normal K L] [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [Algebra K M]
  [ValuativeExtension K M] [Module.Finite K M] [IsGalois K M] [IsScalarTower K L M]
  (σ' : Gal(L/K)) :
  ↑(TauCeti.ramificationIndex L M) *
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation L).integer) σ' =
    ∑ σ with σ.restrictNormal L = σ',
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer) σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's criterion](../../../ring-theory/ideal/serres-criterion.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/LowerIndex.html#TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum).

## Other forms

**Serre's quotient formula for the lower index, over a coset.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/LowerIndex.html#TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum).

```lean
TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_restrictNormal_eq_sum.{u_1, u_2,
    u_3}
  {K : Type u_1} {L : Type u_2} {M : Type u_3} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Normal K L] [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [Algebra K M]
  [ValuativeExtension K M] [Module.Finite K M] [IsScalarTower K L M] [IsGalois L M] (σ : Gal(M/K)) :
  ↑(TauCeti.ramificationIndex L M) *
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation L).integer) (σ.restrictNormal L) =
    ∑ τ,
      TauCeti.IsLocalRing.lowerIndex (↥(ValuativeRel.valuation M).integer)
        (σ * AlgEquiv.restrictScalars K τ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/LowerIndex.html#TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum)
- [Source of `TauCeti.LocalFieldsRamification.ramificationIndex_mul_lowerIndex_eq_sum` in TauCeti/NumberTheory/LocalField/LowerIndex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/LowerIndex.lean#L137)
