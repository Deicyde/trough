---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.cayley, ProbabilisticTheory.QuantumMechanics.cayleyInverse, ProbabilisticTheory.QuantumMechanics.cayley_ne_one, ProbabilisticTheory.QuantumMechanics.cayley_re, ProbabilisticTheory.QuantumMechanics.cayley_im, ProbabilisticTheory.QuantumMechanics.cayleyInverse_cayley, ProbabilisticTheory.QuantumMechanics.cayley_norm, ProbabilisticTheory.QuantumMechanics.cayley_cayleyInverse
statement: formalized
proof: formalized
---

# The Cayley transform

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Cayley.Basic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean): 26 declarations, 7 with a docstring.

> The Cayley transform of a self-adjoint operator is a unitary.

## i. Overview

> The Cayley transform `c(x) = (x - i) / (x + i)` maps the real line onto the unit circle without `1`.
> Applied to a self-adjoint operator `T`, it gives the bounded operator `(T - i)(T + i)⁻¹`, which is
> unitary. This reduces the spectral theory of unbounded self-adjoint operators to that of unitaries.

## ii. Key results

> - `cayley`, `cayleyInverse` : the scalar Cayley transform and its inverse.
> - `cayleyPMap` : the Cayley transform of a partially defined operator.
> - `cayleyUnitary` : the Cayley transform of a self-adjoint operator, as a unitary.

## iv. References

> * None.

## A. The scalar Cayley transform

**`ProbabilisticTheory.QuantumMechanics.cayley`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L55).

> The scalar Cayley transform from the real line to the unit circle.

```lean
def cayley (x : ℝ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cayleyInverse`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L58).

> The inverse Cayley coordinate, with an arbitrary value at the point `1` (infinity).

```lean
def cayleyInverse (z : ℂ) : ℝ
```

**`ProbabilisticTheory.QuantumMechanics.cayley_ne_one`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L60).

```lean
lemma cayley_ne_one (x : ℝ) : cayley x ≠ 1
```

**`ProbabilisticTheory.QuantumMechanics.cayley_re`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L72).

```lean
lemma cayley_re (x : ℝ) : (cayley x).re = (x ^ 2 - 1) / (x ^ 2 + 1)
```

**`ProbabilisticTheory.QuantumMechanics.cayley_im`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L77).

```lean
lemma cayley_im (x : ℝ) : (cayley x).im = (-2 * x) / (x ^ 2 + 1)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyInverse_cayley`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L82).

```lean
lemma cayleyInverse_cayley (x : ℝ) : cayleyInverse (cayley x) = x
```

**`ProbabilisticTheory.QuantumMechanics.cayley_norm`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L88).

```lean
lemma cayley_norm (x : ℝ) : ‖cayley x‖ = 1
```

**`ProbabilisticTheory.QuantumMechanics.cayley_cayleyInverse`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L96).

```lean
lemma cayley_cayleyInverse {z : ℂ} (hz : ‖z‖ = 1) (hz1 : z ≠ 1) :
    cayley (cayleyInverse z) = z
```

**`ProbabilisticTheory.QuantumMechanics.measurable_cayley`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L124).

```lean
lemma measurable_cayley : Measurable cayley
```

**`ProbabilisticTheory.QuantumMechanics.measurable_cayleyInverse`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L128).

```lean
lemma measurable_cayleyInverse : Measurable cayleyInverse
```

## B. The Cayley transform of a partial operator

**`ProbabilisticTheory.QuantumMechanics.cayleyPMap`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L140).

> The Cayley transform before forgetting that it is bounded.

```lean
def cayleyPMap (T : H →ₗ.[ℂ] H) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cayleyPMap_domain_top`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L143).

```lean
lemma cayleyPMap_domain_top {T : H →ₗ.[ℂ] H} (hT : IsSelfAdjoint T) :
    (cayleyPMap T).domain = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.topDomainToContinuousLinearMap`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L182).

> Turn a continuous partial linear map with full domain into a bounded operator on `H`.

```lean
def topDomainToContinuousLinearMap (A : H →ₗ.[ℂ] H) (hdom : A.domain = ⊤)
    (hc : Continuous A.toFun) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.topDomainToContinuousLinearMap_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L197).

```lean
lemma topDomainToContinuousLinearMap_apply (A : H →ₗ.[ℂ] H) (hdom : A.domain = ⊤)
    (hc : Continuous A.toFun) (x : H) :
    topDomainToContinuousLinearMap A hdom hc x = A ⟨x, hdom ▸ Submodule.mem_top⟩
```

**`ProbabilisticTheory.QuantumMechanics.cayleyPMap_eq_one_sub`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L202).

```lean
lemma cayleyPMap_eq_one_sub {T : H →ₗ.[ℂ] H} (hT : IsSelfAdjoint T) :
    cayleyPMap T = 1 - (2 * Complex.I) • (T + Complex.I • 1).inverse
```

**`ProbabilisticTheory.QuantumMechanics.cayleyPMap_eq_one_sub_minus`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L251).

```lean
lemma cayleyPMap_eq_one_sub_minus {T : H →ₗ.[ℂ] H} (hT : IsSelfAdjoint T) :
    cayleyPMap T = 1 - (2 * Complex.I) • (T - (-Complex.I) • 1).inverse
```

## C. The bounded, unitary Cayley transform

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L263).

> The bounded operator represented by the Cayley transform of a self-adjoint `LinearPMap`.

```lean
noncomputable def cayleyContinuousLinearMap (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.continuousLinearMapToPMap`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L273).

> A bounded operator, viewed as an everywhere-defined `LinearPMap`.

```lean
def continuousLinearMapToPMap (L : H →L[ℂ] H) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cayleyPMap_eq_continuousLinearMapToPMap`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L276).

```lean
lemma cayleyPMap_eq_continuousLinearMapToPMap {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) :
    cayleyPMap T = continuousLinearMapToPMap (cayleyContinuousLinearMap T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_norm_shift`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L304).

```lean
lemma cayleyContinuousLinearMap_norm_shift {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) (y : T.domain) :
    ‖T y - Complex.I • (y : H)‖ = ‖T y + Complex.I • (y : H)‖
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_apply_of_mem_range`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L326).

```lean
lemma cayleyContinuousLinearMap_apply_of_mem_range {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) (y : (T + Complex.I • 1).domain) (x : H)
    (hy : (T + Complex.I • 1) y = x) :
    cayleyContinuousLinearMap T hT x = (T - Complex.I • 1) y
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_norm_map`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L380).

```lean
lemma cayleyContinuousLinearMap_norm_map {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) (x : H) :
    ‖cayleyContinuousLinearMap T hT x‖ = ‖x‖
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_isometry`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L402).

```lean
lemma cayleyContinuousLinearMap_isometry {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) : Isometry (cayleyContinuousLinearMap T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_surjective`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L410).

```lean
lemma cayleyContinuousLinearMap_surjective {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) : Function.Surjective (cayleyContinuousLinearMap T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyUnitary`**, a def, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L431).

> The unitary Cayley transform of a self-adjoint partial operator.

```lean
noncomputable def cayleyUnitary (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) : H ≃ₗᵢ[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cayleyUnitary_apply`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean#L438).

```lean
lemma cayleyUnitary_apply (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x : H) :
    cayleyUnitary T hT x = cayleyContinuousLinearMap T hT x
```

## Depends on

- [Spectral theory for closed operators](../../../../physlib/quantummechanics/operators/spectraltheory/basic.md)

## Proof depends on

- [Spectral theory for self-adjoint operators](../../../../physlib/quantummechanics/operators/spectraltheory/selfadjoint.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Basic.lean)
