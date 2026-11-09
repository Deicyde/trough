---
declaration: theorem
origin: cited
lean: TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation
statement: formalized
proof: formalized
---

# The upper bound of Dedekind's different theorem

If the ramification index `e(L/K)` is
nonzero in `L`, the different exponent of `L/K` is at most `e(L/K) − 1 + v_L(e(L/K))`.

```lean
TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Algebra.IsSeparable K L]
  (he : ↑(TauCeti.ramificationIndex K L) ≠ 0) :
  TauCeti.differentExponent K L ≤
    TauCeti.ramificationIndex K L - 1 +
      TauCeti.natCastValuation L (TauCeti.ramificationIndex K L) he
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, the tame case](dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](the-first-half-of-dedekinds-different-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Wild.html#TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation).

## Sources

- [Tau Ceti documentation: `TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Wild.html#TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation)
- [Source of `TauCeti.differentExponent_le_ramificationIndex_sub_one_add_natCastValuation` in TauCeti/NumberTheory/LocalField/Different/Wild.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Different/Wild.lean#L59)
