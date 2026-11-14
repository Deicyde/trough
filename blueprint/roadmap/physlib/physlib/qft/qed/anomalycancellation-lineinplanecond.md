---
declaration: module
origin: cited
lean: PureU1.LineInPlaneProp, PureU1.LineInPlaneCond, PureU1.lineInPlaneCond_perm, PureU1.lineInPlaneCond_eq_last', PureU1.lineInPlaneCond_eq_last, PureU1.linesInPlane_eq_sq, PureU1.linesInPlane_constAbs, PureU1.linesInPlane_four
statement: formalized
proof: formalized
---

# Line in plane condition

The module `Physlib.QFT.QED.AnomalyCancellation.LineInPlaneCond`, [Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean): 11 declarations, 2 with a docstring.

> We say a `LinSol` satisfies the `line in plane` condition if for all distinct `i1`, `i2`, `i3` in
> `Fin n`, we have
> `S i1 = S i2` or `S i1 = - S i2` or `2 S i3 + S i1 + S i2 = 0`.
>
> We look at various consequences of this.
> The main reference for this material is
>
> - https://arxiv.org/pdf/1912.04804.pdf [ref: arxiv\_1912\_04804]
>
> We will show that `n ≥ 4` the `line in plane` condition on solutions implies the
> `constAbs` condition.

**`PureU1.LineInPlaneProp`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L35).

> The proposition on three rationals to satisfy the `linInPlane` condition.

```lean
def LineInPlaneProp : ℚ × ℚ × ℚ → Prop
```

**`PureU1.LineInPlaneCond`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L39).

> The proposition on a `LinSol` to satisfy the `linInPlane` condition.

```lean
def LineInPlaneCond (S : (PureU1 n).LinSols) : Prop
```

**`PureU1.lineInPlaneCond_perm`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L44).

```lean
lemma lineInPlaneCond_perm {S : (PureU1 n).LinSols} (hS : LineInPlaneCond S)
    (M : (FamilyPermutations n).group) :
    LineInPlaneCond ((FamilyPermutations n).linSolRep M S)
```

**`PureU1.lineInPlaneCond_eq_last'`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L53).

```lean
lemma lineInPlaneCond_eq_last' {S : (PureU1 (n.succ.succ)).LinSols} (hS : LineInPlaneCond S)
    (h : ¬ (S.val ((Fin.last n).castSucc))^2 = (S.val ((Fin.last n).succ))^2) :
    (2 - n) * S.val (Fin.last (n + 1)) =
    - (2 - n)* S.val (Fin.castSucc (Fin.last n))
```

**`PureU1.lineInPlaneCond_eq_last`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L81).

```lean
lemma lineInPlaneCond_eq_last {S : (PureU1 (n.succ.succ.succ.succ.succ)).LinSols}
    (hS : LineInPlaneCond S) : ConstAbsProp ((S.val ((Fin.last n.succ.succ.succ).castSucc)),
    (S.val ((Fin.last n.succ.succ.succ).succ)))
```

**`PureU1.linesInPlane_eq_sq`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L103).

```lean
lemma linesInPlane_eq_sq {S : (PureU1 (n.succ.succ.succ.succ.succ)).LinSols}
    (hS : LineInPlaneCond S) : ∀ (i j : Fin n.succ.succ.succ.succ.succ) (_ : i ≠ j),
    ConstAbsProp (S.val i, S.val j)
```

**`PureU1.linesInPlane_constAbs`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L112).

```lean
lemma linesInPlane_constAbs {S : (PureU1 (n.succ.succ.succ.succ.succ)).LinSols}
    (hS : LineInPlaneCond S) : ConstAbs S.val
```

**`PureU1.linesInPlane_four`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L119).

```lean
lemma linesInPlane_four (S : (PureU1 4).Sols) (hS : LineInPlaneCond S.1.1) :
    ConstAbsProp (S.val (0 : Fin 4), S.val (1 : Fin 4))
```

**`PureU1.linesInPlane_eq_sq_four`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L142).

```lean
lemma linesInPlane_eq_sq_four {S : (PureU1 4).Sols}
    (hS : LineInPlaneCond S.1.1) : ∀ (i j : Fin 4) (_ : i ≠ j),
    ConstAbsProp (S.val i, S.val j)
```

**`PureU1.linesInPlane_constAbs_four`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L150).

```lean
lemma linesInPlane_constAbs_four (S : (PureU1 4).Sols)
    (hS : LineInPlaneCond S.1.1) : ConstAbs S.val
```

**`PureU1.linesInPlane_constAbs_AF`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean#L157).

```lean
lemma linesInPlane_constAbs_AF (S : (PureU1 (n.succ.succ.succ.succ)).Sols)
    (hS : LineInPlaneCond S.1.1) : ConstAbs S.val
```

## Depends on

- [Charges assignments with constant abs](anomalycancellation-constabs.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LineInPlaneCond.lean)
