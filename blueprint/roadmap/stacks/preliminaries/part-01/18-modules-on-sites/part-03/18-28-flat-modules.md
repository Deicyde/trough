---
declaration: section
origin: cited
lean: Stacks.IsFlat, Stacks.SheafOfModules.IsFlat, AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat, AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlatMap, AlgebraicGeometry.SheafOfModules.IsFlat, AlgebraicGeometry.SheafOfModules.IsFlatMap, AlgebraicGeometry.SheafOfModules.PresheafOfModules.isFlat_of_objectwise_flat, Stacks.SheafOfModules.FlatSheafification.isFlat_sheafification
statement: formalized
proof: formalized
---

# 18.28 Flat modules

Section 18.28 of the Stacks Project, [Tag 03EQ](https://stacks.math.columbia.edu/tag/03EQ). 16 tags here are carried by 42 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03ER, a definition

[Tag 03ER](https://stacks.math.columbia.edu/tag/03ER) in the Stacks Project.

**`Stacks.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactness.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactness.lean#L391). The attribute's comment: “part (1), for the objectwise tensor product Stacks.tensorRight of this file, whose two module universes are independent of each other and of the ring universe. The tree carries a second objectwise tensor product, and part (1) for that one is AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat, which is also where parts (2) and (4) of the tag are registered”.

> A presheaf of modules is flat when tensoring on the right with it is an exact
> endofunctor.

```lean
abbrev IsFlat (F : PresheafOfModules.{z} (ringPresheaf O)) : Prop
```

**`Stacks.SheafOfModules.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactness.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactness.lean#L590). The attribute's comment: “part (3), for Stacks.sheafTensorRight, the sheafified tensor product over Stacks.commRingSheafToRingSheaf. Part (3) over Stacks.SheafOfModules.Tensor.ringSheaf is AlgebraicGeometry.SheafOfModules.IsFlat, which is also where part (4) of the tag is registered”.

> A sheaf of modules is flat when tensoring on the right with it is an exact endofunctor
> on sheaves of modules.

```lean
abbrev IsFlat {O : Sheaf J CommRingCat.{w}}
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}]
    [HasWeakSheafify J AddCommGrpCat.{z}]
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) : Prop
```

**`AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L256). The attribute's comment: “part (1), for the objectwise tensor product AlgebraicGeometry.SheafOfModules.PresheafOfModules.tensorRight of this file; part (2) just below is stated in terms of it. Part (1) for the other objectwise tensor product in the tree, Stacks.tensorRight of StacksFrontier.Algebra.Category.ModuleCat.Sheaf.TensorExactness, is Stacks.IsFlat”.

> A presheaf of modules is flat when tensoring on the right with it is an
> exact endofunctor.

```lean
abbrev IsFlat {O : Cᵒᵖ ⥤ CommRingCat.{w}}
    (F : _root_.PresheafOfModules.{z} (ringPresheaf O)) : Prop
```

**`AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlatMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L263). The attribute's comment: “part (2)”.

> A morphism of presheaves of rings is flat when its target ring presheaf,
> viewed as a module over the source by restriction of scalars, is flat.

```lean
abbrev IsFlatMap {O O' : Cᵒᵖ ⥤ CommRingCat.{w}} (f : O ⟶ O') : Prop
```

**`AlgebraicGeometry.SheafOfModules.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L285). The attribute's comment: “part (3), over Stacks.SheafOfModules.Tensor.ringSheaf; cf. Stacks.SheafOfModules.IsFlat”. References: SGA 4 V (1.1), “commutative case”.

> A sheaf of modules is flat when tensoring on the right with it is an exact
> endofunctor on sheaves of modules.
>
> This is part (3) of tag 03ER for the native tensor bifunctor, and part (4) just below
> is stated in terms of it. `Stacks.SheafOfModules.IsFlat` uses the same native tensor
> functor.

```lean
abbrev IsFlat {O : Sheaf J CommRingCat.{w}}
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}]
    [HasWeakSheafify J AddCommGrpCat.{z}]
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) : Prop
```

**`AlgebraicGeometry.SheafOfModules.IsFlatMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L294). The attribute's comment: “part (4)”.

> A morphism of sheaves of rings is flat when its target ring sheaf, viewed
> as a module over the source by restriction of scalars, is flat.

```lean
abbrev IsFlatMap {O O' : Sheaf J CommRingCat.{w}} (f : O ⟶ O') : Prop
```

## Tag 03ES, a lemma

[Tag 03ES](https://stacks.math.columbia.edu/tag/03ES) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.PresheafOfModules.isFlat_of_objectwise_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ObjectwiseFlat.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ObjectwiseFlat.lean#L91).

> **A presheaf of modules whose sections over every object are flat is flat.** Finite limits
> and finite colimits of presheaves of modules are computed objectwise, so exactness of the
> objectwise tensor endofunctor is an objectwise condition, and over each object it is exactness
> of tensoring modules by the sections there.

```lean
theorem isFlat_of_objectwise_flat {O : Cᵒᵖ ⥤ CommRingCat.{w}}
    (F : _root_.PresheafOfModules.{z} (ringPresheaf O))
    (hF : ∀ U : Cᵒᵖ, Module.Flat ((ringPresheaf O).obj U) (F.obj U)) :
    IsFlat F
```

## Tag 03ET, a lemma

[Tag 03ET](https://stacks.math.columbia.edu/tag/03ET) in the Stacks Project.

**`Stacks.SheafOfModules.FlatSheafification.isFlat_sheafification`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean#L425).

> The sheaf associated to a flat presheaf of modules is flat over the associated sheaf of
> rings.

```lean
public lemma isFlat_sheafification
    {O : Cᵒᵖ ⥤ CommRingCat.{w}} {Osharp : Sheaf J CommRingCat.{w}}
    (a : O ⋙ forget₂ CommRingCat.{w} RingCat.{w} ⟶
      (Stacks.SheafOfModules.Tensor.ringSheaf Osharp).obj)
    [Presheaf.IsLocallyInjective J a]
    [Presheaf.IsLocallySurjective J a]
    (F : PresheafOfModules.{z} (O ⋙ forget₂ CommRingCat.{w} RingCat.{w}))
    (hF : AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat F) :
    AlgebraicGeometry.SheafOfModules.IsFlat
      ((PresheafOfModules.sheafification
        (R := Stacks.SheafOfModules.Tensor.ringSheaf Osharp) a).obj F)
```

## Tag 0GN1, a lemma

[Tag 0GN1](https://stacks.math.columbia.edu/tag/0GN1) in the Stacks Project.

**`Stacks.SheafOfModules.FlatSheafification.isFlat_sheafification_of_locally_objectwise_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean#L393).

> If a presheaf of modules is objectwise flat after passing to a covering of every object,
> then its associated sheaf is flat.

```lean
public lemma isFlat_sheafification_of_locally_objectwise_flat
    {O : Cᵒᵖ ⥤ CommRingCat.{w}} {Osharp : Sheaf J CommRingCat.{w}}
    (a : O ⋙ forget₂ CommRingCat.{w} RingCat.{w} ⟶
      (Stacks.SheafOfModules.Tensor.ringSheaf Osharp).obj)
    [Presheaf.IsLocallyInjective J a]
    [Presheaf.IsLocallySurjective J a]
    (F : PresheafOfModules.{z} (O ⋙ forget₂ CommRingCat.{w} RingCat.{w}))
    (hF : ∀ U : C,
      ∃ (I : Type (max u v)) (X : I → C) (f : ∀ i, X i ⟶ U),
        Sieve.ofArrows X f ∈ J U ∧
          ∀ i, Module.Flat (O.obj (Opposite.op (X i))) (F.obj (Opposite.op (X i)))) :
    AlgebraicGeometry.SheafOfModules.IsFlat
      ((PresheafOfModules.sheafification
        (R := Stacks.SheafOfModules.Tensor.ringSheaf Osharp)
        a).obj F)
```

## Tag 03EU, a lemma

[Tag 03EU](https://stacks.math.columbia.edu/tag/03EU) in the Stacks Project.

**`Stacks.isFlat_coproduct`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatColimits.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatColimits.lean#L236). The attribute's comment: “part (1), direct sums”.

> **Stacks 03EU, direct sums.** A coproduct of flat presheaves of modules is flat.

```lean
lemma isFlat_coproduct {O : Cᵒᵖ ⥤ CommRingCat.{w}} {ι : Type z}
    (F : ι → PresheafOfModules.{z} (ringPresheaf O))
    (hF : ∀ i, IsFlat (F i)) : IsFlat (∐ F)
```

**`Stacks.isFlat_colimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatColimits.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatColimits.lean#L446). The attribute's comment: “part (1), filtered colimits”.

> **Stacks 03EU, filtered colimits.** A filtered colimit of flat presheaves of modules is
> flat.

```lean
lemma isFlat_colimit {O : Cᵒᵖ ⥤ CommRingCat.{w}}
    {J : Type ju} [Category.{jv} J] [IsFiltered J] [UnivLE.{ju, z}]
    (F : J ⥤ PresheafOfModules.{z} (ringPresheaf O))
    (hF : ∀ j, IsFlat (F.obj j)) : IsFlat (colimit F)
```

**`Stacks.SheafOfModules.FlatColimits.isFlat_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean#L225). The attribute's comment: “part (2), filtered colimits”.

> **Stacks Project, Tag 03EU part (2), filtered colimits.** A filtered colimit of flat
> sheaves of modules is flat.

```lean
theorem isFlat_colimit {O : Sheaf J CommRingCat.{w}}
    {I : Type z} [Category.{z} I] [IsFiltered I]
    (F : I ⥤ _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∀ i, IsFlat (F.obj i)) :
    IsFlat (colimit F)
```

**`Stacks.SheafOfModules.FlatColimits.isFlat_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean#L241). The attribute's comment: “part (2), direct sums”.

> **Stacks Project, Tag 03EU part (2), direct sums.** An arbitrary direct sum of flat sheaves
> of modules is flat. An arbitrary coproduct is the filtered colimit of its finite subcoproducts,
> so this follows from the finite case `isFlat_coproduct_finite` and the filtered-colimit case
> `isFlat_colimit`.

```lean
theorem isFlat_coproduct {O : Sheaf J CommRingCat.{w}} {ι : Type z}
    (F : ι → _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∀ i, IsFlat (F i)) :
    IsFlat (∐ F)
```

**`Stacks.SheafOfModules.FlatCoproduct.isFlat_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCoproduct.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCoproduct.lean#L234).

> **A direct sum of flat sheaves of modules is flat.**

```lean
theorem isFlat_coproduct {O : Sheaf J CommRingCat.{max u v}} {ι : Type (max u v)}
    (F : ι → _root_.SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∀ i, IsFlat (F i)) :
    IsFlat (∐ F)
```

## Tag 0E8J, a lemma

[Tag 0E8J](https://stacks.math.columbia.edu/tag/0E8J) in the Stacks Project.

**`Stacks.SheafOfModules.FlatRestriction.OfEssentiallySmall.isFlat_over_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatRestrictionEssentiallySmall.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatRestrictionEssentiallySmall.lean#L108). The attribute's comment: “for a site essentially u-small, objects in Type c, morphisms and modules in u”.

> Restriction to an object of a ringed site whose objects form a type in a universe of their
> own, with morphisms, sections and modules in one universe `u` and the site essentially `u`-small,
> preserves flatness of sheaves of modules.

```lean
theorem isFlat_over_of_essentiallySmall
    (X : AlgebraicGeometry.RingedSite.{c, u, u}) [EssentiallySmall.{u} X.C] (U : X.C)
    [X.J.HasSheafCompose (forget₂ CommRingCat.{u} RingCat.{u})]
    [(X.J.over U).HasSheafCompose (forget₂ CommRingCat.{u} RingCat.{u})]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{u}] [HasWeakSheafify X.J AddCommGrpCat.{u}]
    [(X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify (X.J.over U) AddCommGrpCat.{u}]
    (F : SheafOfModules.{u} (ringSheaf X.O))
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat F) :
    AlgebraicGeometry.SheafOfModules.IsFlat (O := X.O.over U) (F.over U)
```

**`Stacks.SheafOfModules.FlatRestriction.isFlat_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Gate18b/FlatRestriction.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Gate18b/FlatRestriction.lean#L215). References: SGA 4 V (1.6.1).

> **Stacks Project, Tag 0E8J.** Restriction to an object of a ringed site preserves flatness
> of module sheaves.

```lean
public theorem isFlat_over
    (F : SheafOfModules.{u} (ringSheaf X.O))
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat F) :
    AlgebraicGeometry.SheafOfModules.IsFlat (O := X.O.over U) (F.over U)
```

**`Stacks.SheafOfModules.FlatRestriction.FreeModuleUniverse.isFlat_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Gate18b/FlatRestrictionFreeModuleUniverse.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Gate18b/FlatRestrictionFreeModuleUniverse.lean#L157). The attribute's comment: “objects in Type u, morphisms in v, ring sections in w, modules in max v a, and no smallness assumption on the site”. References: SGA 4 V (1.6.1).

> **Restriction preserves flatness, at a free module universe.** Restriction to an object of
> a ringed site preserves flatness of module sheaves, for objects of the site in `Type u`, morphisms
> in `v`, the structure sheaf in `w` and the modules in `max v a`, with no smallness assumption on
> the site.

```lean
public theorem isFlat_over
    (F : SheafOfModules.{max v a} (ringSheaf X.O))
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat F) :
    AlgebraicGeometry.SheafOfModules.IsFlat (O := X.O.over U) (F.over U)
```

## Tag 03EV, a lemma

[Tag 03EV](https://stacks.math.columbia.edu/tag/03EV) in the Stacks Project.

**`Stacks.Sites.OverModules.presheafExtensionUnit_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatSliceExtension.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatSliceExtension.lean#L47). The attribute's comment: “part (1)”.

> The extension from the slice category over `U` of the rank-one module is a flat presheaf of
> modules.

```lean
theorem presheafExtensionUnit_isFlat {C : Type u} [Category.{v} C]
    (O : Cᵒᵖ ⥤ CommRingCat.{max u v w}) (U : C) :
    AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat
      ((presheafModuleAdjunctionsOver (ringPresheaf O) U).extension.obj
        (PresheafOfModules.unit (overRingPresheaf (ringPresheaf O) U)))
```

**`Stacks.Sites.OverModules.sheafExtensionUnit_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatSliceExtension.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/FlatSliceExtension.lean#L72). The attribute's comment: “part (2)”.

> The extension by zero from the localized site of the structure sheaf is a flat sheaf of
> modules.

```lean
theorem sheafExtensionUnit_isFlat {C : Type u} [Category.{u} C]
    (J : GrothendieckTopology C)
    [J.HasSheafCompose (forget₂ CommRingCat.{u} RingCat.{u})]
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify J AddCommGrpCat.{u}]
    (O : Sheaf J CommRingCat.{u}) (U : C) :
    AlgebraicGeometry.SheafOfModules.IsFlat
      ((SheafOfModules.pullback.{u} (F := Over.forget U)
        (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf O).over U) :
          ((Stacks.SheafOfModules.Tensor.ringSheaf O).over U) ⟶
            ((Stacks.SheafOfModules.Tensor.ringSheaf O).over U))).obj
        (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf O).over U)))
```

## Tag 03EW, a lemma

[Tag 03EW](https://stacks.math.columbia.edu/tag/03EW) in the Stacks Project.

**`Stacks.SimplicialModules.exists_epi_isFlat_simplicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialFlatResolution.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialFlatResolution.lean#L171). The attribute's comment: “part (4) at the simplicial site Δ × C of 09D0”.

> **[Stacks, Tag 03EW] part (4) at the simplicial site of [Stacks, Tag 09D0].** Every
> simplicial `A_•`-module — that is, every sheaf of modules over the sheaf of rings on `Δ × C`
> associated to a simplicial sheaf of commutative rings `A_•`, as in [Stacks, Tag 09D1] — receives
> an epimorphism from a flat one.

```lean
theorem exists_epi_isFlat_simplicial
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} (simplicialCommRingSheaf J A))) :
    ∃ (N : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} (simplicialCommRingSheaf J A)))
      (p : N ⟶ M),
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
        (O := simplicialCommRingSheaf J A) N ∧ Epi p
```

**`SheafOfModules.exists_epi_from_coproduct_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroGenerators.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroGenerators.lean#L308). The attribute's comment: “part (3)”.

> **Every sheaf of `O`-modules is a quotient of a direct sum of extensions by zero
> `j_{U!}O_U` of the structure sheaves of slices.** The sum is indexed by the sections of `M`,
> the summand attached to a section over `U` being `j_{U!}O_U`, and the map sends the
> tautological generating section of that summand to the section.

```lean
theorem exists_epi_from_coproduct_extensionByZero (M : SheafOfModules.{u} O) :
    ∃ (ι : Type u) (U : ι → C)
      (π : (∐ fun i ↦ (extensionByZero.{u, u, u, u} O (U i)).obj (unit (O.over (U i)))) ⟶ M),
        Epi π
```

**`Stacks.SheafOfModules.FlatResolution.exists_epi_from_coproduct_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/PresheafFlatQuotient.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/PresheafFlatQuotient.lean#L199). The attribute's comment: “part (1)”.

> **Stacks 03EW, part (1).** Every presheaf of modules is a quotient of a direct sum of
> extensions from slice categories of the rank-one module. The sum is indexed by all pairs
> `(U, s)` with `s` a section of `F` over `U`, and the component at `(U, s)` is the morphism
> adjoint to `s`.

```lean
theorem exists_epi_from_coproduct_extension (O : Cᵒᵖ ⥤ RingCat.{w})
    (F : _root_.PresheafOfModules.{max u v w z} O) :
    ∃ (ι : Type (max u v w z)) (U : ι → C),
      ∃ (p : (∐ fun i : ι =>
        ((presheafModuleAdjunctionsOver.{v, u, w, max w z} O (U i)).extension.obj
          (uliftUnit.{max u v w z} (overRingPresheaf O (U i))))) ⟶ F), Epi p
```

**`Stacks.SheafOfModules.FlatResolution.exists_epi_from_flat_presheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/PresheafFlatQuotient.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/PresheafFlatQuotient.lean#L249). The attribute's comment: “part (2)”.

> **Stacks 03EW, part (2).** Every presheaf of modules over a presheaf of commutative rings
> is a quotient of a flat presheaf of modules: the direct sum produced by part (1) is a direct
> sum of slice extensions of the rank-one module, each of which is flat.

```lean
theorem exists_epi_from_flat_presheaf (O : Cᵒᵖ ⥤ CommRingCat.{w})
    (F : _root_.PresheafOfModules.{max u v w z} (ringPresheaf O)) :
    ∃ P : _root_.PresheafOfModules.{max u v w z} (ringPresheaf O),
      AlgebraicGeometry.SheafOfModules.PresheafOfModules.IsFlat P ∧
        ∃ (p : P ⟶ F), Epi p
```

**`Stacks.SheafOfModules.FlatResolution.exists_epi_from_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/SheafFlatQuotient.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/SheafFlatQuotient.lean#L60). The attribute's comment: “part (4)”.

> **Stacks 03EW, part (4).** Every sheaf of modules over a sheaf of commutative rings is a
> quotient of a flat sheaf of modules.

```lean
theorem exists_epi_from_flat (O : Sheaf J CommRingCat.{w})
    (F : _root_.SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) :
    ∃ P : _root_.SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf O),
      AlgebraicGeometry.SheafOfModules.IsFlat P ∧ ∃ (p : P ⟶ F), Epi p
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.FlatCover.exists_epi_from_isFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCoverTensorExactness.lean#L158), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/TensorSheafSections.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/TensorSheafSections.lean#L153) (StacksFrontier): “part (4): every sheaf of modules is a quotient of a flat one”.

## Tag 03EX, a lemma

[Tag 03EX](https://stacks.math.columbia.edu/tag/03EX) in the Stacks Project.

**`Stacks.sheafTensorRight_shortExact_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafFlatCover.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafFlatCover.lean#L792). The attribute's comment: “sheaf\_tensor\_exactness”. References: SGA 1 IV (1.1), “(i)”; SGA 4 XVII (4.1.1), “(ii), f = id”.

> **Stacks Project, Tag 03EX, sheaf case.** If the final term of a short exact sequence of
> sheaves of modules is flat, then tensoring the sequence with any sheaf of modules gives a
> short exact sequence of sheaves of modules.

```lean
theorem sheafTensorRight_shortExact_of_flat
    (S : ShortComplex (SheafOfModules.{max t w} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (G : SheafOfModules.{max t w} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hS : S.ShortExact) (hflat : SheafOfModules.IsFlat S.X₃) :
    ∃ h : ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max t w, max t w} O).flip.obj
          G).map S.f ≫
        ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max t w, max t w} O).flip.obj
          G).map S.g = 0,
      (ShortComplex.mk
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max t w, max t w} O).flip.obj
          G).map S.f)
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max t w, max t w} O).flip.obj
          G).map S.g) h).ShortExact
```

**`Stacks.SheafOfModules.shortExact_map_sheafTensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/TensorOfAShortExactSequence.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/TensorOfAShortExactSequence.lean#L166). The attribute's comment: “part (2)”. References: SGA 1 IV (1.1), “(i)”; SGA 4 XVII (4.1.1), “(ii), f = id”.

> Tensoring a short exact sequence of sheaves of modules whose third term is flat with any sheaf
> of modules gives a short exact sequence.

```lean
theorem shortExact_map_sheafTensorObj
    (S : ShortComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hS : S.ShortExact)
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) S.X₃)
    (M : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (S.map ((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj M)).ShortExact
```

**`Stacks.SheafOfModules.FlatResolution.Presheaf.shortExact_map_tensorRight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean#L243). The attribute's comment: “part (1)”. References: EGA IV (2.1.10), “special case”; SGA 1 IV (1.1), “more general”; SGA 4 XVII (4.1.1), “(ii), special case”.

> **Stacks 03EX, part (1).** If the third term of a short exact sequence of presheaves of
> modules is flat, then tensoring the sequence with an arbitrary presheaf of modules gives a
> short exact sequence.
>
> The proof is the source's.  Right exactness of the objectwise tensor product gives exactness in
> the middle and an epimorphism on the right, so the content is injectivity on the left.  For
> that, resolve the second tensor factor `G` by a flat presheaf of modules `P` (Stacks 03EW part
> (2)), let `K` be the kernel of `P ⟶ G`, and chase the 3-by-3 diagram whose columns are the
> sequence tensored with `K`, `P` and `G` and whose rows are `K ⟶ P ⟶ G` tensored with the three
> terms of the sequence: the first column and the second row are exact because tensoring is right
> exact in each variable, the second column is left exact because `P` is flat, and the bottom row
> is left exact because the third term of the sequence is flat.

```lean
theorem shortExact_map_tensorRight
    {S : ShortComplex (_root_.PresheafOfModules.{max u v w z} (ringPresheaf O))}
    (hS : S.ShortExact) (h₃ : PresheafOfModules.IsFlat S.X₃)
    (G : _root_.PresheafOfModules.{max u v w z} (ringPresheaf O)) :
    (S.map (PresheafOfModules.tensorRight G)).ShortExact
```

## Tag 03EY, a lemma

[Tag 03EY](https://stacks.math.columbia.edu/tag/03EY) in the Stacks Project.

**`Stacks.SheafOfModules.FlatTwoOutOfThree.isFlat_middle_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean#L170). The attribute's comment: “sheaves, part (1)”.

> **Tag 03EY, part (1) for sheaves.** In a short exact sequence of sheaves of modules whose
> outer terms are flat, the middle term is flat.

```lean
theorem isFlat_middle_of_shortExact
    (S : ShortComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)))
    (hS : S.ShortExact)
    (h₁ : AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₁)
    (h₃ : AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₃) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₂
```

**`Stacks.SheafOfModules.FlatTwoOutOfThree.isFlat_left_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean#L188). The attribute's comment: “sheaves, part (2)”. References: SGA 4 XVII (4.1.1), “(i)”.

> **Tag 03EY, part (2) for sheaves.** In a short exact sequence of sheaves of modules whose
> middle and right terms are flat, the left term is flat.

```lean
theorem isFlat_left_of_shortExact
    (S : ShortComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)))
    (hS : S.ShortExact)
    (h₂ : AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₂)
    (h₃ : AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₃) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) S.X₁
```

**`Stacks.SheafOfModules.FlatTwoOutOfThree.Presheaf.isFlat_middle_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean#L350). The attribute's comment: “presheaves, part (1)”.

> **Tag 03EY, part (1) for presheaves.** In a short exact sequence of presheaves of modules
> whose outer terms are flat, the middle term is flat.

```lean
theorem isFlat_middle_of_shortExact
    (S : ShortComplex (_root_.PresheafOfModules.{u} (ringPresheaf O)))
    (hS : S.ShortExact)
    (h₁ : PresheafOfModules.IsFlat S.X₁)
    (h₃ : PresheafOfModules.IsFlat S.X₃) :
    PresheafOfModules.IsFlat S.X₂
```

**`Stacks.SheafOfModules.FlatTwoOutOfThree.Presheaf.isFlat_left_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTwoOutOfThree.lean#L367). The attribute's comment: “presheaves, part (2)”. References: SGA 4 XVII (4.1.1), “(i), presheaves”.

> **Tag 03EY, part (2) for presheaves.** In a short exact sequence of presheaves of modules
> whose middle and right terms are flat, the left term is flat.

```lean
theorem isFlat_left_of_shortExact
    (S : ShortComplex (_root_.PresheafOfModules.{u} (ringPresheaf O)))
    (hS : S.ShortExact)
    (h₂ : PresheafOfModules.IsFlat S.X₂)
    (h₃ : PresheafOfModules.IsFlat S.X₃) :
    PresheafOfModules.IsFlat S.X₁
```

## Tag 03EZ, a lemma

[Tag 03EZ](https://stacks.math.columbia.edu/tag/03EZ) in the Stacks Project.

**`Stacks.SheafOfModules.FlatResolution.acyclic_map_sheafTensorRight_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean#L140). The attribute's comment: “sheaves”. References: EGA IV (2.1.10), “Absolute case f = id”.

> **Stacks 03EZ, sheaf case.** An exact `ℕ`-indexed complex of sheaves of modules all of
> whose terms are flat stays exact after tensoring with an arbitrary sheaf of modules.
>
> This is also **Stacks 05NL**, the same statement for a ringed space: a ringed space is the
> ringed site of its lattice of opens, its `O_X`-modules are the sheaves of modules over the
> structure ring sheaf of that site, and the tensor product is `sheafTensorRight`.  The
> site-level statement is recorded against the ringed-space tag for the same reason that the
> site-level flatness of Stacks 03ER(3) is recorded against Stacks 05ND in
> `StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean`.

```lean
theorem acyclic_map_sheafTensorRight_of_isFlat
    (K : ChainComplex
      (_root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℕ)
    (hK : K.Acyclic)
    (hflat : ∀ i, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (K.X i))
    (G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) :
    ((Functor.mapHomologicalComplex
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} R).flip.obj G)
      (ComplexShape.down ℕ)).obj K).Acyclic
```

**`Stacks.SheafOfModules.FlatResolution.Presheaf.acyclic_map_tensorRight_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean#L284). The attribute's comment: “presheaves”. References: EGA IV (2.1.10), “special case”.

> **Stacks 03EZ, presheaf case.** An exact `ℕ`-indexed complex of presheaves of modules all
> of whose terms are flat stays exact after tensoring with an arbitrary presheaf of modules.

```lean
theorem acyclic_map_tensorRight_of_isFlat
    (K : ChainComplex (_root_.PresheafOfModules.{u} (ringPresheaf O)) ℕ)
    (hK : K.Acyclic)
    (hflat : ∀ i, PresheafOfModules.IsFlat (K.X i))
    (G : _root_.PresheafOfModules.{u} (ringPresheaf O)) :
    (((PresheafOfModules.tensorRight G).mapHomologicalComplex
      (ComplexShape.down ℕ)).obj K).Acyclic
```

## Tag 0G6Q, a lemma

[Tag 0G6Q](https://stacks.math.columbia.edu/tag/0G6Q) in the Stacks Project.

**`Stacks.SheafOfModules.FlatTensor.isFlat_tensor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Gate18/FlatTensorProduct.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Gate18/FlatTensorProduct.lean#L473).

> **Stacks Project, Tag 0G6Q.** The tensor product of two flat sheaves of
> modules is flat.

```lean
public lemma isFlat_tensor {O : Sheaf J CommRingCat.{w}}
    [J.WEqualsLocallyBijective AddCommGrpCat.{w}] [HasWeakSheafify J AddCommGrpCat.{w}]
    (G F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hG : AlgebraicGeometry.SheafOfModules.IsFlat G)
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat F) :
    AlgebraicGeometry.SheafOfModules.IsFlat
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, z, z} O).flip.obj F).obj G)
```

## Tag 05V4, a lemma

[Tag 05V4](https://stacks.math.columbia.edu/tag/05V4) in the Stacks Project.

**`Stacks.FlatChangeOfRings.isFlat_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatChangeOfRings.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatChangeOfRings.lean#L373).

> **Stacks Project, Tag 05V4.** Extension of scalars along a morphism of sheaves of
> commutative rings takes a flat sheaf of modules to a flat sheaf of modules.

```lean
theorem isFlat_extendScalars (hG : SheafOfModules.IsFlat G) :
    SheafOfModules.IsFlat ((extendScalars f).obj G)
```

**`Stacks.FlatChangeOfRings.isFlat_pullback_ringSheafMapId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SiteUpSheafificationPullback.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SiteUpSheafificationPullback.lean#L320). The attribute's comment: “read for `SheafOfModules.pullback` along the identity functor of the site”.

> **Stacks 05V4 for `SheafOfModules.pullback`.**  Pullback along a change of rings on a fixed
> site takes a flat sheaf of modules to a flat sheaf of modules.

```lean
theorem isFlat_pullback_ringSheafMapId
    (G : _root_.SheafOfModules.{w} (commRingSheafToRingSheaf O₁))
    (hG : SheafOfModules.IsFlat G) :
    SheafOfModules.IsFlat
      ((_root_.SheafOfModules.pullback.{w} (structureMap (ringSheafMap f))).obj G)
```

## Tag 08FC, a lemma

[Tag 08FC](https://stacks.math.columbia.edu/tag/08FC) in the Stacks Project.

**`Stacks.SheafOfModules.isFlat_iff_hasLocalSingleRelationFactorizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCriterionConverse.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCriterionConverse.lean#L458). The attribute's comment: “parts (1) and (2)”.

> **Stacks 08FC, parts (1) and (2).**  A sheaf of modules on a ringed site is flat exactly
> when every single finite relation among its sections locally factors through a finite free
> module by a matrix annihilating that relation.

```lean
theorem isFlat_iff_hasLocalSingleRelationFactorizations
    (F : _root_.SheafOfModules.{max v w} (commRingSheafToRingSheaf O)) :
    IsFlat F ↔ HasLocalSingleRelationFactorizations O F
```

**`Stacks.SheafOfModules.hasLocalSingleRelationFactorizations_of_isFlat_freeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquivalence.lean, line 1036](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquivalence.lean#L1036). The attribute's comment: “part (1) implies part (2)”. References: SGA 4 V (8.2.11), “(a), special case”.

> A flat sheaf of modules satisfies the single-relation form of the local equational criterion:
> every relation `∑ᵢ aᵢ • sᵢ = 0` among its sections over an object `U` admits, on a covering sieve
> of `U`, a factorisation of the restricted sections through a finite free module by a matrix
> annihilating the restricted relation. The universe `w` of the sections of the structure sheaf is
> independent of the universes of the site.

```lean
theorem hasLocalSingleRelationFactorizations_of_isFlat_freeUniverse
    {F : _root_.SheafOfModules.{w} (commRingSheafToRingSheaf O)} (hF : IsFlat F) :
    HasLocalSingleRelationFactorizations O F
```

**`Stacks.SheafOfModules.isFlat_of_hasLocalSingleRelationFactorizations_freeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquivalenceConverse.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquivalenceConverse.lean#L280). The attribute's comment: “part (2) implies part (1)”.

> **Stacks 08FC, (2) implies (1).** A sheaf of modules satisfying the single-relation form of
> the local equational criterion is flat: every relation `∑ᵢ aᵢ • sᵢ = 0` among its sections
> factoring locally through a finite free module annihilating the relation forces the tensor
> endofunctor `- ⊗ F` on sheaves of modules to be exact.
>
> This is the universe-general form of
> `Stacks.SheafOfModules.isFlat_of_hasLocalSingleRelationFactorizations`, which proves the same
> implication for a structure sheaf `O : Sheaf J CommRingCat.{max v w}` on a site with morphisms
> in `Type v`. Here the section universe `w` is independent of `u` and `v`, and `HasWeakSheafify`
> is assumed in place of `HasSheafify`. A ringed site whose sections are unrelated to its
> morphisms cannot be fed to the `max v w` form, because `w =?= max v u` is not a solvable
> universe constraint. The proof sheafifies the local injectivity of the presheaf-level tensor map
> through `Stacks.SheafOfModules.mono_shf_map_of_isLocallyInjective`.
>
> Together with `Stacks.SheafOfModules.hasLocalSingleRelationFactorizations_of_isFlat_freeUniverse`
> this gives the equivalence of parts (1) and (2) of the source at those universes.

```lean
theorem isFlat_of_hasLocalSingleRelationFactorizations_freeUniverse
    (F : _root_.SheafOfModules.{w} (commRingSheafToRingSheaf O))
    (hF : HasLocalSingleRelationFactorizations O F) : IsFlat F
```

**`Stacks.SheafOfModules.hasLocalSingleRelationFactorizations_iff_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatRelations.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatRelations.lean#L280). The attribute's comment: “parts (2) and (3)”.

> For a sheaf of modules on a ringed site, the single-relation and the finite-matrix forms of
> the local equational criterion for flatness are equivalent.

```lean
theorem hasLocalSingleRelationFactorizations_iff_finite
    (O : Sheaf J CommRingCat.{w}) (F : _root_.SheafOfModules.{w} (commRingSheafToRingSheaf O)) :
    HasLocalSingleRelationFactorizations O F ↔ HasLocalFiniteRelationFactorizations O F
```

## Tag 08M4, a lemma

[Tag 08M4](https://stacks.math.columbia.edu/tag/08M4) in the Stacks Project.

**`Stacks.SheafOfModules.FlatSquareZero.isFlat_iff_reduction_isFlat_and_multiplication_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSquareZeroThickening.lean, line 2709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSquareZeroThickening.lean#L2709).

> Flatness over a square-zero thickening is equivalent to flatness of the reduction and
> injectivity of the canonical multiplication map from the kernel tensored with the reduction.
>
> Here `i` identifies `I` with the kernel of `f`, `nu` is multiplication
> `I ⊗[O'] F' ⟶ F'`, and `q` exhibits `F` as its cokernel.  The last
> displayed formula identifies `mu` with the canonical map
> `I ⊗[O] F ⟶ F'`.

```lean
public theorem isFlat_iff_reduction_isFlat_and_multiplication_mono
    {O' O : Sheaf J CommRingCat.{w}} (f : O' ⟶ O)
    (hf : Presheaf.IsLocallySurjective J f.hom)
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (F' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O'))
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (i : (SheafOfModules.restrictScalars (ringMap f)).obj I ⟶
      SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf O'))
    (hi_zero : ∀ (U : Cᵒᵖ) (a : I.val.obj U),
      f.hom.app U (show O'.obj.obj U from i.val.app U a) = 0)
    (hi_univ : ∀ (U : Cᵒᵖ) (x : O'.obj.obj U), f.hom.app U x = 0 →
      ∃! a : I.val.obj U, (show O'.obj.obj U from i.val.app U a) = x)
    (hsq : ∀ (U : Cᵒᵖ) (a b : I.val.obj U),
      (show O'.obj.obj U from i.val.app U a) *
        (show O'.obj.obj U from i.val.app U b) = 0)
    (nu : (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} O').flip.obj F')).obj
        ((SheafOfModules.restrictScalars (ringMap f)).obj I) ⟶ F')
    (hnu : ∀ (U : Cᵒᵖ) (a : I.val.obj U) (x : F'.val.obj U),
      nu.val.app U
          (((PresheafOfModules.sheafificationAdjunction.{w, v, w, u} (R :=
              Stacks.SheafOfModules.Tensor.ringSheaf
              O')
        (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf O').obj)).unit.app
      (PresheafOfModules.tensorObj ((SheafOfModules.restrictScalars (ringMap f)).obj I).val
          F'.val)).app U
              (a ⊗ₜ[O'.obj.obj U] x)) =
        (show (Stacks.SheafOfModules.Tensor.ringSheaf O').obj.obj U from
          i.val.app U a) • x)
    (q : F' ⟶ (SheafOfModules.restrictScalars (ringMap f)).obj F)
    (hnuq : nu ≫ q = 0)
    (hq : IsColimit (CokernelCofork.ofπ q hnuq))
    (mu : (SheafOfModules.restrictScalars (ringMap f)).obj
        ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} O).flip.obj F)).obj I) ⟶ F')
    (hmu : ∀ (U : Cᵒᵖ) (a : I.val.obj U) (x : F'.val.obj U),
      mu.val.app U
          (((PresheafOfModules.sheafificationAdjunction.{w, v, w, u} (R :=
              Stacks.SheafOfModules.Tensor.ringSheaf
              O)
        (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf O).obj)).unit.app
      (PresheafOfModules.tensorObj I.val F.val)).app U
            (a ⊗ₜ[O.obj.obj U] q.val.app U x)) =
        (show (Stacks.SheafOfModules.Tensor.ringSheaf O').obj.obj U from
          i.val.app U a) • x) :
    AlgebraicGeometry.SheafOfModules.IsFlat F' ↔
      (AlgebraicGeometry.SheafOfModules.IsFlat F ∧ Mono mu)
```

## Tag 0GLY, a lemma

[Tag 0GLY](https://stacks.math.columbia.edu/tag/0GLY) in the Stacks Project.

**`Stacks.Sheaves.FlatNeighbourhood.isIso_tensorUnitMap_of_pow_smul_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatNeighbourhoodTensorUnit.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatNeighbourhoodTensorUnit.lean#L724).

> **Stacks Project, Tag 0GLY.** If a flat map of ring sheaves is an
> isomorphism modulo an ideal `I`, then extension of scalars is an isomorphism on
> every module annihilated by a power of `I`.

```lean
lemma isIso_tensorUnitMap_of_pow_smul_eq_zero
    {O O' : Sheaf J CommRingCat.{w}} (f : O ⟶ O')
    (hf : IsFlatMap f)
    {I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O)}
    (i : I ⟶ RingModule O) [Mono i]
    (hquot : ∃ q : cokernel i ⟶
        cokernel (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} O).flip.obj
            (RestrictedRingModule f)).map i),
      IsIso q ∧ cokernel.π i ≫ q = (tensorUnitMap f (RingModule O)).val ≫
        cokernel.π (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} O).flip.obj
            (RestrictedRingModule f)).map i))
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∃ n : ℕ, ∀ (X : Cᵒᵖ) (a : Fin n → I.val.obj X) (x : F.val.obj X),
      ((F.val.obj X).smul
        (show (Stacks.SheafOfModules.Tensor.ringSheaf O).obj.obj X from
          (Finset.univ.prod (fun k ↦ show O.obj.obj X from (i.val.app X) (a k)) :
            O.obj.obj X))).asHom x = 0) :
    IsIso (tensorUnitMap f F).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.28, Tag 03EQ](https://stacks.math.columbia.edu/tag/03EQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
