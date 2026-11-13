---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsResolution, AlgebraicGeometry.HasResolutionByNormalizedBlowUps, AlgebraicGeometry.hasResolutionByNormalizedBlowUps_of_exists_isResolution, AlgebraicGeometry.exists_isResolution_of_isAdicComplete, AlgebraicGeometry.tfae_exists_isAlteration_isRegular
statement: formalized
proof: formalized
---

# 54.14 Resolution

Section 54.14 of the Stacks Project, [Tag 0BGJ](https://stacks.math.columbia.edu/tag/0BGJ). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BGK, a definition

[Tag 0BGK](https://stacks.math.columbia.edu/tag/0BGK) in the Stacks Project.

**`AlgebraicGeometry.IsResolution`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/Basic.lean#L43).

> A morphism to a Noetherian integral scheme is a **resolution of singularities** if it is a
> modification and its source is regular.

```lean
abbrev IsResolution {X Y : Scheme.{u}} [IsIntegral Y] [IsNoetherian Y]
    (f : X ⟶ Y) : Prop
```

## Tag 0BGL, a definition

[Tag 0BGL](https://stacks.math.columbia.edu/tag/0BGL) in the Stacks Project.

**`AlgebraicGeometry.HasResolutionByNormalizedBlowUps`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/NormalizedBlowUps.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/NormalizedBlowUps.lean#L68).

> **Stacks Project, Tag 0BGL.** A scheme admits a *resolution of singularities by normalized
> blowups* if its normalization can be followed by finitely many normalized blowups at closed
> points, all proper over the scheme, so as to obtain a regular scheme.

```lean
abbrev HasResolutionByNormalizedBlowUps (Y : Scheme.{u}) : Prop
```

## Tag 0BGM, a lemma

[Tag 0BGM](https://stacks.math.columbia.edu/tag/0BGM) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionByNormalizedBlowUps_of_exists_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/CompleteLocalResolution.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/CompleteLocalResolution.lean#L39).

> **Stacks Project, Tag 0BGM.** Let `(A, 𝔪, κ)` be a Noetherian local ring which is normal of
> dimension two. If `Spec(A)` has a resolution of singularities, then `Spec(A)` has a resolution by
> normalized blowups.

```lean
theorem hasResolutionByNormalizedBlowUps_of_exists_isResolution
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A] [IsNormalDomain A]
    (hdim : ringKrullDim A = 2)
    (hres : ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)), IsResolution f) :
    HasResolutionByNormalizedBlowUps (Spec (.of A))
```

## Tag 0BGN, a lemma

[Tag 0BGN](https://stacks.math.columbia.edu/tag/0BGN) in the Stacks Project.

**`AlgebraicGeometry.exists_isResolution_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/CompleteLocalResolution.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/CompleteLocalResolution.lean#L51).

> **Stacks Project, Tag 0BGN.** Let `(A, 𝔪, κ)` be a Noetherian complete local ring which is a
> normal domain of dimension two. Then `Spec(A)` has a resolution of singularities.

```lean
theorem exists_isResolution_of_isAdicComplete
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (maximalIdeal A) A] [IsNormalDomain A] (hdim : ringKrullDim A = 2) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)), IsResolution f
```

## Tag 0BGP, a theorem

[Tag 0BGP](https://stacks.math.columbia.edu/tag/0BGP) in the Stacks Project.

**`AlgebraicGeometry.tfae_exists_isAlteration_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/LipmanTheorem.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/LipmanTheorem.lean#L44).

> **Stacks Project, Tag 0BGP (Lipman).** Let `Y` be a two-dimensional integral Noetherian
> scheme. The following are equivalent:
>
> 1. there exists an alteration `X ⟶ Y` with `X` regular;
> 2. there exists a resolution of singularities of `Y`;
> 3. `Y` has a resolution of singularities by normalized blowups;
> 4. the normalization `Y^ν ⟶ Y` is finite, `Y^ν` has finitely many singular points, and the
>    completion of the local ring of `Y^ν` at each of them is normal.

```lean
theorem tfae_exists_isAlteration_isRegular (Y : Scheme.{u}) [IsIntegral Y] [IsNoetherian Y]
    (hdim : topologicalKrullDim Y = 2) :
    List.TFAE
      [∃ (X : Scheme.{u}) (f : X ⟶ Y), IsAlteration f ∧ IsRegular X,
       ∃ (X : Scheme.{u}) (f : X ⟶ Y), IsResolution f,
       HasResolutionByNormalizedBlowUps Y,
       ∃ hY : ∀ U : Y.Opens, IsCompact (U : Set Y) → (irreducibleComponents U).Finite,
        IsFinite (Scheme.normalization Y hY) ∧
        (singularLocus (Y.normalizationScheme hY)).Finite ∧
        ∀ y : Y.normalizationScheme hY, y ∈ singularLocus (Y.normalizationScheme hY) →
          IsNormalRing (AdicCompletion
            (maximalIdeal ((Y.normalizationScheme hY).presheaf.stalk y))
            ((Y.normalizationScheme hY).presheaf.stalk y))]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.14, Tag 0BGJ](https://stacks.math.columbia.edu/tag/0BGJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
