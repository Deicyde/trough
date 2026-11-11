---
declaration: def
origin: cited
lean: LinearMap.IsLeftInvariantIntegral
statement: formalized
---

# LinearMap.IsLeftInvariantIntegral

Left invariance of an algebraic integral: `(id ⊗ h) Δ(a) = h(a) 1`.

```lean
LinearMap.IsLeftInvariantIntegral.{u_1, u_2} {R : Type u_1} {H : Type u_2} [CommSemiring R]
  [Semiring H] [Bialgebra R H] (h : H →ₗ[R] R) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsLeftInvariantIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral.html#LinearMap.IsLeftInvariantIntegral).

## Sources

- [Tau Ceti documentation: `LinearMap.IsLeftInvariantIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral.html#LinearMap.IsLeftInvariantIntegral)
- [Source of `LinearMap.IsLeftInvariantIntegral` in TauCeti/Algebra/HopfAlgebra/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/HopfAlgebra/Integral.lean#L46)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
