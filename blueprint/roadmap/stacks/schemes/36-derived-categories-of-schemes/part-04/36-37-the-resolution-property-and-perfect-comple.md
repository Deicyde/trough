---
declaration: section
origin: cited
lean: Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_quasiIso, Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_iso_of_hasResolutionProperty, Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_roof_of_hasResolutionProperty, Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_homotopy_of_hasResolutionProperty, Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isTriangulated, Stacks.Perfect.BoundedLocallyFreeComplexes.perfectComplexFunctor_isTriangulated, Stacks.Perfect.BoundedLocallyFreeComplexes.BoundedFiniteLocallyFreeHomotopyCategory, Stacks.Perfect.BoundedLocallyFreeComplexes.PerfectDerivedCategory
statement: formalized
proof: formalized
---

# 36.37 The resolution property and perfect complexes

Section 36.37 of the Stacks Project, [Tag 0F8D](https://stacks.math.columbia.edu/tag/0F8D). 5 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F8E, a lemma

[Tag 0F8E](https://stacks.math.columbia.edu/tag/0F8E) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/FiniteLocallyFreeReplacement.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/FiniteLocallyFreeReplacement.lean#L1029).

> **Stacks Project, Tag 0F8E.** On a quasi-compact and quasi-separated scheme with the
> resolution property, a bounded below complex of quasi-coherent modules representing a perfect
> object of the derived category receives a quasi-isomorphism from a bounded complex of finite
> locally free modules.

```lean
theorem exists_boundedFiniteLocallyFree_quasiIso (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [AlgebraicGeometry.HasResolutionProperty X]
    (F : CochainComplex X.Modules ℤ)
    (hFplus : CochainComplex.plus X.Modules F)
    (hFqc : ∀ i : ℤ, (F.X i).IsQuasicoherent)
    (hFperf : IsPerfect (X := X.toRingedSpace) (DerivedCategory.Q.obj F)) :
    ∃ (E : CochainComplex X.Modules ℤ) (f : E ⟶ F),
      boundedFiniteLocallyFreeComplex X E ∧ QuasiIso f
```

## Tag 0F8F, a lemma

[Tag 0F8F](https://stacks.math.columbia.edu/tag/0F8F) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_iso_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/PerfectRepresentative.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/PerfectRepresentative.lean#L81).

> **[Stacks, Tag 0F8F].**  Let `X` be a quasi-compact and quasi-separated scheme with the
> resolution property.  Every perfect object of `D(𝒪_X)` is isomorphic to the image of a bounded
> complex of finite locally free `𝒪_X`-modules.
>
> The three assumptions on `X` are exactly the source's.  The affine diagonal used in the proof
> comes
> from [Stacks, Tag 0F8C], `AlgebraicGeometry.HasResolutionProperty.isAffineHom_diagonal`.

```lean
theorem exists_boundedFiniteLocallyFree_iso_of_hasResolutionProperty (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [HasResolutionProperty X]
    (K : DerivedCategory X.Modules) (hK : IsPerfect (X := X.toRingedSpace) K) :
    ∃ E : CochainComplex X.Modules ℤ, boundedFiniteLocallyFreeComplex X E ∧
      Nonempty (DerivedCategory.Q.obj E ≅ K)
```

## Tag 0F8G, a lemma

[Tag 0F8G](https://stacks.math.columbia.edu/tag/0F8G) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_roof_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/DerivedRoof.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/DerivedRoof.lean#L183).

> **[Stacks, Tag 0F8G].**  Let `X` be a quasi-compact and quasi-separated scheme with the
> resolution property and let `ℰ^•`, `ℱ^•` be finite complexes of finite locally free
> `𝒪_X`-modules.  Every morphism `α : ℰ^• ⟶ ℱ^•` of `D(𝒪_X)` is represented by a diagram
> `ℰ^• ← 𝒢^• → ℱ^•` with `𝒢^•` a bounded complex of finite locally free `𝒪_X`-modules and
> `𝒢^• → ℰ^•` a quasi-isomorphism.
>
> The assumptions on `X` are exactly the source's.  The affine diagonal used in the proof comes
> from [Stacks, Tag 0F8C], `AlgebraicGeometry.HasResolutionProperty.isAffineHom_diagonal`.

```lean
theorem exists_boundedFiniteLocallyFree_roof_of_hasResolutionProperty (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [HasResolutionProperty X]
    (E F : CochainComplex X.Modules ℤ)
    (hE : boundedFiniteLocallyFreeComplex X E) (hF : boundedFiniteLocallyFreeComplex X F)
    (α : DerivedCategory.Q.obj E ⟶ DerivedCategory.Q.obj F) :
    ∃ (G : CochainComplex X.Modules ℤ) (p : G ⟶ E) (_ : QuasiIso p) (q : G ⟶ F),
      boundedFiniteLocallyFreeComplex X G ∧
        inv (DerivedCategory.Q.map p) ≫ DerivedCategory.Q.map q = α
```

## Tag 0F8H, a lemma

[Tag 0F8H](https://stacks.math.columbia.edu/tag/0F8H) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_homotopy_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/DerivedHomotopy.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/DerivedHomotopy.lean#L209).

> Let `X` be a quasi-compact and quasi-separated scheme with the resolution property and let
> `ℰ^•`, `ℱ^•` be finite complexes of finite locally free `𝒪_X`-modules.  If two maps of complexes
> `α^•, β^• : ℰ^• ⟶ ℱ^•` define the same morphism of `D(𝒪_X)`, then there is a
> quasi-isomorphism `γ^• : 𝒢^• ⟶ ℰ^•` with `𝒢^•` a bounded complex of finite locally free
> `𝒪_X`-modules such that `α^• ∘ γ^•` and `β^• ∘ γ^•` are homotopic.

```lean
theorem exists_boundedFiniteLocallyFree_homotopy_of_hasResolutionProperty (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [HasResolutionProperty X]
    (E F : CochainComplex X.Modules ℤ)
    (hE : boundedFiniteLocallyFreeComplex X E) (hF : boundedFiniteLocallyFreeComplex X F)
    (α β : E ⟶ F) (h : DerivedCategory.Q.map α = DerivedCategory.Q.map β) :
    ∃ (G : CochainComplex X.Modules ℤ) (γ : G ⟶ E) (_ : QuasiIso γ),
      boundedFiniteLocallyFreeComplex X G ∧ Nonempty (Homotopy (γ ≫ α) (γ ≫ β))
```

## Tag 0F8I, a proposition

[Tag 0F8I](https://stacks.math.columbia.edu/tag/0F8I) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean#L58). The attribute's comment: “perfect objects form a triangulated subcategory”. References: SGA 6 I (5.8.4), “special case”; SGA 6 III (4.2), “Identity-morphism case”.

> **Perfect objects form a triangulated subcategory of `D(O_X)`.** This is the ringed-space
> statement `Stacks.Cohomology.PerfectTriangulatedSubcategory.isTriangulated_isPerfect`, read on the
> ringed space underlying `X`.

```lean
instance perfectDerivedProperty_isTriangulated (X : Scheme.{u}) :
    (show ObjectProperty (DerivedCategory X.Modules) from
      fun K => IsPerfect (X := X.toRingedSpace) K).IsTriangulated
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectComplexFunctor_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean#L124). The attribute's comment: “exactness of the canonical functor”.

> **The canonical functor `K^b(A) ⥤ D_perf(O_X)` is exact.** The composite
> `K^b(A) ⥤ K(O_X) ⥤ D(O_X)` is exact, being the inclusion of a triangulated subcategory
> followed by the localization functor of the derived category, and the canonical functor is its
> lift along the perfectness of its values, which is exact because `D_perf(O_X)` is a
> triangulated subcategory.

```lean
instance perfectComplexFunctor_isTriangulated (X : Scheme.{u}) :
    (perfectComplexFunctor X).IsTriangulated
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.BoundedFiniteLocallyFreeHomotopyCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean#L88). The attribute's comment: “the category K^b(A)”.

> The homotopy category `K^b(A)` of bounded complexes of finite locally free modules.

```lean
abbrev BoundedFiniteLocallyFreeHomotopyCategory (X : Scheme.{u})
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.PerfectDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean#L93). The attribute's comment: “the category of perfect objects”.

> The full subcategory `D_perf(O_X)` of perfect objects of the derived category.

```lean
abbrev PerfectDerivedCategory (X : Scheme.{u})
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.quasiIsomorphisms`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean#L99). The attribute's comment: “the system S of quasi-isomorphisms”.

> The system `S` of quasi-isomorphisms of `K^b(A)`.

```lean
abbrev quasiIsomorphisms (X : Scheme.{u}) :
    MorphismProperty (BoundedFiniteLocallyFreeHomotopyCategory X)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean#L109). The attribute's comment: “perfect objects are closed under isomorphism”.

> **Perfect objects form a strictly full subcategory of `D(O_X)`.**

```lean
instance perfectDerivedProperty_isClosedUnderIsomorphisms (X : Scheme.{u}) :
    ObjectProperty.IsClosedUnderIsomorphisms
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.quasiIsomorphisms_isInvertedBy_perfectComplexFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/InvertsQuasiIsomorphisms.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/InvertsQuasiIsomorphisms.lean#L75). The attribute's comment: “the canonical functor inverts the system `S` of quasi-isomorphisms, so that it factors through `S⁻¹K^b(A)`; this is the first field of `Functor.IsLocalization`, for every scheme X”.

> **The canonical functor `K^b(A) ⥤ D_perf(O_X)` inverts the quasi-isomorphisms of `K^b(A)`.**
> A morphism of `K^b(A)` is a quasi-isomorphism exactly when its image in `K(O_X)` is one, so
> `CategoryTheory.DerivedCategory.Qh` sends it to an isomorphism; that image is the image of the
> morphism under the fully faithful inclusion of `D_perf(O_X)`, which therefore reflects the
> invertibility.

```lean
theorem quasiIsomorphisms_isInvertedBy_perfectComplexFunctor (X : Scheme.{u}) :
    (quasiIsomorphisms X).IsInvertedBy (perfectComplexFunctor X)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectComplexFunctor_isLocalization_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Localization.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Localization.lean#L152). The attribute's comment: “the canonical functor presents the perfect derived category as the localization of the bounded homotopy category at the quasi-isomorphisms”.

> **The equivalence clause of [Stacks, Tag 0F8I].**  On a quasi-compact and quasi-separated
> scheme with the resolution property, the canonical functor `K^b(A) ⥤ D_perf(𝒪_X)` presents
> `D_perf(𝒪_X)` as the localization of `K^b(A)` at the quasi-isomorphisms.
>
> The three assumptions on `X` are exactly the source's.  The affine diagonal is supplied
> by [Stacks, Tag 0F8C] (`AlgebraicGeometry.HasResolutionProperty.isAffineHom_diagonal`), which
> rests on the converse of [Stacks, Tag 0F8B] at Noetherian stages
> (`AlgebraicGeometry.hasResolutionProperty_stage`).

```lean
theorem perfectComplexFunctor_isLocalization_of_hasResolutionProperty (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [HasResolutionProperty X] :
    (perfectComplexFunctor X).IsLocalization (quasiIsomorphisms X)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfect_of_boundedFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Perfectness.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Perfectness.lean#L99). The attribute's comment: “the functor lands in perfect objects”.

> **`K^b(A)` lands in `D_perf(O_X)`.** A bounded complex of finite locally free modules is
> strictly perfect on a small enough neighbourhood of each point of `X`, so it is perfect in the
> sense of Tag 08CM with the identity as the local quasi-isomorphism, and it represents its own
> image in the derived category.

```lean
theorem perfect_of_boundedFiniteLocallyFree (X : Scheme.{u})
    (E : BoundedFiniteLocallyFreeHomotopyCategory X) :
    IsPerfect (X := X.toRingedSpace) (DerivedCategory.Qh.obj E.obj)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.isSaturated_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Saturation.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Saturation.lean#L63). The attribute's comment: “`D_perf(O_X)` is a saturated subcategory of `D(O_X)` -- the adjective `saturated` of the source's item (3), which is closure under direct summands, on any ringed space”.

> **Perfectness is a saturated property of objects of `D(O_X)` on a ringed space.**  Both
> summands of a perfect biproduct are perfect by [Stacks, Tag 08CS], and perfectness is closed
> under isomorphism, so the isomorphism closure in the definition of saturation is the property
> itself.  For a scheme `X`, whose `X.Modules` is `OXMod` of `X.toRingedSpace`, this is the
> saturation clause of Tag 0F8I: a direct summand of a perfect object of `D(O_X)` is perfect.

```lean
theorem isSaturated_isPerfect {X : RingedSpace.{u, u}}
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] :
    ObjectProperty.IsSaturated
      (fun K : DerivedCategory (OXMod.{u, u} X) => IsPerfect K)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.boundedFiniteLocallyFreeHomotopyProperty_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean#L269). The attribute's comment: “the homotopy subcategory is triangulated”.

> **`K^b(A)` is a triangulated subcategory of `K(O_X)`.** The property of being a bounded
> complex with finite locally free terms holds of the zero complex, is stable under shift, and is
> stable under mapping cones; the last because `(mappingCone f).X i` is `K.X (i + 1) ⊞ L.X i`.

```lean
instance boundedFiniteLocallyFreeHomotopyProperty_isTriangulated
    (X : Scheme.{u}) :
    (boundedFiniteLocallyFreeHomotopyProperty X).IsTriangulated
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectComplexFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean#L335). The attribute's comment: “the canonical functor”.

> **The canonical functor `K^b(A) ⥤ D_perf(O_X)`.** It is `DerivedCategory.Qh` restricted to
> `K^b(A)`, lifted to the full subcategory of perfect objects along
> `Stacks.Perfect.BoundedLocallyFreeComplexes.perfect_of_boundedFiniteLocallyFree`.

```lean
def perfectComplexFunctor (X : Scheme.{u}) :
    BoundedFiniteLocallyFreeHomotopyCategory X ⥤ PerfectDerivedCategory X
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.quasiIsomorphisms_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean#L367). The attribute's comment: “saturation of the quasi-isomorphism system”.

> **The system `S` of quasi-isomorphisms of `K^b(A)` is saturated.**

```lean
theorem quasiIsomorphisms_isSaturated (X : Scheme.{u}) :
    (quasiIsomorphisms X).IsSaturated
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.quasiIsomorphisms_isCompatibleWithTriangulation`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Triangulated.lean#L374). The attribute's comment: “compatibility of quasi-isomorphisms with triangulation”.

> **The system `S` of quasi-isomorphisms of `K^b(A)` is compatible with the triangulated
> structure.**

```lean
instance quasiIsomorphisms_isCompatibleWithTriangulation (X : Scheme.{u}) :
    (quasiIsomorphisms X).IsCompatibleWithTriangulation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.37, Tag 0F8D](https://stacks.math.columbia.edu/tag/0F8D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
