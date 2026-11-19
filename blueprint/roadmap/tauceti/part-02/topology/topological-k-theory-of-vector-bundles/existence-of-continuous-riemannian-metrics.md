---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_continuousRiemannianMetric
statement: formalized
proof: formalized
---

# Existence of continuous Riemannian metrics

A real vector bundle with finite-dimensional
fibres over a normal paracompact space carries a continuous Riemannian metric.

```lean
TauCeti.nonempty_continuousRiemannianMetric.{u_1, u_2, u_3} {B : Type u_1} [TopologicalSpace B]
  {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type u_3}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → TopologicalSpace (E b)]
  [(b : B) → AddCommGroup (E b)] [(b : B) → _root_.Module ℝ (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] [∀ (b : B), ContinuousConstSMul ℝ (E b)] [NormalSpace B] [ParacompactSpace B]
  [FiniteDimensional ℝ F] : Nonempty (Bundle.ContinuousRiemannianMetric F E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousRiemannianMetric`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Riemannian/Existence.html#TauCeti.nonempty_continuousRiemannianMetric).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousRiemannianMetric`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Riemannian/Existence.html#TauCeti.nonempty_continuousRiemannianMetric)
- [Source of `TauCeti.nonempty_continuousRiemannianMetric` in TauCeti/Topology/VectorBundle/Riemannian/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Riemannian/Existence.lean#L66)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
