---
declaration: section
origin: cited
lean: AlgebraicGeometry.Etale.iff_smoothOfRelativeDimension_zero, AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_flat_and_fibers_etale, AlgebraicGeometry.etale_pullback_map, AlgebraicGeometry.etale_prod_map, AlgebraicGeometry.relativeDimension_zero_of_etale, AlgebraicGeometry.isRegular_of_etale, AlgebraicGeometry.etale_iff_iso_coproduct_spectra_finite_separable, AlgebraicGeometry.etale_of_etale_over
statement: formalized
proof: formalized
---

# 59.26 Étale morphisms

Section 59.26 of the Stacks Project, [Tag 03PA](https://stacks.math.columbia.edu/tag/03PA). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 13 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03PB, a definition

[Tag 03PB](https://stacks.math.columbia.edu/tag/03PB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale.iff_smoothOfRelativeDimension_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.iff_smoothOfRelativeDimension_zero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L157) (StacksFrontier): “Mathlib's étale morphisms are exactly the smooth morphisms of relative dimension 0”. References: SGA 1 II (1.3), “more general”.

## Tag 03PC, a proposition

[Tag 03PC](https://stacks.math.columbia.edu/tag/03PC) in the Stacks Project.

**`AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_flat_and_fibers_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L64). The attribute's comment: “flat_fibres”.

> **Stacks Project, Tag 03PC, part (2), (a) ⟺ (b).** A morphism of schemes is étale if and
> only if it is locally of finite presentation, flat, and all of its fibres are étale.

```lean
public theorem etale_iff_locallyOfFinitePresentation_and_flat_and_fibers_etale
    {X S : Scheme.{u}} (f : X ⟶ S) :
    Etale f ↔ LocallyOfFinitePresentation f ∧ Flat f ∧
      ∀ s : S, Etale (f.fiberToSpecResidueField s)
```

**`AlgebraicGeometry.etale_pullback_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L105). The attribute's comment: “fibre_product”.

> **Stacks Project, Tag 03PC, part (6), fibre products.** Let `i₁ : X ⟶ X'` and
> `i₂ : Y ⟶ Y'` be morphisms of schemes over a base `S`. If both are étale, then so is the
> induced morphism `X ×_S Y ⟶ X' ×_S Y'`.

```lean
public theorem etale_pullback_map {S X X' Y Y' : Scheme.{u}} {f : X ⟶ S} {g : Y ⟶ S}
    {f' : X' ⟶ S} {g' : Y' ⟶ S} {i₁ : X ⟶ X'} {i₂ : Y ⟶ Y'} [Etale i₁] [Etale i₂]
    (e₁ : f = i₁ ≫ f') (e₂ : g = i₂ ≫ g') :
    Etale (pullback.map f g f' g' i₁ i₂ (𝟙 S) ((Category.comp_id _).trans e₁)
      ((Category.comp_id _).trans e₂))
```

**`AlgebraicGeometry.etale_prod_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L131). The attribute's comment: “product”.

> **Stacks Project, Tag 03PC, part (6), products.** The product of two étale morphisms of
> schemes is étale.

```lean
public theorem etale_prod_map {X X' Y Y' : Scheme.{u}} (f : X ⟶ X') (g : Y ⟶ Y')
    [Etale f] [Etale g] : Etale (prod.map f g)
```

**`AlgebraicGeometry.relativeDimension_zero_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L144). The attribute's comment: “relative_dimension_zero”.

> **Stacks Project, Tag 03PC, part (7).** An étale morphism of schemes has relative
> dimension `0`: it is locally quasi-finite, and a locally quasi-finite morphism is exactly one
> of relative dimension `0`.

```lean
public theorem relativeDimension_zero_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] :
    RelativeDimension f 0
```

**`AlgebraicGeometry.isRegular_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L155). The attribute's comment: “regular”.

> **Stacks Project, Tag 03PC, part (8), the regular case.** The source of an étale morphism
> with regular target is regular, an étale morphism being smooth.

```lean
public theorem isRegular_of_etale {X Y : Scheme.{u}} (f : X ⟶ Y) [Etale f] (hY : IsRegular Y) :
    IsRegular X
```

**`AlgebraicGeometry.etale_iff_iso_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean#L75). The attribute's comment: “over_field”. References: EGA IV (17.6.2), “base = Spec k”; SGA 4½ Arcata (2.1.2), “a)”.

> **Stacks Project, Tag 03PC (over a field).** A morphism to the spectrum of a field is
> étale if and only if its source is, over that spectrum, a coproduct of spectra of finite
> separable field extensions.

```lean
public theorem etale_iff_iso_coproduct_spectra_finite_separable
    (k : Type u) [Field k] {U : Scheme.{u}} (f : U ⟶ Spec (.of k)) :
    Etale f ↔
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra k (K i)) (_ : ∀ i, Module.Finite k (K i))
        (_ : ∀ i, Algebra.IsSeparable k (K i))
        (e : U ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (K i)))) = f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.etale_of_etale_over`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Cancellation.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/CancellationOverBase.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/CancellationOverBase.lean#L19) (StacksFrontier): “morphism_over_base”.
- [`AlgebraicGeometry.etale_iff_flat_and_locallyOfFinitePresentation_and_unramified`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean#L49), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L77) (StacksFrontier): “flat_unramified_finite_presentation”.
- [`AlgebraicGeometry.Etale.etale_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L82) (StacksFrontier): “base_change”. References: EGA IV (17.3.3), “(iii), étale case”; EGA IV (17.7.3), “(ii)”; SGA 1 I (4.6); SGA 1 IX (1.3); SGA 1 IX (4.2), “Étaleness of X₁' → S₁'”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (2.1.2), “partial”; SGA 3 VIIB (1.6.C), “special case”; SGA 4 VII (1.4), “partial”; SGA 4½ Arcata (2.1.3).
- [`AlgebraicGeometry.Etale.etale_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L93) (StacksFrontier): “composition”. References: EGA IV (17.3.3), “(ii), étale case”; EGA IV (17.3.5), “étale clause”; SGA 1 I (4.6); SGA 1 V (3.3), “special case”.
- [`AlgebraicGeometry.isReduced_of_etale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L225), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Facts.lean#L150) (StacksFrontier): “reduced”.
- [`AlgebraicGeometry.UniversallyOpen.of_flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.of_flat#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean#L61) (StacksFrontier): “open”. References: EGA IV (1.10.4), “b) ⇒ a), special case”; EGA IV (11.3.1), “special case”; EGA IV (14.4.10), “special case”; EGA IV (15.2.1); EGA IV (15.2.4), “(ii), special case”; EGA IV (18.2.7), “partial”; EGA IV (2.4.6); EGA IV (2.4.7), “more general”; EGA IV (4.4.1), “special case”; SGA 1 IV (6.6), “F = O_X”; SGA 1 VIII (4.9), “more general”; SGA 3 V (10.1.1), “more general”; SGA 3 V (4.1.1), “flat and fp implies open”; SGA 3 VIA (2.5.4), “Final implication”; SGA 3 VIB (3.11), “more general”; SGA 3 VIB (4.3); SGA 3 VIB (7.5), “f|_V is an open morphism”; SGA 3 X (5.4), “partial”; SGA 3 XVI (2.1), “more general”; SGA 6 VIII (1.3), “more general”.
- [`AlgebraicGeometry.Scheme.Hom.isOpenMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.isOpenMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Open.lean#L62) (StacksFrontier): “open”.
- [`Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L212) (StacksFrontier): “jacobian”. References: SGA 1 II (1.3), “clause (i), special case”.
- [`Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/StandardSmoothJacobian.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/StandardSmoothJacobian.lean#L30) (StacksFrontier): “jacobian”. References: SGA 1 II (1.3), “clause (i), special case”.

## Tag 03PD, a definition

[Tag 03PD](https://stacks.math.columbia.edu/tag/03PD) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.IsStandardEtale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsStandardEtale#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L159) (StacksFrontier): “B is standard étale over A: B ≅ (A[t]/(f))_g with f monic and df/dt invertible in B”.

## Tag 03PE, a theorem

[Tag 03PE](https://stacks.math.columbia.edu/tag/03PE) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.exists_isStandardEtale_of_exists_etale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L149), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleMorphisms/Basic.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleMorphisms/Basic.lean#L30) (StacksFrontier): “étale at a prime implies locally standard étale”.
- [`Algebra.instEtaleOfIsStandardEtale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.instEtaleOfIsStandardEtale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleMorphisms/Basic.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleMorphisms/Basic.lean#L33) (StacksFrontier): “standard étale implies étale”. References: SGA 4½ Arcata (2.1.1), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.26, Tag 03PA](https://stacks.math.columbia.edu/tag/03PA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
