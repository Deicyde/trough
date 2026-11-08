---
declaration: theorem
origin: cited
lean: TauCeti.ramificationIndex_sub_one_le_differentExponent, TauCeti.inertiaDegree_mul_ramificationIndex_sub_one_le_discriminantExponent
statement: formalized
proof: formalized
---

# The first half of Dedekind's different theorem

`e(L/K) - 1 ≤ d(L/K)`.

```lean
TauCeti.ramificationIndex_sub_one_le_differentExponent.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L]
  [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Algebra.IsSeparable K L] :
  TauCeti.ramificationIndex K L - 1 ≤ TauCeti.differentExponent K L
```

## Depends on

- [TauCeti.relDiscr](../../part-01/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Dedekind's different theorem, the tame case, as an exponent](../../../ring-theory/part-02/other-results/part-01/dedekinds-different-theorem-the-tame-case-as-an.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ramificationIndex_sub_one_le_differentExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Basic.html#TauCeti.ramificationIndex_sub_one_le_differentExponent).

## Other forms

**The first half of Dedekind's different theorem, for the discriminant.** Formalized in Tau Ceti as [`TauCeti.inertiaDegree_mul_ramificationIndex_sub_one_le_discriminantExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Discriminant/Basic.html#TauCeti.inertiaDegree_mul_ramificationIndex_sub_one_le_discriminantExponent).

```lean
TauCeti.inertiaDegree_mul_ramificationIndex_sub_one_le_discriminantExponent.{u_1, u_2}
  (K : Type u_1) (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Algebra.IsSeparable K L] :
  TauCeti.inertiaDegree K L * (TauCeti.ramificationIndex K L - 1) ≤ TauCeti.discriminantExponent K L
```

## Sources

- [Tau Ceti documentation: `TauCeti.ramificationIndex_sub_one_le_differentExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Basic.html#TauCeti.ramificationIndex_sub_one_le_differentExponent)
- [Source of `TauCeti.ramificationIndex_sub_one_le_differentExponent` in TauCeti/NumberTheory/LocalField/Different/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Different/Basic.lean#L120)
