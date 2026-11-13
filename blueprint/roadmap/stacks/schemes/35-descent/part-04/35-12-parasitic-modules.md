---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsParasitic, AlgebraicGeometry.IsParasiticFor, AlgebraicGeometry.bigZariskiCohomology_isZero_of_isParasitic, AlgebraicGeometry.bigEtaleCohomology_isZero_of_isParasitic, AlgebraicGeometry.bigSmoothCohomology_isZero_of_isParasitic, AlgebraicGeometry.bigSyntomicCohomology_isZero_of_isParasitic, AlgebraicGeometry.bigFppfCohomology_isZero_of_isParasitic, AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_zariski
statement: formalized
proof: formalized
---

# 35.12 Parasitic modules

Section 35.12 of the Stacks Project, [Tag 07AF](https://stacks.math.columbia.edu/tag/07AF). 4 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06ZL, a definition

[Tag 06ZL](https://stacks.math.columbia.edu/tag/06ZL) in the Stacks Project.

**`AlgebraicGeometry.IsParasitic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/Defs.lean#L53). The attribute's comment: “part (1)”.

> A presheaf of modules is *parasitic* when its sections vanish on every object of the site
> which is flat over the base scheme.

```lean
public abbrev IsParasitic (S : Scheme.{u}) {C : Type (u + 1)} [Category.{u} C]
    (toOver : C ⥤ Over S) {𝒪 : Cᵒᵖ ⥤ RingCat.{u}} (F : PresheafOfModules.{u} 𝒪) : Prop
```

**`AlgebraicGeometry.IsParasiticFor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/Defs.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/Defs.lean#L60). The attribute's comment: “part (2)”.

> A presheaf of modules is *parasitic for a topology* when its sections vanish on every
> member of every covering family of the base scheme.

```lean
public abbrev IsParasiticFor (S : Scheme.{u}) {C : Type (u + 1)} [Category.{u} C]
    (toOver : C ⥤ Over S) (isCovering : Covering C → Prop)
    {𝒪 : Cᵒᵖ ⥤ RingCat.{u}} (F : PresheafOfModules.{u} 𝒪) : Prop
```

## Tag 0755, a lemma

[Tag 0755](https://stacks.math.columbia.edu/tag/0755) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiCohomology_isZero_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean#L318). The attribute's comment: “flat\_parasitic\_vanishing”.

> A parasitic module on the big Zariski site has no cohomology at a flat object.

```lean
public theorem bigZariskiCohomology_isZero_of_isParasitic
    (B : AlgebraicGeometry.BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigZariskiOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S hS) RingCat.{u}}
    (F : SheafOfModules.{u} 𝒪)
    (hF : ∀ X : AlgebraicGeometry.BigZariskiOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom → Subsingleton (F.val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigZariskiOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj F).H' p U)
```

**`AlgebraicGeometry.bigEtaleCohomology_isZero_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean#L380). The attribute's comment: “flat\_parasitic\_vanishing”.

> A parasitic module on the big étale site has no cohomology at a flat object.

```lean
public theorem bigEtaleCohomology_isZero_of_isParasitic
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigEtaleOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S hS) RingCat.{u}}
    (F : SheafOfModules.{u} 𝒪)
    (hF : ∀ X : AlgebraicGeometry.BigEtaleOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom → Subsingleton (F.val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigEtaleOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj F).H' p U)
```

**`AlgebraicGeometry.bigSmoothCohomology_isZero_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean#L440). The attribute's comment: “flat\_parasitic\_vanishing”.

> A parasitic module on the big smooth site has no cohomology at a flat object.

```lean
public theorem bigSmoothCohomology_isZero_of_isParasitic
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    [HasSheafify (AlgebraicGeometry.BigSmoothOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S hS) RingCat.{u}}
    (F : SheafOfModules.{u} 𝒪)
    (hF : ∀ X : AlgebraicGeometry.BigSmoothOver B S hS,
      Flat ((Over.post (ObjectProperty.ι _)).obj X).hom →
        Subsingleton (F.val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigSmoothOver B S hS)
    (hU : Flat ((Over.post (ObjectProperty.ι _)).obj U).hom) (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj F).H' p U)
```

**`AlgebraicGeometry.bigSyntomicCohomology_isZero_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean#L512). The attribute's comment: “flat\_parasitic\_vanishing”.

> A parasitic module on the big syntomic site has no cohomology at a flat object.

```lean
public theorem bigSyntomicCohomology_isZero_of_isParasitic
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigSyntomicOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S hS) RingCat.{u}}
    (F : SheafOfModules.{u} 𝒪)
    (hF : ∀ X : AlgebraicGeometry.BigSyntomicOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom → Subsingleton (F.val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigSyntomicOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj F).H' p U)
```

**`AlgebraicGeometry.bigFppfCohomology_isZero_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatVanishing.lean#L596). The attribute's comment: “flat\_parasitic\_vanishing”.

> A parasitic module on the big fppf site has no cohomology at a flat object.

```lean
public theorem bigFppfCohomology_isZero_of_isParasitic
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) RingCat.{u}}
    (F : SheafOfModules.{u} 𝒪)
    (hF : ∀ X : AlgebraicGeometry.BigFppfOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom → Subsingleton (F.val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigFppfOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj F).H' p U)
```

**`AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean#L469). The attribute's comment: “topology\_parasitic\_vanishing”.

> Vanishing on objects open over the base in the big Zariski site.

```lean
public theorem cohomology_isZero_of_isParasiticFor_zariski
    (B : AlgebraicGeometry.BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigZariskiOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S hS) RingCat.{u}}
    (G : SheafOfModules.{u} 𝒪)
    (hG : ∀ E : Covering (AlgebraicGeometry.BigZariskiOver B S hS),
      IsIso (((Over.post B.inclusion).obj E.1).hom) →
      AlgebraicGeometry.BigZariskiOver.IsCovering B S hS E →
      ∀ i : E.2.I₀, Subsingleton (G.val.obj (Opposite.op (E.2.X i))))
    (U : AlgebraicGeometry.BigZariskiOver B S hS)
    (hU : IsOpenImmersion ((Over.post B.inclusion).obj U).hom)
    (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj G).H' p U)
```

**`AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean#L504). The attribute's comment: “topology\_parasitic\_vanishing”.

> Vanishing on objects étale over the base in the big étale site.

```lean
public theorem cohomology_isZero_of_isParasiticFor_etale
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigEtaleOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S hS) RingCat.{u}}
    (G : SheafOfModules.{u} 𝒪)
    (hG : ∀ E : Covering (AlgebraicGeometry.BigEtaleOver B S hS),
      IsIso (((Over.post B.inclusion).obj E.1).hom) →
      AlgebraicGeometry.BigEtaleOver.IsCovering B S hS E →
      ∀ i : E.2.I₀, Subsingleton (G.val.obj (Opposite.op (E.2.X i))))
    (U : AlgebraicGeometry.BigEtaleOver B S hS)
    (hU : Etale ((Over.post B.inclusion).obj U).hom)
    (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj G).H' p U)
```

**`AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean#L538). The attribute's comment: “topology\_parasitic\_vanishing”.

> Vanishing on objects smooth over the base in the big smooth site.

```lean
public theorem cohomology_isZero_of_isParasiticFor_smooth
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    [HasSheafify (AlgebraicGeometry.BigSmoothOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S hS) RingCat.{u}}
    (G : SheafOfModules.{u} 𝒪)
    (hG : ∀ E : Covering (AlgebraicGeometry.BigSmoothOver B S hS),
      IsIso (((Over.post (ObjectProperty.ι _)).obj E.1).hom) →
      AlgebraicGeometry.BigSmoothOver.IsCovering B S hS E →
      ∀ i : E.2.I₀, Subsingleton (G.val.obj (Opposite.op (E.2.X i))))
    (U : AlgebraicGeometry.BigSmoothOver B S hS)
    (hU : Smooth ((Over.post (ObjectProperty.ι _)).obj U).hom)
    (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj G).H' p U)
```

**`AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean#L572). The attribute's comment: “topology\_parasitic\_vanishing”.

> Vanishing on objects syntomic over the base in the big syntomic site.

```lean
public theorem cohomology_isZero_of_isParasiticFor_syntomic
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigSyntomicOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S hS) RingCat.{u}}
    (G : SheafOfModules.{u} 𝒪)
    (hG : ∀ E : Covering (AlgebraicGeometry.BigSyntomicOver B S hS),
      IsIso (((Over.post B.inclusion).obj E.1).hom) →
      AlgebraicGeometry.BigSyntomicOver.IsCovering B S hS E →
      ∀ i : E.2.I₀, Subsingleton (G.val.obj (Opposite.op (E.2.X i))))
    (U : AlgebraicGeometry.BigSyntomicOver B S hS)
    (hU : Syntomic ((Over.post B.inclusion).obj U).hom)
    (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj G).H' p U)
```

**`AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean, line 602](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/TopologyVanishing.lean#L602). The attribute's comment: “topology\_parasitic\_vanishing”.

> Vanishing on objects flat and locally of finite presentation over the
> base in the big fppf site.

```lean
public theorem cohomology_isZero_of_isParasiticFor_fppf
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) RingCat.{u}}
    (G : SheafOfModules.{u} 𝒪)
    (hG : ∀ E : Covering (AlgebraicGeometry.BigFppfOver B S hS),
      IsIso (((Over.post B.inclusion).obj E.1).hom) →
      AlgebraicGeometry.BigFppfOver.IsCovering B S hS E →
      ∀ i : E.2.I₀, Subsingleton (G.val.obj (Opposite.op (E.2.X i))))
    (U : AlgebraicGeometry.BigFppfOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom ∧
      LocallyOfFinitePresentation ((Over.post B.inclusion).obj U).hom)
    (p : ℕ) :
    IsZero (((SheafOfModules.toSheaf _).obj G).H' p U)
```

## Tag 07AG, a lemma

[Tag 07AG](https://stacks.math.columbia.edu/tag/07AG) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiPushforward_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L490). The attribute's comment: “big Zariski direct image”.

> Direct image of a parasitic module on the big Zariski site is parasitic.

```lean
public theorem bigZariskiPushforward_isParasitic
    (B : AlgebraicGeometry.BigZariskiSite.{u}) (T S : B.Schemes) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigZariskiOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigZariskiOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((SheafOfModules.pushforward.{u} φ).obj F).val
```

**`AlgebraicGeometry.bigZariskiHigherDirectImage_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L510). The attribute's comment: “big Zariski higher direct images”.

> Every higher direct image of a parasitic module on the big Zariski site is
> parasitic.

```lean
public theorem bigZariskiHigherDirectImage_isParasitic
    (B : AlgebraicGeometry.BigZariskiSite.{u}) (T S : B.Schemes) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigZariskiOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigZariskiOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigZariskiOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) (i : ℕ) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((Functor.rightDerived (C := SheafOfModules.{u} 𝒪T) (D := SheafOfModules.{u} 𝒪S)
        (SheafOfModules.pushforward.{u} φ) i).obj F).val
```

**`AlgebraicGeometry.bigEtalePushforward_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L546). The attribute's comment: “big étale direct image”.

> Direct image of a parasitic module on the big étale site is parasitic.

```lean
public theorem bigEtalePushforward_isParasitic
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (T S : B.Scheme) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigEtaleOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigEtaleOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((SheafOfModules.pushforward.{u} φ).obj F).val
```

**`AlgebraicGeometry.bigEtaleHigherDirectImage_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L565). The attribute's comment: “big étale higher direct images”.

> Higher direct images of a parasitic module on the big étale site are parasitic.

```lean
public theorem bigEtaleHigherDirectImage_isParasitic
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (T S : B.Scheme) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigEtaleOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigEtaleOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigEtaleOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) (i : ℕ) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((Functor.rightDerived (C := SheafOfModules.{u} 𝒪T) (D := SheafOfModules.{u} 𝒪S)
        (SheafOfModules.pushforward.{u} φ) i).obj F).val
```

**`AlgebraicGeometry.bigSmoothPushforward_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L601). The attribute's comment: “big smooth direct image”.

> Direct image of a parasitic module on the big smooth site is parasitic.

```lean
public theorem bigSmoothPushforward_isParasitic
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (T S : B.category) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigSmoothOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigSmoothOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post (ObjectProperty.ι _)) F.val) :
    IsParasitic S.1 (Over.post (ObjectProperty.ι _))
      ((SheafOfModules.pushforward.{u} φ).obj F).val
```

**`AlgebraicGeometry.bigSmoothHigherDirectImage_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L620). The attribute's comment: “big smooth higher direct images”.

> Higher direct images of a parasitic module on the big smooth site are parasitic.

```lean
public theorem bigSmoothHigherDirectImage_isParasitic
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (T S : B.category) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigSmoothOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigSmoothOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigSmoothOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post (ObjectProperty.ι _)) F.val) (i : ℕ) :
    IsParasitic S.1 (Over.post (ObjectProperty.ι _))
      ((Functor.rightDerived (C := SheafOfModules.{u} 𝒪T) (D := SheafOfModules.{u} 𝒪S)
        (SheafOfModules.pushforward.{u} φ) i).obj F).val
```

**`AlgebraicGeometry.bigSyntomicPushforward_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L656). The attribute's comment: “big syntomic direct image”.

> Direct image of a parasitic module on the big syntomic site is parasitic.

```lean
public theorem bigSyntomicPushforward_isParasitic
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) (T S : B.category) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigSyntomicOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((SheafOfModules.pushforward.{u} φ).obj F).val
```

**`AlgebraicGeometry.bigSyntomicHigherDirectImage_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L675). The attribute's comment: “big syntomic higher direct images”.

> Higher direct images of a parasitic module on the big syntomic site are parasitic.

```lean
public theorem bigSyntomicHigherDirectImage_isParasitic
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) (T S : B.category) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigSyntomicOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigSyntomicOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) (i : ℕ) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((Functor.rightDerived (C := SheafOfModules.{u} 𝒪T) (D := SheafOfModules.{u} 𝒪S)
        (SheafOfModules.pushforward.{u} φ) i).obj F).val
```

**`AlgebraicGeometry.bigFppfPushforward_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 711](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L711). The attribute's comment: “big fppf direct image”.

> Direct image of a parasitic module on the big fppf site is parasitic.

```lean
public theorem bigFppfPushforward_isParasitic
    (B : AlgebraicGeometry.BigFppfSite.{u}) (T S : B.Schemes) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigFppfOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigFppfOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigFppfOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((SheafOfModules.pushforward.{u} φ).obj F).val
```

**`AlgebraicGeometry.bigFppfHigherDirectImage_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/ParasiticPushforward.lean#L730). The attribute's comment: “big fppf higher direct images”.

> Higher direct images of a parasitic module on the big fppf site are parasitic.

```lean
public theorem bigFppfHigherDirectImage_isParasitic
    (B : AlgebraicGeometry.BigFppfSite.{u}) (T S : B.Schemes) (f : T ⟶ S)
    {𝒪S : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S.1 S.2) RingCat.{u}}
    {𝒪T : Sheaf (AlgebraicGeometry.BigFppfOver.topology B T.1 T.2) RingCat.{u}}
    (φ : 𝒪S ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u}
        (AlgebraicGeometry.BigFppfOver.topology B S.1 S.2)
        (AlgebraicGeometry.BigFppfOver.topology B T.1 T.2)).obj
          𝒪T)
    (F : SheafOfModules.{u} 𝒪T)
    (hF : IsParasitic T.1 (Over.post B.inclusion) F.val) (i : ℕ) :
    IsParasitic S.1 (Over.post B.inclusion)
      ((Functor.rightDerived (C := SheafOfModules.{u} 𝒪T) (D := SheafOfModules.{u} 𝒪S)
        (SheafOfModules.pushforward.{u} φ) i).obj F).val
```

## Tag 0756, a lemma

[Tag 0756](https://stacks.math.columbia.edu/tag/0756) in the Stacks Project.

**`AlgebraicGeometry.bigFppfCohomology_map_bijective_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyComparison.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyComparison.lean#L299). The attribute's comment: “cohomology comparison step, from Tag 0755”.

> **A morphism of sheaves of `𝒪`-modules on the big fppf site over `S` whose kernel and
> cokernel are parasitic induces isomorphisms `H^p(U, ℱ) → H^p(U, 𝒢)` at every object `U` flat
> over `S`.**
>
> This is the step of Stacks 0756 which rests on Stacks 0755: the kernel and the cokernel have
> vanishing cohomology at `U` by `AlgebraicGeometry.bigFppfCohomology_isZero_of_isParasitic`, and
> a morphism with that property is an isomorphism on cohomology. The source lemma then identifies
> `H^p(U, ℱ)` with the small-site cohomology `H^p(U, 𝒢|_{U_τ})` by Stacks 03DW, which this
> statement does not assert.
>
> The parasitic hypotheses are the pointwise expansion of `AlgebraicGeometry.IsParasitic`, as in
> `AlgebraicGeometry.bigFppfCohomology_isZero_of_isParasitic`, and the kernel and cokernel are
> those of the category of sheaves of `𝒪`-modules.
>
> The clause string says which step this is.  Its hypotheses are part (2) of [Stacks, Tag 06ZL] —
> vanishing at every object flat over `S`, finite presentation not assumed — whereas 0756 derives
> part (1), vanishing at the objects flat *and locally of finite presentation* over `S`.  The step
> in that second form is `AlgebraicGeometry.bigFppfCohomology_map_bijective_of_isParasiticFor`
> below, which carries the same tag with a clause string naming it.

```lean
public theorem bigFppfCohomology_map_bijective_of_isParasitic
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u}]
    [(AlgebraicGeometry.BigFppfOver.topology B S hS).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) RingCat.{u}}
    {F G : SheafOfModules.{u} 𝒪} (φ : F ⟶ G)
    (hker : ∀ X : AlgebraicGeometry.BigFppfOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom →
        Subsingleton ((kernel φ).val.obj (Opposite.op X)))
    (hcoker : ∀ X : AlgebraicGeometry.BigFppfOver B S hS,
      Flat ((Over.post B.inclusion).obj X).hom →
        Subsingleton ((cokernel φ).val.obj (Opposite.op X)))
    (U : AlgebraicGeometry.BigFppfOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    Function.Bijective
      (Stacks.Cohomology.LongExactSequence.map.{w}
        ((SheafOfModules.toSheaf 𝒪).map φ) p U)
```

**`AlgebraicGeometry.bigFppfCohomology_map_bijective_of_isParasiticFor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyComparison.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyComparison.lean#L358). The attribute's comment: “cohomology comparison step, from Tag 0755, at the objects flat and locally of finite presentation over S, which is the shape 0756 uses”.

> **A morphism of sheaves of `𝒪`-modules on the big fppf site over `S` whose kernel and
> cokernel are parasitic for the fppf topology induces isomorphisms `H^p(U, ℱ) → H^p(U, 𝒢)` at
> every object `U` flat and locally of finite presentation over `S`.**
>
> This is the step of [Stacks, Tag 0756] which rests on [Stacks, Tag 0755], in the form 0756 uses
> it: the kernel and the cokernel have vanishing cohomology at `U` by
> `AlgebraicGeometry.cohomology_isZero_of_isParasiticFor_fppf`, which is part (1) of 0755, and a
> morphism with that property is an isomorphism on cohomology by
> `Stacks.Cohomology.LongExactSequence.bijective_map_of_subsingleton_kernel_cokernel`.
>
> The hypotheses are `AlgebraicGeometry.IsParasiticFor`, part (2) of [Stacks, Tag 06ZL], for the
> fppf coverings of `S`: vanishing on the members of fppf coverings of the base, which are exactly
> the objects flat and locally of finite presentation over `S`.  They are what 0756 derives from
> its assumptions (1) and (2), and they are weaker than the `AlgebraicGeometry.IsParasitic` of
> `AlgebraicGeometry.bigFppfCohomology_map_bijective_of_isParasitic`, which asks for vanishing at
> every flat object, finite presentation not assumed.  Correspondingly the conclusion here is at
> the objects flat and locally of finite presentation, which is where 0756 states it.
>
> This is the form with parasiticity hypothesised, which is what an arbitrary morphism needs.  For
> a morphism which is an isomorphism on sections over every such object the two hypotheses are
> themselves theorems, and the resulting statement is
> `AlgebraicGeometry.bigFppfCohomology_map_bijective_of_isIso_sections`
> (`StacksFrontier.AlgebraicGeometry.Descent.Parasitic.FlatCohomologySectionwiseIso`).  The
> identification of `H^p(U, ℱ)` with the small-site cohomology `H^p(U, 𝒢|_{U_τ})`, which is the
> conclusion of 0756, is established at `τ = Zariski` and `U = S` by
> `AlgebraicGeometry.BigFppfOver.zariskiSmallSiteCohomologyAddEquiv`
> (`StacksFrontier.AlgebraicGeometry.Descent.Parasitic.FlatCohomologySmallSiteComparison`).

```lean
public theorem bigFppfCohomology_map_bijective_of_isParasiticFor
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u}]
    [(AlgebraicGeometry.BigFppfOver.topology B S hS).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) AddCommGrpCat.{u})]
    {𝒪 : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) RingCat.{u}}
    {F G : SheafOfModules.{u} 𝒪} (φ : F ⟶ G)
    (hker : AlgebraicGeometry.IsParasiticFor S (Over.post B.inclusion)
      (AlgebraicGeometry.BigFppfOver.IsCovering B S hS) (kernel φ).val)
    (hcoker : AlgebraicGeometry.IsParasiticFor S (Over.post B.inclusion)
      (AlgebraicGeometry.BigFppfOver.IsCovering B S hS) (cokernel φ).val)
    (U : AlgebraicGeometry.BigFppfOver B S hS)
    (hU : Flat ((Over.post B.inclusion).obj U).hom ∧
      LocallyOfFinitePresentation ((Over.post B.inclusion).obj U).hom) (p : ℕ) :
    Function.Bijective
      (Stacks.Cohomology.LongExactSequence.map.{w}
        ((SheafOfModules.toSheaf 𝒪).map φ) p U)
```

**`AlgebraicGeometry.BigFppfOver.flatSmallEtaleSiteCohomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyEtaleConclusion.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyEtaleConclusion.lean#L277). The attribute's comment: “étale topology”.

> **The conclusion of [Stacks, Tag 0756] at `τ = étale`.**  Let `B` be a big fppf site, `S` a
> scheme below its cutoff and `𝒢` a sheaf of `𝒪`-modules on `(Sch/S)_fppf` such that
>
> 1. `𝒢|_{S_étale}` is quasi-coherent on the small étale site of `S`, and
> 2. for every object of `(Sch/S)_fppf` flat and locally of finite presentation over `S`, with
>    structure morphism `g : X ⟶ S`, the canonical map `ε_g^*(𝒢|_{S_étale}) ⟶ 𝒢|_{X_étale}` of
>    `AlgebraicGeometry.BigFppfOver.etaleClause2Map` is an isomorphism; this is the adjoint
>    transpose of the restriction map `𝒢|_{S_étale} ⟶ ε_{g,*}(𝒢|_{X_étale})` by
>    `AlgebraicGeometry.BigFppfOver.etaleClause2Map_eq_homEquiv_symm`.
>
> Then for **every** object `U` of `(Sch/S)_fppf` flat and locally of finite presentation over `S`,
> with scheme `X`, and every `p`,
>
> ```
> H^p(U, 𝒢)  ≅  H^p(U, 𝒢|_{U_étale}).
> ```
>
> The left-hand side is global cohomology of `𝒢|_{(Sch/X)_fppf}` on the big fppf site of `X`,
> which is the reading of cohomology over an object that
> `AlgebraicGeometry.BigFppfOver.flatSmallSiteCohomologyAddEquiv` fixes at `τ = Zariski`; the
> right-hand side is the cohomology of the size-bounded small étale site of `X` of
> [Stacks, Tag 021B] with values in the restriction of `𝒢` along
> `a_X : ((Sch/X)_fppf, 𝒪) ⟶ (X_étale, 𝒪)`.
>
> The attribute records the topology: this is the tag at `τ = étale`.  See
> `AlgebraicGeometry.BigFppfOver.flatSmallSiteCohomologyAddEquiv` for the tag at
> `τ = Zariski`.

```lean
public def flatSmallEtaleSiteCohomologyAddEquiv (p : ℕ) :
    Sheaf.H.{u} ((SheafOfModules.toSheaf (structureSheaf B (objScheme B S hS U)
        (contains_objScheme B S hS U))).obj ((objRestrict B S hS U).obj G)) p ≃+
      Sheaf.H.{u} ((SheafOfModules.toSheaf (SmallEtale.structureSheaf B.toBigEtaleSite
        (objScheme B S hS U) (contains_objScheme B S hS U))).obj
          (objSmallEtaleRestrict B S hS U G)) p
```

**`AlgebraicGeometry.BigFppfOver.flatSmallSiteCohomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyGeneralBase.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyGeneralBase.lean#L457). The attribute's comment: “Zariski topology”.

> **The conclusion of [Stacks, Tag 0756] at `τ = Zar`.**  Let `B` be a big fppf site, `S` a
> scheme below its cutoff and `𝒢` a sheaf of `𝒪`-modules on `(Sch/S)_fppf` such that
>
> 1. `𝒢|_{S_Zar}` is quasi-coherent, and
> 2. for every object of `(Sch/S)_fppf` flat and locally of finite presentation over `S`, with
>    structure morphism `g : X ⟶ S`, the canonical map `g^*(𝒢|_{S_Zar}) ⟶ 𝒢|_{X_Zar}`,
>    `AlgebraicGeometry.BigFppfOver.zariskiClause2Map`, is an isomorphism; this is the adjoint
>    transpose of the restriction map `𝒢|_{S_Zar} ⟶ g_*(𝒢|_{X_Zar})` by
>    `AlgebraicGeometry.BigFppfOver.zariskiClause2Map_eq_homEquiv_symm`, and it is an isomorphism
>    exactly when the transpose of restriction along `g^{-1}V ⟶ V` is, by
>    `AlgebraicGeometry.BigFppfOver.isIso_zariskiClause2Map_iff`.
>
> Then for **every** object `U` of `(Sch/S)_fppf` flat and locally of finite presentation over `S`,
> with scheme `X`, and every `p`,
>
> ```
> H^p(U, 𝒢)  ≅  H^p(U, 𝒢|_{U_Zar}).
> ```
>
> The left-hand side is global cohomology of `𝒢|_{(Sch/X)_fppf}` on the big fppf site of `X`, the
> localization of `(Sch/S)_fppf` at `U` by [Stacks, Tag 06WI]; the right-hand side is the cohomology
> of the site of opens of `X` with values in the restriction of `𝒢` along the inclusion of the small
> Zariski site of `X`.  See `AlgebraicGeometry.BigFppfOver.flatSmallZariskiSiteCohomologyAddEquiv`
> for the same statement with that side read on the site `AlgebraicGeometry.SmallZariski` of
> [Stacks, Tag 020T] (2).
>
> This is `AlgebraicGeometry.BigFppfOver.zariskiSmallSiteCohomologyAddEquiv` — the conclusion at
> the base of a big site — applied at the base `X` to `𝒢|_{(Sch/X)_fppf}`.  Its two hypotheses
> there are clause (1) over `X`, which is
> `AlgebraicGeometry.BigFppfOver.isQuasicoherent_objZariskiRestrict`, and clause (2) over `X`,
> which is `AlgebraicGeometry.BigFppfOver.isIso_zariskiClause2Map_objRestrict` and rests on the
> mate square `AlgebraicGeometry.BigFppfOver.mateSquare_objRestrictCounit`.
>
> The attribute records the topology: this is the tag at `τ = Zariski`, and nothing here claims the
> étale half; that is
> `AlgebraicGeometry.BigFppfOver.flatSmallEtaleSiteCohomologyAddEquiv`, in
> `StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyEtaleConclusion.lean`.

```lean
public def flatSmallSiteCohomologyAddEquiv (p : ℕ) :
    Sheaf.H.{u} ((SheafOfModules.toSheaf (structureSheaf B (objScheme B S hS U)
        (contains_objScheme B S hS U))).obj ((objRestrict B S hS U).obj G)) p ≃+
      Sheaf.H.{u} ((SheafOfModules.toSheaf (objScheme B S hS U).ringCatSheaf).obj
        ((restrictModule B (objScheme B S hS U) (contains_objScheme B S hS U)).obj
          ((objRestrict B S hS U).obj G))) p
```

**`AlgebraicGeometry.BigFppfOver.flatSmallZariskiSiteCohomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyGeneralBase.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/FlatCohomologyGeneralBase.lean#L488). The attribute's comment: “Zariski topology, with the small site read as in 020T (2)”.

> **The conclusion of [Stacks, Tag 0756] at `τ = Zar`, with the right-hand side on the small
> Zariski site.**  Under the hypotheses of
> `AlgebraicGeometry.BigFppfOver.flatSmallSiteCohomologyAddEquiv`, for every object `U` of
> `(Sch/S)_fppf` flat and locally of finite presentation over `S`, with scheme `X`, and every `p`,
>
> ```
> H^p(U, 𝒢)  ≅  H^p(X_Zar, (𝒢|_{X_Zar})^a),
> ```
>
> the right-hand side being the cohomology of the small Zariski site of [Stacks, Tag 020T] (2)
> with values in the associated sheaf of [Stacks, Tag 03DU] (4) at `τ = Zariski`.  This is the
> previous statement composed with the small Zariski link of [Stacks, Tag 03DW] clause (2),
> `AlgebraicGeometry.smallZariskiQuasiCoherentSiteCohomologyAddEquiv`.
>
> The big Zariski site `BZ` carrying `X_Zar` is unrelated to the big fppf site `B`: the restriction
> `𝒢|_{X_Zar}` is produced as an `𝒪_X`-module and only then read on `X_Zar`.
>
> The attribute records the topology: this is the tag at `τ = Zariski`.

```lean
public def flatSmallZariskiSiteCohomologyAddEquiv (BZ : BigZariskiSite.{u})
    (hXZ : BZ.Contains (objScheme B S hS U)) (p : ℕ) :
    Sheaf.H.{u} ((SheafOfModules.toSheaf (structureSheaf B (objScheme B S hS U)
        (contains_objScheme B S hS U))).obj ((objRestrict B S hS U).obj G)) p ≃+
      Sheaf.H.{u} (@smallZariskiAssociatedSheaf BZ (objScheme B S hS U) hXZ
        ((restrictModule B (objScheme B S hS U) (contains_objScheme B S hS U)).obj
          ((objRestrict B S hS U).obj G))
        (isQuasicoherent_objZariskiRestrict B S hS U G hqc (hcl2 U hU₁ hU₂))) p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.12, Tag 07AF](https://stacks.math.columbia.edu/tag/07AF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
