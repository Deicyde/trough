---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isFilteredColimit_isFinitePresentationOnSite, AlgebraicGeometry.Space.exists_isFilteredColimit_isFinitePresentation, AlgebraicGeometry.Space.finiteTypeQuasicoherentSubobject_isFiltered, AlgebraicGeometry.Space.isFiltered_finiteTypeQuasicoherentSubobject, AlgebraicGeometry.Space.nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs, AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs, AlgebraicGeometry.Space.exists_directed_isFinitePresentation_epi, AlgebraicGeometry.Space.exists_directed_isFinitePresentation_algebra_of_idealQuotients
statement: formalized
proof: formalized
---

# 70.9 Applications

Section 70.9 of the Stacks Project, [Tag 07V8](https://stacks.math.columbia.edu/tag/07V8). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07V9, a lemma

[Tag 07V9](https://stacks.math.columbia.edu/tag/07V9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFilteredColimit_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean#L108). The attribute's comment: “with a small filtered index category and finite presentation in the on-site rendering of Stacks 03DL(7)”.

> **Stacks 07V9.**  Let `X` be a quasi-compact and quasi-separated algebraic space over a scheme
> `S`.  Then every quasi-coherent `𝒪_X`-module `F` is a filtered colimit of `𝒪_X`-modules of
> finite presentation: there is a small filtered category `I`, a diagram `D` of `𝒪_X`-modules of
> finite presentation indexed by it and a colimit cocone on `D` with vertex `F`.
>
> The hypotheses are the source's.  The proof does not use absolute Noetherian approximation; it
> follows the route the source indicates, through the filtration of Decent Spaces, Lemma 07ST, in
> the form of the induction principle of Stacks 08GP.

```lean
theorem exists_isFilteredColimit_isFinitePresentationOnSite
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (F : Modules.{u, u} B S hS X hX) (hF : F.IsQuasicoherentOnSite) :
    ∃ (I : Type u) (inst : SmallCategory I),
      let _ := inst
      ∃ (_ : IsFiltered I) (D : I ⥤ Modules.{u, u} B S hS X hX)
        (φ : D ⟶ (Functor.const I).obj F),
        (∀ i, (D.obj i).IsFinitePresentationOnSite) ∧ Nonempty (IsColimit (Cocone.mk F φ))
```

**`AlgebraicGeometry.Space.exists_isFilteredColimit_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean#L126). The attribute's comment: “in the rendering by Mathlib's finite presentation predicate”.

> **Stacks 07V9**, in the conclusion shape of the conditional statement
> `AlgebraicGeometry.Space.isFilteredColimit_isFinitePresentation_of_isQuasiCompactSpace` (an index
> category with objects in `Type (u + 1)` and morphisms in `Type u`, finite presentation in the
> sense of Mathlib's `SheafOfModules.IsFinitePresentation`), with none of its carried inputs.

```lean
theorem exists_isFilteredColimit_isFinitePresentation
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (F : Modules.{u, u} B S hS X hX) (hF : F.IsQuasicoherentOnSite) :
    ∃ (K : Type (u + 1)) (inst : Category.{u} K),
      let _ := inst
      ∃ (_ : IsFiltered K) (D : K ⥤ Modules.{u, u} B S hS X hX)
        (φ : D ⟶ (Functor.const K).obj F),
        (∀ k, (D.obj k).IsFinitePresentation) ∧ Nonempty (IsColimit (Cocone.mk F φ))
```

## Tag 0829, a lemma

[Tag 0829](https://stacks.math.columbia.edu/tag/0829) in the Stacks Project.

**`AlgebraicGeometry.Space.finiteTypeQuasicoherentSubobject_isFiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjects.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjects.lean#L483). The attribute's comment: “the directedness clause, for an arbitrary quasi-coherent module on an arbitrary algebraic space”.

> The finite type quasi-coherent submodules of a quasi-coherent module form a directed
> system.

```lean
theorem finiteTypeQuasicoherentSubobject_isFiltered
    (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite] :
    IsFiltered (FiniteTypeQuasicoherentSubobject B S hS X hX F)
```

**`AlgebraicGeometry.Space.isFiltered_finiteTypeQuasicoherentSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectsDirected.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectsDirected.lean#L76). The attribute's comment: “directedness, for an arbitrary algebraic space”. References: SGA 3 VIB (11.10), “partial”.

> **The directedness assertion of Stacks 0829.**  The quasi-coherent submodules of finite type
> of a quasi-coherent `𝒪_F`-module form a directed system: the image in the module of the direct
> sum of two of them is a quasi-coherent submodule of finite type containing both.
>
> Stacks 0829 states this for a quasi-compact and quasi-separated algebraic space; those two
> hypotheses enter only its colimit assertion, through Stacks 07V9, so the statement here is for
> an arbitrary algebraic space.

```lean
theorem isFiltered_finiteTypeQuasicoherentSubobject (G : Modules.{u, u} B S hS F hF)
    [G.IsQuasicoherentOnSite] :
    IsFiltered (FiniteTypeQuasicoherentSubobject B S hS F hF G)
```

**`AlgebraicGeometry.Space.nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectsQcqs.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectsQcqs.lean#L98). The attribute's comment: “the colimit clause”.

> **Stacks 0829, the colimit assertion.**  Let `X` be a quasi-compact and quasi-separated
> algebraic space over a scheme `S` and let `F` be a quasi-coherent `𝒪_X`-module.  Then `F` is the
> colimit of the canonical diagram of its finite type quasi-coherent submodules.
>
> The diagram is directed by `AlgebraicGeometry.Space.isFiltered_finiteTypeQuasicoherentSubobject`,
> which together with this declaration covers the whole of Stacks 0829.

```lean
theorem nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite] :
    Nonempty (IsColimit (finiteTypeQuasicoherentSubobjectCocone B S hS X hX F))
```

**`AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeSubmoduleQcqs.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeSubmoduleQcqs.lean#L350). References: SGA 3 VIB (11.10), “more general”.

> **Stacks 0829.** On a quasi-compact quasi-separated algebraic space `X`, a quasi-coherent
> `𝒪_X`-module `F` is the directed colimit of its quasi-coherent submodules of finite type: the
> category `AlgebraicGeometry.Space.FiniteTypeQuasicoherentSubobject` of those submodules is
> filtered and their canonical cocone with point `F` is a colimit cocone.
>
> Directedness is `AlgebraicGeometry.Space.finiteTypeQuasicoherentSubobject_isFiltered`, which
> uses Descent 03DX(2) and the cokernel clause of Stacks 03M1, that is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts` and
> `AlgebraicGeometry.Space.isClosedUnderCokernels_quasicoherentSheaves`. For the colimit, the
> supremum of the submodules is `⊤`: its inclusion is surjective on sections over affine charts,
> every section there lying in one of them by
> `AlgebraicGeometry.Space.exists_isFiniteType_submodule_mem_of_qcqs`.

```lean
theorem isFiltered_and_nonempty_isColimit_finiteTypeQuasicoherentSubobjectCocone_of_qcqs
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (F : Modules.{u, u} B S hS X.1 X.2) [hF : F.IsQuasicoherentOnSite] :
    IsFiltered (FiniteTypeQuasicoherentSubobject B S hS X.1 X.2 F) ∧
      Nonempty (IsColimit (finiteTypeQuasicoherentSubobjectCocone B S hS X.1 X.2 F))
```

## Tag 086Y, a lemma

[Tag 086Y](https://stacks.math.columbia.edu/tag/086Y) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_directed_isFinitePresentation_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationGeneration/Main.lean#L146).

> **Stacks 086Y.**  Let `X` be a quasi-compact and quasi-separated algebraic space over a
> scheme `S` and let `M` be a finite type quasi-coherent `𝒪_X`-module.  Then `M` is the colimit of
> a system of `𝒪_X`-modules of finite presentation indexed by a directed poset, all of whose
> transition maps are surjective.
>
> The source writes `ℱ = lim ℱ_i`, but its proof produces `colim 𝒢_i/𝒦_a`; the conclusion is a
> colimit, as in the scheme-level counterpart Stacks 086M.

```lean
theorem exists_directed_isFinitePresentation_epi
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (M : Modules.{u, u} B S hS X hX) [M.IsQuasicoherentOnSite] [M.IsFiniteTypeOnSite] :
    ∃ (I : Type (u + 1)) (_ : PartialOrder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ Modules.{u, u} B S hS X hX) (φ : D ⟶ (Functor.const I).obj M)
      (_ : IsColimit (Cocone.mk M φ)),
      (∀ i, (D.obj i).IsFinitePresentationOnSite) ∧
        ∀ (i j : I) (h : i ≤ j), Epi (D.map (homOfLE h))
```

## Tag 082A, a lemma

[Tag 082A](https://stacks.math.columbia.edu/tag/082A) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_directed_isFinitePresentation_algebra_of_idealQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IdealQuotientApproximationSystem.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IdealQuotientApproximationSystem.lean#L229). The attribute's comment: “PARTIAL, but the construction and not the reindexing: the members A\_\{i,j} = B\_i/I\_\{i,j} of the source's system and the morphisms between them are constructed here, as quotients of an algebra sheaf on an algebraic space by a sheaf of ideals and factorizations through them, which is the object whose absence was the recorded obstruction. Three inputs are carried, each separately identified. (1) The system datum D, psi -- in the source B\_i = Sym(F\_i) with the maps induced by Stacks 07V9 -- because at the algebraic space level this tree has the symmetric algebra of a module but neither its functoriality in the module nor the ungraded universal property giving Sym(F\_i) to A, both of which exist only for schemes (AlgebraicGeometry.Scheme.Modules.symmetricAlgebraSheafMap, Stacks.SymAlgSheaf.algebraLift), nor quasi-coherence of Sym. (2) Quasi-coherence and finite presentation of each stage, which are conditions on the sections of a sheafification over the affine etale charts; this is where the source's finite generation of I\_\{i,j} is used, so the ideals here are arbitrary. (3) The colimit property of the constructed cocone, colimits in AlgebraicGeometry.Space.AlgebraSheaf being constructed nowhere in this tree. The source's quasi-compactness and quasi-separatedness are absent because they are used only to produce the system datum, which is hypothesis (1)”.

> **Stacks Project, Tag 082A, over the system datum.**  Let `S` be a scheme, `X` an algebraic
> space over `S` and `𝒜` an `𝒪_X`-algebra.  Let `D` be a filtered system of `𝒪_X`-algebras with a
> cocone `ψ` over `𝒜`, and for each `i` let `ℐ_i` be a sheaf of ideals of `D_i` killed by `ψ_i`
> and carried into `ℐ_j` by every transition map.  If every quotient `D_i/ℐ_i` is quasi-coherent
> of finite presentation and the constructed cocone of those quotients over `𝒜` is colimiting,
> then `𝒜` is the colimit of a system of quasi-coherent `𝒪_X`-algebras of finite presentation
> indexed by a directed poset.
>
> The members of the system and the morphisms between them are *constructed*: they are
> `AlgebraicGeometry.Space.idealQuotientSystem` and
> `AlgebraicGeometry.Space.idealQuotientSystemCocone`, built from the quotient of an algebra sheaf
> by a sheaf of ideals and its universal property.  See the module documentation for what each of
> the three hypotheses is and why it is a separate missing ingredient rather than the conclusion.

```lean
theorem exists_directed_isFinitePresentation_algebra_of_idealQuotients [IsFiltered P]
    (hstage : ∀ p : P, ((D.obj p).idealQuotient (I p)).IsQuasicoherent ∧
      ((D.obj p).idealQuotient (I p)).IsFinitePresentation)
    (hcol : IsColimit (Cocone.mk A (idealQuotientSystemCocone A D ψ I hkill hmap))) :
    ∃ (J : Type u) (_ : PartialOrder J) (_ : Nonempty J) (_ : IsDirected J (· ≤ ·))
      (E : J ⥤ AlgebraSheaf.{u, u} B S hS X hX) (φ : E ⟶ (Functor.const J).obj A)
      (_ : IsColimit (Cocone.mk A φ)),
      ∀ j, (E.obj j).IsQuasicoherent ∧ (E.obj j).IsFinitePresentation
```

**`AlgebraicGeometry.Space.exists_directed_isFinitePresentation_algebra_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentAlgebraFinitePresentationColimitQcqs.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentAlgebraFinitePresentationColimitQcqs.lean#L61). The attribute's comment: “a quasi-coherent algebra on a quasi-compact quasi-separated algebraic space is the colimit, among all algebra sheaves, of a system of quasi-coherent algebras of finite presentation indexed by a nonempty directed poset”.

> Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space over `S` and `𝒜` a
> quasi-coherent `𝒪_X`-algebra.  Then `𝒜` is the colimit, in the category of all `𝒪_X`-algebras, of a
> system of quasi-coherent `𝒪_X`-algebras of finite presentation indexed by a nonempty directed
> partially ordered set.  The colimit is taken in `AlgebraicGeometry.Space.AlgebraSheaf`, which is
> stronger than in the full subcategory of the quasi-coherent algebras.

```lean
theorem exists_directed_isFinitePresentation_algebra_of_isQuasiCompactSpace
    (X : AlgebraicSpaces B S hS) (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (A : AlgebraSheaf.{u, u} B S hS X.1 X.2) (hA : A.IsQuasicoherent) :
    ∃ (J : Type u) (_ : PartialOrder J) (_ : Nonempty J) (_ : IsDirected J (· ≤ ·))
      (E : J ⥤ AlgebraSheaf.{u, u} B S hS X.1 X.2) (ψ : E ⟶ (Functor.const J).obj A)
      (_ : IsColimit (Cocone.mk A ψ)),
      ∀ j, (E.obj j).IsQuasicoherent ∧ (E.obj j).IsFinitePresentation
```

## Tag 082B, a lemma

[Tag 082B](https://stacks.math.columbia.edu/tag/082B) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiltered_and_isColimit_finiteTypeSubalgebraCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeSubalgebraColimit.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeSubalgebraColimit.lean#L480).

> **Stacks 082B.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic
> space over `S` and `𝒜` a quasi-coherent `𝒪_X`-algebra.  Then `𝒜` is the directed colimit of its
> finite type quasi-coherent `𝒪_X`-subalgebras: they form a filtered category, and the cocone of
> their inclusions into `𝒜` is a colimit cocone.
>
> Directedness is `AlgebraicGeometry.Space.isFiltered_finiteTypeSubalgebra`.  The cocone is a
> colimit because its legs are injective on sections and, by
> `AlgebraicGeometry.Space.exists_finiteTypeSubalgebra_section`, jointly surjective on the
> sections over affine étale charts.

```lean
theorem isFiltered_and_isColimit_finiteTypeSubalgebraCocone (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1) (A : AlgebraSheaf.{u, u} B S hS X.1 X.2)
    (hA : A.IsQuasicoherent) :
    IsFiltered (FiniteTypeSubalgebra B S hS X.1 X.2 A) ∧
      Nonempty (IsColimit (finiteTypeSubalgebraCocone B S hS X.1 X.2 A))
```

**`AlgebraicGeometry.Space.isFiltered_finiteTypeSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SubalgebraJoinFiniteType.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SubalgebraJoinFiniteType.lean#L403). The attribute's comment: “the directedness assertion; the colimit assertion is blocked on Stacks 07SU through 0829 and 07V9 by the source's own route”.

> **The finite type quasi-coherent subalgebras of a quasi-coherent sheaf of `𝒪_Y`-algebras on
> an algebraic space form a filtered category**, with no hypothesis beyond quasi-coherence of the
> algebra.
>
> Nonemptiness is the image of the canonical morphism from the structure sheaf, and upper bounds
> are the subalgebras generated by two subalgebras.

```lean
theorem isFiltered_finiteTypeSubalgebra (Y : AlgebraicSpaces B S hS)
    (A : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (hA : A.IsQuasicoherent) :
    IsFiltered (FiniteTypeSubalgebra B S hS Y.1 Y.2 A)
```

## Tag 086Z, a lemma

[Tag 086Z](https://stacks.math.columbia.edu/tag/086Z) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation_locallySurjective_of_elementaryData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AlgebraSheafIdealQuotientColimit.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AlgebraSheafIdealQuotientColimit.lean#L729). The attribute's comment: “the same conclusion as AlgebraicGeometry.Space.exists\_directed\_isFinite\_isFinitePresentation\_locallySurjective — the directedness of the index, the finiteness and the finite presentation of every stage, the surjectivity of every transition map and the colimit — but over an ELEMENTARY carried input in place of that theorem's hsource. THIS REGISTRATION IS FORMALLY WEAKER THAN THAT ONE AND DOES NOT REPLACE IT: the carried input here is strictly stronger, so the unrestricted reading of the tag remains the one carried there. What this registration claims is that the three non-elementary conjuncts of hsource — quasi-coherence of every quotient B/I\_j, finite presentation of every quotient B/I\_j, and the colimit property of the constructed cocone — are each DERIVABLE, and it derives them: quasi-coherence from quasi-coherence of B and of I\_j by AlgebraicGeometry.Space.AlgebraSheaf.isQuasicoherent\_idealQuotient, finite presentation from finite presentation of B and finite generation of the ideal of sections I\_j(W) over each affine etale chart by AlgebraicGeometry.Space.AlgebraSheaf.isFinitePresentation\_idealQuotient, and the colimit from local surjectivity of f together with local membership in the family of every section f kills by AlgebraicGeometry.Space.nonempty\_isColimit\_idealQuotientQcohCocone\_of\_locally. Every conjunct that remains carried is a condition on sections of B, of the I\_j and of A over the objects of the small etale site, or on a single affine etale chart. STILL CARRIED, and NOT dischargeable in this tree today: (i) quasi-coherence of AlgebraicGeometry.Space.symmetricAlgebraSheaf for a quasi-coherent module, which is the B of the source and is recorded as absent in StacksFrontier.AlgebraicGeometry.Spaces.SymmetricAlgebraSheafMap (Stacks 01CK/01CL hold for a ringed space, as Stacks.SheafOfModules.isQuasicoherent\_symmetricAlgebraSheaf\_of\_isQuasicoherent, but not for the small etale site of an algebraic space); (ii) finite presentation of that same Sym(F), the sections of which over a chart are only LOCALLY finite sums of homogeneous ones; (iii) integrality at one index, the fourth step of the source. Note also that Stacks 086Y, AlgebraicGeometry.Space.exists\_directed\_isFinitePresentation\_epi\_of\_isFiniteType, is itself proved only over three carried inputs h07V9, hstage and hcoker, so Stacks 086Z is NOT unconditional in this tree by this route or any other presently available”.

> **Stacks Project, Tag 086Z, over elementary data about `ℬ` and the family of ideals.**  Same
> conclusion as
> `AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation_locallySurjective`: `A` is
> the colimit of a system of quasi-coherent `𝒪_Y`-algebras over a nonempty directed preorder, every
> member finite and of finite presentation and every transition map locally surjective.
>
> The carried input no longer mentions the quotients `ℬ/ℐ_j` except at the single index where
> integrality is asked.  It asks instead: `ℬ` quasi-coherent and of finite presentation, each `ℐ_j`
> quasi-coherent as an `𝒪_Y`-module with finitely generated ideal of sections over each affine
> étale chart, `f` locally surjective, and every section of `ℬ` which `f` kills locally a section
> of some `ℐ_j`.  Those are the data of the first three steps of the source's proof and nothing
> more.
>
> See the section documentation above: this is a formally weaker statement than the theorem it
> calls, deliberately, and it does not make Stacks 086Z unconditional.

```lean
theorem exists_directed_isFinite_isFinitePresentation_locallySurjective_of_elementaryData
    (A : QuasicoherentAlgebra B S hS Y)
    (hqc : IsQuasiCompactSpace B S hS Y.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj)
    (hA : A.obj.IsFinite)
    (hdata :
      IsQuasiCompactSpace B S hS Y.obj →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj →
      A.obj.IsFinite →
        ∃ (ℬ : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (f : ℬ ⟶ A.obj) (J : Type u)
          (inst : SmallCategory J),
          let _ := inst
          ∃ (_ : IsFiltered J) (ι : J → ℬ.IdealSheaf)
            (_ : ∀ j j' : J, (j ⟶ j') → ι j ≤ ι j'),
            (∀ (j : J) (U : (SmallEtale B S hS Y.1)ᵒᵖ) (a : ℬ.right.obj.obj U),
                a ∈ (ι j).obj U → (f.right.hom.app U).hom a = 0) ∧
              ℬ.IsQuasicoherent ∧ ℬ.IsFinitePresentation ∧
              (∀ j, (AlgebraSheaf.idealModule ℬ (ι j)).IsQuasicoherentOnSite) ∧
              (∀ (j : J) (W : SmallEtale B S hS Y.1),
                IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
                  (Stacks.Sites.sectionIdeal (ι j) (op W)).FG) ∧
              Presheaf.IsLocallySurjective (SmallEtale.topology B S hS Y.1) f.right.hom ∧
              (∀ (U : (SmallEtale B S hS Y.1)ᵒᵖ) (a : ℬ.right.obj.obj U),
                  (f.right.hom.app U).hom a = 0 →
                    Stacks.Sites.memSieve (O := ℬ.right) ι a ∈
                      SmallEtale.topology B S hS Y.1 U.unop) ∧
              ∃ j, (ℬ.idealQuotient (ι j)).IsIntegral) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ QuasicoherentAlgebra B S hS Y) (φ : D ⟶ (Functor.const I).obj A),
      Nonempty (IsColimit (Cocone.mk A φ)) ∧
      (∀ i, (D.obj i).obj.IsFinite ∧ (D.obj i).obj.IsFinitePresentation) ∧
      ∀ i j (h : i ≤ j), Presheaf.IsLocallySurjective
        (SmallEtale.topology B S hS Y.obj) (D.map (homOfLE h)).hom.right.hom
```

**`AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation_locallySurjective_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteAlgebraFinitePresentationColimitQcqs.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteAlgebraFinitePresentationColimitQcqs.lean#L57).

> **Stacks Project, Tag 086Z.** Let `S` be a scheme, let `Y` be a quasi-compact and
> quasi-separated algebraic space over `S` and let `𝒜` be a finite quasi-coherent `𝒪_Y`-algebra.
> Then `𝒜` is the colimit of a system of quasi-coherent `𝒪_Y`-algebras indexed by a nonempty
> directed preorder, every member of which is finite and of finite presentation, and every
> transition map of which is surjective (locally surjective as a morphism of sheaves on the small
> étale site, which for quasi-coherent algebras is surjectivity on the sections over every affine
> étale chart).
>
> The proof is the source's.  Stacks 086Y gives a quasi-coherent module `𝒢` of finite presentation
> with an epimorphism `𝒢 ⟶ 𝒜`; then
> `AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation_locallySurjective_of_epi`
> forms `Sym(𝒢)`, writes the kernel of `Sym(𝒢) ⟶ 𝒜` as the union of its finite type
> quasi-coherent submodules `ℰ` (Stacks 0829), takes the quotients `Sym(𝒢)/(ℰ)`, shows they are
> finite for `ℰ` large, and reindexes by a directed preorder.

```lean
theorem exists_directed_isFinite_isFinitePresentation_locallySurjective_of_isFinite
    (Y : AlgebraicSpaces B S hS) (A : QuasicoherentAlgebra B S hS Y)
    (hqc : IsQuasiCompactSpace B S hS Y.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj)
    (hA : A.obj.IsFinite) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ QuasicoherentAlgebra B S hS Y) (φ : D ⟶ (Functor.const I).obj A),
      Nonempty (IsColimit (Cocone.mk A φ)) ∧
      (∀ i, (D.obj i).obj.IsFinite ∧ (D.obj i).obj.IsFinitePresentation) ∧
      ∀ i j (h : i ≤ j), Presheaf.IsLocallySurjective
        (SmallEtale.topology B S hS Y.obj) (D.map (homOfLE h)).hom.right.hom
```

**`AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteAlgebraSurjectiveSystem.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteAlgebraSurjectiveSystem.lean#L471). The attribute's comment: “the directedness of the index, the finiteness of every stage, the finite presentation of every stage and the surjectivity of every transition map, over the carried input hsource. hsource is the DATA the first three steps of the source's proof produce, not the system they build: one algebra sheaf B (in the source Sym(F) for the finitely presented module F of Stacks 086Y), a map B to the algebra, and a FILTERED family of sheaves of ideals of B killed by that map and growing along the index (in the source the finite type submodules of the kernel ideal, Stacks 0829), plus quasi-coherence and finite presentation of each quotient B/I\_j, the colimit property of the constructed cocone, and integrality — not finiteness — at ONE index, which is the single-index half of the fourth step. hsource is asked only AT THE Y AND THE A OF THE STATEMENT, not for every quasi-compact quasi-separated space and every finite algebra. The MEMBERS AND THE TRANSITION MAPS OF THE SYSTEM ARE NOT CARRIED: they are AlgebraicGeometry.Space.idealQuotientDiagram and AlgebraicGeometry.Space.idealQuotientQcohCocone, built from the quotient of an algebra sheaf on an algebraic space by a sheaf of ideals and its universal property (AlgebraicGeometry.Space.AlgebraSheaf.idealQuotient, idealQuotientMapOfLE, idealQuotientLift), and SURJECTIVITY OF EVERY TRANSITION MAP IS PROVED, by AlgebraicGeometry.Space.isLocallySurjective\_idealQuotientQcohDiagram\_map, so hsource asserts no surjectivity at all. Of the three inputs that leave Stacks 082A partial in AlgebraicGeometry.Space.exists\_directed\_isFinitePresentation\_algebra\_of\_idealQuotients, ALL THREE ARE NOW DISCHARGEABLE FROM ELEMENTARY DATA and none may be SUBSTITUTED for: in each case that data is not among the remaining conjuncts of hsource, so replacing a conjunct by it would make hsource STRONGER and this theorem weaker. (1) B and the map are now CONSTRUCTIBLE at the algebraic space level: functoriality of the symmetric algebra is AlgebraicGeometry.Space.symmetricAlgebraSheafMap in Spaces/SymmetricAlgebraSheafMap.lean and the ungraded universal property producing a morphism of algebra sheaves Sym(F) to A out of a morphism of modules F to A is AlgebraicGeometry.Space.SymAlgSheaf.algebraLift in Spaces/SymmetricAlgebraSheafUngradedLift.lean, so with Stacks 086Y one may take B = Sym(F) and the map = algebraLift; quasi-coherence of Sym(F) is still unproved at this level but hsource asks NO quasi-coherence of B, so it is not needed here. (2) The colimit property of the constructed cocone is now EQUIVALENT, at the level of all algebra sheaves, to two elementary local conditions — local surjectivity of the map and local membership of every section it kills in some member of the family — by AlgebraicGeometry.Space.nonempty\_isColimit\_idealQuotientAlgCocone\_iff\_locally in Spaces/Limits/AlgebraSheafIdealQuotientColimit.lean, and AlgebraicGeometry.Space.nonempty\_isColimit\_idealQuotientQcohCocone\_of\_locally supplies the quasi-coherent form that hsource asks for from those two conditions, with no affine-chart verification and no cohomology. It is NOT substituted into hsource: the quasi-coherent algebras are a full subcategory, whose inclusion reflects but need not preserve colimits, so at that level the implication runs one way only and substituting the local conditions would make this hypothesis STRONGER and the theorem weaker. (3) Quasi-coherence and finite presentation of a sheafified quotient over an affine etale chart — the identification of the sections of B/I\_j over such a chart with the objectwise quotient — is NOW PROVED, in Spaces/Limits/AlgebraSheafIdealQuotientCokernel.lean. The step that was missing, the identification of the underlying module of B/I\_j with the COKERNEL of the inclusion of I\_j, is AlgebraicGeometry.Space.AlgebraSheaf.underlyingModuleIdealQuotientCokernelIso, an epi-mono factorisation in the balanced category of O\_Y-modules whose exactness input is AlgebraicGeometry.Space.AlgebraSheaf.kerIdeal\_toIdealQuotient (the quotient morphism kills exactly the sections of the ideal, Spaces/Limits/AlgebraSheafIdealQuotientKernel.lean) and whose epimorphism input is local surjectivity of the quotient morphism. From it: quasi-coherence of B/I\_j is AlgebraicGeometry.Space.AlgebraSheaf.isQuasicoherent\_idealQuotient, by AlgebraicGeometry.Space.isQuasicoherentOnSite\_cokernel\_unconditional, GIVEN quasi-coherence of B and of I\_j; the sections over an affine chart W are B(W)/I\_j(W), by AlgebraicGeometry.Space.AlgebraSheaf.bijective\_idealQuotientSectionsLift and idealQuotientSectionsRingEquiv, whose surjectivity half is AlgebraicGeometry.Space.surjective\_val\_app\_of\_epi\_of\_isQuasicoherentOnSite, the restated form of Descent 03DW, unconditional in this tree by faithfully flat descent with no Cech cohomology; and finite presentation of B/I\_j is AlgebraicGeometry.Space.AlgebraSheaf.isFinitePresentation\_idealQuotient, GIVEN finite presentation of B and finite generation of the ideal of sections I\_j(W) over every affine chart, which is where the source's finite generation of the ideals enters and is why no finiteness is asked of them here. The conjunct is nevertheless NOT removed from hsource: hsource asks no quasi-coherence of B, no quasi-coherence of the I\_j, no finiteness of them and no finite presentation of B, and none of those follow from its remaining conjuncts — finite presentation of a structure-algebra map on every affine chart says nothing about the restriction maps being base changes, so it does not imply quasi-coherence — so dropping the conjunct would require ADDING FOUR NEW ONES (quasi-coherence of B, quasi-coherence of each I\_j, finite presentation of B, and finite generation of each I\_j(W)), which makes hsource STRONGER and this theorem weaker. What has changed is that a caller holding those four can now produce the conjunct with no further mathematics. Stacks 086Y and Stacks 0829 are both proved here (as AlgebraicGeometry.Space.exists\_directed\_isFinitePresentation\_epi\_of\_isFiniteType and as AlgebraicGeometry.Space.isColimit\_finiteTypeQuasicoherentSubobjectCocone\_of\_07V9 with AlgebraicGeometry.Space.isFiltered\_finiteTypeQuasicoherentSubobject). hsource asserts no finiteness of any stage and no directedness; finiteness of every stage, directedness, surjectivity of every transition map and survival of the colimit are proved. The source argues on one affine étale chart while this tree's finiteness predicates quantify over all of them, so the chart-uniformity of the carried integrality is carried too”.

> **Stacks Project, Tag 086Z.** Let `S` be a scheme, let `Y` be a quasi-compact and
> quasi-separated algebraic space over `S` and let `A` be a finite quasi-coherent `𝒪_Y`-algebra.
> Then `A` is the colimit of a system of quasi-coherent `𝒪_Y`-algebras indexed by a nonempty
> directed preorder, every member of which is finite and of finite presentation, and every
> transition map of which is surjective.
>
> All four assertions of the source are in the conclusion: the index is a nonempty preorder which
> is directed, every stage is `AlgebraicGeometry.Space.AlgebraSheaf.IsFinite` and
> `AlgebraicGeometry.Space.AlgebraSheaf.IsFinitePresentation`, every transition map is locally
> surjective, and the cocone with vertex `A` is colimiting.  Quasi-coherence of the stages is
> structural, the diagram taking values in `AlgebraicGeometry.Space.QuasicoherentAlgebra`.
>
> The quasi-compactness and quasi-separatedness of `Y` and the finiteness of `A` are used by being
> handed to `hsource`, which is the *data* of the third step of the source's proof — one algebra
> sheaf and a filtered family of sheaves of ideals of it — together with integrality at a single
> index, **for this `Y` and this `A` and no other**.  The system itself is built from that data by
> `AlgebraicGeometry.Space.idealQuotientDiagram` and
> `AlgebraicGeometry.Space.idealQuotientQcohCocone`; see the module documentation for what `hsource`
> stands for and for what is proved on top of it.

```lean
theorem exists_directed_isFinite_isFinitePresentation_locallySurjective
    (Y : AlgebraicSpaces B S hS) (A : QuasicoherentAlgebra B S hS Y)
    (hqc : IsQuasiCompactSpace B S hS Y.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj)
    (hA : A.obj.IsFinite)
    (hsource :
      IsQuasiCompactSpace B S hS Y.obj →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj →
      A.obj.IsFinite →
        ∃ (ℬ : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (f : ℬ ⟶ A.obj) (J : Type u)
          (inst : SmallCategory J),
          let _ := inst
          ∃ (_ : IsFiltered J) (ι : J → ℬ.IdealSheaf)
            (hι : ∀ j j' : J, (j ⟶ j') → ι j ≤ ι j')
            (hkill : ∀ (j : J) (U : (SmallEtale B S hS Y.1)ᵒᵖ) (a : ℬ.right.obj.obj U),
              a ∈ (ι j).obj U → (f.right.hom.app U).hom a = 0)
            (hqcoh : ∀ j, (ℬ.idealQuotient (ι j)).IsQuasicoherent),
            (∀ j, (ℬ.idealQuotient (ι j)).IsFinitePresentation) ∧
            (∃ j, (ℬ.idealQuotient (ι j)).IsIntegral) ∧
            Nonempty (IsColimit (Cocone.mk A
              (idealQuotientQcohCocone ℬ ι hι A f hkill hqcoh)))) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ QuasicoherentAlgebra B S hS Y) (φ : D ⟶ (Functor.const I).obj A),
      Nonempty (IsColimit (Cocone.mk A φ)) ∧
      (∀ i, (D.obj i).obj.IsFinite ∧ (D.obj i).obj.IsFinitePresentation) ∧
      ∀ i j (h : i ≤ j), Presheaf.IsLocallySurjective
        (SmallEtale.topology B S hS Y.obj) (D.map (homOfLE h)).hom.right.hom
```

## Tag 082C, a lemma

[Tag 082C](https://stacks.math.columbia.edu/tag/082C) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiltered_isColimit_finiteSubalgebra_and_exists_directed_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteColimitQcqs.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteColimitQcqs.lean#L98).

> **Stacks 082C.**  Let `X` be a quasi-compact and quasi-separated algebraic space over a
> scheme `S` and let `A` be an integral quasi-coherent `𝒪_X`-algebra.  Then
>
> 1. the finite quasi-coherent subalgebras of `A` form a directed (filtered) category and `A` is
>    the colimit of the cocone of their inclusions, and
> 2. `A` is the colimit of a directed system, over a nonempty directed preorder, of
>    quasi-coherent `𝒪_X`-algebras that are finite and of finite presentation.
>
> The hypotheses are the source's.

```lean
theorem isFiltered_isColimit_finiteSubalgebra_and_exists_directed_finite
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X)
    (A : AlgebraSheaf.{u, u} B S hS X hX) (hA : A.IsQuasicoherent) (hint : A.IsIntegral) :
    (IsFiltered (FiniteSubalgebra B S hS X hX A) ∧
        Nonempty (IsColimit (finiteSubalgebraCocone B S hS X hX A))) ∧
      ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
        (D : I ⥤ AlgebraSheaf.{u, u} B S hS X hX) (t : D ⟶ (Functor.const I).obj A)
        (_ : IsColimit (Cocone.mk A t)),
        ∀ i, (D.obj i).IsQuasicoherent ∧ (D.obj i).IsFinite ∧ (D.obj i).IsFinitePresentation
```

**`AlgebraicGeometry.Space.isFiltered_finiteSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean#L70). The attribute's comment: “part (1), the directedness assertion, and with no hypothesis beyond quasi-coherence and integrality of the algebra: neither quasi-compactness nor quasi-separatedness of the space is used. The colimit assertion of part (1) is AlgebraicGeometry.Space.nonempty\_isColimit\_finiteSubalgebraCocone and part (2) is AlgebraicGeometry.Space.exists\_directed\_isFinite\_isFinitePresentation; those two name their own restrictions, this one has none”.

> The finite quasi-coherent subalgebras of an integral quasi-coherent sheaf of commutative
> `𝒪_Y`-algebras on an algebraic space `Y` form a filtered category.

```lean
theorem isFiltered_finiteSubalgebra (Y : AlgebraicSpaces B S hS)
    (A : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (hqcoh : A.IsQuasicoherent)
    (hint : A.IsIntegral) :
    IsFiltered (FiniteSubalgebra B S hS Y.1 Y.2 A)
```

**`AlgebraicGeometry.Space.nonempty_isColimit_finiteSubalgebraCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean#L99). The attribute's comment: “part (1), the colimit assertion, over the carried input hgen: for every affine etale chart U of the space and every section x of the algebra over U there is a finite quasi-coherent subalgebra of the algebra, on the whole space, having x among its sections over U. hgen is the algebraic-space analogue of what the scheme-level development derives from Stacks 01PF, namely Stacks.AlgebraicGeometry.SubalgebraGeneratedByModule.exists\_finiteTypeSubalgebra\_section, and it is asked only AT THE SPACE AND THE ALGEBRA OF THE STATEMENT. It replaces the colimit assertion of Stacks 082B, which is blocked by the source's own route on Stacks 07SU through Stacks 0829 and Stacks 07V9, and is strictly weaker than it: hgen mentions no cocone, no colimit and no index, and quantifies only over sections over single affine etale charts. Everything else is proved: directedness of the index is AlgebraicGeometry.Space.isFiltered\_finiteSubalgebra, which has no restriction at all, sectionwise injectivity of the legs is AlgebraicGeometry.Space.AlgebraSheaf.injective\_subobject\_arrow\_app, and the passage from sections over the affine etale charts to the colimit property is AlgebraicGeometry.Space.AlgebraSheaf.nonempty\_isColimit\_of\_affineChartSections\_of\_injective. The identification of the finite with the finite type quasi-coherent subalgebras over an integral algebra, which is Algebra Lemma 10.36.5 on the affine etale charts, is proved as AlgebraicGeometry.Space.isQuasicoherentAndIsFinite\_eq\_isQuasicoherentAndIsFiniteType'”.

> An integral quasi-coherent sheaf of commutative `𝒪_Y`-algebras `A` on a quasi-compact and
> quasi-separated algebraic space `Y` is the colimit of the cocone of the inclusions of its finite
> quasi-coherent subalgebras, provided (`hgen`) every section of `A` over an affine étale chart of
> `Y` lies in the image of one finite quasi-coherent subalgebra of `A`.

```lean
theorem nonempty_isColimit_finiteSubalgebraCocone (Y : AlgebraicSpaces B S hS)
    (A : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (hqcoh : A.IsQuasicoherent) (hint : A.IsIntegral)
    (hqc : IsQuasiCompactSpace B S hS Y.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj)
    (hgen : IsQuasiCompactSpace B S hS Y.obj →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj →
      ∀ U : SmallEtale B S hS Y.1,
        IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙ BigFppfOver.toScheme B S hS).obj U) →
        ∀ x : A.right.obj.obj (op U),
          ∃ C : FiniteSubalgebra B S hS Y.1 Y.2 A,
            x ∈ Set.range ((C.obj.arrow.right.hom.app (op U)).hom)) :
    Nonempty (IsColimit (finiteSubalgebraCocone B S hS Y.1 Y.2 A))
```

**`AlgebraicGeometry.Space.exists_directed_isFinite_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralAlgebraFiniteSubalgebraColimit.lean#L191). The attribute's comment: “part (2), over three carried inputs. (a) hgen, the same input as in AlgebraicGeometry.Space.nonempty\_isColimit\_finiteSubalgebraCocone: every section of the algebra over an affine etale chart lies in the image of one finite quasi-coherent subalgebra on the whole space. Part (1) is PROVED from it here and is not assumed. (b) hstage, the carried input of Stacks 086Z itself — see the module documentation of StacksFrontier.AlgebraicGeometry.Spaces.Limits.FiniteAlgebraSurjectiveSystem for what it says — asked at every finite quasi-coherent algebra on the space rather than at one; Stacks 086Z is not restated, the theorem AlgebraicGeometry.Space.exists\_directed\_isFinite\_isFinitePresentation\_locallySurjective is called, so the finiteness, the finite presentation and the directedness of every inner system are that theorem's and not assumed here. (c) hpres, presentability of a finite and finitely presented quasi-coherent algebra ALONG THE TWO SYSTEMS' OWN COCONES, which is the analogue for algebraic spaces of the input the source takes from Cohomology of Spaces Lemma 69.5.3 and is weaker both than that lemma and than CategoryTheory.IsFinitelyPresentable of the stages: nothing is asked about any filtered colimit other than the two being spliced. On schemes the corresponding statement is a theorem, Stacks.AlgebraicGeometry.Tag0817Presentable.presentableAlong\_of\_isFinitePresentation, proved by carrying Stacks 01ZC across the relative spectrum of Stacks 01SA; for algebraic spaces the relative spectrum of Stacks 081W and the limit-preserving criterion AlgebraicGeometry.Space.exists\_stage\_map\_of\_relativelyLimitPreserving of Stacks 04AK are proved but the passage from a colimit of algebra sheaves to a limit of algebraic spaces affine over the base is not, so hpres is not proved. What is proved on top of the three: part (1) from hgen, including its directedness which has no restriction, the lifting of each inner index from Type u to the morphism universe of the quasi-coherent algebras along CategoryTheory.AsSmall, the splice itself, and that every stage of the resulting directed system is finite and of finite presentation. No declaration in this file assumes any assertion of Stacks 082C”.

> An integral quasi-coherent sheaf of commutative `𝒪_Y`-algebras on a quasi-compact and
> quasi-separated algebraic space `Y` is the colimit of a system, indexed by a nonempty directed
> preorder, of quasi-coherent `𝒪_Y`-algebras each of which is finite and of finite presentation,
> provided `hgen` (as in `nonempty_isColimit_finiteSubalgebraCocone`), `hstage` (every finite
> quasi-coherent algebra on `Y` is a filtered colimit of finitely presented quotients of an algebra
> sheaf, one of them integral) and `hpres` (every finite and finitely presented quasi-coherent
> algebra is finitely presentable along every filtered colimit cocone of quasi-coherent algebras).

```lean
theorem exists_directed_isFinite_isFinitePresentation (Y : AlgebraicSpaces B S hS)
    (A : QuasicoherentAlgebra B S hS Y) (hint : A.obj.IsIntegral)
    (hqc : IsQuasiCompactSpace B S hS Y.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj)
    (hgen : IsQuasiCompactSpace B S hS Y.obj →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj →
      ∀ U : SmallEtale B S hS Y.1,
        IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙ BigFppfOver.toScheme B S hS).obj U) →
        ∀ x : A.obj.right.obj.obj (op U),
          ∃ C : FiniteSubalgebra B S hS Y.1 Y.2 A.obj,
            x ∈ Set.range ((C.obj.arrow.right.hom.app (op U)).hom))
    (hstage : ∀ C : QuasicoherentAlgebra B S hS Y,
      IsQuasiCompactSpace B S hS Y.obj →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.obj →
      C.obj.IsFinite →
        ∃ (ℬ : AlgebraSheaf.{u, u} B S hS Y.1 Y.2) (f : ℬ ⟶ C.obj) (J : Type u)
          (inst : SmallCategory J),
          let _ := inst
          ∃ (_ : IsFiltered J) (ι : J → ℬ.IdealSheaf)
            (hι : ∀ j j' : J, (j ⟶ j') → ι j ≤ ι j')
            (hkill : ∀ (j : J) (U : (SmallEtale B S hS Y.1)ᵒᵖ) (a : ℬ.right.obj.obj U),
              a ∈ (ι j).obj U → (f.right.hom.app U).hom a = 0)
            (hqcoh : ∀ j, (ℬ.idealQuotient (ι j)).IsQuasicoherent),
            (∀ j, (ℬ.idealQuotient (ι j)).IsFinitePresentation) ∧
            (∃ j, (ℬ.idealQuotient (ι j)).IsIntegral) ∧
            Nonempty (IsColimit (Cocone.mk C
              (idealQuotientQcohCocone ℬ ι hι C f hkill hqcoh))))
    (hpres : ∀ T : QuasicoherentAlgebra B S hS Y, T.obj.IsFinite → T.obj.IsFinitePresentation →
      ∀ (J : Type (u + 1)) [SmallCategory J] [IsFiltered J]
        (Φ : J ⥤ QuasicoherentAlgebra B S hS Y) (c : Cocone Φ), IsColimit c →
        Stacks.FinitelyPresentableComposition.PresentableAlong T c) :
    ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ QuasicoherentAlgebra B S hS Y) (φ : D ⟶ (Functor.const I).obj A),
      Nonempty (IsColimit (Cocone.mk A φ)) ∧
      ∀ i, (D.obj i).obj.IsFinite ∧ (D.obj i).obj.IsFinitePresentation
```

## Tag 0853, a lemma

[Tag 0853](https://stacks.math.columbia.edu/tag/0853) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteTypeQuasicoherentSubobject_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectExtension.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectExtension.lean#L149). The attribute's comment: “submodules as subobjects, restriction to the open as étale module pullback”.

> **Stacks Project, Tag 0853.** Let `X` be a quasi-compact and quasi-separated algebraic
> space, `U ⊂ X` a quasi-compact open, `ℱ` a quasi-coherent `𝒪_X`-module and `𝒢 ⊂ ℱ|_U` a
> quasi-coherent `𝒪_U`-submodule of finite type.  Then there is a quasi-coherent submodule
> `𝒢' ⊂ ℱ` of finite type with `𝒢'|_U = 𝒢`, the equality being an isomorphism of `𝒢'|_U` with
> `𝒢` commuting with the inclusions into `ℱ|_U`.

```lean
theorem exists_finiteTypeQuasicoherentSubobject_extension (j : U ⟶ X)
    (hj : IsOpenImmersion B S hS j.hom)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (G : Subobject ((etaleModulePullback.{u, u} B S hS j
      (isEtale_of_isOpenImmersion B S hS hj)).obj F))
    [(G : Modules.{u, u} B S hS U.1 U.2).IsQuasicoherentOnSite]
    [(G : Modules.{u, u} B S hS U.1 U.2).IsFiniteType] :
    ∃ G' : Subobject F, (G' : Modules.{u, u} B S hS X.1 X.2).IsQuasicoherentOnSite ∧
      (G' : Modules.{u, u} B S hS X.1 X.2).IsFiniteType ∧
      ∃ e : (etaleModulePullback.{u, u} B S hS j
            (isEtale_of_isOpenImmersion B S hS hj)).obj
          (G' : Modules.{u, u} B S hS X.1 X.2) ≅ (G : Modules.{u, u} B S hS U.1 U.2),
        (etaleModulePullback.{u, u} B S hS j
            (isEtale_of_isOpenImmersion B S hS hj)).map G'.arrow = e.hom ≫ G.arrow
```

**`AlgebraicGeometry.Space.exists_etaleSubmodule_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectExtensionQcqs.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeQuasicoherentSubobjectExtensionQcqs.lean#L81).

> **Stacks 0853.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S`,
> `U ⊆ X` a quasi-compact open subspace, `ℱ` a quasi-coherent `𝒪_X`-module and `𝒢 ⊆ ℱ|_U` a
> quasi-coherent `𝒪_U`-submodule of finite type.  Then there is a quasi-coherent submodule
> `𝒢' ⊆ ℱ` of finite type with `𝒢'|_U = 𝒢`.

```lean
theorem exists_etaleSubmodule_extension (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U : Subfunctor X.1) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (G : ((etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS U hU)
      (isEtale_openSubspaceHom B S hS U hU)).obj F).Submodule)
    (hGq : G.toSheafOfModules.IsQuasicoherentOnSite) (hGf : G.toSheafOfModules.IsFiniteType) :
    ∃ G' : F.Submodule, G'.toSheafOfModules.IsQuasicoherentOnSite ∧
      G'.toSheafOfModules.IsFiniteType ∧
      etaleSubmoduleRestrict B S hS _ (isEtale_openSubspaceHom B S hS U hU) G' = G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.9, Tag 07V8](https://stacks.math.columbia.edu/tag/07V8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
