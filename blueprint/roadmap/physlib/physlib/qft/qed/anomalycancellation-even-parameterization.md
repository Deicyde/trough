---
declaration: module
origin: cited
lean: PureU1.Even.parameterizationAsLinear, PureU1.Even.parameterizationAsLinear_val, PureU1.Even.parameterizationCharge_cube, PureU1.Even.parameterization, PureU1.Even.anomalyFree_param, PureU1.Even.GenericCase, PureU1.Even.genericCase_exists, PureU1.Even.SpecialCase
statement: formalized
proof: formalized
---

# Parameterization in even case

The module `Physlib.QFT.QED.AnomalyCancellation.Even.Parameterization`, [Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean): 14 declarations, 4 with a docstring.

> Given maps `g : Fin n.succ → ℚ`, `f : Fin n → ℚ` and `a : ℚ` we form a solution to the anomaly
> equations. We show that every solution can be got in this way, up to permutation, unless it, up to
> permutation, lives in the unshifted plane.

## References

> * The main reference is https://arxiv.org/pdf/1912.04804.pdf. [ref: arxiv\_1912\_04804]

**`PureU1.Even.parameterizationAsLinear`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L37).

> Given coefficients `g` of a point in the unshifted plane and `f` of a point in the
> shifted plane, and a rational, we get a
> rational `a ∈ ℚ`, we get a
> point in `(PureU1 (2 * n.succ)).AnomalyFreeLinear`, which we will later show extends to an anomaly
> free point.

```lean
def parameterizationAsLinear (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (a : ℚ) :
    (PureU1 (2 * n.succ)).LinSols
```

**`PureU1.Even.parameterizationAsLinear_val`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L45).

```lean
lemma parameterizationAsLinear_val (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (a : ℚ) :
    (parameterizationAsLinear g f a).val =
    a •
      ((accCubeTriLinSymm (Shifted.planeCharges f) (Shifted.planeCharges f)
          (Unshifted.planeCharges g)) • Unshifted.planeCharges g +
        (- accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
          (Shifted.planeCharges f)) • Shifted.planeCharges f)
```

**`PureU1.Even.parameterizationCharge_cube`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L57).

```lean
lemma parameterizationCharge_cube (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (a : ℚ) :
    accCube (2* n.succ) (parameterizationAsLinear g f a).val = 0
```

**`PureU1.Even.parameterization`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L69).

> The construction of a `Sol` from a `Fin n.succ → ℚ`, a `Fin n → ℚ` and a `ℚ`.

```lean
def parameterization (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (a : ℚ) :
    (PureU1 (2 * n.succ)).Sols
```

**`PureU1.Even.anomalyFree_param`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L74).

```lean
lemma anomalyFree_param {S : (PureU1 (2 * n.succ)).Sols}
    (g : Fin n.succ → ℚ) (f : Fin n → ℚ)
    (hS : S.val = Unshifted.planeCharges g + Shifted.planeCharges f) :
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.planeCharges f) =
      - accCubeTriLinSymm (Shifted.planeCharges f) (Shifted.planeCharges f)
        (Unshifted.planeCharges g)
```

**`PureU1.Even.GenericCase`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L100).

> A proposition on a solution which is true if
> `accCubeTriLinSymm (Unshifted.planeCharges g, Unshifted.planeCharges g,
>   Shifted.planeCharges f) ≠ 0`.
> In this case our parameterization above will be able to recover this point.

```lean
def GenericCase (S : (PureU1 (2 * n.succ)).Sols) : Prop
```

**`PureU1.Even.genericCase_exists`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L106).

```lean
lemma genericCase_exists (S : (PureU1 (2 * n.succ)).Sols)
    (hs : ∃ (g : Fin n.succ → ℚ) (f : Fin n → ℚ),
      S.val = Unshifted.planeCharges g + Shifted.planeCharges f ∧
      accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.planeCharges f) ≠ 0) : GenericCase S
```

**`PureU1.Even.SpecialCase`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L121).

> A proposition on a solution which is true if
> `accCubeTriLinSymm (Unshifted.planeCharges g, Unshifted.planeCharges g,
>   Shifted.planeCharges f) = 0`.

```lean
def SpecialCase (S : (PureU1 (2 * n.succ)).Sols) : Prop
```

**`PureU1.Even.specialCase_exists`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L127).

```lean
lemma specialCase_exists (S : (PureU1 (2 * n.succ)).Sols)
    (hs : ∃ (g : Fin n.succ → ℚ) (f : Fin n → ℚ),
      S.val = Unshifted.planeCharges g + Shifted.planeCharges f ∧
      accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.planeCharges f) = 0) : SpecialCase S
```

**`PureU1.Even.generic_or_special`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L139).

```lean
lemma generic_or_special (S : (PureU1 (2 * n.succ)).Sols) :
    GenericCase S ∨ SpecialCase S
```

**`PureU1.Even.generic_case`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L151).

```lean
lemma generic_case {S : (PureU1 (2 * n.succ)).Sols} (h : GenericCase S) :
    ∃ g f a, S = parameterization g f a
```

**`PureU1.Even.special_case_lineInCubic`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L169).

```lean
lemma special_case_lineInCubic {S : (PureU1 (2 * n.succ)).Sols}
    (h : SpecialCase S) : LineInCubic S.1.1
```

**`PureU1.Even.special_case_lineInCubic_perm`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L186).

```lean
lemma special_case_lineInCubic_perm {S : (PureU1 (2 * n.succ)).Sols}
    (h : ∀ (M : (FamilyPermutations (2 * n.succ)).group),
    SpecialCase ((FamilyPermutations (2 * n.succ)).solAction.toFun _ _ S M)) :
    LineInCubicPerm S.1.1
```

**`PureU1.Even.special_case`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean#L192).

```lean
lemma special_case {S : (PureU1 (2 * n.succ.succ)).Sols}
    (h : ∀ (M : (FamilyPermutations (2 * n.succ.succ)).group),
    SpecialCase ((FamilyPermutations (2 * n.succ.succ)).solAction.toFun _ _ S M)) :
    ∃ (M : (FamilyPermutations (2 * n.succ.succ)).group),
    ((FamilyPermutations (2 * n.succ.succ)).solAction.toFun _ _ S M).1.1
    ∈ Submodule.span ℚ (Set.range Unshifted.basis)
```

## Depends on

- [Line In Cubic Even case](anomalycancellation-even-lineincubic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/Parameterization.lean)
