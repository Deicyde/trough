---
declaration: theorem
origin: cited
lean: TauCeti.Contour.cauchyTheorem_ball, TauCeti.Contour.Cycle.cauchyTheorem_starConvex, TauCeti.Contour.cauchyTheorem_of_pathHomotopy_refl, TauCeti.Contour.cauchyTheorem_starConvex
statement: formalized
proof: formalized
---

# Cauchy's theorem on a disc

**Cauchy's theorem on a disc** — the `Metric.ball` case of
`TauCeti.Contour.cauchyTheorem_starConvex`: a function holomorphic on a disc integrates to zero
along every closed piecewise-`C¹` curve inside it, not only along the boundary circles.

```lean
TauCeti.Contour.cauchyTheorem_ball {f : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ} {c : ℂ} {r : ℝ}
  (hf : DifferentiableOn ℂ f (Metric.ball c r)) (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγr : ∀ t ∈ Set.uIcc a b, γ t ∈ Metric.ball c r) (hclosed : γ a = γ b) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0
```

## Depends on

- [TauCeti.Contour.Cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Proof depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem-roadmap-homologycauc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.cauchyTheorem_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyTheorem_ball).

## Other forms

**Cauchy's theorem for a cycle in a star-shaped open set.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyTheorem_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.Cycle.cauchyTheorem_starConvex).

```lean
TauCeti.Contour.Cycle.cauchyTheorem_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {x : ℂ}
  {C : TauCeti.Contour.Cycle} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω) (hCΩ : C.IsIn Ω)
  (hf : DifferentiableOn ℂ f Ω) : (TauCeti.Contour.Cycle.integral f) C = 0
```

**Cauchy's theorem for a null-homotopic contour.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyTheorem_of_pathHomotopy_refl`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/Homotopy.html#TauCeti.Contour.cauchyTheorem_of_pathHomotopy_refl).

```lean
TauCeti.Contour.cauchyTheorem_of_pathHomotopy_refl {f : ℂ → ℂ} {Ω : Set ℂ} (hΩ : IsOpen Ω) {x : ℂ}
  (p : Path x x) (hp : TauCeti.IsPiecewiseC1On (⇑p.extend) 0 1) (φ : p.Homotopy (Path.refl x))
  (hφΩ : ∀ (st : ↑unitInterval × ↑unitInterval), φ st ∈ Ω) (hf : DifferentiableOn ℂ f Ω) :
  ∫ (t : ℝ) in 0..1, deriv (⇑p.extend) t • f (p.extend t) = 0
```

**Cauchy's theorem on a star-shaped open set.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyTheorem_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyTheorem_starConvex).

```lean
TauCeti.Contour.cauchyTheorem_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {γ : ℝ → ℂ} {a b : ℝ} {x : ℂ}
  (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω) (hf : DifferentiableOn ℂ f Ω)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hclosed : γ a = γ b) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.cauchyTheorem_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyTheorem_ball)
- [Source of `TauCeti.Contour.cauchyTheorem_ball` in TauCeti/Analysis/Contour/StarConvex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/StarConvex.lean#L122)
