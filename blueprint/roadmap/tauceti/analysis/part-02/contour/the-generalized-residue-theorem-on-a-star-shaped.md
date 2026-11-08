---
declaration: theorem
origin: cited
lean: TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex, TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles, TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex, TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles
statement: formalized
proof: formalized
---

# The generalized residue theorem on a star-shaped open set, simple-pole regime

Let `Ω` be
open and star-shaped about `x`, `S ⊆ Ω` finite, `f` holomorphic on `Ω ∖ S` with at worst a simple
pole at each point of `S`, and `γ` a closed piecewise-`C¹` immersion in `Ω` based off `S`. Then the
Cauchy principal value of the contour integral is

`p.v. ∮_γ f = 2πi · ∑_{s ∈ S} n_s(γ) · Res_s f`,

with the generalized, possibly non-integer, winding numbers as weights. The curve is free to pass
**through** the singularities; conditions (A′) and (B) of Hungerbühler–Wasem are automatic in this
regime, while null-homology is automatic by star-shapedness. Thus null-homology and conditions (A′)
and (B) require no additional hypotheses in this regime.

```lean
TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex {f : ℂ → ℂ} {Ω : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} {x : ℂ} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω)
  (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hSΩ : ↑S ⊆ Ω) (hclosed : γ a = γ b)
  (hγa : γ a ∉ ↑S) (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hf : DifferentiableOn ℂ f (Ω \ ↑S))
  (hmero : ∀ s ∈ S, MeromorphicAt f s) (h_simple : ∀ s ∈ S, ↑(-1) ≤ meromorphicOrderAt f s) :
  TauCeti.Contour.HasCauchyPV γ a b f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Proof depends on

- [Hungerbühler--Wasem Proposition 2.2 (winding decomposition)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/hungerbuhler-wasem-proposition-2-2-winding-decom.md)
- [The Hungerbühler–Wasem generalized residue theorem for a contour cycle (HW Thm 3.3)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-hungerbuhler-wasem-generalized-residue-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex).

## Other forms

**The generalized residue theorem for a contour cycle with simple poles — HW Thm 3.3's unconditional regime for cycles.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles).

```lean
TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles {f : ℂ → ℂ} {U : Set ℂ}
  {C : TauCeti.Contour.Cycle} (hU : IsOpen U) (S : Finset ℂ) (hSU : ↑S ⊆ U)
  (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, MeromorphicAt f s) (hCU : C.IsIn U)
  (h_imm :
    ∀ γ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.IsPwC1ImmersionOn (Function.extend Subtype.val γ.toFun 0) γ.a γ.b)
  (hbase : ∀ γ ∈ FreeAbelianGroup.support C, Function.extend Subtype.val γ.toFun 0 γ.a ∉ ↑S)
  (hnull : C.IsNullHomologous U) (h_simple : ∀ s ∈ S, ↑(-1) ≤ meromorphicOrderAt f s) :
  C.HasCauchyPV f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s)
```

**The generalized residue theorem for a cycle in a star-shaped open set, simple-pole regime.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex).

```lean
TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex {f : ℂ → ℂ}
  {Ω : Set ℂ} {x : ℂ} {C : TauCeti.Contour.Cycle} {S : Finset ℂ} (hstar : StarConvex ℝ x Ω)
  (hopen : IsOpen Ω) (hSΩ : ↑S ⊆ Ω) (hf : DifferentiableOn ℂ f (Ω \ ↑S))
  (hmero : ∀ s ∈ S, MeromorphicAt f s) (hCΩ : C.IsIn Ω)
  (h_imm :
    ∀ δ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.IsPwC1ImmersionOn (Function.extend Subtype.val δ.toFun 0) δ.a δ.b)
  (hbase : ∀ δ ∈ FreeAbelianGroup.support C, Function.extend Subtype.val δ.toFun 0 δ.a ∉ ↑S)
  (h_simple : ∀ s ∈ S, ↑(-1) ≤ meromorphicOrderAt f s) :
  C.HasCauchyPV f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s)
```

**The generalized residue theorem for simple poles — HW Thm 3.3's unconditional regime.** Formalized in Tau Ceti as [`TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles).

```lean
TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles {f : ℂ → ℂ} {U : Set ℂ}
  (hU : IsOpen U) (S : Finset ℂ) (γ : ℝ → ℂ) (a b : ℝ)
  (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hSU : ↑S ⊆ U) (hclosed : γ a = γ b)
  (hγa : γ a ∉ ↑S) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hf : DifferentiableOn ℂ f (U \ ↑S))
  (hmero : ∀ s ∈ S, MeromorphicAt f s) (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (h_simple : ∀ s ∈ S, ↑(-1) ≤ meromorphicOrderAt f s) :
  TauCeti.Contour.HasCauchyPV γ a b f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex)
- [Source of `TauCeti.Contour.hungerbuhlerWasem_residueTheorem_of_simple_poles_starConvex` in TauCeti/Analysis/Contour/StarConvex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/StarConvex.lean#L221)
