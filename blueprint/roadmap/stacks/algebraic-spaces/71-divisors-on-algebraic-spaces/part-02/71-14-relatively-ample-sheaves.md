---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsRelativelyAmple, AlgebraicGeometry.Space.IsRelativelyAmple.isRepresentable, AlgebraicGeometry.Space.isRelativelyAmple_iff_exists_scheme, AlgebraicGeometry.Space.isRelativelyAmple_baseChange, AlgebraicGeometry.Space.IsRelativelyAmple.relativelyRepresentable, AlgebraicGeometry.Space.IsRelativelyAmple.isQuasiCompact, AlgebraicGeometry.Space.IsRelativelyAmple.isSeparated, AlgebraicGeometry.Space.isRelativelyAmple_of_isRelativelyAmple_baseChange_etale
statement: formalized
proof: formalized
---

# 71.14 Relatively ample sheaves

Section 71.14 of the Stacks Project, [Tag 0D30](https://stacks.math.columbia.edu/tag/0D30). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D31, a definition

[Tag 0D31](https://stacks.math.columbia.edu/tag/0D31) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativelyAmple`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L177).

> **Stacks 0D31.** A module `L` on an algebraic space `X` is *ample relative to*
> `f : X ⟶ Y`, or *`f`-ample*, when `f` is representable and, for every scheme `T` over the base
> with a morphism to `Y` and every cartesian square identifying the fibre product with a scheme
> `U`, the pullback of `L` to `U` is invertible and ample relative to `U ⟶ T` in the sense of
> Stacks 01VH.

```lean
def IsRelativelyAmple {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (L : Modules.{u, u} B S hS X.1 X.2) : Prop
```

## Tag 0D32, a lemma

[Tag 0D32](https://stacks.math.columbia.edu/tag/0D32) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativelyAmple.isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleOverScheme.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleOverScheme.lean#L59). The attribute's comment: “the source is a scheme”.

> If a module is ample relative to `f : X ⟶ Y` and the algebraic space `Y` is a scheme, then
> the algebraic space `X` is a scheme.

```lean
theorem IsRelativelyAmple.isRepresentable {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {L : Modules.{u, u} B S hS X.1 X.2} (h : IsRelativelyAmple B S hS f L)
    [Y.1.IsRepresentable] : X.1.IsRepresentable
```

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_exists_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleOverScheme.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleOverScheme.lean#L144).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over the base, let `L` be
> an invertible `𝒪_X`-module, and assume that the algebraic space `Y` is the scheme `V`. The
> following are equivalent:
>
> 1. `L` is ample relative to `f` in the sense of algebraic spaces, Stacks 0D31;
> 2. `X` is a scheme `U` and the restriction of `L` to `U` is invertible and ample relative to the
>    morphism `U ⟶ V` induced by `f`, in the sense of schemes, Stacks 01VH.

```lean
theorem isRelativelyAmple_iff_exists_scheme {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hLinv : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property L)
    (V : BigFppfOver B S hS) (eY : Y.1 ≅ yoneda.obj V) :
    IsRelativelyAmple B S hS f L ↔
      ∃ (U : BigFppfOver B S hS) (eX : yoneda.obj U ≅ X.1)
        (hL : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
          (baseChangeModule B S hS L U eX.hom)),
        @Stacks.RelativeAmple.IsRelativelyAmple _ _
          ((BigFppfOver.toScheme B S hS).map (yoneda.preimage (eX.hom ≫ f.hom ≫ eY.hom)))
          (baseChangeModule B S hS L U eX.hom) hL
```

## Tag 0D33, a lemma

[Tag 0D33](https://stacks.math.columbia.edu/tag/0D33) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyAmple_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L267).

> **Stacks 0D33.** Relative ampleness is stable under arbitrary base change of algebraic
> spaces: if `L` is `f`-ample and `f' : X' ⟶ Y'` is the base change of `f : X ⟶ Y` along
> `Y' ⟶ Y`, then the pullback of `L` to `X'` is `f'`-ample.

```lean
theorem isRelativelyAmple_baseChange {X Y X' Y' : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {g : Y' ⟶ Y} {p : X' ⟶ X} {f' : X' ⟶ Y'} (hsq : IsPullback p f' f g)
    (L : Modules.{u, u} B S hS X.1 X.2) (hL : IsRelativelyAmple B S hS f L) :
    IsRelativelyAmple B S hS f' ((modulePullback B S hS p).obj L)
```

## Tag 0D34, a lemma

[Tag 0D34](https://stacks.math.columbia.edu/tag/0D34) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativelyAmple.relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L192). The attribute's comment: “representable”.

> **Stacks 0D34, representability.** A relatively ample module is ample relative to a
> representable morphism.

```lean
theorem IsRelativelyAmple.relativelyRepresentable {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {L : Modules.{u, u} B S hS X.1 X.2} (h : IsRelativelyAmple B S hS f L) :
    yoneda.relativelyRepresentable f.hom
```

**`AlgebraicGeometry.Space.IsRelativelyAmple.isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L236). The attribute's comment: “quasi-compact”.

> **Stacks 0D34, quasi-compactness.** A morphism of algebraic spaces admitting a relatively
> ample module is quasi-compact.
>
> Relative ampleness on a scheme contains quasi-compactness of the morphism, so every scheme base
> change of `f` is quasi-compact; for a representable morphism that is quasi-compactness of `f`
> itself, by `AlgebraicGeometry.Space.presheaf_quasiCompact_iff_isQuasiCompact` (Stacks 03HD).

```lean
theorem IsRelativelyAmple.isQuasiCompact {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {L : Modules.{u, u} B S hS X.1 X.2} (h : IsRelativelyAmple B S hS f L) :
    IsQuasiCompact B S hS f.hom
```

**`AlgebraicGeometry.Space.IsRelativelyAmple.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L253). The attribute's comment: “separated”. References: EGA II (4.6.3), “more general”.

> **Stacks 0D34, separatedness.** A morphism of algebraic spaces admitting a relatively ample
> module is separated.
>
> Every scheme base change of `f` carries a relatively ample invertible module, hence is a
> separated morphism of schemes by Stacks 01VI
> (`AlgebraicGeometry.Scheme.Modules.IsRelativelyAmple.isSeparated`); for a representable
> morphism that is separatedness of `f` itself, by `AlgebraicGeometry.Space.isSeparated_iff_presheaf`
> (Stacks 03KY).

```lean
theorem IsRelativelyAmple.isSeparated {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {L : Modules.{u, u} B S hS X.1 X.2} (h : IsRelativelyAmple B S hS f L) :
    IsSeparated B S hS f.hom
```

## Tag 0D35, a lemma

[Tag 0D35](https://stacks.math.columbia.edu/tag/0D35) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyAmple_of_isRelativelyAmple_baseChange_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleEtaleSourceScheme.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleEtaleSourceScheme.lean#L294). The attribute's comment: “(2) implies (1)”.

> **Stacks 0D35, (2) implies (1).** Let `g : V ⟶ U` be a morphism of algebraic spaces which
> are the affine schemes `V₀` and `U₀`, induced by a surjective étale `h₀ : V₀ ⟶ U₀`, let
> `f : X ⟶ U` be a morphism of algebraic spaces, let `L` be an invertible `𝒪_X`-module and let
> `pr : Y ⟶ X`, `f' : Y ⟶ V` present `Y` as `V ×_U X`. If the pullback of `L` to `Y` is ample on
> `Y/V`, then `L` is ample on `X/U`.
>
> The source `X` is a scheme by
> `AlgebraicGeometry.Space.isRepresentable_of_isRelativelyAmple_baseChange_etale`, and then
> ampleness descends along `V₀ ⟶ U₀` by
> `AlgebraicGeometry.Space.isRelativelyAmple_of_baseChange_etale_of_isRepresentable`.

```lean
theorem isRelativelyAmple_of_isRelativelyAmple_baseChange_etale (hsq : IsPullback pr f' f g)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hLinv : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property L)
    (U₀ V₀ : BigFppfOver B S hS) (hU₀ : IsAffine ((BigFppfOver.toScheme B S hS).obj U₀))
    (hV₀ : IsAffine ((BigFppfOver.toScheme B S hS).obj V₀))
    (eU : U.1 ≅ yoneda.obj U₀) (eV : V.1 ≅ yoneda.obj V₀)
    (h₀ : V₀ ⟶ U₀) (hg : g.hom ≫ eU.hom = eV.hom ≫ yoneda.map h₀)
    (hsurj : Surjective ((BigFppfOver.toScheme B S hS).map h₀))
    (hetale : Etale ((BigFppfOver.toScheme B S hS).map h₀))
    (hN : IsRelativelyAmple B S hS f' ((modulePullback B S hS pr).obj L)) :
    IsRelativelyAmple B S hS f L
```

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_isRelativelyAmple_baseChange_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleEtaleSourceScheme.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleEtaleSourceScheme.lean#L323).

> **Stacks 0D35.** Let `g : V ⟶ U` be a morphism of algebraic spaces which are the affine
> schemes `V₀` and `U₀`, induced by a surjective étale morphism `h₀ : V₀ ⟶ U₀`, let `f : X ⟶ U` be
> a morphism of algebraic spaces, let `L` be an invertible `𝒪_X`-module and let `pr : Y ⟶ X`,
> `f' : Y ⟶ V` present `Y` as `V ×_U X`. The following are equivalent:
>
> 1. `L` is ample on `X/U`;
> 2. the pullback of `L` to `Y` is ample on `Y/V`.
>
> Clause (1) implies clause (2) by [Stacks, Tag 0D33],
> `AlgebraicGeometry.Space.isRelativelyAmple_baseChange`, and the converse is
> `AlgebraicGeometry.Space.isRelativelyAmple_of_isRelativelyAmple_baseChange_etale`.

```lean
theorem isRelativelyAmple_iff_isRelativelyAmple_baseChange_etale (hsq : IsPullback pr f' f g)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hLinv : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property L)
    (U₀ V₀ : BigFppfOver B S hS) (hU₀ : IsAffine ((BigFppfOver.toScheme B S hS).obj U₀))
    (hV₀ : IsAffine ((BigFppfOver.toScheme B S hS).obj V₀))
    (eU : U.1 ≅ yoneda.obj U₀) (eV : V.1 ≅ yoneda.obj V₀)
    (h₀ : V₀ ⟶ U₀) (hg : g.hom ≫ eU.hom = eV.hom ≫ yoneda.map h₀)
    (hsurj : Surjective ((BigFppfOver.toScheme B S hS).map h₀))
    (hetale : Etale ((BigFppfOver.toScheme B S hS).map h₀)) :
    IsRelativelyAmple B S hS f L ↔
      IsRelativelyAmple B S hS f' ((modulePullback B S hS pr).obj L)
```

## Tag 0D36, a lemma

[Tag 0D36](https://stacks.math.columbia.edu/tag/0D36) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isAmpleOnBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean#L110). The attribute's comment: “parts (1) and (2), which the source calls equivalent by definition and which the library's Tag 0D31 predicate makes so here too”.

> **Stacks 0D36, parts (1) and (2).** A module is ample relative to `f : X ⟶ Y` precisely when
> every base change of `f` along a scheme of the site is represented by a scheme carrying a
> relatively ample pullback of the module.
>
> The two conditions are the same after unfolding: relative representability of `f` is the
> existence of the cartesian squares, and the ampleness clause is imposed on the same squares by
> both sides.

```lean
theorem isRelativelyAmple_iff_forall_isAmpleOnBaseChange {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (L : Modules.{u, u} B S hS X.1 X.2) :
    IsRelativelyAmple B S hS f L ↔
      ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y.1),
        IsAmpleOnBaseChange B S hS f L T g
```

**`AlgebraicGeometry.Space.isAmpleOnBaseChange_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean#L128). The attribute's comment: “part (1) implies part (2) at a single base change, hence part (1) implies part (3) by restriction to affine Z”.

> **Stacks 0D36, part (1) implies part (3).** For a relatively ample module the base change of
> `f` along any scheme of the site is a scheme carrying a relatively ample pullback; part (3) of
> Stacks 0D36 is this restricted to the affine objects of the site.

```lean
theorem isAmpleOnBaseChange_of_isRelativelyAmple {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {L : Modules.{u, u} B S hS X.1 X.2} (h : IsRelativelyAmple B S hS f L)
    (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y.1) :
    IsAmpleOnBaseChange B S hS f L T g
```

**`AlgebraicGeometry.Space.exists_etaleChart_isAmpleOnBaseChange_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean#L140). The attribute's comment: “part (1) implies part (4): a surjective etale chart of the base over which the pullback is a scheme with ample pullback”.

> **Stacks 0D36, part (1) implies part (4).** A module ample relative to `f : X ⟶ Y` admits a
> scheme `V` of the site and a surjective étale morphism `yoneda.obj V ⟶ Y` over which the base
> change of `f` is a scheme carrying a relatively ample pullback of the module: any atlas of `Y`
> (Stacks 025Y) will do.

```lean
theorem exists_etaleChart_isAmpleOnBaseChange_of_isRelativelyAmple
    {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y} {L : Modules.{u, u} B S hS X.1 X.2}
    (h : IsRelativelyAmple B S hS f L) :
    ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) g ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) g ∧
      IsAmpleOnBaseChange B S hS f L V g
```

**`AlgebraicGeometry.Space.relativelyRepresentable_of_forall_affine_isAmpleOnBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean#L164). The attribute's comment: “part (3) implies the REPRESENTABILITY clause of part (2) — every base change to a scheme is a scheme — unconditionally. The ampleness clause of that implication is not proved here; see `isRelativelyAmple_tfae_of_isInvertible`”.

> **Stacks 0D36, the schematic half of part (3) implies part (2).** If the base change of
> `f : X ⟶ Y` along every affine object of the site is a scheme, then the base change of `f` along
> every object of the site is a scheme.
>
> Relative representability may be tested on the affine objects of the site, by
> `AlgebraicGeometry.Space.presheaf_of_affineBaseChange` for the property `⊤` of morphisms of
> schemes; this is the half of the implication that the source takes from Stacks 03JH.

```lean
theorem relativelyRepresentable_of_forall_affine_isAmpleOnBaseChange
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (L : Modules.{u, u} B S hS X.1 X.2)
    (h : ∀ (T : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
      ∀ g : yoneda.obj T ⟶ Y.1, IsAmpleOnBaseChange B S hS f L T g) :
    yoneda.relativelyRepresentable f.hom
```

**`AlgebraicGeometry.Space.isRelativelyAmple_tfae_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteriaComplete.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteriaComplete.lean#L473).

> **Stacks 0D36.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and `L` an
> invertible `𝒪_X`-module. The following are equivalent:
>
> 1. `L` is ample on `X/Y`;
> 2. for every scheme `T` of the site and every morphism `T ⟶ Y` the algebraic space
>    `X_T = T ×_Y X` is a scheme and the pullback `L_T` is ample on `X_T/T`;
> 3. for every affine scheme `T` of the site and every morphism `T ⟶ Y` the algebraic space `X_T`
>    is a scheme and `L_T` is ample on `X_T/T`;
> 4. there are a scheme `V` of the site and a surjective étale morphism `V ⟶ Y` such that `X_V` is
>    a scheme and `L_V` is ample on `X_V/V`.
>
> Clause (2) at `T ⟶ Y` is `AlgebraicGeometry.Space.IsAmpleOnBaseChange`; see
> `StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleBaseChangeCriteria.lean` for that spelling.
> Clause (3) implies clause (2) is
> `AlgebraicGeometry.Space.isAmpleOnBaseChange_of_forall_affine` (Stacks 03JH and 01VJ), and
> clause (4) implies clause (3) is `AlgebraicGeometry.Space.isAmpleOnBaseChange_of_exists_etaleChart`
> (Stacks 0D35).

```lean
theorem isRelativelyAmple_tfae_of_isInvertible {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hLinv : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS X.1 X.2).O)).property L) :
    List.TFAE
      [IsRelativelyAmple B S hS f L,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y.1),
          IsAmpleOnBaseChange B S hS f L T g,
        ∀ (T : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          ∀ g : yoneda.obj T ⟶ Y.1, IsAmpleOnBaseChange B S hS f L T g,
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) g ∧
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@Etale.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) g ∧
          IsAmpleOnBaseChange B S hS f L V g]
```

## Tag 0GUQ, a lemma

[Tag 0GUQ](https://stacks.math.columbia.edu/tag/0GUQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiAffineHom_iff_isRelativelyAmple_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmple.lean#L311). References: EGA II (5.1.6), “more general”.

> **Stacks 0GUQ.** A morphism `f : X ⟶ Y` of algebraic spaces is quasi-affine if and only if
> the structure sheaf `𝒪_X` is `f`-relatively ample.
>
> Quasi-affineness of Stacks 03WL is identified with its representable form by
> `AlgebraicGeometry.Space.isQuasiAffineHom_tfae_of_isAlgebraicSpace`, and that form quantifies
> over exactly the cartesian squares relative ampleness does; on each of them the equivalence is
> the scheme-level Stacks 0891 in the shape
> `Stacks.AmplePullback.isRelativelyAmple_iff_isQuasiAffineHom_of_iso_unitModule`, applied through
> `AlgebraicGeometry.Space.baseChangeUnitModuleIso`.

```lean
theorem isQuasiAffineHom_iff_isRelativelyAmple_unit {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    IsQuasiAffineHom B S hS f.hom ↔
      IsRelativelyAmple B S hS f
        (SheafOfModules.unit
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.14, Tag 0D30](https://stacks.math.columbia.edu/tag/0D30)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
