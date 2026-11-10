---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.IsJ2, AlgebraicGeometry.Scheme.isJ2_Spec_iff, AlgebraicGeometry.Scheme.isJ2_tfae, AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType', AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_field, AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_completeLocalRing, AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_int, AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_localRing_of_dim_one
statement: formalized
proof: formalized
---

# 29.19 The singular locus, reprise

Section 29.19 of the Stacks Project, [Tag 07R2](https://stacks.math.columbia.edu/tag/07R2). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07R3, a definition

[Tag 07R3](https://stacks.math.columbia.edu/tag/07R3) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsJ2`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwo.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwo.lean#L54).

> A locally Noetherian scheme `X` is **J-2** if the regular locus of every scheme locally of
> finite type over `X` is open.

```lean
public def IsJ2 (X : Scheme.{u}) [IsLocallyNoetherian X] : Prop
```

## Tag 07R4, a lemma

[Tag 07R4](https://stacks.math.columbia.edu/tag/07R4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isJ2_Spec_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoCriteria.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoCriteria.lean#L163). The attribute's comment: “the affine case”.

> **Stacks Project, Tag 07R4.** On the spectrum of a Noetherian ring the scheme-theoretic J-2
> condition is the ring-theoretic one.

```lean
public theorem isJ2_Spec_iff (R : Type u) [CommRing R] [IsNoetherianRing R] :
    IsJ2 (Spec (.of R)) ↔ _root_.IsJ2 R
```

**`AlgebraicGeometry.Scheme.isJ2_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeJTwoLocal/JTwoTFAE.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeJTwoLocal/JTwoTFAE.lean#L136). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 07R4.** For a locally Noetherian scheme, the J-2 condition is
> equivalent to holding on the members of an open covering, to the section ring of every affine
> open being J-2, and to that ring-theoretic condition holding on one affine open covering.

```lean
public theorem isJ2_tfae (X : Scheme.{u}) [IsLocallyNoetherian X] :
    List.TFAE [
      IsJ2 X,
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsJ2 (U i).toScheme,
      ∀ U : X.affineOpens, _root_.IsJ2 Γ(X, U.1),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).1) = ⊤ ∧ ∀ i, _root_.IsJ2 Γ(X, (U i).1)]
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeJTwoLocal/JTwoTFAE.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeJTwoLocal/JTwoTFAE.lean#L173). The attribute's comment: “locally finite type schemes”.

> **Stacks Project, Tag 07R4.** A scheme locally of finite type over a J-2 scheme is J-2.
> Local Noetherianity of the source is derived from that of the base rather than assumed.

```lean
public theorem isJ2_of_locallyOfFiniteType' {X Y : Scheme.{u}} [IsLocallyNoetherian X]
    (hX : IsJ2 X) (f : Y ⟶ X) [LocallyOfFiniteType f] :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian f
    IsJ2 Y
```

## Tag 07R5, a lemma

[Tag 07R5](https://stacks.math.columbia.edu/tag/07R5) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L61). The attribute's comment: “field\_case”. References: EGA IV (6.12.6), “(ii), field base”; SGA 5 I (3.1.1), “field base”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over a field is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_field (k : Type u) [Field k] {X : Scheme.{u}}
    [IsLocallyNoetherian X] (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] : IsJ2 X
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_completeLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L68). The attribute's comment: “complete\_local\_case”. References: EGA IV (6.12.8); SGA 5 I (3.1.1), “complete local base”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over a Noetherian complete
> local ring is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_completeLocalRing (R : Type u) [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] [IsPrecomplete (IsLocalRing.maximalIdeal R) R]
    {X : Scheme.{u}} [IsLocallyNoetherian X] (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] :
    IsJ2 X
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L76). The attribute's comment: “integers\_case”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over the integers is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_int {X : Scheme.{0}} [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of ℤ)) [LocallyOfFiniteType f] : IsJ2 X
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_localRing_of_dim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L83). The attribute's comment: “local\_dimension\_one\_case”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over a Noetherian local ring
> of dimension one is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_localRing_of_dim_one (R : Type u) [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] (hR : ringKrullDim R = 1) {X : Scheme.{u}}
    [IsLocallyNoetherian X] (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] : IsJ2 X
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_nagataRing_of_dim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L92). The attribute's comment: “nagata\_dimension\_one\_case”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over a Nagata ring of
> dimension one is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_nagataRing_of_dim_one (R : Type u) [CommRing R]
    [IsNagataRing R] (hR : ringKrullDim R = 1) {X : Scheme.{u}} [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] : IsJ2 X
```

**`AlgebraicGeometry.Scheme.isJ2_of_locallyOfFiniteType_over_dedekindDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SingularLocus/JTwoStandardClasses.lean#L103). The attribute's comment: “dedekind\_characteristic\_zero\_case”. References: EGA IV (6.12.6), “(i)”; SGA 5 I (3.1.1), “Dedekind char 0 base”.

> **Stacks Project, Tag 07R5.** A scheme locally of finite type over a Dedekind domain of
> characteristic zero is J-2.

```lean
public theorem isJ2_of_locallyOfFiniteType_over_dedekindDomain (R : Type u) [CommRing R]
    [IsDedekindDomain R] [CharZero R] {X : Scheme.{u}} [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] : IsJ2 X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.19, Tag 07R2](https://stacks.math.columbia.edu/tag/07R2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
