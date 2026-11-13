---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsGScheme, AlgebraicGeometry.isGScheme_tfae, AlgebraicGeometry.isGScheme_tfae_cover, AlgebraicGeometry.IsGScheme.restrict
statement: formalized
proof: formalized
---

# 28.14 G-schemes

Section 28.14 of the Stacks Project, [Tag 0HA2](https://stacks.math.columbia.edu/tag/0HA2). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HA3, a definition

[Tag 0HA3](https://stacks.math.columbia.edu/tag/0HA3) in the Stacks Project.

**`AlgebraicGeometry.IsGScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean#L64).

> A scheme is a G-scheme if every point has an affine open neighbourhood whose ring of
> sections is a G-ring.

```lean
public def IsGScheme (X : Scheme.{u}) : Prop
```

## Tag 0HA4, a lemma

[Tag 0HA4](https://stacks.math.columbia.edu/tag/0HA4) in the Stacks Project.

**`AlgebraicGeometry.isGScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean#L169).

> A scheme is a G-scheme if and only if it is locally Noetherian and the map from each local
> ring to its completion is regular, if and only if it is locally Noetherian and the map from the
> local ring at each closed point to its completion is regular.

```lean
theorem isGScheme_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsGScheme X,
      IsLocallyNoetherian X ∧ ∀ x : X,
        IsRegularRingHom (algebraMap (X.presheaf.stalk x)
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))),
      IsLocallyNoetherian X ∧ ∀ x : X, x ∈ closedPoints X →
        IsRegularRingHom (algebraMap (X.presheaf.stalk x)
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)))]
```

## Tag 0HA5, a lemma

[Tag 0HA5](https://stacks.math.columbia.edu/tag/0HA5) in the Stacks Project.

**`AlgebraicGeometry.isGScheme_tfae_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean#L254). The attribute's comment: “equivalent conditions (1)–(4)”.

> A scheme is a G-scheme if and only if the ring of sections on every affine open is a G-ring,
> if and only if it is a G-ring on the members of one affine open covering, if and only if the
> scheme has an open covering by open subschemes which are G-schemes.

```lean
theorem isGScheme_tfae_cover (X : Scheme.{u}) :
    List.TFAE [
      IsGScheme X,
      ∀ U : X.affineOpens, IsGRing Γ(X, U),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsGRing Γ(X, U i),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsGScheme (U i).toScheme]
```

**`AlgebraicGeometry.IsGScheme.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/GScheme.lean#L275). The attribute's comment: “open subschemes”.

> Every open subscheme of a G-scheme is a G-scheme.

```lean
theorem IsGScheme.restrict {X : Scheme.{u}} (hX : IsGScheme X) (U : X.Opens) :
    IsGScheme U.toScheme
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.14, Tag 0HA2](https://stacks.math.columbia.edu/tag/0HA2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
