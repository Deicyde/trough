---
declaration: theorem
origin: cited
lean: TauCeti.integral_extDeriv_Icc_off_countable, ContDiffOn.integral_extDerivWithin_fullSimplex
statement: formalized
proof: formalized
---

# Stokes' theorem on a coordinate box

For `a ≤ b` and a `p`-form `ω` on
`Fin (p + 1) → ℝ` which is continuous on the box `Icc a b`, differentiable in its
interior outside a countable exceptional set and has integrable exterior derivative on it,
the integral of `dω` on the standard basis
over the box is the boundary flux of the signed coefficients `(-1)ⁱ ω(e₀, …, êᵢ, …, eₚ)`: the sum
over `i` of their integrals over the face `xᵢ = bᵢ` minus those over the face `xᵢ = aᵢ`.

```lean
TauCeti.integral_extDeriv_Icc_off_countable.{u_1} {p : ℕ} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {a b : Fin (p + 1) → ℝ} (hab : a ≤ b)
  {ω : (Fin (p + 1) → ℝ) → (Fin (p + 1) → ℝ) [⋀^Fin p]→L[ℝ] F} (hc : ContinuousOn ω (Set.Icc a b))
  {s : Set (Fin (p + 1) → ℝ)} (hs : s.Countable)
  (hd : ∀ x ∈ (Set.univ.pi fun i => Set.Ioo (a i) (b i)) \ s, DifferentiableAt ℝ ω x)
  (hi :
    MeasureTheory.IntegrableOn (fun x => (extDeriv ω x) fun i => Pi.single i 1) (Set.Icc a b)
      MeasureTheory.volume) :
  (∫ (x : Fin (p + 1) → ℝ) in Set.Icc a b, (extDeriv ω x) fun i => Pi.single i 1) =
    TauCeti.boxBoundarySum a b fun i x => (-1) ^ ↑i • (ω x) (i.removeNth fun j => Pi.single j 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus along a coordinate of the standard simplex](../../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-along-a-coor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_extDeriv_Icc_off_countable`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Box.html#TauCeti.integral_extDeriv_Icc_off_countable).

## Other forms

**Stokes' theorem on the standard simplex.** Formalized in Tau Ceti as [`ContDiffOn.integral_extDerivWithin_fullSimplex`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Simplex.html#ContDiffOn.integral_extDerivWithin_fullSimplex).

```lean
ContDiffOn.integral_extDerivWithin_fullSimplex.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ℕ}
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

## Sources

- [Tau Ceti documentation: `TauCeti.integral_extDeriv_Icc_off_countable`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Box.html#TauCeti.integral_extDeriv_Icc_off_countable)
- [Source of `TauCeti.integral_extDeriv_Icc_off_countable` in TauCeti/Analysis/Calculus/DifferentialForm/Box.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/DifferentialForm/Box.lean#L56)
