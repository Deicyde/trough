---
declaration: theorem
origin: cited
lean: IsLocalExtr.mem_criticalPoints
statement: formalized
proof: formalized
---

# Fermat's theorem on a manifold

A local extremum is a critical point.

```lean
IsLocalExtr.mem_criticalPoints.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} {x : M} [I.Boundaryless]
  (h : IsLocalExtr f x) : x ∈ TauCeti.criticalPoints I f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsLocalExtr.mem_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CriticalPoints.html#IsLocalExtr.mem_criticalPoints).

## Sources

- [Tau Ceti documentation: `IsLocalExtr.mem_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CriticalPoints.html#IsLocalExtr.mem_criticalPoints)
- [Source of `IsLocalExtr.mem_criticalPoints` in TauCeti/Geometry/Manifold/Morse/CriticalPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/CriticalPoints.lean#L425)
