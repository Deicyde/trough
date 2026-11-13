---
declaration: module
origin: cited
lean: WaveVectorSpace, WaveVectorSpace.eq_of_val, WaveVectorSpace.val_eq_iff, WaveVectorSpace.eq_of_apply, WaveVectorSpace.zero_val, WaveVectorSpace.add_val, WaveVectorSpace.sub_val, WaveVectorSpace.neg_val
statement: formalized
proof: formalized
---

# Wave Vector Space

The module `Physlib.SpaceAndTime.WaveVectorSpace.Basic`, [Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean): 42 declarations (11 instances with no name), 5 with a docstring.

## i. Overview

> In this module we define the type `WaveVectorSpace d` corresponding to the `d`-dimensional
> space of (angular) wave vectors in `Space d`.
>
> In contrast to `Space d`, `WaveVectorSpace d` has a distinguished zero;
> the purpose of this file is to define this zero, the structure of a `Module`
> on `WaveVectorSpace d`, and the structure of a real `InnerProductSpace` on `WaveVectorSpace d`,
> none of which requires any non-canonical choices.
>
> `WaveVectorSpace d` is implemented as a structure with a field `val : Fin d → ℝ`
> rather than as an `abbrev` of `EuclideanSpace ℝ (Fin d)` or a `def` of a type with value
> `EuclideanSpace ℝ (Fin d)` for the same reasons as for `Space d`;
> see `Physlib.SpaceAndTime.Space.Basic` for a discussion of the (dis)advantages of each.

## ii. Key results

> - `WaveVectorSpace d` : the space of wave vectors in `Space d`
> - `instModuleReal` : `WaveVectorSpace d` is a module over `ℝ`
> - `instInnerProductSpaceReal` : `WaveVectorSpace d` is a real inner product space
> - `equivEuclideanSpace` : the linear isometric equivalence between `WaveVectorSpace d` and `ℝᵈ`

## iv. References

## A. The `WaveVectorSpace` type

**`WaveVectorSpace`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L65).

> The type `WaveVectorSpace d` is the real vector space which corresponds to `d`-dimensional
> (angular) wave vectors in `Space d` with a given (but arbitrary) choice of inverse length unit.
>
> The default value of `d` is `3`. Thus `WaveVectorSpace = WaveVectorSpace 3`

```lean
structure WaveVectorSpace (d : ℕ := 3) where
  /-- The underlying map `Fin d → ℝ` associated with a vector in `WaveVectorSpace`. -/
  val : Fin d → ℝ
```

**`WaveVectorSpace.eq_of_val`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L73).

```lean
lemma eq_of_val {k₁ k₂ : WaveVectorSpace d} (h : k₁.val = k₂.val) : k₁ = k₂
```

**`WaveVectorSpace.val_eq_iff`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L78).

```lean
lemma val_eq_iff {k₁ k₂ : WaveVectorSpace d} : k₁.val = k₂.val ↔ k₁ = k₂
```

## B. Instances on `WaveVectorSpace`

### B.1. Coercion to functions

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L89).

```lean
instance : CoeFun (WaveVectorSpace d) (fun _ ↦ Fin d → ℝ)
```

**`WaveVectorSpace.eq_of_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L93).

```lean
lemma eq_of_apply {k₁ k₂ : WaveVectorSpace d} (h : ∀ i, k₁ i = k₂ i) : k₁ = k₂
```

### B.2. Subsingleton for `d = 0`

**An instance with no name**, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L102).

```lean
instance : Subsingleton (WaveVectorSpace 0)
```

### B.3. Zero

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L109).

```lean
instance : Zero (WaveVectorSpace d)
```

**`WaveVectorSpace.zero_val`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L113).

```lean
lemma zero_val : (0 : WaveVectorSpace d).val = 0
```

### B.4. Additive commutative group

**An instance with no name**, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L123).

```lean
instance : Add (WaveVectorSpace d)
```

**`WaveVectorSpace.add_val`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L127).

```lean
lemma add_val : (k₁ + k₂).val = k₁.val + k₂.val
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L129).

```lean
instance : Sub (WaveVectorSpace d)
```

**`WaveVectorSpace.sub_val`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L133).

```lean
lemma sub_val : (k₁ - k₂).val = k₁.val - k₂.val
```

**An instance with no name**, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L135).

```lean
instance : Neg (WaveVectorSpace d)
```

**`WaveVectorSpace.neg_val`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L139).

```lean
lemma neg_val : (-k).val = -k.val
```

**An instance with no name**, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L141).

```lean
instance : AddCommGroup (WaveVectorSpace d)
```

### B.5. Module over `ℝ`

**An instance with no name**, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L156).

```lean
instance : SMul ℝ (WaveVectorSpace d)
```

**`WaveVectorSpace.smul_val`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L160).

```lean
lemma smul_val (c : ℝ) (k : WaveVectorSpace d) : (c • k).val = c • k.val
```

**`WaveVectorSpace.instModuleReal`**, an instance, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L162).

```lean
instance instModuleReal : Module ℝ (WaveVectorSpace d)
```

### B.6. Inner product space

**An instance with no name**, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L178).

```lean
instance : Inner ℝ (WaveVectorSpace d)
```

**`WaveVectorSpace.inner_apply`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L181).

```lean
lemma inner_apply (k₁ k₂ : WaveVectorSpace d) : ⟪k₁, k₂⟫ = ∑ i, k₁ i * k₂ i
```

**An instance with no name**, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L183).

```lean
instance : InnerProductSpace.Core ℝ (WaveVectorSpace d)
```

**`WaveVectorSpace.instNormedAddCommGroup`**, an instance, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L193).

```lean
noncomputable instance instNormedAddCommGroup : NormedAddCommGroup (WaveVectorSpace d)
```

**`WaveVectorSpace.instInnerProductSpaceReal`**, an instance, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L196).

```lean
noncomputable instance instInnerProductSpaceReal : InnerProductSpace ℝ (WaveVectorSpace d)
```

**`WaveVectorSpace.norm_eq`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L199).

```lean
lemma norm_eq (k : WaveVectorSpace d) : ‖k‖ = √(∑ i, k i ^ 2)
```

**`WaveVectorSpace.norm_sq_eq`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L202).

```lean
lemma norm_sq_eq (k : WaveVectorSpace d) : ‖k‖ ^ 2 = ∑ i, k i ^ 2
```

## C. Linear isometric equivalence with `ℝᵈ`

**`WaveVectorSpace.equivEuclideanSpace`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L212).

> The linear isometric equivalence between `WaveVectorSpace d` and `ℝᵈ`.

```lean
def equivEuclideanSpace : WaveVectorSpace d ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin d)
```

**`WaveVectorSpace.equivEuclideanSpace_apply`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L220).

```lean
lemma equivEuclideanSpace_apply (k : WaveVectorSpace d) (i : Fin d) :
    equivEuclideanSpace k i = k i
```

**`WaveVectorSpace.equivEuclideanSpace_symm_apply`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L225).

```lean
lemma equivEuclideanSpace_symm_apply (v : EuclideanSpace ℝ (Fin d)) (i : Fin d) :
    equivEuclideanSpace.symm v i = v i
```

**`WaveVectorSpace.finrank_waveVectorSpace`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L230).

```lean
lemma finrank_waveVectorSpace : Module.finrank ℝ (WaveVectorSpace d) = d
```

### C.1. Standard basis

**`WaveVectorSpace.basis`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L242).

> The standard basis of `WaveVectorSpace d`.

```lean
def basis : OrthonormalBasis (Fin d) ℝ (WaveVectorSpace d)
```

**`WaveVectorSpace.basis_repr_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L246).

```lean
lemma basis_repr_apply : basis.repr k i = k i
```

**`WaveVectorSpace.basis_repr_symm_apply`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L249).

```lean
lemma basis_repr_symm_apply : basis.repr.symm v i = v i
```

**`WaveVectorSpace.basis_apply`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L252).

```lean
lemma basis_apply : basis i j = δ[i,j]
```

**`WaveVectorSpace.inner_basis`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L255).

```lean
lemma inner_basis : inner ℝ k (basis i) = k i
```

**`WaveVectorSpace.basis_inner`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L259).

```lean
lemma basis_inner : inner ℝ (basis i) k = k i
```

**An instance with no name**, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L262).

```lean
instance : FiniteDimensional ℝ (WaveVectorSpace d)
```

### C.2. Coordinate functions

**`WaveVectorSpace.coord`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L277).

> The standard coordinate functions of `WaveVectorSpace` based on `Fin d`.

```lean
def coord : ℝ
```

**`WaveVectorSpace.coord_apply`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L279).

```lean
lemma coord_apply : k.coord i = k i
```

**`WaveVectorSpace.coordCLM`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L283).

> The standard coordinate functions of `WaveVectorSpace` based on `Fin d`,
> as a continuous linear map.

```lean
def coordCLM : WaveVectorSpace d →L[ℝ] ℝ
```

**`WaveVectorSpace.coordCLM_apply`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L291).

```lean
lemma coordCLM_apply : coordCLM i k = k.coord i
```

**`WaveVectorSpace.coord_contDiff`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L294).

```lean
lemma coord_contDiff : ContDiff ℝ n (coord i)
```

**`WaveVectorSpace.val_contDiff`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean#L297).

```lean
lemma val_contDiff : ContDiff ℝ n (val · i)
```

## Depends on

- [Kronecker delta](../../mathematics/kroneckerdelta/basic.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/Basic.lean)
