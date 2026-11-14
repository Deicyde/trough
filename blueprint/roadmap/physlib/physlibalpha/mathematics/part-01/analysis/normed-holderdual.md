---
declaration: module
origin: cited
lean: HolderDual.abs_sign_mul_le, HolderDual.abs_sum_mul_le, HolderDual.rpow_one_div_le_one_iff, HolderDual.repr_sum_smul_self, HolderDual.apply_eq_sum_repr, HolderDual.ofCoeffs, HolderDual.ofCoeffs_apply_basis, HolderDual.coeffEquiv
statement: formalized
proof: formalized
---

# Hölder duality in finite dimensions

The module `PhyslibAlpha.Mathematics.Analysis.Normed.HolderDual`, [PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean): 21 declarations, 10 with a docstring.

> The dual norm of an `ℓp` coordinate norm is the `ℓq` norm of the values on the basis.

## i. Overview

> A continuous linear functional on a finite-dimensional normed space is determined by its values on
> a basis. When the norm is the `ℓp` norm of the coordinates in that basis, the norm of a functional
> is the `ℓq` norm of its values, `q` the Hölder conjugate of `p`; for the sup norm it is the `ℓ1`
> norm. So the unit ball of the dual is the closed `ℓq` ball, resp. the `ℓ1` ball, of value vectors.

## ii. Key results

> - `HolderDual.coeffEquiv` : a functional is its vector of values on a basis.
> - `HolderDual.dualLp_norm_eq` : Hölder duality for `1 < p < ∞`.
> - `HolderDual.dualSup_norm_eq` : Hölder duality for `p = ∞`.
> - `HolderDual.dualLpEquiv`, `HolderDual.dualSupEquiv` : the unit ball of the dual in coordinates.

## iv. References

> - W. Rudin, *Functional Analysis*, 2nd ed., McGraw-Hill, 1991.

**`HolderDual.abs_sign_mul_le`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L53).

```lean
lemma abs_sign_mul_le (a g : ℝ) (hg : 0 ≤ g) : |(SignType.sign a : ℝ) * g| ≤ g
```

**`HolderDual.abs_sum_mul_le`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L59).

> Hölder's inequality for the absolute value of a finite sum.

```lean
lemma abs_sum_mul_le {n : ℕ} {p q : ℝ} (hpq : p.HolderConjugate q) (c v : Fin n → ℝ) :
    |∑ i, c i * v i| ≤ (∑ i, |c i| ^ q) ^ (1 / q) * (∑ i, |v i| ^ p) ^ (1 / p)
```

**`HolderDual.rpow_one_div_le_one_iff`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L65).

```lean
lemma rpow_one_div_le_one_iff {x q : ℝ} (hx : 0 ≤ x) (hq : 0 < q) :
    x ^ (1 / q) ≤ 1 ↔ x ≤ 1
```

## A. Functionals from their values on a basis

**`HolderDual.repr_sum_smul_self`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L74).

```lean
lemma repr_sum_smul_self (v : Fin n → ℝ) (i : Fin n) : b.repr (∑ j, v j • b j) i = v i
```

**`HolderDual.apply_eq_sum_repr`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L77).

```lean
lemma apply_eq_sum_repr (f : V →L[ℝ] ℝ) (v : V) : f v = ∑ i, f (b i) * b.repr v i
```

**`HolderDual.ofCoeffs`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L83).

> The continuous functional with values `a` on the basis.

```lean
noncomputable def ofCoeffs (a : Fin n → ℝ) : V →L[ℝ] ℝ
```

**`HolderDual.ofCoeffs_apply_basis`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L87).

```lean
lemma ofCoeffs_apply_basis (a : Fin n → ℝ) (i : Fin n) : ofCoeffs b a (b i) = a i
```

**`HolderDual.coeffEquiv`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L91).

> A functional is its vector of values on the basis.

```lean
noncomputable def coeffEquiv : (V →L[ℝ] ℝ) ≃ₗ[ℝ] (Fin n → ℝ)
```

**`HolderDual.coeffEquiv_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L99).

```lean
lemma coeffEquiv_apply (f : V →L[ℝ] ℝ) (i : Fin n) : coeffEquiv b f i = f (b i)
```

**`HolderDual.coeffEquiv_symm_apply_basis`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L101).

```lean
lemma coeffEquiv_symm_apply_basis (a : Fin n → ℝ) (i : Fin n) :
    (coeffEquiv b).symm a (b i) = a i
```

**`HolderDual.image_coeffEquiv_ball`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L107).

> If the norm of a functional is a function `N` of its values on the basis, the unit ball of
> the dual is `{a | N a ≤ 1}` in coordinates.

```lean
lemma image_coeffEquiv_ball {N : (Fin n → ℝ) → ℝ}
    (hN : ∀ f : V →L[ℝ] ℝ, ‖f‖ = N fun i => f (b i)) :
    coeffEquiv b '' {f | ‖f‖ ≤ 1} = {a | N a ≤ 1}
```

**`HolderDual.dualEquivOfNormEq`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L118).

> If the norm of a functional is a function `N` of its values on the basis, the functionals
> of norm at most `1` are the value vectors `a` with `N a ≤ 1`.

```lean
noncomputable def dualEquivOfNormEq {N : (Fin n → ℝ) → ℝ}
    (hN : ∀ f : V →L[ℝ] ℝ, ‖f‖ = N fun i => f (b i)) :
    {f : V →L[ℝ] ℝ // ‖f‖ ≤ 1} ≃ {a : Fin n → ℝ // N a ≤ 1}
```

## B. Hölder duality, `1 < p < ∞`

**`HolderDual.norm_sum_smul_self`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L131).

```lean
lemma norm_sum_smul_self (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p))
    (v : Fin n → ℝ) : ‖∑ j, v j • b j‖ = (∑ i, |v i| ^ p) ^ (1 / p)
```

**`HolderDual.norm_sum_sign_smul_le_one`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L136).

```lean
lemma norm_sum_sign_smul_le_one (hpq : p.HolderConjugate q)
    (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p)) (s : Fin n → ℝ) {g : Fin n → ℝ≥0}
    (hg : ∑ i, g i ^ p ≤ 1) : ‖∑ i, ((SignType.sign (s i) : ℝ) * g i) • b i‖ ≤ 1
```

**`HolderDual.exists_norm_le_one_apply_eq`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L147).

> The unit vector on which a functional attains the `ℓq` norm of its values on the basis.

```lean
lemma exists_norm_le_one_apply_eq (hpq : p.HolderConjugate q)
    (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p)) (f : V →L[ℝ] ℝ) :
    ∃ w : V, ‖w‖ ≤ 1 ∧ f w = (∑ i, |f (b i)| ^ q) ^ (1 / q)
```

**`HolderDual.dualLp_norm_eq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L163).

> **Hölder duality**: the norm of a functional is the `ℓq` norm of its values on the basis.

```lean
lemma dualLp_norm_eq (hpq : p.HolderConjugate q)
    (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p)) (f : V →L[ℝ] ℝ) :
    ‖f‖ = (∑ i, |f (b i)| ^ q) ^ (1 / q)
```

**`HolderDual.dualLpEquiv`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L175).

> The functionals of norm at most `1` are the closed `ℓq` ball of value vectors.

```lean
noncomputable def dualLpEquiv (hpq : p.HolderConjugate q)
    (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p)) :
    {f : V →L[ℝ] ℝ // ‖f‖ ≤ 1} ≃ {a : Fin n → ℝ // ∑ i, |a i| ^ q ≤ 1}
```

## C. Hölder duality, `p = ∞`

**`HolderDual.apply_eq_sum_single`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L185).

```lean
lemma apply_eq_sum_single (f : (Fin m → ℝ) →L[ℝ] ℝ) (v : Fin m → ℝ) :
    f v = ∑ i, f (Pi.single i 1) * v i
```

**`HolderDual.dualSup_norm_eq`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L191).

> **Hölder duality** for the sup norm: the norm of a functional is the `ℓ1` norm of its values
> on the standard basis.

```lean
lemma dualSup_norm_eq (f : (Fin m → ℝ) →L[ℝ] ℝ) : ‖f‖ = ∑ i, |f (Pi.single i 1)|
```

**`HolderDual.norm_eq_sum_abs_basisFun`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L206).

```lean
lemma norm_eq_sum_abs_basisFun (f : (Fin m → ℝ) →L[ℝ] ℝ) :
    ‖f‖ = ∑ i, |f (Pi.basisFun ℝ (Fin m) i)|
```

**`HolderDual.dualSupEquiv`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean#L211).

> The functionals of norm at most `1` on the sup-normed space are the closed `ℓ1` ball.

```lean
noncomputable def dualSupEquiv :
    {f : (Fin m → ℝ) →L[ℝ] ℝ // ‖f‖ ≤ 1} ≃ {a : Fin m → ℝ // ∑ i, |a i| ≤ 1}
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/Normed/HolderDual.lean)
