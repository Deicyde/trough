---
declaration: module
origin: cited
lean: Lorentz.ContrMod, Lorentz.ContrMod.ext, Lorentz.ContrMod.toFin1dℝFun, Lorentz.ContrMod.toFin1dℝAddEquiv, Lorentz.ContrMod.val_add, Lorentz.ContrMod.val_smul, Lorentz.ContrMod.toFin1dℝEquiv, Lorentz.ContrMod.toFin1dℝ
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Modules

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Modules`, [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean): 56 declarations (5 instances with no name), 26 with a docstring.

## Modules associated with Real Lorentz vectors

> We define the modules underlying real Lorentz vectors.
>
> These definitions are preludes to the definitions of
> `Lorentz.contr` and `Lorentz.co`.

**`Lorentz.ContrMod`**, a structure, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L30).

> The module for contravariant (up-index) real Lorentz vectors.

```lean
structure ContrMod (d : ℕ) where
  /-- The underlying value as a vector `Fin 1 ⊕ Fin d → ℝ`. -/
  val : Fin 1 ⊕ Fin d → ℝ
```

**`Lorentz.ContrMod.ext`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L39).

```lean
lemma ext {ψ ψ' : ContrMod d} (h : ψ.val = ψ'.val) : ψ = ψ'
```

**`Lorentz.ContrMod.toFin1dℝFun`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L46).

> The equivalence between `ContrMod` and `Fin 1 ⊕ Fin d → ℝ`.

```lean
def toFin1dℝFun : ContrMod d ≃ (Fin 1 ⊕ Fin d → ℝ)
```

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L54).

> The instance of `AddCommGroup` on `ContrMod` defined via its equivalence
> with `Fin 1 ⊕ Fin d → ℝ`.

```lean
instance : AddCommGroup (ContrMod d)
```

**`Lorentz.ContrMod.toFin1dℝAddEquiv`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L57).

> The additive equivalence between `ContrMod` and `Fin 1 ⊕ Fin d → ℝ`.

```lean
def toFin1dℝAddEquiv : ContrMod d ≃+ (Fin 1 ⊕ Fin d → ℝ)
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L62).

> The instance of `Module` on `ContrMod` defined via its equivalence
> with `Fin 1 ⊕ Fin d → ℝ`.

```lean
instance : Module ℝ (ContrMod d)
```

**`Lorentz.ContrMod.val_add`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L65).

```lean
lemma val_add (ψ ψ' : ContrMod d) : (ψ + ψ').val = ψ.val + ψ'.val
```

**`Lorentz.ContrMod.val_smul`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L68).

```lean
lemma val_smul (r : ℝ) (ψ : ContrMod d) : (r • ψ).val = r • ψ.val
```

**`Lorentz.ContrMod.toFin1dℝEquiv`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L71).

> The linear equivalence between `ContrMod` and `(Fin 1 ⊕ Fin d → ℝ)`.

```lean
def toFin1dℝEquiv : ContrMod d ≃ₗ[ℝ] (Fin 1 ⊕ Fin d → ℝ)
```

**`Lorentz.ContrMod.toFin1dℝ`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L76).

> The underlying element of `Fin 1 ⊕ Fin d → ℝ` of a element in `ContrMod` defined
> through the linear equivalence `toFin1dℝEquiv`.

```lean
abbrev toFin1dℝ (ψ : ContrMod d)
```

**`Lorentz.ContrMod.toFin1dℝ_eq_val`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L78).

```lean
lemma toFin1dℝ_eq_val (ψ : ContrMod d) : ψ.toFin1dℝ = ψ.val
```

## The standard basis.

**`Lorentz.ContrMod.stdBasis`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L86).

> The standard basis of `ContrMod` indexed by `Fin 1 ⊕ Fin d`.

```lean
def stdBasis : Basis (Fin 1 ⊕ Fin d) ℝ (ContrMod d)
```

**`Lorentz.ContrMod.stdBasis_toFin1dℝEquiv_apply_same`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L89).

```lean
lemma stdBasis_toFin1dℝEquiv_apply_same (μ : Fin 1 ⊕ Fin d) :
    toFin1dℝEquiv (stdBasis μ) μ = 1
```

**`Lorentz.ContrMod.stdBasis_apply_same`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L97).

```lean
lemma stdBasis_apply_same (μ : Fin 1 ⊕ Fin d) : (stdBasis μ).val μ = 1
```

**`Lorentz.ContrMod.stdBasis_toFin1dℝEquiv_apply_ne`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L100).

```lean
lemma stdBasis_toFin1dℝEquiv_apply_ne {μ ν : Fin 1 ⊕ Fin d} (h : μ ≠ ν) :
    toFin1dℝEquiv (stdBasis μ) ν = 0
```

**`Lorentz.ContrMod.stdBasis_inl_apply_inr`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L108).

```lean
lemma stdBasis_inl_apply_inr (i : Fin d) : (stdBasis (Sum.inl 0)).val (Sum.inr i) = 0
```

**`Lorentz.ContrMod.stdBasis_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L112).

```lean
lemma stdBasis_apply (μ ν : Fin 1 ⊕ Fin d) : (stdBasis μ).val ν = if μ = ν then 1 else 0
```

**`Lorentz.ContrMod.stdBasis_decomp`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L120).

> Decomposition of a contravariant Lorentz vector into the standard basis.

```lean
lemma stdBasis_decomp (v : ContrMod d) : v = ∑ i, v.toFin1dℝ i • stdBasis i
```

## mulVec

**`Lorentz.ContrMod.mulVec`**, an abbrev, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L139).

> Multiplication of a matrix with a vector in `ContrMod`.

```lean
abbrev mulVec (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : ContrMod d) :
    ContrMod d
```

**`Lorentz.ContrMod.mulVec_toFin1dℝ`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L146).

```lean
lemma mulVec_toFin1dℝ (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : ContrMod d) :
    (M *ᵥ v).toFin1dℝ = M *ᵥ v.toFin1dℝ
```

**`Lorentz.ContrMod.mulVec_val`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L151).

```lean
lemma mulVec_val (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : ContrMod d) :
    (M *ᵥ v).val = M *ᵥ v.val
```

**`Lorentz.ContrMod.mulVec_sub`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L155).

```lean
lemma mulVec_sub (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v w : ContrMod d) :
    M *ᵥ (v - w) = M *ᵥ v - M *ᵥ w
```

**`Lorentz.ContrMod.sub_mulVec`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L159).

```lean
lemma sub_mulVec (M N : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : ContrMod d) :
    (M - N) *ᵥ v = M *ᵥ v - N *ᵥ v
```

**`Lorentz.ContrMod.mulVec_add`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L163).

```lean
lemma mulVec_add (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v w : ContrMod d) :
    M *ᵥ (v + w) = M *ᵥ v + M *ᵥ w
```

**`Lorentz.ContrMod.one_mulVec`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L168).

```lean
lemma one_mulVec (v : ContrMod d) : (1 : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) *ᵥ v = v
```

**`Lorentz.ContrMod.mulVec_mulVec`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L171).

```lean
lemma mulVec_mulVec (M N : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : ContrMod d) :
    M *ᵥ (N *ᵥ v) = (M * N) *ᵥ v
```

## The norm

> (Not the Minkowski norm, but the norm of a vector in `ContrMod d`.)

**`Lorentz.ContrMod.norm`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L185).

> A `NormedAddCommGroup` structure on `ContrMod`. This is not an instance, as we
> don't want it to be applied always.

```lean
def norm : NormedAddCommGroup (ContrMod d)
```

**`Lorentz.ContrMod.toSpace`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L195).

> The underlying space part of a `ContrMod` formed by removing the first element.
> A better name for this might be `tail`.

```lean
def toSpace (v : ContrMod d) : EuclideanSpace ℝ (Fin d)
```

## The representation.

**`Lorentz.ContrMod.rep`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L204).

> The representation of the Lorentz group acting on `ContrMod d`.

```lean
def rep : Representation ℝ (LorentzGroup d) (ContrMod d)
```

**`Lorentz.ContrMod.rep_apply_toFin1dℝ`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L210).

```lean
lemma rep_apply_toFin1dℝ (g : LorentzGroup d) (ψ : ContrMod d) :
    (rep g ψ).toFin1dℝ = g.1 *ᵥ ψ.toFin1dℝ
```

## To Self-Adjoint Matrix

**`Lorentz.ContrMod.toSelfAdjoint`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L221).

> The linear equivalence between the vector-space `ContrMod 3` and self-adjoint
> `2×2`-complex matrices.

```lean
def toSelfAdjoint : ContrMod 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)
```

**`Lorentz.ContrMod.toSelfAdjoint_apply`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L226).

```lean
lemma toSelfAdjoint_apply (x : ContrMod 3) : toSelfAdjoint x =
    x.toFin1dℝ (Sum.inl 0) • ⟨pauliMatrix (Sum.inl 0), pauliMatrix_selfAdjoint _⟩
    - x.toFin1dℝ (Sum.inr 0) • ⟨pauliMatrix (Sum.inr 0), pauliMatrix_selfAdjoint _⟩
    - x.toFin1dℝ (Sum.inr 1) • ⟨pauliMatrix (Sum.inr 1), pauliMatrix_selfAdjoint _⟩
    - x.toFin1dℝ (Sum.inr 2) • ⟨pauliMatrix (Sum.inr 2), pauliMatrix_selfAdjoint _⟩
```

**`Lorentz.ContrMod.toSelfAdjoint_apply_coe`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L243).

```lean
lemma toSelfAdjoint_apply_coe (x : ContrMod 3) : (toSelfAdjoint x).1 =
    x.toFin1dℝ (Sum.inl 0) • PauliMatrix.pauliMatrix (Sum.inl 0)
    - x.toFin1dℝ (Sum.inr 0) • PauliMatrix.pauliMatrix (Sum.inr 0)
    - x.toFin1dℝ (Sum.inr 1) • PauliMatrix.pauliMatrix (Sum.inr 1)
    - x.toFin1dℝ (Sum.inr 2) • PauliMatrix.pauliMatrix (Sum.inr 2)
```

**`Lorentz.ContrMod.toSelfAdjoint_stdBasis`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L251).

```lean
lemma toSelfAdjoint_stdBasis (i : Fin 1 ⊕ Fin 3) :
    toSelfAdjoint (stdBasis i) = PauliMatrix.pauliBasis' i
```

**`Lorentz.ContrMod.toSelfAdjoint_symm_basis`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L280).

```lean
lemma toSelfAdjoint_symm_basis (i : Fin 1 ⊕ Fin 3) :
    toSelfAdjoint.symm (PauliMatrix.pauliBasis' i) = (stdBasis i)
```

## Topology

**An instance with no name**, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L291).

> The type `ContrMod d` carries an instance of a topological group, induced by
> it's equivalence to `Fin 1 ⊕ Fin d → ℝ`.

```lean
instance : TopologicalSpace (ContrMod d)
```

**`Lorentz.ContrMod.toFin1dℝEquiv_isInducing`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L296).

```lean
lemma toFin1dℝEquiv_isInducing : IsInducing (@ContrMod.toFin1dℝEquiv d)
```

**`Lorentz.ContrMod.toFin1dℝEquiv_symm_isInducing`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L299).

```lean
lemma toFin1dℝEquiv_symm_isInducing : IsInducing ((@ContrMod.toFin1dℝEquiv d).symm)
```

**`Lorentz.CoMod`**, a structure, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L307).

> The module for covariant (up-index) complex Lorentz vectors.

```lean
structure CoMod (d : ℕ) where
  /-- The underlying value as a vector `Fin 1 ⊕ Fin d → ℝ`. -/
  val : Fin 1 ⊕ Fin d → ℝ
```

**`Lorentz.CoMod.ext`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L316).

```lean
lemma ext {ψ ψ' : CoMod d} (h : ψ.val = ψ'.val) : ψ = ψ'
```

**`Lorentz.CoMod.toFin1dℝFun`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L323).

> The equivalence between `CoℝModule` and `Fin 1 ⊕ Fin d → ℝ`.

```lean
def toFin1dℝFun : CoMod d ≃ (Fin 1 ⊕ Fin d → ℝ)
```

**An instance with no name**, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L331).

> The instance of `AddCommGroup` on `CoℝModule` defined via its equivalence
> with `Fin 1 ⊕ Fin d → ℝ`.

```lean
instance : AddCommGroup (CoMod d)
```

**`Lorentz.CoMod.toFin1dℝAddEquiv`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L334).

> The additive equivalence between `CoℝModule` and `Fin 1 ⊕ Fin d → ℝ`.

```lean
def toFin1dℝAddEquiv : CoMod d ≃+ (Fin 1 ⊕ Fin d → ℝ)
```

**An instance with no name**, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L339).

> The instance of `Module` on `CoℝModule` defined via its equivalence
> with `Fin 1 ⊕ Fin d → ℝ`.

```lean
instance : Module ℝ (CoMod d)
```

**`Lorentz.CoMod.toFin1dℝEquiv`**, a def, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L342).

> The linear equivalence between `CoℝModule` and `(Fin 1 ⊕ Fin d → ℝ)`.

```lean
def toFin1dℝEquiv : CoMod d ≃ₗ[ℝ] (Fin 1 ⊕ Fin d → ℝ)
```

**`Lorentz.CoMod.toFin1dℝ`**, an abbrev, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L347).

> The underlying element of `Fin 1 ⊕ Fin d → ℝ` of a element in `CoℝModule` defined
> through the linear equivalence `toFin1dℝEquiv`.

```lean
abbrev toFin1dℝ (ψ : CoMod d)
```

## The standard basis.

**`Lorentz.CoMod.stdBasis`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L356).

> The standard basis of `CoℝModule` indexed by `Fin 1 ⊕ Fin d`.

```lean
def stdBasis : Basis (Fin 1 ⊕ Fin d) ℝ (CoMod d)
```

**`Lorentz.CoMod.stdBasis_toFin1dℝEquiv_apply_same`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L359).

```lean
lemma stdBasis_toFin1dℝEquiv_apply_same (μ : Fin 1 ⊕ Fin d) :
    toFin1dℝEquiv (stdBasis μ) μ = 1
```

**`Lorentz.CoMod.stdBasis_apply_same`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L367).

```lean
lemma stdBasis_apply_same (μ : Fin 1 ⊕ Fin d) : (stdBasis μ).val μ = 1
```

**`Lorentz.CoMod.stdBasis_toFin1dℝEquiv_apply_ne`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L370).

```lean
lemma stdBasis_toFin1dℝEquiv_apply_ne {μ ν : Fin 1 ⊕ Fin d} (h : μ ≠ ν) :
    toFin1dℝEquiv (stdBasis μ) ν = 0
```

**`Lorentz.CoMod.stdBasis_apply`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L377).

```lean
lemma stdBasis_apply (μ ν : Fin 1 ⊕ Fin d) : (stdBasis μ).val ν = if μ = ν then 1 else 0
```

**`Lorentz.CoMod.stdBasis_decomp`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L385).

> Decomposition of a covariant Lorentz vector into the standard basis.

```lean
lemma stdBasis_decomp (v : CoMod d) : v = ∑ i, v.toFin1dℝ i • stdBasis i
```

## mulVec

**`Lorentz.CoMod.mulVec`**, an abbrev, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L404).

> Multiplication of a matrix with a vector in `CoMod`.

```lean
abbrev mulVec (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : CoMod d) :
    CoMod d
```

**`Lorentz.CoMod.mulVec_toFin1dℝ`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L411).

```lean
lemma mulVec_toFin1dℝ (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : CoMod d) :
    (M *ᵥ v).toFin1dℝ = M *ᵥ v.toFin1dℝ
```

**`Lorentz.CoMod.mulVec_val`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L416).

```lean
lemma mulVec_val (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) (v : CoMod d) :
    (M *ᵥ v).val = M *ᵥ v.val
```

## The representation

**`Lorentz.CoMod.rep`**, a def, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean#L426).

> The representation of the Lorentz group acting on `CoℝModule d`.

```lean
def rep : Representation ℝ (LorentzGroup d) (CoMod d)
```

## Depends on

- [The Lorentz Group](../../lorentzgroup/basic.md)
- [Physlib.Relativity.PauliMatrices.SelfAdjoint](../../paulimatrices/selfadjoint.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Modules.lean)
