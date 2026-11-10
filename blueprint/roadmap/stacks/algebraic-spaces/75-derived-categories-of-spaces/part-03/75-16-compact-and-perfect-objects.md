---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isCompactObject_iff_isPerfect, AlgebraicGeometry.Space.triangEnvelope_eq_isPerfect_of_isWeakTriangulatedGenerator, AlgebraicGeometry.Space.exists_isPerfect_isWeakTriangulatedGenerator_triangEnvelope_eq, AlgebraicGeometry.Space.isCompactObject_iff_isPerfect_of_supported, AlgebraicGeometry.Space.triangEnvelope_singleton_eq_isPerfect_of_supported, AlgebraicGeometry.Space.exists_isPerfect_comp_tensor_eq_zero_of_cohomologySupportedOn
statement: formalized
proof: formalized
---

# 75.16 Compact and perfect objects

Section 75.16 of the Stacks Project, [Tag 09M7](https://stacks.math.columbia.edu/tag/09M7). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09M8, a proposition

[Tag 09M8](https://stacks.math.columbia.edu/tag/09M8) in the Stacks Project.

**`AlgebraicGeometry.Space.isCompactObject_iff_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectCompactQcqs.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectCompactQcqs.lean#L156).

> **Stacks 09M8.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S`. An
> object of `D_QCoh(𝒪_X)` is compact if and only if it is perfect.

```lean
theorem isCompactObject_iff_isPerfect (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    IsCompactObject.{u} E ↔ (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E.obj
```

## Tag 0GFC, a remark

[Tag 0GFC](https://stacks.math.columbia.edu/tag/0GFC) in the Stacks Project.

**`AlgebraicGeometry.Space.triangEnvelope_eq_isPerfect_of_isWeakTriangulatedGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectClassicalGenerator.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectClassicalGenerator.lean#L87).

> **Stacks 0GFC.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S`, and
> let `G` be a perfect object of `D(𝒪_X)` which is a generator of `D_QCoh(𝒪_X)`. Then `G` is a
> classical generator of `D_perf(𝒪_X)`: the triangulated envelope of `G` in `D_QCoh(𝒪_X)` — its
> closure under shifts, finite direct sums, extensions and direct summands — is exactly the property
> of being perfect.
>
> The source combines [Stacks, Tag 08F3] (direct sums in `D_QCoh(𝒪_X)`), [Stacks, Tag 09M8]
> (compact equals perfect) and [Stacks, Tag 09SR] (a compact generator classically generates the
> compact objects). Such a `G` exists by [Stacks, Tag 09IY]; see
> `AlgebraicGeometry.Space.exists_isPerfect_isWeakTriangulatedGenerator_triangEnvelope_eq`.

```lean
theorem triangEnvelope_eq_isPerfect_of_isWeakTriangulatedGenerator (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (G : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (hG : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect G.obj)
    (hgen : (ObjectProperty.singleton G).IsWeakTriangulatedGenerator) :
    (ObjectProperty.singleton G).triangEnvelope =
      fun E => (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E.obj
```

**`AlgebraicGeometry.Space.exists_isPerfect_isWeakTriangulatedGenerator_triangEnvelope_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectClassicalGenerator.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectClassicalGenerator.lean#L109). The attribute's comment: “the existence of a perfect generator G of D\_QCoh(O\_X), by 09IY”.

> **Stacks 0GFC, the existence clause.** On a quasi-compact and quasi-separated algebraic space
> `X` over `S` there is a perfect object `G` of `D(𝒪_X)` which is a generator of `D_QCoh(𝒪_X)`
> ([Stacks, Tag 09IY]), and every such `G` is a classical generator of `D_perf(𝒪_X)`: its
> triangulated envelope in `D_QCoh(𝒪_X)` is the property of being perfect. The generator is the
> compact generator of `exists_isCompactObject_isWeakTriangulatedGenerator_of_qcqs`, perfect by
> [Stacks, Tag 09M8], exactly as in the proof of `exists_isPerfect_generator`.

```lean
theorem exists_isPerfect_isWeakTriangulatedGenerator_triangEnvelope_eq
    (X : AlgebraicSpaces B S hS) (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) :
    ∃ G : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect G.obj ∧
        (ObjectProperty.singleton G).IsWeakTriangulatedGenerator ∧
          (ObjectProperty.singleton G).triangEnvelope =
            fun E => (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E.obj
```

## Tag 0AED, a lemma

[Tag 0AED](https://stacks.math.columbia.edu/tag/0AED) in the Stacks Project.

**`AlgebraicGeometry.Space.isCompactObject_iff_isPerfect_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedCompactPerfect.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedCompactPerfect.lean#L77).

> **Stacks 0AED.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S`, and `T ⊆ |X|` a closed subset such that `|X| ∖ T` is quasi-compact. An object of
> `D_{QCoh,T}(𝒪_X)` is compact (in `D_{QCoh,T}(𝒪_X)`) if and only if it is perfect as an object of
> `D(𝒪_X)`.
>
> `D_{QCoh,T}(𝒪_X)` is the full subcategory of `D_QCoh(𝒪_X)` of the objects whose cohomology
> sheaves are supported on `T` (`AlgebraicGeometry.Space.quasicoherentDerivedSupportedOn`, with
> support as in Stacks 08GF); compactness is `CategoryTheory.IsCompactObject` (Stacks 07LS) in that
> category, for direct sums indexed by the universe `u` of the site.

```lean
theorem isCompactObject_iff_isPerfect_of_supported (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (T : Set (points B S hS X.1)) (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (E : (quasicoherentDerivedSupportedOn X T).FullSubcategory) :
    IsCompactObject.{u} E ↔ (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E.obj.obj
```

## Tag 0GFD, a remark

[Tag 0GFD](https://stacks.math.columbia.edu/tag/0GFD) in the Stacks Project.

**`AlgebraicGeometry.Space.triangEnvelope_singleton_eq_isPerfect_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectClassicalGenerator.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectClassicalGenerator.lean#L71).

> Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space over `S`, and
> `T ⊆ |X|` a closed subset such that `|X| ∖ T` is quasi-compact. Let `G` be a perfect object of
> `D(𝒪_X)` lying in `D_{QCoh,T}(𝒪_X)` (quasi-coherent cohomology sheaves supported on `T`) which is
> a generator of `D_{QCoh,T}(𝒪_X)`: an object `E` of `D_QCoh(𝒪_X)` supported on `T` with
> `Hom(G[n], E) = 0` for all `n ∈ ℤ` is zero. Then `G` is a classical generator of
> `D_{perf,T}(𝒪_X)`: the triangulated envelope of `G` in `D_{QCoh,T}(𝒪_X)` — the smallest strictly
> full, saturated, triangulated subcategory containing `G` — is exactly the property of being
> perfect in `D(𝒪_X)`.

```lean
theorem triangEnvelope_singleton_eq_isPerfect_of_supported (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (T : Set (points B S hS X.1)) (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (G : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hG : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect G)
    (hGq : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) G)
    (hGs : CohomologySupportedOn B S hS X.1 X.2 T G)
    (hgen : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      CohomologySupportedOn B S hS X.1 X.2 T E.obj →
        (∀ (n : ℤ) (g : G⟦n⟧ ⟶ E.obj), g = 0) → IsZero E.obj) :
    (ObjectProperty.singleton
        (⟨⟨G, hGq⟩, hGs⟩ : (quasicoherentDerivedSupportedOn X T).FullSubcategory)).triangEnvelope =
      fun K => (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect K.obj.obj
```

## Tag 0AEE, a lemma

[Tag 0AEE](https://stacks.math.columbia.edu/tag/0AEE) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_comp_tensor_eq_zero_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectAnnihilator.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectAnnihilator.lean#L182).

> **Stacks 0AEE.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S`, and `T ⊆ |X|` a closed subset whose complement `U` is quasi-compact. Let `α : P ⟶ E` be a
> morphism of `D_QCoh(𝒪_X)` with `E` supported on `T`, where either (1) `P` is perfect, or (2) `P`
> is pseudo-coherent and `E` is bounded below. Then there are a perfect complex `I` of
> `𝒪_X`-modules and a map `u : I ⟶ 𝒪_X[0]` such that `u|_U : I|_U ⟶ 𝒪_U[0]` is an isomorphism and
> `I ⊗^L P ⟶ 𝒪_X[0] ⊗^L P ≅ P ⟶ E` is zero.
>
> `U` is the open subspace of `X` with `|U| = |X| ∖ T`, and `(-)|_U` the restriction along its
> inclusion; `E` supported on `T` means that every cohomology sheaf of `E` is supported on `T`
> (`AlgebraicGeometry.Space.CohomologySupportedOn`, Stacks 08GF); `E` bounded below means that its
> cohomology sheaves vanish in all sufficiently negative degrees.

```lean
theorem exists_isPerfect_comp_tensor_eq_zero_of_cohomologySupportedOn
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (T : Set (points B S hS X.1)) (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    {P E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)}
    (hPq : QcohDerived B S hS X P) (hEq : QcohDerived B S hS X E) (α : P ⟶ E)
    (hEs : CohomologySupportedOn B S hS X.1 X.2 T E)
    (h : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P ∨
      ((smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent P ∧
        DerivedCategoryB.IsBoundedBelow E)) :
    ∃ (I : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (u : I ⟶ unitDerived X),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect I ∧
      IsIso ((etaleModulePullback.{u, u} B S hS
          (openSubspaceHom B S hS
            ((openSubspacesOrderIso B S hS X.1 X.2).symm ⟨Tᶜ, hT.isOpen_compl⟩).1
            ((openSubspacesOrderIso B S hS X.1 X.2).symm ⟨Tᶜ, hT.isOpen_compl⟩).2)
          (isEtale_openSubspaceHom B S hS _ _)).mapDerivedCategory.map u) ∧
      ((smallEtaleDerivedTensorProduct B S hS X).tensor.map u).app P ≫
        (smallEtaleDerivedTensorUnitLeftIso B S hS X P).hom ≫ α = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.16, Tag 09M7](https://stacks.math.columbia.edu/tag/09M7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
