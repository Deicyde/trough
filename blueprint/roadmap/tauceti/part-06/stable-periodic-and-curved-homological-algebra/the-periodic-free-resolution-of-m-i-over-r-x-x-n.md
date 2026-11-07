---
declaration: def
origin: cited
lean: TauCeti.cyclicModuleRootPowProjectiveResolution
statement: formalized
---

# The periodic free resolution of `M_i` over `R[X]/(X ^ n)`

With `x` the class of `X`
and `M_i = A ⧸ (x ^ i)`, the complex
`⋯ ⟶ A --x^(n-i)--> A --x^i--> A --x^(n-i)--> A --x^i--> A ⟶ M_i ⟶ 0` is a projective
resolution of `M_i`.

```lean
TauCeti.cyclicModuleRootPowProjectiveResolution.{u} (R : Type u) [CommRing R] (n i : ℕ) :
  CategoryTheory.ProjectiveResolution
    ↧((AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ ⧸
        Ideal.span {MulOpposite.op (AdjoinRoot.root (Polynomial.X ^ n) ^ i)})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicModuleRootPowProjectiveResolution`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Projective/CyclicResolution.html#TauCeti.cyclicModuleRootPowProjectiveResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicModuleRootPowProjectiveResolution`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Projective/CyclicResolution.html#TauCeti.cyclicModuleRootPowProjectiveResolution)
- [Source of `TauCeti.cyclicModuleRootPowProjectiveResolution` in TauCeti/Algebra/Category/ModuleCat/Projective/CyclicResolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Projective/CyclicResolution.lean#L243)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
