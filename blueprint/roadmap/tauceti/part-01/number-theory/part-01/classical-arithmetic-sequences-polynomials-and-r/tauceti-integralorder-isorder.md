---
declaration: def
origin: cited
lean: TauCeti.IntegralOrder.IsOrder
statement: formalized
---

# TauCeti.IntegralOrder.IsOrder

An `R`-subalgebra `Λ` of an `F`-algebra `E` is an `R`-order in `E` if it is an `R`-lattice in
`E`: finitely generated as an `R`-module, with `F`-span all of `E`.

```lean
TauCeti.IntegralOrder.IsOrder.{u_1, u_2, u_3} {R : Type u_1} (F : Type u_2) {E : Type u_3}
  [CommRing R] [CommRing F] [Ring E] [Algebra R F] [Algebra F E] [Algebra R E] [IsScalarTower R F E]
  (Λ : Subalgebra R E) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralOrder.IsOrder`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Basic.html#TauCeti.IntegralOrder.IsOrder).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralOrder.IsOrder`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Basic.html#TauCeti.IntegralOrder.IsOrder)
- [Source of `TauCeti.IntegralOrder.IsOrder` in TauCeti/RingTheory/IntegralOrder/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/IntegralOrder/Basic.lean#L82)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
