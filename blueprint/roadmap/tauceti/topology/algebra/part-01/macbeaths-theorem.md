---
declaration: def
origin: cited
lean: TauCeti.macbeathEquiv, TauCeti.ker_lift_eq_normalClosure_macbeathRels, TauCeti.ker_lift_eq_normalClosure_macbeathRels_of_locallyFinite, TauCeti.macbeathHom_injective_of_locallyFinite
statement: formalized
---

# Macbeath's theorem

If the translates of a path-connected open set `U` cover a simply
connected space `X`, then `G` is presented by the Macbeath generators and relations of `U`.

```lean
TauCeti.macbeathEquiv.{u_1, u_2} {G : Type u_1} {X : Type u_2} [Group G] [MulAction G X] {U : Set X}
  [TopologicalSpace X] [ContinuousConstSMul G X] [SimplyConnectedSpace X] (hUo : IsOpen U)
  (hUc : IsPathConnected U) (hcover : ⋃ g, g • U = Set.univ) :
  PresentedGroup (TauCeti.macbeathRels G U) ≃* G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.macbeathEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/Macbeath/Basic.html#TauCeti.macbeathEquiv).

## Other forms

**Macbeath's theorem, as a description of the relations.** Formalized in Tau Ceti as [`TauCeti.ker_lift_eq_normalClosure_macbeathRels`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/Macbeath/Basic.html#TauCeti.ker_lift_eq_normalClosure_macbeathRels).

```lean
TauCeti.ker_lift_eq_normalClosure_macbeathRels.{u_1, u_2} {G : Type u_1} {X : Type u_2} [Group G]
  [MulAction G X] {U : Set X} [TopologicalSpace X] [ContinuousConstSMul G X]
  [SimplyConnectedSpace X] (hUo : IsOpen U) (hUc : IsPathConnected U)
  (hcover : ⋃ g, g • U = Set.univ) :
  (FreeGroup.lift Subtype.val).ker = Subgroup.normalClosure (TauCeti.macbeathRels G U)
```

**Macbeath's theorem for a tile, as a description of the relations.** Formalized in Tau Ceti as [`TauCeti.ker_lift_eq_normalClosure_macbeathRels_of_locallyFinite`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/Macbeath/LocallyFinite.html#TauCeti.ker_lift_eq_normalClosure_macbeathRels_of_locallyFinite).

```lean
TauCeti.ker_lift_eq_normalClosure_macbeathRels_of_locallyFinite.{u_1, u_2} {G : Type u_1}
  {X : Type u_2} [Group G] [MulAction G X] [PseudoMetricSpace X] [IsIsometricSMul G X] {P : Set X}
  [LocallyPathConnectedSpace X] [SimplyConnectedSpace X] (hPc : IsClosed P) (hP : IsConnected P)
  (hlf : LocallyFinite fun g => g • P) (hcover : ⋃ g, g • P = Set.univ) :
  (FreeGroup.lift Subtype.val).ker = Subgroup.normalClosure (TauCeti.macbeathRels G P)
```

**Macbeath's theorem for a tile.** Formalized in Tau Ceti as [`TauCeti.macbeathHom_injective_of_locallyFinite`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/Macbeath/LocallyFinite.html#TauCeti.macbeathHom_injective_of_locallyFinite).

```lean
TauCeti.macbeathHom_injective_of_locallyFinite.{u_1, u_2} {G : Type u_1} {X : Type u_2} [Group G]
  [MulAction G X] [PseudoMetricSpace X] [IsIsometricSMul G X] {P : Set X}
  [LocallyPathConnectedSpace X] [SimplyConnectedSpace X] (hPc : IsClosed P) (hP : IsConnected P)
  (hlf : LocallyFinite fun g => g • P) (hcover : ⋃ g, g • P = Set.univ) :
  Function.Injective ⇑(TauCeti.macbeathHom G P)
```

## Sources

- [Tau Ceti documentation: `TauCeti.macbeathEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/Macbeath/Basic.html#TauCeti.macbeathEquiv)
- [Source of `TauCeti.macbeathEquiv` in TauCeti/Topology/Algebra/GroupAction/Macbeath/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/GroupAction/Macbeath/Basic.lean#L408)
