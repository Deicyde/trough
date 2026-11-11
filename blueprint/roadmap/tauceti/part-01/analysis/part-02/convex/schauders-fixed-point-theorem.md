---
declaration: theorem
origin: cited
lean: TauCeti.schauderFixedPoint_closedConvex, TauCeti.schauderFixedPoint_closedConvex_continuousOn, TauCeti.schauderFixedPoint_compactConvex
statement: formalized
proof: formalized
---

# Schauder's fixed-point theorem

a continuous self-map of a nonempty closed convex set `C`
in a real normed space, whose range has compact closure in the space, has a fixed point.

```lean
TauCeti.schauderFixedPoint_closedConvex.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {C : Set E} (hC : IsClosed C) (hconv : Convex ℝ C) (hne : C.Nonempty)
  (f : C(↑C, ↑C)) (hK : IsCompact (closure (Set.range fun x => ↑(f x)))) :
  ∃ x, Function.IsFixedPt (⇑f) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brouwer's fixed-point theorem](../../../algebraic-topology/singular/brouwers-fixed-point-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.schauderFixedPoint_closedConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schauderFixedPoint_closedConvex).

## Other forms

**Schauder's fixed-point theorem.** Formalized in Tau Ceti as [`TauCeti.schauderFixedPoint_closedConvex_continuousOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schauderFixedPoint_closedConvex_continuousOn).

```lean
TauCeti.schauderFixedPoint_closedConvex_continuousOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {C : Set E} (hC : IsClosed C) (hconv : Convex ℝ C) (hne : C.Nonempty)
  {f : E → E} (hf : ContinuousOn f C) (hfC : Set.MapsTo f C C) (hK : IsCompact (closure (f '' C))) :
  ∃ x ∈ C, Function.IsFixedPt f x
```

**Schauder's fixed-point theorem for compact convex sets.** Formalized in Tau Ceti as [`TauCeti.schauderFixedPoint_compactConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schauderFixedPoint_compactConvex).

```lean
TauCeti.schauderFixedPoint_compactConvex.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {C : Set E} (hC : IsCompact C) (hconv : Convex ℝ C) (hne : C.Nonempty)
  (f : C(↑C, ↑C)) : ∃ x, Function.IsFixedPt (⇑f) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.schauderFixedPoint_closedConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schauderFixedPoint_closedConvex)
- [Source of `TauCeti.schauderFixedPoint_closedConvex` in TauCeti/Analysis/Convex/SchauderFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/SchauderFixedPoint.lean#L127)
