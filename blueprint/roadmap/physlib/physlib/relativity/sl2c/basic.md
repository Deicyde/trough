---
declaration: module
origin: cited
lean: Lorentz.SL2C.inverse_coe, Lorentz.SL2C.transpose_coe, Lorentz.SL2C.toSelfAdjointMap, Lorentz.SL2C.toSelfAdjointMap_apply, Lorentz.SL2C.toSelfAdjointMap_apply_det, Lorentz.SL2C.toSelfAdjointMap_apply_pauliBasis'_inl, Lorentz.SL2C.toMatrix, Lorentz.SL2C.toMatrix_apply_contrMod
statement: formalized
proof: formalized
---

# The group SL(2, ℂ) and it's relation to the Lorentz group

The module `Physlib.Relativity.SL2C.Basic`, [Physlib/Relativity/SL2C/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean): 20 declarations, 10 with a docstring.

> The aim of this file is to give the relationship between `SL(2, ℂ)` and the Lorentz group.

## Some basic properties about SL(2, ℂ)

> Possibly to be moved to mathlib at some point.

**`Lorentz.SL2C.inverse_coe`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L37).

```lean
lemma inverse_coe (M : SL(2, ℂ)) : M.1⁻¹ = (M⁻¹).1
```

**`Lorentz.SL2C.transpose_coe`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L41).

```lean
lemma transpose_coe (M : SL(2, ℂ)) : M.1ᵀ = (M.transpose).1
```

## Representation of SL(2, ℂ) on spacetime

> Through the correspondence between spacetime and self-adjoint matrices,
> we can define a representation a representation of `SL(2, ℂ)` on spacetime.

**`Lorentz.SL2C.toSelfAdjointMap`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L54).

> Given an element `M ∈ SL(2, ℂ)` the linear map from `selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)` to
> itself defined by `A ↦ M * A * Mᴴ`.

```lean
noncomputable def toSelfAdjointMap (M : SL(2, ℂ)) :
    selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ) →ₗ[ℝ] selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)
```

**`Lorentz.SL2C.toSelfAdjointMap_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L69).

```lean
lemma toSelfAdjointMap_apply (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    toSelfAdjointMap M A = ⟨M.1 * A.1 * Matrix.conjTranspose M, by
        noncomm_ring [selfAdjoint.mem_iff, star_eq_conjTranspose,
        conjTranspose_mul, conjTranspose_conjTranspose,
        (star_eq_conjTranspose A.1).symm.trans $ selfAdjoint.mem_iff.mp A.2]⟩
```

**`Lorentz.SL2C.toSelfAdjointMap_apply_det`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L75).

```lean
lemma toSelfAdjointMap_apply_det (M : SL(2, ℂ)) (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    det ((toSelfAdjointMap M) A).1 = det A.1
```

**`Lorentz.SL2C.toSelfAdjointMap_apply_pauliBasis'_inl`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L79).

```lean
lemma toSelfAdjointMap_apply_pauliBasis'_inl (M : SL(2, ℂ)) :
    toSelfAdjointMap M (PauliMatrix.pauliBasis' (Sum.inl 0)) =
    ((‖M.1 0 0‖ ^ 2 + ‖M.1 0 1‖ ^ 2 + ‖M.1 1 0‖ ^ 2 + ‖M.1 1 1‖ ^ 2) / 2) •
      PauliMatrix.pauliBasis' (Sum.inl 0) +
    (- ((M.1 0 1).re * (M.1 1 1).re + (M.1 0 1).im * (M.1 1 1).im +
      (M.1 0 0).im * (M.1 1 0).im + (M.1 0 0).re * (M.1 1 0).re)) •
        PauliMatrix.pauliBasis' (Sum.inr 0)
    + ((- (M.1 0 0).re * (M.1 1 0).im + ↑(M.1 1 0).re * (M.1 0 0).im
      - (M.1 0 1).re * (M.1 1 1).im + (M.1 0 1).im * (M.1 1 1).re)) •
        PauliMatrix.pauliBasis' (Sum.inr 1)
    + ((- ‖M.1 0 0‖ ^ 2 - ‖M.1 0 1‖ ^ 2 + ‖M.1 1 0‖ ^ 2 + ‖M.1 1 1‖ ^ 2) / 2) •
      PauliMatrix.pauliBasis' (Sum.inr 2)
```

**`Lorentz.SL2C.toMatrix`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L125).

> The monoid homomorphisms from `SL(2, ℂ)` to matrices indexed by `Fin 1 ⊕ Fin 3`
> formed by the action `M A Mᴴ`.

```lean
def toMatrix : SL(2, ℂ) →* Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ
```

**`Lorentz.SL2C.toMatrix_apply_contrMod`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L142).

```lean
lemma toMatrix_apply_contrMod (M : SL(2, ℂ)) (v : ContrMod 3) :
    (toMatrix M) *ᵥ v = ContrMod.toSelfAdjoint.symm
    ((toSelfAdjointMap M) (ContrMod.toSelfAdjoint v))
```

**`Lorentz.SL2C.toMatrix_mem_lorentzGroup`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L159).

```lean
lemma toMatrix_mem_lorentzGroup (M : SL(2, ℂ)) : toMatrix M ∈ LorentzGroup 3
```

**`Lorentz.SL2C.toLorentzGroup`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L169).

> The group homomorphism from `SL(2, ℂ)` to the Lorentz group `𝓛`.

```lean
def toLorentzGroup : SL(2, ℂ) →* LorentzGroup 3
```

**`Lorentz.SL2C.toLorentzGroup_eq_pauliBasis'`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L178).

```lean
lemma toLorentzGroup_eq_pauliBasis' (M : SL(2, ℂ)) :
    toLorentzGroup M = LinearMap.toMatrix
    PauliMatrix.pauliBasis' PauliMatrix.pauliBasis' (toSelfAdjointMap M)
```

**`Lorentz.SL2C.toSelfAdjointMap_basis`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L183).

```lean
lemma toSelfAdjointMap_basis (i : Fin 1 ⊕ Fin 3) :
    toSelfAdjointMap M (PauliMatrix.pauliBasis' i) =
    ∑ j, (toLorentzGroup M).1 j i • PauliMatrix.pauliBasis' j
```

**`Lorentz.SL2C.toSelfAdjointMap_pauliBasis`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L192).

```lean
lemma toSelfAdjointMap_pauliBasis (i : Fin 1 ⊕ Fin 3) :
    toSelfAdjointMap M (PauliMatrix.pauliBasis i) =
    ∑ j, (toLorentzGroup M⁻¹).1 i j • PauliMatrix.pauliBasis j
```

**`Lorentz.SL2C.toLorentzGroup_eq_trace`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L209).

> The matrix elements of the covering map through the trace pairing:
> `L(M)_{i j} = ½ tr (σ'_i · M σ'_j M†)`.

```lean
lemma toLorentzGroup_eq_trace (M : SL(2,ℂ)) (i j : Fin 1 ⊕ Fin 3) :
    (((toLorentzGroup M).1 i j : ℝ) : ℂ) =
      Matrix.trace ((PauliMatrix.pauliSelfAdjoint' i).1 *
        (M.1 * (PauliMatrix.pauliSelfAdjoint' j).1 * M.1ᴴ)) / 2
```

**`Lorentz.SL2C.toLorentzGroup_fst_col`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L225).

> The first column of the Lorentz matrix formed from an element of `SL(2, ℂ)`.

```lean
lemma toLorentzGroup_fst_col (M : SL(2, ℂ)) :
    (fun μ => (toLorentzGroup M).1 μ (Sum.inl 0)) = fun μ =>
      match μ with
      | Sum.inl 0 => ((‖M.1 0 0‖ ^ 2 + ‖M.1 0 1‖ ^ 2 + ‖M.1 1 0‖ ^ 2 + ‖M.1 1 1‖ ^ 2) / 2)
      | Sum.inr 0 => (- ((M.1 0 1).re * (M.1 1 1).re + (M.1 0 1).im * (M.1 1 1).im +
        (M.1 0 0).im * (M.1 1 0).im + (M.1 0 0).re * (M.1 1 0).re))
      | Sum.inr 1 => ((- (M.1 0 0).re * (M.1 1 0).im + ↑(M.1 1 0).re * (M.1 0 0).im
        - (M.1 0 1).re * (M.1 1 1).im + (M.1 0 1).im * (M.1 1 1).re))
      | Sum.inr 2 => ((- ‖M.1 0 0‖ ^ 2 - ‖M.1 0 1‖ ^ 2 + ‖M.1 1 0‖ ^ 2 + ‖M.1 1 1‖ ^ 2) / 2)
```

**`Lorentz.SL2C.toLorentzGroup_inl_inl`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L260).

> The first element of the image of `SL(2, ℂ)` in the Lorentz group.

```lean
lemma toLorentzGroup_inl_inl (M : SL(2, ℂ)) :
    (toLorentzGroup M).1 (Sum.inl 0) (Sum.inl 0) =
    ((‖M.1 0 0‖ ^ 2 + ‖M.1 0 1‖ ^ 2 + ‖M.1 1 0‖ ^ 2 + ‖M.1 1 1‖ ^ 2) / 2)
```

**`Lorentz.SL2C.toLorentzGroup_isOrthochronous`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L266).

> The image of `SL(2, ℂ)` in the Lorentz group is orthochronous.

```lean
lemma toLorentzGroup_isOrthochronous (M : SL(2, ℂ)) :
    LorentzGroup.IsOrthochronous (toLorentzGroup M)
```

**`Lorentz.SL2C.toLorentzGroup_eq_one_iff`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L273).

> The kernel of the homomorphism from `SL(2, ℂ)` to the Lorentz group is `{1, -1}`.

```lean
lemma toLorentzGroup_eq_one_iff (M : SL(2, ℂ)) :
    toLorentzGroup M = 1 ↔ M.1 = 1 ∨ M.1 = -1
```

## Homomorphism to the restricted Lorentz group

> The homomorphism `toLorentzGroup` restricts to a homomorphism to the restricted Lorentz group.
> In this section we will define this homomorphism.

**`Lorentz.SL2C.toLorentzGroup_det_one`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L314).

> The determinant of the image of `SL(2, ℂ)` in the Lorentz group is one.

```lean
lemma toLorentzGroup_det_one (M : SL(2, ℂ)) : det (toLorentzGroup M).val = 1
```

**`Lorentz.SL2C.toRestrictedLorentzGroup`**, a def, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean#L338).

> The homomorphism from `SL(2, ℂ)` to the restricted Lorentz group.

```lean
def toRestrictedLorentzGroup : SL(2, ℂ) →* LorentzGroup.restricted 3
```

## Depends on

- [The Restricted Lorentz Group](../lorentzgroup/restricted-basic.md)

## Proof depends on

- [Schur triangulation](../../mathematics/formathlib/schurtriangulation.md)
- [Extra lemmas regarding `Lorentz.SL2C.toSelfAdjointMap`](selfadjoint.md)

## Sources

- [Physlib/Relativity/SL2C/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Basic.lean)
