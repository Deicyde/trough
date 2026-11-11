---
declaration: theorem
origin: cited
lean: ContDiffOn.integral_extDerivWithin_fullSimplex
statement: formalized
proof: formalized
---

# Stokes' theorem on the standard simplex

For a `p`-form `ω` that is `C¹` on the standard
simplex `Δᵖ⁺¹`, the integral of its exterior derivative over `Δᵖ⁺¹` is the alternating sum over
`i` of the integrals over `Δᵖ` of its pullbacks along the face maps `simplexMapAmbient i.succAbove`,
all forms being evaluated on the standard basis.

```lean
ContDiffOn.integral_extDerivWithin_fullSimplex.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {p : ℕ}
  {ω : EuclideanSpace ℝ (Fin (p + 1)) → EuclideanSpace ℝ (Fin (p + 1)) [⋀^Fin p]→L[ℝ] F}
  (hω : ContDiffOn ℝ 1 ω (TauCeti.fullSimplex (p + 1))) :
  (∫ (x : EuclideanSpace ℝ (Fin (p + 1))) in TauCeti.fullSimplex (p + 1),
      (extDerivWithin ω (TauCeti.fullSimplex (p + 1)) x) fun i => EuclideanSpace.single i 1) =
    ∑ i,
      (-1) ^ ↑i •
        ∫ (y : EuclideanSpace ℝ (Fin p)) in TauCeti.fullSimplex p,
          (ω ((TauCeti.simplexMapAmbient i.succAbove) y)) fun k =>
            (TauCeti.simplexMapAmbient i.succAbove).contLinear (EuclideanSpace.single k 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus along a coordinate of the standard simplex](../../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-along-a-coor.md)

## Lean

Formalized in Tau Ceti as [`ContDiffOn.integral_extDerivWithin_fullSimplex`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Simplex.html#ContDiffOn.integral_extDerivWithin_fullSimplex).

## Sources

- [Tau Ceti documentation: `ContDiffOn.integral_extDerivWithin_fullSimplex`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Simplex.html#ContDiffOn.integral_extDerivWithin_fullSimplex)
- [Source of `ContDiffOn.integral_extDerivWithin_fullSimplex` in TauCeti/Analysis/Calculus/DifferentialForm/Simplex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/DifferentialForm/Simplex.lean#L160)
