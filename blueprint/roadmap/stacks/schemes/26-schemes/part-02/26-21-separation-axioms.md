---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsSeparated.instMap, AlgebraicGeometry.IsSeparated, AlgebraicGeometry.QuasiSeparated, AlgebraicGeometry.Scheme.IsSeparated, AlgebraicGeometry.quasiSeparatedSpace_iff_quasiSeparated, AlgebraicGeometry.structureMorphism, AlgebraicGeometry.diagonal_preimage_mixedCharts, AlgebraicGeometry.structureMorphism_not_quasiSeparated
statement: formalized
proof: formalized
---

# 26.21 Separation axioms

Section 26.21 of the Stacks Project, [Tag 01KH](https://stacks.math.columbia.edu/tag/01KH). 17 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 26 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01KI, a lemma

[Tag 01KI](https://stacks.math.columbia.edu/tag/01KI) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated.instMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.instMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L253) (StacksFrontier): “the diagonal of Spec S ⟶ Spec R is a closed immersion”. References: EGA I (5.5.7), “more general”; EGA I (5.5.9), “special case”; SGA 3 XI (4.3), “special case”.

## Tag 01KK, a definition

[Tag 01KK](https://stacks.math.columbia.edu/tag/01KK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L256) (StacksFrontier): “(1) separated morphism: the diagonal is a closed immersion”. References: EGA I (5.4.1); EGA I (10.15.1), “Separated morphism X → S”.
- [`AlgebraicGeometry.QuasiSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L258) (StacksFrontier): “(2) quasi-separated morphism: the diagonal is quasi-compact”. References: EGA IV (1.2.1); SGA 1 XIII (1.5); SGA 4 VI (1.9.1), “special case”; SGA 4 Vbis (4.2.0), “partial”; SGA 6 II (3.0); SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.Scheme.IsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IsSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L260) (StacksFrontier): “(3) separated scheme: separated over the terminal scheme Spec ℤ”. References: EGA I (5.4.1); EGA I (10.15.1), “special case”; SGA 2 XIV (1.0); SGA 4 XVII (0.7).
- [`AlgebraicGeometry.quasiSeparatedSpace_iff_quasiSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparatedSpace_iff_quasiSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L262) (StacksFrontier): “(4) quasi-separated scheme: QuasiSeparatedSpace X is equivalent to X ⟶ Spec ℤ being quasi-separated”. References: EGA II (7.2.4), “absolute case”; EGA IV (1.2.1); EGA IV (1.2.7).

## Tag 01KL, an example

[Tag 01KL](https://stacks.math.columbia.edu/tag/01KL) in the Stacks Project.

**`AlgebraicGeometry.structureMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean#L193). The attribute's comment: “structure\_morphism”.

> The structure morphism of infinite-dimensional affine space with doubled
> origin, restricting on both charts to the canonical affine-space morphism.

```lean
public noncomputable def structureMorphism {k : Type u} [CommRing k]
    (D : DoubledOriginData k) :
    { f : D.scheme ⟶ Spec (.of k) //
      ∀ i : Fin 2,
        D.chart i ≫ f = Spec.map (CommRingCat.ofHom (MvPolynomial.C :
          k →+* MvPolynomial ℕ k)) }
```

**`AlgebraicGeometry.diagonal_preimage_mixedCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean#L363). The attribute's comment: “diagonal\_inverse\_image”.

> The diagonal inverse image of the product of the two affine charts is the punctured
> affine space, embedded in the doubled-origin scheme through its first chart.

```lean
public theorem diagonal_preimage_mixedCharts {k : Type u} [CommRing k]
    (D : DoubledOriginData k) {S : Scheme.{u}} (f : D.scheme ⟶ S) :
    (pullback.diagonal f) ⁻¹'
        ((pullback.fst f f) ⁻¹' Set.range (D.chart 0) ∩
          (pullback.snd f f) ⁻¹' Set.range (D.chart 1)) =
      Set.range ((puncturedInfiniteAffineSpace k).ι ≫ D.chart 0)
```

**`AlgebraicGeometry.structureMorphism_not_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean#L439). The attribute's comment: “not\_quasi\_separated”.

> The structure morphism of a doubled-origin infinite-dimensional affine
> space over a field is not quasi-separated.

```lean
public theorem structureMorphism_not_quasiSeparated {k : Type u} [Field k]
    (D : DoubledOriginData k) :
    ¬ QuasiSeparated (structureMorphism D).1
```

**`AlgebraicGeometry.puncturedSpectrum_not_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/PuncturedAffineSpace.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/PuncturedAffineSpace.lean#L72). The attribute's comment: “punctured\_spectrum\_not\_quasi\_compact”.

> The complement of the origin in countably infinite-dimensional affine space over a field is
> not quasi-compact.

```lean
public theorem puncturedSpectrum_not_isCompact (k : Type*) [Field k] :
    ¬ IsCompact {p : PrimeSpectrum (MvPolynomial ℕ k) |
      p.asIdeal ≠ Ideal.span (Set.range (MvPolynomial.X : ℕ → MvPolynomial ℕ k))}
```

**`AlgebraicGeometry.doubledOriginDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ObstructionIX/DoubledOriginDatum.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ObstructionIX/DoubledOriginDatum.lean#L196). The attribute's comment: “doubled\_origin\_scheme”.

> **Stacks Project, Tag 01KL.** Countably infinite-dimensional affine space with its origin
> doubled, as a `DoubledOriginData`: the canonical gluing data of two copies of the affine space,
> together with the identifications of its charts and overlaps with the standard models.

```lean
public def doubledOriginDatum : DoubledOriginData k
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineOpen_opensRange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineOpen_opensRange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/DoubledOrigin.lean#L77) (StacksFrontier): “affine\_open\_charts”.

## Tag 01KM, a lemma

[Tag 01KM](https://stacks.math.columbia.edu/tag/01KM) in the Stacks Project.

**`AlgebraicGeometry.isImmersion_equalizer_ι_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean#L51). The attribute's comment: “the equalizer of a and b is an immersion, i.e. a locally closed subscheme of X”.

> The equalizer of two morphisms `a b : X ⟶ Y` of schemes over `S` is an immersion into `X`:
> it is a base change of the diagonal of `Y ⟶ S`, which is an immersion.

```lean
theorem isImmersion_equalizer_ι_left : IsImmersion (equalizer.ι a b).left
```

**`AlgebraicGeometry.existsUnique_comp_equalizer_ι_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean#L71). The attribute's comment: “maximality: every morphism on which a and b agree factors through the equalizer”.

> Every morphism of schemes `j : W ⟶ X` on which `a` and `b` agree factors uniquely through
> the equalizer of `a` and `b`. In particular the equalizer contains every locally closed
> subscheme of `X` on which `a` and `b` agree.

```lean
theorem existsUnique_comp_equalizer_ι_left {W : Scheme.{u}} (j : W ⟶ X.left)
    (h : j ≫ a.left = j ≫ b.left) :
    ∃! l : W ⟶ (equalizer a b).left, l ≫ (equalizer.ι a b).left = j
```

**`AlgebraicGeometry.exists_largest_isImmersion_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EqualizerImmersion.lean#L90). The attribute's comment: “full statement: the largest locally closed Z with a = b on Z, closed if Y separated”.

> **Stacks 01KM.** Let `a b : X ⟶ Y` be morphisms of schemes over `S`. There is a largest
> locally closed subscheme `Z` of `X` on which `a` and `b` agree: an immersion `ι : Z ⟶ X` with
> `ι ≫ a = ι ≫ b` through which every immersion `j : W ⟶ X` with `j ≫ a = j ≫ b` factors
> uniquely. Moreover `Z` is a closed subscheme if `Y` is separated over `S`. The scheme `Z` is the
> equalizer of `a` and `b`.

```lean
theorem exists_largest_isImmersion_eq :
    ∃ (Z : Scheme.{u}) (ι : Z ⟶ X.left), IsImmersion ι ∧ ι ≫ a.left = ι ≫ b.left ∧
      (∀ (W : Scheme.{u}) (j : W ⟶ X.left), IsImmersion j → j ≫ a.left = j ≫ b.left →
        ∃! l : W ⟶ Z, l ≫ ι = j) ∧
      (IsSeparated Y.hom → IsClosedImmersion ι)
```

## Tag 01KO, a lemma

[Tag 01KO](https://stacks.math.columbia.edu/tag/01KO) in the Stacks Project.

**`AlgebraicGeometry.quasiSeparated_iff_isCompact_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean#L124). The attribute's comment: “conditions (1) and (2)”.

> A morphism `f : X ⟶ S` is quasi-separated if and only if for every pair of affine opens `U`,
> `V` of `X` which map into a common affine open `W` of `S`, the intersection `U ∩ V` is
> quasi-compact.

```lean
public theorem quasiSeparated_iff_isCompact_inf {X S : Scheme.{u}} (f : X ⟶ S) :
    QuasiSeparated f ↔
      ∀ (W : S.Opens), IsAffineOpen W → ∀ U ≤ f ⁻¹ᵁ W, ∀ V ≤ f ⁻¹ᵁ W,
        IsAffineOpen U → IsAffineOpen V → IsCompact ((U ⊓ V : X.Opens) : Set X)
```

**`AlgebraicGeometry.quasiSeparated_iff_finite_iSup_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean#L136). The attribute's comment: “condition (2), as a finite union of affine opens”.

> A morphism `f : X ⟶ S` is quasi-separated if and only if for every pair of affine opens `U`,
> `V` of `X` which map into a common affine open of `S`, the intersection `U ∩ V` is a finite union
> of affine opens of `X`.

```lean
public theorem quasiSeparated_iff_finite_iSup_affineOpens {X S : Scheme.{u}} (f : X ⟶ S) :
    QuasiSeparated f ↔
      ∀ (W : S.Opens), IsAffineOpen W → ∀ U ≤ f ⁻¹ᵁ W, ∀ V ≤ f ⁻¹ᵁ W,
        IsAffineOpen U → IsAffineOpen V →
        ∃ s : Set X.affineOpens, s.Finite ∧ (U ⊓ V : X.Opens) = ⨆ i ∈ s, (i : X.Opens)
```

**`AlgebraicGeometry.quasiSeparated_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean#L150). The attribute's comment: “condition (3) implies (1)”.

> Given an affine open covering `𝒰` of `S` and, for each `i`, an affine open covering `𝒱 i` of
> `f ⁻¹ U i`, if every fibre product `V j ×_{U i} V k` is quasi-compact then `f` is
> quasi-separated.

```lean
public theorem quasiSeparated_of_openCover {X S : Scheme.{u}} (f : X ⟶ S)
    (𝒰 : Scheme.OpenCover.{v} S) [∀ i, IsAffine (𝒰.X i)]
    (𝒱 : ∀ i, Scheme.OpenCover.{w} (pullback f (𝒰.f i))) [∀ i j, IsAffine ((𝒱 i).X j)]
    (h : ∀ i j k, CompactSpace (pullback ((𝒱 i).f j) ((𝒱 i).f k) : Scheme.{u})) :
    QuasiSeparated f
```

**`AlgebraicGeometry.quasiSeparated_of_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean#L164). The attribute's comment: “condition (3) implies (1), for families of opens”.

> Given an affine open covering `S = ⋃ i, W i` and for each `i` an affine open covering
> `f ⁻¹ (W i) = ⋃ j, V i j`, if each intersection `V i j ∩ V i k` is quasi-compact then `f` is
> quasi-separated.

```lean
public theorem quasiSeparated_of_isOpenCover {X S : Scheme.{u}} (f : X ⟶ S)
    {ι : Type*} (W : ι → S.Opens) (hW : IsOpenCover W) (hWaff : ∀ i, IsAffineOpen (W i))
    {κ : ι → Type*} (V : ∀ i, κ i → X.Opens) (hV : ∀ i, ⨆ j, V i j = f ⁻¹ᵁ W i)
    (hVaff : ∀ i j, IsAffineOpen (V i j))
    (hVcompact : ∀ i j k, IsCompact ((V i j ⊓ V i k : X.Opens) : Set X)) :
    QuasiSeparated f
```

**`AlgebraicGeometry.exists_isOpenCover_of_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiSeparated.lean#L185). The attribute's comment: “condition (1) implies (3)”.

> A quasi-separated morphism admits an affine open covering of the base and an affine open
> covering of each preimage whose pairwise intersections are quasi-compact; one may take all the
> affine opens there are.

```lean
public theorem exists_isOpenCover_of_quasiSeparated {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiSeparated f] :
    ∃ (ι : Type u) (W : ι → S.Opens), IsOpenCover W ∧ (∀ i, IsAffineOpen (W i)) ∧
      ∃ (κ : ι → Type u) (V : ∀ i, κ i → X.Opens),
        (∀ i, ⨆ j, V i j = f ⁻¹ᵁ W i) ∧ (∀ i j, IsAffineOpen (V i j)) ∧
        (∀ i j k, IsCompact ((V i j ⊓ V i k : X.Opens) : Set X))
```

## Tag 01KP, a lemma

[Tag 01KP](https://stacks.math.columbia.edu/tag/01KP) in the Stacks Project.

**`AlgebraicGeometry.sectionTensorMap_surjective_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean#L354). The attribute's comment: “part (1)(b)”. References: EGA I (5.5.6), “necessity of generation”.

> For a separated morphism, the tensor product of sections surjects onto
> sections of the intersection of compatible affine opens.

```lean
public theorem sectionTensorMap_surjective_of_isSeparated {X S : Scheme.{u}}
    (f : X ⟶ S) [IsSeparated f] (U V : X.Opens)
    (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (W : S.Opens) (hW : IsAffineOpen W)
    (hUW : U ≤ f ⁻¹ᵁ W) (hVW : V ≤ f ⁻¹ᵁ W) :
    Function.Surjective (sectionTensorMap X U V)
```

**`AlgebraicGeometry.isSeparated_of_affine_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean#L385). The attribute's comment: “part (2)”. References: EGA I (5.5.6), “sufficiency”.

> Affine neighborhoods of every pair of points in a fiber, with affine
> intersection and surjective tensor map on sections, imply separatedness.

```lean
public theorem isSeparated_of_affine_intersections {X S : Scheme.{u}}
    (f : X ⟶ S)
    (h : ∀ x₁ x₂ : X, f.base x₁ = f.base x₂ →
      ∃ (U V : X.Opens) (W : S.Opens),
        x₁ ∈ U ∧ x₂ ∈ V ∧ IsAffineOpen U ∧ IsAffineOpen V ∧
        IsAffineOpen W ∧ U ≤ f ⁻¹ᵁ W ∧ V ≤ f ⁻¹ᵁ W ∧
        IsAffineOpen (U ⊓ V) ∧ Function.Surjective (sectionTensorMap X U V)) :
    IsSeparated f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineHom_diagonal_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineHom_diagonal_iff#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean#L61) (StacksFrontier): “part (1)(a)”. References: EGA I (5.5.10), “special case”; EGA I (5.5.6), “necessity”; EGA III (6.6.4), “binary intersections”.

## Tag 01KQ, an example

[Tag 01KQ](https://stacks.math.columbia.edu/tag/01KQ) in the Stacks Project.

**`AlgebraicGeometry.projectiveLine_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSeparated.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSeparated.lean#L391).

> **Stacks Project, Tag 01KQ.** The structure morphism of the projective line is separated.
> This holds over an arbitrary commutative ring, not only over a field.

```lean
theorem projectiveLine_isSeparated :
    IsSeparated (projectiveLine k ↘ Spec (.of k))
```

## Tag 01KR, a lemma

[Tag 01KR](https://stacks.math.columbia.edu/tag/01KR) in the Stacks Project.

**`AlgebraicGeometry.isImmersion_pullbackMapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean#L48). The attribute's comment: “immersion”.

> The canonical morphism `X ×[T] Y ⟶ X ×[S] Y` is an immersion.

```lean
theorem isImmersion_pullbackMapDesc : IsImmersion (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.isClosedImmersion_pullbackMapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean#L54). The attribute's comment: “closed immersion if T → S is separated”.

> If `h : T ⟶ S` is separated, the canonical morphism `X ×[T] Y ⟶ X ×[S] Y` is a closed
> immersion.

```lean
theorem isClosedImmersion_pullbackMapDesc [IsSeparated h] :
    IsClosedImmersion (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.quasiCompact_pullbackMapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/MapDescImmersion.lean#L61). The attribute's comment: “quasi-compact if T → S is quasi-separated”.

> If `h : T ⟶ S` is quasi-separated, the canonical morphism `X ×[T] Y ⟶ X ×[S] Y` is
> quasi-compact, being a base change of the quasi-compact diagonal of `h`.

```lean
theorem quasiCompact_pullbackMapDesc [QuasiSeparated h] :
    QuasiCompact (pullback.mapDesc f g h)
```

## Tag 01KS, a lemma

[Tag 01KS](https://stacks.math.columbia.edu/tag/01KS) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L272) (StacksFrontier): “the graph X ⟶ X ×\_S Y is an immersion: more general, cancellation for immersions, applied to the graph followed by the first projection, which is 𝟙 X”. References: EGA I (5.3.13); EGA I (5.3.14), “more general”; EGA I (5.5.12), “special case”; EGA IV (8.12.2), “more general”; EGA IV (16.2.3), “more general”; SGA 6 VIII (1.3), “(iv)”; SGA 6 VIII (1.8), “partial”.
- [`AlgebraicGeometry.IsSeparated.instIsClosedImmersionLiftSchemeId`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.instIsClosedImmersionLiftSchemeId#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L275) (StacksFrontier): “the graph is a closed immersion if Y is separated over S”. References: EGA I (5.4.2), “special case”; EGA I (5.4.3); EGA I (5.4.5), “j = id\_X”.
- [`AlgebraicGeometry.QuasiCompact.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L277) (StacksFrontier): “the graph is quasi-compact if Y is quasi-separated over S: more general, cancellation of quasi-compactness against a quasi-separated map, applied to the graph followed by the first projection (quasi-separated as a base change of Y ⟶ S)”. References: EGA I (5.5.12), “(i), special case”; EGA I (6.3.4), “(v)”; EGA I (6.6.4), “more general”; EGA II (8.14.6), “more general”; EGA IV (1.1.2), “more general”; EGA IV (1.2.4); EGA IV (1.5.4), “(v)”; EGA IV (18.12.13), “more general”; SGA 3 VIB (11.1), “partial”; SGA 3 VIB (12.9), “Quasi-compactness of ρ”; SGA 4 VI (1.9.1), “(iv), special case”.

## Tag 01KT, a lemma

[Tag 01KT](https://stacks.math.columbia.edu/tag/01KT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L282) (StacksFrontier): “a section s of f is an immersion: more general, cancellation for immersions, applied to s ≫ f = 𝟙 S”. References: EGA I (5.3.13); EGA I (5.3.14), “more general”; EGA I (5.5.12), “special case”; EGA IV (8.12.2), “more general”; EGA IV (16.2.3), “more general”; SGA 6 VIII (1.3), “(iv)”; SGA 6 VIII (1.8), “partial”.
- [`AlgebraicGeometry.IsClosedImmersion.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L285) (StacksFrontier): “s is a closed immersion if f is separated: more general, cancellation for closed immersions against a separated map, applied to s ≫ f = 𝟙 S”. References: EGA I (5.4.4); EGA I (5.4.6), “more general”; EGA I (5.5.12), “(i), special case”; EGA IV (17.9.3), “partial”; SGA 1 II (4.17), “more general”; SGA 3 VIB (5.6.3), “(i) ⇒ (ii)”; SGA 3 VIB (11.18.1), “more general”.
- [`AlgebraicGeometry.QuasiCompact.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L288) (StacksFrontier): “s is quasi-compact if f is quasi-separated: more general, cancellation of quasi-compactness against a quasi-separated map, applied to s ≫ f = 𝟙 S”. References: EGA I (5.5.12), “(i), special case”; EGA I (6.3.4), “(v)”; EGA I (6.6.4), “more general”; EGA II (8.14.6), “more general”; EGA IV (1.1.2), “more general”; EGA IV (1.2.4); EGA IV (1.5.4), “(v)”; EGA IV (18.12.13), “more general”; SGA 3 VIB (11.1), “partial”; SGA 3 VIB (12.9), “Quasi-compactness of ρ”; SGA 4 VI (1.9.1), “(iv), special case”.

## Tag 01KU, a lemma

[Tag 01KU](https://stacks.math.columbia.edu/tag/01KU) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated.stableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.stableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L292) (StacksFrontier): “(1) a composition of separated morphisms is separated”. References: EGA I (10.15.3), “(i), ordinary preschemes”; EGA I (5.5.1).
- [`AlgebraicGeometry.quasiSeparated_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L294) (StacksFrontier): “(2) a composition of quasi-separated morphisms is quasi-separated”. References: EGA IV (1.2.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.
- [`AlgebraicGeometry.IsSeparated.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L296) (StacksFrontier): “(3) the base change of a separated morphism is separated”. References: EGA I (10.15.3), “(iii), special case”; EGA I (5.5.1); EGA I (5.5.3), “more general”; EGA III (6.9.1), “separatedness of f′\_i”; EGA III (7.7.2), “separatedness of f'”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 IX (4.2), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “separatedness”.
- [`AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L298) (StacksFrontier): “(4) the base change of a quasi-separated morphism is quasi-separated”. References: EGA IV (1.2.2); EGA IV (2.7.1), “(ii)”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.
- [`CategoryTheory.MorphismProperty.pullbackMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.pullbackMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L300) (StacksFrontier): “(5), (6) a fibre product of (quasi-)separated morphisms is (quasi-)separated: more general, for any morphism property stable under base change and composition”.

## Tag 01KV, a lemma

[Tag 01KV](https://stacks.math.columbia.edu/tag/01KV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L304) (StacksFrontier): “if g ∘ f is separated then so is f”. References: EGA I (5.5.1); EGA I (5.5.8), “sufficiency”; EGA I (5.5.12), “special case”; EGA I (10.15.3), “(iv), special case”; EGA IV (18.12.17), “u is separated”; EGA IV (20.2.5).
- [`AlgebraicGeometry.QuasiSeparated.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiSeparated.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L306) (StacksFrontier): “if g ∘ f is quasi-separated then so is f”. References: EGA I (5.5.12), “special case”; EGA IV (1.2.2); SGA 3 VIB (11.1), “partial”; SGA 4 VI (1.9.1), “1.8 (iii) for schemes”.

## Tag 03GI, a lemma

[Tag 03GI](https://stacks.math.columbia.edu/tag/03GI) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.QuasiCompact.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L65) (StacksFrontier). References: EGA I (5.5.12), “(i), special case”; EGA I (6.3.4), “(v)”; EGA I (6.6.4), “more general”; EGA II (8.14.6), “more general”; EGA IV (1.1.2), “more general”; EGA IV (1.2.4); EGA IV (1.5.4), “(v)”; EGA IV (18.12.13), “more general”; SGA 3 VIB (11.1), “partial”; SGA 3 VIB (12.9), “Quasi-compactness of ρ”; SGA 4 VI (1.9.1), “(iv), special case”.

## Tag 01KN, a lemma

[Tag 01KN](https://stacks.math.columbia.edu/tag/01KN) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.instIsSeparatedOfIsAffine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsSeparatedOfIsAffine#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L266) (StacksFrontier): “an affine scheme is separated”. References: EGA I (5.5.7); EGA II (1.2.4), “special case”.
- [`AlgebraicGeometry.Scheme.instIsSeparatedOfIsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsSeparatedOfIsSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L268) (StacksFrontier): “a morphism from an affine scheme is separated: more general, every morphism out of a separated scheme is separated”. References: EGA I (5.5.1), “(v), special case”; EGA I (5.5.8), “sufficiency”; EGA I (5.5.9), “special case”; EGA I (10.15.3), “(iv), special case”; EGA IV (20.2.5), “special case”.

## Tag 01KW, a lemma

[Tag 01KW](https://stacks.math.columbia.edu/tag/01KW) in the Stacks Project.

**`AlgebraicGeometry.isAffineOpen_inf_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean#L440). The attribute's comment: “the intersection is affine”. References: EGA III (6.6.4), “binary intersections”.

> **Stacks 01KW.** For a separated morphism `f : X ⟶ S` over a separated scheme `S`, the
> intersection of two affine opens of `X` is affine. The hypotheses make `X` separated over the
> terminal scheme, so its absolute diagonal is affine.

```lean
public theorem isAffineOpen_inf_of_isSeparated {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [S.IsSeparated] {U V : X.Opens}
    (hU : IsAffineOpen U) (hV : IsAffineOpen V) : IsAffineOpen (U ⊓ V)
```

**`AlgebraicGeometry.isClosedImmersion_prodLift_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/Separated.lean#L455). The attribute's comment: “closed subscheme of the absolute product”.

> **Stacks 01KW.** Under the hypotheses, `U ∩ V` is a closed subscheme of the absolute
> product `U × V`, the product being taken over the terminal scheme.
>
> The map exhibiting it is the canonical `prod.lift` of the two inclusions `U ⊓ V ⟶ U` and
> `U ⊓ V ⟶ V`. It is obtained from the base change `pullback U.ι V.ι ⟶ pullback (U.ι ≫ 𝟙\_)
> (V.ι ≫ 𝟙\_)` of the absolute diagonal of `X`, which is a closed immersion because `X` is a
> separated scheme, by transporting along `(isPullback_opens_inf U V).isoPullback` on the source
> and `prodIsoPullback` on the target.

```lean
public theorem isClosedImmersion_prodLift_of_isSeparated {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [S.IsSeparated] (U V : X.Opens) :
    IsClosedImmersion (prod.lift (X.homOfLE (inf_le_left : U ⊓ V ≤ U))
      (X.homOfLE (inf_le_right : U ⊓ V ≤ V)))
```

## Tag 01KX, an example

[Tag 01KX](https://stacks.math.columbia.edu/tag/01KX) in the Stacks Project.

**`AlgebraicGeometry.generalLinearTwoScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroup.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroup.lean#L62). The attribute's comment: “gl2”.

> The rank-two general linear scheme over `k`.

```lean
public abbrev generalLinearTwoScheme (k : Type u) [CommRing k] : AlgebraicGeometry.Scheme
```

**`AlgebraicGeometry.generalLinearTwoToProjectiveLine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupProjectiveLine.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupProjectiveLine.lean#L387). The attribute's comment: “gl2\_to\_projective\_line”.

> **Stacks Project, Tag 01KX (gl2\_to\_projective\_line).** The morphism `[a : b]` from `GL₂` to
> the projective line, glued from `b/a` on `D(a)` and `a/b` on `D(b)`.

```lean
noncomputable def generalLinearTwoToProjectiveLine :
    generalLinearTwoScheme k ⟶ projectiveLine k
```

**`AlgebraicGeometry.surjective_generalLinearTwoToProjectiveLine`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupProjectiveLine.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupProjectiveLine.lean#L455). The attribute's comment: “gl2\_to\_projective\_line\_surjective”.

> **Stacks Project, Tag 01KX (gl2\_to\_projective\_line\_surjective).** The morphism `[a : b]` from
> `GL₂` to the projective line is surjective: over the first chart the matrix `!![1, X; 0, 1]` is a
> section, and over the second the matrix `!![X, 1; -1, 0]`.

```lean
instance surjective_generalLinearTwoToProjectiveLine (k : Type u) [Field k] :
    Surjective (generalLinearTwoToProjectiveLine k)
```

**`AlgebraicGeometry.generalLinearTwoToPuncturedPlane`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean#L203). The attribute's comment: “gl2\_to\_punctured\_plane”.

> **Stacks Project, Tag 01KX (gl2\_to\_punctured\_plane).** The morphism from `GL₂` to the
> punctured affine plane `U = Spec k[x, y] ∖ {(x, y)}` determined by `x ↦ a`, `y ↦ b`.

```lean
noncomputable def generalLinearTwoToPuncturedPlane :
    generalLinearTwoScheme k ⟶ (puncturedAffinePlaneOf k).puncturedScheme
```

**`AlgebraicGeometry.surjective_generalLinearTwoToPuncturedPlane`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean#L219). The attribute's comment: “gl2\_to\_punctured\_plane\_surjective”.

> **Stacks Project, Tag 01KX (gl2\_to\_punctured\_plane\_surjective).** The morphism from `GL₂` to
> the punctured affine plane is surjective.

```lean
instance surjective_generalLinearTwoToPuncturedPlane :
    Surjective (generalLinearTwoToPuncturedPlane k)
```

**`AlgebraicGeometry.not_range_subset_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/GeneralLinearGroupPuncturedPlane.lean#L235). The attribute's comment: “image\_in\_no\_affine\_open”.

> **Stacks Project, Tag 01KX (image\_in\_no\_affine\_open).** The image of the morphism from `GL₂`
> to the punctured affine plane is contained in no affine open of the punctured plane: it is
> everything, and the punctured plane is not affine.

```lean
theorem not_range_subset_of_isAffineOpen
    (V : ((puncturedAffinePlaneOf k).puncturedScheme).Opens) (hV : IsAffineOpen V) :
    ¬ Set.range (generalLinearTwoToPuncturedPlane k).base ⊆ (V : Set _)
```

**`AlgebraicGeometry.not_isImmersion_to_affine_projectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Separation/ProjectiveLineNoAffineImmersion.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Separation/ProjectiveLineNoAffineImmersion.lean#L59). The attribute's comment: “projective\_line\_no\_immersion\_into\_affine”.

> The projective line over a field admits no immersion into any affine scheme.

```lean
theorem not_isImmersion_to_affine_projectiveLine
    (k : Type u) [Field k] (A : Scheme.{u}) [IsAffine A] (f : projectiveLine k ⟶ A) :
    ¬ IsImmersion f
```

## Tag 0816, a remark

[Tag 0816](https://stacks.math.columbia.edu/tag/0816) in the Stacks Project.

**`AlgebraicGeometry.compactSpace_and_quasiSeparatedSpace_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L176). The attribute's comment: “(1), quasi-compact and quasi-separated”.

> An affine scheme is quasi-compact and quasi-separated.

```lean
theorem compactSpace_and_quasiSeparatedSpace_of_isAffine (X : Scheme.{u}) [IsAffine X] :
    CompactSpace X ∧ QuasiSeparatedSpace X
```

**`AlgebraicGeometry.compactSpace_and_isSeparated_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L181). The attribute's comment: “(1), quasi-compact and separated”.

> An affine scheme is quasi-compact and separated.

```lean
theorem compactSpace_and_isSeparated_of_isAffine (X : Scheme.{u}) [IsAffine X] :
    CompactSpace X ∧ X.IsSeparated
```

**`AlgebraicGeometry.isSeparated_iff_scheme_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L195). The attribute's comment: “(2), separated”.

> A morphism to a separated scheme is separated if and only if its source is a separated
> scheme. The direction from the source to the morphism holds with no hypothesis on the target; it
> is the converse that uses `Y.IsSeparated`.

```lean
theorem isSeparated_iff_scheme_isSeparated (f : X ⟶ Y) [Y.IsSeparated] :
    IsSeparated f ↔ X.IsSeparated
```

**`AlgebraicGeometry.quasiCompact_and_quasiSeparated_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L203). The attribute's comment: “(2), quasi-compact and quasi-separated”.

> A morphism to a quasi-compact quasi-separated scheme is quasi-compact and quasi-separated if
> and only if its source is a quasi-compact quasi-separated scheme.

```lean
theorem quasiCompact_and_quasiSeparated_iff (f : X ⟶ Y) [CompactSpace Y]
    [QuasiSeparatedSpace Y] :
    (QuasiCompact f ∧ QuasiSeparated f) ↔ (CompactSpace X ∧ QuasiSeparatedSpace X)
```

**`AlgebraicGeometry.quasiCompact_and_isSeparated_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L211). The attribute's comment: “(2), quasi-compact and separated”.

> A morphism to a quasi-compact separated scheme is quasi-compact and separated if and only if
> its source is a quasi-compact separated scheme.

```lean
theorem quasiCompact_and_isSeparated_iff (f : X ⟶ Y) [CompactSpace Y] [Y.IsSeparated] :
    (QuasiCompact f ∧ IsSeparated f) ↔ (CompactSpace X ∧ X.IsSeparated)
```

**`AlgebraicGeometry.quasiSeparatedSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L222). The attribute's comment: “(3), quasi-separated”.

> A fibre product of quasi-separated schemes over a quasi-separated scheme is
> quasi-separated.

```lean
theorem quasiSeparatedSpace_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    [QuasiSeparatedSpace X] [QuasiSeparatedSpace Y] [QuasiSeparatedSpace Z] :
    QuasiSeparatedSpace ↑(pullback f g)
```

**`AlgebraicGeometry.isSeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L233). The attribute's comment: “(3), separated”.

> A fibre product of separated schemes over a separated scheme is separated.

```lean
theorem isSeparated_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    [X.IsSeparated] [Y.IsSeparated] [Z.IsSeparated] : (pullback f g).IsSeparated
```

**`AlgebraicGeometry.compactSpace_and_quasiSeparatedSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L251). The attribute's comment: “(3), quasi-compact and quasi-separated”.

> A fibre product of quasi-compact quasi-separated schemes over a quasi-compact
> quasi-separated scheme is quasi-compact and quasi-separated.

```lean
theorem compactSpace_and_quasiSeparatedSpace_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    [CompactSpace Z] [QuasiSeparatedSpace Z] :
    CompactSpace ↑(pullback f g) ∧ QuasiSeparatedSpace ↑(pullback f g)
```

**`AlgebraicGeometry.compactSpace_and_isSeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L260). The attribute's comment: “(3), quasi-compact and separated”.

> A fibre product of quasi-compact separated schemes over a quasi-compact separated scheme is
> quasi-compact and separated.

```lean
theorem compactSpace_and_isSeparated_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    [CompactSpace X] [X.IsSeparated] [CompactSpace Y] [Y.IsSeparated]
    [CompactSpace Z] [Z.IsSeparated] :
    CompactSpace ↑(pullback f g) ∧ (pullback f g).IsSeparated
```

Declarations registered for the tag:

- [`AlgebraicGeometry.quasiSeparatedSpace_of_isAffine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparatedSpace_of_isAffine#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L70) (StacksFrontier): “(1), quasi-separated”. References: EGA IV (1.9.6), “special case”.
- [`AlgebraicGeometry.Scheme.instIsSeparatedOfIsAffine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsSeparatedOfIsAffine#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L72) (StacksFrontier): “(1), separated”. References: EGA I (5.5.7); EGA II (1.2.4), “special case”.
- [`AlgebraicGeometry.quasiSeparated_iff_quasiSeparatedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_iff_quasiSeparatedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/SchemePropertiesPermanence.lean#L75) (StacksFrontier): “(2), quasi-separated”. References: EGA IV (1.2.3); EGA IV (1.2.6), “special case”; SGA 4 VI (1.14), “(ii), special case”; SGA 4 VI (1.8), “(iii), special case”; SGA 4 VI (1.9.1), “(iii), special case”; SGA 4 VIII (5.1), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.21, Tag 01KH](https://stacks.math.columbia.edu/tag/01KH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
