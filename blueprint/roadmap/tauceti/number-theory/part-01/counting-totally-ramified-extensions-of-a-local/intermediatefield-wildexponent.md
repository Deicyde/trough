---
declaration: def
origin: cited
lean: IntermediateField.wildExponent
statement: formalized
---

# IntermediateField.wildExponent

The wild exponent `c(L) = d(L) - [L : K] + 1` of a subextension `L` of `SeparableClosure K`,
written `d(L) + 1 - [L : K]` in truncated subtraction. For `L ∈ σ_K(n)` the truncation is
faithful by `IntermediateField.sub_one_le_discriminantExponent`, and `c(L)` is Serre's nonnegative
integer `d(L) - n + 1`.

```lean
IntermediateField.wildExponent.{u_1} {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] (L : IntermediateField K (SeparableClosure K)) : ℕ
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`IntermediateField.wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Basic.html#IntermediateField.wildExponent).

## Sources

- [Tau Ceti documentation: `IntermediateField.wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Basic.html#IntermediateField.wildExponent)
- [Source of `IntermediateField.wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Basic.lean#L198)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
