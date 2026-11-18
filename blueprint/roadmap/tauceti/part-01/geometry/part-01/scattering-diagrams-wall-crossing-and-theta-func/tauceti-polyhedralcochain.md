---
declaration: def
origin: cited
lean: TauCeti.PolyhedralCochain
statement: formalized
---

# TauCeti.PolyhedralCochain

Polyhedral cochains of codimension `k` with coefficients in the `R`-module `E`: finite sums
of oriented cells with coefficients in `E`, modulo reversal and subdivision.

```lean
TauCeti.PolyhedralCochain.{u_1, u_2, u_3, u_4} {N : Type u_1} {V : Type u_2} [AddCommGroup N]
  [NormedAddCommGroup V] [NormedSpace ℝ V] {i : N →+ V} (R : Type u_3) [Ring R]
  (h : TauCeti.Toric.IsIntegralLattice i) (E : Type u_4) [AddCommGroup E] [_root_.Module R E]
  (k : ℕ) : Type (max (max u_2 u_4) u_4 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PolyhedralCochain`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralCochain/Basic.html#TauCeti.PolyhedralCochain).

## Sources

- [Tau Ceti documentation: `TauCeti.PolyhedralCochain`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralCochain/Basic.html#TauCeti.PolyhedralCochain)
- [Source of `TauCeti.PolyhedralCochain` in TauCeti/Geometry/Convex/PolyhedralCochain/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Convex/PolyhedralCochain/Basic.lean#L285)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
