---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsCohenMacaulay, AlgebraicGeometry.isCohenMacaulay_tfae_stalk, AlgebraicGeometry.isCohenMacaulay_tfae_cover, AlgebraicGeometry.IsCohenMacaulay.restrict
statement: formalized
proof: formalized
---

# 28.8 Cohen-Macaulay schemes

Section 28.8 of the Stacks Project, [Tag 02IN](https://stacks.math.columbia.edu/tag/02IN). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02IO, a definition

[Tag 02IO](https://stacks.math.columbia.edu/tag/02IO) in the Stacks Project.

**`AlgebraicGeometry.IsCohenMacaulay`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulay.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulay.lean#L47). References: EGA IV (5.7.1).

> **Cohen–Macaulay scheme.** A scheme `X` is Cohen–Macaulay if every point belongs to an
> affine open `U` whose ring of sections `Γ(X, U)` is Noetherian and Cohen–Macaulay.

```lean
public def IsCohenMacaulay (X : Scheme.{u}) : Prop
```

## Tag 02IP, a lemma

[Tag 02IP](https://stacks.math.columbia.edu/tag/02IP) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_tfae_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean#L185). References: EGA IV (5.7.1).

> A scheme is Cohen–Macaulay if and only if it is locally Noetherian with Cohen–Macaulay
> local rings at every point, if and only if it is locally Noetherian with Cohen–Macaulay local
> rings at closed points.

```lean
theorem isCohenMacaulay_tfae_stalk (X : Scheme.{u}) :
    List.TFAE [
      IsCohenMacaulay X,
      IsLocallyNoetherian X ∧
        (∀ x : X, ∃ h : IsNoetherianRing (X.presheaf.stalk x),
          @IsCohenMacaulayLocalRing (X.presheaf.stalk x) _ h _),
      IsLocallyNoetherian X ∧
        (∀ x : X, x ∈ closedPoints X →
          ∃ h : IsNoetherianRing (X.presheaf.stalk x),
            @IsCohenMacaulayLocalRing (X.presheaf.stalk x) _ h _)]
```

## Tag 02IQ, a lemma

[Tag 02IQ](https://stacks.math.columbia.edu/tag/02IQ) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_tfae_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean#L413). The attribute's comment: “equivalent conditions”. References: EGA IV (5.7.1), “more general”.

> Cohen–Macaulayness of a scheme is equivalent to the Noetherian Cohen–Macaulay condition on
> every affine coordinate ring, to that condition on one affine open covering, and to having an
> open covering by Cohen–Macaulay schemes.

```lean
theorem isCohenMacaulay_tfae_cover (X : Scheme.{u}) :
    List.TFAE [
      IsCohenMacaulay X,
      ∀ U : X.affineOpens, ∃ h : IsNoetherianRing Γ(X, U.val),
        @IsCohenMacaulayRing Γ(X, U.val) _ h,
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧
          ∀ i, ∃ h : IsNoetherianRing Γ(X, (U i).val),
            @IsCohenMacaulayRing Γ(X, (U i).val) _ h,
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsCohenMacaulay (U i).toScheme]
```

**`AlgebraicGeometry.IsCohenMacaulay.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean#L436). The attribute's comment: “open subschemes”.

> Every open subscheme of a Cohen–Macaulay scheme is Cohen–Macaulay.

```lean
theorem IsCohenMacaulay.restrict {X : Scheme.{u}} (hX : IsCohenMacaulay X) (U : X.Opens) :
    IsCohenMacaulay U.toScheme
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.8, Tag 02IN](https://stacks.math.columbia.edu/tag/02IN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
