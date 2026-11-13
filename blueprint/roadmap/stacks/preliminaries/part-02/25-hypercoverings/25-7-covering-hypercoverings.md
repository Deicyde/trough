---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.isHypercovering_fibreProduct, Stacks.CategoryTheory.Hypercovering.IsHypercovering.prod, Stacks.CategoryTheory.Hypercovering.exists_hypercovering_map_factoring_through_covering, Stacks.CategoryTheory.Hypercovering.power_cosk_unit_isProjection, Stacks.CategoryTheory.Hypercovering.exists_hypercovering_map_factoring_through_locallySurjective
statement: formalized
proof: formalized
---

# 25.7 Covering hypercoverings

Section 25.7 of the Stacks Project, [Tag 01GG](https://stacks.math.columbia.edu/tag/01GG). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01GH, a lemma

[Tag 01GH](https://stacks.math.columbia.edu/tag/01GH) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/FibreProduct.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/FibreProduct.lean#L264).

> A fibre product with a hypercovering is a hypercovering when the other morphism is covering
> in degree zero and on every relative matching object.

```lean
theorem isHypercovering_fibreProduct (J : Pretopology C)
    [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    {K L M : SimplicialObject (FormalCoproduct.{w} (Over X))} (a : K ⟶ L) (b : M ⟶ L)
    (hK : IsHypercovering J K)
    (h₀ : IsCoveringOver J (b.app (op ⦋0⦌)))
    (hmatching : ∀ n : ℕ, IsCoveringOver J
      (Limits.pullback.lift
        (f := (((SimplicialObject.coskAdj n).unit.app L).app (op ⦋n + 1⦌)))
        (g := (((SimplicialObject.Truncated.cosk n).map
          ((SimplicialObject.truncation n).map b)).app (op ⦋n + 1⦌)))
        (b.app (op ⦋n + 1⦌))
        (((SimplicialObject.coskAdj n).unit.app M).app (op ⦋n + 1⦌))
        (NatTrans.congr_app ((SimplicialObject.coskAdj n).unit.naturality b)
          (op ⦋n + 1⦌)))) :
    IsHypercovering J (SimplicialObject.fibreProduct a b)
```

## Tag 01GI, a lemma

[Tag 01GI](https://stacks.math.columbia.edu/tag/01GI) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.IsHypercovering.prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/Product.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/Product.lean#L169).

> **Stacks Project, Tag 01GI.** The product of two hypercoverings of an object of a site with
> fibre products is a hypercovering.

```lean
theorem IsHypercovering.prod (J : Pretopology C)
    [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    {K L : SimplicialObject (FormalCoproduct.{w} (Over X))}
    (hK : IsHypercovering J K) (hL : IsHypercovering J L) :
    IsHypercovering J (K ⨯ L)
```

## Tag 01GJ, a lemma

[Tag 01GJ](https://stacks.math.columbia.edu/tag/01GJ) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercovering_map_factoring_through_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Refinement/FactoringThroughCovering.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Refinement/FactoringThroughCovering.lean#L289). References: SGA 4 V (7.3.2), “2)”.

> **Stacks Project, Tag 01GJ.** A covering of the term in any fixed degree of a
> hypercovering can be refined by a morphism from another hypercovering, whose component in that
> degree factors through the covering.

```lean
public theorem exists_hypercovering_map_factoring_through_covering
    (J : Pretopology C) [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K) (k : ℕ)
    {Z : FormalCoproduct.{w} (Over X)}
    (u : Z ⟶ K.obj (Opposite.op (SimplexCategory.mk k)))
    (hu : IsCoveringOver J u) :
    ∃ (L : SimplicialObject (FormalCoproduct.{w} (Over X))),
      IsHypercovering J L ∧
        ∃ (f : L ⟶ K) (g : L.obj (Opposite.op (SimplexCategory.mk k)) ⟶ Z),
          g ≫ u = f.app (Opposite.op (SimplexCategory.mk k))
```

## Tag 0B16, an equation

[Tag 0B16](https://stacks.math.columbia.edu/tag/0B16) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.power_cosk_unit_isProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ConstantPowerMatching.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ConstantPowerMatching.lean#L599).

> The `(n + 1)`-st matching map of `Hom(C[k], T)` is, functorially in `T`,
> a projection of finite powers of `T`.

```lean
public theorem power_cosk_unit_isProjection
    {D : Type u} [Category.{v} D] [HasFiniteLimits D]
    (k n : ℕ) (hn : 0 < n) :
    letI : ∀ F : SimplicialObject.Truncated D n,
        (SimplexCategory.Truncated.inclusion n).op.HasPointwiseRightKanExtension F :=
      fun F =>
        (hasPointwiseRightKanExtension_of_hasBinaryProducts_or_hasFiniteConnectedLimits
            (C := D)).2 (fun _ => inferInstance) n hn F;
    letI : ∀ m : SimplexCategoryᵒᵖ,
        Fintype ((uliftCoyoneda.{w}.obj (op ⦋k⦌)).obj m.unop) :=
      fun m => by
        rw [CosimplicialObject.uliftCoyoneda_spec.1 ⦋k⦌ m.unop]
        exact Fintype.ofFinite _;
    ∃ S : Finset ((uliftCoyoneda.{w}.obj (op ⦋k⦌)).obj ⦋n + 1⦌),
      ∃ e : ∀ T : D,
          (((SimplicialObject.cosk n).obj
            (((SimplicialObject.const D).obj T).power
              (uliftCoyoneda.{w}.obj (op ⦋k⦌)))).obj (op ⦋n + 1⦌)) ≅
            ∏ᶜ fun _ : ↥S => T,
        (∀ T : D,
          (((SimplicialObject.coskAdj n).unit.app
            (((SimplicialObject.const D).obj T).power
              (uliftCoyoneda.{w}.obj (op ⦋k⦌)))).app
              (op ⦋n + 1⦌)) ≫ (e T).hom =
            eqToHom (SimplicialObject.power_obj
              ((SimplicialObject.const D).obj T)
              (uliftCoyoneda.{w}.obj (op ⦋k⦌)) (op ⦋n + 1⦌)) ≫
              Limits.Pi.map' (fun s : ↥S => (s : _)) (fun _ => 𝟙 T)) ∧
        (∀ (T T' : D) (f : T ⟶ T')
          (g : (((SimplicialObject.const D).obj T).power
              (uliftCoyoneda.{w}.obj (op ⦋k⦌))) ⟶
            (((SimplicialObject.const D).obj T').power
              (uliftCoyoneda.{w}.obj (op ⦋k⦌)))),
          (∀ m : SimplexCategoryᵒᵖ,
            g.app m = Limits.Pi.map (fun _ => f)) →
          (((SimplicialObject.cosk n).map g).app (op ⦋n + 1⦌)) ≫ (e T').hom =
            (e T).hom ≫ Limits.Pi.map (fun _ : ↥S => f))
```

## Tag 01GK, a lemma

[Tag 01GK](https://stacks.math.columbia.edu/tag/01GK) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercovering_map_factoring_through_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjectiveRefinement.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjectiveRefinement.lean#L224). References: SGA 4 V (7.3.2), “2)”.

> **Stacks Project, Tag 01GK.** A locally surjective map onto the presheaf represented by one
> term of a hypercovering can be factored through after refining the hypercovering.

```lean
public theorem exists_hypercovering_map_factoring_through_locallySurjective
    (J : Pretopology C) [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    (K : SimplicialObject (FormalCoproduct.{max u v w} (Over X)))
    (hK : IsHypercovering J K) (n : ℕ)
    (F : Cᵒᵖ ⥤ Type (max u v w))
    (u : F ⟶ (associatedPresheafFunctorOver (X := X)).obj
      (K.obj (Opposite.op (SimplexCategory.mk n))))
    [Presheaf.IsLocallySurjective J.toGrothendieck u] :
    ∃ (L : SimplicialObject (FormalCoproduct.{max u v w} (Over X))),
      IsHypercovering J L ∧
        ∃ (f : L ⟶ K)
          (g : (associatedPresheafFunctorOver (X := X)).obj
            (L.obj (Opposite.op (SimplexCategory.mk n))) ⟶ F),
            g ≫ u = (associatedPresheafFunctorOver (X := X)).map
              (f.app (Opposite.op (SimplexCategory.mk n)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.7, Tag 01GG](https://stacks.math.columbia.edu/tag/01GG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
