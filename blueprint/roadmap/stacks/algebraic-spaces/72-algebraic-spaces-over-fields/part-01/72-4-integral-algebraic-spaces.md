---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsIntegralSpace, AlgebraicGeometry.Space.evalPartial_eq, AlgebraicGeometry.Space.evalRingHom, AlgebraicGeometry.Space.isField_residueField_genericPoint, AlgebraicGeometry.Space.evalRingHom_injective, AlgebraicGeometry.Space.evalRingHom_surjective, AlgebraicGeometry.Space.evalRingHom_bijective, AlgebraicGeometry.Space.rationalFunctionsRingEquiv
statement: formalized
proof: formalized
---

# 72.4 Integral algebraic spaces

Section 72.4 of the Stacks Project, [Tag 0AD3](https://stacks.math.columbia.edu/tag/0AD3). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AD4, a definition

[Tag 0AD4](https://stacks.math.columbia.edu/tag/0AD4) in the Stacks Project.

**`AlgebraicGeometry.Space.IsIntegralSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpace.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpace.lean#L67).

> **Stacks 0AD4.** An algebraic space over `S` is *integral* when it is reduced, decent,
> and its space of points is irreducible.

```lean
abbrev IsIntegralSpace : Prop
```

## Tag 0END, a lemma

[Tag 0END](https://stacks.math.columbia.edu/tag/0END) in the Stacks Project.

**`AlgebraicGeometry.Space.evalPartial_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L359). The attribute's comment: “the characterisation of evaluation at the generic point: the value on a representative is its coordinate along any factorisation of the residue-field morphism through the domain, independently of the factorisation”.

> Evaluation is computed by any lift of the generic field-valued point.

```lean
theorem evalPartial_eq (p : FieldValuedPoint B S hS X)
    (hp : p.class B S hS X = genericPoint B S hS hX hInt)
    (f : PartialMap B S hS hX (affineLineFunctor B S hS))
    (j : yoneda.obj (p.siteObject B S hS X) ⟶ f.domain.toFunctor)
    (hj : j ≫ f.domain.ι = fieldMorphism B S hS X p) :
    evalPartial B S hS hX hInt p hp f =
      (Scheme.ΓSpecIso (CommRingCat.of p.carrier)).hom.hom
        (affineLineCoordinate B S hS (Opposite.op (p.siteObject B S hS X))
          (yonedaEquiv (j ≫ f.hom)))
```

**`AlgebraicGeometry.Space.evalRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L445). The attribute's comment: “evaluation of rational functions at the generic point, as a ring homomorphism R(X) → κ(η)”.

> Evaluation at the generic point, as a ring homomorphism from the rational functions to
> the field of a field-valued representative of that point.

```lean
noncomputable def evalRingHom (p : FieldValuedPoint B S hS X)
    (hp : p.class B S hS X = genericPoint B S hS hX hInt) :
    rationalFunctions B S hS hX →+* p.carrier
```

**`AlgebraicGeometry.Space.isField_residueField_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L580). The attribute's comment: “the residue field at the generic point is a field”.

> **Stacks 0END.** The residue field at the generic point of an integral algebraic space
> over `S` is a field.

```lean
theorem isField_residueField_genericPoint (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    IsField (residueField B S hS X hInt.2.1 (genericPoint B S hS hX hInt))
```

**`AlgebraicGeometry.Space.evalRingHom_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 855](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L855). The attribute's comment: “injectivity of evaluation at the generic point”.

> Evaluation at the generic point is injective: a rational function whose value there
> vanishes has a representative on a representable dense open chart through the generic point,
> and the coordinate of that representative, a regular function on an integral scheme, is
> determined by its value at the dense point of that scheme.

```lean
theorem evalRingHom_injective (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) (p : FieldValuedPoint B S hS X)
    (hp : p.class B S hS X = genericPoint B S hS hX hInt) :
    Function.Injective (evalRingHom B S hS hX hInt p hp)
```

**`AlgebraicGeometry.Space.evalRingHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 992](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L992). The attribute's comment: “surjectivity of evaluation at the generic point”.

> Evaluation at the generic point is surjective: the field of a monomorphic representative
> of the generic point is the residue field of a representable dense open chart at the point
> below the generic point, every element of that residue field is the value of a regular
> function on a smaller open set, and that open set carries a representable dense open chart
> again.

```lean
theorem evalRingHom_surjective (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) (p : FieldValuedPoint B S hS X)
    (hp : p.class B S hS X = genericPoint B S hS hX hInt)
    (hmono : Mono (fieldMorphism B S hS X p)) :
    Function.Surjective (evalRingHom B S hS hX hInt p hp)
```

**`AlgebraicGeometry.Space.evalRingHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1091](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1091). The attribute's comment: “bijectivity of evaluation at the generic point, on a monomorphic field-valued representative”.

> Evaluation at the generic point is a bijection onto the field of a monomorphic
> field-valued representative of that point.

```lean
theorem evalRingHom_bijective (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) (p : FieldValuedPoint B S hS X)
    (hp : p.class B S hS X = genericPoint B S hS hX hInt)
    (hmono : Mono (fieldMorphism B S hS X p)) :
    Function.Bijective (evalRingHom B S hS hX hInt p hp)
```

**`AlgebraicGeometry.Space.rationalFunctionsRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1104). The attribute's comment: “the identification R(X) = κ(η) of the rational functions with the residue field at the generic point”.

> **Stacks 0END.** The ring of rational functions of an integral algebraic space over `S` is
> the residue field at its generic point: evaluation at the generic point is an isomorphism of
> rings from the rational functions of Tag 0EMP onto the residue field of Tag 0EMW.

```lean
noncomputable def rationalFunctionsRingEquiv (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    rationalFunctions B S hS hX ≃+*
      residueField B S hS X hInt.2.1 (genericPoint B S hS hX hInt)
```

**`AlgebraicGeometry.Space.isField_rationalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1141). The attribute's comment: “the rational functions of an integral algebraic space form a field”.

> **Stacks 0END.** The ring of rational functions of an integral algebraic space over `S` is
> a field: it is the residue field at the generic point.

```lean
theorem isField_rationalFunctions (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) : IsField (rationalFunctions B S hS hX)
```

**`AlgebraicGeometry.Space.isField_neighborhoodStalk_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1219). The attribute's comment: “the local ring of an elementary étale neighbourhood at its marked point, over the generic point, is a field; the neighbourhood is a parameter because the statement is about it, and Tag 0BBP provides one”.

> The local ring of an elementary étale neighbourhood of the generic point of an integral
> algebraic space, at the marked point of that neighbourhood, is a field: the scheme of the
> neighbourhood is reduced, because reducedness is an étale-local property and the neighbourhood
> is étale over the space, and the local ring has Krull dimension zero, because the generic point
> is a point of codimension zero by Stacks 0ABV and the dimension of the local ring of an
> algebraic space at a point is measured on any étale chart above it by Stacks 0BAM.

```lean
theorem isField_neighborhoodStalk_genericPoint (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X)
    (E : ElementaryEtaleNeighborhood B S hS X hX (genericPoint B S hS hX hInt)) :
    IsField (E.scheme.left.1.presheaf.stalk E.point)
```

**`AlgebraicGeometry.Space.evalNeighborhoodRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1275). The attribute's comment: “the rational functions are the residue field of an elementary étale neighbourhood of the generic point at its marked point”.

> The ring of rational functions of an integral algebraic space is the residue field of any
> elementary étale neighbourhood of the generic point at its marked point: that residue field is
> a *monomorphic* field-valued representative of the generic point, by the data of Stacks 0BGU,
> so evaluation at the generic point is bijective onto it.

```lean
noncomputable def evalNeighborhoodRingEquiv (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X)
    (E : ElementaryEtaleNeighborhood B S hS X hX (genericPoint B S hS hX hInt)) :
    rationalFunctions B S hS hX ≃+* E.scheme.left.1.residueField E.point
```

**`AlgebraicGeometry.Space.isField_henselianLocalRing_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1291). The attribute's comment: “the henselian local ring O^h\_\{X,η} at the generic point is a field”.

> **Stacks 0END.** The henselian local ring of Stacks 0BGW at the generic point of an integral
> algebraic space is a field: it is a henselisation of the local ring of the elementary étale
> neighbourhood of Stacks 0BBP at its marked point by Stacks 0EMY, that local ring is a field, and
> a henselisation of a field is a field.

```lean
theorem isField_henselianLocalRing_genericPoint (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    IsField (henselianLocalRing B S hS X hX (genericPoint B S hS hX hInt) hInt.2.1 :
      Type (u + 1))
```

**`AlgebraicGeometry.Space.bijective_stalkToHenselianLocalRing_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1307). The attribute's comment: “bijectivity at the generic point of the canonical map O\_\{U,u} → O^h\_\{X,η} of Tag 0EMY”.

> The canonical map of Stacks 0EMY from the local ring of an elementary étale neighbourhood of
> the generic point into the henselian local ring is bijective: it is the structure map of a
> henselisation of a field.

```lean
theorem bijective_stalkToHenselianLocalRing_genericPoint (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X)
    (E : ElementaryEtaleNeighborhood B S hS X hX (genericPoint B S hS hX hInt)) :
    Function.Bijective (stalkToHenselianLocalRing B S hS X hX
      (genericPoint B S hS hX hInt) hInt.2.1 E)
```

**`AlgebraicGeometry.Space.rationalFunctionsHenselianRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1381). The attribute's comment: “the identification R(X) = O^h\_\{X,η} of the rational functions with the henselian local ring at the generic point”.

> **Stacks 0END.** The ring of rational functions of an integral algebraic space over `S` is
> the henselian local ring of Stacks 0BGW at its generic point: the comparison is built from the
> elementary étale neighbourhood of Stacks 0BBP.

```lean
noncomputable def rationalFunctionsHenselianRingEquiv (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    rationalFunctions B S hS hX ≃+*
      (henselianLocalRing B S hS X hX (genericPoint B S hS hX hInt) hInt.2.1 : Type (u + 1))
```

**`AlgebraicGeometry.Space.rationalFunctionsHenselianRingEquivOfNeighborhood_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1417). The attribute's comment: “the characterisation of that identification: a rational function goes to the canonical image of any element of the neighbourhood's local ring whose residue is its value at the generic point”.

> The identification with the henselian local ring is pinned down without inverses: it
> carries a rational function to the canonical image of *any* element of the local ring of the
> neighbourhood whose residue is the value of that function at the generic point.

```lean
theorem rationalFunctionsHenselianRingEquivOfNeighborhood_eq (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X)
    (E : ElementaryEtaleNeighborhood B S hS X hX (genericPoint B S hS hX hInt))
    (x : rationalFunctions B S hS hX) (r : E.scheme.left.1.presheaf.stalk E.point)
    (hr : IsLocalRing.residue (E.scheme.left.1.presheaf.stalk E.point) r =
      evalRingHom B S hS hX hInt (genericNeighborhoodFieldPoint B S hS hX hInt E)
        (neighborhoodFieldPoint_class B S hS X hX (genericPoint B S hS hX hInt) E) x) :
    rationalFunctionsHenselianRingEquivOfNeighborhood B S hS hX hInt E x =
      stalkToHenselianLocalRing B S hS X hX (genericPoint B S hS hX hInt) hInt.2.1 E r
```

**`AlgebraicGeometry.Space.residueFieldHenselianRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1462). The attribute's comment: “the identification O^h\_\{X,η} = κ(η) of the henselian local ring at the generic point with the residue field there”.

> **Stacks 0END.** The residue field at the generic point of an integral algebraic space over
> `S` is the henselian local ring of Stacks 0BGW there: both are the ring of rational
> functions.

```lean
noncomputable def residueFieldHenselianRingEquiv (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    residueField B S hS X hInt.2.1 (genericPoint B S hS hX hInt) ≃+*
      (henselianLocalRing B S hS X hX (genericPoint B S hS hX hInt) hInt.2.1 : Type (u + 1))
```

**`AlgebraicGeometry.Space.rationalFunctionsHenselianRingEquiv_eq_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean, line 1474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericRationalFunctions.lean#L1474). The attribute's comment: “the chain R(X) = O^h\_\{X,η} = κ(η): the three identifications commute”.

> **Stacks 0END.** The tag asserts one chain of identifications `R(X) = O^h_{X,η} = κ(η)`, and
> the three identifications are indeed the three edges of one commuting triangle: going from the
> rational functions to the henselian local ring is going to the residue field and on from
> there.

```lean
theorem rationalFunctionsHenselianRingEquiv_eq_trans (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) :
    rationalFunctionsHenselianRingEquiv B S hS hX hInt =
      (rationalFunctionsRingEquiv B S hS hX hInt).trans
        (residueFieldHenselianRingEquiv B S hS hX hInt)
```

## Tag 0ENE, a definition

[Tag 0ENE](https://stacks.math.columbia.edu/tag/0ENE) in the Stacks Project.

**`AlgebraicGeometry.Space.functionField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FunctionField.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FunctionField.lean#L65). The attribute's comment: “the function field R(X) = k(X) of an integral algebraic space”.

> **Stacks 0ENE.** The function field, or field of rational functions, of an integral
> algebraic space `X` over `S`: the ring `R(X)` of rational functions of Tag 0EMP, which
> Tag 0END shows to be a field by identifying it with the residue field at the generic
> point.

```lean
noncomputable def functionField (hX : IsAlgebraicSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X) : Field (rationalFunctions B S hS hX)
```

## Tag 0BH2, a lemma

[Tag 0BH2](https://stacks.math.columbia.edu/tag/0BH2) in the Stacks Project.

**`AlgebraicGeometry.Space.isDomain_globalSections_of_isIntegralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpaceProperties.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpaceProperties.lean#L285).

> The ring of global regular functions on an integral algebraic space, the compatible families
> of regular functions on its étale charts, is a domain.

```lean
theorem isDomain_globalSections_of_isIntegralSpace (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (hXint : IsIntegralSpace B S hS X) :
    IsDomain (RingCat.sectionsSubring
      (structurePresheaf B S hS X ⋙ forget₂ CommRingCat.{u} RingCat.{u}))
```

## Tag 0AYH, a lemma

[Tag 0AYH](https://stacks.math.columbia.edu/tag/0AYH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAffine_isNormal_isIntegral_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalIntegralEtaleChart.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalIntegralEtaleChart.lean#L248).

> **Stacks 0AYH.** Let `X` be a normal integral algebraic space over `S`. Every point of
> `|X|` is in the image of an étale morphism to `X` from a normal integral affine scheme.
>
> An affine étale chart through the point is shrunk to an affine open which is normal and
> integral by
> `AlgebraicGeometry.Space.exists_isAffineOpen_isNormal_isIntegral_of_isAffine_etaleChart`,
> and that open is an object of the chosen big site by
> `AlgebraicGeometry.BigFppfOver.exists_affineOpen_restrict`.

```lean
theorem exists_isAffine_isNormal_isIntegral_etaleChart (hX : IsAlgebraicSpace B S hS X)
    (hnormal : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsNormal Y))
    (hintegral : IsIntegralSpace B S hS X) (x : points B S hS X) :
    ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X),
      IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
      IsNormal ((BigFppfOver.toScheme B S hS).obj U) ∧
      IsIntegral ((BigFppfOver.toScheme B S hS).obj U) ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) φ ∧
      x ∈ Set.range (pointsMap B S hS (yoneda.obj U) φ)
```

## Tag 0BH3, a lemma

[Tag 0BH3](https://stacks.math.columbia.edu/tag/0BH3) in the Stacks Project.

**`AlgebraicGeometry.Space.isNormalDomain_globalSections_of_isIntegralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpaceProperties.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralSpaceProperties.lean#L409). References: EGA II (8.8.6.1).

> The ring of global regular functions on a normal integral algebraic space, the compatible
> families of regular functions on its étale charts, is a normal domain.

```lean
theorem isNormalDomain_globalSections_of_isIntegralSpace (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (hXint : IsIntegralSpace B S hS X)
    (hXnormal : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsNormal Y)) :
    IsNormalDomain (RingCat.sectionsSubring
      (structurePresheaf B S hS X ⋙ forget₂ CommRingCat.{u} RingCat.{u}))
```

## Tag 0ENF, a lemma

[Tag 0ENF](https://stacks.math.columbia.edu/tag/0ENF) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_closureSingleton_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L101). The attribute's comment: “the map from (1) to (2) is injective, unconditionally”.

> Two points of a decent algebraic space over `S` with the same closure are equal: the map
> from (1) to (2) is injective.

```lean
theorem injective_closureSingleton_points (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) :
    Function.Injective (IrreducibleCloseds.closureSingleton (X := points B S hS X))
```

**`AlgebraicGeometry.Space.bijective_closureSingleton_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L114). The attribute's comment: “the bijection from (1) to (2)”.

> Taking the closure of a point is a bijection from the points of a decent algebraic space
> `X` over `S` onto the irreducible closed subsets of `|X|`.

```lean
theorem bijective_closureSingleton_points (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) :
    Function.Bijective (IrreducibleCloseds.closureSingleton (X := points B S hS X))
```

**`AlgebraicGeometry.Space.IntegralClosedSubspace`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L128). The attribute's comment: “(3): the integral closed subspaces of an algebraic space”.

> An *integral closed subspace* of an algebraic space `X` over `S` is a closed subspace of
> `X`, in the sense of Stacks 02YU, which is an integral algebraic space over `S`, in the sense of
> Stacks 0AD4.

```lean
structure IntegralClosedSubspace (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

**`AlgebraicGeometry.Space.integralClosedSubspaceSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L157). The attribute's comment: “the map from (3) to (2): the point set of an integral closed subspace”.

> The set of points of an integral closed subspace of `X`, as an irreducible closed subset
> of `|X|`. This is the map from (3) to (2).

```lean
def integralClosedSubspaceSupport (hX : IsAlgebraicSpace B S hS X)
    (Z : IntegralClosedSubspace B S hS X) : IrreducibleCloseds (points B S hS X)
```

**`AlgebraicGeometry.Space.injective_integralClosedSubspaceSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L175). The attribute's comment: “the map from (3) to (2) is injective, unconditionally”.

> An integral closed subspace of an algebraic space over `S` is determined by its set of
> points: the map from (3) to (2) is injective.

```lean
theorem injective_integralClosedSubspaceSupport (hX : IsAlgebraicSpace B S hS X) :
    Function.Injective (integralClosedSubspaceSupport B S hS hX)
```

**`AlgebraicGeometry.Space.surjective_integralClosedSubspaceSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L189). The attribute's comment: “the map from (3) to (2) is surjective”.

> Every irreducible closed subset of `|X|`, for `X` a decent algebraic space over `S`, is the
> set of points of an integral closed subspace: the map from (3) to (2) is surjective.

```lean
theorem surjective_integralClosedSubspaceSupport (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) :
    Function.Surjective (integralClosedSubspaceSupport B S hS hX)
```

**`AlgebraicGeometry.Space.bijective_integralClosedSubspaceSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IntegralClosedSubspaces.lean#L216). The attribute's comment: “the bijection from (3) to (2)”.

> Taking the set of points is a bijection from the integral closed subspaces of a decent
> algebraic space `X` over `S` onto the irreducible closed subsets of `|X|`.

```lean
theorem bijective_integralClosedSubspaceSupport (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) :
    Function.Bijective (integralClosedSubspaceSupport B S hS hX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.4, Tag 0AD3](https://stacks.math.columbia.edu/tag/0AD3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
