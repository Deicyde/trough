---
declaration: section
origin: cited
lean: Stacks.ConstantSheaf.IsLocallyConstant, Stacks.ConstantSheaf.IsFiniteLocallyConstant, CategoryTheory.Sheaf.IsConstant, MorphismOfTopoi.isConstant_inverseImage, Stacks.ConstantSheaf.isLocallyConstant_sheafPullback, Stacks.ConstantSheaf.isFiniteLocallyConstant_sheafPullback_of_coverPreserving, MorphismOfTopoi.isConstant_abelianInverseImage, MorphismOfTopoi.isFiniteLocallyConstant_abelianInverseImage_of_smallSites
statement: formalized
proof: formalized
---

# 18.43 Locally constant sheaves

Section 18.43 of the Stacks Project, [Tag 093P](https://stacks.math.columbia.edu/tag/093P). 6 tags here are carried by 34 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 093Q, a definition

[Tag 093Q](https://stacks.math.columbia.edu/tag/093Q) in the Stacks Project.

**`Stacks.ConstantSheaf.IsLocallyConstant`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L73). The attribute's comment: “part (2)”. References: EGA 0 (3.6.1), “locally simple”; SGA 3 X (9.2.1), “(2), (4)”; SGA 4 IX (2.0), “locally constant”.

> **Stacks 093Q (2).** A sheaf is locally constant if every object of the site has a covering
> on each member of which its restriction is a constant sheaf.

```lean
class IsLocallyConstant [∀ U : C, HasWeakSheafify (J.over U) D] (F : Sheaf J D) : Prop
```

**`Stacks.ConstantSheaf.IsFiniteLocallyConstant`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L86). The attribute's comment: “part (3)”.

> **Stacks 093Q (3).** A sheaf with values in a concrete category is finite locally constant
> if every object of the site has a covering on each member of which it is a constant sheaf with
> finite underlying value. For `Type` and `Grp`, this is respectively the source's notion for
> sheaves of sets and sheaves of groups.

```lean
class IsFiniteLocallyConstant {FD : D → D → Type*} {CD : D → Type w}
    [∀ X Y, FunLike (FD X Y) (CD X) (CD Y)] [ConcreteCategory.{w} D FD]
    [∀ U : C, HasWeakSheafify (J.over U) D] (F : Sheaf J D) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.IsConstant`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.IsConstant#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L59) (StacksFrontier): “part (1): a constant sheaf is an object in the essential image of the constant sheaf functor”. References: EGA 0 (3.6.1); SGA 4 IV (2.7.5); SGA 4 IV (4.3.4); SGA 4 IX (2.0).

## Tag 093R, a lemma

[Tag 093R](https://stacks.math.columbia.edu/tag/093R) in the Stacks Project.

**`MorphismOfTopoi.isConstant_inverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/ConstantInverseImage.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/ConstantInverseImage.lean#L198). The attribute's comment: “constant sheaves of sets, for an arbitrary morphism of topoi”.

> **Stacks 093R, the constant case.** The inverse image of a constant sheaf of sets along a
> morphism of topoi is constant.

```lean
public lemma isConstant_inverseImage (G : Sheaf K (Type w)) [Sheaf.IsConstant K G] :
    Sheaf.IsConstant J (f.inverseImage.obj G)
```

**`Stacks.ConstantSheaf.isLocallyConstant_sheafPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/InverseImageFiniteLocallyConstant.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/InverseImageFiniteLocallyConstant.lean#L420). The attribute's comment: “locally constant sheaves with arbitrary coefficients, for the inverse image along a morphism of sites”.

> **Tag 093R, for a morphism of sites.** The inverse image of a locally constant sheaf along a
> continuous functor of sites is locally constant, for arbitrary coefficients.
>
> The trivializing covering is taken over the final object of `C`, whose image is final in `D`
> because `G` is left exact; no object with a final image has to be supplied.
>
> The source states the tag for an arbitrary morphism of topoi, whose inverse image need not be
> induced by a functor between the two sites; the attribute is qualified accordingly.

```lean
public lemma isLocallyConstant_sheafPullback (F : Sheaf J A) [hF : IsLocallyConstant J F] :
    IsLocallyConstant K ((G.sheafPullback A J K).obj F)
```

**`Stacks.ConstantSheaf.isFiniteLocallyConstant_sheafPullback_of_coverPreserving`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/InverseImageFiniteLocallyConstant.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/InverseImageFiniteLocallyConstant.lean#L450). The attribute's comment: “finite locally constant sheaves with arbitrary concrete coefficients, for the inverse image along a morphism of sites”.

> **Tag 093R.** The inverse image of a finite locally constant sheaf along a continuous functor of
> sites is finite locally constant, for arbitrary concrete coefficients. In particular this holds for
> sheaves of abelian groups, which is the case Tag 03RZ (2) needs.
>
> One trivializing covering `{X i ⟶ ⊤_C}` is enough, by
> `Stacks.ConstantSheaf.isFiniteLocallyConstant_of_cover`. Its image under `G` covers `G.obj ⊤_C`,
> which is final in `D` because `G` is left exact, and on a member the restriction of `G^* F` is
> constant with the same finite value, by
> `Stacks.ConstantSheaf.constantIsoOverPullbackSheafPullback`.

```lean
public lemma isFiniteLocallyConstant_sheafPullback_of_coverPreserving (F : Sheaf J A)
    [hF : IsFiniteLocallyConstant (FD := FA) (CD := CA) J F] :
    IsFiniteLocallyConstant (FD := FA) (CD := CA) K ((G.sheafPullback A J K).obj F)
```

**`MorphismOfTopoi.isConstant_abelianInverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianConstantInverseImage.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianConstantInverseImage.lean#L213). The attribute's comment: “constant sheaves of abelian groups, for an arbitrary morphism of topoi”.

> **Stacks 093R, the constant abelian case.** The inverse image of a constant sheaf of abelian
> groups along a morphism of topoi is constant.

```lean
public lemma isConstant_abelianInverseImage (G : Sheaf K AddCommGrpCat.{w}) [Sheaf.IsConstant K G] :
    Sheaf.IsConstant J ((CategoryTheory.Sites.abelianInverseImage f).obj G)
```

**`MorphismOfTopoi.isFiniteLocallyConstant_abelianInverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianInverseImageMorphismOfTopoi.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianInverseImageMorphismOfTopoi.lean#L88). The attribute's comment: “finite locally constant sheaves of abelian groups, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R, the finite abelian case.** The inverse image of a finite locally constant sheaf
> of abelian groups along an arbitrary morphism of topoi between the topoi of sheaves of sets on
> two small sites is finite locally constant.
>
> No functor between the two sites is assumed. Finite local constancy of an abelian sheaf is a
> property of its underlying sheaf of sets by
> `Stacks.ConstantSheaf.isFiniteLocallyConstant_iff_forget`, the underlying sheaf of sets of the
> abelian inverse image is the geometric inverse image of the underlying sheaf of sets, and the
> latter preserves finite local constancy by
> `MorphismOfTopoi.isFiniteLocallyConstant_inverseImage_of_smallSites`.

```lean
public lemma isFiniteLocallyConstant_abelianInverseImage_of_smallSites
    [∀ U : C, HasWeakSheafify (J.over U) AddCommGrpCat.{w}]
    [∀ V : D, HasWeakSheafify (K.over V) AddCommGrpCat.{w}]
    (G : Sheaf K AddCommGrpCat.{w}) [hG : IsFiniteLocallyConstant K G] :
    IsFiniteLocallyConstant J ((CategoryTheory.Sites.abelianInverseImage f).obj G)
```

**`MorphismOfTopoi.isLocallyConstant_abelianInverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianLocallyConstantInverseImage.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianLocallyConstantInverseImage.lean#L215). The attribute's comment: “locally constant sheaves of abelian groups, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R for locally constant sheaves of abelian groups.** The inverse image of a locally
> constant sheaf of abelian groups along an arbitrary morphism of topoi between the topoi of
> sheaves of sets on two small sites is locally constant.
>
> No functor between the two sites, no final object in either, and no finiteness of the local
> values is assumed. The covering of an object `U` of `C` is the one
> `Stacks.Topos.exists_cover_inverseImage_sections` produces for the family of sheaves represented
> by the objects of `D` over which `G` is trivialized as an abelian sheaf, and on a member `V` of
> it the section it carries trivializes the abelian inverse image over `V`, with the same
> trivializing group, by
> `MorphismOfTopoi.abelianConstantIsoOverPullbackInverseImageOfSection`.

```lean
public lemma isLocallyConstant_abelianInverseImage_of_smallSites
    (G : Sheaf K AddCommGrpCat.{w}) [hG : IsLocallyConstant K G] :
    IsLocallyConstant J ((CategoryTheory.Sites.abelianInverseImage f).obj G)
```

**`MorphismOfTopoi.isLocallyConstant_grpInverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/GrpLocallyConstantInverseImage.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/GrpLocallyConstantInverseImage.lean#L211). The attribute's comment: “locally constant sheaves of groups, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R for locally constant sheaves of groups.** The inverse image of a locally constant
> sheaf of groups along an arbitrary morphism of topoi between the topoi of sheaves of sets on two
> small sites is locally constant.
>
> No functor between the two sites, no final object in either, no commutativity of the local
> values and no finiteness of them is assumed. The covering of an object `U` of `C` is the one
> `Stacks.Topos.exists_cover_inverseImage_sections` produces for the family of sheaves represented
> by the objects of `D` over which `G` is trivialized as a sheaf of groups, and on a member `V` of
> it the section it carries trivializes the inverse image over `V`, with the same trivializing
> group, by `MorphismOfTopoi.grpConstantIsoOverPullbackInverseImageOfSection`.

```lean
public lemma isLocallyConstant_grpInverseImage_of_smallSites
    (G : Sheaf K GrpCat.{w}) [hG : IsLocallyConstant K G] :
    IsLocallyConstant J ((CategoryTheory.Sites.grpInverseImage f).obj G)
```

**`MorphismOfTopoi.isLocallyConstant_moduleInverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/ModuleLocallyConstantInverseImage.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/ModuleLocallyConstantInverseImage.lean#L435). The attribute's comment: “locally constant sheaves of modules over a fixed ring, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R for locally constant sheaves of modules over a fixed ring.** The inverse image of a
> locally constant sheaf of `Λ`-modules along an arbitrary morphism of topoi between the topoi of
> sheaves of sets on two small sites is locally constant.
>
> No functor between the two sites, no final object in either, no commutativity of `Λ` and no
> finiteness of the local values is assumed. The covering of an object `U` of `C` is the one
> `Stacks.Topos.exists_cover_inverseImage_sections` produces for the family of sheaves represented
> by the objects of `D` over which `G` is trivialized as a sheaf of `Λ`-modules, and on a member `V`
> of it the section it carries trivializes the inverse image over `V`, with the same trivializing
> module, by `MorphismOfTopoi.moduleConstantIsoOverPullbackInverseImageOfSection`.

```lean
public lemma isLocallyConstant_moduleInverseImage_of_smallSites (Λ : Type r) [Ring Λ]
    (G : Sheaf K (ModuleCat.{w} Λ)) [hG : IsLocallyConstant K G] :
    IsLocallyConstant J ((CategoryTheory.Sites.moduleInverseImage f Λ).obj G)
```

**`MorphismOfTopoi.isLocallyConstant_inverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiPullback.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiPullback.lean#L168). The attribute's comment: “locally constant sheaves of sets, for a morphism of topoi equipped with a localization datum along a functor of sites”.

> **Tag 093R.** The inverse image of a locally constant sheaf of sets along a morphism of
> topoi which is equipped with a localization datum is locally constant.
>
> A trivializing covering of the distinguished object of the target site is carried forward by
> cover preservation to a covering of a final object of the source site, which is enough for
> local constancy there (`Stacks.ConstantSheaf.isLocallyConstant_of_cover`), and on a member the
> restriction of `f⁻¹G` is constant by
> `MorphismOfTopoi.LocalizationDatum.isConstant_overPullback_inverseImage`.

```lean
public lemma isLocallyConstant_inverseImage (d : LocalizationDatum f) (G : Sheaf K (Type w))
    [hG : IsLocallyConstant K G] : IsLocallyConstant J (f.inverseImage.obj G)
```

**`MorphismOfTopoi.isFiniteLocallyConstant_inverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiPullback.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiPullback.lean#L184). The attribute's comment: “finite locally constant sheaves of sets, for a morphism of topoi equipped with a localization datum along a functor of sites”.

> **Tag 093R.** The inverse image of a *finite* locally constant sheaf of sets along a
> morphism of topoi which is equipped with a localization datum is finite locally constant.
>
> The constant values are unchanged by
> `MorphismOfTopoi.LocalizationDatum.constantIsoOverPullbackInverseImage`, so their finiteness
> needs no argument.

```lean
public lemma isFiniteLocallyConstant_inverseImage {FA : Type w → Type w → Type*}
    {CA : Type w → Type wc} [∀ P Q, FunLike (FA P Q) (CA P) (CA Q)]
    [ConcreteCategory.{wc} (Type w) FA]
    (d : LocalizationDatum f) (G : Sheaf K (Type w))
    [hG : IsFiniteLocallyConstant (FD := FA) (CD := CA) K G] :
    IsFiniteLocallyConstant (FD := FA) (CD := CA) J (f.inverseImage.obj G)
```

**`MorphismOfTopoi.isLocallyConstant_inverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiSectionRelocalization.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiSectionRelocalization.lean#L264). The attribute's comment: “locally constant sheaves of sets, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”. References: SGA 3 X (9.2.1), “(4)”.

> **Tag 093R.** The inverse image of a locally constant sheaf of sets along an arbitrary
> morphism of topoi between the topoi of sheaves of sets on two small sites is locally constant.
>
> No functor between the two sites, and no final object in either, is assumed: the covering of an
> object `U` of `C` is the one `Stacks.Topos.exists_cover_inverseImage_sections` produces for the
> family of sheaves represented by the objects over which `G` is trivialized, and on a member of
> it the section it carries trivializes `(f⁻¹G)|_V` by
> `MorphismOfTopoi.constantIsoOverPullbackInverseImageOfSection`.

```lean
public lemma isLocallyConstant_inverseImage_of_smallSites (G : Sheaf K (Type w))
    [hG : IsLocallyConstant K G] : IsLocallyConstant J (f.inverseImage.obj G)
```

**`MorphismOfTopoi.isFiniteLocallyConstant_inverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiSectionRelocalization.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/MorphismOfTopoiSectionRelocalization.lean#L294). The attribute's comment: “finite locally constant sheaves of sets, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R.** The inverse image of a *finite* locally constant sheaf of sets along an
> arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites is finite
> locally constant.
>
> The constant values are unchanged by
> `MorphismOfTopoi.constantIsoOverPullbackInverseImageOfSection`, so their finiteness needs no
> argument; the covering is the one of
> `MorphismOfTopoi.isLocallyConstant_inverseImage_of_smallSites`, taken for the objects over which
> `G` becomes constant with a finite value.

```lean
public lemma isFiniteLocallyConstant_inverseImage_of_smallSites {FA : Type w → Type w → Type*}
    {CA : Type w → Type wc} [∀ P Q, FunLike (FA P Q) (CA P) (CA Q)]
    [ConcreteCategory.{wc} (Type w) FA] (G : Sheaf K (Type w))
    [hG : IsFiniteLocallyConstant (FD := FA) (CD := CA) K G] :
    IsFiniteLocallyConstant (FD := FA) (CD := CA) J (f.inverseImage.obj G)
```

**`MorphismOfTopoi.isLocallyConstant_ringInverseImage_of_smallSites`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/RingLocallyConstantInverseImage.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/RingLocallyConstantInverseImage.lean#L209). The attribute's comment: “locally constant sheaves of rings, for an arbitrary morphism of topoi between the topoi of sheaves of sets on two small sites”.

> **Tag 093R for locally constant sheaves of rings.** The inverse image of a locally constant
> sheaf of rings along an arbitrary morphism of topoi between the topoi of sheaves of sets on two
> small sites is locally constant.
>
> No functor between the two sites, no final object in either, no commutativity of the local
> values and no finiteness of them is assumed. The covering of an object `U` of `C` is the one
> `Stacks.Topos.exists_cover_inverseImage_sections` produces for the family of sheaves represented
> by the objects of `D` over which `G` is trivialized as a sheaf of rings, and on a member `V` of
> it the section it carries trivializes the inverse image over `V`, with the same trivializing
> ring, by `MorphismOfTopoi.ringConstantIsoOverPullbackInverseImageOfSection`.

```lean
public lemma isLocallyConstant_ringInverseImage_of_smallSites
    (G : Sheaf K RingCat.{w}) [hG : IsLocallyConstant K G] :
    IsLocallyConstant J ((CategoryTheory.Sites.ringInverseImage f).obj G)
```

## Tag 093S, a lemma

[Tag 093S](https://stacks.math.columbia.edu/tag/093S) in the Stacks Project.

**`Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_abelian`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantAbelian/Morphisms.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantAbelian/Morphisms.lean#L358). The attribute's comment: “part (2), sheaves of abelian groups; assumes pointwise right Kan extensions along the localization functors, a limit-existence side condition implied by fibre products in the site”. References: SGA 4 IX (2.1), “(ii) map, abelian”.

> A morphism of locally constant sheaves of abelian groups whose source is finite locally
> constant is, on a covering of any object, obtained from a homomorphism of abelian groups.

```lean
lemma exists_cover_restrict_eq_constantSheaf_map_abelian
    (F G : Sheaf J Ab.{w}) (φ : F ⟶ G)
    [hF : IsFiniteLocallyConstant J F] [hG : IsLocallyConstant J G] (U : C) :
    ∃ (I : Type (max u v)) (X : I → C) (f : ∀ i, X i ⟶ U),
      Sieve.ofArrows X f ∈ J U ∧ ∀ i,
        ∃ (A B : Ab.{w}), Finite (A : Type w) ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf (J.over (X i)) Ab.{w}).obj A ≅
              (J.overPullback Ab.{w} (X i)).obj F)
            (eG : (constantSheaf (J.over (X i)) Ab.{w}).obj B ≅
              (J.overPullback Ab.{w} (X i)).obj G),
              (constantSheaf (J.over (X i)) Ab.{w}).map g ≫ eG.hom =
                eF.hom ≫ (J.overPullback Ab.{w} (X i)).map φ
```

**`Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_abelian_smallSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantAbelian/Morphisms.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantAbelian/Morphisms.lean#L392). The attribute's comment: “part (2), sheaves of abelian groups”. References: SGA 4 IX (2.1), “(ii) map, abelian”.

> On a small site `C : Type u`, with the abelian groups in the universe `u`, a morphism of
> locally constant sheaves of abelian groups whose source is finite locally constant is, on a
> covering of any object, obtained from a homomorphism of abelian groups.

```lean
lemma exists_cover_restrict_eq_constantSheaf_map_abelian_smallSite
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (F G : Sheaf J Ab.{u}) (φ : F ⟶ G)
    [IsFiniteLocallyConstant J F] [IsLocallyConstant J G] (U : C) :
    ∃ (I : Type u) (X : I → C) (f : ∀ i, X i ⟶ U),
      Sieve.ofArrows X f ∈ J U ∧ ∀ i,
        ∃ (A B : Ab.{u}), Finite (A : Type u) ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf (J.over (X i)) Ab.{u}).obj A ≅
              (J.overPullback Ab.{u} (X i)).obj F)
            (eG : (constantSheaf (J.over (X i)) Ab.{u}).obj B ≅
              (J.overPullback Ab.{u} (X i)).obj G),
              (constantSheaf (J.over (X i)) Ab.{u}).map g ≫ eG.hom =
                eF.hom ≫ (J.overPullback Ab.{u} (X i)).map φ
```

**`Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_modules`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantModules/Morphisms.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantModules/Morphisms.lean#L477). The attribute's comment: “part (3), sheaves of Λ-modules, with `of finite type` in the equivalent locally-constant-with-finitely-generated-values form of Tag 093N; assumes pointwise right Kan extensions along the localization functors, a limit-existence side condition implied by fibre products in the site”. References: SGA 4 IX (2.1).

> **Stacks 093S (3).** A morphism of locally constant sheaves of `R`-modules whose source is
> locally constant of finite type is, on a covering of any object, obtained from a homomorphism of
> `R`-modules.
>
> Carries one hypothesis the source does not state: the family of pointwise right Kan extensions
> along `(Over.map t).op` out of which `Stacks.ConstantSheaf.constantSheafOverMapIso` is built. It is
> a limit-existence side condition on the coefficient category, implied both by `UnivLE.{max u v, w}`
> and by fibre products in the site; see this file's implementation notes, and
> `Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_modules_of_hasPullbacks` for the
> form carrying no universe condition at all.
> `Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_modules_smallSite` is the form on
> a small site, where that side condition is a theorem rather than a hypothesis, and is what part (3)
> of the tag is registered on.

```lean
lemma exists_cover_restrict_eq_constantSheaf_map_modules
    (F G : Sheaf J (ModuleCat.{w} R)) (φ : F ⟶ G)
    (hF : IsFiniteTypeLocallyConstant R J F) [hG : IsLocallyConstant J G] (U : C) :
    ∃ (I : Type (max u v)) (X : I → C) (f : ∀ i, X i ⟶ U),
      Sieve.ofArrows X f ∈ J U ∧ ∀ i,
        ∃ (A B : ModuleCat.{w} R), ModuleCat.isFG R A ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf (J.over (X i)) (ModuleCat.{w} R)).obj A ≅
              (J.overPullback (ModuleCat.{w} R) (X i)).obj F)
            (eG : (constantSheaf (J.over (X i)) (ModuleCat.{w} R)).obj B ≅
              (J.overPullback (ModuleCat.{w} R) (X i)).obj G),
              (constantSheaf (J.over (X i)) (ModuleCat.{w} R)).map g ≫ eG.hom =
                eF.hom ≫ (J.overPullback (ModuleCat.{w} R) (X i)).map φ
```

**`Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_modules_smallSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantModules/Morphisms.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantModules/Morphisms.lean#L542). The attribute's comment: “part (3), sheaves of Λ-modules, with `of finite type` in the equivalent locally-constant-with-finitely-generated-values form of Tag 093N”. References: SGA 4 IX (2.1).

> **Stacks 093S (3).** A morphism of locally constant sheaves of `R`-modules whose source is
> locally constant of finite type is, on a covering of any object, obtained from a homomorphism of
> `R`-modules.
>
> Stated on a small site, `C : Type u` with `SmallCategory C` and the modules in the same universe,
> which is the setting of the source and this library's convention for a small site. In it the
> statement carries *no* hypothesis beyond the source's: the pointwise right Kan extensions along the
> localization functors `(Over.map t).op`, which
> `Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map_modules` takes as an input, are
> limits over `u`-small index categories and so exist in `ModuleCat.{u} R` by
> `ModuleCat.hasLimitsOfShape`; sheafification on each localized site is automatic for the same
> reason. Neither `UnivLE` nor fibre products in the site are needed.

```lean
lemma exists_cover_restrict_eq_constantSheaf_map_modules_smallSite
    {R : Type r} [Ring R] {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (F G : Sheaf J (ModuleCat.{u} R)) (φ : F ⟶ G)
    (hF : IsFiniteTypeLocallyConstant R J F) [IsLocallyConstant J G] (U : C) :
    ∃ (I : Type u) (X : I → C) (f : ∀ i, X i ⟶ U),
      Sieve.ofArrows X f ∈ J U ∧ ∀ i,
        ∃ (A B : ModuleCat.{u} R), ModuleCat.isFG R A ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf (J.over (X i)) (ModuleCat.{u} R)).obj A ≅
              (J.overPullback (ModuleCat.{u} R) (X i)).obj F)
            (eG : (constantSheaf (J.over (X i)) (ModuleCat.{u} R)).obj B ≅
              (J.overPullback (ModuleCat.{u} R) (X i)).obj G),
              (constantSheaf (J.over (X i)) (ModuleCat.{u} R)).map g ≫ eG.hom =
                eF.hom ≫ (J.overPullback (ModuleCat.{u} R) (X i)).map φ
```

**`Stacks.ConstantSheaf.exists_cover_restrict_eq_constantSheaf_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Morphisms.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Morphisms.lean#L533). The attribute's comment: “sets”. References: SGA 4 IX (2.1), “(i)”.

> A morphism of locally constant sheaves of sets whose source is finite locally constant is, on
> a covering of any object, obtained from a map of sets.

```lean
lemma exists_cover_restrict_eq_constantSheaf_map
    (F G : Sheaf J (Type w)) (φ : F ⟶ G)
    [IsFiniteLocallyConstant J F] [IsLocallyConstant J G] (U : C) :
    ∃ (I : Type (max u v)) (X : I → C) (f : ∀ i, X i ⟶ U),
      Sieve.ofArrows X f ∈ J U ∧ ∀ i,
        ∃ (A B : Type w), Finite A ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf (J.over (X i)) (Type w)).obj A ≅
              (J.overPullback (Type w) (X i)).obj F)
            (eG : (constantSheaf (J.over (X i)) (Type w)).obj B ≅
              (J.overPullback (Type w) (X i)).obj G),
              (constantSheaf (J.over (X i)) (Type w)).map g ≫ eG.hom =
                eF.hom ≫ (J.overPullback (Type w) (X i)).map φ
```

## Tag 093T, a lemma

[Tag 093T](https://stacks.math.columbia.edu/tag/093T) in the Stacks Project.

**`Stacks.ConstantSheaf.constantSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean#L533). The attribute's comment: “constant_hom”.

> **Stacks Project, Tag 093T (1).** For a finitely presented `Λ`-module `M` and any
> `Λ`-module `N`, the constant sheaf on `Hom_Λ(M, N)` is the internal hom of the constant sheaves
> on `M` and on `N`:
> `Hom_Λ(M, N)̲ ≅ SheafHom_{Λ̲}(M̲, N̲)`,
> as sheaves of `Λ`-modules. The module `E` is any representative of `Hom_Λ(M, N)`, supplied with
> the identification `e`.

```lean
noncomputable def constantSheafHomIso
    [Module.FinitePresentation Λ (M : Type (max u v x))] :
    (constantSheaf J (ModuleCat.{max u v x} Λ)).obj E ≅
      moduleSheafHom J Λ ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj M)
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj N)
```

**`Stacks.ConstantSheaf.constantSheafHomIso_hom_app_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean#L548). The attribute's comment: “constant_hom”. References: SGA 3 VIII (1.4), “partial”.

> **Stacks Project, Tag 093T (1), the comparison is the canonical one.** The section of the
> internal hom over `X` which the isomorphism assigns to the constant section determined by a
> homomorphism `f : M ⟶ N` is the restriction to the slice site `C/X` of the morphism of constant
> sheaves induced by `f`.

```lean
theorem constantSheafHomIso_hom_app_apply
    [Module.FinitePresentation Λ (M : Type (max u v x))] (X : Cᵒᵖ) (f : M ⟶ N) :
    ((constantSheafHomIso J Λ M N E e).hom.hom.app X).hom
        (((constantUnit J Λ E).app X).hom (e (ModuleCat.homLinearEquiv (S := Λ) f))) =
      (J.overPullback (ModuleCat.{max u v x} Λ) X.unop).map
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).map f)
```

**`Stacks.ConstantSheaf.constantSheafHomIso_hom_app_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean#L592). The attribute's comment: “constant_hom”.

> **Stacks Project, Tag 093T (1)**, applied to the identity: the comparison sends the constant
> section given by `𝟙 M` to the identity on every slice.

```lean
theorem constantSheafHomIso_hom_app_id
    [Module.FinitePresentation Λ (M : Type (max u v x))] (E' : ModuleCat.{max u v x} Λ)
    (e' : ((M : Type (max u v x)) →ₗ[Λ] (M : Type (max u v x))) ≃ₗ[Λ] E') (X : Cᵒᵖ) :
    ((constantSheafHomIso J Λ M M E' e').hom.hom.app X).hom
        (((constantUnit J Λ E').app X).hom (e' (ModuleCat.homLinearEquiv (S := Λ) (𝟙 M)))) =
      𝟙 ((J.overPullback (ModuleCat.{max u v x} Λ) X.unop).obj
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj M))
```

**`Stacks.ConstantSheaf.constantSheafHomIso_hom_app_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean#L605). The attribute's comment: “constant_hom”.

> **Stacks Project, Tag 093T (1)**, applied to a composition: the comparison respects
> composition of constant homomorphisms on every slice.

```lean
theorem constantSheafHomIso_hom_app_comp
    [Module.FinitePresentation Λ (M : Type (max u v x))]
    [Module.FinitePresentation Λ (N : Type (max u v x))] (P : ModuleCat.{max u v x} Λ)
    (E₁ E₂ : ModuleCat.{max u v x} Λ)
    (e₁ : ((N : Type (max u v x)) →ₗ[Λ] (P : Type (max u v x))) ≃ₗ[Λ] E₁)
    (e₂ : ((M : Type (max u v x)) →ₗ[Λ] (P : Type (max u v x))) ≃ₗ[Λ] E₂)
    (X : Cᵒᵖ) (f : M ⟶ N) (g : N ⟶ P) :
    ((constantSheafHomIso J Λ M P E₂ e₂).hom.hom.app X).hom
        (((constantUnit J Λ E₂).app X).hom
          (e₂ (ModuleCat.homLinearEquiv (S := Λ) (f ≫ g)))) =
      ((constantSheafHomIso J Λ M N E e).hom.hom.app X).hom
          (((constantUnit J Λ E).app X).hom (e (ModuleCat.homLinearEquiv (S := Λ) f))) ≫
        ((constantSheafHomIso J Λ N P E₁ e₁).hom.hom.app X).hom
          (((constantUnit J Λ E₁).app X).hom
            (e₁ (ModuleCat.homLinearEquiv (S := Λ) g)))
```

**`Stacks.ConstantSheaf.constantSheafHomIsoOfHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafHom.lean#L637). The attribute's comment: “constant_hom”.

> **Stacks Project, Tag 093T (1)**, with `Hom_Λ(M, N)` represented by the morphism type of the
> category of `Λ`-modules rather than by an abstract representative.

```lean
noncomputable def constantSheafHomIsoOfHom (M N : ModuleCat.{max u v x} Λ)
    [Module.FinitePresentation Λ (M : Type (max u v x))] :
    (constantSheaf J (ModuleCat.{max u v x} Λ)).obj (ModuleCat.of Λ (M ⟶ N)) ≅
      moduleSheafHom J Λ ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj M)
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj N)
```

**`Stacks.ConstantSheaf.constantSheafIsomHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean#L412). The attribute's comment: “constant Isom”.

> **The canonical map of Stacks Tag 093T (2)**,
> `Isom_Λ(M, N)̲ ⟶ Isom_{Λ̲}(M̲, N̲)`:
> the map which sends a linear equivalence to the isomorphism of constant sheaves it induces,
> factored through the constant sheaf by the universal property of sheafification. That it is an
> isomorphism, which is the content of part (2), is
> `Stacks.ConstantSheaf.constantSheafIsomIso`.

```lean
noncomputable def constantSheafIsomHom :
    (constantSheaf J (Type (max u v x))).obj
        ((M : Type (max u v x)) ≃ₗ[Λ] (N : Type (max u v x))) ⟶
      moduleSheafIsom J Λ ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj M)
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj N)
```

**`Stacks.ConstantSheaf.constantSheafIsomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean#L464). The attribute's comment: “constant Isom”.

> **Stacks Project, Tag 093T (2).** `Isom_Λ(M, N)̲ ≅ Isom_{Λ̲}(M̲, N̲)` for finitely presented
> `M` and `N`, as sheaves of sets. The comparison is the canonical one: it sends the constant section
> given by a linear equivalence `e` to the restriction of the isomorphism of constant sheaves `e̲`,
> which is `Stacks.ConstantSheaf.toSheafify_constantSheafIsomHom` together with
> `Stacks.ConstantSheaf.constantIsomNatTrans_app_apply`.

```lean
noncomputable def constantSheafIsomIso
    [Module.FinitePresentation Λ (M : Type (max u v x))]
    [Module.FinitePresentation Λ (N : Type (max u v x))] :
    (constantSheaf J (Type (max u v x))).obj
        ((M : Type (max u v x)) ≃ₗ[Λ] (N : Type (max u v x))) ≅
      moduleSheafIsom J Λ ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj M)
        ((constantSheaf J (ModuleCat.{max u v x} Λ)).obj N)
```

**`Stacks.ConstantSheaf.isLocallyConstant_moduleSheafIsom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafIsom.lean#L616). The attribute's comment: “Isom of locally constant sheaves”.

> If `F` and `G` are locally constant sheaves of `Λ`-modules of finite presentation, then
> `Isom_{Λ̲}(F, G)` is a locally constant sheaf of sets. The assertion is local on `C`, so `F` and `G`
> may be trivialized simultaneously; over a member of the resulting covering they are the constant
> sheaves on finitely presented modules `M` and `N`, and then
> `Stacks.ConstantSheaf.constantSheafIsomIso` identifies `Isom_{Λ̲}(F, G)` with the constant sheaf on
> `M ≃ₗ[Λ] N`.

```lean
theorem isLocallyConstant_moduleSheafIsom (F G : Sheaf J (ModuleCat.{max u v x} Λ))
    (hF : IsFinitePresentationLocallyConstantModuleSheaf J Λ F)
    (hG : IsFinitePresentationLocallyConstantModuleSheaf J Λ G) :
    IsLocallyConstant J (moduleSheafIsom J Λ F G)
```

**`Stacks.ConstantSheaf.isLocallyConstant_moduleSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyConstantSheafHom.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyConstantSheafHom.lean#L249). The attribute's comment: “sheafHom of locally constant sheaves”.

> **Stacks Project, Tag 093T (3).** If `F` is a locally constant sheaf of `Λ`-modules of finite
> presentation and `G` is a locally constant sheaf of `Λ`-modules, then the internal hom
> `SheafHom_{Λ̲}(F, G)` is a locally constant sheaf of `Λ`-modules.

```lean
theorem isLocallyConstant_moduleSheafHom (F G : Sheaf J (ModuleCat.{max u v x} Λ))
    (hF : IsFinitePresentationLocallyConstantModuleSheaf J Λ F) [IsLocallyConstant J G] :
    IsLocallyConstant J (moduleSheafHom J Λ F G)
```

**`Stacks.ConstantSheaf.moduleSheafIsom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ModuleSheafIsom.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ModuleSheafIsom.lean#L235). The attribute's comment: “the sheaf Isom”.

> **The sheaf of isomorphisms of two sheaves of `Λ`-modules**, i.e. Stacks's
> `Isom_{Λ̲}(F, G)`: the subsheaf of `Stacks.ConstantSheaf.moduleSheafHom` of those sections which
> have an inverse in `Stacks.ConstantSheaf.moduleSheafHom` taken in the other order. The sections
> of the internal hom of sheaves of `Λ`-modules over `X` are the morphisms `F|_X ⟶ G|_X` of sheaves
> of `Λ`-modules, which are also the sections of `CategoryTheory.sheafHom`, so this is the
> subobject Stacks describes.

```lean
def moduleSheafIsom (F G : Sheaf J (ModuleCat.{max u v x} Λ)) :
    Sheaf J (Type (max u v x))
```

## Tag 093U, a lemma

[Tag 093U](https://stacks.math.columbia.edu/tag/093U) in the Stacks Project.

**`Stacks.ConstantSheaf.isWeakSerreClass_isFiniteTypeLocallyConstantModuleSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyConstantExtensions.lean, line 793](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyConstantExtensions.lean#L793). The attribute's comment: “finite_type_modules”. References: SGA 4 IX (2.1), “(ii) ker/coker, (iii)”.

> **Stacks Tag 093U (3).** On a site, the finite type locally constant sheaves of modules over
> a Noetherian ring form a weak Serre subcategory of the category of sheaves of modules.
>
> The five conditions of Tag 0754 are: strict fullness
> (`Stacks.ConstantSheaf.isClosedUnderIsomorphisms_isFiniteTypeLocallyConstantModuleSheaf`),
> containment of `0`
> (`Stacks.ConstantSheaf.containsZero_isFiniteTypeLocallyConstantModuleSheaf`), closure under
> kernels and under cokernels
> (`Stacks.ConstantSheaf.isClosedUnderKernels_isFiniteTypeLocallyConstantModuleSheaf` and
> `Stacks.ConstantSheaf.isClosedUnderCokernels_isFiniteTypeLocallyConstantModuleSheaf`), and
> closure under extensions
> (`Stacks.ConstantSheaf.isClosedUnderExtensions_isFiniteTypeLocallyConstantModuleSheaf`).

```lean
instance isWeakSerreClass_isFiniteTypeLocallyConstantModuleSheaf :
    ObjectProperty.IsWeakSerreClass
      (IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ)
```

**`Stacks.ConstantSheaf.isWeakSerreClass_isFiniteLocallyConstantAbelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianWeakSerre.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianWeakSerre.lean#L439). The attribute's comment: “finite_abelian”. References: SGA 4 IX (2.1), “(ii) ker/coker, (iii)”.

> **Stacks Tag 093U (2).** On a site, the finite locally constant sheaves of abelian groups form
> a weak Serre subcategory of the category of all abelian sheaves.
>
> The clause proved here is part (2). It is not an instance of part (3),
> `Stacks.ConstantSheaf.isWeakSerreClass_isFiniteTypeLocallyConstantModuleSheaf`: there the
> finiteness is finiteness of type over a Noetherian coefficient ring, here it is finiteness of the
> local value itself. Part (3) over `ℤ` is however what the proof reduces to, together with the
> local annihilation invariant `Stacks.ConstantSheaf.IsLocallyAnnihilated`.

```lean
theorem isWeakSerreClass_isFiniteLocallyConstantAbelianSheaf :
    (isFiniteLocallyConstantAbelianSheaf.{v, u, w} J).IsWeakSerreClass
```

**`Stacks.ConstantSheaf.isClosedUnderFiniteLimits_and_finiteColimits_isFiniteLocallyConstantSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/FiniteLimits.lean, line 743](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/FiniteLimits.lean#L743). The attribute's comment: “sets”.

> On a site, the finite locally constant sheaves of sets are closed under finite limits and
> under finite colimits inside the category of all sheaves of sets.
>
> The clause of the tag proved here is part (1), about sheaves of *sets* whose local constant
> values are finite sets. It is not an instance of part (3), which is
> `Stacks.ConstantSheaf.isWeakSerreClass_isFiniteTypeLocallyConstantModuleSheaf`: there the
> finiteness is finiteness of type over a Noetherian coefficient ring, here it is finiteness of the
> local value itself.

```lean
theorem isClosedUnderFiniteLimits_and_finiteColimits_isFiniteLocallyConstantSetSheaf :
    ObjectProperty.IsClosedUnderFiniteLimits
        (isFiniteLocallyConstantSetSheaf.{v, u, w} J) ∧
      ObjectProperty.IsClosedUnderFiniteColimits
        (isFiniteLocallyConstantSetSheaf.{v, u, w} J)
```

## Tag 093V, a lemma

[Tag 093V](https://stacks.math.columbia.edu/tag/093V) in the Stacks Project.

**`Stacks.ConstantSheaf.isLocallyConstant_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/TensorProduct.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/TensorProduct.lean#L159). References: SGA 5 VI (1.4.5), “locally constant claim”.

> The tensor product of two locally constant sheaves of `Λ`-modules on a site is a locally
> constant sheaf of `Λ`-modules.

```lean
theorem isLocallyConstant_tensor (F G : Sheaf J (ModuleCat.{w} Λ))
    [IsLocallyConstant J F] [IsLocallyConstant J G] : IsLocallyConstant J (F ⊗ G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.43, Tag 093P](https://stacks.math.columbia.edu/tag/093P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
