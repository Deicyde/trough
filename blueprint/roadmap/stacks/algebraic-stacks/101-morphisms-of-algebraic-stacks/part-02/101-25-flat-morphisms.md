---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsFlat, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_twoFibreProduct_fst_descent, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_of_isSurjective_of_isFlat_comp, AlgebraicGeometry.Stack.AlgebraicStacks.exists_valuationRing_extension_lift_of_isFlat
statement: formalized
proof: formalized
---

# 101.25 Flat morphisms

Section 101.25 of the Stacks Project, [Tag 06PV](https://stacks.math.columbia.edu/tag/06PV). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06PW, a definition

[Tag 06PW](https://stacks.math.columbia.edu/tag/06PW) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatAlgebraicStack.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatAlgebraicStack.lean#L84).

> **Stacks 06PW.** A 1-morphism of algebraic stacks over `S` is *flat* when it passes the
> existential smooth-diagram test of Stacks 06FM at flatness of morphisms of algebraic spaces:
> there are algebraic spaces `U`, `V` over `S`, a smooth 1-morphism `a` from the category fibred in
> groupoids of `U` to the source which is surjective on objects, a smooth 1-morphism `b` from the
> one of `V` to the target, and a morphism `h : U ⟶ V` making the square 2-commute, with `h` a flat
> morphism of algebraic spaces.

```lean
abbrev IsFlat {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06PX, a lemma

[Tag 06PX](https://stacks.math.columbia.edu/tag/06PX) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismComp.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismComp.lean#L181).

> **Stacks 06PX.** The composite of two flat 1-morphisms of algebraic stacks over `S` is flat.
>
> Stacks 06PW is condition (2) of Stacks 06FM at flatness of morphisms of algebraic spaces, on the
> nose (`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_hasPropertyOnSomeSmoothDiagram`), so
> this is Stacks 06FP at that property: flatness is smooth local on the source-and-target by
> **Stacks 06FC** and stable under composition by **Stacks 03MN**, which is the source's own
> proof.

```lean
theorem isFlat_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsFlat B S hS f) (hg : IsFlat B S hS g) :
    IsFlat B S hS (f ≫ g)
```

## Tag 06PY, a lemma

[Tag 06PY](https://stacks.math.columbia.edu/tag/06PY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatBaseChange.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatBaseChange.lean#L77).

> A base change of a flat 1-morphism of algebraic stacks over `S` is flat: if `P` is a 2-fibre
> product of the cospan `(g, f)` and `f` is flat, then the projection `P.fst` is flat.

```lean
theorem isFlat_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsFlat B S hS f) :
    IsFlat B S hS P.fst
```

## Tag 06PZ, a lemma

[Tag 06PZ](https://stacks.math.columbia.edu/tag/06PZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_twoFibreProduct_fst_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatDescentAlgebraicStack.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatDescentAlgebraicStack.lean#L346).

> **Stacks 06PZ.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒵 ⟶ 𝒴` be 1-morphisms of algebraic stacks over
> `S` with `g` surjective and flat, and let `P` exhibit `𝒵 ×_𝒴 𝒳`. If the base change
> `𝒵 ×_𝒴 𝒳 ⟶ 𝒵` is flat, then `f` is flat.
>
> This is `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_of_isFlat_twoFibreProduct_fst` with its
> hypothesis discharged by [Stacks Project, Tag 05VY].

```lean
theorem isFlat_twoFibreProduct_fst_descent
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hgsurj : Stack.IsSurjective B S hS g)
    (hgflat : IsFlat B S hS g)
    (hfst : IsFlat B S hS P.fst) :
    IsFlat B S hS f
```

## Tag 06Q0, a lemma

[Tag 06Q0](https://stacks.math.columbia.edu/tag/06Q0) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_of_isSurjective_of_isFlat_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatDescentAlgebraicStack.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatDescentAlgebraicStack.lean#L328).

> **Stacks 06Q0.** Let `𝒳 ⟶ 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over `S`. If
> `𝒳 ⟶ 𝒵` is flat and `𝒳 ⟶ 𝒴` is surjective and flat, then `𝒴 ⟶ 𝒵` is flat.
>
> This is `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_of_comp_of_isSurjective_of_isFlat` with
> its hypothesis discharged by [Stacks Project, Tag 05VY].

```lean
theorem isFlat_of_isSurjective_of_isFlat_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsFlat B S hS (f ≫ g))
    (hfsurj : Stack.IsSurjective B S hS f)
    (hfflat : IsFlat B S hS f) :
    IsFlat B S hS g
```

## Tag 0DN5, a lemma

[Tag 0DN5](https://stacks.math.columbia.edu/tag/0DN5) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_valuationRing_extension_lift_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatValuativeLifting.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatValuativeLifting.lean#L126).

> **Stacks 0DN5.** Let `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks over `S` and let
> `g : Spec A ⟶ 𝒴` be a 1-morphism out of the spectrum of a valuation ring `A`, presented as an
> object `V` of the big fppf site of `S` with an isomorphism `e` of its underlying scheme with
> `Spec A`. If the closed point of `Spec A` — presented by a field-valued point `p` of the
> algebraic space `V` represents — is carried by `g` to a point of `|𝒴|` in the image of
> `|𝒳| ⟶ |𝒴|`, then there are an extension of valuation rings `ι : A ⟶ A'`, an object `V'` of the
> site with an isomorphism `e'` of its underlying scheme with `Spec A'` over `Spec ι`, and a
> 1-morphism `Spec A' ⟶ 𝒳` whose composite with `f` is 2-isomorphic to `Spec A' ⟶ Spec A ⟶ 𝒴`.

```lean
theorem exists_valuationRing_extension_lift_of_isFlat
    (A : Type u) [CommRing A] [IsDomain A] [ValuationRing A]
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsFlat B S hS f)
    (V : BigFppfOver B S hS)
    (e : (BigFppfOver.toScheme B S hS).obj V ≅ Spec (.of A))
    (g : schemeStack.{u, w} B S hS V ⟶ 𝒴)
    (p : Space.FieldValuedPoint B S hS (yoneda.obj V))
    (hp : e.hom ((BigFppfOver.toScheme B S hS).map p.value
      (IsLocalRing.closedPoint p.carrier)) = IsLocalRing.closedPoint A)
    (himage : ∃ x : points B S hS 𝒳, pointsMap B S hS f x =
      pointsMap B S hS g (spacePointMap B S hS (yoneda.obj V)
        (schemeFibredCategory B S hS V) (schemeRepChart B S hS V)
        (p.class B S hS (yoneda.obj V)))) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : IsDomain A') (_ : ValuationRing A') (ι : A →+* A'),
      ValuationRing.IsExtension ι ∧
      ∃ (V' : BigFppfOver B S hS)
        (e' : (BigFppfOver.toScheme B S hS).obj V' ≅ Spec (.of A'))
        (j : V' ⟶ V) (lift : schemeStack.{u, w} B S hS V' ⟶ 𝒳),
        (BigFppfOver.toScheme B S hS).map j ≫ e.hom =
            e'.hom ≫ Spec.map (CommRingCat.ofHom ι) ∧
          Nonempty (lift ≫ f ≅ schemeStackMap.{u, w} B S hS j ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.25, Tag 06PV](https://stacks.math.columbia.edu/tag/06PV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
