---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FlatFppf.siteFunctor, AlgebraicGeometry.Stack.FlatFppf.siteFunctor_isContinuous, AlgebraicGeometry.Stack.FlatFppf.siteFunctor_isCocontinuous, AlgebraicGeometry.Stack.LisseEtale.siteFunctor, AlgebraicGeometry.Stack.LisseEtale.siteFunctor_isContinuous, AlgebraicGeometry.Stack.LisseEtale.siteFunctor_isCocontinuous, AlgebraicGeometry.Stack.FlatFppf.primedPushforwardAmbientEquiv', AlgebraicGeometry.Stack.LisseEtale.primedPushforwardAmbientEquiv'
statement: formalized
proof: formalized
---

# 103.15 Functoriality of the lisse-étale and flat-fppf sites

Section 103.15 of the Stacks Project, [Tag 0GR1](https://stacks.math.columbia.edu/tag/0GR1). 4 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07AT, a lemma

[Tag 07AT](https://stacks.math.columbia.edu/tag/07AT) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.siteFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean#L261). The attribute's comment: “the functor of flat-fppf sites along a flat 1-morphism”.

> The restriction of a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` to a functor
> between the flat-fppf sites, specified by the property that its composite with the inclusion of
> the flat objects of `𝒴` is the inclusion of those of `𝒳` followed by the underlying functor of
> `f`.

```lean
def siteFunctor (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFlat B S hS f) :
    {F : FlatFppf B S hS 𝒳 ⥤ FlatFppf B S hS 𝒴 //
      F ⋙ inclusion B S hS 𝒴 =
        inclusion B S hS 𝒳 ⋙ f.hom.hom.toFunctor}
```

**`AlgebraicGeometry.Stack.FlatFppf.siteFunctor_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean#L287). The attribute's comment: “that functor is continuous”.

> The restriction of a flat 1-morphism to the flat-fppf sites is continuous.

```lean
theorem siteFunctor_isContinuous (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFlat B S hS f) :
    (siteFunctor B S hS f hf).1.IsContinuous
      (topology B S hS 𝒳) (topology B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.FlatFppf.siteFunctor_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean#L309). The attribute's comment: “that functor is cocontinuous”.

> The restriction of a flat 1-morphism to the flat-fppf sites is cocontinuous.

```lean
theorem siteFunctor_isCocontinuous (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFlat B S hS f) :
    (siteFunctor B S hS f hf).1.IsCocontinuous
      (topology B S hS 𝒳) (topology B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.LisseEtale.siteFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean#L143). The attribute's comment: “the functor of lisse-etale sites along a smooth 1-morphism”.

> **Stacks 07AT** (1), the site functor. A smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> over `S` restricts to a functor between the lisse-étale sites, specified by the property that its
> composite with the inclusion of the smooth objects of `𝒴` is the inclusion of those of `𝒳`
> followed by the underlying functor of `f`.
>
> The restriction exists because `f` carries smooth objects to smooth objects
> (`AlgebraicGeometry.Stack.LisseEtale.smoothObject_map`), and that equality of composites is what
> says its action on objects and arrows is the action of `f`.

```lean
def siteFunctor (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsSmooth B S hS f) :
    {F : LisseEtale.{u, w} B S hS 𝒳 ⥤ LisseEtale.{u, w} B S hS 𝒴 //
      F ⋙ inclusion.{u, w} B S hS 𝒴 =
        inclusion.{u, w} B S hS 𝒳 ⋙ f.hom.hom.toFunctor}
```

**`AlgebraicGeometry.Stack.LisseEtale.siteFunctor_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean#L155). The attribute's comment: “that functor is continuous, in the smooth case”.

> **Stacks 07AT** (1), continuity. The restriction of a smooth 1-morphism to the lisse-étale
> sites is continuous: its composite with the inclusion of `𝒴` is, and continuity descends along
> that inclusion, which is fully faithful and cocontinuous by **Stacks 0788** (1).

```lean
theorem siteFunctor_isContinuous (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsSmooth B S hS f) :
    (siteFunctor.{u, w} B S hS f hf).1.IsContinuous
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.LisseEtale.siteFunctor_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean#L174). The attribute's comment: “that functor is cocontinuous, in the smooth case”.

> **Stacks 07AT** (1), cocontinuity. The same descent, with the roles of continuity and
> cocontinuity of the inclusion exchanged.

```lean
theorem siteFunctor_isCocontinuous (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsSmooth B S hS f) :
    (siteFunctor.{u, w} B S hS f hf).1.IsCocontinuous
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.FlatFppf.primedPushforwardAmbientEquiv'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardAmbientUnconditional.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardAmbientUnconditional.lean#L176). The attribute's comment: “part (2), the identity `f'_*(g')^{-1} = g^{-1}f_*` for the flat-fppf site, at one flat object `y` of `𝒴` and for a sheaf of sets, with NO hypothesis beyond the sheaf condition on `ℱ`: the topology on the 2-fibre product `V ×_{y, 𝒴} 𝒳` that `AlgebraicGeometry.Stack.FlatFppf.primedPushforwardAmbientEquiv` takes as `J` is `AlgebraicGeometry.Stack.ambientTwoFibreProductTopology`, and its arguments `hℱ`, `hfac` and `hconn` are the theorems `AlgebraicGeometry.Stack.isSheaf_comp_ambientProjection`, `AlgebraicGeometry.Stack.FlatFppf.hasLocalFactorizations_primedInclusion` and `AlgebraicGeometry.Stack.FlatFppf.hasLocallyConnectedFactorizations_primedInclusion`, each proved for every algebraic stack. The site functor itself and its continuity and cocontinuity, which are the first assertion of the tag, are registered in `StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean`. Three pieces of the tag are not covered here: naturality of the bijection in `y`, so that it becomes an equality of sheaves on `𝒴_{flat,fppf}` rather than a family of bijections; the same identity at abelian rather than set coefficients; and the second identity `g'_!(f')^{-1} = f^{-1}g_!`. The first and the third are registered in `StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean`; the abelian form is claimed nowhere in the tree, and the tag does not ask for it -- the source's `ℱ` is a sheaf of sets, which is what the functors of a morphism of topoi act on”.

> **Stacks 07AT (2), the identity `f'_*(g')^{-1} = g^{-1}f_*`, at one flat object of `𝒴` and
> for a sheaf of sets, with no further hypothesis.** For a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks, a flat object `y` of `𝒴` and a sheaf `ℱ` of sets on the fppf site of `𝒳`, the value at
> `y` of the pushforward along the restriction `f'` of `f` to the flat-fppf sites of the restriction
> of `ℱ` to the flat-fppf site of `𝒳` is the value at `y` of the pushforward of `ℱ` along `f`.
>
> This is `AlgebraicGeometry.Stack.FlatFppf.primedPushforwardAmbientEquiv` at the topology of
> `AlgebraicGeometry.Stack.ambientTwoFibreProductTopology`, whose three remaining inputs are
> `AlgebraicGeometry.Stack.isSheaf_comp_ambientProjection`,
> `AlgebraicGeometry.Stack.FlatFppf.hasLocalFactorizations_primedInclusion` and
> `AlgebraicGeometry.Stack.FlatFppf.hasLocallyConnectedFactorizations_primedInclusion`.

```lean
def primedPushforwardAmbientEquiv' (hf : AlgebraicStacks.IsFlat B S hS f)
    (y : FlatFppf B S hS 𝒴) (ℱ : (𝒳.val.val.obj)ᵒᵖ ⥤ Type (u + 1))
    (hℱ : Presieve.IsSheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf) ℱ) :
    ((primedSiteFunctor B S hS f hf).op.ran.obj ((inclusion B S hS 𝒳).op ⋙ ℱ)).obj (op y) ≃
      (f.hom.hom.toFunctor.op.ran.obj ℱ).obj (op y.obj)
```

**`AlgebraicGeometry.Stack.LisseEtale.primedPushforwardAmbientEquiv'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardAmbientUnconditional.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardAmbientUnconditional.lean#L246). The attribute's comment: “part (1), the identity `f'_*(g')^{-1} = g^{-1}f_*` for the lisse-étale site, at one smooth object `y` of `𝒴` and for a sheaf of sets, with NO hypothesis beyond the sheaf condition on `ℱ`: the topology on the 2-fibre product `V ×_{y, 𝒴} 𝒳` that `AlgebraicGeometry.Stack.LisseEtale.primedPushforwardAmbientEquiv` takes as `J` is `AlgebraicGeometry.Stack.ambientTwoFibreProductTopology`, and its arguments `hℱ`, `hfac` and `hconn` are the theorems `AlgebraicGeometry.Stack.isSheaf_comp_ambientProjection`, `AlgebraicGeometry.Stack.LisseEtale.hasLocalFactorizations_primedInclusion` and `AlgebraicGeometry.Stack.LisseEtale.hasLocallyConnectedFactorizations_primedInclusion`, each proved for every algebraic stack. The site functor itself and its continuity and cocontinuity, which are the first assertion of the tag, are registered in `StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean`. Three pieces of the tag are not covered here: naturality of the bijection in `y`, so that it becomes an equality of sheaves on `𝒴_{lisse,étale}` rather than a family of bijections; the same identity at abelian rather than set coefficients; and the second identity `g'_!(f')^{-1} = f^{-1}g_!`. The first and the third are registered in `StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean`; the abelian form is claimed nowhere in the tree, and the tag does not ask for it -- the source's `ℱ` is a sheaf of sets, which is what the functors of a morphism of topoi act on”.

> **Stacks 07AT (1), the identity `f'_*(g')^{-1} = g^{-1}f_*`, at one smooth object of `𝒴` and
> for a sheaf of sets, with no further hypothesis.** For a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks, a smooth object `y` of `𝒴` and a sheaf `ℱ` of sets on the étale site of `𝒳`,
> the value at `y` of the pushforward along the restriction `f'` of `f` to the lisse-étale sites of
> the restriction of `ℱ` to the lisse-étale site of `𝒳` is the value at `y` of the pushforward of
> `ℱ` along `f`.
>
> This is `AlgebraicGeometry.Stack.LisseEtale.primedPushforwardAmbientEquiv` at the topology of
> `AlgebraicGeometry.Stack.ambientTwoFibreProductTopology`, whose three remaining inputs are
> `AlgebraicGeometry.Stack.isSheaf_comp_ambientProjection`,
> `AlgebraicGeometry.Stack.LisseEtale.hasLocalFactorizations_primedInclusion` and
> `AlgebraicGeometry.Stack.LisseEtale.hasLocallyConnectedFactorizations_primedInclusion`.

```lean
def primedPushforwardAmbientEquiv' (hf : AlgebraicStacks.IsSmooth B S hS f)
    (y : LisseEtale.{u, w} B S hS 𝒴) (ℱ : (𝒳.val.val.obj)ᵒᵖ ⥤ Type (u + 1))
    (hℱ : Presieve.IsSheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale) ℱ) :
    ((primedSiteFunctor.{u, w} B S hS f hf).op.ran.obj
        ((inclusion.{u, w} B S hS 𝒳).op ⋙ ℱ)).obj (op y) ≃
      (f.hom.hom.toFunctor.op.ran.obj ℱ).obj (op y.obj)
```

**`AlgebraicGeometry.Stack.LisseEtale.siteFunctorRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L226). The attribute's comment: “part (1), clause (d): the restriction `f'` of a smooth 1-morphism to the lisse-étale sites is a morphism of ringed topoi, at the universe in which the structure sheaf of Stacks 06TV takes its sections. Its structure map is the canonical identification of the two restricted structure sheaves”.

> **Stacks 07AT** (1), clause (d). **The restriction `f'` of a smooth 1-morphism to the
> lisse-étale sites is a morphism of ringed topoi.** Its inverse image is restriction along the site
> functor, and its structure map is the canonical identification of the two lisse-étale structure
> sheaves: both are restrictions of the structure sheaf of **Stacks 06TV** of the base, along the
> two composites of the square, which agree on the nose.

```lean
def siteFunctorRingedToposHom (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsSmooth B S hS f) :
    RingedToposHom
      (ringedTopos.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳))
      (ringedTopos.{u, w} B S hS 𝒴 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒴))
```

**`AlgebraicGeometry.Stack.LisseEtale.isIso_fSharpInverseImage_siteFunctorRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L248). The attribute's comment: “part (1), clause (d): the structure map of `f'` on the lisse-étale sites is an isomorphism, so `f'` is a flat morphism of ringed topoi”.

> **Stacks 07AT** (1), clause (d). The structure map of `f'` is an isomorphism: it is the
> canonical identification of the two restricted structure sheaves.

```lean
theorem isIso_fSharpInverseImage_siteFunctorRingedToposHom (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsSmooth B S hS f) :
    IsIso (siteFunctorRingedToposHom.{u, w} B S hS f hf).fSharpInverseImage
```

**`AlgebraicGeometry.Stack.LisseEtale.ringedSquareTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L367). The attribute's comment: “part (1), clause (e): the square of ringed topoi formed by `f`, its restriction `f'` to the lisse-étale sites and the two inclusions `g`, `g'` of Stacks 0788 2-commutes. The invertible 2-morphism is the adjoint mate of the canonical morphism of the equality of the two inverse images”.

> **Stacks 07AT** (1), clause (e). **The square of ringed topoi 2-commutes**: the composite
> `g' ∘ f'` and the composite `f ∘ g` are 2-isomorphic as morphisms of ringed topoi
> `(Sh(𝒳_{lisse,étale}), O) ⟶ (Sh(𝒴_{étale}), O)`.
>
> The 2-isomorphism is the adjoint mate of the canonical morphism of
> `AlgebraicGeometry.Stack.LisseEtale.ringedSquare_inverseImage_eq`: the two ways around the square
> restrict along the same functor of sites, so their inverse images are *equal*, and every structure
> map in sight is the restriction comparison followed by an equality of structure sheaves, hence a
> transport. Compatibility of the mate with the structure maps is then automatic, both sides of it
> being transports between the same two objects.

```lean
def ringedSquareTwoIso (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsSmooth B S hS f) :
    RingedToposHom.TwoIso
      (A := ringedTopos.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳))
      (B := etaleRingedTopos.{u, w} B S hS 𝒴)
      (ringedSquareDownAcross.{u, w} B S hS f)
      (ringedSquareAcrossDown.{u, w} B S hS f hf)
```

**`AlgebraicGeometry.Stack.FlatFppf.siteFunctorRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L425). The attribute's comment: “part (2), clause (d): the restriction `f'` of a flat 1-morphism to the flat-fppf sites is a morphism of ringed topoi, at the universe in which the structure sheaf of Stacks 06TV takes its sections. Its structure map is the canonical identification of the two restricted structure sheaves”.

> **Stacks 07AT** (2), clause (d). **The restriction `f'` of a flat 1-morphism to the flat-fppf
> sites is a morphism of ringed topoi.** Its inverse image is restriction along the site functor,
> and its structure map is the canonical identification of the two flat-fppf structure sheaves.

```lean
def siteFunctorRingedToposHom (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFlat B S hS f) :
    RingedToposHom (ringedTopos B S hS 𝒳) (ringedTopos B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.FlatFppf.isIso_fSharpInverseImage_siteFunctorRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L442). The attribute's comment: “part (2), clause (d): the structure map of `f'` on the flat-fppf sites is an isomorphism, so `f'` is a flat morphism of ringed topoi”.

> **Stacks 07AT** (2), clause (d). The structure map of `f'` is an isomorphism.

```lean
theorem isIso_fSharpInverseImage_siteFunctorRingedToposHom (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsFlat B S hS f) :
    IsIso (siteFunctorRingedToposHom B S hS f hf).fSharpInverseImage
```

**`AlgebraicGeometry.Stack.FlatFppf.ringedSquareTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteRingedSquare.lean#L536). The attribute's comment: “part (2), clause (e): the square of ringed topoi formed by `f`, its restriction `f'` to the flat-fppf sites and the two inclusions `g`, `g'` of Stacks 0788 2-commutes. The invertible 2-morphism is the adjoint mate of the canonical morphism of the equality of the two inverse images”.

> **Stacks 07AT** (2), clause (e). **The square of ringed topoi 2-commutes**: `g' ∘ f'` and
> `f ∘ g` are 2-isomorphic as morphisms of ringed topoi
> `(Sh(𝒳_{flat,fppf}), O) ⟶ (Sh(𝒳_{fppf}), O)`, the 2-isomorphism being the adjoint mate of the
> canonical morphism of `AlgebraicGeometry.Stack.FlatFppf.ringedSquare_inverseImage_eq`.

```lean
def ringedSquareTwoIso (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFlat B S hS f) :
    RingedToposHom.TwoIso (A := ringedTopos B S hS 𝒳) (B := fppfRingedTopos B S hS 𝒴)
      (ringedSquareDownAcross B S hS f) (ringedSquareAcrossDown B S hS f hf)
```

**`AlgebraicGeometry.Stack.LisseEtale.isIso_sheafBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean#L103). The attribute's comment: “part (1), the identity `f'_*(g')^{-1} = g^{-1}f_*` for the lisse-étale site, on sheaves of sets and natural in the object of the lisse-étale site of `𝒴`: the canonical map of Sites, Section 06UM, which is `CategoryTheory.SubsitePushforward.subsiteRanBaseChange` at the square of `f`, its restriction `f'` and the two inclusions, is invertible. The site functor and its continuity and cocontinuity are registered in `StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleSiteFunctor.lean`”.

> **Stacks 07AT** (1), the identity `f'_*(g')^{-1} = g^{-1}f_*`. For a smooth 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks, the canonical map of Sites, Section 06UM from the restriction
> along the inclusion `g` of the lisse-étale site of `𝒴` of the pushforward along `f`, to the
> pushforward along the restriction `f'` of the restriction along the inclusion `g'` of the
> lisse-étale site of `𝒳`, is an isomorphism of functors on sheaves of sets.

```lean
theorem isIso_sheafBaseChange :
    IsIso (SubsitePushforward.subsiteSheafBaseChange.{_, _, _, _, u + 1} f.hom.hom.toFunctor
      (smoothObject.{u, w} B S hS 𝒳) (smoothObject_map.{u, w} B S hS f hf)
      (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
      (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).2
      (isCocontinuous_subsiteFunctor_topology.{u, w} B S hS f hf)
      (isContinuous_inclusion_topology'.{u, w} B S hS 𝒳)
      (isContinuous_inclusion_topology'.{u, w} B S hS 𝒴))
```

**`AlgebraicGeometry.Stack.LisseEtale.shriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean#L136). The attribute's comment: “part (1), the identity `g'_!(f')^{-1} = f^{-1}g_!` for the lisse-étale site, on sheaves of sets: the conjugate of the first identity along the four adjunctions, exactly as the source derives it”.

> **Stacks 07AT** (1), the identity `g'_!(f')^{-1} = f^{-1}g_!`. It is the conjugate of
> `AlgebraicGeometry.Stack.LisseEtale.isIso_sheafBaseChange` along the adjointness of `f^{-1}` and
> `f_*`, of `g_!` and `g^{-1}`, and of their primed versions.

```lean
noncomputable def shriekBaseChangeIso :
    letI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
      (etaleTopology B)).1
    letI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
      (etaleTopology B)).2
    letI := isContinuous_subsiteFunctor_topology.{u, w} B S hS f hf
    letI := isCocontinuous_subsiteFunctor_topology.{u, w} B S hS f hf
    (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardContinuous (Type (u + 1))
          (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴) ⋙
        setsShriek B S hS 𝒳 ≅
      setsShriek B S hS 𝒴 ⋙ f.hom.hom.toFunctor.sheafPushforwardContinuous (Type (u + 1))
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
```

**`AlgebraicGeometry.Stack.FlatFppf.isIso_sheafBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean#L214). The attribute's comment: “part (2), the identity `f'_*(g')^{-1} = g^{-1}f_*` for the flat-fppf site, on sheaves of sets and natural in the object of the flat-fppf site of `𝒴`: the canonical map of Sites, Section 06UM, which is `CategoryTheory.SubsitePushforward.subsiteRanBaseChange` at the square of `f`, its restriction `f'` and the two inclusions, is invertible. The site functor and its continuity and cocontinuity are registered in `StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfSiteFunctor.lean`”.

> **Stacks 07AT** (2), the identity `f'_*(g')^{-1} = g^{-1}f_*`. For a flat 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks, the canonical map of Sites, Section 06UM from the restriction
> along the inclusion `g` of the flat-fppf site of `𝒴` of the pushforward along `f`, to the
> pushforward along the restriction `f'` of the restriction along the inclusion `g'` of the
> flat-fppf site of `𝒳`, is an isomorphism of functors on sheaves of sets.

```lean
theorem isIso_sheafBaseChange :
    IsIso (SubsitePushforward.subsiteSheafBaseChange.{_, _, _, _, u + 1} f.hom.hom.toFunctor
      (objectProperty B S hS 𝒳) (flatObject_map B S hS f hf)
      (associatedTopology B S hS 𝒳.val.val.p B.topology)
      (associatedTopology B S hS 𝒴.val.val.p B.topology)
      (topology B S hS 𝒳) (topology B S hS 𝒴)
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f B.topology).2
      (isCocontinuous_subsiteFunctor_topology B S hS f hf)
      (isContinuous_inclusion_topology B S hS 𝒳)
      (isContinuous_inclusion_topology B S hS 𝒴))
```

**`AlgebraicGeometry.Stack.FlatFppf.shriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteSheafPushforwardBaseChange.lean#L247). The attribute's comment: “part (2), the identity `g'_!(f')^{-1} = f^{-1}g_!` for the flat-fppf site, on sheaves of sets: the conjugate of the first identity along the four adjunctions, exactly as the source derives it”.

> **Stacks 07AT** (2), the identity `g'_!(f')^{-1} = f^{-1}g_!`. It is the conjugate of
> `AlgebraicGeometry.Stack.FlatFppf.isIso_sheafBaseChange` along the adjointness of `f^{-1}` and
> `f_*`, of `g_!` and `g^{-1}`, and of their primed versions. The two lower-shriek adjunctions are
> the ones of **Stacks 0788** already in the tree.

```lean
noncomputable def shriekBaseChangeIso :
    letI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
      B.topology).1
    letI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
      B.topology).2
    letI := isContinuous_subsiteFunctor_topology B S hS f hf
    letI := isCocontinuous_subsiteFunctor_topology B S hS f hf
    (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (objectProperty B S hS 𝒳)
          (flatObject_map B S hS f hf)).sheafPushforwardContinuous (Type (u + 1))
          (topology B S hS 𝒳) (topology B S hS 𝒴) ⋙
        setsShriek B S hS 𝒳 ≅
      setsShriek B S hS 𝒴 ⋙ f.hom.hom.toFunctor.sheafPushforwardContinuous (Type (u + 1))
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology)
```

## Tag 07AU, an equation

[Tag 07AU](https://stacks.math.columbia.edu/tag/07AU) in the Stacks Project.

**`CategoryTheory.SubsitePushforward.subsitePushforwardSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean#L315).

> **Stacks 07AU**, equation 103.15.1.1. Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories over a
> base `𝒞` with `𝒴` fibred in groupoids, and let `𝒳' ⊆ 𝒳` and `𝒴' ⊆ 𝒴` be full subcategories such
> that `f` carries `𝒳'` into `𝒴'`, so that it restricts to `f' : 𝒳' ⥤ 𝒴'`. Then for a presheaf
> `ℋ` on `𝒳'` and an object `y` of `𝒴'` lying over `V : 𝒞`,
>
> `f'_*ℋ(y) = Γ((V ×_{y, 𝒴} 𝒳)', (pr')^{-1}ℋ)`,
>
> where `f'_*` is the right Kan extension along `f'.op`, the primed 2-fibre product is the full
> subcategory of `V ×_{y, 𝒴} 𝒳` whose objects have their `𝒳`-component in `𝒳'`, and `(pr')^{-1}`
> is restriction along the projection `pr'` to `𝒳'`.
>
> This is the source's equation for the lisse-étale and the flat-fppf site: no property of the
> subcategories beyond fullness is used, and neither the topologies nor their closure conditions
> enter the identification.

```lean
def subsitePushforwardSectionsEquiv (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (f : 𝒳 ⥤ 𝒴) (P : ObjectProperty 𝒳)
    {Q : ObjectProperty 𝒴} (hPQ : ∀ x : P.FullSubcategory, Q (f.obj x.obj))
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (hf : f ⋙ p𝒴 = p𝒳) (c : p𝒴.ChoiceOfPullbacks)
    (y : Q.FullSubcategory) (ℋ : (P.FullSubcategory)ᵒᵖ ⥤ Type w)
    [∀ G : (P.FullSubcategory)ᵒᵖ ⥤ Type w,
      (subsiteFunctor f P hPQ).op.HasPointwiseRightKanExtension G]
    [∀ G : (P.FullSubcategory)ᵒᵖ ⥤ Type w, (P.ι ⋙ f).op.HasPointwiseRightKanExtension G] :
    ((subsiteFunctor f P hPQ).op.ran.obj ℋ).obj (op y) ≃
      Presheaf.globalSections ((primedProjection p𝒳 p𝒴 f P c y).op ⋙ ℋ)
```

**`AlgebraicGeometry.Stack.FlatFppf.sheafPrimedPushforwardSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean#L424).

> **Stacks 07AU, the flat-fppf case**, equation 103.15.1.1. Let `f : 𝒳 ⟶ 𝒴` be a flat
> 1-morphism of algebraic stacks, let `ℋ` be a sheaf of sets on the flat-fppf site of `𝒳` and let
> `y` be a flat object of `𝒴` lying over the scheme `V`. The direct image of `ℋ` along the morphism
> of flat-fppf topoi induced by `f` has
>
> `f'_*ℋ(y) = Γ((V ×_{y, 𝒴} 𝒳)', (pr')^{-1}ℋ)`,
>
> the global sections of `ℋ` restricted along the projection `pr'` of the primed 2-fibre product.
> The direct image is `CategoryTheory.Functor.sheafPushforwardCocontinuous` along the site functor
> of **Stacks 07AT**, whose cocontinuity is
> `AlgebraicGeometry.Stack.FlatFppf.siteFunctor_isCocontinuous`.

```lean
def sheafPrimedPushforwardSectionsEquiv (y : FlatFppf B S hS 𝒴)
    (ℋ : Sheaf (topology B S hS 𝒳) (Type a))
    [∀ F : (FlatFppf B S hS 𝒳)ᵒᵖ ⥤ Type a,
      (primedSiteFunctor B S hS f hf).op.HasPointwiseRightKanExtension F]
    [∀ F : (FlatFppf B S hS 𝒳)ᵒᵖ ⥤ Type a,
      (inclusion B S hS 𝒳 ⋙ f.hom.hom.toFunctor).op.HasPointwiseRightKanExtension F] :
    letI : (primedSiteFunctor B S hS f hf).IsCocontinuous
        (topology B S hS 𝒳) (topology B S hS 𝒴) :=
      siteFunctor_isCocontinuous B S hS f hf
    ((((primedSiteFunctor B S hS f hf).sheafPushforwardCocontinuous (Type a)
        (topology B S hS 𝒳) (topology B S hS 𝒴)).obj ℋ).obj.obj (op y)) ≃
      Presheaf.globalSections ((primedProjection B S hS f y).op ⋙ ℋ.obj)
```

**`AlgebraicGeometry.Stack.LisseEtale.sheafPrimedPushforwardSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsitePushforwardFormula.lean#L513).

> **Stacks 07AU, the lisse-étale case**, equation 103.15.1.1. Let `f : 𝒳 ⟶ 𝒴` be a smooth
> 1-morphism of algebraic stacks, let `ℋ` be a sheaf of sets on the lisse-étale site of `𝒳` and let
> `y` be a smooth object of `𝒴` lying over the scheme `V`. The direct image of `ℋ` along the
> morphism of lisse-étale topoi induced by `f` has
>
> `f'_*ℋ(y) = Γ((V ×_{y, 𝒴} 𝒳)', (pr')^{-1}ℋ)`,
>
> the global sections of `ℋ` restricted along the projection `pr'` of the primed 2-fibre product.
> The direct image is `CategoryTheory.Functor.sheafPushforwardCocontinuous` along the site functor
> of **Stacks 07AT**, whose cocontinuity is
> `AlgebraicGeometry.Stack.LisseEtale.siteFunctor_isCocontinuous`.

```lean
def sheafPrimedPushforwardSectionsEquiv (y : LisseEtale.{u, w} B S hS 𝒴)
    (ℋ : Sheaf (topology.{u, w} B S hS 𝒳) (Type a))
    [∀ F : (LisseEtale.{u, w} B S hS 𝒳)ᵒᵖ ⥤ Type a,
      (primedSiteFunctor.{u, w} B S hS f hf).op.HasPointwiseRightKanExtension F]
    [∀ F : (LisseEtale.{u, w} B S hS 𝒳)ᵒᵖ ⥤ Type a,
      (inclusion.{u, w} B S hS 𝒳 ⋙ f.hom.hom.toFunctor).op.HasPointwiseRightKanExtension F] :
    letI : (primedSiteFunctor.{u, w} B S hS f hf).IsCocontinuous
        (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴) :=
      siteFunctor_isCocontinuous.{u, w} B S hS f hf
    ((((primedSiteFunctor.{u, w} B S hS f hf).sheafPushforwardCocontinuous (Type a)
        (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)).obj ℋ).obj.obj (op y)) ≃
      Presheaf.globalSections ((primedProjection B S hS f y).op ⋙ ℋ.obj)
```

## Tag 0GR2, a lemma

[Tag 0GR2](https://stacks.math.columbia.edu/tag/0GR2) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.rightDerived_sheafPushforward_iso_sheafify_derivedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfHigherDirectImage.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfHigherDirectImage.lean#L74). The attribute's comment: “flat-fppf sheafification formula”.

> **Stacks 0GR2, the flat-fppf case.** The `p`-th higher direct image along the morphism of
> flat-fppf topoi induced by a flat 1-morphism of algebraic stacks is the sheaf associated to the
> `p`-th right derived presheaf direct image, naturally in the abelian sheaf of coefficients.
>
> The flat-fppf site of an algebraic stack is a category of type `Type (u + 1)` with morphisms in
> `Type u`, so it is essentially small at any coefficient universe `max (u + 1) a`; abelian
> sheaves on it then form a Grothendieck abelian category and in particular have enough
> injectives, which is what makes the right derived functors available.

```lean
public theorem rightDerived_sheafPushforward_iso_sheafify_derivedPresheaf (p : ℕ) :
    letI : (siteFunctor B S hS f hf).1.IsCocontinuous
        (topology B S hS 𝒳) (topology B S hS 𝒴) :=
      siteFunctor_isCocontinuous B S hS f hf
    letI : HasSheafify (topology B S hS 𝒳) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : HasSheafify (topology B S hS 𝒴) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : EssentiallySmall.{max (u + 1) a} (FlatFppf B S hS 𝒳) :=
      essentiallySmallSelf (FlatFppf B S hS 𝒳)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall
      (topology B S hS 𝒳) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (topology B S hS 𝒳) AddCommGrpCat.{max (u + 1) a})
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, a}
      (siteFunctor B S hS f hf).1
      (topology B S hS 𝒳) (topology B S hS 𝒴)
    Nonempty
      (((siteFunctor B S hS f hf).1.sheafPushforwardCocontinuous
          AddCommGrpCat.{max (u + 1) a} (topology B S hS 𝒳)
          (topology B S hS 𝒴)).rightDerived p ≅
        Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
            (topology B S hS 𝒳) (siteFunctor B S hS f hf).1 p ⋙
          presheafToSheaf (topology B S hS 𝒴) AddCommGrpCat.{max (u + 1) a})
```

**`AlgebraicGeometry.Stack.FlatFppf.rightDerived_sheafPushforward_iso_sheafify_fibreCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfHigherDirectImageFibre.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfHigherDirectImageFibre.lean#L73). The attribute's comment: “flat-fppf case: Rᵖf'_*ℋ is the sheaf associated to y ↦ Hᵖ((V ×_y 𝒳)', pr'⁻¹ℋ)”.

> **Stacks 0GR2, the flat-fppf case.** Let `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic
> stacks and `f'` the induced morphism of flat-fppf topoi. For every `p` and every abelian sheaf
> `ℋ` on `𝒳_{flat,fppf}`,
>
> `Rᵖ f'_* ℋ = sheaf associated to y ↦ Hᵖ((V ×_{y, 𝒴} 𝒳)', (pr')⁻¹ ℋ)`.
>
> Precisely: `Rᵖ f'_*` is the sheafification of the presheaf-valued functor
> `derivedPresheafDirectImage`, and for every object `y` of `𝒴_{flat,fppf}` the value at `y` of
> that presheaf is `Hᵖ` of the fibre site `(V ×_{y, 𝒴} 𝒳)'` — the pairs `(x, φ : f(x) ⟶ y)`, i.e.
> the localization of `𝒳_{flat,fppf}` at `(f')⁻¹ h_y` — with coefficients in the restriction
> `(pr')⁻¹ ℋ`, both naturally in `ℋ`.

```lean
public theorem rightDerived_sheafPushforward_iso_sheafify_fibreCohomology (p : ℕ) :
    letI : (siteFunctor.{u, w} B S hS f hf).1.IsCocontinuous
        (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴) :=
      siteFunctor_isCocontinuous.{u, w} B S hS f hf
    letI : HasSheafify (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : HasSheafify (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : EssentiallySmall.{max (u + 1) a} (FlatFppf.{u, w} B S hS 𝒳) :=
      essentiallySmallSelf (FlatFppf.{u, w} B S hS 𝒳)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall
      (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a})
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, a}
      (siteFunctor.{u, w} B S hS f hf).1
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
    Nonempty
        (((siteFunctor.{u, w} B S hS f hf).1.sheafPushforwardCocontinuous
            AddCommGrpCat.{max (u + 1) a} (topology.{u, w} B S hS 𝒳)
            (topology.{u, w} B S hS 𝒴)).rightDerived p ≅
          Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
              (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 p ⋙
            presheafToSheaf (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a}) ∧
      ∀ y : FlatFppf.{u, w} B S hS 𝒴,
        letI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{u + 1, u, max (u + 1) a}
          (J := fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
        letI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{u + 1, u, max (u + 1) a}
          (J := fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
        Nonempty
          (Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
                (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 p ⋙
              (evaluation (FlatFppf.{u, w} B S hS 𝒴)ᵒᵖ AddCommGrpCat.{max (u + 1) a}).obj
                (op y) ≅
            fibreRestriction.{u + 1, u + 1, u, a} (topology.{u, w} B S hS 𝒳)
                (siteFunctor.{u, w} B S hS f hf).1 y ⋙
              Sheaf.functorH.{max (u + 1) a, max (u + 1) a, u, u + 1}
                (fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
                p)
```

**`AlgebraicGeometry.Stack.LisseEtale.rightDerived_sheafPushforward_iso_sheafify_derivedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleHigherDirectImage.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleHigherDirectImage.lean#L81). The attribute's comment: “lisse-étale sheafification formula”.

> **Stacks 0GR2, the lisse-étale case.** The `p`-th higher direct image along the morphism of
> lisse-étale topoi induced by a smooth 1-morphism of algebraic stacks is the sheaf associated to
> the `p`-th right derived presheaf direct image, naturally in the abelian sheaf of coefficients.
>
> The lisse-étale site of an algebraic stack is a category of type `Type (u + 1)` with morphisms in
> `Type u`, so it is essentially small at any coefficient universe `max (u + 1) a`; abelian
> sheaves on it then form a Grothendieck abelian category and in particular have enough
> injectives, which is what makes the right derived functors available.

```lean
public theorem rightDerived_sheafPushforward_iso_sheafify_derivedPresheaf (p : ℕ) :
    letI : (siteFunctor.{u, w} B S hS f hf).1.IsCocontinuous
        (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴) :=
      siteFunctor_isCocontinuous.{u, w} B S hS f hf
    letI : HasSheafify (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : HasSheafify (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : EssentiallySmall.{max (u + 1) a} (LisseEtale.{u, w} B S hS 𝒳) :=
      essentiallySmallSelf (LisseEtale.{u, w} B S hS 𝒳)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall
      (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a})
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, a}
      (siteFunctor.{u, w} B S hS f hf).1
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
    Nonempty
      (((siteFunctor.{u, w} B S hS f hf).1.sheafPushforwardCocontinuous
          AddCommGrpCat.{max (u + 1) a} (topology.{u, w} B S hS 𝒳)
          (topology.{u, w} B S hS 𝒴)).rightDerived p ≅
        Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
            (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 p ⋙
          presheafToSheaf (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a})
```

**`AlgebraicGeometry.Stack.LisseEtale.rightDerived_sheafPushforward_iso_sheafify_fibreCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleHigherDirectImageFibre.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleHigherDirectImageFibre.lean#L73). The attribute's comment: “lisse-étale case: Rᵖf'_*ℋ is the sheaf associated to y ↦ Hᵖ((V ×_y 𝒳)', pr'⁻¹ℋ)”.

> **Stacks 0GR2, the lisse-étale case.** Let `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic
> stacks and `f'` the induced morphism of lisse-étale topoi. For every `p` and every abelian sheaf
> `ℋ` on `𝒳_{lisse,étale}`,
>
> `Rᵖ f'_* ℋ = sheaf associated to y ↦ Hᵖ((V ×_{y, 𝒴} 𝒳)', (pr')⁻¹ ℋ)`.
>
> Precisely: `Rᵖ f'_*` is the sheafification of the presheaf-valued functor
> `derivedPresheafDirectImage`, and for every object `y` of `𝒴_{lisse,étale}` the value at `y` of
> that presheaf is `Hᵖ` of the fibre site `(V ×_{y, 𝒴} 𝒳)'` — the pairs `(x, φ : f(x) ⟶ y)`, i.e.
> the localization of `𝒳_{lisse,étale}` at `(f')⁻¹ h_y` — with coefficients in the restriction
> `(pr')⁻¹ ℋ`, both naturally in `ℋ`.

```lean
public theorem rightDerived_sheafPushforward_iso_sheafify_fibreCohomology (p : ℕ) :
    letI : (siteFunctor.{u, w} B S hS f hf).1.IsCocontinuous
        (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴) :=
      siteFunctor_isCocontinuous.{u, w} B S hS f hf
    letI : HasSheafify (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : HasSheafify (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a} :=
      Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp
    letI : EssentiallySmall.{max (u + 1) a} (LisseEtale.{u, w} B S hS 𝒳) :=
      essentiallySmallSelf (LisseEtale.{u, w} B S hS 𝒳)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall
      (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (topology.{u, w} B S hS 𝒳) AddCommGrpCat.{max (u + 1) a})
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, a}
      (siteFunctor.{u, w} B S hS f hf).1
      (topology.{u, w} B S hS 𝒳) (topology.{u, w} B S hS 𝒴)
    Nonempty
        (((siteFunctor.{u, w} B S hS f hf).1.sheafPushforwardCocontinuous
            AddCommGrpCat.{max (u + 1) a} (topology.{u, w} B S hS 𝒳)
            (topology.{u, w} B S hS 𝒴)).rightDerived p ≅
          Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
              (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 p ⋙
            presheafToSheaf (topology.{u, w} B S hS 𝒴) AddCommGrpCat.{max (u + 1) a}) ∧
      ∀ y : LisseEtale.{u, w} B S hS 𝒴,
        letI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{u + 1, u, max (u + 1) a}
          (J := fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
        letI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{u + 1, u, max (u + 1) a}
          (J := fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
        Nonempty
          (Functor.derivedPresheafDirectImage.{u + 1, u + 1, u, u, a}
                (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 p ⋙
              (evaluation (LisseEtale.{u, w} B S hS 𝒴)ᵒᵖ AddCommGrpCat.{max (u + 1) a}).obj
                (op y) ≅
            fibreRestriction.{u + 1, u + 1, u, a} (topology.{u, w} B S hS 𝒳)
                (siteFunctor.{u, w} B S hS f hf).1 y ⋙
              Sheaf.functorH.{max (u + 1) a, max (u + 1) a, u, u + 1}
                (fibreTopology (topology.{u, w} B S hS 𝒳) (siteFunctor.{u, w} B S hS f hf).1 y)
                p)
```

## Tag 0GR3, a lemma

[Tag 0GR3](https://stacks.math.columbia.edu/tag/0GR3) in the Stacks Project.

**`AlgebraicGeometry.Stack.LisseEtale.isIso_baseChangeMapPlus_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedBaseChangeMap.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedBaseChangeMap.lean#L186). The attribute's comment: “the lisse-étale case: the canonical base change map g⁻¹ Rf_* ℱ ⟶ Rf'_* (g')⁻¹ ℱ is an isomorphism for every abelian sheaf ℱ on 𝒳_étale, in D⁺ for any model of the derived categories. The map is Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus (the identification g⁻¹ ∘ Rf_* = R(g⁻¹ ∘ f_*) for the exact g⁻¹, the derived map of the canonical map g⁻¹f_* ⟶ f'_*(g')⁻¹ of Sites 06UM, and the canonical comparison R(f'_* ∘ (g')⁻¹) ⟶ Rf'_* ∘ (g')⁻¹ of 05T2) at ℱ in degree zero. Nothing is assumed: the degree-zero isomorphism is 07AT (AlgebraicGeometry.Stack.LisseEtale.isIso_abelianSheafBaseChange) and the acyclicity of restricted injectives for f'_* is proved by descent (AlgebraicGeometry.Stack.LisseEtale.isZero_rightDerived_restriction_of_injective)”.

> **Stacks 0GR3, the lisse-étale case.** Let `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic
> stacks, `f'` its restriction to the lisse-étale sites (**Stacks 07AT**) and `g`, `g'` the
> inclusions of the lisse-étale sites of `𝒴` and of `𝒳`. For every abelian sheaf `ℱ` on
> `𝒳_étale` the canonical base change map
>
> `g⁻¹ Rf_* ℱ ⟶ Rf'_* (g')⁻¹ ℱ`
>
> is an isomorphism in the bounded below derived category of abelian sheaves on the lisse-étale
> site of `𝒴`, for any model of the derived categories. The map is
> `Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus` at the canonical map
> `g⁻¹f_* ⟶ f'_*(g')⁻¹` of Sites, Section 06UM, evaluated at `ℱ` placed in degree zero.

```lean
theorem isIso_baseChangeMapPlus_app
    (ℱ : Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) AddCommGrpCat.{u + 1}) :
    haveI := isCocontinuous_subsiteFunctor.{u, w} B S hS f hf
    haveI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
      (etaleTopology B)).2
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1}
      f.hom.hom.toFunctor (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
      (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1}
      (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf))
      (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴)
    IsIso ((Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus
      (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B) (smoothObject.{u, w} B S hS 𝒳))
      (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B) (smoothObject.{u, w} B S hS 𝒴))
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)))
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴))
      (SubsitePushforward.subsiteAbelianSheafBaseChange.{_, _, _, _, u + 1}
        f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳) (smoothObject_map.{u, w} B S hS f hf)
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴))).app
      ((DerivedCategory.Plus.singleFunctor _ 0).obj ℱ))
```

**`AlgebraicGeometry.Stack.FlatFppf.isIso_baseChangeMapPlus_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedBaseChangeMap.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedBaseChangeMap.lean#L330). The attribute's comment: “the flat-fppf case: the canonical base change map g⁻¹ Rf_* ℱ ⟶ Rf'_* (g')⁻¹ ℱ is an isomorphism for every abelian sheaf ℱ on 𝒳_fppf, in D⁺ for any model of the derived categories. The map is Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus (the identification g⁻¹ ∘ Rf_* = R(g⁻¹ ∘ f_*) for the exact g⁻¹, the derived map of the canonical map g⁻¹f_* ⟶ f'_*(g')⁻¹ of Sites 06UM, and the canonical comparison R(f'_* ∘ (g')⁻¹) ⟶ Rf'_* ∘ (g')⁻¹ of 05T2) at ℱ in degree zero. Nothing is assumed: the degree-zero isomorphism is 07AT (AlgebraicGeometry.Stack.FlatFppf.isIso_abelianSheafBaseChange) and the acyclicity of restricted injectives for f'_* is proved by descent (AlgebraicGeometry.Stack.FlatFppf.isZero_rightDerived_restriction_of_injective)”.

> **Stacks 0GR3, the flat-fppf case.** Let `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic
> stacks, `f'` its restriction to the flat-fppf sites (**Stacks 07AT**) and `g`, `g'` the
> inclusions of the flat-fppf sites of `𝒴` and of `𝒳`. For every abelian sheaf `ℱ` on
> `𝒳_fppf` the canonical base change map
>
> `g⁻¹ Rf_* ℱ ⟶ Rf'_* (g')⁻¹ ℱ`
>
> is an isomorphism in the bounded below derived category of abelian sheaves on the flat-fppf
> site of `𝒴`, for any model of the derived categories. The map is
> `Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus` at the canonical map
> `g⁻¹f_* ⟶ f'_*(g')⁻¹` of Sites, Section 06UM, evaluated at `ℱ` placed in degree zero.

```lean
theorem isIso_baseChangeMapPlus_app
    (ℱ : Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology) AddCommGrpCat.{u + 1}) :
    haveI := isCocontinuous_subsiteFunctor B S hS f hf
    haveI := (isContinuous_and_isCocontinuous_homFunctor B S hS f).2
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1}
      f.hom.hom.toFunctor (associatedTopology B S hS 𝒳.val.val.p B.topology)
      (associatedTopology B S hS 𝒴.val.val.p B.topology)
    letI := Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1}
      (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf))
      (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴)
    IsIso ((Stacks.Cohomology.BoundedBelowComplexes.baseChangeMapPlus
      (subsiteRestriction B S hS 𝒳.val.val.p B.topology (flatObject B S hS 𝒳.val))
      (subsiteRestriction B S hS 𝒴.val.val.p B.topology (flatObject B S hS 𝒴.val))
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology))
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴))
      (SubsitePushforward.subsiteAbelianSheafBaseChange.{_, _, _, _, u + 1}
        f.hom.hom.toFunctor (flatObject B S hS 𝒳.val) (flatObject_map B S hS f hf)
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology)
        (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴))).app
      ((DerivedCategory.Plus.singleFunctor _ 0).obj ℱ))
```

**`AlgebraicGeometry.Stack.LisseEtale.rightDerivedPushforwardRestrictionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L308). The attribute's comment: “the lisse-étale case, as an isomorphism of functors R^p f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ R^p f'_* in every degree rather than as invertibility of the canonical base-change map, and conditional on two things: its degree-zero case — the identification f'_*(g')⁻¹ = g⁻¹f_* of Stacks 07AT (1), which rests on the instance of Stacks 07AK whose hypotheses the source declines to verify — and restriction to the subsite preserving injective abelian sheaves, which is Stacks 07AS (3)”.

> **Stacks 0GR3, the lisse-étale case: degree zero implies every degree.** Let `f : 𝒳 ⟶ 𝒴` be a
> smooth 1-morphism of algebraic stacks, let `g⁻¹` and `(g')⁻¹` be restriction of abelian sheaves
> to the lisse-étale sites of `𝒴` and of `𝒳`, and let `f_*` and `f'_*` be the direct images along
> `f` and along its restriction `f'` to the lisse-étale sites. Suppose `(g')⁻¹` carries injective
> abelian sheaves to injective ones, and that the degree-zero identification
> `f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'_*` of **Stacks 07AT** (1) holds. Then the higher direct images satisfy
>
> `R^p f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ R^p f'_*`
>
> in every degree `p`, which is the conclusion of **Stacks 0GR3**.

```lean
theorem rightDerivedPushforwardRestrictionIso (p : ℕ) :
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf)).IsContinuous
          (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴) :=
      isContinuous_subsiteFunctor.{u, w} B S hS f hf
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf)).IsCocontinuous
          (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴) :=
      isCocontinuous_subsiteFunctor.{u, w} B S hS f hf
    letI : f.hom.hom.toFunctor.IsContinuous
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) :=
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).1
    letI : f.hom.hom.toFunctor.IsCocontinuous
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) :=
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).2
    letI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    letI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    ∀ (_ : (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
          (smoothObject.{u, w} B S hS 𝒳)).PreservesInjectiveObjects)
      (_ : f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
            (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
            (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) ⋙
          subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
            (smoothObject.{u, w} B S hS 𝒴) ≅
        subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
            (smoothObject.{u, w} B S hS 𝒳) ⋙
          (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
              (smoothObject.{u, w} B S hS 𝒳)
              (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
            AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
            (inclusionTopology.{u, w} B S hS 𝒴)),
      Nonempty
        ((f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).rightDerived p ⋙
            subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
              (smoothObject.{u, w} B S hS 𝒴) ≅
          subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
              (smoothObject.{u, w} B S hS 𝒳) ⋙
            ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                  (smoothObject.{u, w} B S hS 𝒳)
                  (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
                AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
                (inclusionTopology.{u, w} B S hS 𝒴)).rightDerived p)
```

**`AlgebraicGeometry.Stack.FlatFppf.rightDerivedPushforwardRestrictionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 678](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L678). The attribute's comment: “the flat-fppf case, as an isomorphism of functors R^p f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ R^p f'_* in every degree rather than as invertibility of the canonical base-change map, and conditional on two things: its degree-zero case — the identification f'_*(g')⁻¹ = g⁻¹f_* of Stacks 07AT (2), which rests on the instance of Stacks 07AK whose hypotheses the source declines to verify — and restriction to the subsite preserving injective abelian sheaves, which is Stacks 07AS (3)”.

> **Stacks 0GR3, the flat-fppf case: degree zero implies every degree.** Let `f : 𝒳 ⟶ 𝒴` be a
> flat 1-morphism of algebraic stacks, let `g⁻¹` and `(g')⁻¹` be restriction of abelian sheaves
> to the flat-fppf sites of `𝒴` and of `𝒳`, and let `f_*` and `f'_*` be the direct images along
> `f` and along its restriction `f'` to the flat-fppf sites. Suppose `(g')⁻¹` carries injective
> abelian sheaves to injective ones, and that the degree-zero identification
> `f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'_*` of **Stacks 07AT** (2) holds. Then the higher direct images satisfy
>
> `R^p f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ R^p f'_*`
>
> in every degree `p`, which is the conclusion of **Stacks 0GR3**.

```lean
theorem rightDerivedPushforwardRestrictionIso (p : ℕ) :
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf)).IsContinuous
          (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴) :=
      isContinuous_subsiteFunctor B S hS f hf
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf)).IsCocontinuous
          (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴) :=
      isCocontinuous_subsiteFunctor B S hS f hf
    letI : f.hom.hom.toFunctor.IsContinuous
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology) :=
      (isContinuous_and_isCocontinuous_homFunctor B S hS f).1
    letI : f.hom.hom.toFunctor.IsCocontinuous
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology) :=
      (isContinuous_and_isCocontinuous_homFunctor B S hS f).2
    letI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    letI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    ∀ (_ : (subsiteRestriction B S hS 𝒳.val.val.p B.topology
          (flatObject B S hS 𝒳.val)).PreservesInjectiveObjects)
      (_ : f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
            (associatedTopology B S hS 𝒳.val.val.p B.topology)
            (associatedTopology B S hS 𝒴.val.val.p B.topology) ⋙
          subsiteRestriction B S hS 𝒴.val.val.p B.topology
            (flatObject B S hS 𝒴.val) ≅
        subsiteRestriction B S hS 𝒳.val.val.p B.topology
            (flatObject B S hS 𝒳.val) ⋙
          (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
              (flatObject B S hS 𝒳.val)
              (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
            AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
            (inclusionTopology B S hS 𝒴)),
      Nonempty
        ((f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
                (associatedTopology B S hS 𝒳.val.val.p B.topology)
                (associatedTopology B S hS 𝒴.val.val.p B.topology)).rightDerived p ⋙
            subsiteRestriction B S hS 𝒴.val.val.p B.topology
              (flatObject B S hS 𝒴.val) ≅
          subsiteRestriction B S hS 𝒳.val.val.p B.topology
              (flatObject B S hS 𝒳.val) ⋙
            ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                  (flatObject B S hS 𝒳.val)
                  (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
                AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
                (inclusionTopology B S hS 𝒴)).rightDerived p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.15, Tag 0GR1](https://stacks.math.columbia.edu/tag/0GR1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
