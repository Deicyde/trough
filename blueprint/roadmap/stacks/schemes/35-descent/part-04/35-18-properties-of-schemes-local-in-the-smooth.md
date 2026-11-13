---
declaration: section
origin: cited
lean: AlgebraicGeometry.isReduced_isLocal_smooth, AlgebraicGeometry.isLocal_isNormal_etalePrecoverage, AlgebraicGeometry.isNormal_isLocal_smooth, AlgebraicGeometry.isLocallyNoetherian_and_isRegularInCodimension_isLocal_smooth, AlgebraicGeometry.isRegular_isLocal_smooth, AlgebraicGeometry.isNagataScheme_isLocal_smooth
statement: formalized
proof: formalized
---

# 35.18 Properties of schemes local in the smooth topology

Section 35.18 of the Stacks Project, [Tag 034D](https://stacks.math.columbia.edu/tag/034D). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 034E, a lemma

[Tag 034E](https://stacks.math.columbia.edu/tag/034E) in the Stacks Project.

**`AlgebraicGeometry.isReduced_isLocal_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Reduced.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Reduced.lean#L46).

> **Stacks Project, Tag 034E.** Reducedness of schemes is local for the smooth
> precoverage.

```lean
instance isReduced_isLocal_smooth :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsReduced X)
      (Scheme.precoverage @Smooth)
```

## Tag 034F, a lemma

[Tag 034F](https://stacks.math.columbia.edu/tag/034F) in the Stacks Project.

**`AlgebraicGeometry.isLocal_isNormal_etalePrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Normal.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Normal.lean#L239). The attribute's comment: “for the étale precoverage, `AlgebraicGeometry.Scheme.etalePrecoverage`, rather than for the smooth one; normality of a scheme is `AlgebraicGeometry.IsNormal`, Definition 033I, i.e. every local ring is a normal domain”. References: SGA 1 II (3.1), “special case”.

> **Stacks 034F for the étale precoverage.** Normality of a scheme is a local object property
> for `AlgebraicGeometry.Scheme.etalePrecoverage`: a scheme étale over a normal scheme is normal,
> and a scheme covered by normal schemes étale over it is normal.
>
> The source states Lemma 034F for the smooth topology; the étale precoverage is what the
> algebraic-spaces layer consumes, and both affine inputs — Stacks 033C for ascent and Stacks 033G
> for descent — are the smooth ones, so nothing is lost by restricting.
>
> This is item (7) of Remark 03E7: it is the instance that
> `AlgebraicGeometry.Space.exists_atlas_iff_forall_etale` needs in order to turn
> `AlgebraicGeometry.Space.IsNormal` — Definition 03E6 at normality — from a some-chart condition
> into an every-chart equivalence.

```lean
instance isLocal_isNormal_etalePrecoverage :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsNormal X) Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isNormal_isLocal_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/SmoothLocalSource.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/SmoothLocalSource.lean#L88). References: SGA 3 X (8.9), “more general”.

> Normality of schemes is local in the smooth topology.

```lean
public instance isNormal_isLocal_smooth :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsNormal X)
      (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))
```

## Tag 036C, a lemma

[Tag 036C](https://stacks.math.columbia.edu/tag/036C) in the Stacks Project.

**`AlgebraicGeometry.isLocallyNoetherian_and_isRegularInCodimension_isLocal_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/RegularInCodimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/RegularInCodimension.lean#L142). References: EGA IV (17.5.8), “(iii)”.

> **Stacks Project, Tag 036C.** Being locally Noetherian and regular in codimension `k` is
> local for smooth coverings.

```lean
instance isLocallyNoetherian_and_isRegularInCodimension_isLocal_smooth (k : ℕ) :
    ObjectProperty.IsLocal
      (fun X : Scheme.{u} => IsLocallyNoetherian X ∧ IsRegularInCodimension X k)
      (Scheme.precoverage @Smooth)
```

## Tag 036D, a lemma

[Tag 036D](https://stacks.math.columbia.edu/tag/036D) in the Stacks Project.

**`AlgebraicGeometry.isRegular_isLocal_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Regular.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Regular.lean#L59).

> **Stacks Project, Tag 036D.** Regularity of schemes is local for the smooth
> precoverage.

```lean
instance isRegular_isLocal_smooth :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsRegular X)
      (Scheme.precoverage @Smooth)
```

## Tag 036E, a lemma

[Tag 036E](https://stacks.math.columbia.edu/tag/036E) in the Stacks Project.

**`AlgebraicGeometry.isNagataScheme_isLocal_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Nagata.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Nagata.lean#L67).

> **Stacks Project, Tag 036E.** Being Nagata is local for the smooth precoverage on
> schemes.

```lean
instance isNagataScheme_isLocal_smooth :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsNagataScheme X)
      (Scheme.precoverage @Smooth)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.18, Tag 034D](https://stacks.math.columbia.edu/tag/034D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
