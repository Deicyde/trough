---
declaration: section
origin: cited
lean: IsUniversallyJapaneseScheme, IsJapaneseScheme, IsNagataScheme, isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme, isJapaneseScheme_tfae, isJapaneseScheme_open, isUniversallyJapaneseScheme_tfae, isUniversallyJapaneseScheme_open
statement: formalized
proof: formalized
---

# 28.13 Japanese and Nagata schemes

Section 28.13 of the Stacks Project, [Tag 033R](https://stacks.math.columbia.edu/tag/033R). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 033S, a definition

[Tag 033S](https://stacks.math.columbia.edu/tag/033S) in the Stacks Project.

**`IsUniversallyJapaneseScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L60). The attribute's comment: “universally\_japanese\_scheme”. References: EGA IV (5.11.4); SGA 4 IX (2.14.2).

> A scheme is **universally Japanese** if every point has an affine open neighbourhood whose
> ring of sections is universally Japanese.

```lean
public def IsUniversallyJapaneseScheme
    (X : Scheme.{u}) : Prop
```

Declarations registered for the tag:

- [`IsJapaneseScheme`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Nagata.lean#L28), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L186) (StacksFrontier): “japanese\_scheme”.
- [`IsNagataScheme`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Nagata.lean#L36), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L187) (StacksFrontier): “nagata\_scheme”.

## Tag 033U, a lemma

[Tag 033U](https://stacks.math.columbia.edu/tag/033U) in the Stacks Project.

**`isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L169). The attribute's comment: “the forward implication: a Nagata scheme is locally Noetherian”.

> A scheme is Nagata if and only if it is locally Noetherian and universally Japanese.

```lean
public theorem isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme
    (X : Scheme.{u}) :
    IsNagataScheme X ↔
      (IsLocallyNoetherian X ∧
        IsUniversallyJapaneseScheme X)
```

## Tag 033V, a lemma

[Tag 033V](https://stacks.math.columbia.edu/tag/033V) in the Stacks Project.

**`isJapaneseScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L87). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 033V.** For an integral scheme, Japanese-ness is equivalent to
> Japanese-ness of the section ring of every nonempty affine open, to the existence of an affine
> open cover with Japanese section rings, and to the existence of an open cover by Japanese
> schemes.

```lean
public theorem isJapaneseScheme_tfae (X : Scheme.{u}) [IsIntegral X] :
    List.TFAE [
      IsJapaneseScheme X,
      ∀ U : X.affineOpens, ∀ _hU : Nonempty U.1,
        letI : IsDomain Γ(X, U.1) := IsIntegral.component_integral U.1
        IsJapaneseRing Γ(X, U.1),
      ∃ (I : Type u) (U : I → X.affineOpens),
        TopologicalSpace.IsOpenCover (fun i ↦ (U i).1) ∧
          ∀ i, ∃ _hU : Nonempty (U i).1,
            letI : IsDomain Γ(X, (U i).1) := IsIntegral.component_integral (U i).1
            IsJapaneseRing Γ(X, (U i).1),
      ∃ (I : Type u) (U : I → X.Opens),
        TopologicalSpace.IsOpenCover U ∧
        ∀ i, ∃ hU : IsIntegral (U i).toScheme,
            @IsJapaneseScheme (U i).toScheme hU]
```

**`isJapaneseScheme_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L155). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 033V.** Every nonempty open subscheme of a Japanese integral scheme is
> Japanese.

```lean
public theorem isJapaneseScheme_open (X : Scheme.{u}) [IsIntegral X] (hX : IsJapaneseScheme X)
    (U : X.Opens) [Nonempty U] :
    ∃ hU : IsIntegral U.toScheme, @IsJapaneseScheme U.toScheme hU
```

## Tag 033W, a lemma

[Tag 033W](https://stacks.math.columbia.edu/tag/033W) in the Stacks Project.

**`isUniversallyJapaneseScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L241). The attribute's comment: “equivalent conditions”. References: SGA 4 IX (2.14.2).

> **Stacks Project, Tag 033W.** For a scheme `X`, being universally Japanese is equivalent to
> the section ring of every affine open being universally Japanese, to this holding on some affine
> open covering, and to admitting an open covering by universally Japanese open subschemes.

```lean
theorem isUniversallyJapaneseScheme_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsUniversallyJapaneseScheme X,
      ∀ U : X.affineOpens, IsUniversallyJapaneseRing Γ(X, (U : X.Opens)),
      ∃ (I : Type u) (U : I → X.affineOpens),
        IsOpenCover (fun i ↦ (U i : X.Opens)) ∧
          ∀ i, IsUniversallyJapaneseRing Γ(X, (U i : X.Opens)),
      ∃ (I : Type u) (U : I → X.Opens),
        IsOpenCover U ∧ ∀ i, IsUniversallyJapaneseScheme (U i).toScheme]
```

**`isUniversallyJapaneseScheme_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L262). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 033W.** Every open subscheme of a universally Japanese scheme is
> universally Japanese.

```lean
theorem isUniversallyJapaneseScheme_open {X : Scheme.{u}} (hX : IsUniversallyJapaneseScheme X)
    (U : X.Opens) : IsUniversallyJapaneseScheme U.toScheme
```

## Tag 033X, a lemma

[Tag 033X](https://stacks.math.columbia.edu/tag/033X) in the Stacks Project.

**`isNagataScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L209). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 033X.** For a scheme `X`, being Nagata is equivalent to the section
> ring of every affine open being Nagata, to this holding on some affine open covering, and to
> admitting an open covering by Nagata open subschemes.

```lean
theorem isNagataScheme_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsNagataScheme X,
      ∀ U : X.affineOpens, IsNagataRing Γ(X, (U : X.Opens)),
      ∃ (I : Type u) (U : I → X.affineOpens),
        IsOpenCover (fun i ↦ (U i : X.Opens)) ∧
          ∀ i, IsNagataRing Γ(X, (U i : X.Opens)),
      ∃ (I : Type u) (U : I → X.Opens),
        IsOpenCover U ∧ ∀ i, IsNagataScheme (U i).toScheme]
```

**`isNagataScheme_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L228). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 033X.** Every open subscheme of a Nagata scheme is Nagata.

```lean
theorem isNagataScheme_open {X : Scheme.{u}} (hX : IsNagataScheme X) (U : X.Opens) :
    IsNagataScheme U.toScheme
```

## Tag 033Y, a lemma

[Tag 033Y](https://stacks.math.columbia.edu/tag/033Y) in the Stacks Project.

Declarations registered for the tag:

- [`nagata_iff_integral_closed_subschemes_japanese`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Japanese/NagataScheme.lean#L699), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L188) (StacksFrontier).

## Tag 033Z, a lemma

[Tag 033Z](https://stacks.math.columbia.edu/tag/033Z) in the Stacks Project.

**`isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Nagata.lean#L169).

> A scheme is Nagata if and only if it is locally Noetherian and universally Japanese.

```lean
public theorem isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme
    (X : Scheme.{u}) :
    IsNagataScheme X ↔
      (IsLocallyNoetherian X ∧
        IsUniversallyJapaneseScheme X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.13, Tag 033R](https://stacks.math.columbia.edu/tag/033R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
