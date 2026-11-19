---
declaration: def
origin: cited
lean: TauCeti.IsPiecewiseC1On
statement: formalized
---

# Piecewise `C¹` on the interval between `a` and `b`

The curve `γ : ℝ → E` is continuous on
the closed interval `[[a, b]]` (unordered, hence orientation-robust), and there is a finite set of
breakpoints `p ⊆ (min a b, max a b)` such that `γ` is `C¹` on every closed subinterval of `[[a, b]]`
whose interior avoids `p`. Equivalently `γ` is continuously differentiable on each piece between
consecutive breakpoints, with corners allowed only at the breakpoints; an unbounded-derivative cusp
such as `t ↦ √|t|` is excluded, being not `C¹` up to the breakpoint. This is a `Prop` on the raw
function `γ` itself, with no bundled path type.

```lean
TauCeti.IsPiecewiseC1On.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] (γ : ℝ → E)
  (a b : ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPiecewiseC1On`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ContDiff/PiecewiseC1On.html#TauCeti.IsPiecewiseC1On).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPiecewiseC1On`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ContDiff/PiecewiseC1On.html#TauCeti.IsPiecewiseC1On)
- [Source of `TauCeti.IsPiecewiseC1On` in TauCeti/Analysis/Calculus/ContDiff/PiecewiseC1On.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/ContDiff/PiecewiseC1On.lean#L91)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ContourIntegration/STATUS.md)
