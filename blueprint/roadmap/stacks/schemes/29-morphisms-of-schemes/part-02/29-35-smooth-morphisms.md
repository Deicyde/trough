---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsStandardSmooth, InfinitesimalLifting.SmoothAt, AlgebraicGeometry.Smooth, RingHom.Smooth.stacksPropertyIsLocal, AlgebraicGeometry.smooth_resLE, AlgebraicGeometry.smooth_tfae, AlgebraicGeometry.smooth_tfae_and_resLE, AlgebraicGeometry.Smooth.of_smooth_fiberToSpecResidueField
statement: formalized
proof: formalized
---

# 29.35 Smooth morphisms

Section 29.35 of the Stacks Project, [Tag 01V4](https://stacks.math.columbia.edu/tag/01V4). 21 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01V5, a definition

[Tag 01V5](https://stacks.math.columbia.edu/tag/01V5) in the Stacks Project.

**`AlgebraicGeometry.IsStandardSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Defs.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Defs.lean#L81). The attribute's comment: “standard\_smooth\_affine”.

> A morphism of affine schemes is standard smooth if the corresponding ring homomorphism on
> global sections is standard smooth.

```lean
public abbrev IsStandardSmooth {X S : AlgebraicGeometry.Scheme.{u}}
    [AlgebraicGeometry.IsAffine X] [AlgebraicGeometry.IsAffine S] (f : X ⟶ S) : Prop
```

Declarations registered for the tag:

- [`InfinitesimalLifting.SmoothAt`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/InfinitesimalLifting.lean#L148), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/AtPoint.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/AtPoint.lean#L69) (StacksFrontier): “smooth\_at\_point”.
- [`AlgebraicGeometry.Smooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Smooth#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Defs.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Defs.lean#L66) (StacksFrontier): “smooth\_morphism”. References: EGA IV (17.3.1); SGA 1 II (1.1); SGA 3 XI (1.1); SGA 3 XI (1.6); SGA 7 XIV (2.1), “partial”.

## Tag 01V6, a lemma

[Tag 01V6](https://stacks.math.columbia.edu/tag/01V6) in the Stacks Project.

**`RingHom.Smooth.stacksPropertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L114). The attribute's comment: “smoothness of ring maps is local”.

> Smoothness of ring maps is a local property.

```lean
theorem Smooth.stacksPropertyIsLocal : StacksPropertyIsLocal RingHom.Smooth
```

**`AlgebraicGeometry.smooth_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L256). The attribute's comment: “moreover: restriction to open subschemes”.

> If `f` is smooth then so is its restriction `U → V` to any opens `U ⊆ X`, `V ⊆ S` with
> `f(U) ⊆ V`.

```lean
theorem smooth_resLE {f : X ⟶ S} (hf : Smooth f) (V : S.Opens) (U : X.Opens)
    (e : U ≤ f ⁻¹ᵁ V) : Smooth (f.resLE V U e)
```

**`AlgebraicGeometry.smooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L264). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> Smoothness of a morphism of schemes can be checked on all pairs of affine opens, on open
> coverings of target and preimages, or on affine such coverings.

```lean
theorem smooth_tfae (f : X ⟶ S) :
    List.TFAE [
      Smooth f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Smooth,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, Smooth (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.Smooth]
```

**`AlgebraicGeometry.smooth_tfae_and_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L280).

> The whole statement: the four characterizations of smoothness agree, and smoothness passes
> to restrictions to open subschemes.

```lean
theorem smooth_tfae_and_resLE (f : X ⟶ S) :
    List.TFAE [
      Smooth f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Smooth,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, Smooth (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.Smooth] ∧
    (Smooth f → ∀ (U : X.Opens) (V : S.Opens) (e : U ≤ f ⁻¹ᵁ V), Smooth (f.resLE V U e))
```

## Tag 01V8, a lemma

[Tag 01V8](https://stacks.math.columbia.edu/tag/01V8) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Smooth.of_smooth_fiberToSpecResidueField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Smooth.of_smooth_fiberToSpecResidueField#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/FlatSmoothFibres.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/FlatSmoothFibres.lean#L20) (StacksFrontier). References: EGA IV (17.5.1), “b)⇒a), global form”; EGA IV (17.8.2), “special case”; SGA 1 II (2.1), “sufficiency, global form”; SGA 1 II (2.2), “sufficiency with Y=S”; SGA 3 VIB (3.10), “partial”; SGA 3 VIB (4.4), “more general”; SGA 3 VIB (8.4), “(ii)”; SGA 3 VIII (2.1), “partial”; SGA 3 XI (1.2), “(i)”; SGA 3 XV (1.1), “partial”.

## Tag 01VA, a lemma

[Tag 01VA](https://stacks.math.columbia.edu/tag/01VA) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.smooth_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.smooth_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L255) (StacksFrontier). References: EGA IV (17.3.3), “smooth branch of (ii)”; EGA IV (6.8.3), “more general”; SGA 1 II (1.3), “more general”.

## Tag 01VB, a lemma

[Tag 01VB](https://stacks.math.columbia.edu/tag/01VB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.smooth_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.smooth_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/SmoothMorphisms/Basic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/SmoothMorphisms/Basic.lean#L56) (StacksFrontier): “the base change of a smooth morphism is smooth”. References: EGA IV (17.3.3), “smooth branch of (iii)”; EGA IV (17.7.3), “(ii)”; EGA IV (6.8.2), “globally smooth f”; EGA IV (6.8.3), “more general”; SGA 1 II (1.3), “more general”; SGA 1 II (4.13), “global ascent”; SGA 3 VIB (10.1), “smooth morphisms”; SGA 3 VIB (2.1.2), “partial”; SGA 3 XIX (2.1), “(i)”; SGA 6 VIII (1.6), “partial”; SGA 6 VIII (1.8), “partial”; SGA 6 X (7.13.3), “partial”.

## Tag 01VC, a lemma

[Tag 01VC](https://stacks.math.columbia.edu/tag/01VC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instSmoothOfIsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instSmoothOfIsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L256) (StacksFrontier). References: SGA 1 II (1.3), “more general”.

## Tag 01VD, a lemma

[Tag 01VD](https://stacks.math.columbia.edu/tag/01VD) in the Stacks Project.

**`AlgebraicGeometry.syntomic_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SmoothMorphisms/Basic.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/SmoothMorphisms/Basic.lean#L45).

> A smooth morphism of schemes is syntomic.

```lean
theorem syntomic_of_smooth {X S : Scheme.{u}} (f : X ⟶ S) [Smooth f] : Syntomic f
```

## Tag 01VE, a lemma

[Tag 01VE](https://stacks.math.columbia.edu/tag/01VE) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instLocallyOfFinitePresentationOfSmooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instLocallyOfFinitePresentationOfSmooth#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L257) (StacksFrontier). References: SGA 3 III (0.6), “partial”; SGA 3 III (2.5), “partial”.

## Tag 01VF, a lemma

[Tag 01VF](https://stacks.math.columbia.edu/tag/01VF) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instFlatOfSmooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instFlatOfSmooth#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L258) (StacksFrontier). References: EGA IV (17.5.1), “a)⇒flatness in b)”; EGA IV (17.5.2), “necessity”; EGA IV (17.15.15), “necessity: flatness”; SGA 1 II (2.1), “necessity of (a)”; SGA 1 IX (1.2), “more general”; SGA 3 VIB (8.4), “(ii)”; SGA 3 XI (1.2), “(i)”.

## Tag 056G, a lemma

[Tag 056G](https://stacks.math.columbia.edu/tag/056G) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyOpen.of_flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.of_flat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L327) (StacksFrontier): “flat and locally of finite presentation; smooth morphisms are both (instances)”. References: EGA IV (1.10.4), “b) ⇒ a), special case”; EGA IV (11.3.1), “special case”; EGA IV (14.4.10), “special case”; EGA IV (15.2.1); EGA IV (15.2.4), “(ii), special case”; EGA IV (18.2.7), “partial”; EGA IV (2.4.6); EGA IV (2.4.7), “more general”; EGA IV (4.4.1), “special case”; SGA 1 IV (6.6), “F = O\_X”; SGA 1 VIII (4.9), “more general”; SGA 3 V (10.1.1), “more general”; SGA 3 V (4.1.1), “flat and fp implies open”; SGA 3 VIA (2.5.4), “Final implication”; SGA 3 VIB (3.11), “more general”; SGA 3 VIB (4.3); SGA 3 VIB (7.5), “f|\_V is an open morphism”; SGA 3 X (5.4), “partial”; SGA 3 XVI (2.1), “more general”; SGA 6 VIII (1.3), “more general”.

## Tag 01V7, a lemma

[Tag 01V7](https://stacks.math.columbia.edu/tag/01V7) in the Stacks Project.

**`InfinitesimalLifting.smoothAt_iff_exists_affine_isStandardSmooth`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/AtPoint.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/AtPoint.lean#L145).

> Smoothness at a point is equivalent to standard smoothness on a suitable affine
> neighbourhood lying over any prescribed affine neighbourhood of the image point.

```lean
public lemma smoothAt_iff_exists_affine_isStandardSmooth
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) (V : S.Opens)
    (hV : IsAffineOpen V) (hxV : x ∈ f ⁻¹ᵁ V) :
    InfinitesimalLifting.SmoothAt f x ↔
      ∃ (U : X.Opens) (hU : IsAffineOpen U) (_ : x ∈ U)
        (hUV : U ≤ f ⁻¹ᵁ V),
        @AlgebraicGeometry.IsStandardSmooth
          U.toScheme V.toScheme hU hV (f.resLE V U hUV)
```

## Tag 02G1, a lemma

[Tag 02G1](https://stacks.math.columbia.edu/tag/02G1) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isFiniteLocallyFree_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DifferentialsLocallyFree.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DifferentialsLocallyFree.lean#L96). The attribute's comment: “differentials\_finite\_locally\_free”. References: EGA IV (17.15.15), “necessity: Ω loc free”; EGA IV (17.10.2), “locally free”; EGA IV (17.15.5), “a) => c) (free)”; SGA 1 II (4.3), “(ii) local freeness”; SGA 3 XI (1.9), “finite locally free”.

> The sheaf of relative differentials of a smooth morphism of
> schemes is finite locally free.

```lean
theorem Scheme.Hom.isFiniteLocallyFree_relativeDifferentials (f : X ⟶ S) [Smooth f] :
    SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf)
      (Scheme.Hom.relativeDifferentials f)
```

**`AlgebraicGeometry.finrank_stalk_relativeDifferentials_eq_fiberDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DifferentialsRank.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DifferentialsRank.lean#L76). The attribute's comment: “differentials\_rank\_eq\_fibre\_dimension”. References: EGA IV (17.10.2), “rank\_x = dim\_x f”; EGA IV (17.15.5), “a) => c) rank”; EGA IV (17.15.15), “smooth ⇒ rank=dim\_x f”; SGA 3 XI (1.9), “rank = fiber dimension”; SGA 1 II (4.3), “(ii) rank formula”.

> **Stacks Project, Tag 02G1.** For a smooth morphism of schemes, the rank at a point of the
> sheaf of relative differentials is the local dimension of the fibre at that point.

```lean
theorem finrank_stalk_relativeDifferentials_eq_fiberDimensionAt {X S : Scheme.{u}} (f : X ⟶ S)
    [Smooth f] (x : X) :
    (Module.finrank (ToType (X.sheaf.presheaf.stalk x))
        (ToType (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
          (Scheme.Hom.relativeDifferentials f).val.presheaf x)) : WithBot ℕ∞) =
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)
```

## Tag 02G2, a definition

[Tag 02G2](https://stacks.math.columbia.edu/tag/02G2) in the Stacks Project.

**`AlgebraicGeometry.IsSmoothOfRelativeDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/RelativeDimension.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/RelativeDimension.lean#L65).

> **Stacks 02G2.** A morphism of schemes `f : X ⟶ S` is smooth of relative dimension `d` if it
> is smooth and its sheaf of relative differentials `Ω_{X/S}` is finite locally free of constant
> rank `d`.

```lean
def IsSmoothOfRelativeDimension (d : ℕ) (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.smoothOfRelativeDimension_iff_smooth_and_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/RelativeDimension.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/RelativeDimension.lean#L117). The attribute's comment: “Mathlib's chart-wise definition agrees with Stacks'”.

> **Stacks 02G2, Mathlib's notion.** A morphism of schemes is smooth of relative dimension `d`
> in the chart-wise sense of `AlgebraicGeometry.SmoothOfRelativeDimension` exactly when it is
> smooth and its sheaf of relative differentials is finite locally free of rank `d`.

```lean
theorem smoothOfRelativeDimension_iff_smooth_and_isFiniteLocallyFreeOfRank (d : ℕ) (f : X ⟶ S) :
    SmoothOfRelativeDimension d f ↔
      Smooth f ∧ SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (R := X.ringCatSheaf) (Scheme.Hom.relativeDifferentials f) d
```

## Tag 01V9, a lemma

[Tag 01V9](https://stacks.math.columbia.edu/tag/01V9) in the Stacks Project.

**`Stacks.FiberCotangentAssembly.fiberDifferentialsTensorIdentification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiberCotangentAssembly/Basic.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiberCotangentAssembly/Basic.lean#L461). The attribute's comment: “canonical identification in part (4)”.

> The fibre of the sheaf of relative differentials at `x` is canonically identified with the
> fibre of the relative differentials of the scheme-theoretic fibre.

```lean
public noncomputable def fiberDifferentialsTensorIdentification :
    FiberDifferentialsTensorIdentification f x
```

**`Stacks.Tag01V9NumericalCriterion.smoothAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NumericalCriterion/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NumericalCriterion/Basic.lean#L95).

> For a morphism locally of finite presentation, the following
> are equivalent: smoothness at `x`; flatness of the local-ring map together with smoothness of the
> scheme-theoretic fibre; either of the two numerical differential criteria; a standard smooth
> affine neighbourhood; and an affine presentation whose chosen Jacobian determinant does not
> vanish at `x`.

```lean
public theorem smoothAt_tfae [LocallyOfFinitePresentation f] :
    List.TFAE [
      InfinitesimalLifting.SmoothAt f x,
      (f.stalkMap x).hom.Flat ∧
        InfinitesimalLifting.SmoothAt (f.fiberToSpecResidueField (f x)) (f.asFiber x),
      (f.stalkMap x).hom.Flat ∧
        (let B := X.presheaf.stalk x
         let Ω := relativeDifferentialStalk f x
         letI := relativeDifferentialStalkModule f x
         GeneratedByAtMost B Ω (topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x))),
      (f.stalkMap x).hom.Flat ∧
        (let k := X.residueField x
         GeneratedByAtMost k (relativeCotangentSpace f x)
           (topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x))),
      ∃ (U : X.affineOpens) (V : S.affineOpens) (_ : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        AlgebraicGeometry.IsStandardSmooth (f.resLE V.1 U.1 hUV),
      ∃ (U : X.affineOpens) (V : S.affineOpens) (hxU : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        letI : Algebra Γ(S, V.1) Γ(X, U.1) := (f.appLE V U hUV).hom.toAlgebra
        ∃ (n c : ℕ) (P : Algebra.PreSubmersivePresentation
            Γ(S, V.1) Γ(X, U.1) (Fin n) (Fin c)),
          P.jacobian ∉ (U.2.primeIdealOf ⟨x, hxU⟩).asIdeal]
```

## Tag 02V4, a lemma

[Tag 02V4](https://stacks.math.columbia.edu/tag/02V4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.smoothLocus_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/LocusBaseChange.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/LocusBaseChange.lean#L113). References: EGA IV (17.7.2), “(ii)”; EGA IV (17.7.4), “(v)”; EGA IV (17.7.1), “(ii) smooth”; SGA 1 II (4.13), “special case”; SGA 3 VIB (2.5), “special case”; SGA 3 VIB (3.10), “special case”; SGA 3 X (8.9), “partial”.

> **The smooth locus of a base change is the inverse image of the smooth locus.** Let
> ```
> X' → X
> ↓    ↓
> S' → S
> ```
> be a cartesian diagram of schemes, with `f : X ⟶ S` locally of finite presentation. Assume that
> `f` is flat, or that `g : S' ⟶ S` is flat. Then the open subscheme of `X'` where the base-changed
> morphism `f' : X' ⟶ S'` is smooth is the inverse image under `g' : X' ⟶ X` of the open subscheme
> of `X` where `f` is smooth.
>
> **Stacks Project, Tag 02V4.** Both of its cases are covered, the first by flatness of `f` and
> the second by flatness of `g`. The instance `LocallyOfFinitePresentation f'` imposes no condition:
> it follows from that of `f` by stability under base change, and it is what makes the smooth locus
> `f'.smoothLocus` of the base-changed morphism defined.

```lean
theorem Scheme.Hom.smoothLocus_eq_preimage_of_isPullback {f : X ⟶ S} {g : S' ⟶ S} {f' : X' ⟶ S'}
    {g' : X' ⟶ X} [LocallyOfFinitePresentation f] [LocallyOfFinitePresentation f']
    (sq : IsPullback g' f' f g) (hflat : Flat f ∨ Flat g) :
    f'.smoothLocus = g' ⁻¹ᵁ f.smoothLocus
```

## Tag 02K4, a lemma

[Tag 02K4](https://stacks.math.columbia.edu/tag/02K4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.toRelativeDifferentials_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FormallySmooth.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FormallySmooth.lean#L317). References: EGA IV (17.2.3).

> For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ S` with `f` formally smooth, the canonical
> sequence `0 ⟶ f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0` of `𝒪_X`-modules is short exact. The case of a
> smooth `f` is the special case obtained from
> `Stacks.Smooth.smooth_iff_locallyOfFinitePresentation_and_formallySmooth`.

```lean
theorem toRelativeDifferentials_shortExact (f : X ⟶ Y) (g : Y ⟶ S) (hf : FormallySmooth f) :
    ∃ h : relativeDifferentialsMap f g (f ≫ g) (𝟙 S) (Category.comp_id (f ≫ g)).symm ≫
        f.toRelativeDifferentials g = 0,
      (ShortComplex.mk _ _ h).ShortExact
```

## Tag 06AA, a lemma

[Tag 06AA](https://stacks.math.columbia.edu/tag/06AA) in the Stacks Project.

**`Stacks.ConormalSequenceRight.conormalShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/SchemeShortExact.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/SchemeShortExact.lean#L399). References: SGA 7 XI (1.3), “partial”.

> **[Stacks, Tag 06AA].** For an immersion of schemes `i : Z ⟶ X` over `p : X ⟶ S` with `Z`
> smooth over `S`, the conormal sequence `0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0` of
> [Stacks, Tag 01UZ] is short exact.
>
> A smooth morphism is formally smooth by [Stacks, Tag 02H6], and formal smoothness is all the
> proof uses.

```lean
theorem conormalShortComplex_shortExact {Z X S : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (p : X ⟶ S) (hZ : AlgebraicGeometry.Smooth (i ≫ p)) :
    (conormalShortComplex i p).ShortExact
```

## Tag 06AB, a lemma

[Tag 06AB](https://stacks.math.columbia.edu/tag/06AB) in the Stacks Project.

**`Stacks.ConormalSequenceTwoImmersions.mono_conormalTransitivityMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalMono.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalMono.lean#L451). The attribute's comment: “exactness on the left, that is, that the first arrow `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of the sequence of 067L is a monomorphism. Exactness at `𝒞_{Z/X}` and surjectivity onto `i^*Ω_{X/Y}` are the content of 067L and are not restated here; they are proved in the modules named in the module docstring, which also says where the second arrow of the sequence is.”.

> **[Stacks, Tag 06AB], exactness on the left.** For immersions `i : Z ⟶ X` and `j : Z ⟶ Y`
> in a commutative triangle `i ≫ p = j` with `p` smooth, the canonical map
> `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of [Stacks, Tag 067L] is a monomorphism.
>
> A smooth morphism induces a smooth, hence formally smooth, ring map on every compatible pair of
> affine opens, so this is `mono_conormalTransitivityMap_of_formallySmooth`.

```lean
theorem mono_conormalTransitivityMap [Smooth p] (h : i ≫ p = j) :
    Mono (conormalTransitivityMap i j p h)
```

## Tag 02K5, a lemma

[Tag 02K5](https://stacks.math.columbia.edu/tag/02K5) in the Stacks Project.

**`Stacks.Smooth.smooth_of_comp_surjective_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean#L143).

> **Stacks Project, Tag 02KM (smooth case).** If `f` is surjective and smooth and `f ≫ q` is
> smooth, then `q` is smooth.
>
> This is also Stacks 02K5: there the target of `f ≫ q` is additionally assumed locally of finite
> presentation, which that source's own footnote observes is implied by the other hypotheses.

```lean
theorem smooth_of_comp_surjective_smooth (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Smooth f]
    [Smooth (f ≫ q)] : Smooth q
```

## Tag 05D9, a lemma

[Tag 05D9](https://stacks.math.columbia.edu/tag/05D9) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpens_free_conormal_powerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Section.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Section.lean#L253).

> At a smooth point of a section, there are compatible affine open neighbourhoods on which the
> conormal module is free and the completion is a formal power series algebra over the base.

```lean
public theorem exists_affineOpens_free_conormal_powerSeries
    {X S : Scheme.{u}} (f : X ⟶ S) (σ : S ⟶ X)
    (hσ : σ ≫ f = 𝟙 S) (s : S)
    (hsmooth : InfinitesimalLifting.SmoothAt f (σ s)) :
    ∃ (U : S.Opens) (V : X.Opens) (_ : IsAffineOpen U)
      (_ : IsAffineOpen V) (_ : s ∈ U) (_ : σ s ∈ V)
      (hVU : V ≤ f ⁻¹ᵁ U) (hUV : U ≤ σ ⁻¹ᵁ V),
      let A := Γ(S, U)
      let B := Γ(X, V)
      letI : Algebra A B := (f.appLE U V hVU).hom.toAlgebra
      ∃ (sectionHom : B →ₐ[A] A),
        sectionHom.toRingHom = (σ.appLE V U hUV).hom ∧
        (letI : Algebra B A := sectionHom.toAlgebra
         Module.Free A (RingHom.ker sectionHom.toRingHom).Cotangent) ∧
        (letI : Algebra B A := sectionHom.toAlgebra
         Nonempty (AdicCompletion (RingHom.ker sectionHom.toRingHom) B ≃ₐ[A]
           MvPowerSeries (Fin (Module.finrank A
             (RingHom.ker sectionHom.toRingHom).Cotangent)) A))
```

## Tag 0AFF, a lemma

[Tag 0AFF](https://stacks.math.columbia.edu/tag/0AFF) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SmoothDimensionFormula.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SmoothDimensionFormula.lean#L44).

> **Stacks Project, Tag 0AFF.** For a smooth morphism of locally Noetherian schemes the
> dimension of the source at a point is the dimension of the target at its image plus the
> dimension of the fibre at that point.

```lean
public theorem topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber_of_smooth
    {X Y : Scheme.{u}} [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (f : X ⟶ Y) [Smooth f]
    (x : X) :
    topologicalKrullDimAt X x =
      topologicalKrullDimAt Y (f x) +
        topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DimensionFormula.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/DimensionFormula.lean#L99).

> **Stacks Project, Tag 0AFF.** For a smooth morphism of locally Noetherian schemes the
> dimension of the source at a point is the dimension of the target at its image plus the dimension
> of the fibre at that point.

```lean
public theorem topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber_of_smooth
    {X Y : Scheme.{u}} [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (f : X ⟶ Y) [Smooth f]
    (x : X) :
    topologicalKrullDimAt X x =
      topologicalKrullDimAt Y (f x) +
        topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.35, Tag 01V4](https://stacks.math.columbia.edu/tag/01V4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
