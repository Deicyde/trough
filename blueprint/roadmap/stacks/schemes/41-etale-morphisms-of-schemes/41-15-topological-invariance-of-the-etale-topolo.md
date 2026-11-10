---
declaration: section
origin: cited
lean: Stacks.Etale.bijective_pullbackHom_of_etale, Stacks.Etale.etalePullback_isEquivalence_of_surjective_isClosedImmersion
statement: formalized
proof: formalized
---

# 41.15 Topological invariance of the étale topology

Section 41.15 of the Stacks Project, [Tag 06NE](https://stacks.math.columbia.edu/tag/06NE). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025H, a theorem

[Tag 025H](https://stacks.math.columbia.edu/tag/025H) in the Stacks Project.

**`Stacks.Etale.bijective_pullbackHom_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/EtaleDescentIntegral.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/EtaleDescentIntegral.lean#L345). References: EGA IV (18.1.3); EGA IV (18.1.2), “fully faithful”; SGA 1 I (5.5); SGA 1 IX (1.7), “fully faithful”.

> Base change along a closed immersion with the same underlying space induces a bijection on
> morphisms into an étale scheme.

```lean
theorem bijective_pullbackHom_of_etale
    {S S₀ : Scheme.{u}} (i : S₀ ⟶ S) [IsClosedImmersion i]
    (hi : Function.Surjective i.base) (X Y : Over S) [Etale X.hom] :
    Function.Bijective (fun f : Y ⟶ X => (Over.pullback i).map f)
```

## Tag 039R, a theorem

[Tag 039R](https://stacks.math.columbia.edu/tag/039R) in the Stacks Project.

**`Stacks.Etale.etalePullback_isEquivalence_of_surjective_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceThickening.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceThickening.lean#L99). References: EGA IV (18.1.2); SGA 3 X (2.0); SGA 1 IX (1.7); SGA 1 I (5.5), “special case”.

> **Une équivalence remarquable de catégories.** Let `S₀ ⊆ S` be a closed subscheme with the same
> underlying topological space. Base change along the closed immersion is an equivalence from the
> category of schemes étale over `S` to the category of schemes étale over `S₀`.

```lean
theorem etalePullback_isEquivalence_of_surjective_isClosedImmersion (i : S₀ ⟶ S)
    [IsClosedImmersion i] (hi : Function.Surjective i.base) :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) i := ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) i :=
      ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    (show S.Etale ⥤ S₀.Etale from
      MorphismProperty.Over.pullback
        (@Etale : MorphismProperty Scheme.{u}) ⊤ i).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.15, Tag 06NE](https://stacks.math.columbia.edu/tag/06NE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
