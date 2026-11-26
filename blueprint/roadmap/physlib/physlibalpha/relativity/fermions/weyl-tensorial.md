---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl.tensorial, Fermion.LeftHandedWeyl.toTensor_eq_fromSingleT, Fermion.LeftHandedWeyl.toTensor_rep, Fermion.LeftHandedWeyl.toTensor_basis, Fermion.RightHandedWeyl.tensorial, Fermion.RightHandedWeyl.toTensor_eq_fromSingleT, Fermion.RightHandedWeyl.toTensor_rep, Fermion.RightHandedWeyl.toTensor_basis
statement: formalized
proof: formalized
---

# Weyl fermions as tensors

The module `PhyslibAlpha.Relativity.Fermions.Weyl.Tensorial`, [PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean): 8 declarations, 6 with a docstring.

> Left- and right-handed Weyl fermions are the complex Lorentz tensors with one undotted or one
> dotted index.

## i. Overview

> A left-handed Weyl fermion is a complex Lorentz tensor with a single index of colour `.upL`, and a
> right-handed one a tensor with a single index of colour `.upR`. In both cases `fromSingleT` is the
> linear equivalence between the two. It makes `Fermion.LeftHandedWeyl` and
> `Fermion.RightHandedWeyl` tensorial types, so that tensor products of them with other tensorial
> types are tensorial through `TensorSpecies.Tensorial.prod`. The equivalence carries the action of
> `SL(2, ℂ)` on spinors to the action on tensors, and the basis spinor `e_a` to the basis tensor with
> the single component `a`, for left-handed (A) and right-handed (B) fermions alike.

## ii. Key results

> - `Fermion.LeftHandedWeyl.tensorial` : left-handed Weyl fermions are the tensors with one index
>   `.upL`.
> - `Fermion.RightHandedWeyl.tensorial` : right-handed Weyl fermions are the tensors with one index
>   `.upR`.
> - `Fermion.LeftHandedWeyl.toTensor_basis`, `Fermion.RightHandedWeyl.toTensor_basis` : the basis
>   spinor `e_a` is the basis tensor with component `a`.

## iv. References

> The tensorial class is in `Physlib.Relativity.Tensors.Tensorial`. The tensorial instance of complex
> four-vectors is in `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.Tensorial`.

## A. Left-handed Weyl fermions

**`Fermion.LeftHandedWeyl.tensorial`**, an instance, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L63).

> Left-handed Weyl fermions are the complex Lorentz tensors with one index `.upL`, through
> `fromSingleT`.

```lean
noncomputable instance tensorial : Tensorial complexLorentzTensor ![.upL] LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.toTensor_eq_fromSingleT`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L66).

```lean
lemma toTensor_eq_fromSingleT (ψ : LeftHandedWeyl) :
    toTensor ψ = fromSingleT (S := complexLorentzTensor) (c := .upL) ψ
```

**`Fermion.LeftHandedWeyl.toTensor_rep`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L71).

> The equivalence with the one-index tensors carries the action of `SL(2, ℂ)` on left-handed
> spinors to the action on tensors.

```lean
lemma toTensor_rep (g : SL(2,ℂ)) (ψ : LeftHandedWeyl) :
    toTensor (rep g ψ) = g • toTensor ψ
```

**`Fermion.LeftHandedWeyl.toTensor_basis`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L76).

> The basis spinor `e_a` is the basis tensor with the single component `a`.

```lean
lemma toTensor_basis (a : Fin 2) :
    toTensor (basis a) = Tensor.basis (S := complexLorentzTensor) ![.upL]
      (ComponentIdx.single.symm a)
```

## B. Right-handed Weyl fermions

**`Fermion.RightHandedWeyl.tensorial`**, an instance, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L97).

> Right-handed Weyl fermions are the complex Lorentz tensors with one index `.upR`, through
> `fromSingleT`.

```lean
noncomputable instance tensorial : Tensorial complexLorentzTensor ![.upR] RightHandedWeyl
```

**`Fermion.RightHandedWeyl.toTensor_eq_fromSingleT`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L100).

```lean
lemma toTensor_eq_fromSingleT (ψ : RightHandedWeyl) :
    toTensor ψ = fromSingleT (S := complexLorentzTensor) (c := .upR) ψ
```

**`Fermion.RightHandedWeyl.toTensor_rep`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L105).

> The equivalence with the one-index tensors carries the action of `SL(2, ℂ)` on right-handed
> spinors to the action on tensors.

```lean
lemma toTensor_rep (g : SL(2,ℂ)) (ψ : RightHandedWeyl) :
    toTensor (rep g ψ) = g • toTensor ψ
```

**`Fermion.RightHandedWeyl.toTensor_basis`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean#L110).

> The basis spinor `e_a` is the basis tensor with the single component `a`.

```lean
lemma toTensor_basis (a : Fin 2) :
    toTensor (basis a) = Tensor.basis (S := complexLorentzTensor) ![.upR]
      (ComponentIdx.single.symm a)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Tensorial.lean)
