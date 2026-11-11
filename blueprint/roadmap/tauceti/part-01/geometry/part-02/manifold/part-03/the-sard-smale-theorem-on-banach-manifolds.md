---
declaration: theorem
origin: cited
lean: ContMDiff.isMeagre_image_criticalPoints_of_isFredholm, TauCeti.isMeagre_image_of_not_isRegularPoint_of_isFredholm
statement: formalized
proof: formalized
---

# The Sard--Smale theorem on Banach manifolds

The critical values of a `C^n` Fredholm map
whose derivative at each point `x` has index `i x`, with `n > max (i x, 0)`, form a meagre set.
The source is hereditarily Lindelöf, for instance second countable, and both manifolds are without
boundary.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Sard--Smale theorem](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-sard-smale-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContMDiff.isMeagre_image_criticalPoints_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Fredholm.html#ContMDiff.isMeagre_image_criticalPoints_of_isFredholm).

## Other forms

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

- [Tau Ceti documentation: `ContMDiff.isMeagre_image_criticalPoints_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Fredholm.html#ContMDiff.isMeagre_image_criticalPoints_of_isFredholm)
- [Source of `ContMDiff.isMeagre_image_criticalPoints_of_isFredholm` in TauCeti/Geometry/Manifold/Sard/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Sard/Fredholm.lean#L108)
