---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_common_field_fiber_iso, AlgebraicGeometry.exists_common_field_fiber_iso_mapping_point, AlgebraicGeometry.flatIsoLocallyOnBase_source, AlgebraicGeometry.isoLocallyOnBase_source, AlgebraicGeometry.isoLocallyOnBase_source_etale, AlgebraicGeometry.isoLocallyOnBase_source_smooth, AlgebraicGeometry.isoLocallyOnBase_source_syntomic, AlgebraicGeometry.isoLocallyOnBase_source_fppf
statement: formalized
proof: formalized
---

# 40.7 Comparing fibres

Section 40.7 of the Stacks Project, [Tag 04LJ](https://stacks.math.columbia.edu/tag/04LJ). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02YF, a lemma

[Tag 02YF](https://stacks.math.columbia.edu/tag/02YF) in the Stacks Project.

**`AlgebraicGeometry.exists_common_field_fiber_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CommonField.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CommonField.lean#L134). The attribute's comment: “common\_field”.

> If two arrows in a groupoid scheme have the same target, then the fibres of the source
> map over their sources become isomorphic after extending both residue fields to a common
> field.

```lean
public theorem exists_common_field_fiber_iso {S : Scheme.{u}}
    (G : GroupoidScheme S) (r r' : G.arrows.left)
    (h : G.target.left r = G.target.left r') :
    ∃ (K : Type u) (_ : Field K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r)) K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r')) K),
      Nonempty
        (Over.mk (pullback.snd
          (G.source.left.fiberToSpecResidueField (G.source.left r))
          (Spec.map (CommRingCat.ofHom
            (algebraMap (G.objects.left.residueField (G.source.left r)) K)))) ≅
        Over.mk (pullback.snd
          (G.source.left.fiberToSpecResidueField (G.source.left r'))
          (Spec.map (CommRingCat.ofHom
            (algebraMap (G.objects.left.residueField (G.source.left r')) K)))))
```

**`AlgebraicGeometry.exists_common_field_fiber_iso_mapping_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CommonField.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CommonField.lean#L162). The attribute's comment: “point\_compatible”.

> The common field and source-fibre isomorphism for two arrows with the same target can be
> chosen so that the isomorphism carries a point above the first arrow to a point above the
> second.

```lean
public theorem exists_common_field_fiber_iso_mapping_point {S : Scheme.{u}}
    (G : GroupoidScheme S) (r r' : G.arrows.left)
    (h : G.target.left r = G.target.left r') :
    ∃ (K : Type u) (_ : Field K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r)) K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r')) K),
      let g : Spec (.of K) ⟶ Spec (.of (G.objects.left.residueField (G.source.left r))) :=
        Spec.map (CommRingCat.ofHom
          (algebraMap (G.objects.left.residueField (G.source.left r)) K))
      let g' : Spec (.of K) ⟶ Spec (.of (G.objects.left.residueField (G.source.left r'))) :=
        Spec.map (CommRingCat.ofHom
          (algebraMap (G.objects.left.residueField (G.source.left r')) K))
      let P : Scheme.{u} :=
        pullback (G.source.left.fiberToSpecResidueField (G.source.left r)) g
      let _P' : Scheme.{u} :=
        pullback (G.source.left.fiberToSpecResidueField (G.source.left r')) g'
      let POver : Over (Spec (.of K)) := Over.mk
        (pullback.snd (G.source.left.fiberToSpecResidueField (G.source.left r)) g)
      let POver' : Over (Spec (.of K)) := Over.mk
        (pullback.snd (G.source.left.fiberToSpecResidueField (G.source.left r')) g')
      ∃ (x : P) (e : POver ≅ POver'),
        ((pullback.fst
            (G.source.left.fiberToSpecResidueField (G.source.left r)) g) ≫
              G.source.left.fiberι (G.source.left r)).base x = r ∧
          ((pullback.fst
            (G.source.left.fiberToSpecResidueField (G.source.left r')) g') ≫
              G.source.left.fiberι (G.source.left r')).base (e.hom.left.base x) = r'
```

**`AlgebraicGeometry.flatIsoLocallyOnBase_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L170). The attribute's comment: “(3)”.

> **Stacks 02YF (3).** If the source and target maps of a groupoid scheme are flat, then for
> two arrows with the same target the two germs of the source map, at the first arrow over its
> source and at the second arrow over its source, are flat locally on the base isomorphic.

```lean
theorem flatIsoLocallyOnBase_source {S : Scheme.{u}} (G : GroupoidScheme S)
    (hs : Flat G.source.left) (ht : Flat G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    FlatIsoLocallyOnBase G.source.left r G.source.left r'
```

**`AlgebraicGeometry.isoLocallyOnBase_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L183). The attribute's comment: “(4)”.

> **Stacks 02YF (4).** If the source and target maps of a groupoid scheme have a property `P`
> of morphisms of schemes, then for two arrows with the same target the two germs of the source
> map, at the first arrow over its source and at the second arrow over its source, are isomorphic
> locally on the base in the topology belonging to `P`.

```lean
theorem isoLocallyOnBase_source {S : Scheme.{u}} (G : GroupoidScheme S)
    (P : MorphismProperty Scheme.{u}) (hs : P G.source.left) (ht : P G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    IsoLocallyOnBase P G.source.left r G.source.left r'
```

**`AlgebraicGeometry.isoLocallyOnBase_source_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L192). The attribute's comment: “(4) etale”.

> **Stacks 02YF (4), the étale case.**

```lean
theorem isoLocallyOnBase_source_etale {S : Scheme.{u}} (G : GroupoidScheme S)
    (hs : Etale G.source.left) (ht : Etale G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    IsoLocallyOnBase @Etale G.source.left r G.source.left r'
```

**`AlgebraicGeometry.isoLocallyOnBase_source_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L200). The attribute's comment: “(4) smooth”.

> **Stacks 02YF (4), the smooth case.**

```lean
theorem isoLocallyOnBase_source_smooth {S : Scheme.{u}} (G : GroupoidScheme S)
    (hs : Smooth G.source.left) (ht : Smooth G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    IsoLocallyOnBase @Smooth G.source.left r G.source.left r'
```

**`AlgebraicGeometry.isoLocallyOnBase_source_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L208). The attribute's comment: “(4) syntomic”.

> **Stacks 02YF (4), the syntomic case.**

```lean
theorem isoLocallyOnBase_source_syntomic {S : Scheme.{u}} (G : GroupoidScheme S)
    (hs : Syntomic G.source.left) (ht : Syntomic G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    IsoLocallyOnBase @Syntomic G.source.left r G.source.left r'
```

**`AlgebraicGeometry.isoLocallyOnBase_source_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L217). The attribute's comment: “(4) fppf”.

> **Stacks 02YF (4), the fppf case:** source and target flat and locally of finite
> presentation.

```lean
theorem isoLocallyOnBase_source_fppf {S : Scheme.{u}} (G : GroupoidScheme S)
    (hs : Flat G.source.left) (hs' : LocallyOfFinitePresentation G.source.left)
    (ht : Flat G.target.left) (ht' : LocallyOfFinitePresentation G.target.left)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    IsoLocallyOnBase (@Flat ⊓ @LocallyOfFinitePresentation) G.source.left r
      G.source.left r'
```

**`AlgebraicGeometry.source_fiber_comparison_of_target_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/GermComparison.lean#L250).

> **Stacks 02YF.** Let `(U, R, s, t, c)` be a groupoid over a scheme `S` and let `r`, `r'` be
> two arrows with the same target.  Writing `u = s r` and `u' = s r'`, and `F_u = s⁻¹(u)`,
> `F_{u'} = s⁻¹(u')` for the scheme theoretic fibres of the source map:
>
> 1. there is a field `k` extending both `κ(u)` and `κ(u')` together with an isomorphism
>    `(F_u)_k ≅ (F_{u'})_k`;
> 2. that isomorphism may be chosen so that a point lying over `r` maps to a point lying over
>    `r'`;
> 3. if `s` and `t` are flat then the morphisms of germs `s : (R, r) ⟶ (U, u)` and
>    `s : (R, r') ⟶ (U, u')` are flat locally on the base isomorphic;
> 4. if `s` and `t` are étale (resp. smooth, syntomic, or flat and locally of finite
>    presentation) then those two morphisms of germs are locally on the base isomorphic in the
>    étale (resp. smooth, syntomic, fppf) topology.
>
> The four parts are `AlgebraicGeometry.exists_common_field_fiber_iso`,
> `AlgebraicGeometry.exists_common_field_fiber_iso_mapping_point`,
> `AlgebraicGeometry.flatIsoLocallyOnBase_source` and the four cases
> `AlgebraicGeometry.isoLocallyOnBase_source_etale`,
> `AlgebraicGeometry.isoLocallyOnBase_source_smooth`,
> `AlgebraicGeometry.isoLocallyOnBase_source_syntomic`,
> `AlgebraicGeometry.isoLocallyOnBase_source_fppf`; the flatness, étaleness, smoothness,
> syntomicity and finite presentation assumptions of parts (3) and (4) appear as hypotheses of
> those parts, exactly as in the source, and not of the lemma.

```lean
theorem source_fiber_comparison_of_target_eq {S : Scheme.{u}} (G : GroupoidScheme S)
    (r r' : G.arrows.left) (h : G.target.left r = G.target.left r') :
    (∃ (K : Type u) (_ : Field K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r)) K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r')) K),
      Nonempty
        (Over.mk (pullback.snd
          (G.source.left.fiberToSpecResidueField (G.source.left r))
          (Spec.map (CommRingCat.ofHom
            (algebraMap (G.objects.left.residueField (G.source.left r)) K)))) ≅
        Over.mk (pullback.snd
          (G.source.left.fiberToSpecResidueField (G.source.left r'))
          (Spec.map (CommRingCat.ofHom
            (algebraMap (G.objects.left.residueField (G.source.left r')) K)))))) ∧
    (∃ (K : Type u) (_ : Field K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r)) K)
      (_ : Algebra (G.objects.left.residueField (G.source.left r')) K),
      let g : Spec (.of K) ⟶ Spec (.of (G.objects.left.residueField (G.source.left r))) :=
        Spec.map (CommRingCat.ofHom
          (algebraMap (G.objects.left.residueField (G.source.left r)) K))
      let g' : Spec (.of K) ⟶ Spec (.of (G.objects.left.residueField (G.source.left r'))) :=
        Spec.map (CommRingCat.ofHom
          (algebraMap (G.objects.left.residueField (G.source.left r')) K))
      let P : Scheme.{u} :=
        pullback (G.source.left.fiberToSpecResidueField (G.source.left r)) g
      let _P' : Scheme.{u} :=
        pullback (G.source.left.fiberToSpecResidueField (G.source.left r')) g'
      let POver : Over (Spec (.of K)) := Over.mk
        (pullback.snd (G.source.left.fiberToSpecResidueField (G.source.left r)) g)
      let POver' : Over (Spec (.of K)) := Over.mk
        (pullback.snd (G.source.left.fiberToSpecResidueField (G.source.left r')) g')
      ∃ (x : P) (e : POver ≅ POver'),
        ((pullback.fst
            (G.source.left.fiberToSpecResidueField (G.source.left r)) g) ≫
              G.source.left.fiberι (G.source.left r)).base x = r ∧
          ((pullback.fst
            (G.source.left.fiberToSpecResidueField (G.source.left r')) g') ≫
              G.source.left.fiberι (G.source.left r')).base (e.hom.left.base x) = r') ∧
    (Flat G.source.left → Flat G.target.left →
      FlatIsoLocallyOnBase G.source.left r G.source.left r') ∧
    (Etale G.source.left → Etale G.target.left →
      IsoLocallyOnBase @Etale G.source.left r G.source.left r') ∧
    (Smooth G.source.left → Smooth G.target.left →
      IsoLocallyOnBase @Smooth G.source.left r G.source.left r') ∧
    (Syntomic G.source.left → Syntomic G.target.left →
      IsoLocallyOnBase @Syntomic G.source.left r G.source.left r') ∧
    (Flat G.source.left → LocallyOfFinitePresentation G.source.left →
      Flat G.target.left → LocallyOfFinitePresentation G.target.left →
      IsoLocallyOnBase (@Flat ⊓ @LocallyOfFinitePresentation) G.source.left r
        G.source.left r')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.7, Tag 04LJ](https://stacks.math.columbia.edu/tag/04LJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
