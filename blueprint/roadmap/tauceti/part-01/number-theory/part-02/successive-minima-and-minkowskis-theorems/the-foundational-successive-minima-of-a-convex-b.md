---
declaration: theorem
origin: cited
lean: MeasureTheory.coe_successiveMin
statement: formalized
proof: formalized
---

# The foundational successive minima of a convex body

On a convex body `K`, the successive
minimum `MeasureTheory.successiveMin L K i` of an arbitrary set, defined through the rank of
`r • K ∩ L`, is the successive minimum `successiveMin L K i`, defined through independent families.
No hypothesis on `L`, `K` or `E` is needed: an index `i` forces `E` to be finite-dimensional.

```lean
MeasureTheory.coe_successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (L : Submodule ℤ E) (K : ConvexBody E) (i : Fin (Module.finrank ℝ E)) :
  ↑(MeasureTheory.successiveMin L ↑K ↑i) = ZLattice.successiveMin L K i
```

## Depends on

- [MeasureTheory.successiveMin](measuretheory-successivemin.md)
- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.coe_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#MeasureTheory.coe_successiveMin).

## Sources

- [Tau Ceti documentation: `MeasureTheory.coe_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#MeasureTheory.coe_successiveMin)
- [Source of `MeasureTheory.coe_successiveMin` in TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean#L265)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
