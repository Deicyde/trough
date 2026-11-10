---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.Crystals.isColimit_cardinalGeneratedSubcrystalCocone, Stacks.AlgebraicGeometry.Crystals.isFiltered_cardinalGeneratedSubcrystal, AlgebraicGeometry.Space.QuasicoherentModule.exists_generating_family
statement: formalized
proof: formalized
---

# 78.14 Crystals in quasi-coherent sheaves

Section 78.14 of the Stacks Project, [Tag 077Y](https://stacks.math.columbia.edu/tag/077Y). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 077Z, a lemma

[Tag 077Z](https://stacks.math.columbia.edu/tag/077Z) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Crystals.isColimit_cardinalGeneratedSubcrystalCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CrystalFamilyTransport.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CrystalFamilyTransport.lean#L286). The attribute's comment: “the colimit”.

> **Stacks 077Z, the colimit assertion.**  For the cardinal `cardinalBound D`, which depends
> only on the system of schemes and not on the crystal, every crystal in quasi-coherent modules on
> a flat system of schemes is the colimit of its `cardinalBound D`-generated submodules.
>
> Together with `Stacks.AlgebraicGeometry.Crystals.isFiltered_cardinalGeneratedSubcrystal`, which
> says that those submodules form a directed system, this is the whole of the tag: there is a
> cardinal `κ` such that every object of `CQC(X)` is the directed colimit of its `κ`-generated
> submodules.

```lean
def isColimit_cardinalGeneratedSubcrystalCocone (D : SchemeSystem.{u}) [D.IsFlat]
    (M : Crystal D) : IsColimit (cardinalGeneratedSubcrystalCocone M (cardinalBound D))
```

**`Stacks.AlgebraicGeometry.Crystals.isFiltered_cardinalGeneratedSubcrystal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CrystalsInQuasicoherentModules.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CrystalsInQuasicoherentModules.lean#L514). The attribute's comment: “the directed system”.

> **Stacks 077Z, the directedness half.**  For the cardinal `cardinalBound D`, which depends
> only on the system of schemes and not on the crystal, the `cardinalBound D`-generated submodules
> of every crystal on a flat system form a directed system.
>
> This is one of the two declarations carrying the tag; the other,
> `Stacks.AlgebraicGeometry.Crystals.isColimit_cardinalGeneratedSubcrystalCocone`, says that the
> crystal is the colimit of that system.  Together they are the whole statement: for this `κ`
> every object of `CQC(X)` is the directed colimit of its `κ`-generated submodules.

```lean
instance isFiltered_cardinalGeneratedSubcrystal (D : SchemeSystem.{u}) [D.IsFlat]
    (M : Crystal D) : IsFiltered (CardinalGeneratedSubcrystal M (cardinalBound D))
```

## Tag 0780, a lemma

[Tag 0780](https://stacks.math.columbia.edu/tag/0780) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.exists_generating_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentGenerators.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentGenerators.lean#L90).

> **Stacks 0780.**  For a groupoid in algebraic spaces with flat source and target there is a
> family of quasi-coherent modules on the groupoid, independent of the module, such that every
> quasi-coherent module on the groupoid is the directed colimit of those of its submodules that
> are isomorphic to a member of the family.

```lean
theorem exists_generating_family (G : GroupoidInAlgebraicSpaces B S hS A)
    (_hs : IsFlat B S hS G.source.hom) (_ht : IsFlat B S hS G.target.hom) :
    ∃ (T : Type (u + 1)) (F : T → QuasicoherentModule B S hS G),
      ∀ M : QuasicoherentModule B S hS G,
        IsFiltered (IsomorphicGeneratorSubobject T F M) ∧
          Nonempty (IsColimit (isomorphicGeneratorSubobjectCocone T F M))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.14, Tag 077Y](https://stacks.math.columbia.edu/tag/077Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
