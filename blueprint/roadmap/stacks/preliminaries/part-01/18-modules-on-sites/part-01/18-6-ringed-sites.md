---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.HomGeneral.comp, AlgebraicGeometry.RingedSite, AlgebraicGeometry.RingedSite.Hom, AlgebraicGeometry.RingedSite.Hom.comp
statement: formalized
proof: formalized
---

# 18.6 Ringed sites

Section 18.6 of the Stacks Project, [Tag 04KQ](https://stacks.math.columbia.edu/tag/04KQ). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03AD, a definition

[Tag 03AD](https://stacks.math.columbia.edu/tag/03AD) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.HomGeneral.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/CompositionGeneral.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/CompositionGeneral.lean#L63). The attribute's comment: “part (3): composition of morphisms of ringed sites, at independent universes”.

> **Stacks 03AD, part (3), at independent universes.**  Composition of morphisms of ringed
> sites.  On structure sheaves it is `𝒪_Z ⟶ g_*𝒪_Y ⟶ g_*f_*𝒪_X ≅ (g ∘ f)_*𝒪_X`.

```lean
public noncomputable def HomGeneral.comp (f : HomGeneral X Y) (g : HomGeneral Y Z) :
    HomGeneral X Z
```

**`AlgebraicGeometry.RingedSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean#L60). The attribute's comment: “part (1): ringed sites”. References: SGA 4 IV (11.1.1), “ringed site”.

> A ringed site is a category with a Grothendieck topology and a sheaf of commutative
> rings.

```lean
structure RingedSite
```

**`AlgebraicGeometry.RingedSite.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean#L77). The attribute's comment: “part (2): morphisms of ringed sites”. References: SGA 4 IV (13.3).

> A morphism of ringed sites. The functor `u : Y.C ⥤ X.C` represents the underlying morphism
> of sites `X ⟶ Y`, and `fsharp` is its structure map in direct-image form.

```lean
structure Hom (X Y : RingedSite.{u, u, w})
```

**`AlgebraicGeometry.RingedSite.Hom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedSite.lean#L107). The attribute's comment: “part (3): composition of morphisms of ringed sites”.

> Composition of morphisms of ringed sites. On structure sheaves this is
> `O_Z ⟶ g_* O_Y ⟶ g_* f_* O_X ≅ (g ∘ f)_* O_X`.

```lean
noncomputable def Hom.comp {X Y Z : RingedSite.{u, u, w}} (f : Hom X Y) (g : Hom Y Z) :
    Hom X Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.6, Tag 04KQ](https://stacks.math.columbia.edu/tag/04KQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
