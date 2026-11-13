---
declaration: module
origin: cited
lean: StandardModel.su2Epsilon, StandardModel.su2Epsilon_zero_zero, StandardModel.su2Epsilon_zero_one, StandardModel.su2Epsilon_one_zero, StandardModel.su2Epsilon_one_one, StandardModel.sum_su2Epsilon_mul, StandardModel.su2_star_eq_adjugate, StandardModel.su2_conj_apply
statement: formalized
proof: formalized
---

# The antisymmetric symbol and complex conjugation in `SU(2)`

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.SU2Conjugation`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean): 12 declarations, 12 with a docstring.

## i. Overview

> `su2Epsilon` is the antisymmetric symbol on two isospin indices: Physlib's `leviCivitaSymbol`
> on `Fin 2`, normalized by `su2Epsilon 0 1 = 1`. It transforms by the determinant, so every
> `U ∈ SU(2)` fixes it (`sum_su2Epsilon_mul`).
>
> The entrywise conjugate of `U ∈ SU(2)` is `ε U ε⁻¹`, entry by entry `conj U₀₀ = U₁₁`,
> `conj U₀₁ = -U₁₀`, `conj U₁₀ = -U₀₁` and `conj U₁₁ = U₀₀`. This is the pseudo-reality of
> `SU(2)`. It is a different fact from `conj U = (U⁻¹)ᵀ`, which holds for every unitary `U`. The
> classifiers and the Higgs sector use these identities only through explicit re-indexes by `ε`.

## ii. Key results

> - `su2Epsilon` : the antisymmetric symbol `ε_{ab}` on two `su(2)` fundamental indices: the
>   Levi-Civita symbol of `Fin 2`, normalized by `ε 0 1 = 1`
> - `sum_su2Epsilon_mul` : every element of `SU(2)` fixes the antisymmetric symbol: contracted against
>   two rows of `U` it gives `det U` times itself (`sum_leviCivitaSymbol_mul_prod`), and `det U = 1`

## iv. References

> * None.

## A. The antisymmetric symbol

**`StandardModel.su2Epsilon`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L56).

> The antisymmetric symbol `ε_{ab}` on two `su(2)` fundamental indices: the Levi-Civita
> symbol of `Fin 2`, normalized by `ε 0 1 = 1`.

```lean
def su2Epsilon (a b : Fin 2) : ℂ
```

**`StandardModel.su2Epsilon_zero_zero`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L59).

> The antisymmetric symbol vanishes when both indices are zero.

```lean
lemma su2Epsilon_zero_zero : su2Epsilon 0 0 = 0
```

**`StandardModel.su2Epsilon_zero_one`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L64).

> The antisymmetric symbol on the increasing pair.

```lean
lemma su2Epsilon_zero_one : su2Epsilon 0 1 = 1
```

**`StandardModel.su2Epsilon_one_zero`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L71).

> The antisymmetric symbol on the decreasing pair.

```lean
lemma su2Epsilon_one_zero : su2Epsilon 1 0 = -1
```

**`StandardModel.su2Epsilon_one_one`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L78).

> The antisymmetric symbol vanishes when both indices are one.

```lean
lemma su2Epsilon_one_one : su2Epsilon 1 1 = 0
```

**`StandardModel.sum_su2Epsilon_mul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L84).

> Every element of `SU(2)` fixes the antisymmetric symbol: contracted against two rows of
> `U` it gives `det U` times itself (`sum_leviCivitaSymbol_mul_prod`), and `det U = 1`.

```lean
lemma sum_su2Epsilon_mul (U : specialUnitaryGroup (Fin 2) ℂ) (b c : Fin 2) :
    ∑ x : Fin 2, ∑ y : Fin 2, su2Epsilon x y * (U.1 b x * U.1 c y) = su2Epsilon b c
```

## B. The entries of an `SU(2)` matrix under conjugation

> The determinant being one, the adjugate of `U` is its inverse, and `U` being unitary, so is
> its conjugate transpose. Reading the adjugate of a `2 × 2` matrix entry by entry gives the four
> identities.

**`StandardModel.su2_star_eq_adjugate`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L102).

> The conjugate transpose of an `SU(2)` matrix is its adjugate.

```lean
lemma su2_star_eq_adjugate (U : specialUnitaryGroup (Fin 2) ℂ) :
    star U.1 = Matrix.adjugate U.1
```

**`StandardModel.su2_conj_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L113).

> The conjugate of an entry of an `SU(2)` matrix is the transposed entry of its
> adjugate.

```lean
lemma su2_conj_apply (U : specialUnitaryGroup (Fin 2) ℂ) (i j : Fin 2) :
    conj (U.1 i j) = Matrix.adjugate U.1 j i
```

**`StandardModel.su2_conj_apply_zero_zero`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L119).

> Conjugating the upper left entry of an `SU(2)` matrix gives the lower right one.

```lean
lemma su2_conj_apply_zero_zero (U : specialUnitaryGroup (Fin 2) ℂ) :
    conj (U.1 0 0) = U.1 1 1
```

**`StandardModel.su2_conj_apply_one_one`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L125).

> Conjugating the lower right entry of an `SU(2)` matrix gives the upper left one.

```lean
lemma su2_conj_apply_one_one (U : specialUnitaryGroup (Fin 2) ℂ) :
    conj (U.1 1 1) = U.1 0 0
```

**`StandardModel.su2_conj_apply_zero_one`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L132).

> Conjugating the upper right entry of an `SU(2)` matrix gives minus the lower left
> one.

```lean
lemma su2_conj_apply_zero_one (U : specialUnitaryGroup (Fin 2) ℂ) :
    conj (U.1 0 1) = -U.1 1 0
```

**`StandardModel.su2_conj_apply_one_zero`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean#L139).

> Conjugating the lower left entry of an `SU(2)` matrix gives minus the upper right
> one.

```lean
lemma su2_conj_apply_one_zero (U : specialUnitaryGroup (Fin 2) ℂ) :
    conj (U.1 1 0) = -U.1 0 1
```

## Depends on

- [The Levi-Civita symbol in general dimension](../../../../physlib/mathematics/levicivita/basic.md)

## Proof depends on

- [Contracting the Levi-Civita symbol against a matrix](../../../mathematics/part-02/levicivita/basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/SU2Conjugation.lean)
