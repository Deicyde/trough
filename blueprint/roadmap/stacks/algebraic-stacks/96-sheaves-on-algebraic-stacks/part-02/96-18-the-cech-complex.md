---
declaration: section
origin: cited
lean: Stacks.Cech.cosimplicial, Stacks.Cech.complex, Stacks.Cech.complex_d, Stacks.Cech.acyclic_extendedComplex_iff_quasiIso, Stacks.Cech.augmentation_comp_d, Stacks.Cech.extendedComplex, Stacks.RelativeCech.isEquivalence_fibreProductToNerve, Stacks.RelativeCech.isEquivalence_coordinate_zero
statement: formalized
proof: formalized
---

# 96.18 The Čech complex

Section 96.18 of the Stacks Project, [Tag 06X3](https://stacks.math.columbia.edu/tag/06X3). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06X3, the section

[Tag 06X3](https://stacks.math.columbia.edu/tag/06X3) in the Stacks Project.

**`Stacks.Cech.cosimplicial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L168). The attribute's comment: “the cosimplicial object n ↦ Γ(U\_n, f\_n⁻¹F)”.

> The cosimplicial object `n ↦ Γ(U_n, f_n⁻¹F)` underlying the Čech complex.

```lean
public def cosimplicial : CosimplicialObject A
```

**`Stacks.Cech.complex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L188). The attribute's comment: “the Čech complex Č(U → X, F)”.

> The Čech complex `Č(U → X, F)`: the cochain complex of the cosimplicial object
> `n ↦ Γ(U_n, f_n⁻¹F)`.

```lean
public def complex : CochainComplex A ℕ
```

**`Stacks.Cech.complex_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L196). The attribute's comment: “the differential of the Čech complex”.

> The differential of the Čech complex is the alternating sum of the coface pullback maps.

```lean
public theorem complex_d (n : ℕ) :
    (complex p f F).d n (n + 1) =
      ∑ i : Fin (n + 2), (-1 : ℤ) ^ (i : ℕ) • (cosimplicial p f F).δ i
```

**`Stacks.Cech.acyclic_extendedComplex_iff_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ExtendedComplexAcyclic.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ExtendedComplexAcyclic.lean#L146). The attribute's comment: “the extended Čech complex is acyclic iff Γ(X, F)[0] → Č is a quasi-isomorphism”.

> The extended Čech complex `… ⟶ 0 ⟶ Γ(X, F) ⟶ Γ(U_0, f_0⁻¹F) ⟶ Γ(U_1, f_1⁻¹F) ⟶ …`, with
> `Γ(X, F)` in degree `-1`, is acyclic if and only if the canonical morphism
> `Γ(X, F)[0] ⟶ Č(U → X, F)` is a quasi-isomorphism.

```lean
public theorem acyclic_extendedComplex_iff_quasiIso :
    (extendedComplex p f F).Acyclic ↔ QuasiIso (fromGlobalSections p f F)
```

**`Stacks.Cech.augmentation_comp_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean#L278). The attribute's comment: “Γ(X, F) → Γ(U\_0, f\_0⁻¹F) lies in the kernel of d⁰”.

> The map `Γ(X, F) ⟶ Γ(U_0, f_0⁻¹F)` lies in the kernel of the differential `d⁰` of the Čech
> complex: its two composites with the coface pullbacks `δ⁰` and `δ¹` agree, so their alternating
> sum vanishes.

```lean
public theorem augmentation_comp_d :
    augmentation p f F 0 ≫ (complex p f F).d 0 1 = 0
```

**`Stacks.Cech.extendedComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean#L301). The attribute's comment: “the extended Čech complex”.

> The extended Čech complex `… ⟶ 0 ⟶ Γ(X, F) ⟶ Γ(U_0, f_0⁻¹F) ⟶ Γ(U_1, f_1⁻¹F) ⟶ …`, with
> `Γ(X, F)` in degree `-1`.

```lean
public def extendedComplex : CochainComplex A ℤ
```

**`Stacks.RelativeCech.isEquivalence_fibreProductToNerve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean#L204). The attribute's comment: “the nerve in degree n + 1 is the 2-fibre product of the covering with degree n”.

> The degree `n + 1` piece of the Čech nerve of a covering `f : U ⥤ X` is the 2-fibre product
> `U ×_X U_n` of the covering with the degree `n` piece: prepending a coordinate is an equivalence
> of categories.

```lean
public theorem isEquivalence_fibreProductToNerve (n : ℕ) :
    (fibreProductToNerve p f n).IsEquivalence
```

**`Stacks.RelativeCech.isEquivalence_coordinate_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveFibreProduct.lean#L223). The attribute's comment: “the nerve in degree zero is the covering”.

> The degree `0` piece of the Čech nerve of a covering `f : U ⥤ X` is the covering `U` itself:
> reading off the single coordinate of a tuple is an equivalence of categories.

```lean
public theorem isEquivalence_coordinate_zero :
    (Tuple.coordinate p f (0 : Fin 1)).IsEquivalence
```

**`Stacks.RelativeCech.coordinateZeroCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean#L48). The attribute's comment: “f\_0 = f”.

> `f_0 = f`: under the identification `U_0 ≃ U` by the single coordinate
> (`Stacks.RelativeCech.isEquivalence_coordinate_zero`), the projection `f_0 : U_0 ⥤ X` is `f`, the
> isomorphism being given by the comparison isomorphisms of the tuples, which lie over identities
> of the base (`Stacks.RelativeCech.coordinateZeroCompIso_hom_app_isHomLift`).

```lean
public def coordinateZeroCompIso :
    Tuple.coordinate p f (0 : Fin 1) ⋙ f ≅ Tuple.projection p f 0
```

**`Stacks.RelativeCech.nerve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean#L74). The attribute's comment: “the simplicial object U\_•, whose maps compose on the nose over X”.

> The simplicial object `U_•` of the Čech nerve of `f : U ⥤ X`: the category `U_n` of tuples in
> degree `n`, and the reindexing functor `U_φ` along each map `φ : [m] ⟶ [n]`. These compose on the
> nose (`Stacks.RelativeCech.Tuple.reindex_comp`) and are `1`-morphisms over `X`
> (`Stacks.RelativeCech.projection_reindex`).

```lean
public def nerve : SimplicialObject Cat.{max vU vX, max uU uX vX}
```

**`Stacks.RelativeCech.nerve_map_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/NerveSimplicial.lean#L88). The attribute's comment: “the maps of U\_• are 1-morphisms over X”.

> The reindexing functors of `U_•` are `1`-morphisms over `X`: they commute strictly with the
> projections `f_n`.

```lean
public theorem nerve_map_comp_projection {m n : SimplexCategoryᵒᵖ} (φ : m ⟶ n) :
    ((nerve p f).map φ).toFunctor ⋙ Tuple.projection p f n.unop.len =
      Tuple.projection p f m.unop.len
```

## Tag 06X5, a lemma

[Tag 06X5](https://stacks.math.columbia.edu/tag/06X5) in the Stacks Project.

**`Stacks.Cech.complexPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L332). The attribute's comment: “part (1), the morphism of complexes”.

> **Stacks 06X5 (1).** A `2`-commutative square of coverings over the base induces a morphism
> of Čech complexes `Č(U → X, F) ⟶ Č(V → Y, e⁻¹F)`, given in degree `n` by pullback along the
> induced functor `V_n ⥤ U_n` of Čech nerves.

```lean
public def complexPullbackMap : complex pX f F ⟶ complex pY g (e.op ⋙ F)
```

**`Stacks.Cech.complexPullbackMap_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L338). The attribute's comment: “part (1), the degreewise description”.

> **Stacks 06X5 (1).** The morphism of Čech complexes is pullback along the induced functor of
> Čech nerves, degreewise on the limit cones.

```lean
public theorem complexPullbackMap_π (n : ℕ) (a : Tuple pY g n) :
    (complexPullbackMap pX pY f g h e α he hα F).f n ≫
        limit.π ((Tuple.projection pY g n).op ⋙ e.op ⋙ F) (op a) =
      limit.π ((Tuple.projection pX f n).op ⋙ F)
        (op ((nerveMap pX pY f g h e α he hα n).obj a))
```

**`Stacks.Cech.isIso_complexPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L348). The attribute's comment: “part (2)”.

> **Stacks 06X5 (2).** If the two horizontal functors of the square are equivalences, the
> morphism of Čech complexes of part (1) is an isomorphism.

```lean
public theorem isIso_complexPullbackMap [h.IsEquivalence] [e.IsEquivalence]
    (hpV : (g ⋙ pY).IsFiberedInGroupoids) :
    IsIso (complexPullbackMap pX pY f g h e α he hα F)
```

**`Stacks.Cech.nonempty_complexIso_of_natIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Complex.lean#L366). The attribute's comment: “part (3)”.

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

**`Stacks.Cech.nonempty_homotopy_extendedComplex_id_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/Homotopy.lean#L409).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
