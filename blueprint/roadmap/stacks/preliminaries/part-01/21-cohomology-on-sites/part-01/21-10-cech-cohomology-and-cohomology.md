---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.injective_obj, Stacks.CechSite.cechCohomology_isZero_of_injective, Stacks.CechSite.cechCohomology_zero_iso, Stacks.CechSite.cechToDerivedSections, Stacks.CechSite.cechCohomologyToCohomology, Stacks.CechSite.nonempty_cechResolutionComparison, Stacks.CechSite.injective_cechCohomologyToCohomology_one, Stacks.Cohomology.Torsors.locallyTrivialClassEquivCechH1
statement: formalized
proof: formalized
---

# 21.10 Čech cohomology and cohomology

Section 21.10 of the Stacks Project, [Tag 03AV](https://stacks.math.columbia.edu/tag/03AV). 9 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03F6, a lemma

[Tag 03F6](https://stacks.math.columbia.edu/tag/03F6) in the Stacks Project.

**`CategoryTheory.Sheaf.injective_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveSheafVanishing.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveSheafVanishing.lean#L56).

> An injective sheaf is injective as a presheaf.

```lean
theorem Sheaf.injective_obj {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {A : Type u'} [Category.{v'} A] [HasSheafify J A]
    (I : Sheaf J A) [Injective I] : Injective I.obj
```

## Tag 03AW, a lemma

[Tag 03AW](https://stacks.math.columbia.edu/tag/03AW) in the Stacks Project.

**`Stacks.CechSite.cechCohomology_isZero_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroOfASheaf.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroOfASheaf.lean#L78). The attribute's comment: “positive degrees”.

> **Stacks 03AW (positive degrees).** The Čech cohomology of an injective abelian sheaf for a
> covering family vanishes in positive degrees.
>
> Stated before `include hE` because the covering property plays no part: the vanishing is pure
> injectivity, and carrying `hE` would make this strictly weaker than the source statement.

```lean
theorem cechCohomology_isZero_of_injective [Injective I] (p : ℕ) (hp : 0 < p) :
    IsZero (cechCohomology E I.obj p)
```

**`Stacks.CechSite.cechCohomology_zero_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroOfASheaf.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroOfASheaf.lean#L89). The attribute's comment: “degree zero”.

> **Stacks 03AW (degree zero).** The degree-zero Čech cohomology of an abelian sheaf for a
> covering family is its group of sections over the covered object.

```lean
theorem cechCohomology_zero_iso :
    Nonempty (cechCohomology E I.obj 0 ≅ I.obj.obj (op U))
```

## Tag 03AX, a lemma

[Tag 03AX](https://stacks.math.columbia.edu/tag/03AX) in the Stacks Project.

**`Stacks.CechSite.cechToDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean#L694). The attribute's comment: “the derived transformation”.

> **Stacks Project, Tag 03AX (derived transformation).** The Čech complex of a covering
> family maps naturally to derived sections over the covered object.

```lean
def cechToDerivedSections :
    cechDerivedFunctor.{a} K E ⟶ derivedSectionsFunctor.{max a u v w} K U
```

**`Stacks.CechSite.cechCohomologyToCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean#L706). The attribute's comment: “the induced cohomology maps”.

> **Stacks Project, Tag 03AX (cohomology maps).** Taking homology of the Čech-to-derived
> comparison gives maps from Čech cohomology to sheaf cohomology, natural in the sheaf.

```lean
def cechCohomologyToCohomology (p : ℤ) :
    (cechDerivedFunctor.{a} K E ⋙
        DerivedCategory.Plus.homologyFunctor Ab.{max a u v w} p) ⟶
      (derivedSectionsFunctor.{max a u v w} K U ⋙
        DerivedCategory.Plus.homologyFunctor Ab.{max a u v w} p)
```

**`Stacks.CechSite.nonempty_cechResolutionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ToSheafCohomology.lean#L751). The attribute's comment: “the injective-resolution specification”.

> **Stacks Project, Tag 03AX (the injective-resolution specification).** For every injective
> resolution, the Čech-to-derived-sections transformation is the map induced by the two canonical
> augmentations into the total Čech complex.

```lean
theorem nonempty_cechResolutionComparison (F : Sheaf K Ab.{max a u v w})
    (J : InjectiveResolution F) :
    Nonempty (CechResolutionComparison.{a} K E hE F J)
```

## Tag 0A6G, a lemma

[Tag 0A6G](https://stacks.math.columbia.edu/tag/0A6G) in the Stacks Project.

**`Stacks.CechSite.injective_cechCohomologyToCohomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeOneInjectivity.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeOneInjectivity.lean#L334). The attribute's comment: “variant: injectivity of the derived-category comparison; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”.

> **Stacks Project, Tag 0A6G.** For a covering family `𝒰 = {U_i → U}` of an object of a site
> and an abelian sheaf `G`, the map `Ȟ¹(𝒰, G) → H¹(U, G)` of Stacks 03AX is injective.

```lean
theorem injective_cechCohomologyToCohomology_one (hE : Sieve.generate E.presieve₀ ∈ K U)
    (G : Sheaf K Ab.{max a u v w}) :
    Function.Injective ((cechCohomologyToCohomology.{a} K E hE 1).app G)
```

**`Stacks.Cohomology.Torsors.locallyTrivialClassEquivCechH1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassBijection.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassBijection.lean#L204). The attribute's comment: “variant: the Čech class bijection onto Ȟ¹(𝒰,G); the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “partial”.

> **Stacks Project, Tag 0A6G.** First Čech cohomology of a covering family, as the set of
> isomorphism classes of `G|_U`-torsors which restrict to trivial torsors over each member of
> the family.

```lean
def locallyTrivialClassEquivCechH1 (hE : E.sieve₀ ∈ J U)
    (G : Sheaf J AddCommGrpCat.{max a u v w}) :
    LocallyTrivialClass E G ≃ cechH1 E G.obj
```

**`Stacks.CechSite.injective_cechH1ToCohomology_and_bijective_cechClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassCohomologyComparison.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassCohomologyComparison.lean#L149). The attribute's comment: “variant: injectivity and the Čech class bijection at the explicit Ȟ¹(𝒰,G); the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”.

> For a covering family `𝒰 = {U_i → U}` of an object of a site and an abelian sheaf `G`, the
> map `Ȟ¹(𝒰, G) → H¹(U, G)` is injective, and `Ȟ¹(𝒰, G)` is in bijection — under the Čech class
> of a family of local sections — with the isomorphism classes of `G|_U`-torsors which restrict to
> trivial torsors over each `U_i`. Both assertions are about the group
> `Stacks.CechSite.cechH1 E G.obj`.

```lean
theorem injective_cechH1ToCohomology_and_bijective_cechClass (hE : E.sieve₀ ∈ K U)
    (G : Sheaf K AddCommGrpCat.{max a u v w}) :
    Function.Injective (cechH1ToCohomology.{a} K E hE G) ∧
      Function.Bijective (Stacks.Cohomology.Torsors.cechClass E G)
```

**`Stacks.CechSite.injective_torsorCohomologyClass_and_range_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassCohomologyComparison.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassCohomologyComparison.lean#L256). The attribute's comment: “variant: the Čech class of a torsor read in the derived H¹(U,G); the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “Abelian”.

> For a covering family `𝒰 = {U_i → U}` of an object of a site and an abelian sheaf `G`, the
> map which sends an isomorphism class of `G|_U`-torsors trivial over each `U_i` to the image in
> `H¹(U, G)` of its Čech class is injective, and its image is exactly the image of
> `Ȟ¹(𝒰, G) → H¹(U, G)`.
>
> So `Ȟ¹(𝒰, G)` is a subgroup of `H¹(U, G)`, and the Čech class map identifies that subgroup with
> the isomorphism classes of `G|_U`-torsors which restrict to trivial torsors over each `U_i`. The
> map is `Stacks.CechSite.torsorCohomologyClass`, which is the Čech class map
> followed by the comparison (`Stacks.CechSite.torsorCohomologyClass_eq`); on a representative with
> local sections it is the comparison applied to the class of the transition cocycle
> (`Stacks.CechSite.torsorCohomologyClass_mk`), and it vanishes exactly on the trivial torsor
> (`Stacks.CechSite.isTrivial_iff_torsorCohomologyClass_eq_zero`).

```lean
theorem injective_torsorCohomologyClass_and_range_eq (hE : E.sieve₀ ∈ K U)
    (G : Sheaf K AddCommGrpCat.{max a u v w}) :
    Function.Injective (torsorCohomologyClass.{h, a} K E hE G) ∧
      Set.range (torsorCohomologyClass.{h, a} K E hE G) =
        Set.range (cechH1ToCohomology.{a} K E hE G)
```

**`Stacks.CechSite.cechH1ToSliceH_injective_and_range_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassFirstCohomology.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassFirstCohomology.lean#L167).

> Let `𝒰 = {U_i → U}` be a covering of a site and `G` an abelian sheaf. The map
> `Ȟ¹(𝒰, G) → H¹(U, G)` of Stacks 03AX is injective and, through the bijection of Stacks 03AJ between
> isomorphism classes of `G|_U`-torsors and `H¹(U, G)`, identifies `Ȟ¹(𝒰, G)` with the set of
> isomorphism classes of `G|_U`-torsors which restrict to trivial torsors over each `U_i`: the class
> under 03AJ of such a torsor is the image of its Čech class, and the image of `Ȟ¹(𝒰, G)` is exactly
> the set of these classes.
>
> Here `H¹(U, G)` is `Sheaf.H (G.over U) 1`, the target of the bijection of 03AJ, and the map is the
> comparison of 03AX read there through the canonical identification of the two models of first
> cohomology (`Stacks.CechSite.cechH1ToSliceH`). Sheafification, the comparison of the sheaf
> topology with local bijectivity, enough injectives and the `Ext`-groups at the coefficient
> universe `max a u v w` exist on every site and are constructed in the statement. The existence
> of the iterated fibre products of the members of `𝒰` is part of the definition of a covering in
> the source.

```lean
theorem cechH1ToSliceH_injective_and_range_eq (hE : E.sieve₀ ∈ K U)
    (G : Sheaf K AddCommGrpCat.{max a u v w}) :
    letI : HasSheafify K AddCommGrpCat.{max a u v w} :=
      site_hasSheafify_addCommGrp.{u, v, max a w}
    letI : K.WEqualsLocallyBijective AddCommGrpCat.{max a u v w} :=
      site_wEqualsLocallyBijective_addCommGrp.{u, v, max a w}
    letI : EnoughInjectives (Sheaf K AddCommGrpCat.{max a u v w}) :=
      CategoryTheory.Sheaf.enoughInjectives_addCommGrpCat_max.{max a w, v, u} K
    letI : HasSheafify (K.over U) AddCommGrpCat.{max a u v w} :=
      site_hasSheafify_addCommGrp.{max u v, v, max a w}
    letI : EnoughInjectives (Sheaf (K.over U) AddCommGrpCat.{max a u v w}) :=
      CategoryTheory.Sheaf.enoughInjectives_addCommGrpCat_max.{max a w, v, max u v} (K.over U)
    letI : HasExt.{max a u v w} (Sheaf (K.over U) AddCommGrpCat.{max a u v w}) :=
      hasExt_of_enoughInjectives _
    Function.Injective (cechH1ToSliceH.{a} K E hE G) ∧
      (∀ c : LocallyTrivialClass E G,
        cechH1ToSliceH.{a} K E hE G (cechClass E G c) =
          torsorIsoClassesEquivH1.{max a u v w} (G.over U) c.1) ∧
      Set.range (cechH1ToSliceH.{a} K E hE G) =
        torsorIsoClassesEquivH1.{max a u v w} (G.over U) ''
          {c | ∃ F : AbelianTorsor (G.over U),
            Quotient.mk (torsorSetoid (G.over U)) F = c ∧ IsTrivialOnMembers E G F}
```

**`Stacks.Cohomology.Torsors.isTrivial_iff_cechClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassInjectivity.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassInjectivity.lean#L175). The attribute's comment: “variant: the Čech class vanishes exactly on the trivial torsor; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “special case”.

> **A torsor with vanishing Čech class is trivial.** For a covering family, the Čech class of
> a torsor with a section over every member vanishes exactly when the torsor is trivial: the class
> vanishes when the transition cocycle is a Čech coboundary, and subtracting that coboundary from
> the local sections makes the transition cochain vanish on the nose.

```lean
theorem isTrivial_iff_cechClass_eq_zero (hE : E.sieve₀ ∈ J U) (F : AbelianTorsor (G.over U))
    (hs : ∀ i, Nonempty (F.1.presheaf.obj (op (Over.mk (E.f i))))) :
    F.1.IsTrivial ↔
      cechClass E G ⟨Quotient.mk (torsorSetoid (G.over U)) F, ⟨F, rfl, hs⟩⟩ = 0
```

**`Stacks.Cohomology.Torsors.cechClass_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassInjectivity.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CechClassInjectivity.lean#L458). The attribute's comment: “variant: injectivity of the Čech class map; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “partial”.

> **The Čech class is injective on the locally trivial isomorphism classes.** Under the
> bijection of Stacks 03AJ between isomorphism classes of torsors and first cohomology, this is
> the injectivity of the identification of `Ȟ¹(𝒰, G)` with the isomorphism classes of torsors
> which are trivial over every member of `𝒰`.

```lean
theorem cechClass_injective (hE : E.sieve₀ ∈ J U) :
    Function.Injective (cechClass E G)
```

**`Stacks.Cohomology.Torsors.cls_transitionCocycle_congr`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L371). The attribute's comment: “variant: independence of the chosen local sections; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “special case”.

> **The Čech class of the transition cocycle does not depend on the chosen local sections.**

```lean
lemma cls_transitionCocycle_congr (F : AbelianTorsor (G.over U))
    (s s' : ∀ i, F.1.presheaf.obj (op (Over.mk (E.f i)))) :
    cls E G.obj (transitionCocycle E G F s) = cls E G.obj (transitionCocycle E G F s')
```

**`Stacks.Cohomology.Torsors.cls_transitionCocycle_eq_of_isIsomorphic`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L393). The attribute's comment: “variant: independence of the torsor inside its isomorphism class; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “partial”.

> **The Čech class of the transition cocycle depends only on the isomorphism class of the
> torsor.**

```lean
lemma cls_transitionCocycle_eq_of_isIsomorphic {F F' : AbelianTorsor (G.over U)}
    (hFF' : AbelianTorsor.IsIsomorphic F F')
    (s : ∀ i, F.1.presheaf.obj (op (Over.mk (E.f i))))
    (s' : ∀ i, F'.1.presheaf.obj (op (Over.mk (E.f i)))) :
    cls E G.obj (transitionCocycle E G F s) = cls E G.obj (transitionCocycle E G F' s')
```

**`Stacks.Cohomology.Torsors.isTrivialOnMembers_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L429). The attribute's comment: “variant: torsors trivial over each member have sections there; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: SGA 3 IV (5.1.5), “(ii)”.

> **The torsors which restrict to trivial torsors over each member of the covering.** A torsor
> under `G|_U` restricts to a trivial torsor over every member of the family exactly when it has a
> section over every member.

```lean
theorem isTrivialOnMembers_iff (F : AbelianTorsor (G.over U)) :
    IsTrivialOnMembers E G F ↔
      ∀ i, Nonempty (F.1.presheaf.obj (op (Over.mk (E.f i))))
```

**`Stacks.Cohomology.Torsors.cechClass_eq_zero_of_isTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L497). The attribute's comment: “variant: the trivial torsor has vanishing Čech class; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”. References: EGA IV (16.5.15), “partial”.

> **A trivial torsor has vanishing Čech class.** A global section restricts to a family of
> local sections all of whose differences vanish.

```lean
theorem cechClass_eq_zero_of_isTrivial (F : AbelianTorsor (G.over U))
    (hF : F.1.IsTrivial)
    (hs : ∀ i, Nonempty (F.1.presheaf.obj (op (Over.mk (E.f i))))) :
    cechClass E G ⟨Quotient.mk (torsorSetoid (G.over U)) F, ⟨F, rfl, hs⟩⟩ = 0
```

**`Stacks.Cohomology.Torsors.isTrivial_of_transitionCochain_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L577). The attribute's comment: “variant: a torsor whose transition cocycle vanishes is trivial; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”.

> **A vanishing transition cochain makes the torsor trivial.** The local sections then agree
> on every common refinement of two members of the covering, so the sheaf condition for the
> covering sieve glues them to a section over the terminal object of `C/U`, and a torsor with such
> a section is trivial by Stacks 03AI.

```lean
theorem isTrivial_of_transitionCochain_eq_zero (hE : E.sieve₀ ∈ J U)
    (F : AbelianTorsor (G.over U))
    (s : ∀ i, F.1.presheaf.obj (op (Over.mk (E.f i))))
    (hs : transitionCochain E G F s = 0) : F.1.IsTrivial
```

**`Stacks.Cohomology.Torsors.isTrivial_iff_exists_transitionCochain_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/LocalTriviality.lean#L608). The attribute's comment: “variant: triviality in terms of the transition cocycle; the tag is Stacks.CechSite.cechH1ToSliceH\_injective\_and\_range\_eq”.

> **Triviality in terms of the transition cocycle.** For a covering family, a torsor under
> `G|_U` with a section over every member of the family is trivial exactly when some family of
> local sections has vanishing transition cochain, that is, exactly when the local sections can be
> chosen to agree on all the fibre products.

```lean
theorem isTrivial_iff_exists_transitionCochain_eq_zero (hE : E.sieve₀ ∈ J U)
    (F : AbelianTorsor (G.over U)) :
    F.1.IsTrivial ↔
      ∃ s : ∀ i, F.1.presheaf.obj (op (Over.mk (E.f i))), transitionCochain E G F s = 0
```

## Tag 03AY, a lemma

[Tag 03AY](https://stacks.math.columbia.edu/tag/03AY) in the Stacks Project.

**`Stacks.Cohomology.rightDerivedSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedSheafToPresheafNaturality.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedSheafToPresheafNaturality.lean#L283). The attribute's comment: “right derived functors”. References: SGA 4 IV (4.8), “partial”; SGA 4 V (2.4.2), “special case”.

> **Stacks 03AY, right derived functors.** The `p`-th right derived functor of the inclusion of
> abelian sheaves into abelian presheaves on a small site is naturally isomorphic to the functor
> sending an abelian sheaf to its degree-`p` cohomology presheaf.

```lean
noncomputable def rightDerivedSheafToPresheafIso (p : ℕ) :
    (sheafToPresheaf J AddCommGrpCat.{u}).rightDerived p ≅
      Sheaf.cohomologyPresheafFunctor J p
```

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.instPreservesFiniteLimitsFunctorOppositeSheafToPresheafOfHasFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.instPreservesFiniteLimitsFunctorOppositeSheafToPresheafOfHasFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedSheafToPresheaf.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedSheafToPresheaf.lean#L148) (StacksFrontier): “left exact”. References: SGA 3 IV (4.4.1), “(i)”; SGA 4 II (4.1), “special case”.

## Tag 03AZ, a lemma

[Tag 03AZ](https://stacks.math.columbia.edu/tag/03AZ) in the Stacks Project.

**`Stacks.CechSite.exists_cechToCohomology_spectralSequence_sheafCohomologyAbutment`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechToCohomology.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CechToCohomology.lean#L403). The attribute's comment: “the spectral sequence, its second page and its convergence”. References: SGA 4 V (3.6), “more general”.

> **The Čech-to-cohomology spectral sequence of a covering family, for a single abelian
> sheaf.** For a family `𝒰 = E` generating a covering sieve on `U` and an abelian sheaf `F` there
> is a cohomological spectral sequence with second page
>
> ```
> E₂^{p,q} ≅ Ȟ^p(𝒰, H^q(F))
> ```
>
> abutting to a graded family whose value in degree `n : ℕ` is the sheaf cohomology `H^n(U, F)`.
>
> This is `Stacks.CechSite.exists_cechToCohomology_spectralSequence_cohomologyAbutment` with its
> abutment read through `Stacks.CechSite.rightDerivedPlus_sheafIncl_obj_obj_iso`; the abutment is
> indexed by `ℤ`, as `CategoryTheory.SpectralSequence.AbutsTo` requires, and the identification is
> stated in the nonnegative degrees, which are the ones a first-quadrant spectral sequence
> contributes to. Functoriality of the spectral sequence in `F` is not asserted; see the
> implementation notes of this file.

```lean
public theorem exists_cechToCohomology_spectralSequence_sheafCohomologyAbutment
    (hE : E.sieve₀ ∈ J U) (F : Sheaf J AddCommGrpCat.{u}) :
    ∃ (S : CohomologicalSpectralSequence AddCommGrpCat.{u} 0) (H : ℤ → AddCommGrpCat.{u}),
      (∀ p q : ℕ, Nonempty ((S.page 2 zero_le_two).X ((p : ℤ), (q : ℤ)) ≅
        cechCohomology E (F.cohomologyPresheaf q) p)) ∧
      (∀ n : ℕ, Nonempty (H (n : ℤ) ≅ (F.cohomologyPresheaf n).obj (op U))) ∧
      SpectralSequence.AbutsTo S H
```

**`Stacks.CechSite.cechToCohomologySheafCohomologyAbutment`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechToCohomologyAbutment.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CechToCohomologyAbutment.lean#L157). The attribute's comment: “the abutment of the functorial spectral sequence is `H^{p+q}(U, F)`”. References: SGA 4 V (3.2), “abutment (covering)”; SGA 4 V (3.3), “partial”.

> **The abutment clause of [Stacks, Tag 03AZ]**: the functorial Čech-to-cohomology spectral
> sequence of a covering family `𝒰 = {U_i → U}` abuts, through a finite decreasing filtration whose
> graded pieces are its infinity terms, to the sheaf cohomology `H^{p+q}(U, F)` — all of it
> naturally in the abelian sheaf `F`.
>
> Together with `Stacks.CechSite.cechToCohomologySpectralSequenceFunctor` and
> `Stacks.CechSite.cechToCohomologyPageTwoIso` this is the whole of [Stacks, Tag 03AZ] in functorial
> form: a functor from abelian sheaves to first-quadrant `E₂` cohomological spectral sequences, a
> natural identification of its second page with `Ȟ^p(𝒰, H^q(F))` and a functorial filtered
> abutment to `H^{p+q}(U, F)`.
>
> It is `Stacks.CechSite.cechToCohomologyFunctorialAbutment` with its abutment transported along
> `Stacks.CechSite.cechToCohomologyAbutmentIso`;
> `Stacks.Cohomology.Leray.FunctorialFirstQuadrantAbutsTo.ofIsoAbutment` touches no other field --
> the asserted abutment is mentioned in `abutmentIso` alone, so the filtration, its finiteness, its
> top and bottom steps and the graded identification are the ones already proved.

```lean
noncomputable def cechToCohomologySheafCohomologyAbutment (hE : E.presieve₀ ∈ J U) :
    FunctorialFirstQuadrantAbutsTo
      (cechToCohomologySpectralSequenceFunctor J.toGrothendieck E)
      (fun n ↦ Sheaf.cohomologyPresheafFunctor J.toGrothendieck n ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{v}).obj (op U))
```

**`Stacks.CechSite.cechToCohomologySpectralSequenceFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechToCohomologyFunctorial.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CechToCohomologyFunctorial.lean#L228). The attribute's comment: “functoriality of the spectral sequence in the sheaf”.

> **The Čech-to-cohomology spectral sequence of a family of morphisms, as a functor of the
> abelian sheaf.** This is the last sentence of [Stacks, Tag 03AZ]: the spectral sequence whose
> second page is `Ȟ^p(𝒰, H^q(F))` is functorial in `F`.
>
> It is the first-quadrant `E₂` cohomological spectral sequence of the double complex
> `A^{i,j}(F) = Č^j(𝒰, I^i(F))` of the Čech complexes of a functorial injective resolution of `F`,
> obtained by restricting the two-variable spectral sequence of clause (3) of [Stacks, Tag 01GY]
> along `Stacks.CechSite.sheafToCechPair`. Its second page is
> `Stacks.CechSite.cechToCohomologyPageTwoIso` and its functorial filtered abutment is
> `Stacks.CechSite.cechToCohomologyFunctorialAbutment`; that abutment is the cohomology of the
> total complex and is *not* identified with `H^n(U, F)` here.

```lean
noncomputable def cechToCohomologySpectralSequenceFunctor : Sheaf J AddCommGrpCat.{v} ⥤
    E₂CohomologicalSpectralSequenceNat AddCommGrpCat.{v}
```

**`Stacks.CechSite.cechToCohomologyPageTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechToCohomologyFunctorial.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CechToCohomologyFunctorial.lean#L272). The attribute's comment: “functoriality of the second page in the sheaf”. References: SGA 4 V (3.2), “E₂-page (covering)”.

> **The second page of the functorial Čech-to-cohomology spectral sequence is
> `Ȟ^p(𝒰, H^q(F))`, naturally in the sheaf `F`.** Together with
> `Stacks.CechSite.cechToCohomologySpectralSequenceFunctor` this is the functoriality asserted by
> the last sentence of [Stacks, Tag 03AZ]: not merely that each sheaf has such a spectral sequence,
> but that the assignment is a functor and that the second-page identification is a natural
> isomorphism.
>
> It is `Stacks.CategoryTheory.Hypercovering.Functorial.hypercoverPageTwoIso` restricted along
> `Stacks.CechSite.sheafToCechPair`.

```lean
noncomputable def cechToCohomologyPageTwoIso (p q : ℕ) :
    cechToCohomologySpectralSequenceFunctor J E ⋙
        CategoryTheory.SpectralSequence.pageFunctor _ _ 2 2 ⋙
          HomologicalComplex.eval _ _ (p, q) ≅
      cechPageTwoFunctor J E p q
```

Declarations registered for the tag:

- [`exists_cechToCohomology_spectralSequence_cohomologyAbutment`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_cechToCohomology_spectralSequence_cohomologyAbutment#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/CechToCohomology.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CechToCohomology.lean#L380) (StacksFrontier): “the spectral sequence and its second page”.

## Tag 03F7, a lemma

[Tag 03F7](https://stacks.math.columbia.edu/tag/03F7) in the Stacks Project.

**`Stacks.CechSite.Acyclic.isIso_cechCohomologyToCohomology_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/AcyclicCoveringFamily.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/AcyclicCoveringFamily.lean#L528).

> **Stacks Project, Tag 03F7.** Let `𝒰 = {U_i → U}` be a covering family of an object of a
> site and let `F` be an abelian sheaf whose higher cohomology vanishes on every nonempty finite
> fibre product `U_{i_0} ×_U ⋯ ×_U U_{i_r}` of members of the family. Then the canonical
> comparison of [Stacks, Tag 03AX]
>
> ```
> Ȟ^p(𝒰, F) ⟶ H^p(U, F)
> ```
>
> is an isomorphism in every degree `p`: the Čech cohomology of such a family computes the sheaf
> cohomology of the covered object.

```lean
theorem isIso_cechCohomologyToCohomology_app (F : Sheaf K Ab.{max u v})
    (hacyclic : ∀ (r : ℕ) (s : Fin (r + 1) → E.I₀) (q : ℕ), 0 < q →
      IsZero (((tupleSections K E s).rightDerived q).obj F))
    (p : ℤ) :
    IsIso ((cechCohomologyToCohomology.{max u v} K E hE p).app F)
```

**`Stacks.CechSite.Acyclic.cechCohomologyIsoRightDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/AcyclicCoveringFamilyCohomology.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/AcyclicCoveringFamilyCohomology.lean#L90). The attribute's comment: “the conclusion read as an isomorphism between the Cech cohomology group of the family and the j-th right derived sections over the covered object, which is the definition of H^j(U, F) that the acyclicity hypothesis of the tag is stated with”.

> Let `𝒰 = {U_i → U}` be a covering family of an object of a site and let `F` be an abelian
> sheaf whose higher cohomology vanishes on every nonempty finite fibre product
> `U_{i_0} ×_U ⋯ ×_U U_{i_r}` of members of the family. Then
>
> `Ȟ^j(𝒰, F) ≅ H^j(U, F)`
>
> in every degree, the right hand side being the `j`-th right derived functor of sections over `U`.
> The isomorphism is induced by `cechCohomologyToCohomology`.

```lean
def cechCohomologyIsoRightDerivedSections (F : Sheaf K Ab.{max u v})
    (hacyclic : ∀ (r : ℕ) (s : Fin (r + 1) → E.I₀) (q : ℕ), 0 < q →
      IsZero (((tupleSections K E s).rightDerived q).obj F))
    (j : ℕ) :
    cechCohomology E F.obj j ≅
      (((sheafSections K Ab.{max u v}).obj (op U)).rightDerived j).obj F
```

## Tag 03F8, a lemma

[Tag 03F8](https://stacks.math.columbia.edu/tag/03F8) in the Stacks Project.

**`Stacks.CechSite.surjective_on_sections_of_isZero_cechCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/FirstVanishingAndSections.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/FirstVanishingAndSections.lean#L453).

> **Stacks Project, Tag 03F8.** For a short exact sequence of abelian sheaves, vanishing
> of first Čech cohomology of the first sheaf on a cofinal system of coverings makes the last
> map surjective on sections.

```lean
public theorem surjective_on_sections_of_isZero_cechCohomology
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    [HasSheafify J (AddCommGrpCat.{max a w})]
    (S : ShortComplex (Sheaf J (AddCommGrpCat.{max a w}))) (hS : S.ShortExact)
    (U : C) (Cov : Set (PreZeroHypercover.{w} U))
    (hCov : ∀ E ∈ Cov, E.sieve₀ ∈ J U)
    (hcofinal : ∀ R ∈ J U, ∃ E : PreZeroHypercover.{w} U,
      E ∈ Cov ∧ E.sieve₀ ≤ R)
    (hproducts : ∀ (E : PreZeroHypercover.{w} U), E ∈ Cov →
      ∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
        HasProduct (fun a ↦ Over.mk (E.f (i a))))
    (hH1 : ∀ (E : PreZeroHypercover.{w} U) (hE : E ∈ Cov),
      letI := hproducts E hE
      IsZero (cechCohomology E
        ((sheafToPresheaf J (AddCommGrpCat.{max a w})).obj S.X₁) 1)) :
    Function.Surjective
      (((sheafToPresheaf J (AddCommGrpCat.{max a w})).map S.g).app (op U))
```

## Tag 03F9, a lemma

[Tag 03F9](https://stacks.math.columbia.edu/tag/03F9) in the Stacks Project.

**`Stacks.CechSite.subsingleton_ext_of_cechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean#L159). The attribute's comment: “the coefficient universe contains the objects of the site, which replaces the hypothesis that the site be small with morphisms in the coefficient universe”.

> **Stacks Project, Tag 03F9, with the morphism universe of the site free.** If a cofinal
> collection of coverings of a collection of objects has all its nonempty finite fibre products in
> that collection, then vanishing of positive-degree Čech cohomology on those coverings implies
> vanishing of positive-degree cohomology over every object in the collection.
>
> Cohomology over `U` is `Ext` out of the sheafification of the free abelian presheaf on the
> representable presheaf of `U`, lifted to the coefficient universe. The coefficient universe
> contains the object universe of the site, which is what makes Stacks 03OR available for an
> injective abelian presheaf and what replaces the hypothesis that the site be small.

```lean
theorem subsingleton_ext_of_cechCohomology_isZero
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (F : Sheaf J AddCommGrpCat.{max a u v w})
    (hCech : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ), 0 < p →
        letI : ∀ (q : ℕ) (i : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (i a))) := hProducts E hE
        IsZero (cechCohomology E.1 F.obj p))
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    Subsingleton (Ext ((presheafToSheaf J AddCommGrpCat.{max a u v w}).obj
      (uliftYoneda.{max a u v w}.obj U ⋙ AddCommGrpCat.free)) F p)
```

**`Stacks.CechSite.sheafCohomology_isZero_of_cechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingOnCofinalCoverings.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingOnCofinalCoverings.lean#L411).

> **Stacks Project, Tag 03F9.** If a cofinal collection of coverings of a collection of
> objects has all its nonempty finite fibre products in that collection, then vanishing of
> positive-degree Čech cohomology on those coverings implies vanishing of positive-degree sheaf
> cohomology on every object in the collection.

```lean
public theorem sheafCohomology_isZero_of_cechCohomology_isZero
    {C : Type u} [Category.{max v w} C] [Small.{max v w} C] (J : GrothendieckTopology C)
    [HasSheafify J AddCommGrpCat.{max v w}]
    [HasExt.{x} (Sheaf J AddCommGrpCat.{max v w})]
    (B : Set C)
    (Cov : ∀ U : C,
      Set { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U })
    (hProducts : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
      E ∈ Cov U → ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        HasProduct (fun a ↦ Over.mk (E.1.f (i a))))
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (F : Sheaf J AddCommGrpCat.{max v w})
    (hCech : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ), 0 < p →
        letI : ∀ (q : ℕ) (i : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (i a))) := hProducts E hE
        IsZero (cechCohomology E.1 F.obj p))
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    IsZero (Sheaf.H' F p U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.10, Tag 03AV](https://stacks.math.columbia.edu/tag/03AV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
