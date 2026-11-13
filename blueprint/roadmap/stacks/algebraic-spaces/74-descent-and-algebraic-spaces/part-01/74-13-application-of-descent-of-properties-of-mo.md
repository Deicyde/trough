---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isRelativelyAmple_of_isFpqcCovering, AlgebraicGeometry.Space.forall_isRelativelyAmple_baseChange_of_isRelativelyAmple, AlgebraicGeometry.Space.exists_affineFpqcRefinement_isAmpleOnBaseChange, AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isRelativelyAmple_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_factors_iff_isRelativelyAmple_of_isProper
statement: formalized
proof: formalized
---

# 74.13 Application of descent of properties of morphisms

Section 74.13 of the Stacks Project, [Tag 0D3B](https://stacks.math.columbia.edu/tag/0D3B). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D3C, a lemma

[Tag 0D3C](https://stacks.math.columbia.edu/tag/0D3C) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isRelativelyAmple_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocal.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocal.lean#L57).

> **Stacks 0D3C.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, `𝓛` an invertible
> `𝒪_X`-module and `{gᵢ : Yᵢ ⟶ Y}` an fpqc covering, with base changes `fᵢ : Xᵢ ⟶ Yᵢ` of `f` and
> pullbacks `𝓛ᵢ` of `𝓛` to `Xᵢ`. Then `𝓛` is ample on `X/Y` if and only if `𝓛ᵢ` is ample on
> `Xᵢ/Yᵢ` for every `i`.

```lean
theorem isRelativelyAmple_iff_forall_isRelativelyAmple_of_isFpqcCovering
    {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y} {I : Type v}
    {Yᵢ Xᵢ : I → AlgebraicSpaces B S hS} {gᵢ : ∀ i, Yᵢ i ⟶ Y} {fᵢ : ∀ i, Xᵢ i ⟶ Yᵢ i}
    {pᵢ : ∀ i, Xᵢ i ⟶ X} (hsq : ∀ i, IsPullback (pᵢ i) (fᵢ i) f (gᵢ i))
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property L)
    (hfpqc : IsFpqcCovering B S hS fun i => (gᵢ i).hom) :
    IsRelativelyAmple B S hS f L ↔
      ∀ i, IsRelativelyAmple B S hS (fᵢ i) ((modulePullback B S hS (pᵢ i)).obj L)
```

**`AlgebraicGeometry.Space.forall_isRelativelyAmple_baseChange_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean#L145). The attribute's comment: “(1) implies (2), unconditionally; the fpqc hypothesis on the family is not needed for this direction”.

> **Stacks 0D3C, (1) implies (2).** If `L` is ample on `X/Y` then the pullback of `L` to the
> base change of `f` along any member of the family is ample on that base change: this is the
> base-change stability of Stacks 0D33, and nothing is asked of the family.

```lean
theorem forall_isRelativelyAmple_baseChange_of_isRelativelyAmple
    (hL : IsRelativelyAmple B S hS f L) (i : I) :
    IsRelativelyAmple B S hS (fᵢ i) ((modulePullback B S hS (pᵢ i)).obj L)
```

**`AlgebraicGeometry.Space.exists_affineFpqcRefinement_isAmpleOnBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean#L162). The attribute's comment: “the unconditional half of (2) implies (1): the clause of Tag 0D36 on a finite affine fpqc covering of each affine scheme over Y. Descending it to the scheme itself is carried by `isRelativelyAmple_iff_forall_isRelativelyAmple_baseChange`”.

> **The reduction of Stacks 0D3C, (2) implies (1), to the scheme level.** Assume the pullback
> of `L` to each base change `Xᵢ` is ample on `Xᵢ/Yᵢ`. Then every affine scheme `T` over `Y`
> admits a finite family of affine schemes over `T` which covers `T` in the fpqc topology of
> schemes and on each of whose members the base-change clause of Stacks 0D36 for `(f, L)` holds.
>
> The fpqc condition of Stacks 03MQ supplies the family together with a factorisation of each
> member through some `Yᵢ`, and
> `AlgebraicGeometry.Space.isAmpleOnBaseChange_of_isPullback` turns the clause for `(fᵢ, Lᵢ)` at
> that factorisation into the clause for `(f, L)`.

```lean
theorem exists_affineFpqcRefinement_isAmpleOnBaseChange
    (hfpqc : IsFpqcCovering B S hS fun i => (gᵢ i).hom)
    (h : ∀ i, IsRelativelyAmple B S hS (fᵢ i) ((modulePullback B S hS (pᵢ i)).obj L))
    (T : BigAffineFppf B S hS)
    (g : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj T) ⟶ Y.1) :
    ∃ U : PreZeroHypercover.{u + 1} T, Finite U.I₀ ∧
      Presieve.map (BigAffineFppf.toScheme B S hS) U.presieve₀ ∈
        Scheme.fpqcPrecoverage ((BigAffineFppf.toScheme B S hS).obj T) ∧
      ∀ j : U.I₀, IsAmpleOnBaseChange B S hS f L
        ((BigAffineFppf.inclusion B S hS).obj (U.X j))
        (yoneda.map ((BigAffineFppf.inclusion B S hS).map (U.f j)) ≫ g)
```

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isRelativelyAmple_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleFpqcLocalAtTarget.lean#L192). The attribute's comment: “full equivalence, with the hypotheses of the source: L invertible and the family an fpqc covering”.

> **Stacks 0D3C.** Let `L` be an invertible `𝒪_X`-module, let `{gᵢ : Yᵢ ⟶ Y}` be an fpqc
> covering, let `fᵢ : Xᵢ ⟶ Yᵢ` be the base change of `f : X ⟶ Y` and `Lᵢ` the pullback of `L`.
> Then `L` is ample on `X/Y` if and only if `Lᵢ` is ample on `Xᵢ/Yᵢ` for every `i`.
>
> The forward direction is base change. For the converse, `f` is quasi-compact and separated
> (Stacks 0D34, 041L, 0421), the clause of Stacks 0D36 may be tested at the affine schemes over `Y`,
> and at such a scheme it is
> `AlgebraicGeometry.Space.exists_affineFpqcRefinement_isAmpleOnBaseChange` followed by
> `AlgebraicGeometry.Space.exists_isPullback_of_affineFpqcFamily` and
> `AlgebraicGeometry.Space.exists_isRelativelyAmple_of_fpqcFamily`.

```lean
theorem isRelativelyAmple_iff_forall_isRelativelyAmple_baseChange
    (hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property L)
    (hfpqc : IsFpqcCovering B S hS fun i => (gᵢ i).hom) :
    IsRelativelyAmple B S hS f L ↔
      ∀ i, IsRelativelyAmple B S hS (fᵢ i) ((modulePullback B S hS (pᵢ i)).obj L)
```

## Tag 0D3D, a lemma

[Tag 0D3D](https://stacks.math.columbia.edu/tag/0D3D) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_factors_iff_isRelativelyAmple_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean#L236).

> Let `S` be a scheme, `f : X ⟶ Y` a proper morphism of algebraic spaces over `S` and `L` an
> invertible `𝒪_X`-module. There is an open subspace `V ⊆ Y` such that a morphism `g : Y' ⟶ Y` of
> algebraic spaces factors through `V` if and only if the pullback of `L` to `X' = Y' ×_Y X` is ample
> on `X'/Y'` (Stacks 0D31).

```lean
theorem exists_isOpenSubspace_factors_iff_isRelativelyAmple_of_isProper
    {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y} (hf : IsProper B S hS f.hom)
    {L : Modules.{u, u} B S hS X.1 X.2}
    (hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS X.1 X.2).O)).property L) :
    ∃ V : Subfunctor Y.1, IsOpenSubspace B S hS V ∧
      ∀ ⦃X' Y' : AlgebraicSpaces B S hS⦄ (g : Y' ⟶ Y) (p : X' ⟶ X) (f' : X' ⟶ Y'),
        IsPullback p f' f g →
          ((∃ l : Y'.1 ⟶ V.toFunctor, l ≫ V.ι = g.hom) ↔
            IsRelativelyAmple B S hS f' ((modulePullback B S hS p).obj L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.13, Tag 0D3B](https://stacks.math.columbia.edu/tag/0D3B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
