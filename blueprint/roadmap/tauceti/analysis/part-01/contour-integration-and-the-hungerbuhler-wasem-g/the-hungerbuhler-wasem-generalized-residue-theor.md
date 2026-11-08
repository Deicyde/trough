---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem, TauCeti.Contour.hungerbuhlerWasem_residueTheorem
statement: formalized
proof: formalized
---

# The Hungerbühler–Wasem generalized residue theorem for a contour cycle (HW Thm 3.3)

Let `U` be open, `S ⊆ U` finite, `f` holomorphic on `U ∖ S` and meromorphic at each point of
`S`, and let `C` be a contour cycle in `U`, **null-homologous** in `U`, whose curves are
piecewise-`C¹` immersions rooted off `S` and satisfy conditions (A′) and (B). Then the Cauchy
principal value of `f` along `C` exists and

`PV ∮_C f = 2πi · ∑_{s ∈ S} n_s(C) · Res_s f`,

each singularity weighted by the **generalized** winding number of `C` about it. The
singularities are allowed to lie **on** `C`, where those weights are in general not integers and
the contour integral only exists as a principal value.

Null-homology is asked of the cycle only, never of its generators, so the theorem covers the
combinations that make cycles worth having: a difference of two homologous loops around a hole of
`U`, neither of them null-homologous, is null-homologous. Its `S = ∅` case is the homology Cauchy
theorem for cycles
(`TauCeti.Contour.Cycle.homologyCauchyTheorem`), and its one-generator case is the single-curve
theorem `TauCeti.Contour.hungerbuhlerWasem_residueTheorem`. Where the trace of `C` avoids `S`
the principal value is an ordinary integral and the statement is the classical residue theorem
for cycles (`TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous`), which needs neither
immersions nor the conditions.

```lean
TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem {f : ℂ → ℂ} {U : Set ℂ}
  {C : TauCeti.Contour.Cycle} (hU : IsOpen U) (S : Finset ℂ) (hSU : ↑S ⊆ U)
  (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, MeromorphicAt f s) (hCU : C.IsIn U)
  (h_imm :
    ∀ γ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.IsPwC1ImmersionOn (Function.extend Subtype.val γ.toFun 0) γ.a γ.b)
  (hbase : ∀ γ ∈ FreeAbelianGroup.support C, Function.extend Subtype.val γ.toFun 0 γ.a ∉ ↑S)
  (hnull : C.IsNullHomologous U)
  (hA :
    ∀ γ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.ConditionAprime (Function.extend Subtype.val γ.toFun 0) γ.a γ.b f S)
  (hB :
    ∀ γ ∈ FreeAbelianGroup.support C,
      TauCeti.Contour.ConditionB (Function.extend Subtype.val γ.toFun 0) γ.a γ.b f) :
  C.HasCauchyPV f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Proof depends on

- [The canonical Laurent decomposition](../../part-02/contour/the-canonical-laurent-decomposition.md)
- [First exit time at radius `ε` (left side)](first-exit-time-at-radius-left-side.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](the-homology-cauchy-theorem-roadmap-homologycauc.md)
- [The homology Cauchy theorem for contour cycles](../banach-algebras/the-homology-cauchy-theorem-for-contour-cycles.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem).

## Other forms

**The Hungerbühler–Wasem generalized residue theorem (HW Thm 3.3).** Formalized in Tau Ceti as [`TauCeti.Contour.hungerbuhlerWasem_residueTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hungerbuhlerWasem_residueTheorem).

```lean
TauCeti.Contour.hungerbuhlerWasem_residueTheorem {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
  (S : Finset ℂ) (γ : ℝ → ℂ) (a b : ℝ) (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b)
  (hSU : ↑S ⊆ U) (hclosed : γ a = γ b) (hγa : γ a ∉ ↑S) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, MeromorphicAt f s)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (hA : TauCeti.Contour.ConditionAprime γ a b f S) (hB : TauCeti.Contour.ConditionB γ a b f) :
  TauCeti.Contour.HasCauchyPV γ a b f
    (2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.html#TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem)
- [Source of `TauCeti.Contour.Cycle.hungerbuhlerWasem_residueTheorem` in TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cycle/HungerbuhlerWasem.lean#L115)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
