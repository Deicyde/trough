---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtalePushforwardFullyFaithful_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforward_essImage_iff_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforwardCompInverseImageIso_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforwardAbFullyFaithful_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforwardAbCompPullbackIso_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective', Stacks.EtaleCohomology.smallEtalePushforwardAb_essImage_iff_support_of_integral_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforward_fullyFaithful_essImage_leftInverse_of_integral_universallyInjective
statement: formalized
proof: formalized
---

# 59.47 Integral universally injective morphisms

Section 59.47 of the Stacks Project, [Tag 04FY](https://stacks.math.columbia.edu/tag/04FY). 1 tag here is carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04FZ, a proposition

[Tag 04FZ](https://stacks.math.columbia.edu/tag/04FZ) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforwardFullyFaithful_of_integral_universallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean#L172). The attribute's comment: “part (1): fully faithful”.

> **Stacks 04FZ, part (1).** Direct image of sheaves of sets along an integral universally
> injective morphism is fully faithful.

```lean
public def smallEtalePushforwardFullyFaithful_of_integral_universallyInjective :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
      (smallEtaleTopology Y) (smallEtaleTopology X)).FullyFaithful
```

**`Stacks.EtaleCohomology.smallEtalePushforward_essImage_iff_of_integral_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean#L187). The attribute's comment: “part (1): essential image”.

> **Stacks 04FZ, part (1).** A sheaf of sets on `Y_étale` lies in the essential image of direct
> image along an integral universally injective morphism exactly when its restriction to the open
> complement of `f(X)` is the singleton sheaf.

```lean
public theorem smallEtalePushforward_essImage_iff_of_integral_universallyInjective
    (F : Sheaf (smallEtaleTopology Y) (Type (max (u + 1) v))) :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
        (smallEtaleTopology Y) (smallEtaleTopology X)).essImage F ↔
      Nonempty (IsTerminal
        ((smallEtaleInverseImage.{u, v} (openComplementRange f).ι).obj F))
```

**`Stacks.EtaleCohomology.smallEtalePushforwardCompInverseImageIso_of_integral_universallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean#L201). The attribute's comment: “trailing clause for sheaves of sets: left inverse”.

> **Stacks 04FZ, trailing clause.** Inverse image along an integral universally injective
> morphism is a left inverse to direct image on sheaves of sets.

```lean
public def smallEtalePushforwardCompInverseImageIso_of_integral_universallyInjective :
    (smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
        (smallEtaleTopology Y) (smallEtaleTopology X) ⋙
      smallEtaleInverseImage.{u, v} f ≅
      𝟭 (Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAbFullyFaithful_of_integral_universallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean#L239). The attribute's comment: “part (2): fully faithful”.

> **Stacks 04FZ, part (2).** Direct image of abelian sheaves along an integral universally
> injective morphism is fully faithful.

```lean
public def smallEtalePushforwardAbFullyFaithful_of_integral_universallyInjective :
    (smallEtalePushforwardAb f).FullyFaithful
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAbCompPullbackIso_of_integral_universallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforward.lean#L280). The attribute's comment: “trailing clause for abelian sheaves: left inverse”.

> **Stacks 04FZ, trailing clause.** Inverse image along an integral universally injective
> morphism is a left inverse to direct image on abelian sheaves.

```lean
public def smallEtalePushforwardAbCompPullbackIso_of_integral_universallyInjective :
    smallEtalePushforwardAb f ⋙ (smallEtaleBaseChange f).sheafPullback Ab.{u + 1}
        (smallEtaleTopology Y) (smallEtaleTopology X) ≅
      𝟭 (Sheaf (smallEtaleTopology X) Ab.{u + 1})
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean#L144). The attribute's comment: “part (2): essential image, as vanishing of the restriction away from f(X)”.

> An abelian sheaf on `Y_étale` lies in the essential image of direct image along an integral
> universally injective morphism exactly when its restriction to the open complement of `f(X)`
> vanishes.

```lean
public theorem smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective'
    (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}) :
    (smallEtalePushforwardAb f).essImage F ↔
      IsZero (((smallEtaleBaseChange (openComplementRange f).ι).sheafPullback Ab.{u + 1}
        (smallEtaleTopology Y)
        (smallEtaleTopology (openComplementRange f).toScheme)).obj F)
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_essImage_iff_support_of_integral_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean#L156). The attribute's comment: “part (2): essential image”.

> An abelian sheaf on `Y_étale` is a direct image along an integral universally injective
> morphism exactly when its support is contained in `f(X)`.

```lean
public theorem smallEtalePushforwardAb_essImage_iff_support_of_integral_universallyInjective
    (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}) :
    (smallEtalePushforwardAb f).essImage F ↔ smallEtaleSupportAb F ⊆ Set.range f.base
```

**`Stacks.EtaleCohomology.smallEtalePushforward_fullyFaithful_essImage_leftInverse_of_integral_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean#L179).

> Let `f : X ⟶ Y` be a morphism of schemes which is integral and universally injective.
> Then (1) `f_{small, *} : Sh(X_étale) ⟶ Sh(Y_étale)` is fully faithful and its essential image is
> those sheaves of sets on `Y_étale` whose restriction to `Y \ f(X)` is isomorphic to `*`, and (2)
> `f_{small, *} : Ab(X_étale) ⟶ Ab(Y_étale)` is fully faithful and its essential image is those
> abelian sheaves on `Y_étale` whose support is contained in `f(X)`; and in both cases
> `f_{small}^{-1}` is a left inverse to `f_{small, *}`.
>
> The four conjuncts are, in order: part (1), part (2), and the trailing clause for each of the
> two sheaf categories. The complement `Y \ f(X)` is the open subscheme `openComplementRange f`,
> open because an integral morphism is universally closed; being isomorphic to `*` is being a
> terminal object of the category of sheaves of sets on that complement; and the support of an
> abelian sheaf is `smallEtaleSupportAb`, the set of points of `Y` at which some geometric stalk
> of the sheaf is nonzero.

```lean
public theorem
    smallEtalePushforward_fullyFaithful_essImage_leftInverse_of_integral_universallyInjective :
    (((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
          (smallEtaleTopology Y) (smallEtaleTopology X)).Full ∧
        ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
          (smallEtaleTopology Y) (smallEtaleTopology X)).Faithful ∧
        ∀ F : Sheaf (smallEtaleTopology Y) (Type (max (u + 1) v)),
          ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
              (smallEtaleTopology Y) (smallEtaleTopology X)).essImage F ↔
            Nonempty (IsTerminal
              ((smallEtaleInverseImage.{u, v} (openComplementRange f).ι).obj F))) ∧
      ((smallEtalePushforwardAb f).Full ∧ (smallEtalePushforwardAb f).Faithful ∧
        ∀ F : Sheaf (smallEtaleTopology Y) Ab.{u + 1},
          (smallEtalePushforwardAb f).essImage F ↔
            smallEtaleSupportAb F ⊆ Set.range f.base) ∧
      Nonempty ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
            (smallEtaleTopology Y) (smallEtaleTopology X) ⋙
          smallEtaleInverseImage.{u, v} f ≅
            𝟭 (Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))) ∧
      Nonempty (smallEtalePushforwardAb f ⋙ (smallEtaleBaseChange f).sheafPullback Ab.{u + 1}
            (smallEtaleTopology Y) (smallEtaleTopology X) ≅
          𝟭 (Sheaf (smallEtaleTopology X) Ab.{u + 1}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.47, Tag 04FY](https://stacks.math.columbia.edu/tag/04FY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
