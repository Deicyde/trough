---
declaration: def
origin: cited
lean: TauCeti.principalUnitsEquiv
statement: formalized
---

# The principal units are a copy of `ℤ_p`

For `f ≥ 1`, with `f ≥ 2` when `p = 2`, and a
unit `w` of exact level `f`, the `p`-adic power map `l ↦ w ^ l` is a topological group
isomorphism from the additive group of `ℤ_[p]` onto `U^(f) = 1 + p ^ f ℤ_p`. It is onto because
`w` topologically generates `U^(f)`, and injective because `w` has infinite order.

```lean
TauCeti.principalUnitsEquiv {p : ℕ} [Fact (Nat.Prime p)] {f : ℕ} (hf : 0 < f) (hf₂ : p = 2 → 2 ≤ f)
  {w : ℤ_[p]ˣ} (hw : w ∈ TauCeti.unitsPrincipal p f) (hw' : w ∉ TauCeti.unitsPrincipal p (f + 1)) :
  Multiplicative ℤ_[p] ≃ₜ* ↥(TauCeti.unitsPrincipal p f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.principalUnitsEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/PadicUnits.html#TauCeti.principalUnitsEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.principalUnitsEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/PadicUnits.html#TauCeti.principalUnitsEquiv)
- [Source of `TauCeti.principalUnitsEquiv` in TauCeti/Topology/Algebra/Group/Profinite/ProP/PadicUnits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/PadicUnits.lean#L224)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
