---
declaration: theorem
origin: cited
lean: CliffordAlgebra.kostant_isotypic
statement: formalized
proof: formalized
---

# Kostant's isotypy theorem

Any two irreducible Lie submodules of the Clifford algebra of the
Killing form, under left multiplication by the quadratic lift of the adjoint representation, are
isomorphic.

```lean
CliffordAlgebra.kostant_isotypic.{u, v} {K : Type u} [Field K] [CharZero K] {L : Type v} [LieRing L]
  [LieAlgebra K L] [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L]
  [IsAlgClosed K] :
  LieModule.IsIsotypic K L (CliffordAlgebra (TauCeti.LieAlgebra.killingQuadraticForm K L))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.kostant_isotypic`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.kostant_isotypic).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.kostant_isotypic`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.kostant_isotypic)
- [Source of `CliffordAlgebra.kostant_isotypic` in TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean#L142)
