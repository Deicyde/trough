---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: CircleDeg1Lift.semiconj_of_group_action_of_forall_translationNumber_eq
mathlib_file: Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean
---

# Translation numbers define a group action up to semiconjugacy

Consider two actions `f₁ f₂ : G →* CircleDeg1Lift` of a group on the real line by lifts of
orientation-preserving circle homeomorphisms. Suppose that for each `g : G` the homeomorphisms
`f₁ g` and `f₂ g` have equal rotation numbers. Then there exists `F : CircleDeg1Lift` such that
`F * f₁ g = f₂ g * F` for all `g : G`.

This is a version of Proposition 5.4 from [Étienne Ghys, Groupes d'homéomorphismes du cercle et
cohomologie bornée][ghys87:groupes].

```lean
CircleDeg1Lift.semiconj_of_group_action_of_forall_translationNumber_eq.{u_1} {G : Type u_1}
  [Group G] (f₁ f₂ : G →* CircleDeg1Lift)
  (h : ∀ (g : G), (f₁ g).translationNumber = (f₂ g).translationNumber) :
  ∃ F, ∀ (g : G), Function.Semiconj ⇑F ⇑(f₁ g) ⇑(f₂ g)
```

## Depends on

- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Group morphism](../../general-algebra/group-theory/part-01/group-morphism.md)
- [Translation number](translation-number.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `CircleDeg1Lift.semiconj_of_group_action_of_forall_translationNumber_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html#CircleDeg1Lift.semiconj_of_group_action_of_forall_translationNumber_eq)
- [Source of `CircleDeg1Lift.semiconj_of_group_action_of_forall_translationNumber_eq` in Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean#L825)
- [Mathlib overview: Dynamics › Circle dynamics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L558)
