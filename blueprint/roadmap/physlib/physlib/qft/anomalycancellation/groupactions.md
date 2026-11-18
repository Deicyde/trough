---
declaration: module
origin: cited
lean: ACCSystemGroupAction, ACCSystemGroupAction.linSolMap, ACCSystemGroupAction.linSolRep, ACCSystemGroupAction.rep_linSolRep_commute, ACCSystemGroupAction.quadSolAction, ACCSystemGroupAction.linSolRep_quadSolAction_commute, ACCSystemGroupAction.rep_quadSolAction_commute, ACCSystemGroupAction.solAction
statement: formalized
proof: formalized
---

# Group actions on ACC systems.

The module `Physlib.QFT.AnomalyCancellation.GroupActions`, [Physlib/QFT/AnomalyCancellation/GroupActions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean): 12 declarations (1 instance with no name), 7 with a docstring.

> We define a group action on an ACC system as a representation on the vector spaces of charges
> under which the anomaly equations are invariant.
>
> From this we define
> - The representation acting on the vector space of solutions to the linear ACCs.
> - The group action acting on solutions to the linear + quadratic equations.
> - The group action acting on solutions to the anomaly cancellation conditions.

**`ACCSystemGroupAction`**, a structure, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L28).

> The type of a group action on a system of charges is defined as a representation on
> the vector spaces of charges under which the anomaly equations are invariant.

```lean
structure ACCSystemGroupAction (χ : ACCSystem) where
  /-- The underlying type of the group. -/
  group : Type
  /-- An instance given the `group` component the structure of a `Group`. -/
  groupInst : Group group
  /-- The representation of group acting on the vector space of charges. -/
  rep : Representation ℚ group χ.Charges
  /-- The invariance of the linear ACCs under the group action. -/
  linearInvariant : ∀ i g S, χ.linearACCs i (rep g S) = χ.linearACCs i S
  /-- The invariance of the quadratic ACCs under the group action. -/
  quadInvariant : ∀ i g S, (χ.quadraticACCs i) (rep g S) = (χ.quadraticACCs i) S
  /-- The invariance of the cubic ACC under the group action. -/
  cubicInvariant : ∀ g S, χ.cubicACC (rep g S) = χ.cubicACC S
```

**An instance with no name**, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L45).

> The given instance of a group on the `group` field of a `ACCSystemGroupAction`.

```lean
instance {χ : ACCSystem} (G : ACCSystemGroupAction χ) : Group G.group
```

**`ACCSystemGroupAction.linSolMap`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L48).

> The action of a group element on the vector space of linear solutions.

```lean
def linSolMap {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group) :
    χ.LinSols →ₗ[ℚ] χ.LinSols
```

**`ACCSystemGroupAction.linSolRep`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L58).

> The representation acting on the vector space of solutions to the linear ACCs.

```lean
def linSolRep {χ : ACCSystem} (G : ACCSystemGroupAction χ) :
    Representation ℚ G.group χ.LinSols
```

**`ACCSystemGroupAction.rep_linSolRep_commute`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L74).

> The representation on the charges and anomaly free solutions
> commutes with the inclusion.

```lean
lemma rep_linSolRep_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.LinSols) : χ.linSolsIncl (G.linSolRep g S) =
    G.rep g (χ.linSolsIncl S)
```

**`ACCSystemGroupAction.quadSolAction`**, an instance, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L80).

> A multiplicative action of `G.group` on `quadSols`.

```lean
instance quadSolAction {χ : ACCSystem} (G : ACCSystemGroupAction χ) :
    MulAction G.group χ.QuadSols
```

**`ACCSystemGroupAction.linSolRep_quadSolAction_commute`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L94).

```lean
lemma linSolRep_quadSolAction_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.QuadSols) : χ.quadSolsInclLinSols (G.quadSolAction.toFun _ _ S g) =
    G.linSolRep g (χ.quadSolsInclLinSols S)
```

**`ACCSystemGroupAction.rep_quadSolAction_commute`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L98).

```lean
lemma rep_quadSolAction_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.QuadSols) : χ.quadSolsIncl (G.quadSolAction.toFun _ _ S g) =
    G.rep g (χ.quadSolsIncl S)
```

**`ACCSystemGroupAction.solAction`**, an instance, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L103).

> The group action acting on solutions to the anomaly cancellation conditions.

```lean
instance solAction {χ : ACCSystem} (G : ACCSystemGroupAction χ) : MulAction G.group χ.Sols
```

**`ACCSystemGroupAction.quadSolAction_solAction_commute`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L119).

```lean
lemma quadSolAction_solAction_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.Sols) : χ.solsInclQuadSols (G.solAction.toFun _ _ S g) =
    G.quadSolAction.toFun _ _ (χ.solsInclQuadSols S) g
```

**`ACCSystemGroupAction.linSolRep_solAction_commute`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L123).

```lean
lemma linSolRep_solAction_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.Sols) : χ.solsInclLinSols (G.solAction.toFun _ _ S g) =
    G.linSolRep g (χ.solsInclLinSols S)
```

**`ACCSystemGroupAction.rep_solAction_commute`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean#L127).

```lean
lemma rep_solAction_commute {χ : ACCSystem} (G : ACCSystemGroupAction χ) (g : G.group)
    (S : χ.Sols) : χ.solsIncl (G.solAction.toFun _ _ S g) = G.rep g (χ.solsIncl S)
```

## Depends on

- [Anomaly cancellation conditions](basic.md)

## Sources

- [Physlib/QFT/AnomalyCancellation/GroupActions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/GroupActions.lean)
