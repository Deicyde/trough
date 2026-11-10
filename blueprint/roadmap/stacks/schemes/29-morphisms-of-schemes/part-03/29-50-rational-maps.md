---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.PartialMap, AlgebraicGeometry.Scheme.PartialMap.equiv, AlgebraicGeometry.Scheme.RationalMap, AlgebraicGeometry.Scheme.RationalMap.IsOver, AlgebraicGeometry.GenericPointMapContext.bijective_genericPointMapForRationalMaps_of_locallyOfFinitePresentation, AlgebraicGeometry.GenericPointMapContext.genericPointMapForRationalMaps_injective, AlgebraicGeometry.GenericPointMapContext.bijective_genericPointMapForRationalMaps_of_isReduced, AlgebraicGeometry.Scheme.rationalFunctions
statement: formalized
proof: formalized
---

# 29.50 Rational maps

Section 29.50 of the Stacks Project, [Tag 01RR](https://stacks.math.columbia.edu/tag/01RR). 12 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01RS, a definition

[Tag 01RS](https://stacks.math.columbia.edu/tag/01RS) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.PartialMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.PartialMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L136) (StacksFrontier): “(1) a morphism defined on a dense open subscheme”. References: SGA 3 XVIII (1.5), “representatives f”.
- [`AlgebraicGeometry.Scheme.PartialMap.equiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.PartialMap.equiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L138) (StacksFrontier): “(1) equivalence”. References: EGA I (7.1.1); EGA I (7.1.2); EGA IV (20.2.8), “special case”.
- [`AlgebraicGeometry.Scheme.RationalMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.RationalMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L139) (StacksFrontier): “(2) rational map”. References: EGA I (7.1.2).
- [`AlgebraicGeometry.Scheme.RationalMap.IsOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.RationalMap.IsOver#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L140) (StacksFrontier): “(3) S-rational map”. References: EGA I (7.1.2); EGA IV (18.10.19); SGA 3 XVIII (1.5), “special case”.

## Tag 0BX8, a lemma

[Tag 0BX8](https://stacks.math.columbia.edu/tag/0BX8) in the Stacks Project.

**`AlgebraicGeometry.GenericPointMapContext.bijective_genericPointMapForRationalMaps_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapFinitePresentation.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapFinitePresentation.lean#L279). The attribute's comment: “finite_presentation_bijectivity”. References: EGA IV (20.3.7), “bijectivity (fin pres)”; EGA I (7.1.11), “bijectivity”.

> When the target is locally of finite presentation over the base, every
> compatible collection of points and local maps at the generic points comes
> from a unique rational map over the base.

```lean
public theorem bijective_genericPointMapForRationalMaps_of_locallyOfFinitePresentation
    [LocallyOfFinitePresentation C.toBaseTarget] :
    Function.Bijective C.genericPointMapForRationalMaps
```

**`AlgebraicGeometry.GenericPointMapContext.genericPointMapForRationalMaps_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapInjective.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapInjective.lean#L76). The attribute's comment: “injectivity”. References: EGA IV (20.2.11), “(i)”; EGA IV (20.3.7), “injectivity”; EGA I (7.1.11), “injectivity”.

> A rational map over the base is determined by its values and induced local
> maps at the generic points of the irreducible components when the target is
> locally of finite type over the base.

```lean
public theorem genericPointMapForRationalMaps_injective
    (C : GenericPointMapContext.{u}) [LocallyOfFiniteType C.toBaseTarget] :
    Function.Injective C.genericPointMapForRationalMaps
```

**`AlgebraicGeometry.GenericPointMapContext.bijective_genericPointMapForRationalMaps_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapReduced.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericPointMapReduced.lean#L203). The attribute's comment: “reduced_source_bijectivity”. References: EGA IV (20.2.11), “(ii) reduced case”; EGA I (7.1.11), “bijectivity, X reduced”.

> For a reduced source and a target locally of finite type over the base,
> rational maps over the base are determined by, and realize, arbitrary
> compatible local data at the generic points of the source.

```lean
public theorem bijective_genericPointMapForRationalMaps_of_isReduced
    [LocallyOfFiniteType C.toBaseTarget] [IsReduced C.X] :
    Function.Bijective C.genericPointMapForRationalMaps
```

## Tag 01RT, a definition

[Tag 01RT](https://stacks.math.columbia.edu/tag/01RT) in the Stacks Project.

**`AlgebraicGeometry.Scheme.rationalFunctions`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/Basic.lean#L117). References: EGA I (7.1.2); EGA IV (20.2.8), “special case”.

> A rational function on a scheme is a rational map to the affine line over the integers.

```lean
abbrev Scheme.rationalFunctions (X : Scheme.{u}) : Type u
```

## Tag 01RU, a definition

[Tag 01RU](https://stacks.math.columbia.edu/tag/01RU) in the Stacks Project.

**`Stacks.Chow.rationalFunctionsRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions.lean#L466).

> **Stacks 01RU.** The ring structure on rational maps to the affine line is the one induced
> by the ring operations on sections on every dense open: there is a commutative ring structure on
> `R(X)` for which, for every dense open `U ⊆ X`, the map sending a section `s ∈ Γ(X, U)` to the
> rational function it represents is a ring homomorphism.

```lean
theorem rationalFunctionsRing (X : Scheme.{u}) :
    ∃ R : CommRing (rationalFunctions X),
      letI := R
      ∀ U : DenseOpen X,
        ∃ φ : Γ(X, U.1) →+* rationalFunctions X,
          ∀ s, φ s = ofSection X U s
```

## Tag 01RV, a lemma

[Tag 01RV](https://stacks.math.columbia.edu/tag/01RV) in the Stacks Project.

**`Stacks.Chow.rationalFunctionsEquivStalks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean#L592). The attribute's comment: “product of generic local rings”. References: EGA I (7.1.13), “more general”; EGA I (7.1.5), “more general”; EGA I (7.1.8), “partial”; EGA I (7.3.3), “partial”; SGA 1 I (10.3), “more general”; SGA 4 IX (4.0), “partial”.

> **Stacks 01RV.** The rational functions of a scheme with finitely many irreducible
> components are the product of the local rings at the generic points of those components; the
> identification sends a section on a dense open to its family of germs.

```lean
def rationalFunctionsEquivStalks (X : Scheme.{u}) [Finite (irreducibleComponents X)] :
    { e : rationalFunctions X ≃+*
        (∀ Z : irreducibleComponents X, X.presheaf.stalk Z.2.1.genericPoint) //
      ∀ (U : DenseOpen X) (s : Γ(X, U.1)) (Z : irreducibleComponents X)
        (h : Z.2.1.genericPoint ∈ U.1),
        e (ofSection X U s) Z = X.presheaf.germ U.1 Z.2.1.genericPoint h s }
```

**`Stacks.Chow.rationalFunctionsEquivResidueFields`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean#L608). The attribute's comment: “product of generic residue fields”. References: EGA I (7.3.3), “special case”; SGA 1 I (10.3), “special case”; SGA 4 IX (4.0), “special case”.

> **Stacks 01RV.** On a reduced scheme the generic local rings are the residue fields at the
> generic points, so the rational functions are their product.

```lean
def rationalFunctionsEquivResidueFields (X : Scheme.{u}) [Finite (irreducibleComponents X)]
    [IsReduced X] :
    { e : rationalFunctions X ≃+*
        (∀ Z : irreducibleComponents X, X.residueField Z.2.1.genericPoint) //
      ∀ (U : DenseOpen X) (s : Γ(X, U.1)) (Z : irreducibleComponents X)
        (h : Z.2.1.genericPoint ∈ U.1),
        e (ofSection X U s) Z = X.evaluation U.1 Z.2.1.genericPoint h s }
```

**`Stacks.Chow.rationalFunctionsEquivFunctionField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean#L625). The attribute's comment: “integral function field”. References: EGA I (7.1.5), “integral case”.

> **Stacks 01RV.** On an integral scheme the rational functions are the function field, that
> is, the stalk at the generic point.

```lean
def rationalFunctionsEquivFunctionField (X : Scheme.{u}) [IsIntegral X] :
    { e : rationalFunctions X ≃+* X.functionField //
      ∀ (U : DenseOpen X) (s : Γ(X, U.1)) (h : genericPoint X ∈ U.1),
        e (ofSection X U s) = X.presheaf.germ U.1 (genericPoint X) h s }
```

**`Stacks.Chow.rationalFunctionsEquivResidueField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean#L666). The attribute's comment: “integral residue field”. References: EGA I (7.1.5), “κ(η) when integral”.

> **Stacks 01RV.** On an integral scheme the rational functions are the residue field of the
> generic point.

```lean
def rationalFunctionsEquivResidueField (X : Scheme.{u}) [IsIntegral X] :
    { e : rationalFunctions X ≃+* X.residueField (genericPoint X) //
      ∀ (U : DenseOpen X) (s : Γ(X, U.1)) (h : genericPoint X ∈ U.1),
        e (ofSection X U s) = X.evaluation U.1 (genericPoint X) h s }
```

**`Stacks.Chow.isField_rationalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/FunctionField.lean#L682). The attribute's comment: “field property”. References: EGA I (7.1.5), “field when integral”; EGA I (7.1.8), “special case”.

> **Stacks 01RV.** The ring of rational functions of an integral scheme is a field.

```lean
theorem isField_rationalFunctions (X : Scheme.{u}) [IsIntegral X] :
    IsField (rationalFunctions X)
```

## Tag 01RW, a definition

[Tag 01RW](https://stacks.math.columbia.edu/tag/01RW) in the Stacks Project.

**`AlgebraicGeometry.Scheme.functionFieldOfRationalFunctions`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/FunctionField.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/FunctionField.lean#L44).

> The *function field*, or *field of rational functions*, of an integral scheme `X`: the ring
> `R(X)` of rational functions on `X`, which is a field because `X` is integral.

```lean
abbrev functionFieldOfRationalFunctions (X : Scheme.{u}) [IsIntegral X] : Type u
```

## Tag 02NF, a lemma

[Tag 02NF](https://stacks.math.columbia.edu/tag/02NF) in the Stacks Project.

**`Stacks.Chow.not_subset_range_genericStalk_of_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/LocalRings.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/LocalRings.lean#L69). The attribute's comment: “noninclusion of local rings”. References: EGA I (8.2.4); EGA I (8.2.3), “sufficiency direction”.

> **Stacks Project, Tag 02NF.** On an integral separated scheme, if an irreducible closed
> subset `Z₁` is not contained in an irreducible closed subset `Z₂`, then the local ring at the
> generic point of `Z₁` is not contained in the local ring at the generic point of `Z₂`, as
> subrings of the field of rational functions.

```lean
theorem not_subset_range_genericStalk_of_not_le (X : Scheme.{u})
    [IsIntegral X] [Scheme.IsSeparated X] (Z₁ Z₂ : IrreducibleCloseds X) (hZ : ¬ Z₁ ≤ Z₂) :
    ¬ Set.range (algebraMap (X.presheaf.stalk Z₁.isIrreducible.genericPoint) X.functionField) ⊆
      Set.range (algebraMap (X.presheaf.stalk Z₂.isIrreducible.genericPoint)
        X.functionField)
```

**`Stacks.Chow.exists_section_notMem_range_genericStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/LocalRings.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalFunctions/LocalRings.lean#L143). The attribute's comment: “closed-point neighbourhood form”. References: EGA I (8.2.4), “closed point case”; EGA I (8.2.3), “closed point, separated”.

> **Stacks Project, Tag 02NF.** On an integral separated scheme, a closed point `x` outside an
> irreducible closed subset `Z` carries a function regular on a neighbourhood of `x` whose class
> in the field of rational functions does not lie in the local ring at the generic point of
> `Z`.

```lean
theorem exists_section_notMem_range_genericStalk (X : Scheme.{u})
    [IsIntegral X] [Scheme.IsSeparated X] (Z : IrreducibleCloseds X) (x : X)
    (hx : IsClosed ({x} : Set X)) (hxZ : x ∉ Z) :
    ∃ (U : X.Opens) (hxU : x ∈ U) (s : Γ(X, U)),
      algebraMap (X.presheaf.stalk x) X.functionField (X.presheaf.germ U x hxU s) ∉
        Set.range (algebraMap (X.presheaf.stalk Z.isIrreducible.genericPoint)
          X.functionField)
```

## Tag 0A1X, a definition

[Tag 0A1X](https://stacks.math.columbia.edu/tag/0A1X) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.RationalMap.domain`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.RationalMap.domain#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L265) (StacksFrontier): “the domain of definition”. References: EGA I (7.2.1); EGA IV (18.10.19); EGA IV (20.2.3), “special case”.
- [`AlgebraicGeometry.Scheme.RationalMap.mem_domain`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.RationalMap.mem_domain#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L266) (StacksFrontier): “a point is in it iff some representative is defined there”. References: EGA I (7.2.1); EGA IV (20.2.3), “special case”.

## Tag 0A1Y, a lemma

[Tag 0A1Y](https://stacks.math.columbia.edu/tag/0A1Y) in the Stacks Project.

**`AlgebraicGeometry.Scheme.RationalMap.existsUnique_hom_domain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/DomainOfDefinition.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/DomainOfDefinition.lean#L59). The attribute's comment: “existence and uniqueness of the morphism on the domain of definition”. References: EGA I (7.2.2), “special case”; EGA IV (20.2.4), “special case”; EGA IV (20.2.8), “special case”; EGA IV (20.3.2), “special case”.

> Let `X` and `Y` be schemes with `X` reduced and `Y` separated, and let `φ` be a rational map
> from `X` to `Y` with domain of definition `φ.domain`. There is exactly one morphism
> `φ.domain ⟶ Y` representing `φ`, that is, exactly one morphism on the domain of definition whose
> partial map lies in the equivalence class `φ`.

```lean
theorem existsUnique_hom_domain [IsReduced X] [Y.IsSeparated] (φ : X ⤏ Y) :
    ∃! f : φ.domain.toScheme ⟶ Y,
      (PartialMap.mk φ.domain φ.dense_domain f).toRationalMap = φ
```

**`AlgebraicGeometry.Scheme.RationalMap.isOver_of_toRationalMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/DomainOfDefinition.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/DomainOfDefinition.lean#L77). The attribute's comment: “the morphism on the domain of definition is a morphism over a separated base”. References: EGA IV (20.2.5), “special case”.

> Let `X` and `Y` be schemes over a separated scheme `S`, with `X` reduced and `Y` separated,
> and let `φ` be an `S`-rational map from `X` to `Y`. Then the morphism on the domain of definition
> of `φ` that represents `φ` is a morphism over `S`.

```lean
theorem isOver_of_toRationalMap_eq [X.Over S] [Y.Over S] [IsReduced X] [Y.IsSeparated]
    [S.IsSeparated] (φ : X ⤏ Y) [φ.IsOver S] {f : φ.domain.toScheme ⟶ Y}
    (hf : (PartialMap.mk φ.domain φ.dense_domain f).toRationalMap = φ) :
    f.IsOver S
```

## Tag 0A20, a definition

[Tag 0A20](https://stacks.math.columbia.edu/tag/0A20) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.BirationalOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.BirationalOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean#L92) (StacksFrontier): “(2)”.

## Tag 0BAA, a lemma

[Tag 0BAA](https://stacks.math.columbia.edu/tag/0BAA) in the Stacks Project.

**`AlgebraicGeometry.birational_iff_exists_nonempty_open_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/BirationalOpenIso.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/BirationalOpenIso.lean#L40). The attribute's comment: “part (1)”.

> Two irreducible schemes are birational if and only if they have isomorphic
> nonempty open subschemes.

```lean
public theorem birational_iff_exists_nonempty_open_iso
    {X Y : Scheme.{u}} [IrreducibleSpace X] [IrreducibleSpace Y] :
    Scheme.Birational X Y ↔
      ∃ (U : X.Opens) (V : Y.Opens),
        (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
          Nonempty (U.toScheme ≅ V.toScheme)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.birationalOver_iff_exists_nonempty_open_iso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/BirationalOpenIso.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/BirationalOpenIso.lean#L49) (StacksFrontier): “part (2)”.

## Tag 01RX, a remark

[Tag 01RX](https://stacks.math.columbia.edu/tag/01RX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.PseudoMap`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L82). The attribute's comment: “the pseudo-maps: morphisms into `Y` defined on scheme-theoretically dense opens of `X`, the objects whose equivalence classes the remark calls pseudo-morphisms”.

> A pseudo-map from `X` to `Y` is a morphism into `Y` defined on a scheme-theoretically dense
> open subscheme of `X`. This is the variant of `AlgebraicGeometry.Scheme.PartialMap` in which the
> domain of definition is required to be scheme-theoretically dense.

```lean
structure PseudoMap (X Y : Scheme.{u})
```

**`AlgebraicGeometry.Scheme.PseudoMap.equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L140). The attribute's comment: “the equivalence relation on pseudo-maps: agreement after restriction to a scheme-theoretically dense open”. References: EGA IV (20.2.1).

> Two pseudo-maps are equivalent if they agree after restriction to a scheme-theoretically
> dense open subscheme.

```lean
protected noncomputable def equiv (f g : X.PseudoMap Y) : Prop
```

**`AlgebraicGeometry.Scheme.PseudoMap.equivalence_rel`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L169). The attribute's comment: “equivalence relation, via stability of scheme-theoretic density under intersection (Tag 01RF)”.

> Equivalence of pseudo-maps is an equivalence relation.

```lean
lemma equivalence_rel : Equivalence (@Scheme.PseudoMap.equiv X Y)
```

**`AlgebraicGeometry.Scheme.PseudoMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L188). The attribute's comment: “the pseudo-morphisms from `X` to `Y`: the equivalence classes of pseudo-maps”.

> A pseudo-morphism from `X` to `Y` is an equivalence class of pseudo-maps, where two
> pseudo-maps are equivalent if they agree on a scheme-theoretically dense open subscheme.

```lean
noncomputable def PseudoMorphism (X Y : Scheme.{u}) : Type u
```

**`AlgebraicGeometry.Scheme.PseudoMorphism.IsOver`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L206). The attribute's comment: “the `S`-pseudo-morphisms: the analogue for pseudo-morphisms of part (3) of the definition of an `S`-rational map”.

> A pseudo-morphism is an `S`-pseudo-morphism if some pseudo-map in the equivalence class is
> an `S`-morphism.

```lean
class PseudoMorphism.IsOver [X.Over S] [Y.Over S] (f : X.PseudoMorphism Y) : Prop
```

**`AlgebraicGeometry.Scheme.PseudoMorphism.equivRationalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/PseudoMorphism.lean#L262). The attribute's comment: “agreement of pseudo-morphisms with rational maps for reduced `X`”. References: EGA IV (20.2.7); EGA IV (20.4.3), “Identification”.

> If `X` is reduced, pseudo-morphisms from `X` to `Y` are the same thing as rational maps from
> `X` to `Y`.

```lean
noncomputable def PseudoMorphism.equivRationalMap : X.PseudoMorphism Y ≃ X.RationalMap Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.50, Tag 01RR](https://stacks.math.columbia.edu/tag/01RR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
