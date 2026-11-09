---
declaration: def
origin: cited
lean: TauCeti.shapeOperator
statement: formalized
---

# TauCeti.shapeOperator

The **shape operator** `S_ν` of `i : V → E` at `x` in the direction `ν`: the endomorphism of
`V` with `⟪Di(x) (S_ν v), Di(x) w⟫ = ⟪ν, B(v, w)⟫` for all `v` and `w`, where `B` is the second
fundamental form. It is defined when `Di(x)` is injective, so that the induced metric
`⟪Di(x) v, Di(x) w⟫` is nondegenerate, and is `0` otherwise.

```lean
TauCeti.shapeOperator.{u_1, u_2} {V : Type u_1} {E : Type u_2} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  (i : V → E) (x : V) (ν : E) : Module.End ℝ V
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.shapeOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#TauCeti.shapeOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.shapeOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#TauCeti.shapeOperator)
- [Source of `TauCeti.shapeOperator` in TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean#L86)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
