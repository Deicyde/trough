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
- [Source of `TauCeti.GlobalNumberFields.intAddMulOrder` in TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Global/Orders/IntAddMulOrder.lean#L84)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
