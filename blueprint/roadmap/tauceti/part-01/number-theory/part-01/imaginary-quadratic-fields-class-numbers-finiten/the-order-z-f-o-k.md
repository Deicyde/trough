---
declaration: def
origin: cited
lean: TauCeti.GlobalNumberFields.intAddMulOrder
statement: formalized
---

# The order `ℤ + f 𝓞 K`

the algebraic integers congruent to a rational integer modulo `f`.

```lean
TauCeti.GlobalNumberFields.intAddMulOrder.{u_1} (K : Type u_1) [Field K] [NumberField K] (f : ℕ)
  [NeZero f] : TauCeti.GlobalNumberFields.NumberFieldOrder K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.intAddMulOrder`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.html#TauCeti.GlobalNumberFields.intAddMulOrder).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.intAddMulOrder`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.html#TauCeti.GlobalNumberFields.intAddMulOrder)
- [Source of `TauCeti.GlobalNumberFields.intAddMulOrder` in TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.lean#L84)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
