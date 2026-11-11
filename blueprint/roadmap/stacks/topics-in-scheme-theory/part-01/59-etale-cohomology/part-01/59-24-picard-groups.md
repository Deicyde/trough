---
declaration: section
origin: cited
lean: Stacks.Kummer.etaleH1MultiplicativeAddEquivPicard, Stacks.Picard.AllTopologies.identifications, Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup, Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup_symm_classOf, Stacks.Picard.FirstCohomology.h1UnitsAddEquivPicard, Stacks.Picard.FirstCohomology.h1UnitsAddEquivPicard_symm_classOf
statement: formalized
proof: formalized
---

# 59.24 Picard groups

Section 59.24 of the Stacks Project, [Tag 03P7](https://stacks.math.columbia.edu/tag/03P7). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03P8, a theorem

[Tag 03P8](https://stacks.math.columbia.edu/tag/03P8) in the Stacks Project.

**`Stacks.Kummer.etaleH1MultiplicativeAddEquivPicard`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Picard/MultiplicativeFirstCohomology.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Picard/MultiplicativeFirstCohomology.lean#L207). The attribute's comment: “the étale identification H¹\_étale(X, 𝐆\_m) = Pic(X), for every scheme X; the fppf, syntomic and smooth identifications are not covered”. References: SGA 4 IX (3.3); SGA 4 XII (8.6); SGA 4½ Arcata (2.2.3); SGA 4½ Arcata (3.3.1), “more general”.

> **Stacks Project, Tag 03P8, the étale identification.** For any scheme `X`, the first étale
> cohomology of the multiplicative group is the Picard group: `H¹_étale(X, 𝐆_m) = Pic(X)`.
>
> The identification is the composite of the canonical ones: restriction to a size-bounded small
> étale site (Tag 00XU), the identification of `H¹` of the units of the small étale ringed site with
> its Picard group (Tag 040E), and the identification of that Picard group with `Pic(X)` by
> `𝓕 ↦ 𝓕^a` (Tag 03DX (2)); the coefficient universe of `𝐆_m` is immaterial for `H¹`.

```lean
noncomputable def etaleH1MultiplicativeAddEquivPicard
    [HasExt.{w} (Sheaf S.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    Sheaf.H.{w} (multiplicativeSheaf.{u, v} S) 1 ≃+ Stacks.Picard.ofScheme S
```

**`Stacks.Picard.AllTopologies.identifications`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/MultiplicativeGroupFirstCohomology.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/MultiplicativeGroupFirstCohomology.lean#L217). References: SGA 1 XI (5.3), “G\_m clause, special case”; SGA 1 XI (6.4), “picardSpace field”; SGA 3 VIII (4.4), “partial”; SGA 4 VII (4.2.1), “special case”; SGA 4 XII (8.6), “more general”; SGA 4½ Arcata (3.3.1), “more general”.

> **Stacks Project, Tag 03P8.** For any scheme `X` there are canonical identifications
>
> `H¹\_fppf(X, 𝐆\_m) = H¹\_syntomic(X, 𝐆\_m) = H¹\_smooth(X, 𝐆\_m) = H¹\_étale(X, 𝐆\_m)
>   = H¹\_Zar(X, 𝐆\_m) = Pic(X) = H¹(X, 𝒪\_X^*)`.
>
> The five big-site groups are identified with `Pic(X)` by
> `Stacks.Picard.AllTopologies.baseH1UnitsAddEquivSchemePicardGroup`, which is Tag 040E on the big
> `τ`-site followed by clause (1) of Descent, Proposition 03DX at `τ` read on Picard groups; the
> last link is Tag 040E on the site of opens of `X`,
> `Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup`.
>
> Every identification is normalized on invertible modules:
> `Stacks.Picard.AllTopologies.baseH1UnitsAddEquivSchemePicardGroup_symm_classOf` and
> `Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup_symm_classOf` send the class of an
> invertible module to the first cohomology class of its torsor of local generators, and the six
> `identifications_*` lemmas below express each field in those terms.

```lean
public def identifications : Identifications.{t} B X hX
```

**`Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean#L109). The attribute's comment: “the identification H¹\_Zar(X, 𝐆\_m) = Pic(X); the four comparisons of H¹\_fppf, H¹\_syntomic, H¹\_smooth and H¹\_étale with H¹\_Zar are not covered”.

> **Stacks Project, Tag 03P8, the Zariski identification.** For any scheme `X` there is a
> canonical isomorphism of abelian groups `H¹_{Zar}(X, 𝐆_m) = Pic(X)`.

```lean
def zariskiH1UnitsAddEquivPicardGroup :
    Sheaf.H (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (schemeRingedSite X)) 1 ≃+
      Stacks.SheafOfModules.Picard.PicardGroup (schemeRingedSite X).O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf (schemeRingedSite X).O).2
```

**`Stacks.Picard.ZariskiSite.zariskiH1UnitsAddEquivPicardGroup_symm_classOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean#L120). The attribute's comment: “the Zariski identification is the canonical one, normalized on line bundles”.

> **Stacks Project, Tag 03P8, the Zariski identification is the canonical one.** Its inverse
> sends the class of an invertible module to the first cohomology class of its torsor of local
> generators.

```lean
theorem zariskiH1UnitsAddEquivPicardGroup_symm_classOf
    (L : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (schemeRingedSite X).O))
    (hL : Stacks.SheafOfModules.IsInvertible (schemeRingedSite X).O.obj
      (Stacks.SheafOfModules.Tensor.ringSheaf (schemeRingedSite X).O).2 L) :
    (zariskiH1UnitsAddEquivPicardGroup X).symm
        (Stacks.SheafOfModules.Picard.classOf (schemeRingedSite X).O.obj
          (Stacks.SheafOfModules.Tensor.ringSheaf (schemeRingedSite X).O).2 L hL) =
      Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1
        (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (schemeRingedSite X))
        (Quotient.mk (Stacks.Cohomology.Torsors.torsorSetoid
            (Stacks.Cohomology.Torsors.Generators.unitsAddSheaf (schemeRingedSite X)))
          (Stacks.Cohomology.Torsors.Generators.generatorTorsor (schemeRingedSite X)
            (schemeRingedSite_isLocallyRinged X) L hL).torsor)
```

Declarations registered for the tag:

- [`Stacks.Picard.FirstCohomology.h1UnitsAddEquivPicard`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/FirstCohomologyNaturality.lean#L552), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean#L144) (StacksFrontier): “the identification Pic(X) = H¹(X, 𝒪\_X^*)”.
- [`Stacks.Picard.FirstCohomology.h1UnitsAddEquivPicard_symm_classOf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/FirstCohomologyNaturality.lean#L557), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/ZariskiSiteFirstCohomology.lean#L147) (StacksFrontier): “the identification Pic(X) = H¹(X, 𝒪\_X^*) is the canonical one”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.24, Tag 03P7](https://stacks.math.columbia.edu/tag/03P7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
