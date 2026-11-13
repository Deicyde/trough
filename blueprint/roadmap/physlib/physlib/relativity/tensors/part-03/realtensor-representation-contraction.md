---
declaration: module
origin: cited
lean: Lorentz.Vector.contract, Lorentz.CoVector.contract, Lorentz.Vector.contract_tmul, Lorentz.CoVector.contract_tmul, Lorentz.Vector.contract_basis_left, Lorentz.CoVector.contract_basis_left, Lorentz.Vector.contract_basis_right, Lorentz.CoVector.contract_basis_right
statement: formalized
proof: formalized
---

# Contraction of Real Lorentz Vectors and Covectors

The module `Physlib.Relativity.Tensors.RealTensor.Representation.Contraction`, [Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean): 11 declarations, 2 with a docstring.

> We define the intertwining maps which define the contraction of a contravariant Lorentz vector with
> a covariant Lorentz vector, and vice versa.
>
> Note: This file will eventually replace `./Pre/Contraction.lean` when we move
>   `realLorentzTensor` over to `Vector` and `CoVector`.

## A. The definitions

**`Lorentz.Vector.contract`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L45).

> The intertwining map defining the contraction of a contravariant Lorentz vector with a
> covariant Lorentz vector.

```lean
def Vector.contract : (Vector.rep.tprod CoVector.rep).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

**`Lorentz.CoVector.contract`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L65).

> The intertwining map defining the contraction of a covariant Lorentz vector with a
> contravariant Lorentz vector.

```lean
def CoVector.contract : (CoVector.rep.tprod Vector.rep).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

## B. Properties of the contractions

**`Lorentz.Vector.contract_tmul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L89).

```lean
lemma Vector.contract_tmul (φ : Vector d) (ψ : CoVector d) :
    Vector.contract (φ ⊗ₜ ψ) = ∑ i, φ i * ψ i
```

**`Lorentz.CoVector.contract_tmul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L92).

```lean
lemma CoVector.contract_tmul (φ : CoVector d) (ψ : Vector d) :
    CoVector.contract (φ ⊗ₜ ψ) = ∑ i, φ i * ψ i
```

**`Lorentz.Vector.contract_basis_left`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L95).

```lean
lemma Vector.contract_basis_left (μ : Fin 1 ⊕ Fin d) (ψ : CoVector d) :
    Vector.contract (basis μ ⊗ₜ ψ) = ψ μ
```

**`Lorentz.CoVector.contract_basis_left`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L98).

```lean
lemma CoVector.contract_basis_left (μ : Fin 1 ⊕ Fin d) (φ : Vector d) :
    CoVector.contract (basis μ ⊗ₜ φ) = φ μ
```

**`Lorentz.Vector.contract_basis_right`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L101).

```lean
lemma Vector.contract_basis_right (φ : Vector d) (μ : Fin 1 ⊕ Fin d) :
    Vector.contract (φ ⊗ₜ basis μ) = φ μ
```

**`Lorentz.CoVector.contract_basis_right`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L104).

```lean
lemma CoVector.contract_basis_right (ψ : CoVector d) (μ : Fin 1 ⊕ Fin d) :
    CoVector.contract (ψ ⊗ₜ basis μ) = ψ μ
```

**`Lorentz.Vector.contract_eq_coVector_contract`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L107).

```lean
lemma Vector.contract_eq_coVector_contract (φ : Vector d) (ψ : CoVector d) :
    Vector.contract (φ ⊗ₜ ψ) = CoVector.contract (ψ ⊗ₜ φ)
```

**`Lorentz.Vector.contract_rep`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L111).

```lean
lemma Vector.contract_rep (Λ : LorentzGroup d) (φ : Vector d) (ψ : CoVector d) :
    Vector.contract ((Vector.rep Λ φ) ⊗ₜ (CoVector.rep Λ ψ)) = Vector.contract (φ ⊗ₜ ψ)
```

**`Lorentz.CoVector.contract_rep`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean#L115).

```lean
lemma CoVector.contract_rep (Λ : LorentzGroup d) (φ : CoVector d) (ψ : Vector d) :
    CoVector.contract ((CoVector.rep Λ φ) ⊗ₜ (Vector.rep Λ ψ)) = CoVector.contract (φ ⊗ₜ ψ)
```

## Depends on

- [Representation of the Lorentz group on Lorentz vectors](realtensor-covector-representation.md)
- [Representation of the Lorentz group on Lorentz vectors](realtensor-vector-representation.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Representation/Contraction.lean)
