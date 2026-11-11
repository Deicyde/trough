---
declaration: structure
origin: cited
lean: FormalGroup.TopNilpotentPoint
statement: formalized
---

# FormalGroup.TopNilpotentPoint

The **points of a formal group law `F` in `A`**: the elements of a topological ring `A`
satisfying `PowerSeries.HasEval`, that is, the topologically nilpotent elements. Evaluation of
power series over `R` at these elements converges when `A` is a complete, Hausdorff, linearly
topologised `R`-algebra; under those assumptions they form a group under `x +_F y = F(x, y)`.
This is the analogue for `A` of the power-series carrier `F.Point σ`.

This is a structure rather than a subtype of `A` so that its group law, which depends on `F`, is
not confused with the ring operations of `A`.

```lean
FormalGroup.TopNilpotentPoint.{u_1, u_2} {R : Type u_1} [CommRing R] (F : FormalGroup R)
  (A : Type u_2) [CommRing A] [TopologicalSpace A] : Type u_2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FormalGroup.TopNilpotentPoint`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/TopNilpotentPoint/Basic.html#FormalGroup.TopNilpotentPoint).

## Sources

- [Tau Ceti documentation: `FormalGroup.TopNilpotentPoint`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/TopNilpotentPoint/Basic.html#FormalGroup.TopNilpotentPoint)
- [Source of `FormalGroup.TopNilpotentPoint` in TauCeti/RingTheory/FormalGroup/TopNilpotentPoint/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/TopNilpotentPoint/Basic.lean#L76)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
