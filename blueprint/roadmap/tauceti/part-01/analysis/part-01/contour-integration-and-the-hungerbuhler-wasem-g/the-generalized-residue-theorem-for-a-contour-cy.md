---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles, TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex, TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles, TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex
statement: formalized
proof: formalized
---

# The generalized residue theorem for a contour cycle with simple poles — HW Thm 3.3's unconditional regime for cycles

When every prescribed singularity in `U` is at worst a simple
pole, conditions (A′) and (B) hold automatically along each curve of the cycle
(`TauCeti.Contour.conditionAprime_of_simple_poles`,
`TauCeti.Contour.conditionB_of_simple_poles`), leaving no regularity hypotheses beyond the
immersions. This is the form the argument principle consumes, a logarithmic derivative having
only simple poles. No singularity is required to lie in `U`, and no hypothesis is imposed on `f`
at those outside `U`: they carry winding number zero by null-homology and drop out of the sum.

```lean
TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles {f : ℂ → ℂ} {U : Set ℂ}
  {C : TauCeti.Contour.Cycle} (hU : IsOpen U) (S : Finset ℂ) (hf : DifferentiableOn ℂ f (U \ ↑S))
  (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s) (hCU : C.IsIn U)
  (h_imm :
    ∀ γ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.IsPwC1ImmersionOn (Function.extend Subtype.val γ.toFun 0) γ.a γ.b)
  (hbase : ∀ γ ∈ FreeAbelianGroup.support C, Function.extend Subtype.val γ.toFun 0 γ.a ∉ ↑S)
  (hnull : C.IsNullHomologous U) (h_simple : ∀ s ∈ S, s ∈ U → ↑(-1) ≤ meromorphicOrderAt f s) :
  C.HasCauchyPV f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [Piecewise `C¹` on the interval between `a` and `b`](piecewise-c1-on-the-interval-between-a-and-b.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Proof depends on

- [The Hungerbühler–Wasem generalized residue theorem for a contour cycle (HW Thm 3.3)](the-hungerbuhler-wasem-generalized-residue-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles).

## Other forms

**The generalized residue theorem for a cycle in a star-shaped open set, simple-pole regime.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex).

```lean
TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex {f : ℂ → ℂ}
  {Ω : Set ℂ} {x : ℂ} {C : TauCeti.Contour.Cycle} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω)
  (hopen : IsOpen Ω) (hf : DifferentiableOn ℂ f (Ω \ ↑S))
  (hmero : ∀ s ∈ S, s ∈ Ω → MeromorphicAt f s) (hCΩ : C.IsIn Ω)
  (h_imm :
    ∀ δ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.IsPwC1ImmersionOn (Function.extend Subtype.val δ.toFun 0) δ.a δ.b)
  (hbase : ∀ δ ∈ FreeAbelianGroup.support C, Function.extend Subtype.val δ.toFun 0 δ.a ∉ ↑S)
  (h_simple : ∀ s ∈ S, s ∈ Ω → ↑(-1) ≤ meromorphicOrderAt f s) :
  C.HasCauchyPV f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s)
```

**The generalized residue theorem for simple poles — HW Thm 3.3's unconditional regime.** Formalized in Tau Ceti as [`TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles).

```lean
TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles {f : ℂ → ℂ} {U : Set ℂ}
  (hU : IsOpen U) (S : Finset ℂ) (γ : ℝ → ℂ) (a b : ℝ)
  (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hclosed : γ a = γ b) (hγa : γ a ∉ ↑S)
  (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hf : DifferentiableOn ℂ f (U \ ↑S))
  (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s) (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (h_simple : ∀ s ∈ S, s ∈ U → ↑(-1) ≤ meromorphicOrderAt f s) :
  TauCeti.Contour.HasCauchyPV γ a b f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s)
```

**The generalized residue theorem on a star-shaped open set, simple-pole regime.** Formalized in Tau Ceti as [`TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex).

```lean
TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex {f : ℂ → ℂ} {Ω : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} {x : ℂ} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω)
  (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hclosed : γ a = γ b) (hγa : γ a ∉ ↑S)
  (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hf : DifferentiableOn ℂ f (Ω \ ↑S))
  (hmero : ∀ s ∈ S, s ∈ Ω → MeromorphicAt f s)
  (h_simple : ∀ s ∈ S, s ∈ Ω → ↑(-1) ≤ meromorphicOrderAt f s) :
  TauCeti.Contour.HasCauchyPV γ a b f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles)
- [Source of `TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles` in TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.lean#L167)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ContourIntegration/STATUS.md)
