---
declaration: theorem
origin: cited
lean: TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff, TauCeti.discriminantExponent_eq_inertiaDegree_mul_ramificationIndex_sub_one_iff
statement: formalized
proof: formalized
---

# Dedekind's different theorem, the tame case

`d(L/K) = e(L/K) - 1` exactly when `L/K` is
tamely ramified.

```lean
TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L]
  [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Algebra.IsSeparable K L] :
  TauCeti.differentExponent K L = TauCeti.ramificationIndex K L - 1 ↔ TauCeti.IsTamelyRamified K L
```

## Depends on

- [TauCeti.relDiscr](../../part-01/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Dedekind's different theorem, the tame case, as an exponent](../../../ring-theory/part-02/other-results/part-01/dedekinds-different-theorem-the-tame-case-as-an.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Basic.html#TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff).

## Other forms

**Dedekind's different theorem for the discriminant in the tame case.** Formalized in Tau Ceti as [`TauCeti.discriminantExponent_eq_inertiaDegree_mul_ramificationIndex_sub_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Discriminant/Basic.html#TauCeti.discriminantExponent_eq_inertiaDegree_mul_ramificationIndex_sub_one_iff).

```lean
TauCeti.discriminantExponent_eq_inertiaDegree_mul_ramificationIndex_sub_one_iff.{u_1, u_2}
  (K : Type u_1) (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Algebra.IsSeparable K L] :
  TauCeti.discriminantExponent K L =
      TauCeti.inertiaDegree K L * (TauCeti.ramificationIndex K L - 1) ↔
    TauCeti.IsTamelyRamified K L
```

## Sources

- [Tau Ceti documentation: `TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Basic.html#TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff)
- [Source of `TauCeti.differentExponent_eq_ramificationIndex_sub_one_iff` in TauCeti/NumberTheory/LocalField/Different/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Different/Basic.lean#L145)
