---
declaration: section
origin: cited
lean: Stacks.RelativeCech.isEquivalence_fibreProductToNerve, Stacks.RelativeCech.isEquivalence_coordinate_zero, Stacks.Cech.complexPullbackMap, Stacks.Cech.complexPullbackMap_π, Stacks.Cech.isIso_complexPullbackMap, Stacks.Cech.nonempty_complexIso_of_natIso, Stacks.Cech.nonempty_homotopy_extendedComplex_id_zero
statement: formalized
proof: formalized
---

# 96.18 The Čech complex

Section 96.18 of the Stacks Project, [Tag 06X3](https://stacks.math.columbia.edu/tag/06X3). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06X3, the section

[Tag 06X3](https://stacks.math.columbia.edu/tag/06X3) in the Stacks Project.

**`Stacks.RelativeCech.isEquivalence_fibreProductToNerve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean#L204). The attribute's comment: “the nerve in degree n + 1 is the 2-fibre product of the covering with degree n”.

> The degree `n + 1` piece of the Čech nerve of a covering `f : U ⥤ X` is the 2-fibre product
> `U ×_X U_n` of the covering with the degree `n` piece: prepending a coordinate is an equivalence
> of categories.

```lean
public theorem isEquivalence_fibreProductToNerve (n : ℕ) :
    (fibreProductToNerve p f n).IsEquivalence
```

**`Stacks.RelativeCech.isEquivalence_coordinate_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean#L223). The attribute's comment: “the nerve in degree zero is the covering”.

> The degree `0` piece of the Čech nerve of a covering `f : U ⥤ X` is the covering `U` itself:
> reading off the single coordinate of a tuple is an equivalence of categories.

```lean
public theorem isEquivalence_coordinate_zero :
    (Tuple.coordinate p f (0 : Fin 1)).IsEquivalence
```

## Tag 06X5, a lemma

[Tag 06X5](https://stacks.math.columbia.edu/tag/06X5) in the Stacks Project.

**`Stacks.Cech.complexPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L328). The attribute's comment: “part (1), the morphism of complexes”.

> **Stacks 06X5 (1).** A `2`-commutative square of coverings over the base induces a morphism
> of Čech complexes `Č(U → X, F) ⟶ Č(V → Y, e⁻¹F)`, given in degree `n` by pullback along the
> induced functor `V_n ⥤ U_n` of Čech nerves.

```lean
public def complexPullbackMap : complex pX f F ⟶ complex pY g (e.op ⋙ F)
```

**`Stacks.Cech.complexPullbackMap_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L334). The attribute's comment: “part (1), the degreewise description”.

> **Stacks 06X5 (1).** The morphism of Čech complexes is pullback along the induced functor of
> Čech nerves, degreewise on the limit cones.

```lean
public theorem complexPullbackMap_π (n : ℕ) (a : Tuple pY g n) :
    (complexPullbackMap pX pY f g h e α he hα F).f n ≫
        limit.π ((Tuple.projection pY g n).op ⋙ e.op ⋙ F) (op a) =
      limit.π ((Tuple.projection pX f n).op ⋙ F)
        (op ((nerveMap pX pY f g h e α he hα n).obj a))
```

**`Stacks.Cech.isIso_complexPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L344). The attribute's comment: “part (2)”.

> **Stacks 06X5 (2).** If the two horizontal functors of the square are equivalences, the
> morphism of Čech complexes of part (1) is an isomorphism.

```lean
public theorem isIso_complexPullbackMap [h.IsEquivalence] [e.IsEquivalence]
    (hpV : (g ⋙ pY).IsFiberedInGroupoids) :
    IsIso (complexPullbackMap pX pY f g h e α he hα F)
```

**`Stacks.Cech.nonempty_complexIso_of_natIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L362). The attribute's comment: “part (3)”.

> **Stacks 06X5 (3).** `2`-isomorphic coverings `f, f' : U ⥤ X` have isomorphic Čech
> complexes.

```lean
public theorem nonempty_complexIso_of_natIso [Preadditive A] (p : X ⥤ C) (f f' : U ⥤ X)
    (α : f ≅ f') (hα : ∀ u : U, p.IsHomLift (𝟙 (p.obj (f.obj u))) (α.hom.app u))
    (hpU' : (f' ⋙ p).IsFiberedInGroupoids) (F : Xᵒᵖ ⥤ A)
    [∀ n : ℕ, HasLimitsOfShape (Tuple p f n)ᵒᵖ A]
    [∀ n : ℕ, HasLimitsOfShape (Tuple p f' n)ᵒᵖ A] :
    Nonempty (complex p f F ≅ complex p f' F)
```

## Tag 06X6, a lemma

[Tag 06X6](https://stacks.math.columbia.edu/tag/06X6) in the Stacks Project.

**`Stacks.Cech.nonempty_homotopy_extendedComplex_id_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean#L407).

> **Stacks 06X6.** If there is a `1`-morphism `s : X ⥤ U` such that `f ∘ s` is `2`-isomorphic
> to `id_X`, then the extended Čech complex is homotopic to zero: its identity is homotopic to its
> zero endomorphism.

```lean
public theorem nonempty_homotopy_extendedComplex_id_zero (s : X ⥤ U) (t : s ⋙ f ≅ 𝟭 X)
    (ht : ∀ x : X, p.IsHomLift (𝟙 (p.obj x)) (t.hom.app x)) :
    Nonempty (Homotopy (𝟙 (extendedComplex p f F)) 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.18, Tag 06X3](https://stacks.math.columbia.edu/tag/06X3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
