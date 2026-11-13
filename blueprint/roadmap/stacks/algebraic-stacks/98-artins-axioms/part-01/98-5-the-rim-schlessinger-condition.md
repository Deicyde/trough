---
declaration: section
origin: cited
lean: Deformation.Artin.SatisfiesRS, AlgebraicGeometry.Stack.ThickeningPushout.satisfiesRS, Deformation.Artin.satisfiesRS_of_isAlgebraicStack, Deformation.Artin.satisfiesRS_twoFibreProductOver
statement: formalized
proof: formalized
---

# 98.5 The Rim-Schlessinger condition

Section 98.5 of the Stacks Project, [Tag 06L9](https://stacks.math.columbia.edu/tag/06L9). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07WP, a definition

[Tag 07WP](https://stacks.math.columbia.edu/tag/07WP) in the Stacks Project.

**`Deformation.Artin.SatisfiesRS`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/ConditionRS.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/RimSchlessinger/ConditionRS.lean#L79).

> Condition (RS): restriction across a finite-type local Artinian pushout
> along a closed immersion is an equivalence onto the two-fibre product of fibres.

```lean
public abbrev SatisfiesRS (hp : p.IsFiberedInGroupoids) : Prop
```

## Tag 07WQ, a lemma

[Tag 07WQ](https://stacks.math.columbia.edu/tag/07WQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.ThickeningPushout.satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningPushoutEquivalence.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningPushoutEquivalence.lean#L87).

> **Stacks 07WQ.** An algebraic stack satisfies the Rim–Schlessinger condition (RS). The
> source states this over a locally Noetherian base; the hypothesis is not needed, since the proof
> is Stacks 07WN, which holds over any base.

```lean
theorem satisfiesRS.{w'} (𝒵 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (h𝒵 : IsAlgebraicStack.{u, w'} B S hS 𝒵) :
    Deformation.Artin.SatisfiesRS B S hS 𝒵.p (Classical.choose h𝒵)
```

**`Deformation.Artin.satisfiesRS_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/ArtinianAtlas.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/RimSchlessinger/ArtinianAtlas.lean#L221).

> **Stacks 07WQ: an algebraic stack satisfies condition (RS).** Let `𝒳` be an algebraic stack
> over `S`. At every pushout `Y' = Y ⨿_X X'` of spectra of Artinian local rings of finite type over
> `S` along a closed immersion `X ⟶ X'`, the comparison from the fibre over `Y'` to the two-fibre
> product of the fibres over `Y` and `X'` over the fibre over `X` is an equivalence.
>
> Full faithfulness comes from the representable diagonal alone
> (`Deformation.Artin.fullyFaithful_fiberSquareComparison_of_hasRepresentableDiagonal`). For
> essential surjectivity, a span of `𝒳` over the square has a cocone
> (`Deformation.Artin.nonempty_cocone_of_atlas_of_hasLiftsAlong`): its object over `Y` lifts along
> the smooth presentation `(Sch/U) ⟶ 𝒳` étale-locally, the étale neighbourhoods extend across the
> thickening `Y ⟶ Y'`, and over each of them the lift is carried across the base change of
> `X ⟶ X'`. That base change is a closed immersion with nilpotent kernel into an affine scheme
> étale, hence finite, over the Artinian local `X'`, and the presentation has lifts along it
> (`AlgebraicGeometry.Stack.hasLiftsAlong_of_isNilpotent`): it is formally smooth on objects
> against such test objects because a smooth morphism of algebraic spaces lifts over them
> (`AlgebraicGeometry.Space.formallySmoothOn_hasFiniteLocalNilpotentSections_of_isSmooth`).

```lean
theorem satisfiesRS_of_isAlgebraicStack (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    SatisfiesRS B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
```

## Tag 07WR, a lemma

[Tag 07WR](https://stacks.math.columbia.edu/tag/07WR) in the Stacks Project.

**`Deformation.Artin.satisfiesRS_twoFibreProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/RimSchlessinger.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ArtinCriteria/RimSchlessinger.lean#L1177).

> Condition (RS) is preserved by the two-fibre product of categories fibred in groupoids over
> the big fppf site.

```lean
public theorem satisfiesRS_twoFibreProductOver
    (p𝒳 : 𝒳 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (p𝒴 : 𝒴 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (p𝒵 : 𝒵 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (F : 𝒳 ⥤ 𝒴) (G : 𝒵 ⥤ 𝒴)
    (h𝒳 : p𝒳.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (h𝒵 : p𝒵.IsFiberedInGroupoids)
    (hF : F ⋙ p𝒴 = p𝒳) (hG : G ⋙ p𝒴 = p𝒵)
    (hRS𝒳 : Deformation.Artin.SatisfiesRS B S hS p𝒳 h𝒳)
    (hRS𝒴 : Deformation.Artin.SatisfiesRS B S hS p𝒴 h𝒴)
    (hRS𝒵 : Deformation.Artin.SatisfiesRS B S hS p𝒵 h𝒵) :
    Deformation.Artin.SatisfiesRS B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 F G)
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 F G
        h𝒳 h𝒵 h𝒴 hF hG)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.5, Tag 06L9](https://stacks.math.columbia.edu/tag/06L9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
