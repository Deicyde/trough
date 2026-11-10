---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Opens.IsSchemeTheoreticallyDense, AlgebraicGeometry.Scheme.Hom.image, Stacks.Morphisms.DenseNotTopologicallyDense.injective_localizationProduct, Stacks.Morphisms.DenseNotTopologicallyDense.schemeTheoreticImage_openInclusion, Stacks.Morphisms.DenseNotTopologicallyDense.surjective_xProjection, Stacks.Morphisms.DenseNotTopologicallyDense.xProjection_openComplement_avoids_xOpen, Stacks.Morphisms.DenseNotTopologicallyDense.not_surjective_xProjection_openComplement, Stacks.Morphisms.DenseNotTopologicallyDense.not_dense_openComplement
statement: formalized
proof: formalized
---

# 29.7 Scheme theoretic closure and density

Section 29.7 of the Stacks Project, [Tag 01RA](https://stacks.math.columbia.edu/tag/01RA). 10 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01RB, a definition

[Tag 01RB](https://stacks.math.columbia.edu/tag/01RB) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Opens.IsSchemeTheoreticallyDense`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean#L71). The attribute's comment: “part (2)”. References: SGA 3 IX (4.1), “single open subscheme”.

> An open subscheme `U` of `X` is scheme-theoretically dense if, for every open subscheme
> `V` of `X`, the scheme-theoretic image in `V` of `U ∩ V` is all of `V`.

```lean
abbrev IsSchemeTheoreticallyDense {X : Scheme.{u}} (U : X.Opens) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.image#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean#L54) (StacksFrontier): “part (1): the scheme-theoretic closure of an open subscheme”. References: EGA I (9.5.1); EGA I (9.5.2); EGA I (9.5.3); EGA IV (2.3.2).

## Tag 01RC, an example

[Tag 01RC](https://stacks.math.columbia.edu/tag/01RC) in the Stacks Project.

**`Stacks.Morphisms.DenseNotTopologicallyDense.injective_localizationProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L233). The attribute's comment: “localization injection”.

> The canonical map from `A` to the product of its localizations at the `zₙ` is
> injective.

```lean
public theorem injective_localizationProduct :
    Function.Injective (fun a : coordinateRing k =>
      fun n : ℕ => (algebraMap (coordinateRing k) (Localization.Away (z k n))) a)
```

**`Stacks.Morphisms.DenseNotTopologicallyDense.schemeTheoreticImage_openInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L374). The attribute's comment: “scheme-theoretic closure”.

> The scheme-theoretic closure of the open `U` is all of `X`.

```lean
public theorem schemeTheoreticImage_openInclusion :
    IsSchemeTheoreticallyDominant (openComplement k).ι
```

**`Stacks.Morphisms.DenseNotTopologicallyDense.surjective_xProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L390). The attribute's comment: “surjective projection”.

> The projection `X = Spec A → Spec k[x]` is surjective.

```lean
public theorem surjective_xProjection : Function.Surjective (xProjection k).base
```

**`Stacks.Morphisms.DenseNotTopologicallyDense.xProjection_openComplement_avoids_xOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L400). The attribute's comment: “restricted projection”.

> The image of `U` under the projection to `Spec k[x]` avoids the basic open `D(x)`.

```lean
public theorem xProjection_openComplement_avoids_xOpen :
    ∀ p : exampleScheme k, p ∈ (openComplement k : Set (exampleScheme k)) →
      (xProjection k).base p ∉
        (PrimeSpectrum.basicOpen (MvPolynomial.X () : xRing k) :
          Set (PrimeSpectrum (xRing k)))
```

**`Stacks.Morphisms.DenseNotTopologicallyDense.not_surjective_xProjection_openComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L430). The attribute's comment: “restricted projection not surjective”.

> The restriction of the projection to `Spec k[x]` to the open `U` is not surjective.

```lean
public theorem not_surjective_xProjection_openComplement :
    ¬ Set.SurjOn (xProjection k).base
      (openComplement k : Set (exampleScheme k))
      (Set.univ : Set (PrimeSpectrum (xRing k)))
```

**`Stacks.Morphisms.DenseNotTopologicallyDense.not_dense_openComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseNotTopologicallyDense.lean#L441). The attribute's comment: “not topologically dense”.

> Although its scheme-theoretic closure is all of `X`, the open `U` is not topologically
> dense in `X`.

```lean
public theorem not_dense_openComplement :
    ¬ Dense (openComplement k : Set (exampleScheme k))
```

## Tag 01RD, a lemma

[Tag 01RD](https://stacks.math.columbia.edu/tag/01RD) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Opens.isSchemeTheoreticallyDense_iff_isSchemeTheoreticallyDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean#L133).

> An open subscheme whose inclusion is quasi-compact is scheme-theoretically dense exactly
> when its scheme-theoretic closure is the whole scheme, that is, when its inclusion is
> scheme-theoretically dominant.

```lean
theorem isSchemeTheoreticallyDense_iff_isSchemeTheoreticallyDominant {X : Scheme.{u}}
    (U : X.Opens) [QuasiCompact U.ι] :
    IsSchemeTheoreticallyDense U ↔ IsSchemeTheoreticallyDominant U.ι
```

## Tag 056C, an example

[Tag 056C](https://stacks.math.columbia.edu/tag/056C) in the Stacks Project.

**`Stacks.Morphisms.schemeTheoreticImage_iso_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean#L187). The attribute's comment: “scheme-theoretic closure”.

> The scheme-theoretic closure of the finite union of standard opens is the
> closed subscheme `Spec (A/I)`, with its canonical map to `Spec A`.

```lean
public theorem schemeTheoreticImage_iso_quotient [Finite ι] (f : ι → A) :
    ∃ e : (standardOpenUnion f).ι.image ≅ Spec (.of (A ⧸ localizationKernel f)),
      (standardOpenUnion f).ι.imageι =
        e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (localizationKernel f)))
```

**`Stacks.Morphisms.quasiCompact_standardOpenUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean#L241). The attribute's comment: “quasi-compactness”.

> The inclusion of a finite union of standard opens is quasi-compact.

```lean
public theorem quasiCompact_standardOpenUnion [Finite ι] (f : ι → A) :
    QuasiCompact (standardOpenUnion f).ι
```

**`Stacks.Morphisms.schemeTheoreticallyDense_iff_localizationKernel_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Fibres/StandardOpenUnion.lean#L257). The attribute's comment: “scheme-theoretic density”.

> A finite union of standard opens is scheme-theoretically dense precisely
> when the canonical map to the product of localizations is injective.

```lean
public theorem schemeTheoreticallyDense_iff_localizationKernel_eq_bot [Finite ι]
    (f : ι → A) :
    AlgebraicGeometry.Scheme.Opens.IsSchemeTheoreticallyDense (standardOpenUnion f) ↔
      localizationKernel f = ⊥
```

## Tag 01RE, a lemma

[Tag 01RE](https://stacks.math.columbia.edu/tag/01RE) in the Stacks Project.

**`AlgebraicGeometry.isSchemeTheoreticallyDense_opensRange_iff_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseOpenImmersion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DenseOpenImmersion.lean#L181).

> An open immersion has scheme-theoretically dense image if and only if its structure-sheaf
> map is injective.

```lean
public theorem isSchemeTheoreticallyDense_opensRange_iff_mono
    {U X : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] :
    Scheme.Opens.IsSchemeTheoreticallyDense j.opensRange ↔ Mono j.c
```

## Tag 01RF, a lemma

[Tag 01RF](https://stacks.math.columbia.edu/tag/01RF) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Opens.isSchemeTheoreticallyDense_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean#L77).

> The intersection of scheme-theoretically dense open subschemes is
> scheme-theoretically dense.

```lean
theorem isSchemeTheoreticallyDense_inf {X : Scheme.{u}} (U V : X.Opens)
    (hU : IsSchemeTheoreticallyDense U)
    (hV : IsSchemeTheoreticallyDense V) :
    IsSchemeTheoreticallyDense (U ⊓ V)
```

## Tag 01RG, a lemma

[Tag 01RG](https://stacks.math.columbia.edu/tag/01RG) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_toImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean#L97). The attribute's comment: “open immersion”. References: EGA I (9.5.10), “Y open in closure”.

> An immersion which is quasi-compact, or has reduced source, is open in its
> scheme-theoretic image.

```lean
lemma isOpenImmersion_toImage {Z X : Scheme.{u}} (h : Z ⟶ X)
    [IsImmersion h] (hq_or_hr : QuasiCompact h ∨ IsReduced Z) :
    IsOpenImmersion h.toImage
```

**`AlgebraicGeometry.isSchemeTheoreticallyDense_toImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean#L107). The attribute's comment: “scheme-theoretic density”.

> The open subscheme corresponding to an immersion in its scheme-theoretic image is
> scheme-theoretically dense.

```lean
lemma isSchemeTheoreticallyDense_toImage {Z X : Scheme.{u}} (h : Z ⟶ X)
    [IsImmersion h] (hq_or_hr : QuasiCompact h ∨ IsReduced Z) :
    (letI : IsOpenImmersion h.toImage := isOpenImmersion_toImage h hq_or_hr
     Scheme.Opens.IsSchemeTheoreticallyDense h.toImage.opensRange)
```

**`AlgebraicGeometry.isDominant_toImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/ImmersionImage.lean#L138). The attribute's comment: “topological density”. References: EGA I (9.5.10), “topological density”.

> The image of an immersion is topologically dense in its scheme-theoretic image.

```lean
lemma isDominant_toImage {Z X : Scheme.{u}} (h : Z ⟶ X)
    [IsImmersion h] (hq_or_hr : QuasiCompact h ∨ IsReduced Z) :
    IsDominant h.toImage
```

## Tag 056D, a lemma

[Tag 056D](https://stacks.math.columbia.edu/tag/056D) in the Stacks Project.

**`AlgebraicGeometry.dense_open_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean#L66).

> For an open subscheme of a reduced scheme, topological density, having the whole scheme as
> scheme-theoretic closure, and scheme-theoretic density are equivalent.

```lean
theorem dense_open_tfae {X : Scheme.{u}} [IsReduced X]
    (U : X.Opens) :
    List.TFAE [
      Dense (U : Set X),
      IsIso U.ι.imageι,
      Scheme.Opens.IsSchemeTheoreticallyDense U]
```

## Tag 056E, a lemma

[Tag 056E](https://stacks.math.columbia.edu/tag/056E) in the Stacks Project.

**`AlgebraicGeometry.isSchemeTheoreticallyDominant_iff_isSchemeTheoreticallyDense`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean#L117). The attribute's comment: “equivalence”.

> For a reduced open subscheme, having scheme-theoretic closure equal to the ambient scheme is
> equivalent to being scheme-theoretically dense.

```lean
lemma isSchemeTheoreticallyDominant_iff_isSchemeTheoreticallyDense
    {X : Scheme.{u}} (U : X.Opens) [IsReduced U] :
    IsSchemeTheoreticallyDominant U.ι ↔ Scheme.Opens.IsSchemeTheoreticallyDense U
```

**`AlgebraicGeometry.isReduced_of_isSchemeTheoreticallyDense`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/SchemeTheoreticClosure.lean#L126). The attribute's comment: “reducedness”.

> A scheme with a reduced scheme-theoretically dense open subscheme is reduced.

```lean
lemma isReduced_of_isSchemeTheoreticallyDense
    {X : Scheme.{u}} (U : X.Opens) [IsReduced U]
    (hU : Scheme.Opens.IsSchemeTheoreticallyDense U) : IsReduced X
```

## Tag 01RH, a lemma

[Tag 01RH](https://stacks.math.columbia.edu/tag/01RH) in the Stacks Project.

**`AlgebraicGeometry.eq_of_isSchemeTheoreticallyDominant_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/SchemeTheoreticallyDense.lean#L146). The attribute's comment: “hypothesis: the scheme-theoretic closure of `U` in `X` is `X`, i.e. `U.ι` is scheme-theoretically dominant”.

> Let `X`, `Y` be schemes over `S` and let `f, g : X ⟶ Y` be morphisms over `S` which agree
> after restriction to an open subscheme `U ⊆ X`. If the scheme-theoretic closure of `U` in `X` is
> `X`, that is, `U.ι` is scheme-theoretically dominant, and `Y ⟶ S` is separated, then `f = g`.

```lean
theorem eq_of_isSchemeTheoreticallyDominant_ι {S : Scheme.{u}} {X Y : Over S}
    (f g : X ⟶ Y) (U : X.left.Opens) [IsSchemeTheoreticallyDominant U.ι]
    [IsSeparated Y.hom] (hfg : U.ι ≫ f.left = U.ι ≫ g.left) :
    f = g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.7, Tag 01RA](https://stacks.math.columbia.edu/tag/01RA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
