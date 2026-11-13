---
declaration: module
origin: cited
lean: Lorentz.Vector.rep, Lorentz.Vector.rep_apply_eq_mulVec, Lorentz.Vector.rep_apply_eq_sum, Lorentz.Vector.rep_apply_basis, Lorentz.Vector.rep_toMatrix, Lorentz.Vector.rep_injective, Lorentz.Vector.rep_surjective, Lorentz.Vector.rep_bijective
statement: formalized
proof: formalized
---

# Representation of the Lorentz group on Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Representation`, [Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean): 10 declarations, 1 with a docstring.

> In this module we define the representation of the Lorentz group on Lorentz vectors.
> This does not define the MulAction on `Lorentz.Vector`, which is induced
> by its tensor structure.

**`Lorentz.Vector.rep`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L34).

> The representation of the Lorentz group on Lorentz vectors.

```lean
def rep {d : ℕ} : Representation ℝ (LorentzGroup d) (Vector d)
```

## Properties of the representation.

**`Lorentz.Vector.rep_apply_eq_mulVec`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L45).

```lean
lemma rep_apply_eq_mulVec (d : ℕ) (Λ : LorentzGroup d) (v : Vector d) :
    rep Λ v = Λ *ᵥ v
```

**`Lorentz.Vector.rep_apply_eq_sum`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L48).

```lean
lemma rep_apply_eq_sum (d : ℕ) (Λ : LorentzGroup d) (v : Vector d) (k : Fin 1 ⊕ Fin d) :
    rep Λ v k = ∑ j, Λ.1 k j • v j
```

**`Lorentz.Vector.rep_apply_basis`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L51).

```lean
lemma rep_apply_basis {d} (μ : Fin 1 ⊕ Fin d) (Λ : LorentzGroup d) :
    rep Λ (basis μ) = ∑ j, Λ.1 j μ • basis j
```

**`Lorentz.Vector.rep_toMatrix`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L56).

```lean
lemma rep_toMatrix (d : ℕ) (Λ : LorentzGroup d) :
    LinearMap.toMatrix basis basis (rep Λ) = Λ.1
```

**`Lorentz.Vector.rep_injective`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L60).

```lean
lemma rep_injective (d : ℕ) (Λ : LorentzGroup d) : Function.Injective (rep Λ)
```

**`Lorentz.Vector.rep_surjective`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L63).

```lean
lemma rep_surjective (d : ℕ) (Λ : LorentzGroup d) : Function.Surjective (rep Λ)
```

**`Lorentz.Vector.rep_bijective`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L66).

```lean
lemma rep_bijective (d : ℕ) (Λ : LorentzGroup d) : Function.Bijective (rep Λ)
```

**`Lorentz.Vector.rep_contDiff`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L70).

```lean
lemma rep_contDiff (d : ℕ) {n} (Λ : LorentzGroup d) : ContDiff ℝ n (rep Λ)
```

**`Lorentz.Vector.rep_left_injective`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean#L75).

```lean
lemma rep_left_injective (d : ℕ) : Function.Injective (rep (d := d))
```

## Depends on

- [The Lorentz Group](../../lorentzgroup/basic.md)
- [Lorentz Vectors](realtensor-vector-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Representation.lean)
