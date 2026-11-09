---
declaration: theorem
origin: cited
lean: TauCeti.integral2_slice_sub_eq_sides
statement: formalized
proof: formalized
---

# Stokes' formula on the boundary of a cube for a closed two-form `ψ` that is C¹ on `(ℝ × ℝ) × ℝ`

its integrals over the top and bottom faces `[a, b] × {1}` and `[a, b] × {0}`
differ by the signed sum of its integrals over the four side faces, each parametrized by the
direction of its edge followed by the last coordinate. All integrals are iterated integrals over
oriented intervals, so the corners `a` and `b` may come in either order.

The proof applies Stokes' formula on the rectangle to the cylinder homotopy `h ψ`, whose exterior
derivative is the difference of the top and bottom slices of the closed form `ψ`.

```lean
TauCeti.integral2_slice_sub_eq_sides.{u_1} {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] {ψ : (ℝ × ℝ) × ℝ → ((ℝ × ℝ) × ℝ) [⋀^Fin 2]→L[ℝ] F} (hψ : ContDiff ℝ 1 ψ)
  (hdψ : extDeriv ψ = 0) (a b : ℝ × ℝ) :
  (∫ (s : ℝ) in a.1..b.1, ∫ (t : ℝ) in a.2..b.2, (ψ ((s, t), 1)) ![((1, 0), 0), ((0, 1), 0)]) -
      ∫ (s : ℝ) in a.1..b.1, ∫ (t : ℝ) in a.2..b.2, (ψ ((s, t), 0)) ![((1, 0), 0), ((0, 1), 0)] =
    ((∫ (t : ℝ) in a.2..b.2, ∫ (c : ℝ) in 0..1, (ψ ((a.1, t), c)) ![((0, 1), 0), (0, 1)]) -
        ∫ (t : ℝ) in a.2..b.2, ∫ (c : ℝ) in 0..1, (ψ ((b.1, t), c)) ![((0, 1), 0), (0, 1)]) -
      ((∫ (s : ℝ) in a.1..b.1, ∫ (c : ℝ) in 0..1, (ψ ((s, a.2), c)) ![((1, 0), 0), (0, 1)]) -
        ∫ (s : ℝ) in a.1..b.1, ∫ (c : ℝ) in 0..1, (ψ ((s, b.2), c)) ![((1, 0), 0), (0, 1)])
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral2_slice_sub_eq_sides`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral2_slice_sub_eq_sides).

## Sources

- [Tau Ceti documentation: `TauCeti.integral2_slice_sub_eq_sides`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral2_slice_sub_eq_sides)
- [Source of `TauCeti.integral2_slice_sub_eq_sides` in TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean#L184)
