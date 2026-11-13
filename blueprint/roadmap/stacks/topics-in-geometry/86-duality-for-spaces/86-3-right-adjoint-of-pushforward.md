---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isLeftAdjoint_quasicoherentDerivedPushforward, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjoint_boundedBelow, AlgebraicGeometry.Space.smallEtalePushforwardTrace, AlgebraicGeometry.Space.smallEtalePushforwardTrace_eq, AlgebraicGeometry.Space.isIso_coherator_map_smallEtalePushforwardTrace, AlgebraicGeometry.Space.UncoheratedTrace.coherator_cannot_be_dropped, AlgebraicGeometry.Space.coheratorPushforwardSheafHomIso, AlgebraicGeometry.Space.isIso_coherator_counit_pushforward_sheafHom
statement: formalized
proof: formalized
---

# 86.3 Right adjoint of pushforward

Section 86.3 of the Stacks Project, [Tag 0E54](https://stacks.math.columbia.edu/tag/0E54). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E55, a lemma

[Tag 0E55](https://stacks.math.columbia.edu/tag/0E55) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isLeftAdjoint_quasicoherentDerivedPushforward`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CompactGeneration/QcqsCompactGeneration.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CompactGeneration/QcqsCompactGenerationRegistration.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CompactGeneration/QcqsCompactGenerationRegistration.lean#L18) (StacksFrontier).

## Tag 0E56, a lemma

[Tag 0E56](https://stacks.math.columbia.edu/tag/0E56) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjoint_boundedBelow`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBoundedBelow.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean#L32) (StacksFrontier).

## Tag 0E57, an equation

[Tag 0E57](https://stacks.math.columbia.edu/tag/0E57) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtalePushforwardTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean#L88).

> For a morphism `f : X ⟶ Y` of quasi-compact and quasi-separated algebraic spaces with right
> adjoint `a` of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, and `L` in `D_QCoh(𝒪_X)`, `K` in
> `D_QCoh(𝒪_Y)`, the canonical map `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)`: the map
> `smallEtaleDerivedSheafHomPushforwardMap` followed by `R𝓗om(Rf_*L, -)` of the counit
> `Rf_*a(K) ⟶ K`.
>
> Here `a` is `quasicoherentDerivedRightAdjoint`, the right adjoint of the restricted functor
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` given by [Stacks, Tag 0E55], and the second arrow is the
> counit of that adjunction on `D_QCoh`; the first arrow is the map of [Stacks, Tag 0B6D],
> adjoint to the relative cup product followed by `Rf_*` of the evaluation.

```lean
def smallEtalePushforwardTrace (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    (derivedModulePushforward B S hS f).obj
        (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj) ⟶
      ((smallEtaleDerivedSheafHom B S hS Y).obj
        (op ((derivedModulePushforward B S hS f).obj L.obj))).obj K.obj
```

**`AlgebraicGeometry.Space.smallEtalePushforwardTrace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean#L108). The attribute's comment: “the defining composition”.

> The trace map is `smallEtaleDerivedSheafHomPushforwardMap` followed by `R𝓗om(Rf_*L, -)` of
> the counit of the adjunction `Rf_* ⊣ a` on `D_QCoh`.

```lean
theorem smallEtalePushforwardTrace_eq (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    smallEtalePushforwardTrace hZ f hXqc hXqs hYqs L K =
      smallEtaleDerivedSheafHomPushforwardMap f L.obj
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj ≫
        ((smallEtaleDerivedSheafHom B S hS Y).obj
          (op ((derivedModulePushforward B S hS f).obj L.obj))).map
          ((quasicoherentDerivedRightAdjointAdjunction hZ f hXqc hXqs hYqs
            (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y.2 hYqs hXqc f.hom)
            (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X.2 hXqs
              f.hom)).counit.app K).hom
```

## Tag 0E58, a lemma

[Tag 0E58](https://stacks.math.columbia.edu/tag/0E58) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_coherator_map_smallEtalePushforwardTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTrace.lean#L126).

> Let `f : X ⟶ Y` be a morphism of quasi-compact and quasi-separated algebraic spaces, `a` the
> right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, `L` in `D_QCoh(𝒪_X)` and `K` in
> `D_QCoh(𝒪_Y)`. Then the trace map `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)` becomes an isomorphism
> after applying any right adjoint `DQ_Y` of the inclusion `D_QCoh(𝒪_Y) ⟶ D(𝒪_Y)`.

```lean
theorem isIso_coherator_map_smallEtalePushforwardTrace
    {DQ : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2}
    (adjQ : (QcohDerived B S hS Y).ι ⊣ DQ)
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    IsIso (DQ.map (smallEtalePushforwardTrace hZ f hXqc hXqs hYqs L K))
```

## Tag 0GG3, an example

[Tag 0GG3](https://stacks.math.columbia.edu/tag/0GG3) in the Stacks Project.

**`AlgebraicGeometry.Space.UncoheratedTrace.coherator_cannot_be_dropped`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityCoheratorNecessary.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityCoheratorNecessary.lean#L286). The attribute's comment: “the counterexample of 0GEU on algebraic spaces: for f : A^1\_S -> S with S affine carrying t with no t^j = t^(j+1) b (S = Spec Z, t = 2), L = O\_X, K = O\_Y, the left side of the 0E57 map lies in D\_QCoh, the right side has H^0 the non-quasi-coherent product of copies of O\_Y, and no map between them is an isomorphism, for every right adjoint a”.

> The statement of [Stacks, Tag 0E58] is not true without the coherator `DQ_Y`. Let `S` be an
> affine scheme of the big fppf site with a regular function `t` admitting no equation
> `t^j = t^{j+1} b` (for instance `S = Spec ℤ`, `t = 2`), let `Y = h_S`, `X = h_{𝔸¹_S}`,
> `f : X ⟶ Y` the structure morphism, `L = 𝒪_X` and `K = 𝒪_Y`. Then:
>
> 1. `X` and `Y` are quasi-compact and quasi-separated algebraic spaces;
> 2. `Rf_*` sends `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_Y)`, and `L`, `K` lie in `D_QCoh`;
> 3. the left hand side `Rf_*R𝓗om_{𝒪_X}(L, M)` lies in `D_QCoh(𝒪_Y)` for every `M` in
>    `D_QCoh(𝒪_X)`, in particular for `M = a(K)`;
> 4. the right hand side `R𝓗om_{𝒪_Y}(Rf_*L, K)` has zeroth cohomology sheaf `∏_{n ≥ 0} 𝒪_Y`,
>    which is not quasi-coherent, so the right hand side is not in `D_QCoh(𝒪_Y)`;
> 5. hence, for every right adjoint `a` of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, no morphism
>    `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)` — the map (0E57) in particular — is an
>    isomorphism.

```lean
theorem coherator_cannot_be_dropped (hZ : B.Contains (⊤_ Scheme.{u})) (t : Γ(S, ⊤))
    (ht : ∀ (j : ℕ) (b : Γ(S, ⊤)), t ^ j ≠ t ^ (j + 1) * b) :
    (IsQuasiCompactSpace B S hS (affineLineAlgebraicSpace B S hS).1 ∧
      IsAbsolutelyQuasiSeparated B S hS hZ (affineLineAlgebraicSpace B S hS).1 ∧
      IsQuasiCompactSpace B S hS (affineBaseSpace B S hS).1 ∧
        IsAbsolutelyQuasiSeparated B S hS hZ (affineBaseSpace B S hS).1) ∧
    PreservesQuasicoherentDerived Rf ∧
    quasicoherentDerivedProperty (affineLineAlgebraicSpace B S hS)
      (structureSheafDerived B S hS (affineLineAlgebraicSpace B S hS)) ∧
    quasicoherentDerivedProperty (affineBaseSpace B S hS)
      (structureSheafDerived B S hS (affineBaseSpace B S hS)) ∧
    (∀ M : DerivedCategory (Modules.{u, u} B S hS (affineLineAlgebraicSpace B S hS).1
      (affineLineAlgebraicSpace B S hS).2),
      quasicoherentDerivedProperty (affineLineAlgebraicSpace B S hS) M →
        quasicoherentDerivedProperty (affineBaseSpace B S hS) (traceSource B S hS Rf M)) ∧
    Nonempty ((DerivedCategory.homologyFunctor _ 0).obj (traceTarget B S hS Rf) ≅
      piUnit (affineBaseSpace B S hS).2) ∧
    ¬ (piUnit (affineBaseSpace B S hS).2).IsQuasicoherentOnSite ∧
    ¬ quasicoherentDerivedProperty (affineBaseSpace B S hS) (traceTarget B S hS Rf) ∧
    ∀ (a : QuasicoherentDerivedCategoryOfModel (affineBaseSpace B S hS) ⥤
      QuasicoherentDerivedCategoryOfModel (affineLineAlgebraicSpace B S hS))
      (_ : liftQuasicoherentDerived Rf (preservesQuasicoherentDerived B S hS Rf α) ⊣ a)
      (φ : traceSource B S hS Rf
          (a.obj ⟨structureSheafDerived B S hS (affineBaseSpace B S hS),
            structureSheafDerived_mem B S hS (affineBaseSpace B S hS)⟩).obj ⟶
        traceTarget B S hS Rf),
      ¬ IsIso φ
```

## Tag 0GG4, a remark

[Tag 0GG4](https://stacks.math.columbia.edu/tag/0GG4) in the Stacks Project.

**`AlgebraicGeometry.Space.coheratorPushforwardSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L60). The attribute's comment: “the identification of the coherators by Stacks 0CR5”.

> **Stacks 0GG4, the identification of the coherators.** For right adjoints `DQ_X`, `DQ_Y` of
> the inclusions `D_QCoh ⟶ D`, `DQ_Y(Rf_*R𝓗om(L, a(K))) ≅ Rf_*DQ_X(R𝓗om(L, a(K)))` (Stacks 0CR5).

```lean
def coheratorPushforwardSheafHomIso
    {DQX : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2}
    {DQY : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2}
    (adjX : (QcohDerived B S hS X).ι ⊣ DQX) (adjY : (QcohDerived B S hS Y).ι ⊣ DQY)
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    DQY.obj ((derivedModulePushforward B S hS f).obj
        (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj)) ≅
      (quasicoherentDerivedPushforward B S hS f
          (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y.2 hYqs hXqc f.hom)
          (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X.2 hXqs f.hom)).obj
        (DQX.obj (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj))
```

**`AlgebraicGeometry.Space.isIso_coherator_counit_pushforward_sheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L85). The attribute's comment: “erasing the coherator on the source of the map of Stacks 0E58”.

> **Stacks 0GG4, erasing the coherator on the source.** If `R𝓗om(L, a(K))` has
> quasi-coherent cohomology, then `DQ_Y(Rf_*R𝓗om(L, a(K))) ⟶ Rf_*R𝓗om(L, a(K))` is an
> isomorphism.

```lean
theorem isIso_coherator_counit_pushforward_sheafHom
    {DQ : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2}
    (adjQ : (QcohDerived B S hS Y).ι ⊣ DQ)
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (h : QcohDerived B S hS X (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
      ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj)) :
    IsIso (adjQ.counit.app ((derivedModulePushforward B S hS f).obj
      (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
        ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj)))
```

**`AlgebraicGeometry.Space.isIso_coherator_counit_sheafHom_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L104). The attribute's comment: “erasing the coherator on the target of the map of Stacks 0E58”.

> **Stacks 0GG4, erasing the coherator on the target.** If `R𝓗om(Rf_*L, K)` has
> quasi-coherent cohomology, then `DQ_Y(R𝓗om(Rf_*L, K)) ⟶ R𝓗om(Rf_*L, K)` is an isomorphism.

```lean
theorem isIso_coherator_counit_sheafHom_pushforward
    {DQ : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2}
    (adjQ : (QcohDerived B S hS Y).ι ⊣ DQ)
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (h : QcohDerived B S hS Y (((smallEtaleDerivedSheafHom B S hS Y).obj
      (op ((derivedModulePushforward B S hS f).obj L.obj))).obj K.obj)) :
    IsIso (adjQ.counit.app (((smallEtaleDerivedSheafHom B S hS Y).obj
      (op ((derivedModulePushforward B S hS f).obj L.obj))).obj K.obj))
```

**`AlgebraicGeometry.Space.isIso_smallEtalePushforwardTrace_of_qcohDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L121). The attribute's comment: “the map of Stacks 0E57 is an isomorphism if both sides have quasi-coherent cohomology”.

> **Stacks 0GG4, the quasi-coherence criterion.** If `R𝓗om(L, a(K))` and `R𝓗om(Rf_*L, K)` both
> have quasi-coherent cohomology, then the map `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)` of
> Stacks 0E57 is an isomorphism.

```lean
theorem isIso_smallEtalePushforwardTrace_of_qcohDerived
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hA : QcohDerived B S hS X (((smallEtaleDerivedSheafHom B S hS X).obj (op L.obj)).obj
      ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K).obj))
    (hB : QcohDerived B S hS Y (((smallEtaleDerivedSheafHom B S hS Y).obj
      (op ((derivedModulePushforward B S hS f).obj L.obj))).obj K.obj)) :
    IsIso (smallEtalePushforwardTrace hZ f hXqc hXqs hYqs L K)
```

**`AlgebraicGeometry.Space.isIso_smallEtalePushforwardTrace_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L140). The attribute's comment: “(1)”.

> **Stacks 0GG4 (1).** If `L` and `Rf_*L` are perfect, then the map
> `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)` of Stacks 0E57 is an isomorphism.

```lean
theorem isIso_smallEtalePushforwardTrace_of_isPerfect
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hL : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) L.obj)
    (hfL : RingedSite.IsPerfect (smallEtaleRingedSite B S hS Y.1 Y.2)
      ((derivedModulePushforward B S hS f).obj L.obj)) :
    IsIso (smallEtalePushforwardTrace hZ f hXqc hXqs hYqs L K)
```

**`AlgebraicGeometry.Space.isIso_smallEtalePushforwardTrace_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceCriterion.lean#L156). The attribute's comment: “(2)”.

> **Stacks 0GG4 (2).** If `K` is bounded below and `L` and `Rf_*L` are pseudo-coherent, then
> the map `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)` of Stacks 0E57 is an isomorphism.

```lean
theorem isIso_smallEtalePushforwardTrace_of_isPseudoCoherent
    (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hK : DerivedCategoryB.IsBoundedBelow K.obj)
    (hL : RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) L.obj)
    (hfL : RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS Y.1 Y.2)
      ((derivedModulePushforward B S hS f).obj L.obj)) :
    IsIso (smallEtalePushforwardTrace hZ f hXqc hXqs hYqs L K)
```

## Tag 0GG5, an example

[Tag 0GG5](https://stacks.math.columbia.edu/tag/0GG5) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtalePushforwardTrace_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceProper.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPushforwardTraceProper.lean#L107).

> **Stacks 0GG5.** Let `f : X ⟶ Y` be a proper morphism of Noetherian algebraic spaces over
> `S`, `L` in `D^-_Coh(𝒪_X)` and `K` in `D^+_QCoh(𝒪_Y)`. Then the map
> `Rf_*R𝓗om(L, a(K)) ⟶ R𝓗om(Rf_*L, K)` of Stacks 0E57 is an isomorphism.

```lean
theorem isIso_smallEtalePushforwardTrace_of_isProper (hf : IsProper B S hS f.hom)
    (hX : IsNoetherian B S hS hZ X.1) (hY : IsNoetherian B S hS hZ Y.1)
    (L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hL : DerivedCategoryB.derivedCategoryBMinus (isCoherent.{u, u} B S hS X.1 X.2) L)
    (K : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))) K) :
    IsIso (smallEtalePushforwardTrace hZ f hX.1 hX.2.1 hY.2.1
      ⟨L, fun i => (hL.2 i).toIsQuasicoherentOnSite⟩ ⟨K, hK.2⟩)
```

## Tag 0E59, a lemma

[Tag 0E59](https://stacks.math.columbia.edu/tag/0E59) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_globalDerivedHomTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityGlobalDerivedHomTrace.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityGlobalDerivedHomTrace.lean#L201).

> **Stacks 0E59.** Let `f : X ⟶ Y` be a morphism of quasi-separated and quasi-compact algebraic
> spaces. For all `L` in `D_QCoh(𝒪_X)` and `K` in `D_QCoh(𝒪_Y)` the map of Stacks 0E57 induces an
> isomorphism `RHom_X(L, a(K)) ⟶ RHom_Y(Rf_*L, K)` of global derived homs.

```lean
theorem isIso_globalDerivedHomTrace (L : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    IsIso (globalDerivedHomTrace hZ f hXqc hXqs hYqs L K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.3, Tag 0E54](https://stacks.math.columbia.edu/tag/0E54)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
