---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsRegular, AlgebraicGeometry.isRegular_tfae, AlgebraicGeometry.isRegular_tfae_cover, AlgebraicGeometry.IsRegular.restrict, AlgebraicGeometry.isNormal_of_isRegular
statement: formalized
proof: formalized
---

# 28.9 Regular schemes

Section 28.9 of the Stacks Project, [Tag 02IR](https://stacks.math.columbia.edu/tag/02IR). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02IS, a definition

[Tag 02IS](https://stacks.math.columbia.edu/tag/02IS) in the Stacks Project.

**`AlgebraicGeometry.IsRegular`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Regular.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Regular.lean#L68). The attribute's comment: “the source's requirement on `𝒪_X(U)`, Noetherian *and* regular, is Mathlib's class `IsRegularRing`: it extends `IsNoetherianRing`, and its further field is that the localization at every prime is a regular local ring. Both halves of the requirement are therefore written into this definition, the Noetherian one recoverable as `IsRegularRing.toIsNoetherian`; see the module docstring”.

> A scheme is regular, or nonsingular, if every point has an affine open neighbourhood whose
> ring of sections is Noetherian and regular.

```lean
public abbrev IsRegular (X : Scheme.{u}) : Prop
```

## Tag 02IT, a lemma

[Tag 02IT](https://stacks.math.columbia.edu/tag/02IT) in the Stacks Project.

**`AlgebraicGeometry.isRegular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean#L144).

> A scheme is regular if and only if it is locally Noetherian with regular local rings at
> every point, if and only if it is locally Noetherian with regular local rings at closed points.

```lean
theorem isRegular_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsRegular X,
      IsLocallyNoetherian X ∧ ∀ x : X, IsRegularLocalRing (X.presheaf.stalk x),
      IsLocallyNoetherian X ∧
        (∀ x : X, x ∈ closedPoints X → IsRegularLocalRing (X.presheaf.stalk x))]
```

## Tag 02IU, a lemma

[Tag 02IU](https://stacks.math.columbia.edu/tag/02IU) in the Stacks Project.

**`AlgebraicGeometry.isRegular_tfae_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean#L255). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 02IU.** A scheme is regular if and only if the ring of sections is
> regular on every affine open, if and only if it is regular on the members of one affine open
> covering, if and only if the scheme has an open covering by regular open subschemes.

```lean
theorem isRegular_tfae_cover (X : Scheme.{u}) :
    List.TFAE [
      IsRegular X,
      ∀ U : X.affineOpens, IsRegularRing Γ(X, U),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsRegularRing Γ(X, U i),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsRegular (U i).toScheme]
```

**`AlgebraicGeometry.IsRegular.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean#L276). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 02IU.** Every open subscheme of a regular scheme is regular.

```lean
theorem IsRegular.restrict {X : Scheme.{u}} (hX : IsRegular X) (U : X.Opens) :
    IsRegular U.toScheme
```

## Tag 0569, a lemma

[Tag 0569](https://stacks.math.columbia.edu/tag/0569) in the Stacks Project.

**`AlgebraicGeometry.isNormal_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Regular.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Regular.lean#L74). The attribute's comment: “a regular scheme is normal; the sole hypothesis is `IsRegular` of Tag 02IS, whose `IsRegularRing` already carries Noetherianness, so nothing beyond the source is assumed”.

> **Stacks Project, Tag 0569.** Every regular scheme is normal.

```lean
public theorem isNormal_of_isRegular (X : Scheme.{u}) (hX : IsRegular X) :
    IsNormal X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.9, Tag 02IR](https://stacks.math.columbia.edu/tag/02IR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
