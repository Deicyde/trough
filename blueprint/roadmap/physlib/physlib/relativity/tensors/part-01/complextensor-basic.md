---
declaration: module
origin: cited
lean: complexLorentzTensor.Color, complexLorentzTensor.repDim, complexLorentzTensor.basisIdx, complexLorentzTensor.basisIdxFintype, complexLorentzTensor.basisIdxDecidableEq, complexLorentzTensor.modules, complexLorentzTensor.modulesAddCommGroup, complexLorentzTensor.modulesModule
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Basic

The module `Physlib.Relativity.Tensors.ComplexTensor.Basic`, [Physlib/Relativity/Tensors/ComplexTensor/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean): 21 declarations (2 instances with no name), 15 with a docstring.

## Complex Lorentz tensors

**`complexLorentzTensor.Color`**, an inductive, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L27).

> The colors associated with complex representations of SL(2, ℂ) of interest to physics.

```lean
inductive Color
  /-- The color associated with Left handed fermions. -/
  | upL : Color
  /-- The color associated with dual-Left handed fermions. -/
  | downL : Color
  /-- The color associated with Right handed fermions. -/
  | upR : Color
  /-- The color associated with dual-Right handed fermions. -/
  | downR : Color
  /-- The color associated with contravariant Lorentz vectors. -/
  | up : Color
  /-- The color associated with covariant Lorentz vectors. -/
  | down : Color
```

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L43).

> Color for complex Lorentz tensors is decidable.

```lean
instance : DecidableEq Color
```

**`complexLorentzTensor.repDim`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L84).

> The dimensions of each of the different types of complex Lorentz vector space.

```lean
abbrev repDim (c : Color) : ℕ
```

**`complexLorentzTensor.basisIdx`**, an abbrev, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L95).

> The type indexing the standard basis of each complex Lorentz vector space: `Fin 2` for the
> Weyl colors and `Fin 1 ⊕ Fin 3` for the vector colors.

```lean
abbrev basisIdx : Color → Type
```

**`complexLorentzTensor.basisIdxFintype`**, an instance, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L103).

```lean
instance basisIdxFintype : ∀ c, Fintype (basisIdx c)
```

**`complexLorentzTensor.basisIdxDecidableEq`**, an instance, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L111).

```lean
instance basisIdxDecidableEq : ∀ c, DecidableEq (basisIdx c)
```

**`complexLorentzTensor.modules`**, an abbrev, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L120).

> The modules associated with each of the different types of complex Lorentz vector space.

```lean
abbrev modules : Color → Type
```

**`complexLorentzTensor.modulesAddCommGroup`**, an instance, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L128).

```lean
instance modulesAddCommGroup : ∀ c, AddCommGroup (modules c)
```

**`complexLorentzTensor.modulesModule`**, an instance, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L136).

```lean
noncomputable instance modulesModule : ∀ c, Module ℂ (modules c)
```

**`complexLorentzTensor`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L150).

> The tensor structure for complex Lorentz tensors.

```lean
def complexLorentzTensor : TensorSpecies ℂ complexLorentzTensor.Color SL(2, ℂ)
    (fun c => match c with
      | Color.upL => Fermion.LeftHandedWeyl
      | Color.downL => Fermion.DualLeftHandedWeyl
      | Color.upR => Fermion.RightHandedWeyl
      | Color.downR => Fermion.DualRightHandedWeyl
      | Color.up => Lorentz.ComplexVector
      | Color.down => Lorentz.ComplexCoVector)
    basisIdx
    (fun c => match c with
      | Color.upL => Fermion.LeftHandedWeyl.rep
      | Color.downL => Fermion.DualLeftHandedWeyl.rep
      | Color.upR => Fermion.RightHandedWeyl.rep
      | Color.downR => Fermion.DualRightHandedWeyl.rep
      | Color.up => Lorentz.ComplexVector.SL2CRep
      | Color.down => Lorentz.ComplexCoVector.SL2CRep)
    (fun c => match c with
    | Color.upL => Fermion.LeftHandedWeyl.basis
    | Color.downL => Fermion.DualLeftHandedWeyl.basis
    | Color.upR => Fermion.RightHandedWeyl.basis
    | Color.downR => Fermion.DualRightHandedWeyl.basis
    | Color.up => Lorentz.ComplexVector.basis
    | Color.down => Lorentz.ComplexCoVector.basis)
```

**`complexLorentzTensor.instWithMetric`**, an instance, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L235).

> The metrics of the complex Lorentz tensors: `ε` on the four Weyl colors and `η` on the two
> vector colors.

```lean
instance instWithMetric : complexLorentzTensor.WithMetric
```

**`complexLorentzTensor.basis`**, an abbrev, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L257).

> The basis associated with each of the different types of complex Lorentz vector space.

```lean
abbrev basis (c : Color) : Module.Basis (basisIdx c) ℂ (modules c)
```

**`complexLorentzTensor.rep`**, an abbrev, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L267).

> The reps associated with each of the different types of complex Lorentz vector space.

```lean
abbrev rep (c : Color) : Representation ℂ SL(2, ℂ) (modules c)
```

**`complexLorentzTensor.repDim_tau`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L287).

```lean
lemma repDim_tau {c : complexLorentzTensor.Color} :
    repDim (complexLorentzTensor.τ c) = repDim c
```

**`complexLorentzTensor.basisIdxTauEquiv`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L292).

> A color and its dual carry the same basis index type.

```lean
def basisIdxTauEquiv : (c : complexLorentzTensor.Color) →
    basisIdx (complexLorentzTensor.τ c) ≃ basisIdx c
```

**`complexLorentzTensor.isContrDualMatching_basisIdxTauEquiv`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L303).

> At every complex Lorentz color, the bases at the color and its dual are dual bases, with
> labels matched by the identity.

```lean
lemma isContrDualMatching_basisIdxTauEquiv (c : complexLorentzTensor.Color) :
    IsContrDualMatching complexLorentzTensor c (basisIdxTauEquiv c)
```

**An instance with no name**, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L316).

> Complex Lorentz tensors have dual bases under contraction, with the identity matching.

```lean
instance : HasContrDualBases complexLorentzTensor
```

**`complexLorentzTensor.contrDualIdxEquiv_eq_basisIdxTauEquiv`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L321).

> The dual-label matching of complex Lorentz tensors is the identity.

```lean
lemma contrDualIdxEquiv_eq_basisIdxTauEquiv (c : complexLorentzTensor.Color) :
    HasContrDualBases.contrDualIdxEquiv complexLorentzTensor c = basisIdxTauEquiv c
```

**`complexLorentzTensor.contrPCoeff_basis`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L326).

```lean
lemma contrPCoeff_basis {n : ℕ} {c : Fin n → complexLorentzTensor.Color} (i j : Fin n)
    (hij : i ≠ j ∧ (complexLorentzTensor.τ (c i) = c j))
    (b : ComponentIdx (S := complexLorentzTensor) c) :
    Pure.contrPCoeff i j hij (Pure.basisVector c b) =
      if b i = basisIdxTauEquiv (c i) (basisIdxCongr hij.2.symm (b j)) then 1 else 0
```

**`complexLorentzTensor.Color.bar`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L334).

> Complex conjugation of colours: it swaps handedness and fixes the vector colours.

```lean
def Color.bar : Color → Color
```

**`complexLorentzConjTensor`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean#L347).

> The complex Lorentz tensors as a conjugation species: conjugation swaps left- and
> right-handed Weyl colours and fixes the vector colours.

```lean
def complexLorentzConjTensor : ConjTensorSpecies ℂ Color SL(2, ℂ) modules
    basisIdx rep basis
```

## Depends on

- [Metrics of Weyl fermions](../../fermions/weyl/metric.md)
- [Metric for complex Lorentz vectors](complextensor-metrics-pre.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Basic.lean)
