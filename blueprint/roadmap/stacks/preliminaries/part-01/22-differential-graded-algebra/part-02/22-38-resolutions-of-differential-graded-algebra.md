---
declaration: section
origin: cited
lean: Stacks.DGA.exists_kFlat_freeGraded_resolution, DifferentialGradedAlgebra.exists_kFlat_resolution_bijective_cohomologyMap, DifferentialGradedAlgebra.exists_kFlat_resolution_derivedEquivalence, DifferentialGraded.Bimodule.exists_derivedTensorFunctorCompIso, DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_of_dgaResolutionRepresents, DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIsoOfKFlatBase, DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIso, DifferentialGradedModule.countable_cohomology_of_isHomotopyColimit_of_isCompactObject
statement: formalized
proof: formalized
---

# 22.38 Resolutions of differential graded algebras

Section 22.38 of the Stacks Project, [Tag 0BZ6](https://stacks.math.columbia.edu/tag/0BZ6). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BZ7, a lemma

[Tag 0BZ7](https://stacks.math.columbia.edu/tag/0BZ7) in the Stacks Project.

**`Stacks.DGA.exists_kFlat_freeGraded_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/FreeResolution/KFlatResolution.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/FreeResolution/KFlatResolution.lean#L749).

> Every differential graded algebra has a quasi-isomorphic K-flat resolution
> which is free as a graded algebra.

```lean
public theorem exists_kFlat_freeGraded_resolution
    (B : DifferentialGradedAlgebra.{u, max u v} R) :
    ∃ (A : DifferentialGradedAlgebra.{u, max u v} R)
      (f : A.A →ₐ[R] B.A)
      (CA CB : CochainComplex (ModuleCat.{max u v} R) ℤ)
      (eA : ModelsComplex A CA) (eB : ModelsComplex B CB)
      (g : CA ⟶ CB),
      IsFreeGradedAlgebra A ∧
        CA.KFlat ∧
      IsDGAMorphism A B f ∧
        (∀ (n : ℤ) (x : CA.X n),
          (eB.equiv n (g.f n x)).1 = f ((eA.equiv n x).1)) ∧
        QuasiIso g
```

**`DifferentialGradedAlgebra.exists_kFlat_resolution_bijective_cohomologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionDerivedEquivalence.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionDerivedEquivalence.lean#L297). The attribute's comment: “the resolution read as a homomorphism of differential graded algebras which is K-flat over the base and bijective on cohomology in every degree, which is the hypothesis of Tag 09S6”.

> **Stacks Tag 0BZ7, in the encoding Tag 09S6 consumes.** Every differential graded
> `R`-algebra `(B, d)` admits a homomorphism `φ : (B', d) → (B, d)` of differential graded algebras
> with `(B', d)` K-flat as a complex of `R`-modules and with `H^k(φ)` bijective for every `k`, i.e.
> `φ` an isomorphism on cohomology algebras.
>
> This is `Stacks.DGA.exists_kFlat_freeGraded_resolution` with its raw encoding converted: the
> `Stacks.DGA.IsDGAMorphism` bundled by `DifferentialGradedAlgebra.Hom.ofIsDGAMorphism`, the
> modelling complexes removed and their K-flatness transported to the canonical complex `B'^•` by
> `Stacks.DGA.ModelsComplex.kFlat_regularModule`, and the quasi-isomorphism of complexes turned
> into bijectivity on cohomology by
> `DifferentialGradedAlgebra.Hom.bijective_cohomologyMap_of_quasiIso`. Freeness of `B'` as a graded
> algebra, which Tag 0BZ7 also provides, is dropped: the reduction of Tag 0BZ8 to a K-flat middle
> algebra uses only K-flatness.

```lean
theorem exists_kFlat_resolution_bijective_cohomologyMap (B : DifferentialGradedAlgebra.{u, u} R) :
    ∃ (B' : DifferentialGradedAlgebra.{u, u} R) (φ : B'.Hom B),
      CochainComplex.KFlat.{u, u} (regularModule B').toCochainComplex ∧
        ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)
```

**`DifferentialGradedAlgebra.exists_kFlat_resolution_derivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionDerivedEquivalence.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionDerivedEquivalence.lean#L319). The attribute's comment: “the resolution together with the derived equivalence of Tag 09S6 it gives”.

> **The derived equivalence attached to the K-flat resolution of a differential graded
> algebra.** Every differential graded `R`-algebra `(B, d)` is the target of a homomorphism
> `φ : (B', d) → (B, d)` with `(B', d)` K-flat as a complex of `R`-modules along which extension of
> scalars `- ⊗_{B'}^𝐋 B : D(B', d) → D(B, d)` is an equivalence of categories, with derived
> restriction of scalars as quasi-inverse
> (`DifferentialGraded.Bimodule.derivedExtensionEquivalence`).
>
> This is Tag 0BZ7 followed by Tag 09S6, and it is the first ingredient of the reduction of
> Tag 0BZ8 to a K-flat middle algebra; the second is the transport of the conclusion of Tag 0BZ8
> through the three composites `D(A) → D(B) → D(B')`, `D(B') → D(B) → D(C)` and
> `D(A) → D(B') → D(C)`.

```lean
theorem exists_kFlat_resolution_derivedEquivalence (B : DifferentialGradedAlgebra.{u, u} R) :
    ∃ (B' : DifferentialGradedAlgebra.{u, u} R) (φ : B'.Hom B),
      CochainComplex.KFlat.{u, u} (regularModule B').toCochainComplex ∧
        (DifferentialGraded.Bimodule.derivedTensorFunctor
          (DifferentialGraded.Bimodule.regular φ)).IsEquivalence
```

## Tag 0BZ8, a lemma

[Tag 0BZ8](https://stacks.math.columbia.edu/tag/0BZ8) in the Stacks Project.

**`DifferentialGraded.Bimodule.exists_derivedTensorFunctorCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionGeneralBase.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionGeneralBase.lean#L190). The attribute's comment: “the composition of the two derived tensor functors is a derived tensor functor, with no hypothesis on the middle algebra”.

> **Stacks Tag 0BZ8.** *"Let `R` be a ring. Let `(A, d)`, `(B, d)`, and `(C, d)` be differential
> graded `R`-algebras. Assume that `A ⊗_R C` represents `A ⊗^𝐋_R C` in `D(R)`. Let `N` be a
> differential graded `(A, B)`-bimodule. Let `N'` be a differential graded `(B, C)`-bimodule. Then
> the composition `D(A, d) → D(B, d) → D(C, d)` of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'` is isomorphic to
> `- ⊗_A^𝐋 N''` for some differential graded `(A, C)`-bimodule `N''`."*
>
> Representability is the only hypothesis: there is none on `B`. The bimodule is produced
> explicitly by `DifferentialGraded.Bimodule.resolutionCompTensorBimodule`, from the K-flat
> resolution `ψ : (B', d) → (B, d)` of Tag 0BZ7 that
> `DifferentialGradedAlgebra.exists_kFlat_resolution_bijective_cohomologyMap` supplies; the
> isomorphism is
> `DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIsoOfResolution`. For a `B`
> that is already K-flat the bimodule can be taken to be `compTensorResolution N N'`, the bimodule
> of Tag 0BZ5, by
> `DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIsoOfKFlatBase`.

```lean
theorem exists_derivedTensorFunctorCompIso {A B C : DifferentialGradedAlgebra.{u, u} R}
    (hrep : DgaResolutionRepresentsDerivedTensor A C)
    (N : Bimodule A B) (N' : Bimodule B C) :
    ∃ N'' : Bimodule A C,
      Nonempty (derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
        derivedTensorFunctor N'')
```

**`DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_of_dgaResolutionRepresents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionKFlatBase.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionKFlatBase.lean#L135). The attribute's comment: “the second half of the proof: for B K-flat as a complex of R-modules, representability of A ⊗^L\_R C by A ⊗\_R C makes the map (0BZ4) an isomorphism”.

> **The second half of the proof of Stacks Tag 0BZ8.** If the differential graded algebra
> `(B, d)` is K-flat as a complex of `R`-modules and `A ⊗_R C` represents `A ⊗^𝐋_R C` in `D(R)`,
> then the canonical map `(A ⊗_R B)_B ⊗_B^𝐋 {}_B(B ⊗_R C)_C ⟶ (A ⊗_R B ⊗_R C)_C` of Tag 0BZ4 is an
> isomorphism — which by Tag 0BZ5 is all that the conclusion of Tag 0BZ8 needs.
>
> The source resolves `(A ⊗_R B)_B` by `L ⊗_R B` for a property-(P) differential graded `R`-module
> `L` quasi-isomorphic to `A`; the comparison of Tag 09LS at `(A ⊗_R B)_B` is then the map
> `L ⊗_R B ⊗_R C ⟶ A ⊗_R B ⊗_R C`, which K-flatness of `B` reduces to `L ⊗_R C ⟶ A ⊗_R C`, and
> that is the representability hypothesis. Here the resolution is an arbitrary property-(P)
> resolution `Q ⟶ (A ⊗_R B)_B`, and what replaces the source's computation is that the complex
> underlying `Q` is K-flat over `R` and that tensoring a K-flat resolution with `C` does not
> depend on which resolution is taken; the resolution the hypothesis is evaluated at is then
> `Tot(P^• ⊗_R B^•)` for a K-flat resolution `P^• ⟶ A^•` of complexes of `R`-modules.

```lean
theorem isIso_derivedTensorBaseChangeComparison_of_dgaResolutionRepresents
    (A B C : DifferentialGradedAlgebra.{u, u} R)
    (hB : CochainComplex.KFlat.{u, u} (regularModule B).toCochainComplex)
    (hrep : DgaResolutionRepresentsDerivedTensor A C) :
    IsIso (derivedTensorBaseChangeComparison A B C)
```

**`DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIsoOfKFlatBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionKFlatBase.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionKFlatBase.lean#L215). The attribute's comment: “for B K-flat as a complex of R-modules, with representability of A ⊗^L\_R C by A ⊗\_R C as its only other hypothesis”.

> **Stacks Tag 0BZ8 for a K-flat middle algebra.** Let `R` be a ring, let `(A, d)`, `(B, d)`
> and `(C, d)` be differential graded `R`-algebras with `A ⊗_R C` representing `A ⊗^𝐋_R C` in
> `D(R)` and with `B` K-flat as a complex of `R`-modules, let `N` be a differential graded
> `(A, B)`-bimodule and `N'` a differential graded `(B, C)`-bimodule. Then the composition
> `D(A, d) → D(B, d) → D(C, d)` of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'` is isomorphic to `- ⊗_A^𝐋 N''` for
> the differential graded `(A, C)`-bimodule `N'' = Ñ ⊗_B Ñ'` of
> `DifferentialGraded.Bimodule.compTensorResolution`.
>
> This is `DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIso` with its carried
> hypothesis `hbridge` discharged; the representability hypothesis `hrep` of the source is the only
> hypothesis left besides K-flatness of `B`, which the source's reduction by Tag 0BZ7 and Tag 09S6
> removes — that is
> `DifferentialGraded.Bimodule.exists_derivedTensorFunctorCompIso` of
> `StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionGeneralBase.lean`, at the cost of no
> longer naming the bimodule `N''`.

```lean
def dgaResolutionDerivedTensorFunctorCompIsoOfKFlatBase
    {A B C : DifferentialGradedAlgebra.{u, u} R}
    (hB : CochainComplex.KFlat.{u, u} (regularModule B).toCochainComplex)
    (hrep : DgaResolutionRepresentsDerivedTensor A C)
    (N : Bimodule A B) (N' : Bimodule B C) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensorResolution N N')
```

**`DifferentialGraded.Bimodule.dgaResolutionDerivedTensorFunctorCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionTensorRepresents.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DgaResolutionTensorRepresents.lean#L113). The attribute's comment: “with the passage from the representability hypothesis to the Stacks 0BZ4 hypothesis of Stacks 0BZ5 as hbridge, which is proved for B K-flat as a complex of R-modules by dgaResolutionRepresentsInvertsBaseChange\_of\_kFlat and for a general B needs the transport along the Stacks 09S6 equivalence that the source's K-flat replacement of B by Stacks 0BZ7 sets up”.

> Let `(A, d)`, `(B, d)` and `(C, d)` be differential graded `R`-algebras with `A ⊗_R C`
> representing `A ⊗^𝐋_R C` in `D(R)` (`hrep`), and assume that representability makes
> `derivedTensorBaseChangeComparison A B C` an isomorphism (`hbridge`). Let `N` be a differential
> graded `(A, B)`-bimodule and `N'` a differential graded `(B, C)`-bimodule. Then the composition
> `D(A, d) → D(B, d) → D(C, d)` of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'` is isomorphic to `- ⊗_A^𝐋 N''` for
> the differential graded `(A, C)`-bimodule `N'' = Ñ ⊗_B Ñ'` of
> `DifferentialGraded.Bimodule.compTensorResolution`, the composite of property-(P) replacements.

```lean
def dgaResolutionDerivedTensorFunctorCompIso
    (hbridge : DgaResolutionRepresentsInvertsBaseChange A B C)
    (hrep : DgaResolutionRepresentsDerivedTensor A C)
    (N : Bimodule A B) (N' : Bimodule B C) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensorResolution N N')
```

## Tag 0CRM, a lemma

[Tag 0CRM](https://stacks.math.columbia.edu/tag/0CRM) in the Stacks Project.

**`DifferentialGradedModule.countable_cohomology_of_isHomotopyColimit_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableCohomology.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableCohomology.lean#L189). The attribute's comment: “(1) implies (2)”.

> **Stacks 0CRM, the implication (1) ⇒ (2).** *"Let `(A, d)` be a differential graded algebra
> such that `H^i(A)` is countable for every `i`. Let `M` be an object of `D(A, d)`. If
> `M = hocolim Eₙ` with each `Eₙ` compact, then `H^i(M)` is countable for every `i`."*
>
> Cohomology commutes with the derived colimit in the weak sense that the long exact sequence of the
> triangle `⊕ Eₙ → ⊕ Eₙ → M → (⊕ Eₙ)[1]` places `H^i(M)` between two cohomology modules of `⊕ Eₙ`,
> and those are countable because each `Eₙ` is compact.

```lean
theorem countable_cohomology_of_isHomotopyColimit_of_isCompactObject
    (hA : ∀ k : ℤ, Countable (A.Cohomology k)) (M : derivedCategory.{u, u, u} A)
    (F : ℕ ⥤ derivedCategory.{u, u, u} A) (hF : ∀ j, IsCompactObject.{u} (F.obj j))
    (hM : IsHomotopyColimit F M) (i : ℤ) :
    Countable ((cohomologyFunctor A i).obj M)
```

**`DifferentialGradedModule.exists_isHomotopyColimit_isCompactObject_of_countable_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableConverse.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableConverse.lean#L499). The attribute's comment: “(2) implies (1)”.

> **Stacks 0CRM, the implication (2) ⇒ (1).** *"Let `(A, d)` be a differential graded algebra
> such that `H^i(A)` is countable for every `i`. Let `M` be an object of `D(A, d)`. If `H^i(M)` is
> countable for every `i` then `M = hocolim Eₙ` with each `Eₙ` compact."*
>
> The system is the diagonally refined cell tower described in the implementation notes of this
> file: at the `n`-th step the `n`-th cell of `M` is attached and the dead cells in the window
> `4 ^ n` of the current enumeration are killed, finitely many at a time, so that every term stays
> compact; the two hypotheses of the gluing criterion
> `CategoryTheory.Pretriangulated.isHomotopyColimit_of_forall_fac_of_forall_eventually_eq_zero`
> are `DifferentialGradedModule.exists_comp_eq_of_surjective` and
> `DifferentialGradedModule.exists_comp_map_eq_zero`.
>
> Compactness is concluded in the universe-restricted spelling `IsCompactObject.{u}`, which makes
> this statement stronger than the source's; see the implementation notes.

```lean
theorem exists_isHomotopyColimit_isCompactObject_of_countable_cohomology
    (hA : ∀ k : ℤ, Countable (A.Cohomology k)) (M : derivedCategory.{u, u, u} A)
    (hM : ∀ i : ℤ, Countable ((cohomologyFunctor A i).obj M)) :
    ∃ F : ℕ ⥤ derivedCategory.{u, u, u} A,
      (∀ n : ℕ, IsCompactObject.{u} (F.obj n)) ∧ IsHomotopyColimit F M
```

**`DifferentialGradedModule.exists_isHomotopyColimit_isCompactObject_iff_countable_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableConverse.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactCountableConverse.lean#L527).

> **Stacks 0CRM.** *"Let `(A, d)` be a differential graded algebra with `H^i(A)` countable for
> each `i`. Let `M` be an object of `D(A, d)`. Then the following are equivalent: (1)
> `M = hocolim Eₙ` with `Eₙ` compact in `D(A, d)`, and (2) `H^i(M)` is countable for each `i`."*
>
> The implication (1) ⇒ (2) is
> `DifferentialGradedModule.countable_cohomology_of_isHomotopyColimit_of_isCompactObject` and the
> implication (2) ⇒ (1) is
> `DifferentialGradedModule.exists_isHomotopyColimit_isCompactObject_of_countable_cohomology`.
> Compactness is read in the universe-restricted spelling `IsCompactObject.{u}` on both sides; see
> the implementation notes of this file.

```lean
theorem exists_isHomotopyColimit_isCompactObject_iff_countable_cohomology
    (hA : ∀ k : ℤ, Countable (A.Cohomology k)) (M : derivedCategory.{u, u, u} A) :
    (∃ F : ℕ ⥤ derivedCategory.{u, u, u} A,
        (∀ n : ℕ, IsCompactObject.{u} (F.obj n)) ∧ IsHomotopyColimit F M) ↔
      ∀ i : ℤ, Countable ((cohomologyFunctor A i).obj M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.38, Tag 0BZ6](https://stacks.math.columbia.edu/tag/0BZ6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
