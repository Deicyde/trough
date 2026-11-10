---
declaration: section
origin: cited
lean: AlgebraicGeometry.finiteType_specField_tfae, AlgebraicGeometry.finiteType_iff_residueField_comp_finiteType, AlgebraicGeometry.IsFiniteTypePoint, AlgebraicGeometry.Scheme.finiteTypePoints, AlgebraicGeometry.Scheme.finiteTypePoints_eq_iUnion_closedPoints, AlgebraicGeometry.mapsTo_finiteTypePoints, AlgebraicGeometry.image_finiteTypePoints_eq, AlgebraicGeometry.inter_finiteTypePoints_nonempty
statement: formalized
proof: formalized
---

# 29.16 Points of finite type and Jacobson schemes

Section 29.16 of the Stacks Project, [Tag 01T9](https://stacks.math.columbia.edu/tag/01T9). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01TA, a lemma

[Tag 01TA](https://stacks.math.columbia.edu/tag/01TA) in the Stacks Project.

**`AlgebraicGeometry.finiteType_specField_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/SpecField.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/SpecField.lean#L136).

> **Stacks Project, Tag 01TA.** For a morphism from the spectrum of a field, being of finite
> type, being locally of finite type, admitting a finite affine coordinate-ring map around its
> image, and having closed image with finite residue field extension are equivalent.

```lean
theorem finiteType_specField_tfae {k : Type u} [Field k] {S : Scheme.{u}}
    (f : Spec (.of k) ⟶ S) :
    List.TFAE [
      LocallyOfFiniteType f ∧ QuasiCompact f,
      LocallyOfFiniteType f,
      ∃ (U : S.affineOpens)
          (hU : (⊤ : (Spec (.of k)).Opens) ≤ f ⁻¹ᵁ U.1),
        ((f.appLE U ⊤ hU) ≫ (Scheme.ΓSpecIso (.of k)).hom).hom.Finite,
      ∃ (U : S.affineOpens)
          (_hU : (⊤ : (Spec (.of k)).Opens) ≤ f ⁻¹ᵁ U.1)
          (x : U.1),
        (x : S) = ((Scheme.SpecToEquivOfField k S) f).1 ∧
          IsClosed ({x} : Set U.1) ∧
          letI := ((Scheme.SpecToEquivOfField k S) f).2.hom.toAlgebra
          Module.Finite (S.residueField ((Scheme.SpecToEquivOfField k S) f).1) k]
```

## Tag 02HV, a lemma

[Tag 02HV](https://stacks.math.columbia.edu/tag/02HV) in the Stacks Project.

**`AlgebraicGeometry.finiteType_iff_residueField_comp_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/ArtinianLocalRing.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/ArtinianLocalRing.lean#L43).

> A morphism from the spectrum of an Artinian local ring is of finite type if and only if
> its composite with the spectrum of the residue field is of finite type.

```lean
theorem finiteType_iff_residueField_comp_finiteType
    (S : Scheme.{u}) (A : Type u) [CommRing A] [IsLocalRing A] [IsArtinianRing A]
    (f : Spec (CommRingCat.of A) ⟶ S) :
    (LocallyOfFiniteType f ∧ QuasiCompact f) ↔
      (LocallyOfFiniteType
          (Spec.map (CommRingCat.ofHom (IsLocalRing.residue A)) ≫ f) ∧
        QuasiCompact
          (Spec.map (CommRingCat.ofHom (IsLocalRing.residue A)) ≫ f))
```

## Tag 02J1, a definition

[Tag 02J1](https://stacks.math.columbia.edu/tag/02J1) in the Stacks Project.

**`AlgebraicGeometry.IsFiniteTypePoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L108). The attribute's comment: “finite\_type\_point”.

> A point `s` of a scheme `S` is a finite type point if the canonical morphism
> `Spec(κ(s)) ⟶ S` is of finite type.

```lean
public abbrev IsFiniteTypePoint {S : AlgebraicGeometry.Scheme.{u}} (s : S) : Prop
```

**`AlgebraicGeometry.Scheme.finiteTypePoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L71). The attribute's comment: “finite\_type\_points\_set”.

> The set of finite type points of a scheme.

```lean
abbrev Scheme.finiteTypePoints (S : Scheme.{u}) : Set S
```

## Tag 02J2, a lemma

[Tag 02J2](https://stacks.math.columbia.edu/tag/02J2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.finiteTypePoints_eq_iUnion_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L276).

> The set of finite type points of a scheme `S` is the union, over the open subschemes `U` of
> `S`, of the sets of closed points of `U`; the same union taken over the affine open subschemes
> of `S` has the same value.

```lean
theorem Scheme.finiteTypePoints_eq_iUnion_closedPoints (S : Scheme.{u}) :
    S.finiteTypePoints = (⋃ U : S.Opens, Subtype.val '' closedPoints ↑U) ∧
      S.finiteTypePoints = ⋃ U : S.affineOpens, Subtype.val '' closedPoints ↑U.1
```

## Tag 02J3, a lemma

[Tag 02J3](https://stacks.math.columbia.edu/tag/02J3) in the Stacks Project.

**`AlgebraicGeometry.mapsTo_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L110).

> A locally finite type morphism of schemes sends finite type points to finite type
> points.

```lean
theorem mapsTo_finiteTypePoints {T S : Scheme.{u}} (f : T ⟶ S)
    [LocallyOfFiniteType f] :
    Set.MapsTo f.base T.finiteTypePoints S.finiteTypePoints
```

## Tag 06EB, a lemma

[Tag 06EB](https://stacks.math.columbia.edu/tag/06EB) in the Stacks Project.

**`AlgebraicGeometry.image_finiteTypePoints_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L218).

> A surjective morphism which is locally of finite type maps the finite type points of its
> source onto those of its target.

```lean
theorem image_finiteTypePoints_eq {T S : Scheme.{u}} (f : T ⟶ S)
    [LocallyOfFiniteType f] [Surjective f] :
    f.base '' T.finiteTypePoints = S.finiteTypePoints
```

## Tag 02J4, a lemma

[Tag 02J4](https://stacks.math.columbia.edu/tag/02J4) in the Stacks Project.

**`AlgebraicGeometry.inter_finiteTypePoints_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L157). The attribute's comment: “locally closed subsets”.

> Every nonempty locally closed subset of a scheme contains a finite type point.

```lean
theorem inter_finiteTypePoints_nonempty {S : Scheme.{u}} {T : Set S}
    (hT : IsLocallyClosed T) (hne : T.Nonempty) :
    (T ∩ S.finiteTypePoints).Nonempty
```

**`AlgebraicGeometry.closure_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Basic.lean#L200). The attribute's comment: “closed subsets”.

> The finite type points lying in a closed subset of a scheme are dense in that subset.

```lean
theorem closure_inter_finiteTypePoints {S : Scheme.{u}} {T : Set S}
    (hT : IsClosed T) : closure (T ∩ S.finiteTypePoints) = T
```

## Tag 01TB, a lemma

[Tag 01TB](https://stacks.math.columbia.edu/tag/01TB) in the Stacks Project.

**`AlgebraicGeometry.isFiniteTypePoint_of_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L119). The attribute's comment: “closed points are finite type points”.

> A closed point of a scheme is a finite type point: the morphism from the spectrum of its
> residue field is a closed immersion
> (`AlgebraicGeometry.isClosed_singleton_iff_isClosedImmersion`), hence both locally of finite
> type and quasi-compact.

```lean
public theorem isFiniteTypePoint_of_isClosed_singleton {X : Scheme.{u}} {x : X}
    (hx : IsClosed ({x} : Set X)) : IsFiniteTypePoint x
```

**`AlgebraicGeometry.jacobsonSpace_finiteTypePoints_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Tfae.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Tfae.lean#L45). References: EGA IV (10.4.7), “(1) => (3)”; EGA IV (10.9.2), “more general”.

> A scheme is Jacobson exactly when its finite type points are its closed points; equivalently,
> closed points under every locally finite type morphism to it have closed image, and the induced
> residue field extensions are finite.

```lean
public theorem jacobsonSpace_finiteTypePoints_tfae (S : Scheme.{u}) :
    List.TFAE [
      JacobsonSpace S,
      S.finiteTypePoints = {s | IsClosed ({s} : Set S)},
      ∀ (T : Scheme.{u}) (f : T ⟶ S) [LocallyOfFiniteType f] (t : T),
        IsClosed ({t} : Set T) → IsClosed ({f t} : Set S),
      ∀ (T : Scheme.{u}) (f : T ⟶ S) [LocallyOfFiniteType f] (t : T),
        IsClosed ({t} : Set T) → (
          IsClosed ({f t} : Set S) ∧
            letI := (f.residueFieldMap t).hom.toAlgebra
            Module.Finite (S.residueField (f t)) (T.residueField t))]
```

## Tag 02J5, a lemma

[Tag 02J5](https://stacks.math.columbia.edu/tag/02J5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType.jacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType.jacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L167) (StacksFrontier). References: EGA IV (10.4.7); EGA IV (10.4.9), “more general”; EGA IV (10.6.1), “(i), condition 1° for X”; EGA IV (10.7.1), “1°, partial”; SGA 3 VIB (1.3.0), “Jacobson property of G”; SGA 4 VIII (3.13), “more general”.

## Tag 02J6, a lemma

[Tag 02J6](https://stacks.math.columbia.edu/tag/02J6) in the Stacks Project.

**`AlgebraicGeometry.jacobsonSpace_of_locallyOfFiniteType_over_integers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean#L67). The attribute's comment: “over\_integers”. References: EGA IV (10.4.7), “base = Spec Z”; EGA IV (10.4.6), “over Z”; EGA IV (10.4.9), “over Z”; EGA IV (10.7.1), “1° over Z”.

> A scheme locally of finite type over the integers is Jacobson.

```lean
theorem jacobsonSpace_of_locallyOfFiniteType_over_integers {X : Scheme.{u}}
    (f : X ⟶ ⊤_ Scheme.{u}) [LocallyOfFiniteType f] : JacobsonSpace X
```

**`AlgebraicGeometry.jacobsonSpace_of_locallyOfFiniteType_over_oneDimensionalNoetherianDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean#L81). The attribute's comment: “over\_dimension\_one\_domain”. References: EGA IV (10.4.7), “1-dim Noeth domain base”; EGA IV (10.7.1), “special case”.

> A scheme locally of finite type over a one-dimensional Noetherian domain with infinitely
> many prime ideals is Jacobson.

```lean
theorem jacobsonSpace_of_locallyOfFiniteType_over_oneDimensionalNoetherianDomain
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1) (hprimes : {p : Ideal A | p.IsPrime}.Infinite)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] :
    JacobsonSpace X
```

**`AlgebraicGeometry.jacobsonSpace_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean#L108). The attribute's comment: “part (4): the punctured spectrum itself, R Noetherian local”. References: EGA IV (10.4.7), “punctured spectrum base”; EGA IV (10.5.7), “special case”.

> The punctured spectrum `Spec R \ {𝔪}` of a Noetherian local ring `R` is a Jacobson
> scheme.

```lean
theorem jacobsonSpace_puncturedSpectrum (R : Type u) [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] :
    JacobsonSpace (Stacks.Divisors.puncturedSpectrum R).toScheme
```

**`AlgebraicGeometry.jacobsonSpace_of_locallyOfFiniteType_over_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean#L117). The attribute's comment: “part (4): schemes lft over the punctured spectrum, R Noetherian local”. References: EGA IV (10.4.7), “punctured spectrum base”; EGA IV (10.5.7), “special case”.

> A scheme locally of finite type over the punctured spectrum of a Noetherian local ring is
> Jacobson.

```lean
theorem jacobsonSpace_of_locallyOfFiniteType_over_puncturedSpectrum
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    {X : Scheme.{u}} (f : X ⟶ (Stacks.Divisors.puncturedSpectrum R).toScheme)
    [LocallyOfFiniteType f] : JacobsonSpace X
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType.jacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType.jacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/JacobsonPoints/Jacobson.lean#L53) (StacksFrontier): “over\_field”. References: EGA IV (10.4.7); EGA IV (10.4.9), “more general”; EGA IV (10.6.1), “(i), condition 1° for X”; EGA IV (10.7.1), “1°, partial”; SGA 3 VIB (1.3.0), “Jacobson property of G”; SGA 4 VIII (3.13), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.16, Tag 01T9](https://stacks.math.columbia.edu/tag/01T9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
