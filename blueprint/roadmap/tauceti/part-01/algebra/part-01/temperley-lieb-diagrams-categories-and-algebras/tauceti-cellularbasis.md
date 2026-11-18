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
- [Source of `TauCeti.CellularBasis` in TauCeti/Algebra/Cellular/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cellular/Basic.lean#L92)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
