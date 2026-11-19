---
declaration: structure
origin: cited
lean: TauCeti.LieAlgebroid
statement: formalized
---

# TauCeti.LieAlgebroid

A Lie algebroid structure on a smooth real vector bundle `V → M`: a smooth fibrewise linear
anchor `ρ : V → TM` and an `ℝ`-bilinear Lie bracket on the smooth sections of `V` satisfying the
Leibniz rule `[a, f • b] = f • [a, b] + (ρ(a) f) • b`. That the anchor intertwines the brackets is
a consequence, `TauCeti.LieAlgebroid.anchor_bracket`.

```lean
TauCeti.LieAlgebroid.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H) {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] (F : Type u_4)
  [NormedAddCommGroup F] [NormedSpace ℝ F] (V : M → Type u_5)
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] : Type (max (max u_1 u_3) u_5)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebroid`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.html#TauCeti.LieAlgebroid).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebroid`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.html#TauCeti.LieAlgebroid)
- [Source of `TauCeti.LieAlgebroid` in TauCeti/Geometry/Manifold/LieAlgebroid/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.lean#L78)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
