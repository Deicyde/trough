---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.Tag05JXGeneral.universallyClosed_tfae_essentiallyFiniteType, Stacks.AlgebraicGeometry.NagataValuativeCriterion.isSeparated_iff_hasEssentiallyFiniteTypeValuativeUniqueness, Stacks.AlgebraicGeometry.NagataValuativeCriterion.isSeparated_iff_hasAtMostOneLiftOverPuncturedCurves, Stacks.AlgebraicGeometry.NagataValuativeCriterion.isProper_iff_hasEssentiallyFiniteTypeValuativeLift
statement: formalized
proof: formalized
---

# 32.17 Valuative criteria over a Nagata base

Section 32.17 of the Stacks Project, [Tag 0GWU](https://stacks.math.columbia.edu/tag/0GWU). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GWV, a lemma

[Tag 0GWV](https://stacks.math.columbia.edu/tag/0GWV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag05JXGeneral.universallyClosed_tfae_essentiallyFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/General/Nagata.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/General/Nagata.lean#L64).

> **Stacks Project, Tag 0GWV.**  Over a Nagata base `S`, for a quasi-compact `f : X ⟶ Y` with
> `X` and `Y` locally of finite type over `S`, universal closedness, closedness of every
> finite-dimensional affine-space base change, and the essentially-finite-type one-dimensional
> extension test are equivalent.
>
> Three of the four edges come from the Nagata files; the fourth, `2 ⇒ 1`, is Stacks `05JX`
> (3) ⇒ (1), proved in `Basic.lean` for an arbitrary quasi-compact morphism.

```lean
theorem universallyClosed_tfae_essentiallyFiniteType
    {S X Y : Scheme.{u}} (hX : X ⟶ S) (hY : Y ⟶ S) (f : X ⟶ Y)
    (hf : f ≫ hY = hX) (hS : IsNagataScheme S)
    [LocallyOfFiniteType hX] [LocallyOfFiniteType hY] [QuasiCompact f] :
    List.TFAE
      [UniversallyClosed f,
       ∀ n : ℕ, IsClosedMap (AffineSpace.map (ULift.{u} (Fin n)) f),
       HasEssentiallyFiniteTypeValuativeExtension f hY]
```

## Tag 0GWW, a lemma

[Tag 0GWW](https://stacks.math.columbia.edu/tag/0GWW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.NagataValuativeCriterion.isSeparated_iff_hasEssentiallyFiniteTypeValuativeUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedAndProper.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedAndProper.lean#L168).

> **Stacks Project, Tag 0GWW.**  Over a Nagata base `S`, a morphism `f : X ⟶ Y` between schemes
> locally of finite type over `S` is separated if and only if the lift in every one-dimensional
> finite-type test diagram is unique.
>
> Uniqueness for a separated morphism holds because `Spec (Frac 𝒪_{C,c}) ⟶ Spec 𝒪_{C,c}` is
> dominant and `Spec 𝒪_{C,c}` is reduced.  Conversely the extension condition for the diagonal of
> `f` follows from the assumed uniqueness, and tag `0GWV` turns it into universal closedness of the
> diagonal, which for an immersion means that it is a closed immersion.

```lean
theorem isSeparated_iff_hasEssentiallyFiniteTypeValuativeUniqueness
    {S X Y : Scheme.{u}} (hX : X ⟶ S) (hY : Y ⟶ S) (f : X ⟶ Y)
    (hf : f ≫ hY = hX) (hS : IsNagataScheme S)
    [LocallyOfFiniteType hX] [LocallyOfFiniteType hY] :
    IsSeparated f ↔ HasEssentiallyFiniteTypeValuativeUniqueness f hY
```

**`Stacks.AlgebraicGeometry.NagataValuativeCriterion.isSeparated_iff_hasAtMostOneLiftOverPuncturedCurves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedPunctured.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedPunctured.lean#L148).

> **Stacks Project, Tag 0GWW.**  Let `S` be a Nagata scheme and let `f : X ⟶ Y` be a morphism
> of schemes locally of finite type over `S`.  Then `f` is separated if and only if, for every
> normal integral scheme `C` of finite type over `S`, every closed point `c ∈ C` with
> `dim 𝒪_{C,c} = 1`, and every commutative square over `S` with `C \ {c} ⟶ X` along the top and
> `C ⟶ Y` along the bottom, at most one `Spec 𝒪_{C,c} ⟶ X` makes the induced square from
> `Spec (Frac 𝒪_{C,c}) ⟶ Spec 𝒪_{C,c}` to `f` commute.
>
> This is `isSeparated_iff_hasEssentiallyFiniteTypeValuativeUniqueness`, whose condition is
> equivalent to this one by `hasAtMostOneLiftOverPuncturedCurves_iff`.

```lean
theorem isSeparated_iff_hasAtMostOneLiftOverPuncturedCurves
    {S X Y : Scheme.{u}} (hX : X ⟶ S) (hY : Y ⟶ S) (f : X ⟶ Y)
    (hf : f ≫ hY = hX) (hS : IsNagataScheme S)
    [LocallyOfFiniteType hX] [LocallyOfFiniteType hY] :
    IsSeparated f ↔ HasAtMostOneLiftOverPuncturedCurves hX hY f
```

## Tag 0GWX, a lemma

[Tag 0GWX](https://stacks.math.columbia.edu/tag/0GWX) in the Stacks Project.

**`Stacks.AlgebraicGeometry.NagataValuativeCriterion.isProper_iff_hasEssentiallyFiniteTypeValuativeLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedAndProper.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataValuativeCriterion/SeparatedAndProper.lean#L223).

> **Stacks Project, Tag 0GWX.**  Over a Nagata base `S`, a quasi-compact morphism `f : X ⟶ Y`
> between schemes locally of finite type over `S` is proper if and only if every one-dimensional
> finite-type test diagram admits exactly one lift.
>
> This is formal from tags `0GWV` and `0GWW` and the definition of a proper morphism as one that is
> locally of finite type, separated and universally closed.

```lean
theorem isProper_iff_hasEssentiallyFiniteTypeValuativeLift
    {S X Y : Scheme.{u}} (hX : X ⟶ S) (hY : Y ⟶ S) (f : X ⟶ Y)
    (hf : f ≫ hY = hX) (hS : IsNagataScheme S)
    [LocallyOfFiniteType hX] [LocallyOfFiniteType hY] [QuasiCompact f] :
    IsProper f ↔ HasEssentiallyFiniteTypeValuativeLift f hY
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.17, Tag 0GWU](https://stacks.math.columbia.edu/tag/0GWU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
