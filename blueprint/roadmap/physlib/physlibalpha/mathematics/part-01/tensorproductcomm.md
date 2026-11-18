---
declaration: module
origin: cited
lean: lTensor_map_id_comm, congr_assoc_map_id_comm
statement: formalized
proof: formalized
---

# Commuting tensor-factor endomorphisms

The module `PhyslibAlpha.Mathematics.TensorProductComm`, [PhyslibAlpha/Mathematics/TensorProductComm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TensorProductComm.lean): 2 declarations, 2 with a docstring.

## i. Overview

> An endomorphism of one tensor factor of `W ⊗ X` commutes with a map acting on another
> factor, since the two act independently. `lTensor_map_id_comm` is that fact for two
> factors, and `congr_assoc_map_id_comm` is its analogue after reassociating and recombining
> a third factor into the second.

## ii. Key results

> - `lTensor_map_id_comm` : an endomorphism of the second tensor factor commutes with one of the first
> - `congr_assoc_map_id_comm` : reassociating and recombining the last two tensor factors commutes
>   with an endomorphism of the first

## iv. References

> * None.

## A. Commuting tensor-factor endomorphisms

**`lTensor_map_id_comm`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TensorProductComm.lean#L45).

> An endomorphism of the second tensor factor commutes with one of the first.

```lean
lemma lTensor_map_id_comm {k : Type} [CommSemiring k] {W X : Type} [AddCommMonoid W]
    [Module k W] [AddCommMonoid X] [Module k X] (f : X →ₗ[k] X) (g : W →ₗ[k] W)
    (t : W ⊗[k] X) :
    (LinearMap.lTensor W f) (TensorProduct.map g LinearMap.id t) =
      TensorProduct.map g LinearMap.id ((LinearMap.lTensor W f) t)
```

**`congr_assoc_map_id_comm`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TensorProductComm.lean#L56).

> Reassociating and recombining the last two tensor factors commutes with an
> endomorphism of the first.

```lean
lemma congr_assoc_map_id_comm {k : Type} [CommSemiring k] {W X Y Z : Type} [AddCommMonoid W]
    [Module k W] [AddCommMonoid X] [Module k X] [AddCommMonoid Y] [Module k Y]
    [AddCommMonoid Z] [Module k Z] (E : X ⊗[k] Y ≃ₗ[k] Z) (g : W →ₗ[k] W)
    (t : (W ⊗[k] X) ⊗[k] Y) :
    (TensorProduct.congr (LinearEquiv.refl k W) E) (TensorProduct.assoc k W X Y
        (TensorProduct.map (TensorProduct.map g LinearMap.id) LinearMap.id t)) =
      TensorProduct.map g LinearMap.id
        ((TensorProduct.congr (LinearEquiv.refl k W) E) (TensorProduct.assoc k W X Y t))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TensorProductComm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TensorProductComm.lean)
