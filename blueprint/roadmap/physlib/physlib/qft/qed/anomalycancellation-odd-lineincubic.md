---
declaration: module
origin: cited
lean: PureU1.Odd.LineInCubic, PureU1.Odd.lineInCubic_expand, PureU1.Odd.line_in_cubic_P_P_P!, PureU1.Odd.LineInCubicPerm, PureU1.Odd.lineInCubicPerm_self, PureU1.Odd.lineInCubicPerm_permute, PureU1.Odd.lineInCubicPerm_swap, PureU1.Odd.P_P_P!_accCube'
statement: formalized
proof: formalized
---

# Line In Cubic Odd case

The module `Physlib.QFT.QED.AnomalyCancellation.Odd.LineInCubic`, [Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean): 12 declarations, 5 with a docstring.

> We say that a linear solution satisfies the `lineInCubic` property
> if the line through that point and through the two different planes formed by the basis of
> `LinSols` lies in the cubic.
>
> We show that for a solution all its permutations satisfy this property,
> then the charge must be zero.

## References

> * The main reference for this file is https://arxiv.org/pdf/1912.04804.pdf. [ref: arxiv\_1912\_04804]

**`PureU1.Odd.LineInCubic`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L37).

> A property on `LinSols`, satisfied if every point on the line between the two planes
> in the basis through that point is in the cubic.

```lean
def LineInCubic (S : (PureU1 (2 * n + 1)).LinSols) : Prop
```

**`PureU1.Odd.lineInCubic_expand`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L45).

> The condition that a linear solution sits on a line between the two planes
> within the cubic expands into a on `accCubeTriLinSymm` applied to the points
> within the planes.

```lean
lemma lineInCubic_expand {S : (PureU1 (2 * n + 1)).LinSols} (h : LineInCubic S) :
    ∀ (g : Fin n → ℚ) (f : Fin n → ℚ)
      (_ : S.val = Unshifted.planeCharges g + Shifted.planeCharges f)
      (a b : ℚ),
    3 * a * b *
      (a * accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
          (Shifted.planeCharges f) +
        b * accCubeTriLinSymm (Shifted.planeCharges f) (Shifted.planeCharges f)
          (Unshifted.planeCharges g)) = 0
```

**`PureU1.Odd.line_in_cubic_P_P_P!`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L67).

```lean
lemma line_in_cubic_P_P_P! {S : (PureU1 (2 * n + 1)).LinSols} (h : LineInCubic S) :
    ∀ (g : Fin n → ℚ) (f : Fin n → ℚ)
      (_ : S.val = Unshifted.planeCharges g + Shifted.planeCharges f),
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.planeCharges f) = 0
```

**`PureU1.Odd.LineInCubicPerm`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L77).

> A `LinSol` satisfies `lineInCubicPerm` if all its permutations satisfy `lineInCubic`.

```lean
def LineInCubicPerm (S : (PureU1 (2 * n + 1)).LinSols) : Prop
```

**`PureU1.Odd.lineInCubicPerm_self`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L82).

> If `lineInCubicPerm S`, then `lineInCubic S`.

```lean
lemma lineInCubicPerm_self {S : (PureU1 (2 * n + 1)).LinSols} (hS : LineInCubicPerm S) :
    LineInCubic S
```

**`PureU1.Odd.lineInCubicPerm_permute`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L86).

> If `lineInCubicPerm S`, then `lineInCubicPerm (M S)` for all permutations `M`.

```lean
lemma lineInCubicPerm_permute {S : (PureU1 (2 * n + 1)).LinSols}
    (hS : LineInCubicPerm S) (M' : (FamilyPermutations (2 * n + 1)).group) :
    LineInCubicPerm ((FamilyPermutations (2 * n + 1)).linSolRep M' S)
```

**`PureU1.Odd.lineInCubicPerm_swap`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L92).

```lean
lemma lineInCubicPerm_swap {S : (PureU1 (2 * n.succ + 1)).LinSols}
    (LIC : LineInCubicPerm S) :
    ∀ (j : Fin n.succ) (g f : Fin n.succ → ℚ) (_ : S.val = Pa g f),
      (S.val (oddShiftSnd j) - S.val (oddShiftFst j))
      * accCubeTriLinSymm
        (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.basisAsCharges j) = 0
```

**`PureU1.Odd.P_P_P!_accCube'`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L107).

```lean
lemma P_P_P!_accCube' {S : (PureU1 (2 * n.succ.succ + 1)).LinSols}
    (f g : Fin n.succ.succ → ℚ) (hS : S.val = Pa f g) :
    accCubeTriLinSymm (Unshifted.planeCharges f) (Unshifted.planeCharges f)
      (Shifted.basisAsCharges 0) =
    (S.val (oddShiftFst 0) + S.val (oddShiftSnd 0)) *
    (2 * S.val oddShiftZero + S.val (oddShiftFst 0) + S.val (oddShiftSnd 0))
```

**`PureU1.Odd.lineInCubicPerm_last_cond`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L129).

```lean
lemma lineInCubicPerm_last_cond {S : (PureU1 (2 * n.succ.succ+1)).LinSols}
    (LIC : LineInCubicPerm S) :
    LineInPlaneProp ((S.val (oddShiftSnd 0)), ((S.val (oddShiftFst 0)), (S.val oddShiftZero)))
```

**`PureU1.Odd.lineInCubicPerm_last_perm`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L141).

```lean
lemma lineInCubicPerm_last_perm {S : (PureU1 (2 * n.succ.succ + 1)).LinSols}
    (LIC : LineInCubicPerm S) : LineInPlaneCond S
```

**`PureU1.Odd.lineInCubicPerm_constAbs`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L147).

```lean
lemma lineInCubicPerm_constAbs {S : (PureU1 (2 * n.succ.succ + 1)).LinSols}
    (LIC : LineInCubicPerm S) : ConstAbs S.val
```

**`PureU1.Odd.lineInCubicPerm_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean#L151).

```lean
lemma lineInCubicPerm_zero {S : (PureU1 (2 * n.succ.succ + 1)).LinSols}
    (LIC : LineInCubicPerm S) : S = 0
```

## Depends on

- [Line in plane condition](anomalycancellation-lineinplanecond.md)
- [Splitting the linear solutions in the odd case into two ACC-satisfying planes](anomalycancellation-odd-basislinear.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/LineInCubic.lean)
