---
declaration: theorem
origin: cited
lean: TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential, ContMDiff.isMeagre_image_criticalPoints_of_isFredholm, TauCeti.isMeagre_image_of_not_isRegularPoint_of_isFredholm
statement: formalized
proof: formalized
---

# Sard–Smale for the universal differential

On a compact Hausdorff manifold without
boundary modelled on a real normed space, and for `k ≥ 2`, the `C^k` functions that are
regular parameters of the universal differential `(x, f) ↦ df_x` form a residual set for the weak
Whitney topology, the topology of the Banach space of `C^k` functions.

```lean
TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential.{u_1, u_2} {E : Type u_1}
  {M : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M] [T2Space M] [CompactSpace M] {k : ℕ} (hk : 2 ≤ k) :
  {f |
      TauCeti.IsRegularSectionParameter E Prod.fst
        (TauCeti.universalDifferential (modelWithCornersSelf ℝ E)) f} ∈
    residual (ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) M ℝ ↑k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Sard--Smale theorem](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-sard-smale-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Generic/Universal/Residual.html#TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential).

## Other forms

**The Sard--Smale theorem on Banach manifolds.** Formalized in Tau Ceti as [`ContMDiff.isMeagre_image_criticalPoints_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Fredholm.html#ContMDiff.isMeagre_image_criticalPoints_of_isFredholm).

```lean
ContMDiff.isMeagre_image_criticalPoints_of_isFredholm.{u_1, u_2, u_3, u_4, u_5, u_6}
  {n : WithTop ℕ∞} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {E' : Type u_4} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] [CompleteSpace E'] {H' : Type u_5} [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [J.Boundaryless] {N : Type u_6} [TopologicalSpace N]
  [ChartedSpace H' N] [IsManifold J 1 N] {f : M → N} [HereditarilyLindelofSpace M]
  (hf : ContMDiff I J n f) (hFred : ∀ (x : M), (mfderiv% f x).IsFredholm)
  (hn : ∀ (x : M), ↑((mfderiv% f x).index.toNat + 1) ≤ n) :
  IsMeagre (f '' {x | ¬TauCeti.IsRegularPoint I J f x})
```

**The Sard--Smale theorem on Banach manifolds.** Formalized in Tau Ceti as [`TauCeti.isMeagre_image_of_not_isRegularPoint_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Fredholm.html#TauCeti.isMeagre_image_of_not_isRegularPoint_of_isFredholm).

```lean
TauCeti.isMeagre_image_of_not_isRegularPoint_of_isFredholm.{u_1, u_2, u_3, u_4, u_5, u_6}
  {n : WithTop ℕ∞} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {E' : Type u_4} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] [CompleteSpace E'] {H' : Type u_5} [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [J.Boundaryless] {N : Type u_6} [TopologicalSpace N]
  [ChartedSpace H' N] [IsManifold J 1 N] {f : M → N} {s : Set M} [LindelofSpace ↑s]
  (hf : ∀ x ∈ s, ContMDiffAt I J n f x) (hFred : ∀ x ∈ s, (mfderiv% f x).IsFredholm)
  (hn : ∀ x ∈ s, ↑((mfderiv% f x).index.toNat + 1) ≤ n)
  (hs : ∀ x ∈ s, ¬TauCeti.IsRegularPoint I J f x) : IsMeagre (f '' s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Generic/Universal/Residual.html#TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential)
- [Source of `TauCeti.mem_residual_setOf_isRegularSectionParameter_universalDifferential` in TauCeti/Geometry/Manifold/Morse/Generic/Universal/Residual.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Generic/Universal/Residual.lean#L81)
