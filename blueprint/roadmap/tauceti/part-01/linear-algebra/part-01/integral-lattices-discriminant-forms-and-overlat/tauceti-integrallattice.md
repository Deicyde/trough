---
declaration: structure
origin: cited
lean: TauCeti.IntegralLattice
statement: formalized
---

# TauCeti.IntegralLattice

An integral symmetric lattice in a rational vector space.

The field `le_dual` says exactly that the form takes integer values on pairs of vectors in
`carrier`.

```lean
TauCeti.IntegralLattice.{u} (V : Type u) [AddCommGroup V] [_root_.Module ℚ V] : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Basic.html#TauCeti.IntegralLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Basic.html#TauCeti.IntegralLattice)
- [Source of `TauCeti.IntegralLattice` in TauCeti/LinearAlgebra/IntegralLattice/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Basic.lean#L54)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
