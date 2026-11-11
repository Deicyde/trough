---
declaration: def
origin: cited
lean: TauCeti.IsNashAt
statement: formalized
---

# TauCeti.IsNashAt

A real function `f` on `σ → ℝ` is a *Nash germ* at `x` if it is analytic at `x` and satisfies
a nonzero polynomial relation `P (y, f y) = 0` for all `y` near `x`. Here
`P : (MvPolynomial σ ℝ)[X]` is a polynomial in the value variable whose coefficients are
polynomials in the coordinates, and `P (y, t)` is `(P.map (MvPolynomial.eval y)).eval t`.

```lean
TauCeti.IsNashAt.{u_1} {σ : Type u_1} [Fintype σ] (f : (σ → ℝ) → ℝ) (x : σ → ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNashAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Basic.html#TauCeti.IsNashAt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNashAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Basic.html#TauCeti.IsNashAt)
- [Source of `TauCeti.IsNashAt` in TauCeti/Geometry/RealAlgebraic/Nash/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Nash/Basic.lean#L67)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
