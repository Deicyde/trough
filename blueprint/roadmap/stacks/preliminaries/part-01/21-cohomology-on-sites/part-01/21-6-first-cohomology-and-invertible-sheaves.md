---
declaration: section
origin: cited
lean: Stacks.Picard.SmallEtaleSite.etaleH1UnitsAddEquivPicardGroup, Stacks.Picard.SmallEtaleSite.etaleH1UnitsAddEquivPicardGroup_symm_classOf, AlgebraicGeometry.Space.h1UnitsAddEquivPicardGroup, Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroupOfEssentiallySmall, Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup, Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup'
statement: formalized
proof: formalized
---

# 21.6 First cohomology and invertible sheaves

Section 21.6 of the Stacks Project, [Tag 040D](https://stacks.math.columbia.edu/tag/040D). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 040E, a lemma

[Tag 040E](https://stacks.math.columbia.edu/tag/040E) in the Stacks Project.

**`Stacks.Picard.SmallEtaleSite.etaleH1UnitsAddEquivPicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/SmallEtaleSiteFirstCohomology.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/SmallEtaleSiteFirstCohomology.lean#L83). The attribute's comment: “the identification H¹\_étale(S, 𝐆\_m) = Pic(𝒪\_étale), on the small étale site”.

> **Stacks Project, Tag 040E, at `τ = étale` on the small site.** For a scheme `S` in a big
> étale site containing it there is a canonical isomorphism of abelian groups
> `H¹_{étale}(S, 𝐆_m) = Pic(𝒪_étale)`.

```lean
def etaleH1UnitsAddEquivPicardGroup :
    Sheaf.H
        (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (smallEtaleRingedSite B S hS)) 1 ≃+
      Stacks.SheafOfModules.Picard.PicardGroup (smallEtaleRingedSite B S hS).O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O).2
```

**`Stacks.Picard.SmallEtaleSite.etaleH1UnitsAddEquivPicardGroup_symm_classOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/SmallEtaleSiteFirstCohomology.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/SmallEtaleSiteFirstCohomology.lean#L95). The attribute's comment: “the étale identification is normalized on invertible modules”.

> **Stacks Project, Tag 040E at `τ = étale`, the identification is the canonical one.** Its
> inverse sends the class of an invertible `𝒪_étale`-module to the first cohomology class of its
> torsor of local generators.

```lean
theorem etaleH1UnitsAddEquivPicardGroup_symm_classOf
    (L : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O))
    (hL : Stacks.SheafOfModules.IsInvertible (smallEtaleRingedSite B S hS).O.obj
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O).2 L) :
    (etaleH1UnitsAddEquivPicardGroup B S hS).symm
        (Stacks.SheafOfModules.Picard.classOf (smallEtaleRingedSite B S hS).O.obj
          (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O).2 L hL) =
      Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1
        (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (smallEtaleRingedSite B S hS))
        (Quotient.mk (Stacks.Cohomology.Torsors.torsorSetoid
            (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (smallEtaleRingedSite B S hS)))
          (Stacks.Cohomology.Torsors.Generators.generatorTorsor' (smallEtaleRingedSite B S hS)
            (smallEtaleRingedSite_isLocallyRinged B S hS) L hL).torsor)
```

**`AlgebraicGeometry.Space.h1UnitsAddEquivPicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardGroupFirstCohomology.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PicardGroupFirstCohomology.lean#L73). The attribute's comment: “for the small étale site of an algebraic space”.

> **Stacks 040E for an algebraic space.** The first cohomology of the sheaf of units on the
> small étale site of an algebraic space `Z` is the Picard group of `Z`.

```lean
def h1UnitsAddEquivPicardGroup :
    Sheaf.H.{u + 1} (unitsAddSheafEtale B S hS Z) 1 ≃+ picardGroup Z
```

**`Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroupOfEssentiallySmall`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupEssentiallySmall.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupEssentiallySmall.lean#L81). The attribute's comment: “on an essentially small ringed site, with the universe of the sections of the structure sheaf independent of the universes of the site”.

> **Stacks Project, Tag 040E on an essentially small ringed site.** Let `(C, O)` be a locally
> ringed site whose underlying category is essentially small at the universe of the sections of
> `O`. There is a canonical isomorphism of abelian groups `H^1(C, O^*) = Pic(O)`.
>
> This is `Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup` with the three
> universes of the ringed site independent.

```lean
def h1UnitsAddEquivPicardGroupOfEssentiallySmall
    (hX : AlgebraicGeometry.RingedSite.IsLocallyRinged X) :
    Sheaf.H.{a} (unitsAddSheaf X) 1 ≃+
      Stacks.SheafOfModules.Picard.PicardGroup X.O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O).2
```

**`Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupOfARingedSite.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupOfARingedSite.lean#L702). References: SGA 3 VIII (4.4), “Pic ≅ H¹(O*)”; SGA 4½ Arcata (2.2.3).

> **Stacks Project, Tag 040E.** Let `(C, O)` be a locally ringed site. There is a canonical
> isomorphism of abelian groups `H^1(C, O^*) = Pic(O)`.

```lean
def h1UnitsAddEquivPicardGroup :
    Sheaf.H (unitsAddSheaf X) 1 ≃+
      Stacks.SheafOfModules.Picard.PicardGroup X.O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O).2
```

**`Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupOfARingedSiteGeneral/H1UnitsPicardGroup.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PicardGroupOfARingedSiteGeneral/H1UnitsPicardGroup.lean#L659). The attribute's comment: “with the three universes of the ringed site independent, on a site essentially small at the universe of the sections of the structure sheaf”.

> **Stacks Project, Tag 040E.** Let `(C, O)` be a locally ringed site. There is a canonical
> isomorphism of abelian groups `H^1(C, O^*) = Pic(O)`.
>
> This generalizes `Stacks.Cohomology.Torsors.Generators.h1UnitsAddEquivPicardGroup`,
> stated for `RingedSite.{u, u, u}`, to independent universes.

```lean
def h1UnitsAddEquivPicardGroup' :
    Sheaf.H (unitsAddSheaf X) 1 ≃+
      Stacks.SheafOfModules.Picard.PicardGroup X.O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O).2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.6, Tag 040D](https://stacks.math.columbia.edu/tag/040D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
