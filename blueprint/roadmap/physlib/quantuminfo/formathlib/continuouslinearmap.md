---
declaration: module
origin: cited
lean: ContinuousLinearMap.support_eq_sup_eigenspace_nonzero, ContinuousLinearMap.ker_mk
statement: formalized
proof: formalized
---

# Continuous linear maps

The module `QuantumInfo.ForMathlib.ContinuousLinearMap`, [QuantumInfo/ForMathlib/ContinuousLinearMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousLinearMap.lean): 2 declarations, 1 with a docstring, 1 listed as significant.

> This file collects auxiliary results about `ContinuousLinearMap`s that are not (yet) available in
> Mathlib.

## Main results

> * `ContinuousLinearMap.ker_mk`: the kernel of the continuous linear map built from a continuous
>   semilinear map `f` agrees with the kernel of `f`.
> * `ContinuousLinearMap.support_eq_sup_eigenspace_nonzero`: the range of a symmetric continuous
>   linear map on a finite-dimensional Euclidean space is the supremum of its eigenspaces for
>   nonzero eigenvalues.

**`ContinuousLinearMap.ker_mk`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousLinearMap.lean#L34).

```lean
lemma ker_mk (f : M →ₛₗ[σ] M₂) (hf : Continuous f.toFun) :
    (ContinuousLinearMap.mk f hf).ker = LinearMap.ker f
```

**`ContinuousLinearMap.support_eq_sup_eigenspace_nonzero`**, a theorem, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousLinearMap.lean#L45). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The support of a Hermitian matrix is the sum of its nonzero eigenspaces.

```lean
theorem support_eq_sup_eigenspace_nonzero (A : EuclideanSpace 𝕜 n →L[𝕜] EuclideanSpace 𝕜 n)
    (hA : A.IsSymmetric) : A.range = ⨆ μ ≠ 0, Module.End.eigenspace A μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/ContinuousLinearMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousLinearMap.lean)
