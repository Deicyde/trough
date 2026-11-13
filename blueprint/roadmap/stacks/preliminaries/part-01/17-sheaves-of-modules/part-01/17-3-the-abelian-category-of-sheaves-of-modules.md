---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.exact_iff_stalkShortComplex_exact, SheafOfModules.instAbelian, AlgebraicGeometry.SheafOfModules.isColimit_colimitSheafificationCocone, AlgebraicGeometry.SheafOfModules.stalkFunctor_preservesColimits, AlgebraicGeometry.SheafOfModules.ab5OfSize, AlgebraicGeometry.SheafOfModules.forget_preservesFiniteBiproducts, SheafOfModules.instHasColimitsOfSizeOfPresheafOfModulesObjFunctorOppositeRingCatIsSheaf, SheafOfModules.hasLimitsOfSize
statement: formalized
proof: formalized
---

# 17.3 The abelian category of sheaves of modules

Section 17.3 of the Stacks Project, [Tag 01AF](https://stacks.math.columbia.edu/tag/01AF). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01AG, a lemma

[Tag 01AG](https://stacks.math.columbia.edu/tag/01AG) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.exact_iff_stalkShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Exactness.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Exactness.lean#L77). The attribute's comment: “exactness on stalks”.

> A complex of sheaves of modules is exact at its middle term if and only
> if the corresponding complex of stalks is exact at every point.

```lean
theorem exact_iff_stalkShortComplex_exact
    (S : ShortComplex (_root_.SheafOfModules.{u} 𝒪)) :
    S.Exact ↔ ∀ x : X, (stalkShortComplex 𝒪 S x).Exact
```

Declarations registered for the tag:

- [`SheafOfModules.instAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instAbelian#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Exactness.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Exactness.lean#L42) (StacksFrontier): “the category of sheaves of modules is abelian”. References: SGA 3 I (3.1.1), “more general”; SGA 3 I (4.7.1.1), “more general”; SGA 4 II (6.7); SGA 4 IV (11.1.2), “partial”; SGA 4 Vbis (2.4.0), “The fibers of Mod(E°”; SGA 4 XVII (2.2.6), “partial”; SGA 6 I (1.3), “partial”.

## Tag 01AH, a lemma

[Tag 01AH](https://stacks.math.columbia.edu/tag/01AH) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.isColimit_colimitSheafificationCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Colimits.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Colimits.lean#L112). The attribute's comment: “colimits\_sheafification”.

> Sheafification of a colimit of the underlying presheaves of modules is a
> colimit of the original diagram of sheaves of modules.

```lean
theorem isColimit_colimitSheafificationCocone
    (D : K ⥤ _root_.SheafOfModules.{v} R)
    (c : Cocone (D ⋙ _root_.SheafOfModules.forget R)) (hc : IsColimit c) :
    Nonempty (IsColimit (colimitSheafificationCocone R D c))
```

**`AlgebraicGeometry.SheafOfModules.stalkFunctor_preservesColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Colimits.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Colimits.lean#L260). The attribute's comment: “colimits\_stalks”. References: EGA 0 (4.3.2), “special case”.

> The canonical map from the colimit of the stalks of a diagram of sheaves
> of modules to the stalk of its colimit is an isomorphism. It is the inverse of
> `CategoryTheory.Limits.preservesColimitIso`; its compatibility with the colimit
> inclusions is `CategoryTheory.Limits.ι_preservesColimitIso_inv`.

```lean
lemma stalkFunctor_preservesColimits : PreservesColimits (stalkFunctor O x)
```

**`AlgebraicGeometry.SheafOfModules.ab5OfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean#L63). The attribute's comment: “part (3): filtered colimits are exact”. References: SGA 4 II (6.7), “special case”.

> Filtered colimits of sheaves of modules on a topological space are exact.

```lean
theorem ab5OfSize : AB5OfSize.{u, u} (_root_.SheafOfModules.{u} O)
```

**`AlgebraicGeometry.SheafOfModules.forget_preservesFiniteBiproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean#L69). The attribute's comment: “part (4): finite direct sums are the finite direct sums of presheaves”.

> Finite direct sums of sheaves of modules are the finite direct sums of the underlying
> presheaves of modules: forgetting the sheaf condition preserves finite biproducts.

```lean
theorem forget_preservesFiniteBiproducts :
    PreservesFiniteBiproducts
      (_root_.SheafOfModules.forget O : _root_.SheafOfModules.{u} O ⥤ _)
```

Declarations registered for the tag:

- [`SheafOfModules.instHasColimitsOfSizeOfPresheafOfModulesObjFunctorOppositeRingCatIsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instHasColimitsOfSizeOfPresheafOfModulesObjFunctorOppositeRingCatIsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Colimits.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Colimits.lean#L79) (StacksFrontier): “colimits\_exist”.
- [`SheafOfModules.hasLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.hasLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean#L50) (StacksFrontier): “part (1): all limits exist”.
- [`SheafOfModules.forgetPreservesLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.forgetPreservesLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean#L51) (StacksFrontier): “part (1): limits are the limits of the underlying presheaves of modules”.
- [`SheafOfModules.evaluationPreservesLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.evaluationPreservesLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/LimitsAndDirectSums.lean#L53) (StacksFrontier): “part (1): limits commute with taking sections over opens”.

## Tag 01AJ, a lemma

[Tag 01AJ](https://stacks.math.columbia.edu/tag/01AJ) in the Stacks Project.

**`RingedSpaceModuleAdjunction.preservesLimits_modulePushforward`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean#L41). The attribute's comment: “(1)”. References: SGA 4 IV (13.6), “ringed spaces, u\_*”.

> Pushforward of sheaves of modules along a morphism of ringed spaces commutes with all
> limits.

```lean
public lemma preservesLimits_modulePushforward {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) :
    PreservesLimitsOfSize.{u, u} (modulePushforward f)
```

**`RingedSpaceModuleAdjunction.exactFunctor_sheafPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean#L47). The attribute's comment: “(3)”.

> The inverse image of sheaves of abelian groups along a continuous map is exact.

```lean
public lemma exactFunctor_sheafPullback {Xt Yt : TopCat.{u}} (g : Xt ⟶ Yt) :
    exactFunctor (TopCat.Sheaf AddCommGrpCat.{u} Yt) (TopCat.Sheaf AddCommGrpCat.{u} Xt)
      (TopCat.Sheaf.pullback AddCommGrpCat.{u} g)
```

Declarations registered for the tag:

- [`RingedSpaceModuleAdjunction.preservesColimits_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetPullbackRightExact.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/ExactnessOfPushforwardAndPullback.lean#L55) (StacksFrontier): “(2)”.

## Tag 01AK, a lemma

[Tag 01AK](https://stacks.math.columbia.edu/tag/01AK) in the Stacks Project.

**`ExtensionByZero.jExt_exactFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroExact.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroExact.lean#L99).

> **Stacks 01AK.** Extension by zero along the inclusion of an open subspace is an exact
> functor on sheaves of abelian groups.

```lean
theorem jExt_exactFunctor {X : TopCat.{u}} (U : Opens X) :
    exactFunctor
      (TopCat.Sheaf AddCommGrpCat.{u} (Usp U))
      (TopCat.Sheaf AddCommGrpCat.{u} X)
      (jExt U)
```

## Tag 01AI, a lemma

[Tag 01AI](https://stacks.math.columbia.edu/tag/01AI) in the Stacks Project.

**`Stacks.SheafOfModules.preservesCoproducts_evaluation_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasiCompactCoproductSections.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasiCompactCoproductSections.lean#L86).

> **Stacks Project, Tag 01AI.** On a quasi-compact open subset, taking sections commutes
> with direct sums of sheaves of modules.

```lean
theorem preservesCoproducts_evaluation_of_isCompact
    (U : Opens X) (hU : IsCompact (U : Set X)) :
    PreservesColimitsOfShape (Discrete I)
      (_root_.SheafOfModules.evaluation.{w} R (op U))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.3, Tag 01AF](https://stacks.math.columbia.edu/tag/01AF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
