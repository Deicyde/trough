---
declaration: module
origin: cited
lean: ProbabilisticTheory.PhiLM, ProbabilisticTheory.Phi, ProbabilisticTheory.Phi_apply, ProbabilisticTheory.PsiLM, ProbabilisticTheory.Psi, ProbabilisticTheory.Psi_apply, ProbabilisticTheory.Psi_Phi, ProbabilisticTheory.Phi_Psi
statement: formalized
proof: formalized
---

# W⋆-algebra structures are W⋆-algebras

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.Mathlib`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean): 15 declarations, 13 with a docstring.

> A W⋆-algebra structure with a chosen predual gives a W⋆-algebra in Mathlib's sense.

## i. Overview

> Mathlib's `WStarAlgebra` asks for a conjugate-linear isometric isomorphism from the dual of a Banach
> space onto `A`. For any Banach space `X`, `f ↦ conj ∘ f` is a conjugate-linear isometric isomorphism
> from the dual of `X` to the dual of `ConjSpace X`. Composing with the inverse of the linear
> identification of `A` with the dual of its predual shows that a W⋆-algebra structure gives a
> W⋆-algebra in Mathlib's sense, when the predual lives in the same universe as `A`.

## ii. Key results

> - `PhiEquiv` : the conjugate-linear isometric isomorphism between the duals of `X` and `ConjSpace
>   X`.
> - `WStarAlgebraStructure.toWStarAlgebra` : a W⋆-algebra structure gives a W⋆-algebra.

## iv. References

> * None.

## A. The conjugate-linear self-duality `Phi` of the strong dual, via `ConjSpace`

**`ProbabilisticTheory.PhiLM`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L57).

> The map `f ↦ (x ↦ conj (f x))` from the dual of `X` to linear functionals on `ConjSpace X`.

```lean
def PhiLM (f : StrongDual ℂ X) : ConjSpace X →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.Phi`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L66).

> `Phi f`, as a continuous linear functional on `ConjSpace X`: the same bound `‖f‖` works, since
> `conj` is an isometry of `ℂ`.

```lean
def Phi (f : StrongDual ℂ X) : StrongDual ℂ (ConjSpace X)
```

**`ProbabilisticTheory.Phi_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L72).

```lean
lemma Phi_apply (f : StrongDual ℂ X) (x : ConjSpace X) :
    Phi f x = starRingEnd ℂ (f (ofConj x))
```

**`ProbabilisticTheory.PsiLM`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L77).

> The linear part of `Psi`, the same construction the other way around:
> `g ↦ (x ↦ conj (g (toConj x)))`.

```lean
def PsiLM (g : StrongDual ℂ (ConjSpace X)) : X →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.Psi`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L88).

> `Psi g`, as a continuous linear functional on `X`.

```lean
def Psi (g : StrongDual ℂ (ConjSpace X)) : StrongDual ℂ X
```

**`ProbabilisticTheory.Psi_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L94).

```lean
lemma Psi_apply (g : StrongDual ℂ (ConjSpace X)) (x : X) :
    Psi g x = starRingEnd ℂ (g (toConj x))
```

**`ProbabilisticTheory.Psi_Phi`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L98).

> `Psi` undoes `Phi`: `conj (conj (f x)) = f x`.

```lean
lemma Psi_Phi (f : StrongDual ℂ X) : Psi (Phi f) = f
```

**`ProbabilisticTheory.Phi_Psi`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L102).

> `Phi` undoes `Psi`, the same computation run the other way.

```lean
lemma Phi_Psi (g : StrongDual ℂ (ConjSpace X)) : Phi (Psi g) = g
```

**`ProbabilisticTheory.PhiLM'`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L110).

> `Phi`, bundled as a (conjugate-)linear map `StrongDual ℂ X →ₛₗ[starRingEnd ℂ]
> StrongDual ℂ (ConjSpace X)`: additive since `conj` and evaluation both are, and conjugate-linear
> in `f` because `conj ((c • f) x) = conj (c * f x) = conj c * conj (f x)`.

```lean
def PhiLM' : StrongDual ℂ X →ₛₗ[starRingEnd ℂ] StrongDual ℂ (ConjSpace X)
```

**`ProbabilisticTheory.norm_Phi_le`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L116).

> `‖Phi f‖ ≤ ‖f‖`, from the bound used to build `Phi f` via `LinearMap.mkContinuous`.

```lean
lemma norm_Phi_le (f : StrongDual ℂ X) : ‖Phi f‖ ≤ ‖f‖
```

**`ProbabilisticTheory.norm_Psi_le`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L120).

> `‖Psi g‖ ≤ ‖g‖`, the mirror-image bound for `Psi`.

```lean
lemma norm_Psi_le (g : StrongDual ℂ (ConjSpace X)) : ‖Psi g‖ ≤ ‖g‖
```

**`ProbabilisticTheory.norm_Phi_eq`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L125).

> `Phi` is isometric: `≤` from `norm_Phi_le` directly, `≥` from applying `norm_Psi_le` to
> `Phi f` and using that `Psi` undoes `Phi`.

```lean
lemma norm_Phi_eq (f : StrongDual ℂ X) : ‖Phi f‖ = ‖f‖
```

**`ProbabilisticTheory.PhiLI`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L131).

> `Phi`, bundled as a conjugate-linear *isometric embedding*.

```lean
def PhiLI : StrongDual ℂ X →ₛₗᵢ[starRingEnd ℂ] StrongDual ℂ (ConjSpace X)
```

**`ProbabilisticTheory.PhiEquiv`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L137).

> **`Phi`, bundled as a conjugate-linear isometric equivalence.** Surjective because `Psi` is a
> two-sided inverse (`Phi_Psi`); an isometric embedding is automatically injective, so this is
> exactly `Phi`'s promotion to a `≃ₗᵢ⋆[ℂ]`.

```lean
def PhiEquiv : StrongDual ℂ X ≃ₗᵢ⋆[ℂ] StrongDual ℂ (ConjSpace X)
```

## B. Closing the connection to Mathlib's `WStarAlgebra`

**`ProbabilisticTheory.WStarAlgebraStructure.toWStarAlgebra`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean#L146).

> **A W⋆-algebra structure gives a W⋆-algebra** in Mathlib's sense, when the predual lives in the
> universe of `A`.

```lean
lemma WStarAlgebraStructure.toWStarAlgebra
    {A : Type u} [WStarAlgebraStructure.{u, u} A] : WStarAlgebra A
```

## Depends on

- [W⋆-algebras and normal states](basic.md)
- [The complex conjugate of a normed space](conjspace.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Mathlib.lean)
