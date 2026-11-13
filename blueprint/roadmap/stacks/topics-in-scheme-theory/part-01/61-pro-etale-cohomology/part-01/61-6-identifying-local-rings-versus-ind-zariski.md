---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exists_surjective_indZariski_range_comap_eq_preimage_components, AlgebraicGeometry.ProEtale.exists_indZariski_of_profinite_component_map, AlgebraicGeometry.ProEtale.isIndZariski_locallyConstant, AlgebraicGeometry.ProEtale.primeSpectrum_locallyConstant_homeomorph, AlgebraicGeometry.ProEtale.isColimit_functionRingCocone, AlgebraicGeometry.ProEtale.bijective_of_wLocalMap_identifiesLocalRings, AlgebraicGeometry.ProEtale.isIndZariski_of_wLocalMap_identifiesLocalRings, AlgebraicGeometry.ProEtale.exists_faithfullyFlat_indZariski_extension
statement: formalized
proof: formalized
---

# 61.6 Identifying local rings versus ind-Zariski

Section 61.6 of the Stacks Project, [Tag 097B](https://stacks.math.columbia.edu/tag/097B). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 097C, a lemma

[Tag 097C](https://stacks.math.columbia.edu/tag/097C) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_surjective_indZariski_range_comap_eq_preimage_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/ComponentRestriction.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/ComponentRestriction.lean#L216).

> **Stacks Project, Tag 097C.** A closed union of connected components of an affine spectrum
> is the spectrum of a surjective ind-Zariski algebra, homeomorphic to that union via
> contraction.

```lean
theorem exists_surjective_indZariski_range_comap_eq_preimage_components
    (A : Type u) [CommRing A]
    (T : Set (ConnectedComponents (PrimeSpectrum A))) (hT : IsClosed T) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      IsIndZariski.{u, u, u} A B ∧
      Function.Surjective (algebraMap A B) ∧
      IsEmbedding (PrimeSpectrum.comap (algebraMap A B)) ∧
      Set.range (PrimeSpectrum.comap (algebraMap A B)) =
        ((↑) : PrimeSpectrum A → ConnectedComponents (PrimeSpectrum A)) ⁻¹' T
```

## Tag 097D, a lemma

[Tag 097D](https://stacks.math.columbia.edu/tag/097D) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_indZariski_of_profinite_component_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/ProfiniteComponentRealization.lean, line 1758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/ProfiniteComponentRealization.lean#L1758).

> **Stacks Project, Tag 097D.** A profinite space over the connected components of an affine
> spectrum is realized by the spectrum of an ind-Zariski algebra, with its canonical component
> space and cartesian square.

```lean
theorem exists_indZariski_of_profinite_component_map
    (A : Type u) [CommRing A] (T : Type v) [TopologicalSpace T]
    (hT : IsProfiniteStacks T)
    (f : C(T, ConnectedComponents (PrimeSpectrum A))) :
    ∃ (B : Type (max u v)) (_ : CommRing B) (_ : Algebra A B),
      IsIndZariski.{u, max u v, max u v} A B ∧
      ∃ g : C(PrimeSpectrum B, T),
      ∃ e : ConnectedComponents (PrimeSpectrum B) ≃ₜ T,
        (∀ p : PrimeSpectrum B, e (ConnectedComponents.mk p) = g p) ∧
        IsPullback
          (TopCat.ofHom (⟨fun p => ULift.up (PrimeSpectrum.comap (algebraMap A B) p),
            continuous_uliftUp.comp (PrimeSpectrum.continuous_comap (algebraMap A B))⟩ :
              C(PrimeSpectrum B, ULift.{v} (PrimeSpectrum A))))
          (TopCat.ofHom (⟨fun p => ULift.up (g p), continuous_uliftUp.comp g.continuous⟩ :
            C(PrimeSpectrum B, ULift.{u} T)))
          (TopCat.ofHom (⟨fun p => ULift.up (ConnectedComponents.mk p.down),
            continuous_uliftUp.comp
              (ConnectedComponents.continuous_coe.comp continuous_uliftDown)⟩ :
                C(ULift.{v} (PrimeSpectrum A),
                  ULift.{v} (ConnectedComponents (PrimeSpectrum A)))))
          (TopCat.ofHom (⟨fun t => ULift.up (f t.down),
            continuous_uliftUp.comp (f.continuous.comp continuous_uliftDown)⟩ :
              C(ULift.{u} T, ULift.{v} (ConnectedComponents (PrimeSpectrum A)))))
```

## Tag 09BJ, an example

[Tag 09BJ](https://stacks.math.columbia.edu/tag/09BJ) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isIndZariski_locallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean#L336). The attribute's comment: “ind-Zariski algebra”.

> **Stacks Project, Tag 09BJ.** Locally constant functions on a profinite space form an
> ind-Zariski algebra over a field.

```lean
theorem isIndZariski_locallyConstant
    (k : Type u) [Field k] (T : Type v) [TopologicalSpace T]
    (hT : IsProfiniteStacks T) :
    IsIndZariski.{u, max u v, max u v} k (LocallyConstant T k)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_locallyConstant_homeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean#L440). The attribute's comment: “spectrum”.

> **Stacks Project, Tag 09BJ.** The spectrum of the ring of locally constant functions on a
> profinite space is homeomorphic to that space.

```lean
theorem primeSpectrum_locallyConstant_homeomorph
    (k : Type u) [Field k] (T : Type v) [TopologicalSpace T]
    (hT : IsProfiniteStacks T) :
    Nonempty (PrimeSpectrum (LocallyConstant T k) ≃ₜ T)
```

**`AlgebraicGeometry.ProEtale.isColimit_functionRingCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocallyConstantFunctions.lean#L510). The attribute's comment: “filtered colimit of finite-stage function rings”.

> **Stacks Project, Tag 09BJ.** For any presentation of a space as a limit of finite discrete
> spaces, its ring of locally constant functions is the colimit of the finite-stage function
> rings.

```lean
theorem isColimit_functionRingCocone
    (k : Type u) [Field k] {J : Type w} [SmallCategory J] [IsCofiltered J]
    (F : J ⥤ TopCat.{v}) (c : Cone F)
    (hc : IsLimit c)
    (hfinite : ∀ j, Finite (F.obj j) ∧ DiscreteTopology (F.obj j)) :
    Nonempty (IsColimit (functionRingCocone k c))
```

## Tag 097E, a lemma

[Tag 097E](https://stacks.math.columbia.edu/tag/097E) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bijective_of_wLocalMap_identifiesLocalRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/IdentifiesLocalRingsIso.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/IdentifiesLocalRingsIso.lean#L265).

> A ring map whose map of spectra is a w-local map of w-local spaces, which identifies all
> local rings and bijects connected components, is bijective.

```lean
theorem bijective_of_wLocalMap_identifiesLocalRings
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [WLocalSpace (PrimeSpectrum A)]
    [WLocalSpace (PrimeSpectrum B)]
    (hlocal : Algebra.IdentifiesLocalRings A B)
    (hwlocal : IsWLocalMap (PrimeSpectrum.comap (algebraMap A B)))
    (hcomponents : Function.Bijective
      (PrimeSpectrum.continuous_comap (algebraMap A B)).connectedComponentsMap) :
    Function.Bijective (algebraMap A B)
```

## Tag 097F, a lemma

[Tag 097F](https://stacks.math.columbia.edu/tag/097F) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isIndZariski_of_wLocalMap_identifiesLocalRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/IdentifiesLocalRingsIndZariski.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/IdentifiesLocalRingsIndZariski.lean#L125).

> A w-local morphism between w-local affine spectra that identifies local rings
> is ind-Zariski.

```lean
theorem isIndZariski_of_wLocalMap_identifiesLocalRings
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [WLocalSpace (PrimeSpectrum A)]
    [WLocalSpace (PrimeSpectrum B)]
    (hlocal : Algebra.IdentifiesLocalRings A B)
    (hwlocal : IsWLocalMap (PrimeSpectrum.comap (algebraMap A B))) :
    IsIndZariski.{u, v, max u v} A B
```

## Tag 097G, a proposition

[Tag 097G](https://stacks.math.columbia.edu/tag/097G) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_faithfullyFlat_indZariski_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/FaithfullyFlatExtension.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/FaithfullyFlatExtension.lean#L48).

> A map identifying local rings becomes ind-Zariski after a faithfully flat
> ind-Zariski extension of its target.

```lean
theorem exists_faithfullyFlat_indZariski_extension
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] (f : A →+* B)
    (hf : letI := f.toAlgebra; Algebra.IdentifiesLocalRings A B) :
    ∃ (B' : Type v) (_ : CommRing B') (g : B →+* B'),
      g.FaithfullyFlat ∧
        (letI := g.toAlgebra; IsIndZariski.{v, v, max u v} B B') ∧
        (letI := (g.comp f).toAlgebra;
          IsIndZariski.{u, v, max u v} A B')
```

## Tag 09AZ, a lemma

[Tag 09AZ](https://stacks.math.columbia.edu/tag/09AZ) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.wLocal_extremallyDisconnected_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/RetractionCharacterization.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/RetractionCharacterization.lean#L293).

> For a commutative ring `A` the following are equivalent: every faithfully
> flat `A`-algebra identifying local rings admits a retraction; every faithfully flat ind-Zariski
> `A`-algebra admits a retraction; `Spec A` is w-local and `π₀(Spec A)` is extremally
> disconnected.

```lean
theorem wLocal_extremallyDisconnected_tfae (A : Type u) [CommRing A] :
    List.TFAE
      [∀ (B : Type (max u v)) [CommRing B] [Algebra A B],
          Module.FaithfullyFlat A B → Algebra.IdentifiesLocalRings A B → Nonempty (B →ₐ[A] A),
        ∀ (B : Type (max u v)) [CommRing B] [Algebra A B],
          Module.FaithfullyFlat A B →
            IsIndZariski.{u, max u v, max u v} A B → Nonempty (B →ₐ[A] A),
        WLocalSpace (PrimeSpectrum A) ∧
          ExtremallyDisconnected (ConnectedComponents (PrimeSpectrum A))]
```

## Tag 09B0, a lemma

[Tag 09B0](https://stacks.math.columbia.edu/tag/09B0) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_faithfullyFlat_indZariski_wLocal_extremallyDisconnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WLocalIndZariskiCover.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WLocalIndZariskiCover.lean#L65).

> **Stacks 09B0.** Every ring has a faithfully flat ind-Zariski extension whose spectrum is
> w-local and whose space of connected components is extremally disconnected.

```lean
theorem exists_faithfullyFlat_indZariski_wLocal_extremallyDisconnected (A : Type u) [CommRing A] :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      (algebraMap A B).FaithfullyFlat ∧
        IsIndZariski.{u, u, u} A B ∧
          WLocalSpace (PrimeSpectrum B) ∧
            ExtremallyDisconnected (ConnectedComponents (PrimeSpectrum B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.6, Tag 097B](https://stacks.math.columbia.edu/tag/097B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
