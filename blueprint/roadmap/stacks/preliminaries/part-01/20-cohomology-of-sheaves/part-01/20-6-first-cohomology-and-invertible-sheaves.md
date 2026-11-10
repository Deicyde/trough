---
declaration: section
origin: cited
lean: Stacks.Cohomology.Generators.generatorTorsorOfInvertible, Stacks.Cohomology.Generators.h1UnitsAddEquivPicardGroup, Stacks.Cohomology.Generators.h1UnitsAddEquivPicardGroup_symm_classOf
statement: formalized
proof: formalized
---

# 20.6 First cohomology and invertible sheaves

Section 20.6 of the Stacks Project, [Tag 09NT](https://stacks.math.columbia.edu/tag/09NT). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09NU, a lemma

[Tag 09NU](https://stacks.math.columbia.edu/tag/09NU) in the Stacks Project.

**`Stacks.Cohomology.Generators.generatorTorsorOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/GeneratorTorsorOfAnInvertibleModule.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/GeneratorTorsorOfAnInvertibleModule.lean#L71). The attribute's comment: “the generator torsor”. References: EGA IV (21.13.13), “special case”.

> The sections of an invertible module `L` that trivialize it form a sheaf of sets on which
> the sheaf of units acts simply transitively: the *generator torsor* of `L`.  The identification
> of its sections with the trivializing sections of `L`, and the compatibility of that
> identification with restriction and with the action of units, are part of the data.

```lean
def generatorTorsorOfInvertible (X : RingedSpace.{u, u})
    [∀ x : X, IsLocalRing (X.presheaf.stalk x)]
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj
      (structureSheaf X.sheaf).property L) :
    GeneratorTorsor X L
```

**`Stacks.Cohomology.Generators.h1UnitsAddEquivPicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PicardGroupAndFirstCohomology.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PicardGroupAndFirstCohomology.lean#L294). The attribute's comment: “the additive equivalence”. References: EGA 0 (5.4.7), “special case”; EGA IV (21.3.6), “special case”; SGA 4½ Arcata (2.2.3), “ringed space case”; SGA 1 XI (6.4), “more general”; SGA 3 VIII (4.4), “Pic(S) ≅ H¹(S, O_S^×)”.

> For a ringed space all of whose stalks are local rings, the first cohomology of the sheaf of
> units is canonically isomorphic, as an abelian group, to the Picard group.

```lean
def h1UnitsAddEquivPicardGroup :
    Stacks.Cohomology.SheafTorsor.sheafCohomologyOne X (unitsSheaf X) ≃+
      Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
        (structureSheaf X.sheaf).property
```

**`Stacks.Cohomology.Generators.h1UnitsAddEquivPicardGroup_symm_classOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PicardGroupAndFirstCohomology.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PicardGroupAndFirstCohomology.lean#L304). The attribute's comment: “characterization by generator torsors”.

> The inverse of the canonical isomorphism `H^1(X, 𝒪_X^*) ≅ Pic(X)` sends the class of an
> invertible module to the first-cohomology class of its torsor of generators.

```lean
theorem h1UnitsAddEquivPicardGroup_symm_classOf
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj
      (structureSheaf X.sheaf).property L) :
    (h1UnitsAddEquivPicardGroup X).symm (Stacks.SheafOfModules.Picard.classOf X.sheaf.obj
        (structureSheaf X.sheaf).property L hL) =
      Stacks.Cohomology.SheafTorsor.torsorClassEquivSheafCohomologyOne X (unitsSheaf X)
        (Quotient.mk _ (generatorTorsorOfInvertible X L hL).toTorsor)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.6, Tag 09NT](https://stacks.math.columbia.edu/tag/09NT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
