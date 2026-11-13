---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_etale_decomposition_isFinite_of_isQuasiFiniteAt, AlgebraicGeometry.Space.exists_etale_finite_clopen_part, AlgebraicGeometry.Space.exists_etale_decomposition_isFinite_point_of_isQuasiFiniteAt
statement: formalized
proof: formalized
---

# 76.33 Étale localization of morphisms

Section 76.33 of the Stacks Project, [Tag 082G](https://stacks.math.columbia.edu/tag/082G). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 082H, a lemma

[Tag 082H](https://stacks.math.columbia.edu/tag/082H) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etale_decomposition_isFinite_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSplitQuasiFinitePart.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSplitQuasiFinitePart.lean#L338).

> **Stacks Project, Tag 082H.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`,
> let `y` be a point of `|Y|` and let `x₁, …, x_n` be points of `|X|` mapping to `y`. Assume that
> `f` is locally of finite type, that `f` is separated, that `f` is quasi-finite at each `xᵢ`, and
> that `f` is quasi-compact or `Y` is decent. Then there are an object `U` of the big fppf category
> over `S`, an **étale** morphism `g : h_U ⟶ Y` and a point `u` of `|h_U|` over `y`, together with a
> decomposition of `U ×_Y X` into two open-and-closed subspaces `W` and `V` — their join sheafifies
> to everything and their meet is the sheafification of nothing — such that
>
> * `V ⟶ U` is **finite**;
> * every point of the fibre of `|V| ⟶ |U|` over `u` maps to one of the `xᵢ`;
> * no point of the fibre of `|W| ⟶ |U|` over `u` maps to any `xᵢ`.
>
> This is the composite of the three paragraphs of the source proof with its finiteness clause; see
> the module documentation for which file carries which. The hypotheses are those of the tag and
> nothing else, apart from the ambient `HasSheafify` assumption on the site discussed there.

```lean
theorem exists_etale_decomposition_isFinite_of_isQuasiFiniteAt
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (y : points B S hS Y) {n : ℕ} (x : Fin n → points B S hS X)
    (hx : ∀ i, pointsMap B S hS X f (x i) = y)
    (hft : IsLocallyOfFiniteType B S hS f) (hsep : IsSeparated B S hS f)
    (hqf : ∀ i, IsQuasiFiniteAt B S hS f (x i))
    (hqc : IsQuasiCompact B S hS f ∨ IsDecentSpace B S hS Y) :
    ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y)
      (u : points B S hS (yoneda.obj U)) (W V : Subfunctor (pullback g f)),
      IsEtale B S hS g ∧
      pointsMap B S hS (yoneda.obj U) g u = y ∧
      IsOpenSubspace B S hS W ∧ IsClosedSubspace B S hS W ∧
      IsOpenSubspace B S hS V ∧ IsClosedSubspace B S hS V ∧
      (W ⊔ V).sheafify (BigFppfOver.topology B S hS) = ⊤ ∧
      W ⊓ V = (⊥ : Subfunctor (pullback g f)).sheafify (BigFppfOver.topology B S hS) ∧
      IsFinite B S hS (V.ι ≫ pullback.fst g f) ∧
      (∀ v : points B S hS V.toFunctor,
        pointsMap B S hS V.toFunctor (V.ι ≫ pullback.fst g f) v = u →
          ∃ i, pointsMap B S hS V.toFunctor (V.ι ≫ pullback.snd g f) v = x i) ∧
      (∀ t : points B S hS W.toFunctor,
        pointsMap B S hS W.toFunctor (W.ι ≫ pullback.fst g f) t = u →
          ∀ i, pointsMap B S hS W.toFunctor (W.ι ≫ pullback.snd g f) t ≠ x i)
```

## Tag 0ADU, a lemma

[Tag 0ADU](https://stacks.math.columbia.edu/tag/0ADU) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etale_finite_clopen_part`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleQuasiFinitePart.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleQuasiFinitePart.lean#L383).

> **Stacks 0ADU.** An étale neighbourhood of the image of `x` splits the pullback into two
> open-and-closed parts, one of them finite over the neighbourhood and containing a point above
> `x`.

```lean
public theorem exists_etale_finite_clopen_part
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (x : points B S hS X.1)
    (hft : IsLocallyOfFiniteType B S hS f.hom)
    (hsep : IsSeparated B S hS f.hom)
    (hqf : IsQuasiFiniteAt B S hS f.hom x) :
    ∃ (U : AlgebraicSpaces B S hS) (g : U ⟶ Y)
      (u : points B S hS U.1)
      (W V : Subfunctor (pullback g.hom f.hom)),
      IsEtale B S hS g.hom ∧
      pointsMap B S hS U.1 g.hom u = pointsMap B S hS X.1 f.hom x ∧
      IsOpenSubspace B S hS W ∧
      IsClosedSubspace B S hS W ∧
      IsOpenSubspace B S hS V ∧
      IsClosedSubspace B S hS V ∧
      (W ⊔ V).sheafify (BigFppfOver.topology B S hS) = ⊤ ∧
      W ⊓ V = (⊥ : Subfunctor (pullback g.hom f.hom)).sheafify
        (BigFppfOver.topology B S hS) ∧
      IsFinite B S hS (V.ι ≫ pullback.fst g.hom f.hom) ∧
      ∃ v : points B S hS V.toFunctor,
        pointsMap B S hS V.toFunctor (V.ι ≫ pullback.snd g.hom f.hom) v = x ∧
        pointsMap B S hS V.toFunctor (V.ι ≫ pullback.fst g.hom f.hom) v = u
```

**`AlgebraicGeometry.Space.exists_etale_decomposition_isFinite_point_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSplitQuasiFinitePoint.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSplitQuasiFinitePoint.lean#L202).

> **Stacks Project, Tag 0ADU.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`,
> let `x` be a point of `|X|` and let `y` be its image in `|Y|`. Assume that `f` is locally of
> finite type, that `f` is separated and that `f` is quasi-finite at `x`. Then there are an object
> `U` of the big fppf category over `S`, an **étale** morphism `g : h_U ⟶ Y` and a point `u` of
> `|h_U|` over `y`, together with a decomposition of `U ×_Y X` into two open-and-closed subspaces
> `W` and `V` — their join sheafifies to everything and their meet is the sheafification of
> nothing — such that `V ⟶ U` is **finite** and some point of `|V|` lies over `x` in `|X|` and
> over `u` in `|U|`.
>
> This is the single-point case of Stacks 082H,
> `AlgebraicGeometry.Space.exists_etale_decomposition_isFinite_of_isQuasiFiniteAt`, applied over
> an étale scheme chart of `Y` through `y`; see the module documentation for how the extra
> hypothesis of that lemma and its standing `HasSheafify` assumption on the site are both
> discharged. The hypotheses are those of the tag and nothing else.

```lean
theorem exists_etale_decomposition_isFinite_point_of_isQuasiFiniteAt
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (x : points B S hS X) (y : points B S hS Y)
    (hxy : pointsMap B S hS X f x = y)
    (hft : IsLocallyOfFiniteType B S hS f) (hsep : IsSeparated B S hS f)
    (hqf : IsQuasiFiniteAt B S hS f x) :
    ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y)
      (u : points B S hS (yoneda.obj U)) (W V : Subfunctor (pullback g f)),
      IsEtale B S hS g ∧
      pointsMap B S hS (yoneda.obj U) g u = y ∧
      IsOpenSubspace B S hS W ∧ IsClosedSubspace B S hS W ∧
      IsOpenSubspace B S hS V ∧ IsClosedSubspace B S hS V ∧
      (W ⊔ V).sheafify (BigFppfOver.topology B S hS) = ⊤ ∧
      W ⊓ V = (⊥ : Subfunctor (pullback g f)).sheafify (BigFppfOver.topology B S hS) ∧
      IsFinite B S hS (V.ι ≫ pullback.fst g f) ∧
      ∃ v : points B S hS V.toFunctor,
        pointsMap B S hS V.toFunctor (V.ι ≫ pullback.snd g f) v = x ∧
        pointsMap B S hS V.toFunctor (V.ι ≫ pullback.fst g f) v = u
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.33, Tag 082G](https://stacks.math.columbia.edu/tag/082G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
