---
declaration: module
origin: cited
lean: PureU1.Even.LineInCubic, PureU1.Even.lineInCubic_expand, PureU1.Even.line_in_cubic_unshifted_unshifted_shifted, PureU1.Even.LineInCubicPerm, PureU1.Even.lineInCubicPerm_self, PureU1.Even.lineInCubicPerm_permute, PureU1.Even.lineInCubicPerm_swap, PureU1.Even.unshifted_unshifted_shifted_accCube'
statement: formalized
proof: formalized
---

# Line In Cubic Even case

The module `Physlib.QFT.QED.AnomalyCancellation.Even.LineInCubic`, [Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean): 13 declarations, 5 with a docstring.

> We say that a linear solution satisfies the `lineInCubic` property
> if the line through that point and through the two different planes formed by the basis of
> `LinSols` lies in the cubic.
>
> We show that for a solution all its permutations satisfy this property, then there exists
> a permutation for which it lies in the unshifted plane.

## References

> * The main reference for this file is https://arxiv.org/pdf/1912.04804.pdf. [ref: arxiv\_1912\_04804]

**`PureU1.Even.LineInCubic`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L38).

> A property on `LinSols`, satisfied if every point on the line between the two planes
> in the basis through that point is in the cubic.

```lean
def LineInCubic (S : (PureU1 (2 * n.succ)).LinSols) : Prop
```

**`PureU1.Even.lineInCubic_expand`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L43).

```lean
lemma lineInCubic_expand {S : (PureU1 (2 * n.succ)).LinSols} (h : LineInCubic S) :
    ∀ (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (_ : S.val = Pa g f) (a b : ℚ),
    3 * a * b *
      (a * accCubeTriLinSymm (Unshifted.planeCharges g)
          (Unshifted.planeCharges g) (Shifted.planeCharges f) +
        b * accCubeTriLinSymm (Shifted.planeCharges f)
          (Shifted.planeCharges f) (Unshifted.planeCharges g)) = 0
```

**`PureU1.Even.line_in_cubic_unshifted_unshifted_shifted`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L72).

> This lemma states that for a given `S` of type `(PureU1 (2 * n.succ)).AnomalyFreeLinear` and
> a proof `h` that the line through `S` lies on a cubic curve,
> for any functions `g : Fin n.succ → ℚ` and `f : Fin n → ℚ`, if
> `S.val = Unshifted.planeCharges g + Shifted.planeCharges f`,
> then
> `accCubeTriLinSymm.toFun (Unshifted.planeCharges g, Unshifted.planeCharges g,
>   Shifted.planeCharges f) = 0`.

```lean
lemma line_in_cubic_unshifted_unshifted_shifted
    {S : (PureU1 (2 * n.succ)).LinSols} (h : LineInCubic S) :
    ∀ (g : Fin n.succ → ℚ) (f : Fin n → ℚ)
      (_ : S.val = Unshifted.planeCharges g + Shifted.planeCharges f),
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.planeCharges f) = 0
```

**`PureU1.Even.LineInCubicPerm`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L83).

> A `LinSol` satisfies `LineInCubicPerm` if all its permutations satisfy `lineInCubic`.

```lean
def LineInCubicPerm (S : (PureU1 (2 * n.succ)).LinSols) : Prop
```

**`PureU1.Even.lineInCubicPerm_self`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L88).

> If `lineInCubicPerm S` then `lineInCubic S`.

```lean
lemma lineInCubicPerm_self {S : (PureU1 (2 * n.succ)).LinSols}
    (hS : LineInCubicPerm S) : LineInCubic S
```

**`PureU1.Even.lineInCubicPerm_permute`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L92).

> If `lineInCubicPerm S` then `lineInCubicPerm (M S)` for all permutations `M`.

```lean
lemma lineInCubicPerm_permute {S : (PureU1 (2 * n.succ)).LinSols}
    (hS : LineInCubicPerm S) (M' : (FamilyPermutations (2 * n.succ)).group) :
    LineInCubicPerm ((FamilyPermutations (2 * n.succ)).linSolRep M' S)
```

**`PureU1.Even.lineInCubicPerm_swap`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L101).

```lean
lemma lineInCubicPerm_swap {S : (PureU1 (2 * n.succ)).LinSols}
    (LIC : LineInCubicPerm S) :
    ∀ (j : Fin n) (g : Fin n.succ → ℚ) (f : Fin n → ℚ) (_ : S.val = Pa g f),
      (S.val (evenShiftSnd j) - S.val (evenShiftFst j))
      * accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
        (Shifted.basisAsCharges j) = 0
```

**`PureU1.Even.unshifted_unshifted_shifted_accCube'`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L116).

```lean
lemma unshifted_unshifted_shifted_accCube' {S : (PureU1 (2 * n.succ.succ)).LinSols}
    (f : Fin n.succ.succ → ℚ) (g : Fin n.succ → ℚ) (hS : S.val = Pa f g) :
    accCubeTriLinSymm (Unshifted.planeCharges f) (Unshifted.planeCharges f)
      (Shifted.basisAsCharges (Fin.last n)) =
    - (S.val (evenShiftSnd (Fin.last n)) + S.val (evenShiftFst (Fin.last n))) *
    (2 * S.val evenShiftLast +
    S.val (evenShiftSnd (Fin.last n)) + S.val (evenShiftFst (Fin.last n)))
```

**`PureU1.Even.lineInCubicPerm_last_cond`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L127).

```lean
lemma lineInCubicPerm_last_cond {S : (PureU1 (2 * n.succ.succ)).LinSols}
    (LIC : LineInCubicPerm S) :
    LineInPlaneProp
    ((S.val (evenShiftSnd (Fin.last n))), ((S.val (evenShiftFst (Fin.last n))),
      (S.val evenShiftLast)))
```

**`PureU1.Even.lineInCubicPerm_last_perm`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L141).

```lean
lemma lineInCubicPerm_last_perm {S : (PureU1 (2 * n.succ.succ)).LinSols}
    (LIC : LineInCubicPerm S) : LineInPlaneCond S
```

**`PureU1.Even.lineInCubicPerm_constAbs`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L152).

```lean
lemma lineInCubicPerm_constAbs {S : (PureU1 (2 * n.succ.succ)).Sols}
    (LIC : LineInCubicPerm S.1.1) : ConstAbs S.val
```

**`PureU1.Even.lineInCubicPerm_vectorLike`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L156).

```lean
lemma lineInCubicPerm_vectorLike {S : (PureU1 (2 * n.succ.succ)).Sols}
    (LIC : LineInCubicPerm S.1.1) : VectorLikeEven S.val
```

**`PureU1.Even.lineInCubicPerm_in_plane`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean#L160).

```lean
lemma lineInCubicPerm_in_plane (S : (PureU1 (2 * n.succ.succ)).Sols)
    (LIC : LineInCubicPerm S.1.1) : ∃ (M : (FamilyPermutations (2 * n.succ.succ)).group),
    (FamilyPermutations (2 * n.succ.succ)).linSolRep M S.1.1
    ∈ Submodule.span ℚ (Set.range Unshifted.basis)
```

## Depends on

- [Splitting the linear solutions in the even case into two ACC-satisfying planes](anomalycancellation-even-basislinear.md)
- [Line in plane condition](anomalycancellation-lineinplanecond.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/LineInCubic.lean)
