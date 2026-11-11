---
declaration: theorem
origin: cited
lean: TauCeti.brouwerFixedPoint_topCatDisk, TauCeti.brouwerFixedPoint_closedBall, TauCeti.brouwerFixedPoint_compactConvex, TauCeti.brouwerFixedPoint_compactConvex_continuousOn, TauCeti.brouwerFixedPoint_compactConvex_finiteSpan
statement: formalized
proof: formalized
---

# Brouwer's fixed-point theorem

every continuous self-map of the disk `Dⁿ` has a fixed
point.

```lean
TauCeti.brouwerFixedPoint_topCatDisk.{w} (n : ℕ) (f : TopCat.disk n ⟶ TopCat.disk n) :
  ∃ x, Function.IsFixedPt (⇑(CategoryTheory.ConcreteCategory.hom f)) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The no-retraction theorem](the-no-retraction-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brouwerFixedPoint_topCatDisk`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_topCatDisk).

## Other forms

**Brouwer's fixed-point theorem for closed balls.** Formalized in Tau Ceti as [`TauCeti.brouwerFixedPoint_closedBall`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_closedBall).

```lean
TauCeti.brouwerFixedPoint_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] (x : E) {r : ℝ} (hr : 0 ≤ r)
  (f : C(↑(Metric.closedBall x r), ↑(Metric.closedBall x r))) : ∃ y, Function.IsFixedPt (⇑f) y
```

**Brouwer's fixed-point theorem for compact convex sets.** Formalized in Tau Ceti as [`TauCeti.brouwerFixedPoint_compactConvex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_compactConvex).

```lean
TauCeti.brouwerFixedPoint_compactConvex.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {C : Set E} (hC : IsCompact C) (hconv : Convex ℝ C)
  (hne : C.Nonempty) (f : C(↑C, ↑C)) : ∃ x, Function.IsFixedPt (⇑f) x
```

**Brouwer's fixed-point theorem for compact convex sets, for a function on the ambient space.** Formalized in Tau Ceti as [`TauCeti.brouwerFixedPoint_compactConvex_continuousOn`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_compactConvex_continuousOn).

```lean
TauCeti.brouwerFixedPoint_compactConvex_continuousOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {C : Set E} [FiniteDimensional ℝ ↥(Submodule.span ℝ C)] (hC : IsCompact C)
  (hconv : Convex ℝ C) (hne : C.Nonempty) {f : E → E} (hf : ContinuousOn f C)
  (hfC : Set.MapsTo f C C) : ∃ x ∈ C, Function.IsFixedPt f x
```

**Brouwer's fixed-point theorem for compact convex sets in a finite-dimensional subspace.** Formalized in Tau Ceti as [`TauCeti.brouwerFixedPoint_compactConvex_finiteSpan`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_compactConvex_finiteSpan).

```lean
TauCeti.brouwerFixedPoint_compactConvex_finiteSpan.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] (V : Submodule ℝ E) [FiniteDimensional ℝ ↥V] {C : Set E} (hCV : C ⊆ ↑V)
  (hC : IsCompact C) (hconv : Convex ℝ C) (hne : C.Nonempty) (f : C(↑C, ↑C)) :
  ∃ x, Function.IsFixedPt (⇑f) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.brouwerFixedPoint_topCatDisk`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.brouwerFixedPoint_topCatDisk)
- [Source of `TauCeti.brouwerFixedPoint_topCatDisk` in TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.lean#L89)
