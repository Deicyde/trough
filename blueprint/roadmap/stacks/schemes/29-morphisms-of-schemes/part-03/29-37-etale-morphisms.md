---
declaration: section
origin: cited
lean: AlgebraicGeometry.EtaleAt, AlgebraicGeometry.IsStandardEtale, AlgebraicGeometry.Etale, AlgebraicGeometry.etale_resLE, AlgebraicGeometry.etale_tfae, AlgebraicGeometry.etale_tfae_and_resLE, AlgebraicGeometry.Etale.etale_comp, AlgebraicGeometry.Etale.etale_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 29.37 Étale morphisms

Section 29.37 of the Stacks Project, [Tag 02GH](https://stacks.math.columbia.edu/tag/02GH). 21 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02GI, a definition

[Tag 02GI](https://stacks.math.columbia.edu/tag/02GI) in the Stacks Project.

**`AlgebraicGeometry.EtaleAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Defs.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Defs.lean#L59). The attribute's comment: “etale\_at\_point”. References: SGA 1 IX (1.1).

> A morphism of schemes is étale at `x` if it induces an étale map on the
> coordinate rings of some affine open neighbourhood of `x` and some affine
> open neighbourhood of its image.

```lean
public abbrev EtaleAt (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.IsStandardEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/StandardEtale.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/StandardEtale.lean#L59). The attribute's comment: “standard\_etale\_morphism”.

> A morphism of affine schemes is *standard étale* if its map on global sections is a
> standard étale ring map.

```lean
public abbrev IsStandardEtale {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Defs.lean#L53) (StacksFrontier): “etale\_morphism”. References: EGA IV (17.3.1); SGA 1 I (4.1); SGA 3 XI (1.1); SGA 3 XI (1.6); SGA 4 VII (1.1).

## Tag 02GJ, a lemma

[Tag 02GJ](https://stacks.math.columbia.edu/tag/02GJ) in the Stacks Project.

**`AlgebraicGeometry.etale_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean#L52). The attribute's comment: “moreover: restriction to open subschemes”.

> If `f` is étale then so is its restriction `U → V` to any opens `U ⊆ X`, `V ⊆ S` with
> `f(U) ⊆ V`.

```lean
theorem etale_resLE {f : X ⟶ S} (hf : Etale f) (U : X.Opens) (V : S.Opens)
    (e : U ≤ f ⁻¹ᵁ V) : Etale (f.resLE V U e)
```

**`AlgebraicGeometry.etale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean#L60). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> Étaleness of a morphism of schemes can be checked on all pairs of affine opens, on open
> coverings of the target and of the preimages of their members, or on affine such coverings.

```lean
theorem etale_tfae (f : X ⟶ S) :
    List.TFAE [
      Etale f,
      ∀ (U : X.affineOpens) (V : S.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Etale,
      ∃ (J : Type u) (V : J → S.Opens) (I : J → Type u) (U : ∀ j, I j → X.Opens),
        ⨆ j, V j = ⊤ ∧ (∀ j, ⨆ i, U j i = f ⁻¹ᵁ V j) ∧
          ∀ j i, ∃ e : U j i ≤ f ⁻¹ᵁ V j, Etale (f.resLE (V j) (U j i) e),
      ∃ (J : Type u) (V : J → S.affineOpens) (I : J → Type u) (U : ∀ j, I j → X.affineOpens),
        ⨆ j, (V j).1 = ⊤ ∧ (∀ j, ⨆ i, (U j i).1 = f ⁻¹ᵁ (V j).1) ∧
          ∀ j i, ∃ e : (U j i).1 ≤ f ⁻¹ᵁ (V j).1, (f.appLE (V j) (U j i) e).hom.Etale]
```

**`AlgebraicGeometry.etale_tfae_and_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalCharacterization.lean#L110).

> The whole statement: the four characterizations of étaleness agree, and étaleness passes to
> restrictions to open subschemes.

```lean
theorem etale_tfae_and_resLE (f : X ⟶ S) :
    List.TFAE [
      Etale f,
      ∀ (U : X.affineOpens) (V : S.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Etale,
      ∃ (J : Type u) (V : J → S.Opens) (I : J → Type u) (U : ∀ j, I j → X.Opens),
        ⨆ j, V j = ⊤ ∧ (∀ j, ⨆ i, U j i = f ⁻¹ᵁ V j) ∧
          ∀ j i, ∃ e : U j i ≤ f ⁻¹ᵁ V j, Etale (f.resLE (V j) (U j i) e),
      ∃ (J : Type u) (V : J → S.affineOpens) (I : J → Type u) (U : ∀ j, I j → X.affineOpens),
        ⨆ j, (V j).1 = ⊤ ∧ (∀ j, ⨆ i, (U j i).1 = f ⁻¹ᵁ (V j).1) ∧
          ∀ j i, ∃ e : (U j i).1 ≤ f ⁻¹ᵁ (V j).1, (f.appLE (V j) (U j i) e).hom.Etale] ∧
    (Etale f → ∀ (U : X.Opens) (V : S.Opens) (e : U ≤ f ⁻¹ᵁ V), Etale (f.resLE V U e))
```

## Tag 02GN, a lemma

[Tag 02GN](https://stacks.math.columbia.edu/tag/02GN) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale.etale_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L168) (StacksFrontier). References: EGA IV (17.3.3), “(ii), étale case”; EGA IV (17.3.5), “étale clause”; SGA 1 I (4.6); SGA 1 V (3.3), “special case”.

## Tag 02GO, a lemma

[Tag 02GO](https://stacks.math.columbia.edu/tag/02GO) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale.etale_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L169) (StacksFrontier). References: EGA IV (17.3.3), “(iii), étale case”; EGA IV (17.7.3), “(ii)”; SGA 1 I (4.6); SGA 1 IX (1.3); SGA 1 IX (4.2), “Étaleness of X₁' → S₁'”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (2.1.2), “partial”; SGA 3 VIIB (1.6.C), “special case”; SGA 4 VII (1.4), “partial”; SGA 4½ Arcata (2.1.3).

## Tag 02GK, a lemma

[Tag 02GK](https://stacks.math.columbia.edu/tag/02GK) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_iff_smoothAt_and_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Basic.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Basic.lean#L116). References: EGA IV (17.6.2), “more general”; SGA 3 XI (1.4), “more general”.

> A morphism of schemes is étale at a point if and only if it is smooth and
> unramified at that point.

```lean
public theorem etaleAt_iff_smoothAt_and_unramifiedAt {X S : Scheme.{u}}
    (f : X ⟶ S) (x : X) :
    EtaleAt f x ↔
      (InfinitesimalLifting.SmoothAt f x ∧ UnramifiedAt f x)
```

**`AlgebraicGeometry.Space.isEtaleAt_iff_isSmoothAt_and_isUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtPointCriteria.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtPointCriteria.lean#L177). The attribute's comment: “for algebraic spaces, at a point”.

> A morphism of algebraic spaces over `S` is étale at a point of its source if and only if it
> is smooth and unramified at that point.

```lean
theorem isEtaleAt_iff_isSmoothAt_and_isUnramifiedAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (x : points B S hS X) :
    IsEtaleAt B S hS f x ↔ IsSmoothAt B S hS f x ∧ IsUnramifiedAt B S hS f x
```

## Tag 03WS, a lemma

[Tag 03WS](https://stacks.math.columbia.edu/tag/03WS) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean#L54).

> An étale morphism of schemes is locally quasi-finite.

```lean
theorem locallyQuasiFinite_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] :
    LocallyOfFiniteType f ∧ LocallyQuasiFinite f
```

## Tag 02GL, a lemma

[Tag 02GL](https://stacks.math.columbia.edu/tag/02GL) in the Stacks Project.

**`AlgebraicGeometry.Etale.exists_iso_fiber_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean#L111). The attribute's comment: “part (2)”. References: EGA IV (17.6.2), “a) => c')”.

> **Stacks Project, Tag 02GL, part (2).** Every fibre of an étale morphism is, over the
> residue field of the base point, a coproduct of spectra of finite separable field extensions.

```lean
public theorem Etale.exists_iso_fiber_coproduct_spectra_finite_separable
    {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] (s : S) :
    ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
      (_ : ∀ i, Algebra (S.residueField s) (K i))
      (_ : ∀ i, Module.Finite (S.residueField s) (K i))
      (_ : ∀ i, Algebra.IsSeparable (S.residueField s) (K i))
      (e : f.fiber s ≅ ∐ fun i ↦ Spec (.of (K i))),
      e.hom ≫ Sigma.desc (fun i ↦
        Spec.map (CommRingCat.ofHom (algebraMap (S.residueField s) (K i)))) =
        f.fiberToSpecResidueField s
```

Declarations registered for the tag:

- [`AlgebraicGeometry.etale_iff_iso_coproduct_spectra_finite_separable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean#L75), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean#L105) (StacksFrontier): “part (1)”.

## Tag 02GM, a lemma

[Tag 02GM](https://stacks.math.columbia.edu/tag/02GM) in the Stacks Project.

**`AlgebraicGeometry.etale_of_flat_of_fibers_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/FlatFibers.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/FlatFibers.lean#L55). References: EGA IV (17.6.2), “c') => a)”; EGA IV (18.2.3), “a') ⇒ a)”; SGA 1 IX (1.2), “converse direction”; SGA 4 VII (1.1), “flat+fibers => étale”.

> A flat, locally finitely presented morphism with fibres that are disjoint unions of spectra
> of finite separable extensions of residue fields is étale.

```lean
public theorem etale_of_flat_of_fibers_finite_separable
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (h : ∀ s : S,
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra (S.residueField s) (K i))
        (_ : ∀ i, Module.Finite (S.residueField s) (K i))
        (_ : ∀ i, Algebra.IsSeparable (S.residueField s) (K i))
        (e : f.fiber s ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦
          Spec.map (CommRingCat.ofHom (algebraMap (S.residueField s) (K i)))) =
            f.fiberToSpecResidueField s) :
    Etale f
```

## Tag 02GP, a lemma

[Tag 02GP](https://stacks.math.columbia.edu/tag/02GP) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale.instOfIsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.instOfIsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OpenImmersionCriterion.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OpenImmersionCriterion.lean#L49) (StacksFrontier). References: EGA IV (17.1.3), “more general”; EGA IV (17.3.3); EGA IV (17.9.1), “(a) ⇒ étaleness in (c)”; SGA 1 I (4.6); SGA 1 I (5.1), “necessity”; SGA 1 IX (1.4), “Necessity”.

## Tag 02GQ, a lemma

[Tag 02GQ](https://stacks.math.columbia.edu/tag/02GQ) in the Stacks Project.

**`AlgebraicGeometry.syntomic_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean#L59).

> An étale morphism of schemes is syntomic.

```lean
lemma syntomic_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] : Syntomic f
```

## Tag 02GR, a lemma

[Tag 02GR](https://stacks.math.columbia.edu/tag/02GR) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean#L64).

> An étale morphism of schemes is locally of finite presentation.

```lean
lemma locallyOfFinitePresentation_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] :
    LocallyOfFinitePresentation f
```

## Tag 02GS, a lemma

[Tag 02GS](https://stacks.math.columbia.edu/tag/02GS) in the Stacks Project.

**`AlgebraicGeometry.flat_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Etale.lean#L70).

> An étale morphism of schemes is flat.

```lean
lemma flat_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] : Flat f
```

## Tag 03WT, a lemma

[Tag 03WT](https://stacks.math.columbia.edu/tag/03WT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyOpen.of_flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.of_flat#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean#L36) (StacksFrontier): “a flat morphism locally of finite presentation is universally open”. References: EGA IV (1.10.4), “b) ⇒ a), special case”; EGA IV (11.3.1), “special case”; EGA IV (14.4.10), “special case”; EGA IV (15.2.1); EGA IV (15.2.4), “(ii), special case”; EGA IV (18.2.7), “partial”; EGA IV (2.4.6); EGA IV (2.4.7), “more general”; EGA IV (4.4.1), “special case”; SGA 1 IV (6.6), “F = O\_X”; SGA 1 VIII (4.9), “more general”; SGA 3 V (10.1.1), “more general”; SGA 3 V (4.1.1), “flat and fp implies open”; SGA 3 VIA (2.5.4), “Final implication”; SGA 3 VIB (3.11), “more general”; SGA 3 VIB (4.3); SGA 3 VIB (7.5), “f|\_V is an open morphism”; SGA 3 X (5.4), “partial”; SGA 3 XVI (2.1), “more general”; SGA 6 VIII (1.3), “more general”.
- [`AlgebraicGeometry.Scheme.Hom.isOpenMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.isOpenMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean#L58) (StacksFrontier): “a universally open morphism is open on the underlying spaces”.

## Tag 02GT, a lemma

[Tag 02GT](https://stacks.math.columbia.edu/tag/02GT) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_iff_exists_isStandardEtale_restrict`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/StandardEtale.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/StandardEtale.lean#L143).

> A scheme morphism is étale at a point if and only if, over any fixed
> affine open neighbourhood of its image, it is standard étale on some affine
> open neighbourhood of the point.

```lean
public lemma etaleAt_iff_exists_isStandardEtale_restrict
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) (V : S.Opens)
    (hV : IsAffineOpen V) (hxV : f x ∈ V) :
    EtaleAt f x ↔
      ∃ (U : X.Opens) (hU : IsAffineOpen U) (_ : x ∈ U)
        (hUV : U ≤ f ⁻¹ᵁ V),
        @AlgebraicGeometry.IsStandardEtale
          U.toScheme V.toScheme hU hV (f.resLE V U hUV)
```

## Tag 02GU, a lemma

[Tag 02GU](https://stacks.math.columbia.edu/tag/02GU) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/AtPointCriteria.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/AtPointCriteria.lean#L408). References: SGA 4½ Arcata (2.1.1), “b) <=> c)”.

> **Stacks Project, Tag 02GU.** Ten equivalent criteria for a morphism of schemes locally of
> finite presentation to be étale at a point.

```lean
public theorem etaleAt_tfae {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (x : X) :
    List.TFAE [
      EtaleAt f x,
      (f.stalkMap x).hom.Flat ∧
        EtaleAt (f.fiberToSpecResidueField (f x)) (f.asFiber x),
      (f.stalkMap x).hom.Flat ∧
        UnramifiedAt (f.fiberToSpecResidueField (f x)) (f.asFiber x),
      (f.stalkMap x).hom.Flat ∧
        Subsingleton (relativeDifferentialStalk f x),
      (f.stalkMap x).hom.Flat ∧
        Subsingleton (fiberRelativeCotangentSpace f x),
      (f.stalkMap x).hom.Flat ∧
        Subsingleton (relativeCotangentSpace f x),
      (f.stalkMap x).hom.Flat ∧
        (Ideal.map (f.stalkMap x).hom
            (IsLocalRing.maximalIdeal (S.presheaf.stalk (f x))) =
          IsLocalRing.maximalIdeal (X.presheaf.stalk x) ∧
          (letI := (f.residueFieldMap x).hom.toAlgebra
           Module.Finite (S.residueField (f x)) (X.residueField x) ∧
             Algebra.IsSeparable (S.residueField (f x)) (X.residueField x))),
      ∃ (U : X.affineOpens) (V : S.affineOpens) (_ : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        letI : Algebra Γ(S, V.1) Γ(X, U.1) :=
          (f.appLE V U hUV).hom.toAlgebra
        Algebra.IsStandardSmoothOfRelativeDimension 0 Γ(S, V.1) Γ(X, U.1),
      ∃ (U : X.affineOpens) (V : S.affineOpens) (hxU : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        letI : Algebra Γ(S, V.1) Γ(X, U.1) :=
          (f.appLE V U hUV).hom.toAlgebra
        ∃ (n : ℕ) (P : Algebra.PreSubmersivePresentation
            Γ(S, V.1) Γ(X, U.1) (Fin n) (Fin n)),
          P.jacobian ∉ (U.2.primeIdealOf ⟨x, hxU⟩).asIdeal,
      ∃ (U : X.affineOpens) (V : S.affineOpens) (_ : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        IsStandardEtale (f.resLE V.1 U.1 hUV),
      ∃ (U : X.affineOpens) (V : S.affineOpens) (hxU : x ∈ U.1)
          (hUV : U.1 ≤ f ⁻¹ᵁ V.1)
          (p q : Γ(S, V.1)[X]),
        p.Monic ∧
          ∃ e : Γ(X, U.1) ≃+* StandardEtale.StandardEtaleAlg Γ(S, V.1) p q,
            e.toRingHom.comp (f.appLE V U hUV).hom =
              StandardEtale.standardEtaleMap Γ(S, V.1) p q ∧
            e.symm ((Ideal.Quotient.mk
              (Ideal.span {(algebraMap Γ(S, V.1)[X]
                (Localization.Away q)) p}))
              ((algebraMap Γ(S, V.1)[X] (Localization.Away q))
                (derivative p))) ∉
              (U.2.primeIdealOf ⟨x, hxU⟩).asIdeal]
```

## Tag 02GV, a lemma

[Tag 02GV](https://stacks.math.columbia.edu/tag/02GV) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_iff_isFlatAt_and_gUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/EtaleFlatUnramified.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/EtaleFlatUnramified.lean#L123). The attribute's comment: “at a point”. References: EGA IV (17.6.2), “more general”; SGA 3 XI (1.4), “more general”.

> A morphism of schemes is étale at a point if and only if it is flat and
> G-unramified at that point.

```lean
public theorem etaleAt_iff_isFlatAt_and_gUnramifiedAt {X S : Scheme.{u}}
    (f : X ⟶ S) (x : X) :
    EtaleAt f x ↔
      (IsFlatAt (LocallyRingedSpace.forgetToSheafedSpace.map f.toLRSHom) x ∧
        GUnramifiedAt f x)
```

**`AlgebraicGeometry.etale_iff_flat_and_gUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/EtaleFlatUnramified.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/EtaleFlatUnramified.lean#L132). The attribute's comment: “globally”. References: EGA IV (17.6.2); SGA 3 XI (1.4), “more general”.

> A morphism of schemes is étale if and only if it is flat and G-unramified.

```lean
public theorem etale_iff_flat_and_gUnramified {X S : Scheme.{u}} (f : X ⟶ S) :
    Etale f ↔ (Flat f ∧ GUnramified f)
```

## Tag 0476, a lemma

[Tag 0476](https://stacks.math.columbia.edu/tag/0476) in the Stacks Project.

**`AlgebraicGeometry.setOf_etaleAt_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocusBaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocusBaseChange.lean#L125). References: EGA IV (17.7.4), “(vi)”; EGA IV (17.7.1), “(ii) étale”.

> **Stacks Project, Tag 0476.** Let
> ```
> X' → X
> ↓    ↓
> S' → S
> ```
> be a cartesian diagram of schemes, and let `W ⊆ X`, respectively `W' ⊆ X'`, be the open
> subscheme of points where `f : X ⟶ S`, respectively the base-changed morphism `f' : X' ⟶ S'`, is
> étale. Then `W' = (g')⁻¹(W)` provided `f` is locally of finite presentation and, in addition,
> either `f` is flat — the source's case (1) — or `g : S' ⟶ S` is flat — the source's case (2).

```lean
theorem setOf_etaleAt_eq_preimage_of_isPullback {f : X ⟶ S} {g : S' ⟶ S} {f' : X' ⟶ S'}
    {g' : X' ⟶ X} [LocallyOfFinitePresentation f] (sq : IsPullback g' f' f g)
    (hflat : Flat f ∨ Flat g) :
    {x' : X' | EtaleAt f' x'} = g'.base ⁻¹' {x : X | EtaleAt f x}
```

## Tag 0HB1, a lemma

[Tag 0HB1](https://stacks.math.columbia.edu/tag/0HB1) in the Stacks Project.

**`AlgebraicGeometry.Etale.of_comp_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean#L89). The attribute's comment: “Lemma 29.37.18 (lemma-etale-permanence-better): with `g : Y ⟶ S` unramified and `f ≫ g : X ⟶ S` étale, the morphism `f` is étale.”.

> Let `f : X ⟶ Y` be a morphism of schemes over `S`, with structure morphism `g : Y ⟶ S`. If
> `X` is étale over `S` and `Y` is unramified over `S`, then `f` is étale. The proof factors `f`
> through the graph `X ⟶ X ×_S Y`, a base change of the diagonal of `g`, which is an open
> immersion since `g` is unramified (Tag 02GE).

```lean
theorem Etale.of_comp_of_unramified {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [Etale (f ≫ g)] [Unramified g] : Etale f
```

## Tag 02GW, a lemma

[Tag 02GW](https://stacks.math.columbia.edu/tag/02GW) in the Stacks Project.

**`AlgebraicGeometry.etale_of_etale_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Cancellation.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Cancellation.lean#L46). References: SGA 4 VII (1.2).

> **Stacks Project, Tag 02GW.** A morphism between two schemes that are étale over a common
> base, and which commutes with the structure morphisms, is étale.

```lean
theorem etale_of_etale_over {X Y S : Scheme.{u}} (f : X ⟶ Y) {p : X ⟶ S} {q : Y ⟶ S}
    (h : f ≫ q = p) [Etale p] [Etale q] : Etale f
```

## Tag 02K6, a lemma

[Tag 02K6](https://stacks.math.columbia.edu/tag/02K6) in the Stacks Project.

**`Stacks.Etale.etale_of_comp_surjective_etale_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Descent.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Descent.lean#L156).

> **Stacks Project, Tag 02K6.** If `f : X ⟶ Y` is surjective and étale, the composition
> `f ≫ q` is étale and `q : Y ⟶ S` is locally of finite presentation, then `q` is étale.

```lean
theorem etale_of_comp_surjective_etale_of_locallyOfFinitePresentation (f : X ⟶ Y) (q : Y ⟶ S)
    [Surjective f] [Etale f] [Etale (f ≫ q)] [LocallyOfFinitePresentation q] :
    Etale q
```

## Tag 054L, a lemma

[Tag 054L](https://stacks.math.columbia.edu/tag/054L) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_open_etale_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleAffineSpace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleAffineSpace.lean#L100). References: EGA IV (17.11.4), “smooth ⇒ étale/A^d”.

> A morphism of schemes which is smooth at a point is, over any affine open neighbourhood `V`
> of the image of that point, étale-locally an affine space over `V`: there is an affine open
> neighbourhood `U` of the point mapping into `V` and an étale morphism from `U` to an affine
> space over `V` commuting with the morphism.

```lean
theorem exists_affine_open_etale_affineSpace {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X)
    (V : Y.Opens) (hV : IsAffineOpen V) (hxV : x ∈ f ⁻¹ᵁ V)
    (hf : InfinitesimalLifting.SmoothAt f x) :
    ∃ (d : ℕ) (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U) (hUV : U ≤ f ⁻¹ᵁ V)
      (π : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) V.toScheme),
      Etale π ∧
        π ≫ (AffineSpace (ULift.{u} (Fin d)) V.toScheme ↘ V.toScheme) =
          f.resLE V U hUV
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.37, Tag 02GH](https://stacks.math.columbia.edu/tag/02GH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
