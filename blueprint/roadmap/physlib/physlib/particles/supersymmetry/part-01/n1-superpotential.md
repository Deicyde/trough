---
declaration: module
origin: cited
lean: SUSY.N1.Superpotential, SUSY.N1.Superpotential.dW, SUSY.N1.Superpotential.repr_dW
statement: formalized
proof: formalized
---

# SUSY N=1 superpotential

The module `Physlib.Particles.SuperSymmetry.N1.Superpotential`, [Physlib/Particles/SuperSymmetry/N1/Superpotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean): 4 declarations (1 instance with no name), 4 with a docstring.

> The superpotential of the N=1 chiral sector, and its gradient as a chiral tensor.

## i. Overview

> A superpotential on a domain `D` of configurations is a function `W` that is holomorphic on `D`.
> It coerces to that function, so `W u` is its value at `u`.
> Its gradient `∂_I W` is the covector of colour `chiralDown` whose components are the holomorphic
> Wirtinger derivatives of `W`. The conjugates `W̄` and `∂̄_J̄ W̄` are `star W` and
> `conjChiralCovector` of the gradient.

## ii. Key results

> - `SUSY.N1.Superpotential` : a superpotential, holomorphic on a domain.
> - `SUSY.N1.Superpotential.dW` : its gradient, a `chiralDown` covector.
> - `SUSY.N1.Superpotential.repr_dW` : the components of the gradient are `∂_I W`.

## iv. References

> * None.

## A. The superpotential

**`SUSY.N1.Superpotential`**, a structure, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean#L57).

> A superpotential on the domain `D`: a function `W` of the chiral configuration, holomorphic on
> `D`.

```lean
structure Superpotential (ι : Type) [Fintype ι] [DecidableEq ι]
    (D : Set (ChiralScalarConfiguration ι)) where
  /-- The superpotential `W`. -/
  W : ChiralScalarConfiguration ι → ℂ
  /-- `W` is holomorphic on `D`. -/
  holomorphic : ∀ u ∈ D, DifferentiableAt ℂ W u
```

**An instance with no name**, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean#L71).

> A superpotential is applied as the function `W`.

```lean
instance : CoeFun (Superpotential ι D) (fun _ => ChiralScalarConfiguration ι → ℂ)
```

## B. The gradient

**`SUSY.N1.Superpotential.dW`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean#L79).

> The gradient `∂_I W` of the superpotential, a covector of colour `chiralDown`.

```lean
def dW (W : Superpotential ι D) (u : ChiralScalarConfiguration ι) :
    (chiralTensor (ι := ι)).Tensor ![chiralDown]
```

**`SUSY.N1.Superpotential.repr_dW`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean#L84).

> The `I`-th component of the gradient is `∂_I W`.

```lean
lemma repr_dW (W : Superpotential ι D) (u : ChiralScalarConfiguration ι) (I : ι) :
    (basis (S := (chiralTensor (ι := ι)).toTensorSpecies) ![chiralDown]).repr (W.dW u) ![I] =
      dWirtingerCoord W I u
```

## Depends on

- [Partial Wirtinger derivatives `∂_I`, `∂̄_I` in a complex coordinate basis on `ℂ^n`](../../../mathematics/calculus/wirtinger-coordinate.md)
- [SUSY N=1 chiral sector: index, configuration, and conjugation data](n1-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/N1/Superpotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Superpotential.lean)
