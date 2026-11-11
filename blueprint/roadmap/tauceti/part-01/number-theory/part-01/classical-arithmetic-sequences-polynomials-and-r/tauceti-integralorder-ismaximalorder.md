---
declaration: def
origin: cited
lean: TauCeti.IntegralOrder.IsMaximalOrder
statement: formalized
---

# TauCeti.IntegralOrder.IsMaximalOrder

An `R`-subalgebra `Λ` of an `F`-algebra `E` is a maximal `R`-order in `E` if it is an `R`-order
in `E` and is not properly contained in another `R`-order in `E`. The definition is exposed, so the
API of `Maximal` applies to it directly, e.g. `h.eq_of_le` and `h.not_gt` for `Maximal.eq_of_le` and
`Maximal.not_gt`.

```lean
TauCeti.IntegralOrder.IsMaximalOrder.{u_1, u_2, u_3} {R : Type u_1} (F : Type u_2) {E : Type u_3}
  [CommRing R] [CommRing F] [Ring E] [Algebra R F] [Algebra F E] [Algebra R E] [IsScalarTower R F E]
  (Λ : Subalgebra R E) : Prop
```

## Depends on

- [TauCeti.IntegralOrder.IsOrder](tauceti-integralorder-isorder.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralOrder.IsMaximalOrder`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Maximal.html#TauCeti.IntegralOrder.IsMaximalOrder).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralOrder.IsMaximalOrder`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Maximal.html#TauCeti.IntegralOrder.IsMaximalOrder)
- [Source of `TauCeti.IntegralOrder.IsMaximalOrder` in TauCeti/RingTheory/IntegralOrder/Maximal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/IntegralOrder/Maximal.lean#L81)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
