---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.unitaryToPMap, ProbabilisticTheory.QuantumMechanics.unitaryToPMap_domain, ProbabilisticTheory.QuantumMechanics.one_sub_unitaryToPMap_domain, ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap, ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_domain, ProbabilisticTheory.QuantumMechanics.one_sub_unitaryToPMap_denseRange_of_ker_eq_bot, ProbabilisticTheory.QuantumMechanics.unitaryToPMap_cayleyUnitary_eq_cayleyPMap, ProbabilisticTheory.QuantumMechanics.cayleyUnitary_one_sub_ker_eq_bot
statement: formalized
proof: formalized
---

# The inverse Cayley transform

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Cayley.Inverse`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean): 26 declarations, 4 with a docstring.

> The inverse Cayley transform of a unitary without eigenvalue 1 is self-adjoint.

## i. Overview

> For a unitary `u`, the inverse Cayley transform is the operator `i (1 + u)(1 - u)⁻¹`, defined on the
> range of `1 - u`. If `1` is not an eigenvalue of `u`, the range of `1 - u` is dense and the inverse
> Cayley transform is self-adjoint. It inverts the Cayley transform of a self-adjoint operator.

## ii. Key results

> - `inverseCayleyPMap` : the inverse Cayley transform of a unitary.
> - `CayleyUnitaryData` : a unitary without eigenvalue `1`.
> - `inverseCayleyPMap_isSelfAdjoint` : the inverse Cayley transform is self-adjoint.
> - `cayleyContinuousLinearMap_inverseCayleyPMap_eq` : the Cayley transform of the inverse Cayley
>   transform is `u`.

## iv. References

> * None.

## A. The partial inverse Cayley transform

**`ProbabilisticTheory.QuantumMechanics.unitaryToPMap`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L59).

> A bounded unitary operator viewed as a total `LinearPMap`.

```lean
def unitaryToPMap (u : H ≃ₗᵢ[ℂ] H) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.unitaryToPMap_domain`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L64).

```lean
lemma unitaryToPMap_domain (u : H ≃ₗᵢ[ℂ] H) : (unitaryToPMap u).domain = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.one_sub_unitaryToPMap_domain`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L69).

```lean
lemma one_sub_unitaryToPMap_domain (u : H ≃ₗᵢ[ℂ] H) :
    (1 - unitaryToPMap u).domain = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L74).

> The partial inverse Cayley transform of a unitary operator.

```lean
def inverseCayleyPMap (u : H ≃ₗᵢ[ℂ] H) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_domain`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L78).

```lean
lemma inverseCayleyPMap_domain (u : H ≃ₗᵢ[ℂ] H) :
    (inverseCayleyPMap u).domain = (1 - unitaryToPMap u).toFun.range
```

## B. Density of the range of `1 - u`

**`ProbabilisticTheory.QuantumMechanics.one_sub_unitaryToPMap_denseRange_of_ker_eq_bot`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L101).

```lean
lemma one_sub_unitaryToPMap_denseRange_of_ker_eq_bot {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) :
    Dense ((1 - unitaryToPMap u).toFun.range : Set H)
```

**`ProbabilisticTheory.QuantumMechanics.unitaryToPMap_cayleyUnitary_eq_cayleyPMap`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L162).

```lean
lemma unitaryToPMap_cayleyUnitary_eq_cayleyPMap {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) :
    unitaryToPMap (cayleyUnitary T hT) = cayleyPMap T
```

**`ProbabilisticTheory.QuantumMechanics.cayleyUnitary_one_sub_ker_eq_bot`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L172).

```lean
lemma cayleyUnitary_one_sub_ker_eq_bot {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) :
    (1 - unitaryToPMap (cayleyUnitary T hT)).toFun.ker = ⊥
```

**`ProbabilisticTheory.QuantumMechanics.linearPMap_range_smul`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L210).

```lean
lemma linearPMap_range_smul {Q : H →ₗ.[ℂ] H} (a : ℂ) (ha : a ≠ 0) :
    (a • Q).toFun.range = Q.toFun.range
```

**`ProbabilisticTheory.QuantumMechanics.linearPMap_comp_inverse_apply`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L236).

```lean
lemma linearPMap_comp_inverse_apply {Q : H →ₗ.[ℂ] H}
    (hker : Q.toFun.ker = ⊥) (y : Q.inverse.domain) :
    Q (⟨Q.inverse y, by
      rw [← LinearPMap.inverse_range (LinearPMap.toFun_ker_eq_bot_iff.mp hker)]
      exact LinearMap.mem_range_self _ y⟩ : Q.domain) = y
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_cayleyUnitary_domain`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L259).

```lean
lemma inverseCayleyPMap_cayleyUnitary_domain {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) :
    (inverseCayleyPMap (cayleyUnitary T hT)).domain = T.domain
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_apply_on_range`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L294).

```lean
lemma inverseCayleyPMap_apply_on_range {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) (a : (1 - unitaryToPMap u).domain) :
    inverseCayleyPMap u (⟨(1 - unitaryToPMap u) a, by
          rw [inverseCayleyPMap_domain u]
          exact LinearMap.mem_range_self _ a⟩) =
      Complex.I • (1 + unitaryToPMap u) a
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_cayleyUnitary`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L312).

```lean
lemma inverseCayleyPMap_cayleyUnitary {T : H →ₗ.[ℂ] H}
    (hT : IsSelfAdjoint T) :
    inverseCayleyPMap (cayleyUnitary T hT) = T
```

**`ProbabilisticTheory.QuantumMechanics.cayley_inner_identity`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L426).

```lean
lemma cayley_inner_identity (u : H ≃ₗᵢ[ℂ] H) (a b : H) :
    ⟪Complex.I • (a + u a), b - u b⟫_ℂ =
      ⟪a - u a, Complex.I • (b + u b)⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_isSymmetric`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L439).

> The inverse Cayley operator is symmetric whenever `1 - u` is injective.

```lean
lemma inverseCayleyPMap_isSymmetric {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) :
    (inverseCayleyPMap u).IsSymmetric
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_add_I_apply_on_range`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L473).

```lean
lemma inverseCayleyPMap_add_I_apply_on_range {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) (a : (1 - unitaryToPMap u).domain) :
    let x : (inverseCayleyPMap u).domain :=
      ⟨(1 - unitaryToPMap u) a, by
        rw [inverseCayleyPMap_domain u]
        exact LinearMap.mem_range_self _ a⟩
    inverseCayleyPMap u x + Complex.I • x = (2 * Complex.I) • (a : H)
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_sub_I_apply_on_range`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L486).

```lean
lemma inverseCayleyPMap_sub_I_apply_on_range {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) (a : (1 - unitaryToPMap u).domain) :
    let x : (inverseCayleyPMap u).domain :=
      ⟨(1 - unitaryToPMap u) a, by
        rw [inverseCayleyPMap_domain u]
        exact LinearMap.mem_range_self _ a⟩
    inverseCayleyPMap u x - Complex.I • x = (2 * Complex.I) • u (a : H)
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_hasDenseDomain`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L499).

```lean
lemma inverseCayleyPMap_hasDenseDomain {u : H ≃ₗᵢ[ℂ] H}
    (h_dense : Dense ((1 - unitaryToPMap u).toFun.range : Set H)) :
    (inverseCayleyPMap u).HasDenseDomain
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_add_I_range_eq_top`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L507).

```lean
lemma inverseCayleyPMap_add_I_range_eq_top {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) :
    (inverseCayleyPMap u + Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_sub_I_range_eq_top`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L534).

```lean
lemma inverseCayleyPMap_sub_I_range_eq_top {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) :
    (inverseCayleyPMap u - Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

## C. Self-adjointness of the inverse Cayley transform

**`ProbabilisticTheory.QuantumMechanics.CayleyUnitaryData`**, a structure, [line 565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L565).

> The standard hypotheses for taking an inverse Cayley transform.

```lean
structure CayleyUnitaryData (u : H ≃ₗᵢ[ℂ] H) : Prop where
  /-- The point `1` is not an eigenvalue of the unitary. -/
  one_sub_injective : (1 - unitaryToPMap u).toFun.ker = ⊥
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_isSelfAdjoint`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L569).

```lean
lemma inverseCayleyPMap_isSelfAdjoint {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥)
    (h_dense : Dense ((1 - unitaryToPMap u).toFun.range : Set H)) :
    IsSelfAdjoint (inverseCayleyPMap u)
```

## D. Round trip with the forward Cayley transform

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_inverseCayleyPMap_apply`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L580).

```lean
lemma cayleyContinuousLinearMap_inverseCayleyPMap_apply {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥)
    (h_dense : Dense ((1 - unitaryToPMap u).toFun.range : Set H)) (x : H) :
    cayleyContinuousLinearMap (inverseCayleyPMap u)
      (inverseCayleyPMap_isSelfAdjoint hker h_dense) x = u x
```

**`ProbabilisticTheory.QuantumMechanics.cayleyContinuousLinearMap_inverseCayleyPMap_eq`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L626).

```lean
lemma cayleyContinuousLinearMap_inverseCayleyPMap_eq {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥)
    (h_dense : Dense ((1 - unitaryToPMap u).toFun.range : Set H)) :
    cayleyContinuousLinearMap (inverseCayleyPMap u)
        (inverseCayleyPMap_isSelfAdjoint hker h_dense) =
      u.toLinearIsometry.toContinuousLinearMap
```

**`ProbabilisticTheory.QuantumMechanics.inverseCayleyPMap_isSelfAdjoint_of_ker_eq_bot`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L635).

```lean
lemma inverseCayleyPMap_isSelfAdjoint_of_ker_eq_bot {u : H ≃ₗᵢ[ℂ] H}
    (hker : (1 - unitaryToPMap u).toFun.ker = ⊥) :
    IsSelfAdjoint (inverseCayleyPMap u)
```

**`ProbabilisticTheory.QuantumMechanics.CayleyUnitaryData.inverse_isSelfAdjoint`**, a lemma, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean#L641).

```lean
lemma CayleyUnitaryData.inverse_isSelfAdjoint {u : H ≃ₗᵢ[ℂ] H}
    (hu : CayleyUnitaryData u) : IsSelfAdjoint (inverseCayleyPMap u)
```

## Depends on

- [The Cayley transform](unbounded-cayley-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Inverse.lean)
