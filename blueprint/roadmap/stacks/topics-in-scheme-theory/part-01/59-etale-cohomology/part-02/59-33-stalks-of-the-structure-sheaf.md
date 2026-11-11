---
declaration: section
origin: cited
lean: AlgebraicGeometry.structureSheafStalkFromLocalRing, AlgebraicGeometry.structureSheafStalkToGeometricField, AlgebraicGeometry.structureSheafStalkFromLocalRing_germ, AlgebraicGeometry.structureSheafStalkToGeometricField_ι, AlgebraicGeometry.etaleLocalRing_strictHenselization_canonical, AlgebraicGeometry.etaleLocalRing_strictHenselization_unique, AlgebraicGeometry.isConstant_smallEtalePullbackAb_strictHenselization, AlgebraicGeometry.Space.geometricEval
statement: formalized
proof: formalized
---

# 59.33 Stalks of the structure sheaf

Section 59.33 of the Stacks Project, [Tag 04HW](https://stacks.math.columbia.edu/tag/04HW). 4 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04HX, a lemma

[Tag 04HX](https://stacks.math.columbia.edu/tag/04HX) in the Stacks Project.

**`AlgebraicGeometry.structureSheafStalkFromLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L197). The attribute's comment: “the ordinary-to-étale germ map”.

> The canonical map from the ordinary local ring to the stalk of the
> ring-valued étale structure sheaf.

```lean
public noncomputable def structureSheafStalkFromLocalRing
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S) :
    S.presheaf.stalk (s.hom (closedPoint s.residueField)) →+*
      ↥(etaleStalk B S hS s
        (SmallEtale.structureSheaf B S hS).obj)
```

**`AlgebraicGeometry.structureSheafStalkToGeometricField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L265). The attribute's comment: “the geometric evaluation map”.

> Evaluation of a structure-sheaf stalk germ in the geometric residue field.

```lean
public noncomputable def structureSheafStalkToGeometricField
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S) :
    ↥(etaleStalk B S hS s
      (SmallEtale.structureSheaf B S hS).obj) →+* s.residueField
```

**`AlgebraicGeometry.structureSheafStalkFromLocalRing_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L585). The attribute's comment: “compatibility with ordinary germs”.

> The canonical ordinary-to-étale germ map is characterized at every
> étale neighborhood by ordinary restriction of sections.

```lean
public theorem structureSheafStalkFromLocalRing_germ
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S)
    (U : (geometricPointFiber B S hS s).Elementsᵒᵖ)
    (r : S.presheaf.stalk (s.hom (closedPoint s.residueField)))
    (a : Γ((SmallEtale.toScheme B S hS).obj U.unop.1, ⊤)) :
    let f : ((SmallEtale.toScheme B S hS).obj U.unop.1) ⟶ S :=
      B.inclusion.map U.unop.1.obj.hom
    let p := U.unop.2.1
    let x := p (closedPoint s.residueField)
    let h : f x = s.hom (closedPoint s.residueField) :=
      (Scheme.Hom.comp_apply p f (closedPoint s.residueField)).symm.trans
        (congrArg (fun q : s.source ⟶ S => q (closedPoint s.residueField)) U.unop.2.2)
    (f.stalkMap x).hom (h.symm ▸ r) =
        ((SmallEtale.toScheme B S hS).obj U.unop.1).presheaf.germ
          ⊤ x trivial a →
      structureSheafStalkFromLocalRing B S hS s r = (colimit.ι
        ((Functor.Elements.π (geometricPointFiber B S hS s)).op ⋙
          (SmallEtale.structureSheaf B S hS).obj) U).hom a
```

**`AlgebraicGeometry.structureSheafStalkToGeometricField_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 654](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L654). The attribute's comment: “geometric evaluation of germs”.

> Evaluation of a germ of the structure sheaf is its value at the chosen
> geometric lift on every étale neighborhood.

```lean
public theorem structureSheafStalkToGeometricField_ι
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S)
    (U : (geometricPointFiber B S hS s).Elementsᵒᵖ) :
    (structureSheafStalkToGeometricField B S hS s).comp ((colimit.ι
      ((Functor.Elements.π (geometricPointFiber B S hS s)).op ⋙
        (SmallEtale.structureSheaf B S hS).obj) U).hom) =
      ((U.unop.2.1).appTop ≫ (Scheme.ΓSpecIso (.of s.residueField)).hom).hom
```

**`AlgebraicGeometry.etaleLocalRing_strictHenselization_canonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L982). The attribute's comment: “the strict-henselization identification”.

> The étale stalk is canonically the strict henselization of the ordinary
> local ring, with its residue field identified with the separable subextension
> of the geometric point's field.

```lean
public noncomputable def etaleLocalRing_strictHenselization_canonical
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S)
    (T : IsLocalRing.HenselizationTower
        (S.presheaf.stalk (s.hom (closedPoint s.residueField)))
        (separableClosure (ResidueField
          (S.presheaf.stalk (s.hom (closedPoint s.residueField))))
          s.residueField)) :
    { e : T.strictHenselization ≃+*
        ↥(etaleStalk B S hS s
          (SmallEtale.structureSheaf B S hS).obj) //
      (∀ r, e (algebraMap
        (S.presheaf.stalk (s.hom (closedPoint s.residueField)))
        T.strictHenselization r) = structureSheafStalkFromLocalRing B S hS s r) ∧
      (∀ a, structureSheafStalkToGeometricField B S hS s (e a) =
        ((T.strictHenselizationResidueEquiv.symm
          (residue T.strictHenselization a) :
            separableClosure (ResidueField
              (S.presheaf.stalk (s.hom (closedPoint s.residueField))))
              s.residueField) : s.residueField)) }
```

**`AlgebraicGeometry.etaleLocalRing_strictHenselization_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean, line 1058](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/EtaleLocalRing.lean#L1058). The attribute's comment: “uniqueness of the canonical identification”.

> The comparison is uniquely determined by the map from the ordinary local
> ring and by the inclusion of the relative separable closure in the geometric
> point's field.

```lean
public theorem etaleLocalRing_strictHenselization_unique
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S)
    (T : IsLocalRing.HenselizationTower
      (S.presheaf.stalk (s.hom (closedPoint s.residueField)))
      (separableClosure (ResidueField
        (S.presheaf.stalk (s.hom (closedPoint s.residueField)))) s.residueField))
    (e : T.strictHenselization ≃+*
      ↥(etaleStalk B S hS s
        (SmallEtale.structureSheaf B S hS).obj))
    (hbase : ∀ r, e (algebraMap
      (S.presheaf.stalk (s.hom (closedPoint s.residueField)))
      T.strictHenselization r) = structureSheafStalkFromLocalRing B S hS s r)
    (hres : ∀ a, structureSheafStalkToGeometricField B S hS s (e a) =
      ((T.strictHenselizationResidueEquiv.symm
        (residue T.strictHenselization a) :
          separableClosure (ResidueField
            (S.presheaf.stalk (s.hom (closedPoint s.residueField))))
            s.residueField) : s.residueField)) :
    e = (etaleLocalRing_strictHenselization_canonical B S hS s T).val
```

**`AlgebraicGeometry.isConstant_smallEtalePullbackAb_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationLocallyConstant.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationLocallyConstant.lean#L150). The attribute's comment: “a locally constant abelian étale sheaf becomes constant on the strict henselization, because every étale covering of a strictly henselian local scheme splits”.

> **A locally constant abelian étale sheaf has constant inverse image on the strict
> henselization.** The inverse image is locally constant by Tag 093R, and over the spectrum of the
> strictly henselian local ring `𝒪^{sh}_{X,x}` a locally constant sheaf is constant, because the
> canonical geometric point there has the final object of the small étale site as an initial étale
> neighbourhood.

```lean
theorem isConstant_smallEtalePullbackAb_strictHenselization
    (G : Sheaf (smallEtaleTopology X) Ab.{u + 1})
    (hG : Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology X) G) :
    Sheaf.IsConstant (smallEtaleTopology (strictHenselization B X hX x))
      ((smallEtalePullbackAb (strictHenselizationToBase B X hX x)).obj G)
```

**`AlgebraicGeometry.Space.geometricEval`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricEvaluation.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricEvaluation.lean#L98). The attribute's comment: “the geometric evaluation map, for an algebraic space”.

> **Evaluation of germs at a geometric point.**  The homomorphism from the étale local ring of
> `F` at `x̄` to the field of `x̄` sending the germ of a regular function on a small étale
> neighbourhood to its value at the chosen lift of `x̄`.

```lean
def geometricEval (x : GeometricPoint B S hS F) :
    ↥(etaleLocalRing B S hS F x) →+* x.val.carrier
```

## Tag 03PS, a definition

[Tag 03PS](https://stacks.math.columbia.edu/tag/03PS) in the Stacks Project.

**`AlgebraicGeometry.etaleLocalRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean#L62). The attribute's comment: “part (1)”. References: SGA 7 I (0.0.4), “strict henselization”; SGA 4 VIII (4.3), “strictly local ring”.

> The étale local ring of `S` at a geometric point `s`: the stalk at `s` of the structure
> sheaf of the small étale site of `S`.

```lean
public abbrev etaleLocalRing (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (s : GeometricPoint S) : RingCat.{u}
```

**`AlgebraicGeometry.henselizationRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean#L74). The attribute's comment: “part (2)”.

> The henselization of the local ring of `S` at a point `x`.

```lean
public abbrev henselizationRing (S : Scheme.{u}) (x : S) : Type u
```

**`AlgebraicGeometry.henselization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SchemeLocalRings.lean#L95). The attribute's comment: “part (4)”.

> The henselization of a scheme at an ordinary point: the spectrum of the henselization of
> its local ring.

```lean
public abbrev henselization (S : Scheme.{u}) (x : S) : Scheme.{u}
```

**`AlgebraicGeometry.strictHenselization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/StrictHenselization.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/StrictHenselization.lean#L166). The attribute's comment: “part (3)”. References: SGA 2 XIV (1.1); SGA 4 VIII (4.3); SGA 4 VIII (7.1), “partial”; SGA 4½ Arcata (2.3.3), “Ỹ = Spec(O\_\{Y”; SGA 4½ Arcata (5.1.1); SGA 4½ Th finitude (2.11); SGA 7 I (0.0.4); SGA 7 XIII (2.1.3), “The scheme X\_(x̄)”; SGA 7 XVI (1.6), “S\_(s̄) only”.

> The strict henselization of a scheme at a geometric point: the spectrum of the étale local
> ring there.

```lean
public abbrev strictHenselization : Scheme.{u}
```

## Tag 04HY, a lemma

[Tag 04HY](https://stacks.math.columbia.edu/tag/04HY) in the Stacks Project.

**`AlgebraicGeometry.instIsFilteredOppositeElementaryEtaleNeighborhood`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean, line 1253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean#L1253). The attribute's comment: “the henselization is the colimit of O(U) over the étale neighbourhoods with κ(s)”. References: EGA IV (18.6.3), “more general”.

> **Stacks Project, Tag 05KS.** The opposite of the category of elementary
> étale neighborhoods of a point is filtered.

```lean
instance instIsFilteredOppositeElementaryEtaleNeighborhood
    (S : Scheme.{u}) (s : S) :
    IsFiltered (ElementaryEtaleNeighborhood S s)ᵒᵖ
```

**`AlgebraicGeometry.isColimit_globalSections`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Henselization.lean#L1354). The attribute's comment: “the henselization is the colimit of O(U) over the étale neighbourhoods with κ(s)”.

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

## Tag 04HZ, a lemma

[Tag 04HZ](https://stacks.math.columbia.edu/tag/04HZ) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleRingedSite_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleRingedSite.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleRingedSite.lean#L159).

> The small étale site of a scheme, endowed with its structure sheaf, is a
> locally ringed site.

```lean
public theorem smallEtaleRingedSite_isLocallyRinged :
    RingedSite.IsLocallyRinged (smallEtaleRingedSite B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.33, Tag 04HW](https://stacks.math.columbia.edu/tag/04HW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
