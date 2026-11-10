---
declaration: section
origin: cited
lean: AlgebraicGeometry.SatisfiesDescent, AlgebraicGeometry.DescentData.isFamilyEffective_affineBase_of_affineSingleton, AlgebraicGeometry.DescentData.isFamilyEffective_affineBase_fpqc_of_affineSingleton, AlgebraicGeometry.DescentData.isFamilyEffective_of_affineSingleton, AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton, AlgebraicGeometry.DescentData.isFamilyEffective_of_affineSingleton_of_anyIndex, AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton_of_anyIndex, AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffine
statement: formalized
proof: formalized
---

# 35.36 Descending types of morphisms

Section 35.36 of the Stacks Project, [Tag 02W1](https://stacks.math.columbia.edu/tag/02W1). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02W2, a definition

[Tag 02W2](https://stacks.math.columbia.edu/tag/02W2) in the Stacks Project.

**`AlgebraicGeometry.SatisfiesDescent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/MorphismDescent.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/MorphismDescent.lean#L47).

> **Stacks Project, Tag 02W2.** Morphisms with property `P` satisfy descent for the coverings
> of a precoverage `K` if every descent datum relative to a `K`-covering whose components are
> `P`-morphisms is effective.

```lean
abbrev SatisfiesDescent (P : MorphismProperty Scheme.{u}) (K : Precoverage Scheme.{u}) : Prop
```

## Tag 02W3, a lemma

[Tag 02W3](https://stacks.math.columbia.edu/tag/02W3) in the Stacks Project.

**`AlgebraicGeometry.DescentData.isFamilyEffective_affineBase_of_affineSingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphisms.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphisms.lean#L142). The attribute's comment: “the case of an affine base, for τ = fppf, étale, smooth and syntomic”.

> **Stacks Project, Tag 02W3, the case of an affine base, for the fppf, étale, smooth and
> syntomic coverings.** Let `P` be a property of morphisms of schemes over a base which is stable
> under any base change and such that a nonempty finite disjoint union of morphisms with `P` again
> has `P`. Let `τ` be one of fppf, étale, smooth and syntomic, and suppose that for every
> surjective morphism of affine schemes which is flat of finite presentation, étale, smooth or
> syntomic according to `τ`, every descent datum relative to it whose member has `P` is effective.
> Then every descent datum relative to a `τ`-covering of an affine scheme whose members have `P`
> is effective.

```lean
theorem isFamilyEffective_affineBase_of_affineSingleton
    {P : MorphismProperty Scheme.{u}} [P.IsStableUnderBaseChange]
    (τ : CoveringTopology) (hτ : τ ≠ .zariski)
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → coveringMorphismProperty τ a →
      ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {S : Scheme.{u}} [IsAffine S] (𝒰 : PreZeroHypercover.{u} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.precoverage (coveringMorphismProperty τ) S)
    (D : DescentData 𝒰.f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_affineBase_fpqc_of_affineSingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphisms.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphisms.lean#L174). The attribute's comment: “the case of an affine base, for τ = fpqc”.

> **Stacks Project, Tag 02W3, the case of an affine base, for the fpqc coverings.** Let `P` be
> a property of morphisms of schemes over a base which is stable under any base change and such
> that a nonempty finite disjoint union of morphisms with `P` again has `P`. Suppose that for
> every surjective flat morphism of affine schemes, every descent datum relative to it whose
> member has `P` is effective. Then every descent datum relative to an fpqc covering of an affine
> scheme whose members have `P` is effective.

```lean
theorem isFamilyEffective_affineBase_fpqc_of_affineSingleton
    {P : MorphismProperty Scheme.{u}} [P.IsStableUnderBaseChange]
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → Flat a → ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {S : Scheme.{u}} [IsAffine S] (𝒰 : PreZeroHypercover.{u} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData 𝒰.f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_affineSingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean#L121). The attribute's comment: “for τ = fppf, étale, smooth and syntomic, over an arbitrary base, for a covering family indexed in the universe of the schemes”.

> **Stacks Project, Tag 02W3, for the fppf, étale, smooth and syntomic coverings.** Let `P` be
> a property of morphisms of schemes over a base which is stable under any base change and such
> that a nonempty finite disjoint union of morphisms with `P` again has `P`. Let `τ` be one of
> fppf, étale, smooth and syntomic, and suppose that for every surjective morphism of affine
> schemes which is flat of finite presentation, étale, smooth or syntomic according to `τ`, every
> descent datum relative to it whose member has `P` is effective. Then every descent datum
> relative to a `τ`-covering of an arbitrary scheme whose members have `P` is effective.

```lean
theorem isFamilyEffective_of_affineSingleton [P.IsStableUnderBaseChange]
    (τ : CoveringTopology) (hτ : τ ≠ .zariski)
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → coveringMorphismProperty τ a →
      ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {S : Scheme.{u}} (𝒰 : PreZeroHypercover.{u} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.precoverage (coveringMorphismProperty τ) S)
    (D : DescentData 𝒰.f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean#L150). The attribute's comment: “for τ = fpqc, over an arbitrary base, for a covering family indexed in the universe of the schemes”.

> **Stacks Project, Tag 02W3, for the fpqc coverings.** Let `P` be a property of morphisms of
> schemes over a base which is stable under any base change and such that a nonempty finite
> disjoint union of morphisms with `P` again has `P`. Suppose that for every surjective flat
> morphism of affine schemes, every descent datum relative to it whose member has `P` is
> effective. Then every descent datum relative to an fpqc covering of an arbitrary scheme whose
> members have `P` is effective.

```lean
theorem isFamilyEffective_fpqc_of_affineSingleton [P.IsStableUnderBaseChange]
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → Flat a → ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {S : Scheme.{u}} (𝒰 : PreZeroHypercover.{u} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData 𝒰.f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_affineSingleton_of_anyIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean#L178). The attribute's comment: “for τ = fppf, étale, smooth and syntomic, over an arbitrary base, for a covering family indexed in an arbitrary universe”.

> **Stacks Project, Tag 02W3, for the fppf, étale, smooth and syntomic coverings, with no
> restriction on the index type of the covering family.** Let `P` be a property of morphisms of
> schemes over a base which is stable under any base change and such that a nonempty finite
> disjoint union of morphisms with `P` again has `P`. Let `τ` be one of fppf, étale, smooth and
> syntomic, and suppose that for every surjective morphism of affine schemes which is flat of
> finite presentation, étale, smooth or syntomic according to `τ`, every descent datum relative to
> it whose member has `P` is effective. Then every descent datum relative to a `τ`-covering of an
> arbitrary scheme, indexed by a type in an arbitrary universe, whose members have `P` is
> effective.

```lean
theorem isFamilyEffective_of_affineSingleton_of_anyIndex [P.IsStableUnderBaseChange]
    (τ : CoveringTopology) (hτ : τ ≠ .zariski)
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → coveringMorphismProperty τ a →
      ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {I : Type v} {S : Scheme.{u}} {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.precoverage (coveringMorphismProperty τ) S)
    (D : DescentData f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton_of_anyIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/DescendingTypesOfMorphismsGeneralBase.lean#L210). The attribute's comment: “for τ = fpqc, over an arbitrary base, for a covering family indexed in an arbitrary universe”.

> **Stacks Project, Tag 02W3, for the fpqc coverings, with no restriction on the index type of
> the covering family.** Let `P` be a property of morphisms of schemes over a base which is stable
> under any base change and such that a nonempty finite disjoint union of morphisms with `P` again
> has `P`. Suppose that for every surjective flat morphism of affine schemes, every descent datum
> relative to it whose member has `P` is effective. Then every descent datum relative to an fpqc
> covering of an arbitrary scheme, indexed by a type in an arbitrary universe, whose members have
> `P` is effective.

```lean
theorem isFamilyEffective_fpqc_of_affineSingleton_of_anyIndex [P.IsStableUnderBaseChange]
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (g : ∀ j, Y j ⟶ Z j), (∀ j, P (g j)) → P (Limits.Sigma.map g))
    (haffine : ∀ {A T : Scheme.{u}} [IsAffine A] [IsAffine T] (a : A ⟶ T),
      Surjective a → Flat a → ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    {I : Type v} {S : Scheme.{u}} {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcDescentReduction.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcDescentReduction.lean#L76). The attribute's comment: “the fpqc case over an affine base”.

> Let `P` be stable under base change and closed under finite disjoint unions, and let every
> descent datum relative to a surjective flat morphism of affine schemes whose component has `P` be
> effective.  Then over an affine base every descent datum relative to an fpqc covering whose
> components have `P` is effective.

```lean
theorem isFamilyEffective_of_isAffine
    [P.IsStableUnderBaseChange]
    (hcoprod : ∀ {J : Type u} [Finite J] [Nonempty J] {Y Z : J → Scheme.{u}}
      (a : ∀ j, Y j ⟶ Z j), (∀ j, P (a j)) → P (Limits.Sigma.map a))
    (haffine : ∀ {T Z : Scheme.{u}} [IsAffine T] [IsAffine Z] (a : Z ⟶ T),
      Surjective a → Flat a → ∀ E : DescentDatum a, P (E.obj ()).hom → E.IsEffective)
    [IsAffine S] (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hP : ∀ i, P (D.obj i).hom) :
    D.IsFamilyEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.36, Tag 02W1](https://stacks.math.columbia.edu/tag/02W1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
