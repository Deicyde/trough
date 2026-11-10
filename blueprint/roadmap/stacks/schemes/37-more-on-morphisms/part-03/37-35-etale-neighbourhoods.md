---
declaration: section
origin: cited
lean: AlgebraicGeometry.EtaleNeighborhood, AlgebraicGeometry.EtaleNeighborhood.Hom, AlgebraicGeometry.EtaleNeighborhood.IsElementary, AlgebraicGeometry.exists_etaleNeighborhood_residueField_algEquiv, AlgebraicGeometry.exists_common_refinement, AlgebraicGeometry.exists_equalizing_refinement, Stacks.EtaleCohomology.isCofiltered_elementaryEtaleNeighborhood, AlgebraicGeometry.instIsFilteredOppositeElementaryEtaleNeighborhood
statement: formalized
proof: formalized
---

# 37.35 Étale neighbourhoods

Section 37.35 of the Stacks Project, [Tag 02LD](https://stacks.math.columbia.edu/tag/02LD). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02LE, a definition

[Tag 02LE](https://stacks.math.columbia.edu/tag/02LE) in the Stacks Project.

**`AlgebraicGeometry.EtaleNeighborhood`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean#L62). The attribute's comment: “part (1)”.

> An *étale neighbourhood* of a scheme `S` at a point `s` is a scheme which is étale over `S`,
> together with a distinguished point lying over `s`.

```lean
structure EtaleNeighborhood (S : Scheme.{u}) (s : S)
```

**`AlgebraicGeometry.EtaleNeighborhood.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean#L82). The attribute's comment: “part (2)”.

> A morphism of étale neighbourhoods of `(S, s)` is a morphism of schemes over `S` which
> carries the distinguished point to the distinguished point.

```lean
structure Hom (U V : EtaleNeighborhood S s)
```

**`AlgebraicGeometry.EtaleNeighborhood.IsElementary`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleNeighborhood.lean#L127). The attribute's comment: “part (3)”.

> An étale neighbourhood is *elementary* if the induced extension of residue fields is
> trivial.

```lean
abbrev IsElementary (U : EtaleNeighborhood S s) : Prop
```

## Tag 02LF, a lemma

[Tag 02LF](https://stacks.math.columbia.edu/tag/02LF) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_residueField_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ResidueField.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ResidueField.lean#L133). References: EGA IV (18.8.6), “more general”; SGA 2 XIV (3.4).

> **Stacks Project, Tag 02LF.** Every finite separable extension of the
> residue field at a point is realized by the residue field at the chosen point
> of an étale neighborhood.

```lean
theorem exists_etaleNeighborhood_residueField_algEquiv
    (S : Scheme.{u}) (s : S) (k : Type v) [Field k]
    [Algebra (S.residueField s) k]
    [Module.Finite (S.residueField s) k]
    [Algebra.IsSeparable (S.residueField s) k] :
    ∃ U : EtaleNeighborhood S s,
      letI := U.residueFieldMap.hom.toAlgebra
      Nonempty (U.scheme.residueField U.point ≃ₐ[S.residueField s] k)
```

## Tag 057A, a lemma

[Tag 057A](https://stacks.math.columbia.edu/tag/057A) in the Stacks Project.

**`AlgebraicGeometry.exists_common_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Refinement.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Refinement.lean#L68). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 057A, part (1).** Two étale neighborhoods of a point
> admit a common refinement.

```lean
theorem exists_common_refinement {S : Scheme.{u}} {s : S}
    (U V : EtaleNeighborhood S s) :
    ∃ W : EtaleNeighborhood S s, Nonempty ((W ⟶ U) × (W ⟶ V))
```

**`AlgebraicGeometry.exists_equalizing_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Refinement.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Refinement.lean#L144). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 057A, part (2).** Two neighborhood maps which induce
> the same map on residue fields become equal after a refinement.

```lean
theorem exists_equalizing_refinement (f g : U ⟶ V)
    (hκ : (V.scheme.residueFieldCongr f.map_point).inv ≫
        f.hom.residueFieldMap U.point =
      (V.scheme.residueFieldCongr g.map_point).inv ≫
        g.hom.residueFieldMap U.point) :
    ∃ W : EtaleNeighborhood S s, ∃ h : W ⟶ U, h ≫ f = h ≫ g
```

## Tag 057B, a lemma

[Tag 057B](https://stacks.math.columbia.edu/tag/057B) in the Stacks Project.

**`Stacks.EtaleCohomology.isCofiltered_elementaryEtaleNeighborhood`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleStalk/ElementaryFiber.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleStalk/ElementaryFiber.lean#L288).

> **Stacks 057B.** The category of elementary étale neighbourhoods of a point of a scheme is
> cofiltered: two neighbourhoods are dominated by their fibre product and two morphisms of
> elementary neighbourhoods are equalized after a refinement, both by Tag 057A.

```lean
public instance isCofiltered_elementaryEtaleNeighborhood (X : Scheme.{u}) (x : X) :
    IsCofiltered (ElementaryEtaleNeighborhood X x)
```

## Tag 05KS, a lemma

[Tag 05KS](https://stacks.math.columbia.edu/tag/05KS) in the Stacks Project.

**`AlgebraicGeometry.instIsFilteredOppositeElementaryEtaleNeighborhood`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean, line 1253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean#L1253). The attribute's comment: “the indexing category is filtered”. References: EGA IV (18.6.3), “more general”.

> **Stacks Project, Tag 05KS.** The opposite of the category of elementary
> étale neighborhoods of a point is filtered.

```lean
instance instIsFilteredOppositeElementaryEtaleNeighborhood
    (S : Scheme.{u}) (s : S) :
    IsFiltered (ElementaryEtaleNeighborhood S s)ᵒᵖ
```

**`AlgebraicGeometry.isColimit_globalSections`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean#L1354). The attribute's comment: “the henselization is the colimit”.

> **Stacks Project, Tag 05KS.** A henselization of the local ring of a
> scheme at a point is a colimit of the rings of global sections of its
> elementary étale neighborhoods.

```lean
lemma isColimit_globalSections (S : Scheme.{u}) (s : S)
    (Rh : Type u) [CommRing Rh] [IsLocalRing Rh]
    [Algebra (S.presheaf.stalk s) Rh]
    [IsLocalRing.IsHenselization (S.presheaf.stalk s)
      (IsLocalRing.ResidueField (S.presheaf.stalk s)) Rh] :
    ∃ ι : globalSections S s ⟶
        (Functor.const _).obj (CommRingCat.of Rh),
      (∀ U x, IsLocalRing.residue Rh ((ι.app U).hom x) =
        henselizationResidueFieldMap S s Rh
          (elementaryEtaleAugmentation S s U.unop x)) ∧
      (∀ U : (ElementaryEtaleNeighborhood S s)ᵒᵖ,
        IsOverStalk S s Rh U.unop (ι.app U).hom) ∧
      (∀ ι' : globalSections S s ⟶ (Functor.const _).obj (CommRingCat.of Rh),
        (∀ U x, IsLocalRing.residue Rh ((ι'.app U).hom x) =
          henselizationResidueFieldMap S s Rh
            (elementaryEtaleAugmentation S s U.unop x)) →
        (∀ U : (ElementaryEtaleNeighborhood S s)ᵒᵖ,
          IsOverStalk S s Rh U.unop (ι'.app U).hom) → ι' = ι) ∧
      Nonempty (IsColimit (Cocone.mk _ ι))
```

## Tag 0CAS, a lemma

[Tag 0CAS](https://stacks.math.columbia.edu/tag/0CAS) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_fiber_openImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberLifting.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberLifting.lean#L455).

> **Stacks Project, Tag 0CAS.** An étale neighborhood on a fiber can be
> refined by an open immersion from the fiber of an étale neighborhood on the
> total space.

```lean
public theorem exists_etaleNeighborhood_fiber_openImmersion
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (V : EtaleNeighborhood (f.fiber (f x)) (f.asFiber x)) :
    ∃ (U : EtaleNeighborhood X x)
      (u : (U.toBase ≫ f).fiber (f x))
      (p : (U.toBase ≫ f).fiber (f x) ⟶ f.fiber (f x))
      (h : (U.toBase ≫ f).fiber (f x) ⟶ V.scheme),
      (U.toBase ≫ f).fiberι (f x) u = U.point ∧
      p ≫ f.fiberι (f x) = (U.toBase ≫ f).fiberι (f x) ≫ U.toBase ∧
      Etale p ∧
      p u = f.asFiber x ∧
      h ≫ V.toBase = p ∧
      h u = V.point ∧
      IsOpenImmersion h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.35, Tag 02LD](https://stacks.math.columbia.edu/tag/02LD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
