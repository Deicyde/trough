---
declaration: theorem
origin: cited
lean: TauCeti.Contour.classicalResidueTheorem_circle, TauCeti.Contour.classicalResidueTheorem_circle_of_meromorphicOrderAt_neg, TauCeti.Contour.classicalResidueTheorem_starConvex
statement: formalized
proof: formalized
---

# The classical residue theorem on a circle

If `f` is meromorphic on the
closed disc `C(c, R)` (`R > 0`) and every point of nonzero meromorphic order lies in a finite set
`S` inside the open disc, then `∮_{C(c,R)} f = 2πi · ∑_{s ∈ S} residue f s`. Since residues at
non-poles vanish, `classicalResidueTheorem_circle_of_meromorphicOrderAt_neg` proves the same
conclusion asking only the poles (points of negative order) to lie in `S`.

```lean
TauCeti.Contour.classicalResidueTheorem_circle {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
  (S : Finset ℂ) (hf : MeromorphicOn f (Metric.closedBall c R)) (hS : ↑S ⊆ Metric.ball c R)
  (hsupp : ∀ z ∈ Metric.closedBall c R, meromorphicOrderAt f z ≠ 0 → z ∈ S) :
  circleIntegral f c R = 2 * ↑Real.pi * Complex.I * ∑ s ∈ S, TauCeti.Contour.residue f s
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Cauchy–Goursat for a pole-free meromorphic function](../../part-02/contour/cauchy-goursat-for-a-pole-free-meromorphic-funct.md)
- [The classical residue theorem for a null-homologous contour cycle](the-classical-residue-theorem-for-a-null-homolog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.classicalResidueTheorem_circle`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.classicalResidueTheorem_circle).

## Other forms

**The classical residue theorem on a circle (sharp support form).** Formalized in Tau Ceti as [`TauCeti.Contour.classicalResidueTheorem_circle_of_meromorphicOrderAt_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.classicalResidueTheorem_circle_of_meromorphicOrderAt_neg).

```lean
TauCeti.Contour.classicalResidueTheorem_circle_of_meromorphicOrderAt_neg {f : ℂ → ℂ} {c : ℂ} {R : ℝ}
  (hR : 0 < R) (S : Finset ℂ) (hf : MeromorphicOn f (Metric.closedBall c R))
  (hS : ↑S ⊆ Metric.ball c R)
  (hsupp : ∀ z ∈ Metric.closedBall c R, meromorphicOrderAt f z < 0 → z ∈ S) :
  circleIntegral f c R = 2 * ↑Real.pi * Complex.I * ∑ s ∈ S, TauCeti.Contour.residue f s
```

**The classical residue theorem on a star-shaped open set.** Formalized in Tau Ceti as [`TauCeti.Contour.classicalResidueTheorem_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.classicalResidueTheorem_starConvex).

```lean
TauCeti.Contour.classicalResidueTheorem_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  {x : ℂ} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω)
  (hf : DifferentiableOn ℂ f (Ω \ ↑S)) (hmero : ∀ s ∈ S, s ∈ Ω → MeromorphicAt f s)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hclosed : γ a = γ b)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ∉ ↑S) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.classicalResidueTheorem_circle`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.classicalResidueTheorem_circle)
- [Source of `TauCeti.Contour.classicalResidueTheorem_circle` in TauCeti/Analysis/Contour/Residue/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Residue/Theorem.lean#L344)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
