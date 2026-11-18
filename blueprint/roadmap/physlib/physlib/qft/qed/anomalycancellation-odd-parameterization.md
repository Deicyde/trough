---
declaration: module
origin: cited
lean: PureU1.Odd.parameterizationAsLinear, PureU1.Odd.parameterizationAsLinear_val, PureU1.Odd.parameterizationCharge_cube, PureU1.Odd.parameterization, PureU1.Odd.anomalyFree_param, PureU1.Odd.GenericCase, PureU1.Odd.genericCase_exists, PureU1.Odd.SpecialCase
statement: formalized
proof: formalized
---

# Parameterization in odd case

The module `Physlib.QFT.QED.AnomalyCancellation.Odd.Parameterization`, [Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean): 14 declarations, 5 with a docstring.

> Given maps `g : Fin n → ℚ`, `f : Fin n → ℚ` and `a : ℚ` we form a solution to the anomaly
> equations. We show that every solution can be got in this way, up to permutation, unless it is zero.

## References

> * The main reference is https://arxiv.org/pdf/1912.04804.pdf. [ref: arxiv\_1912\_04804]

**`PureU1.Odd.parameterizationAsLinear`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L31).

> Given a `g f : Fin n → ℚ` and a `a : ℚ` we form a linear solution. We will later
> show that this can be extended to a complete solution.

```lean
def parameterizationAsLinear (g f : Fin n → ℚ) (a : ℚ) :
    (PureU1 (2 * n + 1)).LinSols
```

**`PureU1.Odd.parameterizationAsLinear_val`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L39).

```lean
lemma parameterizationAsLinear_val (g f : Fin n → ℚ) (a : ℚ) :
    (parameterizationAsLinear g f a).val =
    a •
      ((accCubeTriLinSymm (Shifted.planeCharges f) (Shifted.planeCharges f)
          (Unshifted.planeCharges g)) • Unshifted.planeCharges g +
        (- accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
          (Shifted.planeCharges f)) • Shifted.planeCharges f)
```

**`PureU1.Odd.parameterizationCharge_cube`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L52).

> The parameterization satisfies the cubic ACC.

```lean
lemma parameterizationCharge_cube (g f : Fin n → ℚ) (a : ℚ) :
    accCube (2 * n + 1) (parameterizationAsLinear g f a).val = 0
```

**`PureU1.Odd.parameterization`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L64).

> Given a `g f : Fin n → ℚ` and a `a : ℚ` we form a solution.

```lean
def parameterization (g f : Fin n → ℚ) (a : ℚ) :
    (PureU1 (2 * n + 1)).Sols
```

**`PureU1.Odd.anomalyFree_param`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L69).

```lean
lemma anomalyFree_param {S : (PureU1 (2 * n + 1)).Sols}
    (g f : Fin n → ℚ) (hS : S.val = Unshifted.planeCharges g + Shifted.planeCharges f) :
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.planeCharges f) =
    - accCubeTriLinSymm (Shifted.planeCharges f) (Shifted.planeCharges f)
      (Unshifted.planeCharges g)
```

**`PureU1.Odd.GenericCase`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L94).

> A proposition on a solution which is true if
> `accCubeTriLinSymm (Unshifted.planeCharges g, Unshifted.planeCharges g,
> Shifted.planeCharges f) ≠ 0`.
> In this case our parameterization above will be able to recover this point.

```lean
def GenericCase (S : (PureU1 (2 * n.succ + 1)).Sols) : Prop
```

**`PureU1.Odd.genericCase_exists`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L100).

```lean
lemma genericCase_exists (S : (PureU1 (2 * n.succ + 1)).Sols)
    (hs : ∃ (g f : Fin n.succ → ℚ),
      S.val = Unshifted.planeCharges g + Shifted.planeCharges f ∧
      accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.planeCharges f) ≠ 0) : GenericCase S
```

**`PureU1.Odd.SpecialCase`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L116).

> A proposition on a solution which is true if
> `accCubeTriLinSymm (Unshifted.planeCharges g, Unshifted.planeCharges g,
> Shifted.planeCharges f) ≠ 0`.
> In this case we will show that S is zero if it is true for all permutations.

```lean
def SpecialCase (S : (PureU1 (2 * n.succ + 1)).Sols) : Prop
```

**`PureU1.Odd.specialCase_exists`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L122).

```lean
lemma specialCase_exists (S : (PureU1 (2 * n.succ + 1)).Sols)
    (hs : ∃ (g f : Fin n.succ → ℚ),
      S.val = Unshifted.planeCharges g + Shifted.planeCharges f ∧
      accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.planeCharges f) = 0) : SpecialCase S
```

**`PureU1.Odd.generic_or_special`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L134).

```lean
lemma generic_or_special (S : (PureU1 (2 * n.succ + 1)).Sols) :
    GenericCase S ∨ SpecialCase S
```

**`PureU1.Odd.generic_case`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L147).

```lean
lemma generic_case {S : (PureU1 (2 * n.succ + 1)).Sols} (h : GenericCase S) :
    ∃ g f a, S = parameterization g f a
```

**`PureU1.Odd.special_case_lineInCubic`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L162).

```lean
lemma special_case_lineInCubic {S : (PureU1 (2 * n.succ + 1)).Sols}
    (h : SpecialCase S) :
      LineInCubic S.1.1
```

**`PureU1.Odd.special_case_lineInCubic_perm`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L180).

```lean
lemma special_case_lineInCubic_perm {S : (PureU1 (2 * n.succ + 1)).Sols}
    (h : ∀ (M : (FamilyPermutations (2 * n.succ + 1)).group),
    SpecialCase ((FamilyPermutations (2 * n.succ + 1)).solAction.toFun _ _ S M)) :
    LineInCubicPerm S.1.1
```

**`PureU1.Odd.special_case`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean#L188).

```lean
lemma special_case {S : (PureU1 (2 * n.succ.succ + 1)).Sols}
    (h : ∀ (M : (FamilyPermutations (2 * n.succ.succ + 1)).group),
    SpecialCase ((FamilyPermutations (2 * n.succ.succ + 1)).solAction.toFun _ _ S M)) :
    S.1.1 = 0
```

## Depends on

- [Line In Cubic Odd case](anomalycancellation-odd-lineincubic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/Parameterization.lean)
