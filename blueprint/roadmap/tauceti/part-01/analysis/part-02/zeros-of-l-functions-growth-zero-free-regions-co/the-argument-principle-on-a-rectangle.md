---
declaration: theorem
origin: cited
lean: TauCeti.Contour.argumentPrinciple_rectBoundary
statement: formalized
proof: formalized
---

# The argument principle on a rectangle

Let `z` be the lower left corner of a closed
rectangle `Rectangle z w` contained in an open set `U`, and let `f` be analytic and nonvanishing at
every point of `U` outside a finite set `S` that avoids the frontier of the rectangle, meromorphic
at the points of `S` in `U`, with integer orders `ord` there. Then the contour integral of
`logDeriv f` along the counterclockwise boundary is `2πi` times the sum of the orders at the points
of `S` in the rectangle.

Nothing is asked of `f` or `ord` at points of `S` outside `U`, which lie outside the rectangle and
do not contribute.

```lean
TauCeti.Contour.argumentPrinciple_rectBoundary {f : ℂ → ℂ} {S : Finset ℂ} {U : Set ℂ} {z w : ℂ}
  {ord : ℂ → ℤ} (hre : z.re ≤ w.re) (him : z.im ≤ w.im) (hU : IsOpen U) (hRU : z.Rectangle w ⊆ U)
  (hoff : ∀ x ∈ U, x ∉ S → AnalyticAt ℂ f x ∧ f x ≠ 0) (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s)
  (hord : ∀ s ∈ S, s ∈ U → meromorphicOrderAt f s = ↑(ord s))
  (hS : ∀ s ∈ S, s ∉ frontier (z.Rectangle w)) :
  ∫ (t : ℝ) in 0..4, deriv (z.rectBoundary w) t • logDeriv f (z.rectBoundary w t) =
    2 * ↑Real.pi * Complex.I * ∑ s ∈ S with s ∈ z.Rectangle w, ↑(ord s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)
- [Fundamental theorem for absolutely continuous curves, integrability](../../../measure-theory/function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)
- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.argumentPrinciple_rectBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Argument/Rectangle.html#TauCeti.Contour.argumentPrinciple_rectBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.argumentPrinciple_rectBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Argument/Rectangle.html#TauCeti.Contour.argumentPrinciple_rectBoundary)
- [Source of `TauCeti.Contour.argumentPrinciple_rectBoundary` in TauCeti/Analysis/Contour/Argument/Rectangle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/Argument/Rectangle.lean#L70)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
