---
declaration: section
origin: cited
lean: AlgebraicGeometry.finiteEtalePushoutRestriction_isEquivalence, AlgebraicGeometry.finiteEtalePushoutEquivalence, AlgebraicGeometry.finiteEtalePushoutEquivalence_functor
statement: formalized
proof: formalized
---

# 58.18 Pushouts and fundamental groups

Section 58.18 of the Stacks Project, [Tag 0EK3](https://stacks.math.columbia.edu/tag/0EK3). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EK4, a lemma

[Tag 0EK4](https://stacks.math.columbia.edu/tag/0EK4) in the Stacks Project.

**`AlgebraicGeometry.finiteEtalePushoutRestriction_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean, line 878](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean#L878). The attribute's comment: “the restriction functor is an equivalence”.

> **Stacks Project, Tag 0EK4.**  The restriction functor
> `FÉt_{Y ⨿_Z X} ⟶ FÉt_Y ×_{FÉt_Z} FÉt_X` is an equivalence of categories.  Composed with the
> pushout of finite étale cartesian triples, which is an equivalence by
> [Stacks Project, Tag 0ECL], it is reading a triple in the 2-fibre product, which is an
> equivalence; so it is one itself.

```lean
instance finiteEtalePushoutRestriction_isEquivalence
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    (finiteEtalePushoutRestriction s).IsEquivalence
```

**`AlgebraicGeometry.finiteEtalePushoutEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean, line 894](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean#L894).

> **Stacks Project, Tag 0EK4.**  In the pushout situation of [Stacks Project, Tag 0ECI] — for
> example when `Z ⟶ Y` and `Z ⟶ X` are closed immersions of schemes — there is an equivalence of
> categories
> `FÉt_{Y ⨿_Z X} ⟶ FÉt_Y ×_{FÉt_Z} FÉt_X`.
> Its functor is `AlgebraicGeometry.finiteEtalePushoutRestriction`, which sends a finite étale
> cover of the pushout to its base changes to `Y` and to `X` together with the canonical
> identification of their restrictions to `Z`.

```lean
noncomputable def finiteEtalePushoutEquivalence
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    FiniteEtaleOver (pushoutScheme s) ≌
      CategoricalPullback (finiteEtaleBaseChange s.j) (finiteEtaleBaseChange s.i)
```

**`AlgebraicGeometry.finiteEtalePushoutEquivalence_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean, line 902](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtalePushout.lean#L902). The attribute's comment: “the comparison functor”.

> The equivalence of [Stacks Project, Tag 0EK4] is the restriction functor.

```lean
theorem finiteEtalePushoutEquivalence_functor
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    (finiteEtalePushoutEquivalence s).functor = finiteEtalePushoutRestriction s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.18, Tag 0EK3](https://stacks.math.columbia.edu/tag/0EK3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
