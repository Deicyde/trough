---
declaration: theorem
origin: cited
lean: TauCeti.numberField_CoefficientField
statement: formalized
proof: formalized
---

# The coefficient field of a newform of weight at least two is a number field

```lean
TauCeti.numberField_CoefficientField {N : ℕ} [NeZero N] {k : ℤ} (f : HeckeRing.GL2.Newform N k)
  (hk : 2 ≤ k) : NumberField ↥(TauCeti.CoefficientField f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [HeckeRing.GL2.Newform.heckeUCuspNat\_eq\_qExpansion\_coeff\_smul](heckering-gl2-newform-heckeucuspnat-eq-qexpansio.md)
- [Periods determine a cusp form](periods-determine-a-cusp-form.md)
- [TauCeti.ModularSymbols](tauceti-modularsymbols.md)
- [TauCeti.ModularSymbols.periodMap](tauceti-modularsymbols-periodmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.numberField_CoefficientField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.html#TauCeti.numberField_CoefficientField).

## Sources

- [Tau Ceti documentation: `TauCeti.numberField_CoefficientField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.html#TauCeti.numberField_CoefficientField)
- [Source of `TauCeti.numberField_CoefficientField` in TauCeti/NumberTheory/ModularForms/Newforms/NumberField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.lean#L156)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
