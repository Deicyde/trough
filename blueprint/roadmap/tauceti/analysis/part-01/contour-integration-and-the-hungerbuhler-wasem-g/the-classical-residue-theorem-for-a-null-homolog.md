---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous, TauCeti.Contour.Cycle.classicalResidueTheorem_starConvex, TauCeti.Contour.classicalResidueTheorem_nullHomologous, TauCeti.Contour.classicalResidueTheorem_circle_of_meromorphicOrderAt_neg, TauCeti.Contour.classicalResidueTheorem_starConvex
statement: formalized
proof: formalized
---

# The classical residue theorem for a null-homologous contour cycle

Let `U` be open, `S` a
finite set, `f` differentiable on `U ∖ S` and meromorphic at each point of `S` lying in `U`, and let
`C` be a contour cycle in `U`, **null-homologous** in `U`, whose trace **avoids** `S`. Then

`Cycle.integral f C = 2πi · ∑_{s ∈ S} n_s(C) · Res_s f`,

each pole weighted by the generalized winding number of `C` about it.

Null-homology is asked of the cycle only, never of its generators, so the theorem covers the
combinations that make cycles worth having: a difference of two loops around a hole of `U`, neither
of them null-homologous, is. Points of `S` outside `U` are harmless rather than excluded, their
winding number vanishing by null-homology, and `S` may list regular points of `f`, whose residues
are `0`.

Its `S = ∅` case is the homology Cauchy theorem for cycles
(`TauCeti.Contour.Cycle.homologyCauchyTheorem`), and its one-generator case is the single-curve
theorem `TauCeti.Contour.classicalResidueTheorem_nullHomologous`.

```lean
TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous {f : ℂ → ℂ} {S : Finset ℂ} {U : Set ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s)
  {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U) (hoff : ∀ s ∈ S, s ∉ C.trace)
  (hnull : C.IsNullHomologous U) :
  (TauCeti.Contour.Cycle.integral f) C =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Proof depends on

- [The canonical Laurent decomposition](../../part-02/contour/the-canonical-laurent-decomposition.md)
- [The homology Cauchy theorem for contour cycles](../banach-algebras/the-homology-cauchy-theorem-for-contour-cycles.md)
- [The residue theorem for a fixed polar-part decomposition](the-residue-theorem-for-a-fixed-polar-part-decom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous).

## Other forms

**The classical residue theorem for a cycle in a star-shaped open set.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.classicalResidueTheorem_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.Cycle.classicalResidueTheorem_starConvex).

```lean
TauCeti.Contour.Cycle.classicalResidueTheorem_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {x : ℂ}
  {C : TauCeti.Contour.Cycle} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω)
  (hf : DifferentiableOn ℂ f (Ω \ ↑S)) (hmero : ∀ s ∈ S, s ∈ Ω → MeromorphicAt f s) (hCΩ : C.IsIn Ω)
  (hoff : ∀ s ∈ S, s ∉ C.trace) :
  (TauCeti.Contour.Cycle.integral f) C =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s
```

**The classical residue theorem for an arbitrary null-homologous cycle.** Formalized in Tau Ceti as [`TauCeti.Contour.classicalResidueTheorem_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Cycle.html#TauCeti.Contour.classicalResidueTheorem_nullHomologous).

```lean
TauCeti.Contour.classicalResidueTheorem_nullHomologous {f : ℂ → ℂ} {S : Finset ℂ} {U : Set ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s)
  {γ : ℝ → ℂ} {a b : ℝ} (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hclosed : γ a = γ b) (hoff : ∀ t ∈ Set.uIcc a b, γ t ∉ ↑S)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s
```

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

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous)
- [Source of `TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous` in TauCeti/Analysis/Contour/Cycle/Residue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cycle/Residue.lean#L121)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
