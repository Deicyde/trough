---
declaration: section
origin: cited
lean: CategoryTheory.isFiltered_costructuredArrow, CategoryTheory.exists_iso_comp_linearYoneda_of_finiteDimensional, Stacks.AlgebraicGeometry.DerivedVarieties.Representability.exists_iso_linearYoneda_of_isHomological_of_isProper, Stacks.AlgebraicGeometry.DerivedVarieties.Representability.exists_iso_linearCoyoneda_of_isHomological_of_isRegular
statement: formalized
proof: formalized
---

# 57.6 A representability theorem

Section 57.6 of the Stacks Project, [Tag 0FYE](https://stacks.math.columbia.edu/tag/0FYE). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FYF, a lemma

[Tag 0FYF](https://stacks.math.columbia.edu/tag/0FYF) in the Stacks Project.

**`CategoryTheory.isFiltered_costructuredArrow`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Filtered.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Filtered.lean#L54).

> **Stacks Project, Tag 0FYF.** The category of arrows to a fixed object along a triangulated
> functor is filtered.

```lean
lemma isFiltered_costructuredArrow (X : D) :
    IsFiltered (CostructuredArrow ι X)
```

## Tag 0FYG, a lemma

[Tag 0FYG](https://stacks.math.columbia.edu/tag/0FYG) in the Stacks Project.

**`CategoryTheory.exists_iso_comp_linearYoneda_of_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Basic.lean, line 1229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Basic.lean#L1229).

> **Stacks Project, Tag 0FYG.** A finite-dimensional linear cohomological functor on the
> compact objects of a compactly generated triangulated category is represented by an object of
> the ambient category.

```lean
theorem exists_iso_comp_linearYoneda_of_finiteDimensional
    (k : Type w) [Field k]
    (D : Type u) [Category.{v} D] [Preadditive D] [CategoryTheory.Linear k D]
    [HasZeroObject D] [HasShift D ℤ] [∀ n : ℤ, (shiftFunctor D n).Additive]
    [Pretriangulated D] [IsTriangulated D] [HasCoproducts.{v} D]
    (hD : Pretriangulated.IsCompactlyGenerated.{v} D)
    (H : (ObjectProperty.FullSubcategory (IsCompactObject.{v} (C := D)))ᵒᵖ ⥤
      ModuleCat.{v} k)
    [H.IsHomological]
    (hHlinear : ∀ {X Y} (f : X ⟶ Y) (r : k), H.map ((r • f.unop).op) = r • H.map f)
    (hH : ∀ X, FiniteDimensional k (H.obj X)) :
    ∃ Y : D, Nonempty
      (H ≅ (ObjectProperty.ι (IsCompactObject.{v} (C := D))).op ⋙
        (linearYoneda k D).obj Y)
```

## Tag 0FYH, a theorem

[Tag 0FYH](https://stacks.math.columbia.edu/tag/0FYH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Representability.exists_iso_linearYoneda_of_isHomological_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/ProperOverField.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/ProperOverField.lean#L408).

> **Stacks Project, Tag 0FYH.** Let `X` be a proper scheme over a field `k`. Let
> `F : D_perf(𝒪_X)^opp → Vect_k` be a `k`-linear cohomological functor such that
> `∑_{n ∈ ℤ} dim_k F(E[n]) < ∞` for all `E ∈ D_perf(𝒪_X)`. Then `F` is isomorphic to a functor of
> the form `E ↦ Hom_X(E, K)` for some `K ∈ D^b_Coh(𝒪_X)`.
>
> Here `D_perf(𝒪_X)` is `AlgebraicGeometry.perfectDerived`, the perfect objects of the derived
> category of `𝒪_X`-modules with its triangulated structure; "cohomological" is
> `CategoryTheory.Functor.IsHomological` on the opposite category; `k`-linearity is for the
> `k`-structure induced by the structure morphism, `AlgebraicGeometry.modulesLinear`; the sum is the
> cardinal sum of the `k`-ranks over all of `ℤ`, and `< ∞` is `< ℵ₀`; and `D^b_Coh(𝒪_X)` is
> `DerivedCategoryB.derivedCategoryBBounded` at coherence.
>
> The proof is the source's: by [Stacks, Tag 0FYG] `F ≅ Hom_X(-, K)` for some `K ∈ D_QCoh(𝒪_X)`
> (`exists_iso_linearYoneda_of_isHomological`, through [Stacks, Tags 08DT, 09IS and 09M1]), and then
> `K ∈ D^b_Coh(𝒪_X)` by [Stacks, Tag 0FYD]
> (`CoherentCharacterizationConverse.derivedCategoryBBounded_of_hasFiniteTotalExt`),
> `Ext^n_X(E, K) = Hom_X(E[-n], K) = F(E[-n])` having finite total dimension.

```lean
theorem exists_iso_linearYoneda_of_isHomological_of_isProper [IsProper X.hom]
    (F : (perfectDerived X.left)ᵒᵖ ⥤ ModuleCat.{u} k) [F.IsHomological]
    (hF : ∀ {E E' : (perfectDerived X.left)ᵒᵖ} (f : E ⟶ E') (r : k),
      F.map ((r • f.unop).op) = r • F.map f)
    (hfin : ∀ E : perfectDerived X.left,
      Cardinal.sum (fun n : ℤ => Module.rank k (F.obj (op (E⟦n⟧)))) < Cardinal.aleph0) :
    ∃ K : DerivedCategory X.left.Modules,
      DerivedCategoryB.derivedCategoryBBounded (fun M : X.left.Modules => M.IsCoherent) K ∧
        Nonempty (F ≅ (ObjectProperty.ι _).op ⋙
          (linearYoneda k (DerivedCategory X.left.Modules)).obj K)
```

## Tag 0H4A, a lemma

[Tag 0H4A](https://stacks.math.columbia.edu/tag/0H4A) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Representability.exists_iso_linearCoyoneda_of_isHomological_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Regular.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/RepresentabilityTheorem/Regular.lean#L180).

> **Stacks Project, Tag 0H4A.** Let `X` be a proper scheme over a field `k` which is regular. Let
> `G : D_perf(𝒪_X) → Vect_k` be a `k`-linear homological functor such that
> `∑_{n ∈ ℤ} dim_k G(E[n]) < ∞` for all `E ∈ D_perf(𝒪_X)`. Then `G` is isomorphic to a functor of the
> form `E ↦ Hom_X(K, E)` for some `K ∈ D_perf(𝒪_X)`.
>
> Here `D_perf(𝒪_X)` is `AlgebraicGeometry.perfectDerived`, the perfect objects of the derived
> category of `𝒪_X`-modules with its triangulated structure; "homological" is
> `CategoryTheory.Functor.IsHomological`; `k`-linearity is for the `k`-structure induced by the
> structure morphism, `AlgebraicGeometry.modulesLinear`; the sum is the cardinal sum of the
> `k`-ranks over all of `ℤ`, and `< ∞` is `< ℵ₀`; regularity is `AlgebraicGeometry.IsRegular`
> ([Stacks, Tag 02IS]); and the isomorphism is one of `Vect_k`-valued functors with
> `linearCoyoneda`, the `k`-linear `Hom_X(K, -)`.
>
> The proof is the source's (`exists_iso_linearCoyoneda_of_representability`): `F(E) = G(E^∨)` is
> cohomological of finite total dimension, so `F ≅ Hom_X(-, K')` with `K' ∈ D^b_Coh(𝒪_X)` by
> [Stacks, Tag 0FYH] (`exists_iso_linearYoneda_of_isHomological_of_isProper`), `K'` is perfect by
> [Stacks, Tag 0FDC], and `G ≅ Hom_X(K'^∨, -)` by [Stacks, Tag 08DQ].

```lean
theorem exists_iso_linearCoyoneda_of_isHomological_of_isRegular [IsProper X.hom]
    (hX : IsRegular X.left)
    (G : perfectDerived X.left ⥤ ModuleCat.{u} k) [G.IsHomological]
    (hG : ∀ {E E' : perfectDerived X.left} (f : E ⟶ E') (r : k), G.map (r • f) = r • G.map f)
    (hfin : ∀ E : perfectDerived X.left,
      Cardinal.sum (fun n : ℤ => Module.rank k (G.obj (E⟦n⟧))) < Cardinal.aleph0) :
    ∃ K : perfectDerived X.left,
      Nonempty (G ≅ (linearCoyoneda k (perfectDerived X.left)).obj (op K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.6, Tag 0FYE](https://stacks.math.columbia.edu/tag/0FYE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
