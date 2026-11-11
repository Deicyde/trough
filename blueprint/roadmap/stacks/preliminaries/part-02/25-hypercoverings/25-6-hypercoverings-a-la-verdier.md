---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.HypercoveringOf, Stacks.CategoryTheory.Hypercovering.HypercoveringOfTerminal, Stacks.CategoryTheory.Hypercovering.nonempty_cechCohomologyZeroIso, Stacks.CategoryTheory.Hypercovering.cechCohomology_isZero_of_injective, Stacks.CategoryTheory.Hypercovering.cechCohomologyIsoOfInjective, Stacks.CategoryTheory.Hypercovering.exists_hypercoverPresheafToDerivedSections, Stacks.CategoryTheory.Hypercovering.exists_presheafCechCohomologyToCohomology, Stacks.CategoryTheory.Hypercovering.presheafHypercoveringSpectralSequenceFunctoriality
statement: formalized
proof: formalized
---

# 25.6 Hypercoverings a la Verdier

Section 25.6 of the Stacks Project, [Tag 09VT](https://stacks.math.columbia.edu/tag/09VT). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09VU, a definition

[Tag 09VU](https://stacks.math.columbia.edu/tag/09VU) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.HypercoveringOf`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Presheaf.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Presheaf.lean#L201). The attribute's comment: “hypercovering of a presheaf”. References: SGA 4 V (7.3.1.2); SGA 4 V (7.3.1.3), “a)”.

> A hypercovering of a presheaf of sets.

```lean
structure HypercoveringOf (J : Pretopology C) (G : Cᵒᵖ ⥤ Type q)
```

**`Stacks.CategoryTheory.Hypercovering.HypercoveringOfTerminal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Presheaf.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Presheaf.lean#L226). The attribute's comment: “hypercovering of the final presheaf”. References: SGA 4 V (7.3.1.2); SGA 4 V (7.3.1.3), “a)”.

> A hypercovering is a hypercovering of the final presheaf.

```lean
abbrev HypercoveringOfTerminal (J : Pretopology C)
```

## Tag 09VV, a lemma

[Tag 09VV](https://stacks.math.columbia.edu/tag/09VV) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.nonempty_cechCohomologyZeroIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cohomology.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cohomology.lean#L527).

> **Stacks Project, Tag 09VV.** Degree-zero Čech cohomology of a hypercovering of a presheaf is
> the degree-zero cohomology of that presheaf with coefficients in the given sheaf of abelian
> groups.
>
> The source asserts an identification; the isomorphism realising it is `cechCohomologyZeroIso`,
> of which this is the existence statement.

```lean
theorem nonempty_cechCohomologyZeroIso (J : Pretopology C)
    (G : Functor Cᵒᵖ (Type q)) (K : HypercoveringOf.{q, w} J G)
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)}) :
    Nonempty (cechCohomology J G K F 0 ≅ presheafCohomologyZero J G F)
```

## Tag 09VW, a lemma

[Tag 09VW](https://stacks.math.columbia.edu/tag/09VW) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.cechCohomology_isZero_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Injectives.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Injectives.lean#L362). The attribute's comment: “positive degrees”.

> **Stacks Project, Tag 09VW (positive degrees).** Positive-degree Čech cohomology of an
> injective abelian sheaf on a hypercovering of a presheaf vanishes.

```lean
theorem cechCohomology_isZero_of_injective (J : Pretopology C)
    (G : Cᵒᵖ ⥤ Type q) (K : HypercoveringOf.{q, w} J G)
    (I : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)})
    [Injective I] (p : ℕ) (hp : 0 < p) :
    IsZero (cechCohomology.{q, w, v, u} J G K I p)
```

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyIsoOfInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Injectives.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Injectives.lean#L423).

> **Stacks Project, Tag 09VW.** For a hypercovering `K` of a presheaf `G` and an injective
> abelian sheaf `I`, the Čech cohomology `Ȟᵖ(K, I)` is the degree-zero cohomology `H⁰(G, I)` of `G`
> when `p = 0` and is zero when `p > 0`.
>
> The degree-zero branch is Tag 09VV's `cechCohomologyZeroIso`, which holds for every abelian sheaf
> and needs no injectivity; the positive-degree branch is `cechCohomology_isZero_of_injective`.

```lean
noncomputable def cechCohomologyIsoOfInjective (J : Pretopology C)
    (G : Cᵒᵖ ⥤ Type q) (K : HypercoveringOf.{q, w} J G)
    (I : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)})
    [Injective I] (p : ℕ) :
    cechCohomology.{q, w, v, u} J G K I p ≅
      if p = 0 then presheafCohomologyZero.{q, w, v, u} J G I else 0
```

## Tag 09VX, a lemma

[Tag 09VX](https://stacks.math.columbia.edu/tag/09VX) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercoverPresheafToDerivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafCohomologyComparison.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafCohomologyComparison.lean#L162). The attribute's comment: “the comparison map s(F(K)) ⟶ RΓ(G, F) in D⁺(Ab), functorial in F”.

> For a hypercovering `K` of a presheaf `G` on a site with equalizers and fibre products there
> are a canonical map `ψ` from the sections over `G` to derived sections at the single complex, and
> a map
>
> `α : s(-(K)) ⟶ RΓ(G, -)`
>
> in `D⁺(Ab)`, functorial in the abelian sheaf, compatible with the augmentation of `s(-(K))` by the
> sections over `G`; and both are isomorphisms at every injective sheaf.

```lean
theorem exists_hypercoverPresheafToDerivedSections :
    ∃ (ψ : (presheafSectionsFunctor.{q, w, v, u} J G K ⋙
          singlePlus AddCommGrpCat.{max (max u v) (max q w)}) ⋙ DerivedCategory.Plus.Q ⟶
        presheafDerivedSectionsFunctor.{q, w, v, u} J G K)
      (α : hypercoverPresheafDerivedFunctor.{q, w, v, u} J G K ⟶
        presheafDerivedSectionsFunctor.{q, w, v, u} J G K),
      Functor.whiskerRight
            (epsNat (presheafSectionsFunctor.{q, w, v, u} J G K)
              (SemiRepresentable.sectionsComplexIntFunctor.{q, w, v, u} J.toGrothendieck
                K.toSimplicialObject)
              ((hypercoverPresheafAugmentation.{q, w, v, u} J G K).app)
              (fun {_ _} φ ↦ (hypercoverPresheafAugmentation.{q, w, v, u} J G K).naturality φ)
              (SemiRepresentable.isZero_sectionsComplexIntFunctor_obj_X.{q, w, v, u}
                J.toGrothendieck K.toSimplicialObject))
            DerivedCategory.Plus.Q ≫ α = ψ ∧
        (∀ F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)},
          Injective F → IsIso (ψ.app F)) ∧
        ∀ F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)},
          Injective F → IsIso (α.app F)
```

**`Stacks.CategoryTheory.Hypercovering.exists_presheafCechCohomologyToCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafCohomologyComparison.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafCohomologyComparison.lean#L220). The attribute's comment: “the induced natural transformations Ȟ^i(K, -) ⟶ H^i(G, -)”.

> The comparison map of `exists_hypercoverPresheafToDerivedSections` induces, in every degree
> `i`, a natural transformation
>
> `Ȟ^i(K, -) ⟶ H^i(G, -)`
>
> of functors from abelian sheaves to abelian groups, and these are isomorphisms at every injective
> sheaf.
>
> The source is the `i`-th cohomology of the complex `s(-(K))` itself, i.e. the Čech cohomology of
> the hypercovering, and the target is the `i`-th cohomology of `RΓ(G, -)`.

```lean
theorem exists_presheafCechCohomologyToCohomology :
    ∃ β : ∀ i : ℤ,
        (SemiRepresentable.sectionsComplexIntFunctor.{q, w, v, u} J.toGrothendieck
              K.toSimplicialObject ⋙
            HomologicalComplex.homologyFunctor AddCommGrpCat.{max (max u v) (max q w)}
              (ComplexShape.up ℤ) i) ⟶
          (presheafDerivedSectionsFunctor.{q, w, v, u} J G K ⋙
            DerivedCategory.Plus.homologyFunctor
              AddCommGrpCat.{max (max u v) (max q w)} i),
      ∀ (i : ℤ) (F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max q w)}),
        Injective F → IsIso ((β i).app F)
```

**`Stacks.CategoryTheory.Hypercovering.presheafHypercoveringSpectralSequenceFunctoriality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafSpectralSequence/Functoriality.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafSpectralSequence/Functoriality.lean#L280). The attribute's comment: “spectral sequence functorial in the hypercovering”.

> **The spectral sequence of [Stacks, Tag 09VX] is functorial in the hypercovering**: the data
> `PresheafHypercoveringSpectralSequenceFunctoriality`, supplied by
> `hypercoverPresheafSpectralSequenceFunctorMap` and its two laws.

```lean
def presheafHypercoveringSpectralSequenceFunctoriality :
    PresheafHypercoveringSpectralSequenceFunctoriality.{q, w, v, u} J G
```

**`Stacks.CategoryTheory.Hypercovering.presheafHypercoveringSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafSpectralSequence/Functoriality.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/PresheafSpectralSequence/Functoriality.lean#L332). The attribute's comment: “spectral sequence”. References: SGA 4 V (7.4.0), “(7.4.0.3)”.

> **The functorial spectral sequence of a hypercovering of a presheaf**, with second page
> `Ȟ^p(K, H̲^{q'}(F))` and abutment `H^{p+q'}(G, F)`.
>
> This is the spectral sequence clause of [Stacks, Tag 09VX]: the three fields are
> `hypercoverPresheafSpectralSequenceFunctor`, `hypercoverPresheafPageTwoIso` and
> `hypercoverPresheafAbutment`.  The functoriality of this spectral sequence in the hypercovering,
> which is the last sentence of that clause, is
> `presheafHypercoveringSpectralSequenceFunctoriality`, whose `map` is a morphism between the
> `sequence` fields of two hypercoverings.

```lean
def presheafHypercoveringSpectralSequence :
    PresheafHypercoveringSpectralSequenceData J G K
```

## Tag 09VY, a lemma

[Tag 09VY](https://stacks.math.columbia.edu/tag/09VY) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.hypercoveringGlobalSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalCohomologySpectralSequence.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalCohomologySpectralSequence.lean#L245). References: SGA 4 V (7.4.0), “(7.4.0.3)”; SGA 4 V (3.6), “more general”.

> **Stacks Project, Tag 09VY.**  For a hypercovering `K` of the final presheaf on a site with
> equalizers and fibre products there is a spectral sequence, functorial in the sheaf of abelian
> groups `F`, with second page `E_2^{p,q} = Ȟ^p(K, H̲^q(F))` converging to the global cohomology
> groups `H^{p+q}(F)`.
>
> It is [Stacks, Tag 09VX] at the final presheaf, with its abutment transported along
> `globalCohomologyAbutmentIso`.

```lean
def hypercoveringGlobalSpectralSequence :
    HypercoveringGlobalSpectralSequenceData J K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.6, Tag 09VT](https://stacks.math.columbia.edu/tag/09VT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
