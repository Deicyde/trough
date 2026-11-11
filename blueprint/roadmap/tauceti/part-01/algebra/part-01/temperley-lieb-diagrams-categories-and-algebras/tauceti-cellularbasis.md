---
declaration: structure
origin: cited
lean: TauCeti.CellularBasis
statement: formalized
---

# TauCeti.CellularBasis

A **cellular basis** of an `R`-algebra `A`, in the sense of Graham and Lehrer: a basis
`C μ s t` indexed by a cell `μ` of the poset `Λ` and by `s t : M μ`, together with an
anti-involution of `A` sending `C μ s t` to `C μ t s`, such that left multiplication by any
`a : A` acts on `C μ s t`, modulo the basis vectors of the cells strictly below `μ`, by a
combination of the `C μ u t` whose coefficients do not depend on `t`.

```lean
TauCeti.CellularBasis.{u_1, u_2, u_3, u_4} (R : Type u_1) (A : Type u_2) {Λ : Type u_3} [CommRing R]
  [Ring A] [Algebra R A] [Preorder Λ] (M : Λ → Type u_4) [(μ : Λ) → Fintype (M μ)] :
  Type (max (max (max u_1 u_2) u_3) u_4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CellularBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Cellular/Basic.html#TauCeti.CellularBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.CellularBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Cellular/Basic.html#TauCeti.CellularBasis)
- [Source of `TauCeti.CellularBasis` in TauCeti/Algebra/Cellular/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cellular/Basic.lean#L88)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
