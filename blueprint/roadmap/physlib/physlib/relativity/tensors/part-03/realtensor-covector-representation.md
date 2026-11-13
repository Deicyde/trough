---
declaration: module
origin: cited
lean: Lorentz.CoVector.rep, Lorentz.CoVector.rep_apply_eq_mulVec, Lorentz.CoVector.rep_apply_eq_sum, Lorentz.CoVector.rep_apply_eq_sum_coe, Lorentz.CoVector.rep_apply_basis, Lorentz.CoVector.rep_toMatrix, Lorentz.CoVector.rep_injective, Lorentz.CoVector.rep_surjective
statement: formalized
proof: formalized
---

# Representation of the Lorentz group on Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.CoVector.Representation`, [Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean): 9 declarations, 1 with a docstring.

> In this module we define the representation of the Lorentz group on Lorentz covectors.
> This does not define the MulAction on `Lorentz.CoVector`, which is induced
> by its tensor structure.

**`Lorentz.CoVector.rep`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L34).

> The representation of the Lorentz group on Lorentz covectors.

```lean
def rep {d : ℕ} : Representation ℝ (LorentzGroup d) (CoVector d)
```

## Properties of the representation.

**`Lorentz.CoVector.rep_apply_eq_mulVec`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L48).

```lean
lemma rep_apply_eq_mulVec (d : ℕ) (Λ : LorentzGroup d) (v : CoVector d) :
    rep Λ v = (LorentzGroup.transpose Λ⁻¹) *ᵥ v
```

**`Lorentz.CoVector.rep_apply_eq_sum`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L51).

```lean
lemma rep_apply_eq_sum (d : ℕ) (Λ : LorentzGroup d) (v : CoVector d) (k : Fin 1 ⊕ Fin d) :
    rep Λ v k = ∑ j, (Λ⁻¹).1 j k • v j
```

**`Lorentz.CoVector.rep_apply_eq_sum_coe`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L54).

```lean
lemma rep_apply_eq_sum_coe (d : ℕ) (Λ : LorentzGroup d) (v : CoVector d) (k : Fin 1 ⊕ Fin d) :
    rep Λ v k = ∑ j, Λ.1⁻¹ j k • v j
```

**`Lorentz.CoVector.rep_apply_basis`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L58).

```lean
lemma rep_apply_basis {d} (μ : Fin 1 ⊕ Fin d) (Λ : LorentzGroup d) :
    rep Λ (basis μ) = ∑ j, Λ.1⁻¹ μ j • basis j
```

**`Lorentz.CoVector.rep_toMatrix`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L63).

```lean
lemma rep_toMatrix (d : ℕ) (Λ : LorentzGroup d) :
    LinearMap.toMatrix basis basis (rep Λ) = Λ.1⁻¹ᵀ
```

**`Lorentz.CoVector.rep_injective`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L69).

```lean
lemma rep_injective (d : ℕ) (Λ : LorentzGroup d) : Function.Injective (rep Λ)
```

**`Lorentz.CoVector.rep_surjective`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L74).

```lean
lemma rep_surjective (d : ℕ) (Λ : LorentzGroup d) : Function.Surjective (rep Λ)
```

**`Lorentz.CoVector.rep_bijective`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L80).

```lean
lemma rep_bijective (d : ℕ) (Λ : LorentzGroup d) : Function.Bijective (rep Λ)
```

## Depends on

- [The Lorentz Group](../../lorentzgroup/basic.md)
- [Lorentz co vectors](realtensor-covector-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Representation.lean)
