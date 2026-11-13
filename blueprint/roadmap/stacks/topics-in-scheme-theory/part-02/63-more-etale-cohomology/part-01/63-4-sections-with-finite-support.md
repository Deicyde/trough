---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.isFiniteSupport_iff_exists_isProper, AlgebraicGeometry.SmallEtale.FiniteSupport, AlgebraicGeometry.SmallEtale.finiteSupport_closedWithin, AlgebraicGeometry.SmallEtale.finiteSupportSections, AlgebraicGeometry.SmallEtale.exists_finiteSupport_sum, AlgebraicGeometry.SmallEtale.finiteSupportPresheaf, AlgebraicGeometry.SmallEtale.finiteSupportPushforward, AlgebraicGeometry.SmallEtale.finiteSupport_isLocallyClosed
statement: formalized
proof: formalized
---

# 63.4 Sections with finite support

Section 63.4 of the Stacks Project, [Tag 0F6E](https://stacks.math.columbia.edu/tag/0F6E). 15 tags here are carried by 88 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F6E, the section

[Tag 0F6E](https://stacks.math.columbia.edu/tag/0F6E) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isFiniteSupport_iff_exists_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L123). The attribute's comment: “the footnote: a support is finite over the base exactly when it is proper”.

> **Stacks 0F6E, the footnote.** For a locally quasi-finite `f`, a subset of `X_V` is an
> eligible support of the finite-support direct image — the range of an immersion finite over
> `V` — exactly when it is the range of an immersion *proper* over `V`. The source states this as
> "since `f` is locally quasi-finite, `Z → V` is finite if and only if it is proper".

```lean
public theorem isFiniteSupport_iff_exists_isProper
    [LocallyQuasiFinite (B.inclusion.map f)] (V : SmallEtale B Y.obj Y.property)
    (E : Set ((SmallEtale.toScheme B X.obj X.property).obj (baseChange B f V))) :
    IsFiniteSupport B f V E ↔
      ∃ (Z : Scheme.{u})
        (i : Z ⟶ (SmallEtale.toScheme B X.obj X.property).obj (baseChange B f V)),
        IsImmersion i ∧
          IsProper (i ≫ B.inclusion.map (pullback.fst V.obj.hom f)) ∧
          Set.range i.base = E
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SmallEtale.FiniteSupport`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L233), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L140) (StacksFrontier): “the eligible supports, locally closed and finite over the base”.
- [`AlgebraicGeometry.SmallEtale.finiteSupport_closedWithin`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L251), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L143) (StacksFrontier): “closedness of one eligible support in another”.
- [`AlgebraicGeometry.SmallEtale.finiteSupportSections`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L326), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L146) (StacksFrontier): “the group of finite-support sections, as a colimit of supported sections”.
- [`AlgebraicGeometry.SmallEtale.exists_finiteSupport_sum`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L336), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L149) (StacksFrontier): “a finite-support section as a finite formal sum of supported sections”.
- [`AlgebraicGeometry.SmallEtale.finiteSupportPresheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L851), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L152) (StacksFrontier): “the restriction maps, assembling the groups into a presheaf”.
- [`AlgebraicGeometry.SmallEtale.finiteSupportPushforward`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L964), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportProper.lean#L155) (StacksFrontier): “the finite-support direct image presheaf as a functor”.

## Tag 0F6J, an equation

[Tag 0F6J](https://stacks.math.columbia.edu/tag/0F6J) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.exists_finiteSupport_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L336). The attribute's comment: “the formal sum presentation”.

> **Stacks 0F6J.** Every section with finite support over `V` is a finite formal sum
> `s = ∑ (Z_i, s_i)`, where each `Z_i` is a support finite over `V` and `s_i ∈ H_{Z_i}(F)`,
> the pair `(Z_i, s_i)` standing for the image of `s_i` under the colimit inclusion at `Z_i`.

```lean
public theorem exists_finiteSupport_sum
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (V : SmallEtale B Y.obj Y.property) [Small.{v} (FiniteSupport B f V)]
    (s : ↥(finiteSupportSections B f F V)) :
    ∃ (n : ℕ) (Z : Fin n → FiniteSupport B f V)
      (t : ∀ i, supportedSections B X.obj X.property F (baseChange B f V) (Z i).1
        (finiteSupport_isLocallyClosed B f V (Z i))),
      s = ∑ i, colimit.ι (finiteSupportDiagram B f F V) (Z i) (t i)
```

## Tag 0F6M, an equation

[Tag 0F6M](https://stacks.math.columbia.edu/tag/0F6M) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.FiniteSupport`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L233). The attribute's comment: “the index of the colimit”.

> **Stacks 0F6M.** The partially ordered set of supports of `X_V` which are finite over
> `V`.

```lean
public abbrev FiniteSupport (V : SmallEtale B Y.obj Y.property)
```

**`AlgebraicGeometry.SmallEtale.finiteSupport_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L240). The attribute's comment: “local closedness of the supports”.

> The support of a subscheme finite over `V` is locally closed, so the group `H_Z(F)` of
> Stacks 0F6F is defined for it.

```lean
public theorem finiteSupport_isLocallyClosed (V : SmallEtale B Y.obj Y.property)
    (E : FiniteSupport B f V) : IsLocallyClosed E.1
```

**`AlgebraicGeometry.SmallEtale.finiteSupport_closedWithin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L251). The attribute's comment: “closedness of the transition inclusions”.

> One support finite over `V` contained in another is closed in it. This is the relation
> making the transition maps of Stacks 0F6F available on the index, and in the source it is the
> observation that `Z → Z'` is a closed immersion because `Z → V` is finite and `Z' → V` is
> separated.

```lean
public theorem finiteSupport_closedWithin (V : SmallEtale B Y.obj Y.property)
    (E E' : FiniteSupport B f V) (h : E ≤ E') :
    IsClosed ((Subtype.val : E'.1 → _) ⁻¹' E.1)
```

**`AlgebraicGeometry.SmallEtale.finiteSupportDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L297). The attribute's comment: “the diagram of supported sections”.

> **Stacks 0F6M.** The diagram `Z ↦ H_Z(F)` of supported sections over the supports finite
> over `V`, with the transition maps of Stacks 0F6F along the inclusions.

```lean
public def finiteSupportDiagram
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (V : SmallEtale B Y.obj Y.property) :
    FiniteSupport B f V ⥤ AddCommGrpCat.{v}
```

**`AlgebraicGeometry.SmallEtale.finiteSupportSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L326). The attribute's comment: “the colimit formula”.

> **Stacks 0F6M.** The abelian group of sections with finite support over `V`, namely the
> colimit of `H_Z(F)` over the supports finite over `V`.

```lean
public abbrev finiteSupportSections
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (V : SmallEtale B Y.obj Y.property)
    [Small.{v} (FiniteSupport B f V)] : AddCommGrpCat.{v}
```

**`AlgebraicGeometry.SmallEtale.isFiniteSupport_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L349). The attribute's comment: “base change of the supports”.

> **Stacks 0F6M.** The inverse image of a support finite over `V` along a morphism
> `V' ⟶ V` of the small étale site of `Y` is a support finite over `V'`.

```lean
public theorem isFiniteSupport_preimage {V V' : SmallEtale B Y.obj Y.property} (g : V' ⟶ V)
    (E : FiniteSupport B f V) :
    IsFiniteSupport B f V' (((SmallEtale.toScheme B X.obj X.property).map
      ((smallEtaleBaseChange B f).map g)).base ⁻¹' E.1)
```

**`AlgebraicGeometry.SmallEtale.finiteSupportBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L458). The attribute's comment: “base change of supported sections”.

> **Stacks 0F6M.** Base change of a support finite over `V` and of its supported sections
> along a morphism `V' ⟶ V` of the small étale site of `Y`. The support is the set-theoretic
> inverse image and the map on sections is restriction.

```lean
public def finiteSupportBaseChange
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    {V V' : SmallEtale B Y.obj Y.property} (g : V' ⟶ V)
    (E : FiniteSupport B f V) : FiniteSupportBaseChange B f F g E
```

**`AlgebraicGeometry.SmallEtale.finiteSupportPresheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L851). The attribute's comment: “the finite-support presheaf”.

> **Stacks 0F6M.** The abelian presheaf `V ↦ colim_Z H_Z(F)` on the small étale site of
> `Y`, with base change of supports as its restriction maps.

```lean
public abbrev finiteSupportPresheaf
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (hsmall : ∀ V : SmallEtale B Y.obj Y.property, Small.{v} (FiniteSupport B f V)) :
    (SmallEtale B Y.obj Y.property)ᵒᵖ ⥤ AddCommGrpCat.{v}
```

**`AlgebraicGeometry.SmallEtale.finiteSupportPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean, line 964](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupport.lean#L964). The attribute's comment: “the finite-support direct image functor”.

> **Stacks 0F6M.** The direct image with finite support, as a functor from abelian sheaves
> on the small étale site of `X` to abelian presheaves on the small étale site of `Y`. Its
> values are the colimits `colim_Z H_Z(F)` and both of its functorial actions are pinned down on
> the colimit generators.

```lean
public def finiteSupportPushforward
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    (hsmall : ∀ V : SmallEtale B Y.obj Y.property, Small.{v} (FiniteSupport B f V)) :
    {P : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v} ⥤
        ((SmallEtale B Y.obj Y.property)ᵒᵖ ⥤ AddCommGrpCat.{v}) //
      FiniteSupportPushforwardSpec B f hsmall P}
```

## Tag 0F6N, a lemma

[Tag 0F6N](https://stacks.math.columbia.edu/tag/0F6N) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekFunctorIsoProperSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L196). The attribute's comment: “functor comparison of the two models of f\_!”.

> The two models of the direct image with compact support agree: the
> sheafification of the finite-support direct image presheaf is the proper-support subsheaf of
> the ordinary direct image.

```lean
public def fShriekFunctorIsoProperSupport [IsSeparated (B.inclusion.map g)]
    [LocallyQuasiFinite (B.inclusion.map g)] :
    fShriekFunctor.{u, v} B g ≅ properSupportFunctor.{u, max (u + 1) v} B g
```

**`AlgebraicGeometry.SmallEtale.finiteSupportPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportPushforward.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportPushforward.lean#L211). References: SGA 4 XVII (6.3.16), “colimit formula”.

> For a separated, locally finite type and locally quasi-finite morphism `f` of a big étale
> site, the finite-support direct image presheaf `f_{p!}` of [Stacks, Tag 0F6M] is isomorphic to
> the proper-support direct image `f_!` of [Stacks, Tag 0F4X], as functors from abelian
> sheaves on the small étale site of `X` to abelian presheaves on the small étale site of `Y`. The
> isomorphism is pinned down on the colimit generators: the generator of an eligible support
> carrying a supported section goes to the section of `f_!F` which restricts to that section on
> the canonical open of the support.

```lean
public def finiteSupportPushforwardIso (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsSeparated (B.inclusion.map f)] [LocallyOfFiniteType (B.inclusion.map f)]
    [LocallyQuasiFinite (B.inclusion.map f)] :
    let hsmall : ∀ V : SmallEtale B Y.obj Y.property,
      Small.{max u v} (FiniteSupport B f V) := fun _ => inferInstance
    let P := finiteSupportPushforward.{u, max u v} B f hsmall
    {e : P.val ≅ properSupportFunctor B f ⋙
        sheafToPresheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{max u v} //
      ∀ (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max u v})
        (V : SmallEtale B Y.obj Y.property) (E : FiniteSupport B f V)
        (s : supportedSections B X.obj X.property F (baseChange B f V) E.1
          (finiteSupport_isLocallyClosed B f V E)),
        letI := hsmall V
        (F.obj.map (openObjectι B X.obj X.property (baseChange B f V)
            (finiteSupportOpen B f V E)).op).hom
          ((colimit.ι (finiteSupportDiagram B f F V) E ≫
            eqToHom (P.property.obj_eq F V).symm ≫
            (e.hom.app F).app (op V) ≫
            (fShriekSubsheaf B f F).val.arrow.hom.app (op V)).hom s) = s.val}
```

## Tag 0F6P, a lemma

[Tag 0F6P](https://stacks.math.columbia.edu/tag/0F6P) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.finiteSupportStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkFunctorIso.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkFunctorIso.lean#L53). The attribute's comment: “the germ decomposition as an isomorphism of functors on `Ab(X_étale)`”.

> **Stacks 0F6P.** For a locally quasi-finite morphism `f : X ⟶ Y` and a geometric point `ȳ`
> of `Y`, functorially in the abelian sheaf `F` on the small étale site of `X`, the stalk at `ȳ` of
> the finite-support direct image `f_{p!}F` is the direct sum of the stalks of `F` over the
> geometric points of `X` lying over `ȳ`: `(f_{p!}F)_ȳ ≅ ⊕_{f(x̄) = ȳ} F_x̄`. The component at `F`
> is `finiteSupportStalkIso`.

```lean
public def finiteSupportStalkFunctorIso :
    (finiteSupportPushforward B f hsmall).1 ⋙
        etaleStalkPresheafFunctor B Y.obj Y.property s AddCommGrpCat.{max u v} ≅
      fiberStalksFunctor.{u, v} B f s
```

**`AlgebraicGeometry.SmallEtale.surjective_finiteSupportStalkToFiberStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkGeometric.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkGeometric.lean#L598). The attribute's comment: “surjectivity of the germ decomposition”.

> **The surjectivity half of Stacks 0F6P.** The germ decomposition map
> `(f_{p!}F)_ȳ ⟶ ⊕_{f(x̄) = ȳ} F_x̄` is surjective.

```lean
public theorem surjective_finiteSupportStalkToFiberStalks
    (hsmall : ∀ V : SmallEtale B Y.obj Y.property, Small.{max u v} (FiniteSupport B f V)) :
    Function.Surjective (finiteSupportStalkToFiberStalks B f s F hsmall)
```

**`AlgebraicGeometry.SmallEtale.injective_finiteSupportStalkToFiberStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkIso.lean, line 962](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkIso.lean#L962). The attribute's comment: “injectivity of the germ decomposition”.

> **The injectivity half of Stacks 0F6P.** The germ decomposition map
> `(f_{p!}F)_ȳ ⟶ ⊕_{f(x̄) = ȳ} F_x̄` is injective.
>
> An element of the stalk is a finite sum of germs of supported sections over one étale
> neighbourhood of `ȳ`, and such a sum of germs vanishes as soon as the family of germ
> decompositions does.

```lean
public theorem injective_finiteSupportStalkToFiberStalks :
    Function.Injective (finiteSupportStalkToFiberStalks B f s F hsmall)
```

**`AlgebraicGeometry.SmallEtale.finiteSupportStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkIso.lean, line 995](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkIso.lean#L995). The attribute's comment: “the germ decomposition is an isomorphism”.

> **Stacks 0F6P.** For a locally quasi-finite morphism `f : X ⟶ Y`, the stalk of the
> finite-support direct image `f_{p!}F` at a geometric point `ȳ` of `Y` is the direct sum of the
> stalks of `F` over the geometric points of `X` lying over `ȳ`:
> `(f_{p!}F)_ȳ ≅ ⊕_{f(x̄) = ȳ} F_x̄`.

```lean
public def finiteSupportStalkIso :
    etaleStalk B Y.obj Y.property s ((finiteSupportPushforward B f hsmall).1.obj F) ≅
      AddCommGrpCat.of (fiberStalks B f s F)
```

## Tag 0F6Q, a lemma

[Tag 0F6Q](https://stacks.math.columbia.edu/tag/0F6Q) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.etaleExtensionToFiniteSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean#L419). The attribute's comment: “canonical natural presheaf map”.

> **Stacks 0F6Q.** The canonical map `j_{p!} ⟶ f_{p!}` from the presheaf extension by zero
> along the étale morphism `U ⟶ X` to the finite-support direct image presheaf, natural in the
> abelian sheaf on the small étale site of `U`. It is the map the universal property of the left
> Kan extension produces from the graph generators.

```lean
public def etaleExtensionToFiniteSupport :
    abelianPresheafExtensionByZero B X hX U ⟶ etaleFiniteSupportPresheaf B X hX U
```

**`AlgebraicGeometry.SmallEtale.etaleExtensionToFiniteSupport_on_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean#L463). The attribute's comment: “graph-support formula on generators”.

> **Stacks 0F6Q.** The value of the canonical map on a generator of the presheaf extension
> by zero: the section of `F` over an étale object `W → U`, viewed in the summand of `j_{p!}F`
> over `W` indexed by `W ⟶ U`, goes to the colimit generator of `colim_Z H_Z(F)` at the graph of
> `W → U`, carrying the section supported on that graph. Naturality of the comparison then
> extends the formula to every lift `V ⟶ U` of an arbitrary étale test object `V ⟶ X`.

```lean
public theorem etaleExtensionToFiniteSupport_on_graph
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      AddCommGrpCat.{u + 1})
    (W : SmallEtale B U.obj.left.1 U.obj.left.property) (s : F.obj.obj (op W)) :
    ((etaleExtensionToFiniteSupport B X hX U).app F).app
        (op ((smallEtalePostcompose B X hX U).obj W))
        (((smallEtalePostcompose B X hX U).op.lanUnit.app F.obj).app (op W) s) =
      colimit.ι (finiteSupportDiagram B U.obj.hom F ((smallEtalePostcompose B X hX U).obj W))
        (etaleGraphFiniteSupport B X hX U W) (etaleGraphSection B X hX U F W s)
```

**`AlgebraicGeometry.SmallEtale.graphSupportedSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Comparison.lean#L537). The attribute's comment: “graph supports”.

> **Stacks 0F6Q, the graph supports.** For an étale object `W → U` the graph of `W → U` is
> an open immersion `W ⟶ U ×_X W` whose image is a support finite over `W`, and a section of an
> abelian sheaf over `W` is a section supported on that graph.

```lean
public def graphSupportedSection (W : SmallEtale B U.obj.left.1 U.obj.left.property) :
    GraphSupportedSectionData B X hX U W
```

**`AlgebraicGeometry.SmallEtale.etaleExtensionToFiniteSupport_sheafify_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Stalk.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportExtensionByZero/Stalk.lean#L511). The attribute's comment: “isomorphism after sheafification”.

> **Stacks 0F6Q.** The canonical map `j_{p!}F ⟶ f_{p!}F` becomes an isomorphism after
> sheafification: it is an isomorphism on every geometric stalk, both sides becoming the direct
> sum of the stalks of `F` over the geometric fibre, and a map of abelian étale sheaves which is
> an isomorphism on every geometric stalk is an isomorphism. So the sheaf `j_!F = (j_{p!}F)^#` of
> Stacks 03S3 is identified with `(f_{p!}F)^#`.

```lean
public theorem etaleExtensionToFiniteSupport_sheafify_isIso
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      AddCommGrpCat.{u + 1}) :
    IsIso ((presheafToSheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}).map
      ((etaleExtensionToFiniteSupport B X hX U).app F))
```

## Tag 0F6R, a definition

[Tag 0F6R](https://stacks.math.columbia.edu/tag/0F6R) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalk.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalk.lean#L141).

> **Stacks 0F6R.** The direct image with compact support `f_!` of a locally quasi-finite
> morphism, on abelian sheaves on the small étale sites: the sheafification of the finite-support
> direct image presheaf `f_{p!}` of Stacks 0F6M.

```lean
public def fShriekFunctor :
    Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{max (u + 1) v}
```

## Tag 0F5F, a lemma

[Tag 0F5F](https://stacks.math.columbia.edu/tag/0F5F) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean#L78). The attribute's comment: “part (1), stalk decomposition”.

> **Stacks 0F5F, part (1).** The stalk of the direct image with compact support `f_!F` of a
> locally quasi-finite morphism at a geometric point `ȳ` of `Y` is the direct sum of the stalks of
> `F` over the geometric points of `X` lying over `ȳ`: `(f_!F)_ȳ ≅ ⊕_{f(x̄) = ȳ} F_x̄`.

```lean
public def fShriekStalkIso (s : GeometricPoint Y.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    etaleStalk B Y.obj Y.property s ((fShriekFunctor.{u, v} B f).obj F).obj ≅
      AddCommGrpCat.of (fiberStalks.{u, max (u + 1) v} B f s F)
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkIso_comp_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean#L90). The attribute's comment: “part (1), canonical comparison”.

> **Stacks 0F5F, part (1).** The stalk decomposition of `f_!F` is the canonical one: the
> comparison of the stalk of `f_!F` with the stalk of the finite-support direct image presheaf
> `f_{p!}F`, which is induced by the sheafification unit, carries it to the germ decomposition of
> Stacks 0F6P.

```lean
public theorem fShriekStalkIso_comp_sheafification (s : GeometricPoint Y.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    colim.map (Functor.whiskerLeft
        (Functor.Elements.π (geometricPointFiber B Y.obj Y.property s)).op
        (toSheafify (SmallEtale.topology B Y.obj Y.property)
          ((finiteSupportPushforward.{u, max (u + 1) v} B f
            (fun _ => inferInstance)).1.obj F))) ≫
      (fShriekStalkIso.{u, v} B f s F).hom =
      (finiteSupportStalkIso.{u, max (u + 1) v} B f s F fun _ => inferInstance).hom
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean#L105). The attribute's comment: “part (1), functoriality”.

> **Stacks 0F5F, part (1).** The stalk decomposition of the direct image with compact support is
> natural in the abelian sheaf: a morphism of sheaves on `X` acts on the direct sum of stalks over
> the geometric fibre by its maps on those stalks.

```lean
public theorem fShriekStalkIso_natural (s : GeometricPoint Y.obj)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}}
    (φ : F ⟶ G) :
    colim.map (Functor.whiskerLeft
        (Functor.Elements.π (geometricPointFiber B Y.obj Y.property s)).op
        ((fShriekFunctor.{u, v} B f).map φ).1) ≫ (fShriekStalkIso.{u, v} B f s G).hom =
      (fShriekStalkIso.{u, v} B f s F).hom ≫
        AddCommGrpCat.ofHom (fiberStalksMap.{u, max (u + 1) v} B f s φ)
```

**`AlgebraicGeometry.SmallEtale.fShriekFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean#L370). The attribute's comment: “part (2), exactness”.

> **Stacks 0F5F, part (2).** The direct image with compact support of a locally quasi-finite
> morphism is an exact functor on abelian étale sheaves.
>
> Preservation of finite colimits is the colimit preservation of the stalk decomposition;
> preservation of finite limits follows from it together with preservation of monomorphisms.

```lean
public theorem fShriekFunctor_exact :
    exactFunctor _ _ (fShriekFunctor.{u, v} B f)
```

**`AlgebraicGeometry.SmallEtale.fShriekFunctor_preservesCoproductsOfShape`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkDecomposition.lean#L392). The attribute's comment: “part (2), direct sums”.

> **Stacks 0F5F, part (2).** The direct image with compact support of a locally quasi-finite
> morphism commutes with arbitrary direct sums of abelian étale sheaves.

```lean
public theorem fShriekFunctor_preservesCoproductsOfShape (I : Type (max (u + 1) v)) :
    PreservesColimitsOfShape (Discrete I) (fShriekFunctor.{u, v} B f)
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkFunctorDecomposition.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekStalkFunctorDecomposition.lean#L51). The attribute's comment: “part (1), stalk decomposition as an isomorphism of functors”.

> **Stacks 0F5F, part (1), as an isomorphism of functors.** The composite of the direct image
> with compact support `f_!` with the stalk functor at a geometric point `ȳ` of `Y` is the
> coproduct of the stalk functors of `X` at the geometric points lying over `ȳ`.

```lean
public def fShriekStalkFunctorIso (s : GeometricPoint Y.obj) :
    fShriekFunctor.{u, v} B f ⋙ (geometricPointSitePoint B Y.obj Y.property s).sheafFiber
        (A := AddCommGrpCat.{max (u + 1) v}) ≅
      Adjunction.sigmaFamily (fun x : GeometricFiberPoint B f s =>
        (geometricPointSitePoint B X.obj X.property (x.toGeometricPoint B f s)).sheafFiber
          (A := AddCommGrpCat.{max (u + 1) v}))
```

## Tag 0F6S, a remark

[Tag 0F6S](https://stacks.math.columbia.edu/tag/0F6S) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.shriekLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverComplex.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverComplex.lean#L137). The attribute's comment: “covariance along an inclusion of opens of the source”.

> **The Čech face map.** For an inclusion `V ≤ W` of open subschemes of `X`, the covariance map
> `(j_V ≫ f)_!((-)|_V) ⟶ (j_W ≫ f)_!((-)|_W)` of Stacks 0F6S for the open immersion `V ⟶ W`.

```lean
public def shriekLE {V W : (B.inclusion.obj X).Opens} (h : V ≤ W) :
    openShriekPushforward.{u, v} B (openSchemeι B V) f ⟶
      openShriekPushforward.{u, v} B (openSchemeι B W) f
```

**`AlgebraicGeometry.SmallEtale.ofHom_of_comp_fShriekStalkIso_openCovariance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverStalkCovariance.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverStalkCovariance.lean#L164). The attribute's comment: “part (1), stalk compatibility on the stalk decomposition of Stacks 0F5F”.

> **Stacks 0F6S, part (1)**, on the stalk decompositions of Stacks 0F5F: on the direct sums of
> stalks over the geometric fibres the covariance map of the direct images with compact support is
> extension by zero along the inclusion of geometric fibres, so it carries the summand of a point of
> the geometric fibre of `j ≫ f` to the summand of its image in the geometric fibre of `f`.

```lean
public theorem ofHom_of_comp_fShriekStalkIso_openCovariance
    [DecidableEq (GeometricFiberPoint B (j ≫ f) s)]
    [DecidableEq (GeometricFiberPoint B f s)] (y : GeometricFiberPoint B (j ≫ f) s) :
    AddCommGrpCat.ofHom (DirectSum.of (fun y' : GeometricFiberPoint B (j ≫ f) s =>
          ↑(etaleStalk B X'.obj X'.property (y'.toGeometricPoint B (j ≫ f) s)
            ((openRestriction.{u, v} B j).obj F).obj)) y) ≫
        (fShriekStalkIso.{u, v} B (j ≫ f) s ((openRestriction.{u, v} B j).obj F)).inv ≫
        ((geometricPointSitePoint B Y.obj Y.property s).sheafFiber
            (A := AddCommGrpCat.{max (u + 1) v})).map
          ((openCovarianceShriekMap.{u, v} B j f).app F) ≫
        (fShriekStalkIso.{u, v} B f s F).hom =
      (openFiberStalkIso.{u, v} B j f F s y).hom ≫
        AddCommGrpCat.ofHom (DirectSum.of (fun x : GeometricFiberPoint B f s =>
          ↑(etaleStalk B X.obj X.property (x.toGeometricPoint B f s) F.obj))
            (openFiberPoint B j f s y))
```

**`AlgebraicGeometry.SmallEtale.openCovariancePresheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovariance/PresheafMap.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovariance/PresheafMap.lean#L466). The attribute's comment: “covariance, presheaf map”.

> The canonical covariance map of finite-support direct-image presheaves for an open
> subscheme of the source. Its generator formula and the canonical extension of supported
> sections are part of the construction; naturality in the test object and in the abelian sheaf
> is part of its being a natural transformation of functors.

```lean
public def openCovariancePresheafMap :
    {α : openFiniteSupportPushforward.{u, v} B j f ⟶
      wholeFiniteSupportPushforward.{u, v} B f //
      OpenCovariancePresheafMapSpec B j f α}
```

**`AlgebraicGeometry.SmallEtale.openCovarianceShriekMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovariance/PresheafMap.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovariance/PresheafMap.lean#L506). The attribute's comment: “covariance”.

> Sheafifying the canonical presheaf map gives covariance of the direct image with compact
> support under an open immersion of the source.

```lean
public def openCovarianceShriekMap :
    openShriekPushforward.{u, v} B j f ⟶ fShriekFunctor.{u, v} B f
```

**`AlgebraicGeometry.SmallEtale.mono_openCovarianceShriekMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceInjectivity.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceInjectivity.lean#L199). The attribute's comment: “part (4), injectivity for a separated morphism”.

> **Stacks 0F6S, part (4), for a separated morphism.** The covariance map of the direct images
> with compact support attached to an open subscheme of the source is a monomorphism: it is the
> sheafification of the presheaf covariance map, and sheafification of abelian sheaves is left
> exact.

```lean
public theorem mono_openCovarianceShriekMap_app :
    Mono ((openCovarianceShriekMap.{u, v} B j f).app F)
```

**`AlgebraicGeometry.SmallEtale.openCovariancePresheafMap_comp_finiteSupportPushforwardIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceSeparated.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceSeparated.lean#L261). The attribute's comment: “part (2), agreement with the map of Stacks 0F53 through Stacks 0F6N”.

> **Stacks 0F6S, part (2).** For a separated morphism the covariance map of finite-support
> direct-image presheaves attached to an open subscheme of the source is the extension by zero of
> Stacks 0F53, transported along the isomorphism of Stacks 0F6N.

```lean
public theorem openCovariancePresheafMap_comp_finiteSupportPushforwardIso :
    (openCovariancePresheafMap.{u, v} B j f).val.app F ≫
        (finiteSupportPushforwardIso.{u, max (u + 1) v} B f).val.hom.app F =
      (finiteSupportPushforwardIso.{u, max (u + 1) v} B (j ≫ f)).val.hom.app
          ((openRestriction.{u, v} B j).obj F) ≫
        (openInclusionShriekMap.{u, max (u + 1) v} B j f F).val.hom
```

**`AlgebraicGeometry.SmallEtale.fiberStalkComponent_covarianceSectionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean#L293). The attribute's comment: “part (1), stalk compatibility on a generator, summand in the open”.

> **Stacks Project, Tag 0F6S part (1)** on a colimit generator, in a summand indexed by a point
> of the geometric fibre of `j ≫ f`: the germ of the extended section at the image point is the
> germ of the original section, read through the identification of the two stalks.

```lean
public theorem fiberStalkComponent_covarianceSectionMap
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    (V : SmallEtale B Y.obj Y.property)
    (u : (geometricPointFiber B Y.obj Y.property s).obj V)
    (E : FiniteSupport B (j ≫ f) V)
    (a : supportedSections B X'.obj X'.property ((openRestriction.{u, v} B j).obj F)
      (baseChange B (j ≫ f) V) E.1 (finiteSupport_isLocallyClosed B (j ≫ f) V E))
    (x : GeometricFiberPoint B (j ≫ f) s) :
    fiberStalkComponent.{u, max (u + 1) v} B f s F V u (imageFiniteSupport B j f V E)
        (covarianceSectionMap B j f F V E _ (imageFiniteSupport_coe B j f V E) a)
        (openFiberPoint B j f s x) =
      (openFiberStalkIso.{u, v} B j f F s x).hom
        (fiberStalkComponent.{u, max (u + 1) v} B (j ≫ f) s
          ((openRestriction.{u, v} B j).obj F) V u E a x)
```

**`AlgebraicGeometry.SmallEtale.fiberStalkComponent_covarianceSectionMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean#L402). The attribute's comment: “part (1), stalk compatibility on a generator, summand outside the open”.

> **Stacks Project, Tag 0F6S part (1)** on a colimit generator, in a summand outside the image
> of the geometric fibre of `j ≫ f`: the germ of the extended section vanishes there, the extended
> section being supported on the image of the original support.

```lean
public theorem fiberStalkComponent_covarianceSectionMap_eq_zero
    (V : SmallEtale B Y.obj Y.property)
    (u : (geometricPointFiber B Y.obj Y.property s).obj V)
    (E : FiniteSupport B (j ≫ f) V) (D : FiniteSupport B f V)
    (hD : D.1 = (openBaseChangeHom B j f V).base '' E.1)
    (a : supportedSections B X'.obj X'.property ((openRestriction.{u, v} B j).obj F)
      (baseChange B (j ≫ f) V) E.1 (finiteSupport_isLocallyClosed B (j ≫ f) V E))
    (y : GeometricFiberPoint B f s)
    (hy : ∀ x : GeometricFiberPoint B (j ≫ f) s, openFiberPoint B j f s x ≠ y) :
    fiberStalkComponent.{u, max (u + 1) v} B f s F V u D
      (covarianceSectionMap B j f F V E D hD a) y = 0
```

**`AlgebraicGeometry.SmallEtale.fiberStalks_openCovarianceStalkMap_openFiberPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean#L552). The attribute's comment: “part (1), stalk compatibility, presheaf form, summands in the open”.

> **Stacks Project, Tag 0F6S part (1)** for the finite-support direct-image presheaves, in a
> summand indexed by a point of the geometric fibre of `j ≫ f`: on the stalk decompositions of
> Stacks 0F6P the covariance map of Stacks 0F6S carries the summand at a point of the geometric
> fibre of `j ≫ f` to the summand at its image, through the identification of the two stalks.

```lean
public theorem fiberStalks_openCovarianceStalkMap_openFiberPoint
    (V : SmallEtale B Y.obj Y.property)
    (w : (geometricPointFiber B Y.obj Y.property s).obj V) (E : FiniteSupport B (j ≫ f) V)
    (a : (finiteSupportDiagram B (j ≫ f) ((openRestriction.{u, v} B j).obj F) V).obj E)
    (x : GeometricFiberPoint B (j ≫ f) s) :
    ((finiteSupportStalkIso.{u, max (u + 1) v} B f s F (fun _ => inferInstance)).hom
          ((openCovarianceStalkMap.{u, v} B j f F s)
            (finiteSupportStalkGenerator.{u, v} B (j ≫ f)
              ((openRestriction.{u, v} B j).obj F) s
              (Functor.elementsMk (geometricPointFiber B Y.obj Y.property s) V w) E a)) :
        fiberStalks.{u, max (u + 1) v} B f s F) (openFiberPoint B j f s x) =
      (openFiberStalkIso.{u, v} B j f F s x).hom
        (((finiteSupportStalkIso.{u, max (u + 1) v} B (j ≫ f) s
              ((openRestriction.{u, v} B j).obj F) (fun _ => inferInstance)).hom
            (finiteSupportStalkGenerator.{u, v} B (j ≫ f)
              ((openRestriction.{u, v} B j).obj F) s
              (Functor.elementsMk (geometricPointFiber B Y.obj Y.property s) V w) E a) :
          fiberStalks.{u, max (u + 1) v} B (j ≫ f) s
            ((openRestriction.{u, v} B j).obj F)) x)
```

**`AlgebraicGeometry.SmallEtale.fiberStalks_openCovarianceStalkMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalk.lean#L590). The attribute's comment: “part (1), stalk compatibility, presheaf form, summands outside the open”.

> **Stacks Project, Tag 0F6S part (1)** for the finite-support direct-image presheaves, in a
> summand outside the image of the geometric fibre of `j ≫ f`: on the stalk decompositions of
> Stacks 0F6P the covariance map of Stacks 0F6S has vanishing component there. Together with the
> previous theorem this says that on the stalk at `s` the covariance map is the extension by zero
> along the inclusion of geometric fibres.

```lean
public theorem fiberStalks_openCovarianceStalkMap_eq_zero
    (V : SmallEtale B Y.obj Y.property)
    (w : (geometricPointFiber B Y.obj Y.property s).obj V) (E : FiniteSupport B (j ≫ f) V)
    (a : (finiteSupportDiagram B (j ≫ f) ((openRestriction.{u, v} B j).obj F) V).obj E)
    (y : GeometricFiberPoint B f s)
    (hy : ∀ x : GeometricFiberPoint B (j ≫ f) s, openFiberPoint B j f s x ≠ y) :
    ((finiteSupportStalkIso.{u, max (u + 1) v} B f s F (fun _ => inferInstance)).hom
        ((openCovarianceStalkMap.{u, v} B j f F s)
          (finiteSupportStalkGenerator.{u, v} B (j ≫ f)
            ((openRestriction.{u, v} B j).obj F) s
            (Functor.elementsMk (geometricPointFiber B Y.obj Y.property s) V w) E a)) :
      fiberStalks.{u, max (u + 1) v} B f s F) y = 0
```

**`AlgebraicGeometry.SmallEtale.fiberStalks_openCovarianceStalkMap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean#L152). The attribute's comment: “part (1), stalk compatibility, presheaf form, summands in the open, any element”.

> **Stacks 0F6S, part (1)** on an arbitrary element of the stalk: on the stalk decompositions of
> Stacks 0F6P the covariance map carries the component at a point of the geometric fibre of `j ≫ f`
> to the component at its image, through the identification of the two stalks.

```lean
public theorem fiberStalks_openCovarianceStalkMap_apply
    (z : ↑(etaleStalk B Y.obj Y.property s
      ((finiteSupportPushforward.{u, max (u + 1) v} B (j ≫ f)
        (fun _ => inferInstance)).val.obj ((openRestriction.{u, v} B j).obj F))))
    (x : GeometricFiberPoint B (j ≫ f) s) :
    ((finiteSupportStalkIso.{u, max (u + 1) v} B f s F (fun _ => inferInstance)).hom
          ((openCovarianceStalkMap.{u, v} B j f F s) z) :
        fiberStalks.{u, max (u + 1) v} B f s F) (openFiberPoint B j f s x) =
      (openFiberStalkIso.{u, v} B j f F s x).hom
        (((finiteSupportStalkIso.{u, max (u + 1) v} B (j ≫ f) s
              ((openRestriction.{u, v} B j).obj F) (fun _ => inferInstance)).hom z :
          fiberStalks.{u, max (u + 1) v} B (j ≫ f) s
            ((openRestriction.{u, v} B j).obj F)) x)
```

**`AlgebraicGeometry.SmallEtale.fiberStalks_openCovarianceStalkMap_apply_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean#L173). The attribute's comment: “part (1), stalk compatibility, presheaf form, summands outside, any element”.

> **Stacks 0F6S, part (1)** on an arbitrary element of the stalk, in a summand outside the image
> of the geometric fibre of `j ≫ f`: the component of the image vanishes there.

```lean
public theorem fiberStalks_openCovarianceStalkMap_apply_eq_zero
    (z : ↑(etaleStalk B Y.obj Y.property s
      ((finiteSupportPushforward.{u, max (u + 1) v} B (j ≫ f)
        (fun _ => inferInstance)).val.obj ((openRestriction.{u, v} B j).obj F))))
    (y : GeometricFiberPoint B f s)
    (hy : ∀ x : GeometricFiberPoint B (j ≫ f) s, openFiberPoint B j f s x ≠ y) :
    ((finiteSupportStalkIso.{u, max (u + 1) v} B f s F (fun _ => inferInstance)).hom
        ((openCovarianceStalkMap.{u, v} B j f F s) z) :
      fiberStalks.{u, max (u + 1) v} B f s F) y = 0
```

**`AlgebraicGeometry.SmallEtale.mono_openCovarianceShriekMap_app_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceStalkInjectivity.lean#L275). The attribute's comment: “part (4), injectivity”.

> **Stacks Project, Tag 0F6S, part (4)**, in its unrestricted form: for an open immersion
> `j : X' ⟶ X` and a morphism `f : X ⟶ Y` locally of finite type and locally quasi-finite, with no
> separatedness assumed, the covariance map `(j ≫ f)_!(F|_{X'}) ⟶ f_!F` of the direct images with
> compact support is a monomorphism.
>
> On the stalk at a geometric point the map is extension by zero along the inclusion of geometric
> fibres of Stacks 0F6P, hence injective; the stalks at the geometric points jointly detect
> monomorphisms of abelian sheaves on the small étale site.

```lean
public theorem mono_openCovarianceShriekMap_app_general :
    Mono ((openCovarianceShriekMap.{u, v} B j f).app F)
```

**`AlgebraicGeometry.SmallEtale.openCovariancePresheafMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceTransitivity.lean, line 860](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceTransitivity.lean#L860). The attribute's comment: “part (3), transitivity, presheaf form”.

> **Stacks 0F6S, part (3).** Transitivity of covariance for the finite-support direct-image
> presheaves: for nested open subschemes of the source, the covariance map of the composite open
> immersion is the composite of the two covariance maps, once the two descriptions of restriction
> to the smallest open subscheme are identified.

```lean
public theorem openCovariancePresheafMap_comp :
    (openFiniteSupportCompIso.{u, v} B j k f).hom ≫
        Functor.whiskerLeft (openRestriction.{u, v} B k)
          (openCovariancePresheafMap.{u, v} B j (k ≫ f)).val ≫
        (openCovariancePresheafMap.{u, v} B k f).val =
      (openCovariancePresheafMap.{u, v} B (j ≫ k) f).val
```

**`AlgebraicGeometry.SmallEtale.openCovarianceShriekMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceTransitivity.lean, line 926](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/OpenCovarianceTransitivity.lean#L926). The attribute's comment: “part (3), transitivity”.

> **Stacks 0F6S, part (3).** Transitivity of covariance after sheafification: for nested open
> subschemes of the source, the covariance map of the direct image with compact support along the
> composite open immersion is the composite of the two covariance maps.

```lean
public theorem openCovarianceShriekMap_comp :
    (openShriekCompIso.{u, v} B j k f).hom ≫
        Functor.whiskerLeft (openRestriction.{u, v} B k)
          (openCovarianceShriekMap.{u, v} B j (k ≫ f)) ≫
        openCovarianceShriekMap.{u, v} B k f =
      openCovarianceShriekMap.{u, v} B (j ≫ k) f
```

## Tag 0F5H, a lemma

[Tag 0F5H](https://stacks.math.columbia.edu/tag/0F5H) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.cechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverComplex.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverComplex.lean#L296). The attribute's comment: “the complex, functorial in the abelian sheaf”.

> **Stacks 0F5H.** The Čech complex of an open covering `X = ⋃_{i ∈ I} X_i` for the direct
> image with compact support along a locally quasi-finite morphism `f : X ⟶ Y`: a complex
>
> `… → ⊕_{i₀,i₁} f_{i₀i₁,!}((-)|_{X_{i₀i₁}}) → ⊕_{i₀} f_{i₀,!}((-)|_{X_{i₀}}) → f_!(-) → 0`
>
> of functors on abelian sheaves on the small étale site of `X`, hence functorial in the sheaf.

```lean
public def cechComplex : ChainComplex (ShriekCat.{u, v} B X Y) ℕ
```

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.cechComplexObj_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverExactness.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverExactness.lean#L427). The attribute's comment: “exactness of the complex”.

> **Stacks 0F5H, exactness.** For a family of open subschemes covering `X`, the Čech complex
> `⋯ ⟶ ⊕_{i₀} f_{i₀,!}(F|_{X_{i₀}}) ⟶ f_!F ⟶ 0` of an abelian sheaf `F` on the small étale site of
> `X` is acyclic.

```lean
public theorem cechComplexObj_acyclic (hU : (⨆ i, U i) = ⊤)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    (cechComplexObj.{u, v} B f U F).Acyclic
```

## Tag 0F5I, a remark

[Tag 0F5I](https://stacks.math.columbia.edu/tag/0F5I) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.exists_isSeparated_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean#L97). The attribute's comment: “the covering with every restriction separated, by affine opens”.

> **Stacks 0F5I.** A locally quasi-finite morphism `f : X ⟶ Y` admits an open covering
> `X = ⋃_{i ∈ I} X_i` such that every restriction `f_{i₀…i_p} : X_{i₀…i_p} ⟶ Y` is separated: the
> covering of `X` by its affine opens is one.

```lean
public theorem exists_isSeparated_openCover :
    ∃ (J : Type (max (u + 1) v)) (V : J → (B.inclusion.obj X).Opens),
      (⨆ j, V j) = ⊤ ∧ (∀ j, IsAffineOpen (V j)) ∧
        ∀ {n : ℕ} (t : Fin (n + 1) → J),
          IsSeparated (B.inclusion.map (openSchemeι B (coverOpen B V t) ≫ f))
```

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.cechFamilyIsoProperSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean#L121). The attribute's comment: “each term is the construction of Section 0F4W, the restrictions being separated”.

> **Stacks 0F5I.** Along a covering by affine opens the term of the Čech complex at a tuple of
> indices is the proper-support direct image of Section 0F4W: the restriction `f_{i₀…i_p}` is
> separated, so the two models of the direct image with compact support agree on it by
> Stacks 0F6N.

```lean
public def cechFamilyIsoProperSupport (hU : ∀ i, IsAffineOpen (U i)) {n : ℕ}
    (t : Fin (n + 1) → I) :
    cechFamily.{u, v} B f U (n + 1) t ≅
      openRestriction.{u, v} B (openSchemeι B (coverOpen B U t)) ⋙
        properSupportFunctor.{u, max (u + 1) v} B (openSchemeι B (coverOpen B U t) ≫ f)
```

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.cechComplexObj_isColimit_cokernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean#L150). The attribute's comment: “f\_! F is the cokernel of the penultimate map of the complex of Stacks 0F5H”.

> **Stacks 0F5I.** For an open covering of `X` and an abelian sheaf `F` on the small étale site
> of `X`, the sheaf `f_! F` is the cokernel of the penultimate differential of the Čech complex of
> Stacks 0F5H:
>
> `f_! F = Coker(⊕_{i₀,i₁} f_{i₀i₁,!} F|_{X_{i₀i₁}} ⟶ ⊕_{i₀} f_{i₀,!} F|_{X_{i₀}})`.

```lean
public def cechComplexObj_isColimit_cokernel (hU : (⨆ i, U i) = ⊤)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    IsColimit (CokernelCofork.ofπ ((cechAugMap.{u, v} B f U 1).app F)
      ((cechComplexObj.{u, v} B f U F).d_comp_d 2 1 0))
```

**`AlgebraicGeometry.SmallEtale.OpenCoverShriek.cechComplex_isColimit_cokernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCoverCokernel.lean#L185). The attribute's comment: “the functor f\_! is that cokernel, the alternative construction”.

> **Stacks 0F5I.** The alternative construction of the functor `f_!` for a locally quasi-finite
> morphism: for an open covering of `X` the functor `f_!` is the cokernel, in the category of
> functors on abelian sheaves of the small étale site of `X`, of the penultimate differential of the
> Čech complex of Stacks 0F5H. Taking this cokernel as the definition of `f_!` therefore recovers
> `f_!` together with its functoriality.

```lean
public def cechComplex_isColimit_cokernel (hU : (⨆ i, U i) = ⊤) :
    IsColimit (CokernelCofork.ofπ (cechAugMap.{u, v} B f U 1)
      ((cechComplex.{u, v} B f U).d_comp_d 2 1 0))
```

## Tag 0F78, a remark

[Tag 0F78](https://stacks.math.columbia.edu/tag/0F78) in the Stacks Project.

**`AlgebraicGeometry.sheafifiedPushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean#L66). The attribute's comment: “canonical map”.

> **Stacks 0F78.** The map from the sheafification of `G` to the small-étale direct image of
> the sheafification of `G'` induced by a map `α : G ⟶ g_* G'` of abelian presheaves.

```lean
public def sheafifiedPushforwardMap
    (G : (SmallEtale B S.obj S.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (G' : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (α : G ⟶ (smallEtaleBaseChange B g).op ⋙ G') :
    (SmallEtale.topology B S.obj S.property).sheafify G ⟶
      (smallEtaleBaseChange B g).op ⋙
        (SmallEtale.topology B T.obj T.property).sheafify G'
```

**`AlgebraicGeometry.sheafifiedPushforwardMap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean#L84). The attribute's comment: “commutative square”.

> **Stacks 0F78.** The induced map commutes with the two sheafification maps.

```lean
public theorem sheafifiedPushforwardMap_comm
    (G : (SmallEtale B S.obj S.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (G' : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (α : G ⟶ (smallEtaleBaseChange B g).op ⋙ G') :
    (SmallEtale.topology B S.obj S.property).toSheafify G ≫
        sheafifiedPushforwardMap B g G G' α =
      α ≫ Functor.whiskerLeft (smallEtaleBaseChange B g).op
        ((SmallEtale.topology B T.obj T.property).toSheafify G')
```

**`AlgebraicGeometry.sheafifiedPushforwardMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean#L97). The attribute's comment: “uniqueness”.

> **Stacks 0F78.** The commutative square of the previous result determines the induced map
> uniquely.

```lean
public theorem sheafifiedPushforwardMap_unique
    (G : (SmallEtale B S.obj S.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (G' : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (α : G ⟶ (smallEtaleBaseChange B g).op ⋙ G')
    (β : (SmallEtale.topology B S.obj S.property).sheafify G ⟶
      (smallEtaleBaseChange B g).op ⋙
        (SmallEtale.topology B T.obj T.property).sheafify G')
    (hβ : (SmallEtale.topology B S.obj S.property).toSheafify G ≫ β =
      α ≫ Functor.whiskerLeft (smallEtaleBaseChange B g).op
        ((SmallEtale.topology B T.obj T.property).toSheafify G')) :
    β = sheafifiedPushforwardMap B g G G' α
```

**`AlgebraicGeometry.sheafifiedPushforwardAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean#L113). The attribute's comment: “adjoint map”.

> **Stacks 0F78.** The induced map transported through the adjunction between the small-étale
> inverse image and direct image along `g`.

```lean
public def sheafifiedPushforwardAdjoint
    (G : (SmallEtale B S.obj S.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (G' : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (α : G ⟶ (smallEtaleBaseChange B g).op ⋙ G') :
    ((smallEtaleBaseChange B g).sheafPullback AddCommGrpCat.{u + 1}
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)).obj
        ⟨(SmallEtale.topology B S.obj S.property).sheafify G,
          (SmallEtale.topology B S.obj S.property).sheafify_isSheaf G⟩ ⟶
      ⟨(SmallEtale.topology B T.obj T.property).sheafify G',
        (SmallEtale.topology B T.obj T.property).sheafify_isSheaf G'⟩
```

**`AlgebraicGeometry.sheafifiedPushforwardMap_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SheafifiedPushforward.lean#L137). The attribute's comment: “geometric stalk formula”.

> **Stacks 0F78.** The germ, at a lift `p'` of a geometric point of `T`, of a section of `G`
> over an étale neighborhood `U` of the image point is carried by the adjoint map to the germ
> over the base-changed neighborhood of the image of the section under `α`.

```lean
public theorem sheafifiedPushforwardMap_stalk
    (G : (SmallEtale B S.obj S.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (G' : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
    (α : G ⟶ (smallEtaleBaseChange B g).op ⋙ G')
    (s' : GeometricPoint T.obj)
    [HasColimit ((Functor.Elements.π
      (geometricPointFiber B T.obj T.property s')).op ⋙
        (((smallEtaleBaseChange B g).sheafPullback AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property)).obj
            ⟨(SmallEtale.topology B S.obj S.property).sheafify G,
              (SmallEtale.topology B S.obj S.property).sheafify_isSheaf G⟩).obj)]
    [HasColimit ((Functor.Elements.π
      (geometricPointFiber B T.obj T.property s')).op ⋙
        (SmallEtale.topology B T.obj T.property).sheafify G')] :
    let F : Sheaf (SmallEtale.topology B S.obj S.property) AddCommGrpCat.{u + 1} :=
      ⟨(SmallEtale.topology B S.obj S.property).sheafify G,
        (SmallEtale.topology B S.obj S.property).sheafify_isSheaf G⟩
    let D := (Functor.Elements.π
      (geometricPointFiber B T.obj T.property s')).op ⋙
        (((smallEtaleBaseChange B g).sheafPullback AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property)).obj F).obj
    let D' := (Functor.Elements.π
      (geometricPointFiber B T.obj T.property s')).op ⋙
        (SmallEtale.topology B T.obj T.property).sheafify G'
    ∀ (U : SmallEtale B S.obj S.property)
        (p' : (geometricPointFiber B T.obj T.property s').obj
          ((smallEtaleBaseChange B g).obj U)),
        (((SmallEtale.topology B S.obj S.property).toSheafify G).app (op U) ≫
            (((smallEtaleBaseChange B g).sheafAdjunctionContinuous
              AddCommGrpCat.{u + 1}
              (SmallEtale.topology B S.obj S.property)
              (SmallEtale.topology B T.obj T.property)).unit.app F).hom.app (op U) ≫
            colimit.ι D (op (Functor.elementsMk _ ((smallEtaleBaseChange B g).obj U) p')) ≫
            colim.map (Functor.whiskerLeft
              ((Functor.Elements.π
                (geometricPointFiber B T.obj T.property s')).op)
              (sheafifiedPushforwardAdjoint B g G G' α).hom)) =
          α.app (op U) ≫
            ((SmallEtale.topology B T.obj T.property).toSheafify G').app
              (op ((smallEtaleBaseChange B g).obj U)) ≫
              colimit.ι D' (op (Functor.elementsMk _ ((smallEtaleBaseChange B g).obj U) p'))
```

## Tag 0F5J, a lemma

[Tag 0F5J](https://stacks.math.columbia.edu/tag/0F5J) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fiberPointBaseChange_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L102). The attribute's comment: “the bijection of geometric fibres induced by the horizontal morphism”.

> **Stacks 0F5J.** For a cartesian square, `p` induces a bijection from the geometric fibre
> of `f'` over a geometric point `t` of `Y'` onto the geometric fibre of `f` over the image of
> `t`: transitivity of fibre products identifies `X'_t` with `X_{g ∘ t}`.

```lean
public theorem fiberPointBaseChange_bijective (sq : IsPullback p f' f g)
    (t : GeometricPoint Y'.obj) :
    Function.Bijective (fiberPointBaseChange B p f' f g sq t)
```

**`AlgebraicGeometry.SmallEtale.fiberStalkBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L149). The attribute's comment: “the identification of the stalks over corresponding points of the fibres”.

> **Stacks 0F5J.** The stalk of the inverse image `p⁻¹F` at a point `x` of the geometric
> fibre of `f'` is the stalk of `F` at the corresponding point of the geometric fibre of `f`.
> This is the right vertical arrow of the comparison square of Stacks 0F5J.

```lean
public def fiberStalkBaseChangeIso (sq : IsPullback p f' f g) (t : GeometricPoint Y'.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v})
    (x : GeometricFiberPoint B f' t) :
    etaleStalk B X.obj X.property
        ((fiberPointBaseChange B p f' f g sq t x).toGeometricPoint B f
          (t.map (B.inclusion.map g))) F.obj ≅
      etaleStalk B X'.obj X'.property (x.toGeometricPoint B f' t)
        ((abPullback.{u, v} B p).obj F).obj
```

**`AlgebraicGeometry.SmallEtale.fiberStalksBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L164). The attribute's comment: “the comparison of the two direct sums of stalks over the geometric fibres”.

> **Stacks 0F5J.** The direct sums of stalks over the two geometric fibres agree: the fibres
> are in bijection through `p`, and over corresponding points the stalks of `F` and of `p⁻¹F`
> agree.

```lean
public def fiberStalksBaseChangeEquiv (sq : IsPullback p f' f g) (t : GeometricPoint Y'.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    fiberStalks.{u, max (u + 1) v} B f (t.map (B.inclusion.map g)) F ≃+
      fiberStalks.{u, max (u + 1) v} B f' t ((abPullback.{u, v} B p).obj F)
```

**`AlgebraicGeometry.SmallEtale.fiberStalksBaseChangeEquiv_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L190). The attribute's comment: “functoriality in the sheaf of the comparison of the direct sums of stalks”.

> **Stacks 0F5J.** The comparison of the two direct sums of stalks is functorial in the
> abelian sheaf: it intertwines the map induced on the direct sum of stalks over the geometric
> fibre of `f` by a morphism of sheaves with the map induced over the geometric fibre of `f'` by
> its inverse image.

```lean
public theorem fiberStalksBaseChangeEquiv_natural (sq : IsPullback p f' f g)
    (t : GeometricPoint Y'.obj)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}}
    (φ : F ⟶ G) (w : fiberStalks.{u, max (u + 1) v} B f (t.map (B.inclusion.map g)) F) :
    fiberStalksBaseChangeEquiv B p f' f g sq t G
        (fiberStalksMap.{u, max (u + 1) v} B f (t.map (B.inclusion.map g)) φ w) =
      fiberStalksMap.{u, max (u + 1) v} B f' t ((abPullback.{u, v} B p).map φ)
        (fiberStalksBaseChangeEquiv B p f' f g sq t F w)
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L232). The attribute's comment: “the base-change isomorphism on the stalk at a geometric point of the base”.

> **Stacks 0F5J.** The base-change comparison on stalks: for a geometric point `t` of `Y'`
> the stalk of `g⁻¹f_!F` at `t` is the stalk of `f'_!p⁻¹F` at `t`. It is obtained from the stalk
> decompositions of Stacks 0F5F on both sides, the bijection of geometric fibres and the
> identification of the stalks over corresponding points of the fibres, so it is compatible with
> those decompositions by construction.

```lean
public def fShriekStalkBaseChangeIso (sq : IsPullback p f' f g) (t : GeometricPoint Y'.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    etaleStalk B Y'.obj Y'.property t
        ((abPullback.{u, v} B g).obj ((fShriekFunctor.{u, v} B f).obj F)).obj ≅
      etaleStalk B Y'.obj Y'.property t
        ((fShriekFunctor.{u, v} B f').obj ((abPullback.{u, v} B p).obj F)).obj
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkBaseChangeIso_comp_fShriekStalkIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChange.lean#L250). The attribute's comment: “compatibility of the stalkwise comparison with the decompositions of 0F5F”.

> **Stacks 0F5J.** The precise compatibility of the stalkwise base-change comparison with the
> stalk decompositions of Stacks 0F5F: the square whose horizontal arrows are those
> decompositions, whose left vertical arrow is the comparison preceded by the identification of
> the stalk of an inverse image, and whose right vertical arrow is the summandwise comparison of
> the two direct sums, commutes.

```lean
public theorem fShriekStalkBaseChangeIso_comp_fShriekStalkIso (sq : IsPullback p f' f g)
    (t : GeometricPoint Y'.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    (etaleStalkSmallEtalePullObjIso B g t AddCommGrpCat.{max (u + 1) v}
          ((fShriekFunctor.{u, v} B f).obj F)).inv ≫
        (fShriekStalkBaseChangeIso B p f' f g sq t F).hom ≫
        (fShriekStalkIso.{u, v} B f' t ((abPullback.{u, v} B p).obj F)).hom =
      (fShriekStalkIso.{u, v} B f (t.map (B.inclusion.map g)) F).hom ≫
        AddCommGrpCat.ofHom
          (fiberStalksBaseChangeEquiv B p f' f g sq t F).toAddMonoidHom
```

**`AlgebraicGeometry.SmallEtale.fiberStalkComponent_fiberBaseChangeSectionsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L215). The attribute's comment: “the germ of a base-changed supported section at a point of the geometric fibre”.

> **Stacks 0F5J.** The germ at a point of the geometric fibre of `f'` of the base change of a
> supported section is the germ of the section at the corresponding point of the geometric fibre
> of `f`, read through the identification of the two stalks. This is the commutative square of the
> source, on a single summand of the stalk decompositions of Stacks 0F5F.

```lean
public theorem fiberStalkComponent_fiberBaseChangeSectionsMap
    (s : supportedSections B X.obj X.property F (baseChange B f V) E.1
      (finiteSupport_isLocallyClosed B f V E))
    (x : GeometricFiberPoint B f' t) :
    fiberStalkComponent.{u, u + 1} B f' t ((abPullback.{u, u + 1} B p).obj F)
        (baseChange B g V) (geometricPointFiberBaseChangeEquiv B g t V u)
        (fiberBaseChangeSupport B p f' f g sq V E)
        (fiberBaseChangeSectionsMap.{u, u + 1} B p f' f g sq V E F s) x =
      (fiberStalkBaseChangeIso.{u, u + 1} B p f' f g sq t F x).hom
        (fiberStalkComponent.{u, u + 1} B f (t.map (B.inclusion.map g)) F V u E s
          (fiberPointBaseChange B p f' f g sq t x))
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeDiagramMap_comp_fiberStalkHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L338). The attribute's comment: “the germ decompositions exchanged by the base-change map on supported sections”.

> **Stacks 0F5J.** The germ decompositions of Stacks 0F5F on the two sides of the square are
> exchanged by the base-change map on supported sections and the comparison of the direct sums of
> stalks over the two geometric fibres.

```lean
public theorem fiberBaseChangeDiagramMap_comp_fiberStalkHom
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyOfFiniteType (B.inclusion.map f')] :
    fiberBaseChangeDiagramMap.{u, u + 1} B p f' f g sq V F E ≫
        fiberStalkHom.{u, u + 1} B f' t ((abPullback.{u, u + 1} B p).obj F)
          (baseChange B g V) (geometricPointFiberBaseChangeEquiv B g t V u)
          (fiberBaseChangeSupport B p f' f g sq V E) =
      fiberStalkHom.{u, u + 1} B f (t.map (B.inclusion.map g)) F V u E ≫
        (AddEquiv.toAddCommGrpIso
          (fiberStalksBaseChangeEquiv.{u, u + 1} B p f' f g sq t F)).hom
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeMap_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L593). The attribute's comment: “the base-change map on the stalk at a geometric point, through the 0F5F decompositions”.

> **Stacks 0F5J.** On the stalk at a geometric point `t` of `Y'` the base-change map is the
> base-change comparison of stalks: the identification of the stalk of an inverse image, the stalk
> decomposition of Stacks 0F5F for `f`, and the comparison of the direct sums of stalks over the
> two geometric fibres.

```lean
public theorem fShriekBaseChangeMap_stalk :
    (etaleStalkPresheafFunctor B Y'.obj Y'.property t AddCommGrpCat.{u + 1}).map
          (fShriekBaseChangeMap.{u} B p f' f g sq F).hom ≫
        (fShriekStalkIso.{u, u + 1} B f' t ((abPullback.{u, u + 1} B p).obj F)).hom =
      (etaleStalkSmallEtalePullObjIso B g t AddCommGrpCat.{u + 1}
          ((fShriekFunctor.{u, u + 1} B f).obj F)).hom ≫
        (fShriekStalkIso.{u, u + 1} B f (t.map (B.inclusion.map g)) F).hom ≫
        (AddEquiv.toAddCommGrpIso
          (fiberStalksBaseChangeEquiv.{u, u + 1} B p f' f g sq t F)).hom
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeMap_stalk_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 662](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L662). The attribute's comment: “the stalk of the base-change map is the stalkwise base-change isomorphism”.

> **Stacks 0F5J.** The base-change map is, on the stalk at a geometric point of `Y'`, the
> base-change isomorphism of stalks of `StacksFrontier.AlgebraicGeometry.Etale.FShriekBaseChange`.

```lean
public theorem fShriekBaseChangeMap_stalk_eq :
    (etaleStalkPresheafFunctor B Y'.obj Y'.property t AddCommGrpCat.{u + 1}).map
        (fShriekBaseChangeMap.{u} B p f' f g sq F).hom =
      (fShriekStalkBaseChangeIso.{u, u + 1} B p f' f g sq t F).hom
```

**`AlgebraicGeometry.SmallEtale.isIso_fShriekBaseChangeMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 684](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L684). The attribute's comment: “the base-change map is an isomorphism”.

> **Stacks 0F5J.** The base-change map `g⁻¹f_!F ⟶ f'_!(p⁻¹F)` is an isomorphism: it is an
> isomorphism on the stalk at every geometric point of `Y'`, both sides becoming the direct sum of
> the stalks of `F` over the geometric fibre, and a map of abelian étale sheaves which is an
> isomorphism on every geometric stalk is an isomorphism, which is Stacks 03PU.

```lean
public instance isIso_fShriekBaseChangeMap :
    IsIso (fShriekBaseChangeMap.{u} B p f' f g sq F)
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L703). The attribute's comment: “the isomorphism g⁻¹f\_!F ≅ f'\_!(p⁻¹F), functorial in F”.

> **Stacks 0F5J.** For a cartesian square with `f` locally quasi-finite there is an
> isomorphism `g⁻¹f_!F ≅ f'_!(p⁻¹F)`, functorial in the abelian sheaf `F` on the small étale site
> of `X`: the map `c` of the source, sheafified and transposed, which is an isomorphism because it
> is one on every geometric stalk.

```lean
public def fShriekBaseChangeNatIso :
    fShriekFunctor.{u, u + 1} B f ⋙ abPullback.{u, u + 1} B g ≅
      abPullback.{u, u + 1} B p ⋙ fShriekFunctor.{u, u + 1} B f'
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeNatIso_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 722](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L722). The attribute's comment: “the isomorphism agrees with the stalk descriptions of 0F5F”.

> **Stacks 0F5J.** The base-change isomorphism agrees with the stalk descriptions of
> Stacks 0F5F: on the stalk at a geometric point `t` of `Y'` it is the identification of the stalk
> of an inverse image followed by the stalk decomposition of `f_!F` at the image point, the
> comparison of the direct sums of stalks over the two geometric fibres, and the inverse of the
> stalk decomposition of `f'_!(p⁻¹F)`.

```lean
public theorem fShriekBaseChangeNatIso_stalk (t : GeometricPoint Y'.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    (etaleStalkPresheafFunctor B Y'.obj Y'.property t AddCommGrpCat.{u + 1}).map
          ((fShriekBaseChangeNatIso.{u} B p f' f g sq).hom.app F).hom ≫
        (fShriekStalkIso.{u, u + 1} B f' t ((abPullback.{u, u + 1} B p).obj F)).hom =
      (etaleStalkSmallEtalePullObjIso B g t AddCommGrpCat.{u + 1}
          ((fShriekFunctor.{u, u + 1} B f).obj F)).hom ≫
        (fShriekStalkIso.{u, u + 1} B f (t.map (B.inclusion.map g)) F).hom ≫
        (AddEquiv.toAddCommGrpIso
          (fiberStalksBaseChangeEquiv.{u, u + 1} B p f' f g sq t F)).hom
```

**`AlgebraicGeometry.SmallEtale.exists_fShriekBaseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean, line 751](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeIso.lean#L751). The attribute's comment: “the isomorphism, functorial in the sheaf and compatible with the 0F5F stalk descriptions”.

> **Stacks 0F5J.** For a cartesian square of a big étale site with `f` locally quasi-finite
> there is an isomorphism `g⁻¹f_!F ≅ f'_!(p⁻¹F)`, functorial in `F` in the abelian sheaves on the
> small étale site of `X`, which agrees with the stalk descriptions of Stacks 0F5F: on the stalk
> at a geometric point `t` of `Y'` it is the identification of the stalk of an inverse image, the
> stalk decomposition of `f_!F` at the image point, and the comparison of the direct sums of the
> stalks over the two geometric fibres.
>
> Only the hypotheses of the source are assumed: the finite-type and quasi-finiteness conditions
> on the base change `f'` are supplied from the cartesian square.

```lean
public theorem exists_fShriekBaseChangeIso :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    ∃ e : fShriekFunctor.{u, u + 1} B f ⋙ abPullback.{u, u + 1} B g ≅
        abPullback.{u, u + 1} B p ⋙ fShriekFunctor.{u, u + 1} B f',
      ∀ (t : GeometricPoint Y'.obj)
        (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}),
        (etaleStalkPresheafFunctor B Y'.obj Y'.property t AddCommGrpCat.{u + 1}).map
              (e.hom.app F).hom ≫
            (fShriekStalkIso.{u, u + 1} B f' t ((abPullback.{u, u + 1} B p).obj F)).hom =
          (etaleStalkSmallEtalePullObjIso B g t AddCommGrpCat.{u + 1}
              ((fShriekFunctor.{u, u + 1} B f).obj F)).hom ≫
            (fShriekStalkIso.{u, u + 1} B f (t.map (B.inclusion.map g)) F).hom ≫
            (AddEquiv.toAddCommGrpIso
              (fiberStalksBaseChangeEquiv.{u, u + 1} B p f' f g sq t F)).hom
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangePresheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean#L232). The attribute's comment: “the map c of abelian presheaves”.

> **Stacks 0F5J.** The map `c` of the proof: the map of abelian presheaves on the small étale
> site of `Y` from the finite-support direct image `f_{p!}F` to the direct image along `g` of
> `f'_!(p⁻¹F)`.

```lean
public def fiberBaseChangePresheafMap
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    (finiteSupportPushforward.{u, u + 1} B f (fun _ => inferInstance)).1.obj F ⟶
      (smallEtaleBaseChange B g).op ⋙
        ((fShriekFunctor.{u, u + 1} B f').obj ((abPullback.{u, u + 1} B p).obj F)).obj
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean#L281). The attribute's comment: “the base-change map of sheaves, before it is shown to be an isomorphism”.

> **Stacks 0F5J.** The base-change map `g⁻¹f_!F ⟶ f'_!(p⁻¹F)` of abelian sheaves on the small
> étale site of `Y'`: the map `c` of the source, sheafified and transposed through the
> inverse-image adjunction along `g`.

```lean
public def fShriekBaseChangeMap
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    (abPullback.{u, u + 1} B g).obj ((fShriekFunctor.{u, u + 1} B f).obj F) ⟶
      (fShriekFunctor.{u, u + 1} B f').obj ((abPullback.{u, u + 1} B p).obj F)
```

**`AlgebraicGeometry.SmallEtale.fShriekBaseChangeNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeMap.lean#L380). The attribute's comment: “functoriality in the sheaf of the base-change map of sheaves”.

> **Stacks 0F5J.** The base-change map `g⁻¹f_!F ⟶ f'_!(p⁻¹F)` is functorial in `F`: it is a
> morphism of functors on abelian sheaves on the small étale site of `X`.

```lean
public def fShriekBaseChangeNatTrans :
    fShriekFunctor.{u, u + 1} B f ⋙ abPullback.{u, u + 1} B g ⟶
      abPullback.{u, u + 1} B p ⋙ fShriekFunctor.{u, u + 1} B f'
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeColimitMap_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeRestriction.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeRestriction.lean#L362). The attribute's comment: “naturality in the test object of the map c”.

> **Stacks 0F5J.** The base-change map on finite-support sections is compatible with the
> restriction maps of the finite-support direct image presheaves: restricting a section to a
> smaller test object `V₁` of `Y` and then base changing it along the square is base changing it
> and then restricting along `V'₁ ⟶ V'`. This is the naturality in `V` of the map `c` of the
> source.

```lean
public theorem fiberBaseChangeColimitMap_restriction :
    finiteSupportBaseChangeHom B f F i ≫ fiberBaseChangeColimitMap B p f' f g sq V₁ F =
      fiberBaseChangeColimitMap B p f' f g sq V F ≫
        finiteSupportBaseChangeHom B f' ((abPullback.{u, v} B p).obj F)
          ((smallEtaleBaseChange B g).map i)
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L461). The attribute's comment: “the base change of a support finite over the test object”.

> **Stacks 0F5J.** The base change of a support finite over `V` along the cartesian square:
> the inverse image of the support under the comparison of the two étale base changes. It is
> again a support finite over `V'`.

```lean
public def fiberBaseChangeSupport (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property) (E : FiniteSupport B f V) :
    FiniteSupport B f' (baseChange B g V)
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L614). The attribute's comment: “the pullback map H\_Z(F) ⟶ H\_\{Z'}(p⁻¹F) on supported sections”.

> **Stacks 0F5J.** The pullback map on supported sections: a section of `F` supported on a
> support `E` finite over `V` is carried by the unit of the inverse-image adjunction to a section
> of `p⁻¹F` supported on the base change of `E`.

```lean
public def fiberBaseChangeSectionsMap (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property) (E : FiniteSupport B f V)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    supportedSections B X.obj X.property F (baseChange B f V) E.1
        (finiteSupport_isLocallyClosed B f V E) →+
      supportedSections B X'.obj X'.property ((abPullback.{u, v} B p).obj F)
        (baseChange B f' (baseChange B g V)) (fiberBaseChangeSupport B p f' f g sq V E).1
        (finiteSupport_isLocallyClosed B f' (baseChange B g V)
          (fiberBaseChangeSupport B p f' f g sq V E))
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeSectionsMap_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 796](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L796). The attribute's comment: “compatibility of the pullback map with the transitions of the colimit”.

> **Stacks 0F5J.** The pullback map on supported sections is compatible with the transition
> maps of Stacks 0F6H: enlarging the support commutes with base change. This is what makes the
> pullback maps a map out of the colimit defining `f_{p!}F`.

```lean
public theorem fiberBaseChangeSectionsMap_transition (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property) {E E₁ : FiniteSupport B f V} (hle : E ≤ E₁)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    (fiberBaseChangeSectionsMap B p f' f g sq V E₁ F).comp
        (supportedSectionsMap B X.obj X.property F (baseChange B f V) E.1 E₁.1
          (finiteSupport_isLocallyClosed B f V E) (finiteSupport_isLocallyClosed B f V E₁) hle
          (finiteSupport_closedWithin B f V E E₁ hle)) =
      (supportedSectionsMap B X'.obj X'.property ((abPullback.{u, v} B p).obj F)
          (baseChange B f' (baseChange B g V))
          (fiberBaseChangeSupport B p f' f g sq V E).1
          (fiberBaseChangeSupport B p f' f g sq V E₁).1
          (finiteSupport_isLocallyClosed B f' (baseChange B g V)
            (fiberBaseChangeSupport B p f' f g sq V E))
          (finiteSupport_isLocallyClosed B f' (baseChange B g V)
            (fiberBaseChangeSupport B p f' f g sq V E₁))
          (fiberBaseChangeSupport_mono B p f' f g sq V hle)
          (finiteSupport_closedWithin B f' (baseChange B g V)
            (fiberBaseChangeSupport B p f' f g sq V E)
            (fiberBaseChangeSupport B p f' f g sq V E₁)
            (fiberBaseChangeSupport_mono B p f' f g sq V hle))).comp
        (fiberBaseChangeSectionsMap B p f' f g sq V E F)
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeSectionsMap_sheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L851). The attribute's comment: “functoriality in the sheaf of the pullback map on supported sections”.

> **Stacks 0F5J.** The pullback map on supported sections is functorial in the abelian
> sheaf: a morphism of sheaves on `X` acts on the pullbacks through its inverse image.

```lean
public theorem fiberBaseChangeSectionsMap_sheafMap (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property) (E : FiniteSupport B f V)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}}
    (φ : F ⟶ G) :
    (fiberBaseChangeSectionsMap B p f' f g sq V E G).comp
        (supportedSectionsSheafMap B X.obj X.property φ (baseChange B f V) E.1
          (finiteSupport_isLocallyClosed B f V E)) =
      (supportedSectionsSheafMap B X'.obj X'.property ((abPullback.{u, v} B p).map φ)
          (baseChange B f' (baseChange B g V))
          (fiberBaseChangeSupport B p f' f g sq V E).1
          (finiteSupport_isLocallyClosed B f' (baseChange B g V)
            (fiberBaseChangeSupport B p f' f g sq V E))).comp
        (fiberBaseChangeSectionsMap B p f' f g sq V E F)
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeColimitMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 917](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L917). The attribute's comment: “the map c on finite-support sections over a test object”.

> **Stacks 0F5J.** The base-change map on finite-support sections over an étale test object
> `V` of `Y`: the generator of a support `Z` carrying a section `s` goes to the generator of the
> base change of `Z` carrying the pullback of `s`. This is the map `c` of the source, over `V`.

```lean
public def fiberBaseChangeColimitMap (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    finiteSupportSections B f F V ⟶
      finiteSupportSections B f' ((abPullback.{u, v} B p).obj F) (baseChange B g V)
```

**`AlgebraicGeometry.SmallEtale.fiberBaseChangeColimitMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean, line 940](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekBaseChangeSupport.lean#L940). The attribute's comment: “functoriality in the sheaf of the map c over a test object”.

> **Stacks 0F5J.** The base-change map on finite-support sections over an étale test object
> is functorial in the abelian sheaf.

```lean
public theorem fiberBaseChangeColimitMap_natural (sq : IsPullback p f' f g)
    (V : SmallEtale B Y.obj Y.property)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}}
    (φ : F ⟶ G) :
    colim.map (finiteSupportDiagramMap B f φ V) ≫
        fiberBaseChangeColimitMap B p f' f g sq V G =
      fiberBaseChangeColimitMap B p f' f g sq V F ≫
        colim.map (finiteSupportDiagramMap B f' ((abPullback.{u, v} B p).map φ)
          (baseChange B g V))
```

## Tag 0F79, a lemma

[Tag 0F79](https://stacks.math.columbia.edu/tag/0F79) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekCompProperIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportCompat.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportCompat.lean#L70). The attribute's comment: “part (b), compatibility with the base change isomorphisms of 0F5J and 0F55”.

> **Stacks 0F79, part (b).** For a base change `b : Z₁ ⟶ Z`, with cartesian squares
> `X₁ = X ×_Y Y₁` and `Y₁ = Y ×_Z Z₁`, the isomorphism `(g ∘ f)_! ≅ g_! ∘ f_!` of Stacks 0F79 is
> compatible with the base-change isomorphisms of Stacks 0F5J and 0F55: the base-change
> isomorphism `b⁻¹ (g ∘ f)_! F ≅ (g₁ ∘ f₁)_! a⁻¹ F` of Stacks 0F5J followed by the isomorphism for
> `f₁` and `g₁` equals `b⁻¹` of the isomorphism for `f` and `g`, followed by the base change
> `b⁻¹ g_! ⟶ g₁_! b'⁻¹` of Stacks 0F55 and `g₁_!` of the base-change isomorphism
> `b'⁻¹ f_! F ≅ f₁_! a⁻¹ F` of Stacks 0F5J.

```lean
public theorem fShriekCompProperIso_baseChange :
    letI := locallyOfFiniteType_of_isPullback B a f₁ f b' sq₁
    letI := locallyQuasiFinite_of_isPullback B a f₁ f b' sq₁
    letI := locallyOfFiniteType_of_isPullback B b' g₁ g b sq₂
    letI : IsSeparated (B.inclusion.map g₁) :=
      MorphismProperty.of_isPullback (sq₂.map B.inclusion) inferInstance
    letI : LocallyQuasiFinite (B.inclusion.map (f₁ ≫ g₁)) :=
      MorphismProperty.of_isPullback ((sq₁.paste_vert sq₂).map B.inclusion) inferInstance
    (fShriekBaseChangeNatIso.{u} B a (f₁ ≫ g₁) (f ≫ g) b (sq₁.paste_vert sq₂)).hom.app F ≫
        (fShriekCompProperIso.{u, u + 1} B f₁ g₁).hom.app ((abPullback.{u, u + 1} B a).obj F) =
      (abPullback.{u, u + 1} B b).map ((fShriekCompProperIso.{u, u + 1} B f g).hom.app F) ≫
        properSupportBaseChange.{u, u + 1} B b' g₁ g b sq₂
          ((fShriekFunctor.{u, u + 1} B f).obj F) ≫
        (properSupportFunctor.{u, u + 1} B g₁).map
          ((fShriekBaseChangeNatIso.{u} B a f₁ f b' sq₁).hom.app F)
```

**`AlgebraicGeometry.SmallEtale.fShriekCompProperIso_eq_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportCompat.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportCompat.lean#L108). The attribute's comment: “part (c), the isomorphism of 0F50 via the identifications of 0F6N for f' separated”.

> **Stacks 0F79, part (c).** If `f` is separated as well, the isomorphism
> `(g ∘ f)_! ≅ g_! ∘ f_!` of Stacks 0F79 is the isomorphism `(g ∘ f)_! = g_! ∘ f_!` of
> proper-support direct images of Stacks 0F50, read through the identifications of Stacks 0F6N of
> `(g ∘ f)_!` and `f_!` with their proper-support models.

```lean
public theorem fShriekCompProperIso_eq_of_isSeparated [IsSeparated (B.inclusion.map f)] :
    letI := isSeparated_map_comp B f g
    fShriekCompProperIso.{u, v} B f g =
      fShriekFunctorIsoProperSupport.{u, v} B (f ≫ g) ≪≫
        (properSupportFunctor_compIso B f g).val.symm ≪≫
        Functor.isoWhiskerRight (fShriekFunctorIsoProperSupport.{u, v} B f).symm
          (properSupportFunctor.{u, max (u + 1) v} B g)
```

**`AlgebraicGeometry.SmallEtale.fShriekCompProperIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportIso.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportIso.lean#L592). The attribute's comment: “the canonical isomorphism g\_! ∘ f'\_! ≅ f\_!”.

> **Stacks 0F79.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of a big étale site with `f`
> and `f ≫ g` locally quasi-finite (locally of finite type and locally quasi-finite) and `g`
> separated and locally of finite type. Then there is a canonical isomorphism of functors on
> abelian étale sheaves `(g ∘ f)_! ≅ g_! ∘ f_!`, where `f_!` and `(g ∘ f)_!` are the direct images
> with compact support of locally quasi-finite morphisms (Stacks 0F6R) and `g_!` is the
> proper-support direct image of Stacks 0F4X. Its component at `F` is the map `c'` of the source,
> `AlgebraicGeometry.SmallEtale.sepCompShriekMap`: the sheafification of the map sending a local
> generator `(T, s)` of `(g ∘ f)_{p!} F` over `W` to the generator `(T, s)` of `f_{p!} F` over
> `W ×_Z Y`, through `X_{W ×_Z Y} = X_W`.

```lean
public def fShriekCompProperIso :
    fShriekFunctor.{u, v} B (f ≫ g) ≅
      fShriekFunctor.{u, v} B f ⋙ properSupportFunctor.{u, max (u + 1) v} B g
```

**`AlgebraicGeometry.SmallEtale.sepCompShriekMap_openCovariance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportOpen.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompProperSupportOpen.lean#L400). The attribute's comment: “part (a), compatibility with covariance for open embeddings, Remarks 0F53, 0F6S”.

> **Stacks 0F79, part (a).** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be as in Stacks 0F79, let
> `jY : Y₁ ⟶ Y` be an open immersion, and let `X₁ = X ×_Y Y₁` with projections `jX : X₁ ⟶ X` and
> `f₁ : X₁ ⟶ Y₁`. Then the isomorphism `c'` of Stacks 0F79 is compatible with covariance with
> respect to open embeddings: the composite of the covariance map
> `(jX ≫ f ≫ g)_!(F|_{X₁}) ⟶ (f ≫ g)_! F` of Stacks 0F6S with `c' : (f ≫ g)_! F ⟶ g_!(f_! F)`
> equals the composite of `c'` for `f₁` and `jY ≫ g`,
> `(f₁ ≫ jY ≫ g)_!(F|_{X₁}) ⟶ (jY ≫ g)_!(f₁_!(F|_{X₁}))`, the identification
> `f₁_!(F|_{X₁}) ≅ (f_! F)|_{Y₁}` of Stacks 0F5J ("the construction of `f_!` is local on the base")
> and the extension by zero `(jY ≫ g)_!((f_! F)|_{Y₁}) ⟶ g_!(f_! F)` of Stacks 0F53.

```lean
public theorem sepCompShriekMap_openCovariance :
    letI : IsOpenImmersion (B.inclusion.map jX) :=
      MorphismProperty.of_isPullback (sq.flip.map B.inclusion) inferInstance
    letI := locallyOfFiniteType_of_isPullback B jX f₁ f jY sq
    letI := locallyQuasiFinite_of_isPullback B jX f₁ f jY sq
    letI : IsSeparated (B.inclusion.map (jY ≫ g)) := by
      rw [Functor.map_comp]
      infer_instance
    letI : LocallyQuasiFinite (B.inclusion.map (f₁ ≫ jY ≫ g)) := by
      rw [show f₁ ≫ jY ≫ g = jX ≫ f ≫ g by rw [← Category.assoc, ← sq.w, Category.assoc]]
      infer_instance
    (openCovarianceShriekMap.{u, u + 1} B jX (f ≫ g)).app F ≫ sepCompShriekMap.{u, u + 1} B f g F =
      eqToHom (congrArg (fun G => G.obj ((openRestriction.{u, u + 1} B jX).obj F))
        (fShriekFunctor_congr.{u, u + 1} B
          (show jX ≫ f ≫ g = f₁ ≫ jY ≫ g by rw [← Category.assoc, sq.w, Category.assoc]))) ≫
      sepCompShriekMap.{u, u + 1} B f₁ (jY ≫ g) ((openRestriction.{u, u + 1} B jX).obj F) ≫
      (properSupportFunctor.{u, u + 1} B (jY ≫ g)).map
        ((fShriekBaseChangeNatIso.{u} B jX f₁ f jY sq).inv.app F) ≫
      (openInclusionShriekMap.{u, u + 1} B jY g ((fShriekFunctor.{u, u + 1} B f).obj F)).val
```

## Tag 0F6T, a lemma

[Tag 0F6T](https://stacks.math.columbia.edu/tag/0F6T) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekCompIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompBaseChange.lean#L164). The attribute's comment: “part (5)”.

> **Stacks 0F6T, part (5).** For a diagram with both squares cartesian
> ```
> X' --c--> X
> |f'       |f
> Y' --b--> Y
> |g'       |g
> Z' --a--> Z
> ```
> and `f`, `g` locally quasi-finite, the composition isomorphisms and the base-change isomorphisms
> of Stacks 0F5J make the diagram
> ```
> a⁻¹(g ∘ f)_! ----------------> (g' ∘ f')_! c⁻¹
>      |                                |
> a⁻¹ g_! f_! --> g'_! b⁻¹ f_! --> g'_! f'_! c⁻¹
> ```
> commute. The base changes `f'` and `g'` are locally quasi-finite because `f` and `g` are.

```lean
public theorem fShriekCompIso_baseChange :
    letI := locallyOfFiniteType_of_isPullback B c f' f b sq₁
    letI := locallyQuasiFinite_of_isPullback B c f' f b sq₁
    letI := locallyOfFiniteType_of_isPullback B b g' g a sq₂
    letI := locallyQuasiFinite_of_isPullback B b g' g a sq₂
    (fShriekBaseChangeNatIso.{u} B c (f' ≫ g') (f ≫ g) a (sq₁.paste_vert sq₂)).hom ≫
        Functor.whiskerLeft (abPullback.{u, u + 1} B c) (fShriekCompIso.{u, u + 1} B f' g').hom =
      Functor.whiskerRight (fShriekCompIso.{u, u + 1} B f g).hom (abPullback.{u, u + 1} B a) ≫
        Functor.whiskerLeft (fShriekFunctor.{u, u + 1} B f)
          (fShriekBaseChangeNatIso.{u} B b g' g a sq₂).hom ≫
        Functor.whiskerRight (fShriekBaseChangeNatIso.{u} B c f' f b sq₁).hom
          (fShriekFunctor.{u, u + 1} B g')
```

**`AlgebraicGeometry.SmallEtale.fShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean#L136). The attribute's comment: “the canonical isomorphism (g ∘ f)\_! ≅ g\_! ∘ f\_!”.

> **Stacks 0F6T.** For composable locally quasi-finite morphisms `f : X ⟶ Y` and `g : Y ⟶ Z`
> there is a canonical isomorphism of functors `(g ∘ f)_! ≅ g_! ∘ f_!` on abelian étale sheaves:
> the comparison of `AlgebraicGeometry.SmallEtale.compShriekMap`, glued from the comparisons on the
> inverse images of the affine opens of `Y`, natural in the sheaf and an isomorphism on every
> geometric stalk.

```lean
public def fShriekCompIso :
    fShriekFunctor.{u, v} B (f ≫ g) ≅ fShriekFunctor.{u, v} B f ⋙ fShriekFunctor.{u, v} B g
```

**`AlgebraicGeometry.SmallEtale.fShriekCompIso_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean#L153). The attribute's comment: “part (3)”.

> **Stacks 0F6T, part (3).** At a geometric point `z̄` of `Z`, the isomorphism
> `((g ∘ f)_!F)_z̄ ≅ (g_!f_!F)_z̄` followed by the stalk decomposition
> `(g_!f_!F)_z̄ = ⊕_{g(ȳ) = z̄} (f_!F)_ȳ` of Stacks 0F5F is the stalk decomposition
> `((g ∘ f)_!F)_z̄ = ⊕_{g(f(x̄)) = z̄} F_x̄` followed by the regrouping of the geometric fibre of
> `g ∘ f` over the one of `g`, each `F_x̄` being placed in `(f_!F)_{f(x̄)} = ⊕_{f(x̄') = f(x̄)} F_x̄'`
> through the decomposition of Stacks 0F5F for `f`.

```lean
public theorem fShriekCompIso_stalk (s : GeometricPoint Z.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) v}) :
    ((geometricPointSitePoint B Z.obj Z.property s).sheafFiber
        (A := AddCommGrpCat.{max (u + 1) v})).map ((fShriekCompIso B f g).hom.app F) ≫
      (fShriekStalkIso.{u, v} B g s ((fShriekFunctor.{u, v} B f).obj F)).hom =
    (fShriekStalkIso.{u, v} B (f ≫ g) s F).hom ≫
      AddCommGrpCat.ofHom (compFiberStalksMap B f g s F)
```

**`AlgebraicGeometry.SmallEtale.fShriekCompIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompIso.lean#L275). The attribute's comment: “part (4)”.

> **Stacks 0F6T, part (4).** For a third locally quasi-finite morphism `h : Z ⟶ T` the two
> isomorphisms `(h ∘ g ∘ f)_! ≅ h_! ∘ g_! ∘ f_!` obtained from the composition isomorphisms agree:
> through `(h ∘ g)_! ∘ f_!` and through `h_! ∘ (g ∘ f)_!`. The identification
> `(h ∘ (g ∘ f))_! = ((h ∘ g) ∘ f)_!` along the associativity of composition is written out.

```lean
public theorem fShriekCompIso_assoc :
    eqToHom (fShriekFunctor_congr.{u, v} B (Category.assoc f g h)) ≫
        (fShriekCompIso B f (g ≫ h)).hom ≫
        Functor.whiskerLeft (fShriekFunctor.{u, v} B f) (fShriekCompIso B g h).hom =
      (fShriekCompIso B (f ≫ g) h).hom ≫
        Functor.whiskerRight (fShriekCompIso B f g).hom (fShriekFunctor.{u, v} B h)
```

**`AlgebraicGeometry.SmallEtale.fShriekCompIso_eq_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompSeparated.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompSeparated.lean#L463). The attribute's comment: “part (1)”.

> **Stacks 0F6T, part (1).** If `f` and `g` are separated, the isomorphism
> `(g ∘ f)_! ≅ g_! ∘ f_!` agrees with the identification `g_! f_! = (g ∘ f)_!` of proper-support
> direct images of Stacks 0F50, read through the identifications of Stacks 0F6N of the
> finite-support model of `f_!`, `g_!` and `(g ∘ f)_!` with the proper-support model.

```lean
public theorem fShriekCompIso_eq_of_isSeparated :
    fShriekCompIso B f g =
      fShriekFunctorIsoProperSupport.{u, v} B (f ≫ g) ≪≫
        (properSupportFunctor_compIso B f g).val.symm ≪≫
        Functor.isoWhiskerRight (fShriekFunctorIsoProperSupport.{u, v} B f).symm
          (properSupportFunctor.{u, max (u + 1) v} B g) ≪≫
        Functor.isoWhiskerLeft (fShriekFunctor.{u, v} B f)
          (fShriekFunctorIsoProperSupport.{u, v} B g).symm
```

**`AlgebraicGeometry.SmallEtale.fShriekCompIso_generator_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompSeparated.lean, line 787](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompSeparated.lean#L787). The attribute's comment: “part (2)”.

> **Stacks 0F6T, part (2).** If `g` is separated, the isomorphism `(g ∘ f)_! ≅ g_! ∘ f_!`
> agrees with the isomorphism of Stacks 0F79: read in the proper-support model of `g_!` through
> Stacks 0F6N, it is the sheafification of the map `c` of the proof of Stacks 0F79, which sends a
> local generator `(Z, s)` of `(g ∘ f)_{p!}F` over `W` — a section `s` of `F` over `X_W` supported
> on `Z ⊆ X_W` finite over `W` — to the generator `(Z, s)` of `f_{p!}F` over `W ×_Z Y`, through
> `X_{W ×_Z Y} = X_W`. The generators generate `(g ∘ f)_{p!}F`, so this determines the
> isomorphism.

```lean
public theorem fShriekCompIso_generator_of_isSeparated (W : SmallEtale B Z.obj Z.property)
    (E : FiniteSupport B (f ≫ g) W) (a : (finiteSupportDiagram B (f ≫ g) F W).obj E) :
    properSupportSection B g ((fShriekFunctor.{u, v} B f).obj F) W
        (((fShriekFunctorIsoProperSupport.{u, v} B g).hom.app
          ((fShriekFunctor.{u, v} B f).obj F)).hom.app (op W)
          (((fShriekCompIso B f g).hom.app F).hom.app (op W)
            ((finiteSupportPushforwardGenerator B (f ≫ g) F W E ≫
              (toSheafify (SmallEtale.topology B Z.obj Z.property)
                ((finiteSupportPushforward.{u, max (u + 1) v} B (f ≫ g)
                  (fun _ => inferInstance)).val.obj F)).app (op W)) a))) =
      (finiteSupportPushforwardGenerator B f F (baseChange B g W) (sepCompSupport B f g W E) ≫
        (toSheafify (SmallEtale.topology B Y.obj Y.property)
          ((finiteSupportPushforward.{u, max (u + 1) v} B f
            (fun _ => inferInstance)).val.obj F)).app (op (baseChange B g W)))
        (sepCompSection B f g F W E a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.4, Tag 0F6E](https://stacks.math.columbia.edu/tag/0F6E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
