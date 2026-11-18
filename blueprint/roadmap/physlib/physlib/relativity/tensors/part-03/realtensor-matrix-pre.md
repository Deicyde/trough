---
declaration: module
origin: cited
lean: Lorentz.contrContrToMatrixRe, Lorentz.contrContrToMatrixRe_symm_expand_tmul, Lorentz.coCoToMatrixRe, Lorentz.coCoToMatrixRe_symm_expand_tmul, Lorentz.contrCoToMatrixRe, Lorentz.contrCoToMatrixRe_symm_expand_tmul, Lorentz.coContrToMatrixRe, Lorentz.coContrToMatrixRe_symm_expand_tmul
statement: formalized
proof: formalized
---

# Tensor products of two real Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Matrix.Pre`, [Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean): 16 declarations, 8 with a docstring.

**`Lorentz.contrContrToMatrixRe`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L24).

> Equivalence of `ContrMod ⊗ ContrMod` to `(1 + d) x (1 + d)` real matrices.

```lean
def contrContrToMatrixRe {d : ℕ} : (ContrMod d ⊗[ℝ] ContrMod d) ≃ₗ[ℝ]
    Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

**`Lorentz.contrContrToMatrixRe_symm_expand_tmul`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L32).

> Expanding `contrContrToMatrixRe` in terms of the standard basis.

```lean
lemma contrContrToMatrixRe_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) :
    contrContrToMatrixRe.symm M = ∑ i, ∑ j, M i j • (contrBasis d i ⊗ₜ[ℝ] contrBasis d j)
```

**`Lorentz.coCoToMatrixRe`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L44).

> Equivalence of `CoMod ⊗ CoMod` to `(1 + d) x (1 + d)` real matrices.

```lean
def coCoToMatrixRe {d : ℕ} : (CoMod d ⊗[ℝ] CoMod d) ≃ₗ[ℝ]
    Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

**`Lorentz.coCoToMatrixRe_symm_expand_tmul`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L52).

> Expanding `coCoToMatrixRe` in terms of the standard basis.

```lean
lemma coCoToMatrixRe_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) :
    coCoToMatrixRe.symm M = ∑ i, ∑ j, M i j • (coBasis d i ⊗ₜ[ℝ] coBasis d j)
```

**`Lorentz.contrCoToMatrixRe`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L63).

> Equivalence of `ContrMod d ⊗ CoMod d` to `(1 + d) x (1 + d)` real matrices.

```lean
def contrCoToMatrixRe {d : ℕ} : (ContrMod d ⊗[ℝ] CoMod d) ≃ₗ[ℝ]
    Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

**`Lorentz.contrCoToMatrixRe_symm_expand_tmul`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L71).

> Expansion of ` (coBasis d) (coBasis d)` in terms of the standard basis.

```lean
lemma contrCoToMatrixRe_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) :
    contrCoToMatrixRe.symm M = ∑ i, ∑ j, M i j • (contrBasis d i ⊗ₜ[ℝ] coBasis d j)
```

**`Lorentz.coContrToMatrixRe`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L83).

> Equivalence of `CoMod d ⊗ ContrMod d` to `(1 + d) x (1 + d)` real matrices.

```lean
def coContrToMatrixRe : (CoMod d ⊗[ℝ] ContrMod d) ≃ₗ[ℝ]
    Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

**`Lorentz.coContrToMatrixRe_symm_expand_tmul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L91).

> Expansion of `coContrToMatrixRe` in terms of the standard basis.

```lean
lemma coContrToMatrixRe_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) :
    coContrToMatrixRe.symm M = ∑ i, ∑ j, M i j • (coBasis d i ⊗ₜ[ℝ] contrBasis d j)
```

## Group actions

**`Lorentz.contrContrToMatrixRe_ρ`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L109).

```lean
lemma contrContrToMatrixRe_ρ {d : ℕ} (v : (ContrMod d ⊗[ℝ] ContrMod d)) (M : LorentzGroup d) :
    contrContrToMatrixRe (TensorProduct.map (ContrMod.rep M) (ContrMod.rep M) v) =
    M.1 * contrContrToMatrixRe v * Mᵀ
```

**`Lorentz.coCoToMatrixRe_ρ`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L144).

```lean
lemma coCoToMatrixRe_ρ {d : ℕ} (v : (CoMod d ⊗[ℝ] CoMod d)) (M : LorentzGroup d) :
    coCoToMatrixRe (TensorProduct.map (CoMod.rep M) (CoMod.rep M) v) =
    M.1⁻¹ᵀ * coCoToMatrixRe v * M⁻¹
```

**`Lorentz.contrCoToMatrixRe_ρ`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L179).

```lean
lemma contrCoToMatrixRe_ρ {d : ℕ} (v : (ContrMod d ⊗[ℝ] CoMod d)) (M : LorentzGroup d) :
    contrCoToMatrixRe (TensorProduct.map (ContrMod.rep M) (CoMod.rep M) v) =
    M.1 * contrCoToMatrixRe v * M.1⁻¹
```

**`Lorentz.coContrToMatrixRe_ρ`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L214).

```lean
lemma coContrToMatrixRe_ρ {d : ℕ} (v : (CoMod d ⊗[ℝ] ContrMod d)) (M : LorentzGroup d) :
    coContrToMatrixRe (TensorProduct.map (CoMod.rep M) (ContrMod.rep M) v) =
    M.1⁻¹ᵀ * coContrToMatrixRe v * M.1ᵀ
```

## The symm version of the group actions.

**`Lorentz.contrContrToMatrixRe_ρ_symm`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L254).

```lean
lemma contrContrToMatrixRe_ρ_symm {d : ℕ} (v : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
    (M : LorentzGroup d) :
    TensorProduct.map (ContrMod.rep M) (ContrMod.rep M) (contrContrToMatrixRe.symm v) =
    contrContrToMatrixRe.symm (M.1 * v * M.1ᵀ)
```

**`Lorentz.coCoToMatrixRe_ρ_symm`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L261).

```lean
lemma coCoToMatrixRe_ρ_symm {d : ℕ} (v : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
    (M : LorentzGroup d) :
    TensorProduct.map (CoMod.rep M) (CoMod.rep M) (coCoToMatrixRe.symm v) =
    coCoToMatrixRe.symm (M.1⁻¹ᵀ * v * M.1⁻¹)
```

**`Lorentz.contrCoToMatrixRe_ρ_symm`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L271).

```lean
lemma contrCoToMatrixRe_ρ_symm {d : ℕ} (v : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
    (M : LorentzGroup d) :
    TensorProduct.map (ContrMod.rep M) (CoMod.rep M) (contrCoToMatrixRe.symm v) =
    contrCoToMatrixRe.symm (M.1 * v * M.1⁻¹)
```

**`Lorentz.coContrToMatrixRe_ρ_symm`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean#L279).

```lean
lemma coContrToMatrixRe_ρ_symm {d : ℕ} (v : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
    (M : LorentzGroup d) :
    TensorProduct.map (CoMod.rep M) (ContrMod.rep M) (coContrToMatrixRe.symm v) =
    coContrToMatrixRe.symm (M.1⁻¹ᵀ * v * M.1ᵀ)
```

## Depends on

- [Real Lorentz vectors](../part-04/realtensor-vector-pre-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Matrix/Pre.lean)
