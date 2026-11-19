---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint
statement: formalized
proof: formalized
---

# Bott's normal-slice criterion

A critical submanifold `i` of `f` is Morse–Bott exactly
when, at every `s : S`, the normal slice `v ↦ f (exp_{i s} v)` on the orthogonal normal space has
a nondegenerate critical point at `0`.

```lean
TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M]
  [Bundle.RiemannianBundle fun y => TangentSpace I y]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun y => TangentSpace I y] {E' : Type u_4} {H' : Type u_5}
  {S : Type u_6} {P : Type u_7} [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [TopologicalSpace S] [ChartedSpace H' S] {f : M → ℝ}
  {n : WithTop ℕ∞} {i : TauCeti.SmoothEmbedding J I n S M} (hn : n ≠ 0)
  (h : i.IsCriticalSubmanifold f) :
  i.IsNondegenerateCriticalSubmanifold f ↔
    ∀ (s : S),
      TauCeti.IsNondegenerateCriticalPoint
        (fun v => f (i.normalExp hn ⟨s, (i.normalClass s hn) ↑v⟩)) 0
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Proof depends on

- [The Koszul formula](../../../part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/NormalExp.html#TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/NormalExp.html#TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint)
- [Source of `TauCeti.SmoothEmbedding.IsCriticalSubmanifold.isNondegenerateCriticalSubmanifold_iff_forall_isNondegenerateCriticalPoint` in TauCeti/Geometry/Manifold/Morse/Bott/NormalExp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Bott/NormalExp.lean#L163)
