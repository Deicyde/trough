---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero, TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint, TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator, TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator_of_equation_eq_zero
statement: formalized
proof: formalized
---

# The Weitzenböck formula at a vortex

where the vortex equation holds,
`L_x L_x* = (-Δ + P) ⊕ (-Δ_a + 1 / 8 + P / 2)` with `P = p² + q² = |α|² / 4`. The section part is
displayed in real coordinates as in `gaugeFixedOperator_gaugeFixedAdjoint`.

```lean
TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero
  {x η : ℂ → EuclideanSpace ℝ (Fin 4)} {z : ℂ} (hx : DifferentiableAt ℝ x z)
  (hη : ContDiffAt ℝ 2 η z) (hsol : TauCeti.Vortex.equation x z = 0) :
  TauCeti.Vortex.gaugeFixedOperator x (TauCeti.Vortex.gaugeFixedAdjoint x η) z =
    !₂[-Laplacian.laplacian (fun w => (η w).ofLp 0) z +
        ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (η z).ofLp 0,
      -Laplacian.laplacian (fun w => (η w).ofLp 1) z +
        ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (η z).ofLp 1,
      -Laplacian.laplacian (fun w => (η w).ofLp 2) z +
            (1 / 8 + ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 + (x z).ofLp 0 ^ 2 +
                (x z).ofLp 1 ^ 2) *
              (η z).ofLp 2 +
          ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
              (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
            (η z).ofLp 3 +
        2 *
          ((x z).ofLp 0 * (fderiv ℝ (fun w => (η w).ofLp 3) z) 1 +
            (x z).ofLp 1 * (fderiv ℝ (fun w => (η w).ofLp 3) z) Complex.I),
      -Laplacian.laplacian (fun w => (η w).ofLp 3) z +
            (1 / 8 + ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 + (x z).ofLp 0 ^ 2 +
                (x z).ofLp 1 ^ 2) *
              (η z).ofLp 3 -
          ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
              (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
            (η z).ofLp 2 -
        2 *
          ((x z).ofLp 0 * (fderiv ℝ (fun w => (η w).ofLp 2) z) 1 +
            (x z).ofLp 1 * (fderiv ℝ (fun w => (η w).ofLp 2) z) Complex.I)]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/GaugeFixed.html#TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero).

## Other forms

**The Weitzenböck formula for `L_x L_x*`.** Formalized in Tau Ceti as [`TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/GaugeFixed.html#TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint).

```lean
TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint {x η : ℂ → EuclideanSpace ℝ (Fin 4)} {z : ℂ}
  (hx : DifferentiableAt ℝ x z) (hη : ContDiffAt ℝ 2 η z) :
  TauCeti.Vortex.gaugeFixedOperator x (TauCeti.Vortex.gaugeFixedAdjoint x η) z =
    !₂[-Laplacian.laplacian (fun w => (η w).ofLp 0) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (η z).ofLp 0 -
          (η z).ofLp 2 * (TauCeti.Vortex.equation x z).ofLp 2 +
        (η z).ofLp 3 * (TauCeti.Vortex.equation x z).ofLp 1,
      -Laplacian.laplacian (fun w => (η w).ofLp 1) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (η z).ofLp 1 +
          (η z).ofLp 2 * (TauCeti.Vortex.equation x z).ofLp 1 +
        (η z).ofLp 3 * (TauCeti.Vortex.equation x z).ofLp 2,
      -Laplacian.laplacian (fun w => (η w).ofLp 2) z +
                ((TauCeti.Vortex.equation x z).ofLp 0 + 1 / 8 +
                        ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 +
                      (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (η z).ofLp 2 +
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (η z).ofLp 3 +
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (η w).ofLp 3) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (η w).ofLp 3) z) Complex.I) -
          (TauCeti.Vortex.equation x z).ofLp 2 * (η z).ofLp 0 +
        (TauCeti.Vortex.equation x z).ofLp 1 * (η z).ofLp 1,
      -Laplacian.laplacian (fun w => (η w).ofLp 3) z +
                ((TauCeti.Vortex.equation x z).ofLp 0 + 1 / 8 +
                        ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 +
                      (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (η z).ofLp 3 -
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (η z).ofLp 2 -
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (η w).ofLp 2) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (η w).ofLp 2) z) Complex.I) +
          (TauCeti.Vortex.equation x z).ofLp 1 * (η z).ofLp 0 +
        (TauCeti.Vortex.equation x z).ofLp 2 * (η z).ofLp 1]
```

**The Weitzenböck formula for `L_x* L_x` at an arbitrary field.** Formalized in Tau Ceti as [`TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/GaugeFixed.html#TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator).

```lean
TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator {x y : ℂ → EuclideanSpace ℝ (Fin 4)} {z : ℂ}
  (hx : DifferentiableAt ℝ x z) (hy : ContDiffAt ℝ 2 y z) :
  TauCeti.Vortex.gaugeFixedAdjoint x (TauCeti.Vortex.gaugeFixedOperator x y) z =
    !₂[-Laplacian.laplacian (fun w => (y w).ofLp 0) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (y z).ofLp 0 +
          ((x z).ofLp 0 * (x z).ofLp 2 + (x z).ofLp 1 * (x z).ofLp 3 -
                (fderiv ℝ (fun w => (x w).ofLp 2) z) Complex.I +
              (fderiv ℝ (fun w => (x w).ofLp 3) z) 1) *
            (y z).ofLp 2 -
        ((x z).ofLp 1 * (x z).ofLp 2 - (x z).ofLp 0 * (x z).ofLp 3 +
              (fderiv ℝ (fun w => (x w).ofLp 2) z) 1 +
            (fderiv ℝ (fun w => (x w).ofLp 3) z) Complex.I) *
          (y z).ofLp 3,
      -Laplacian.laplacian (fun w => (y w).ofLp 1) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (y z).ofLp 1 +
          ((x z).ofLp 1 * (x z).ofLp 2 - (x z).ofLp 0 * (x z).ofLp 3 +
                (fderiv ℝ (fun w => (x w).ofLp 2) z) 1 +
              (fderiv ℝ (fun w => (x w).ofLp 3) z) Complex.I) *
            (y z).ofLp 2 +
        ((x z).ofLp 0 * (x z).ofLp 2 + (x z).ofLp 1 * (x z).ofLp 3 -
              (fderiv ℝ (fun w => (x w).ofLp 2) z) Complex.I +
            (fderiv ℝ (fun w => (x w).ofLp 3) z) 1) *
          (y z).ofLp 3,
      -Laplacian.laplacian (fun w => (y w).ofLp 2) z +
                (TauCeti.Vortex.curvature x z + (x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2 +
                      (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (y z).ofLp 2 +
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (y z).ofLp 3 +
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (y w).ofLp 3) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (y w).ofLp 3) z) Complex.I) +
          ((x z).ofLp 0 * (x z).ofLp 2 + (x z).ofLp 1 * (x z).ofLp 3 -
                (fderiv ℝ (fun w => (x w).ofLp 2) z) Complex.I +
              (fderiv ℝ (fun w => (x w).ofLp 3) z) 1) *
            (y z).ofLp 0 +
        ((x z).ofLp 1 * (x z).ofLp 2 - (x z).ofLp 0 * (x z).ofLp 3 +
              (fderiv ℝ (fun w => (x w).ofLp 2) z) 1 +
            (fderiv ℝ (fun w => (x w).ofLp 3) z) Complex.I) *
          (y z).ofLp 1,
      -Laplacian.laplacian (fun w => (y w).ofLp 3) z +
                (TauCeti.Vortex.curvature x z + (x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2 +
                      (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (y z).ofLp 3 -
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (y z).ofLp 2 -
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (y w).ofLp 2) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (y w).ofLp 2) z) Complex.I) -
          ((x z).ofLp 1 * (x z).ofLp 2 - (x z).ofLp 0 * (x z).ofLp 3 +
                (fderiv ℝ (fun w => (x w).ofLp 2) z) 1 +
              (fderiv ℝ (fun w => (x w).ofLp 3) z) Complex.I) *
            (y z).ofLp 0 +
        ((x z).ofLp 0 * (x z).ofLp 2 + (x z).ofLp 1 * (x z).ofLp 3 -
              (fderiv ℝ (fun w => (x w).ofLp 2) z) Complex.I +
            (fderiv ℝ (fun w => (x w).ofLp 3) z) 1) *
          (y z).ofLp 1]
```

**The Weitzenböck formula for `L_x* L_x` at a vortex.** Formalized in Tau Ceti as [`TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator_of_equation_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/GaugeFixed.html#TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator_of_equation_eq_zero).

```lean
TauCeti.Vortex.gaugeFixedAdjoint_gaugeFixedOperator_of_equation_eq_zero
  {x y : ℂ → EuclideanSpace ℝ (Fin 4)} {z : ℂ} (hx : DifferentiableAt ℝ x z)
  (hy : ContDiffAt ℝ 2 y z) (hsol : TauCeti.Vortex.equation x z = 0) :
  TauCeti.Vortex.gaugeFixedAdjoint x (TauCeti.Vortex.gaugeFixedOperator x y) z =
    !₂[-Laplacian.laplacian (fun w => (y w).ofLp 0) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (y z).ofLp 0 +
          (TauCeti.Vortex.covariantDerivative x z 1).im * (y z).ofLp 2 -
        (TauCeti.Vortex.covariantDerivative x z 1).re * (y z).ofLp 3,
      -Laplacian.laplacian (fun w => (y w).ofLp 1) z +
            ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) * (y z).ofLp 1 +
          (TauCeti.Vortex.covariantDerivative x z 1).re * (y z).ofLp 2 +
        (TauCeti.Vortex.covariantDerivative x z 1).im * (y z).ofLp 3,
      -Laplacian.laplacian (fun w => (y w).ofLp 2) z +
                (3 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 - 1 / 8 + (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (y z).ofLp 2 +
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (y z).ofLp 3 +
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (y w).ofLp 3) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (y w).ofLp 3) z) Complex.I) +
          (TauCeti.Vortex.covariantDerivative x z 1).im * (y z).ofLp 0 +
        (TauCeti.Vortex.covariantDerivative x z 1).re * (y z).ofLp 1,
      -Laplacian.laplacian (fun w => (y w).ofLp 3) z +
                (3 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2) / 2 - 1 / 8 + (x z).ofLp 0 ^ 2 +
                    (x z).ofLp 1 ^ 2) *
                  (y z).ofLp 3 -
              ((fderiv ℝ (fun w => (x w).ofLp 0) z) 1 +
                  (fderiv ℝ (fun w => (x w).ofLp 1) z) Complex.I) *
                (y z).ofLp 2 -
            2 *
              ((x z).ofLp 0 * (fderiv ℝ (fun w => (y w).ofLp 2) z) 1 +
                (x z).ofLp 1 * (fderiv ℝ (fun w => (y w).ofLp 2) z) Complex.I) -
          (TauCeti.Vortex.covariantDerivative x z 1).re * (y z).ofLp 0 +
        (TauCeti.Vortex.covariantDerivative x z 1).im * (y z).ofLp 1]
```

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/GaugeFixed.html#TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero)
- [Source of `TauCeti.Vortex.gaugeFixedOperator_gaugeFixedAdjoint_of_equation_eq_zero` in TauCeti/Analysis/PDE/Vortex/GaugeFixed.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Vortex/GaugeFixed.lean#L363)
