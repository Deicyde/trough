---
declaration: module
origin: cited
lean: LinearMap.map_smul_of_commutesI, LinearMap.commutesI_of_basis, ContinuousLinearMap.complexOfCommutesI, ContinuousLinearMap.complexOfCommutesI_apply
statement: formalized
proof: formalized
---

# Upgrading a real-linear map to a complex-linear one

The module `Physlib.Mathematics.ForMathlib.ComplexLinear`, [Physlib/Mathematics/ForMathlib/ComplexLinear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean): 4 declarations, 3 with a docstring.

## i. Overview

> An `ℝ`-linear map between complex vector spaces that commutes with multiplication by `i` is
> `ℂ`-linear, since `c = c.re + c.im · i`. Mathlib has the case of a map out of `ℂ`
> (`real_linearMap_map_smul_complex`, `ContinuousLinearMap.complexOfReal`); this file treats an
> arbitrary domain.

## ii. Key results

> - `LinearMap.map_smul_of_commutesI` : the law along one direction.
> - `LinearMap.commutesI_of_basis` : commuting with `i` on a `ℂ`-basis suffices.
> - `ContinuousLinearMap.complexOfCommutesI` : the resulting continuous `ℂ`-linear map.

## iv. References

> There are no known references for the material in this module.

## A. The scalar law

**`LinearMap.map_smul_of_commutesI`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean#L55).

> An `ℝ`-linear map commuting with `i` along `v` commutes with every complex scalar along `v`.

```lean
lemma map_smul_of_commutesI (L : V →ₗ[ℝ] E) {v : V}
    (h : L (Complex.I • v) = Complex.I • L v) (c : ℂ) :
    L (c • v) = c • L v
```

## B. Commuting with `i` on a basis

**`LinearMap.commutesI_of_basis`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean#L73).

> An `ℝ`-linear map commuting with `i` on a `ℂ`-basis commutes with `i` everywhere.

```lean
lemma commutesI_of_basis {ι : Type*} [Fintype ι] (L : V →ₗ[ℝ] E) (b : Module.Basis ι ℂ V)
    (h : ∀ i, L (Complex.I • b i) = Complex.I • L (b i)) (v : V) :
    L (Complex.I • v) = Complex.I • L v
```

## C. The complex-linear map

**`ContinuousLinearMap.complexOfCommutesI`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean#L95).

> A continuous `ℝ`-linear map commuting with `i`, as a continuous `ℂ`-linear map.

```lean
def complexOfCommutesI (L : V →L[ℝ] E)
    (h : ∀ v, L (Complex.I • v) = Complex.I • L v) : V →L[ℂ] E
```

**`ContinuousLinearMap.complexOfCommutesI_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean#L103).

```lean
lemma complexOfCommutesI_apply (L : V →L[ℝ] E)
    (h : ∀ v, L (Complex.I • v) = Complex.I • L v) (v : V) :
    complexOfCommutesI L h v = L v
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/ComplexLinear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/ComplexLinear.lean)
