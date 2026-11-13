---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.DerivedExistenceSystem, AlgebraicGeometry.Space.DerivedExistenceSystem.derivedLimit_isBoundedAbove, AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange, AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherentOnLimit_quasicoherentDerivedLimit, AlgebraicGeometry.Space.DerivedExistenceSystem.isIso_etaleSectionsBaseChangeMap, AlgebraicGeometry.Space.DerivedExistenceSystem.exists_isPseudoCoherent_stageDerivedPullback_iso, AlgebraicGeometry.Space.SupportedDerivedExistenceSystem, AlgebraicGeometry.Space.SupportedDerivedExistenceSystem.exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso_isProperOver_supportOfSheaf
statement: formalized
proof: formalized
---

# 77.13 Grothendieck's Existence Theorem, bis

Section 77.13 of the Stacks Project, [Tag 0DIJ](https://stacks.math.columbia.edu/tag/0DIJ). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DIK, a situation

[Tag 0DIK](https://stacks.math.columbia.edu/tag/0DIK) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSystem.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSystem.lean#L108). The attribute's comment: “the situation as stated, with the derived pullback along each Xₙ → Xₙ₊₁ constructed by Stacks 06YY; its fields are the data and hypotheses of the source, together with a big fppf site containing Spec A and every Spec Aₙ in which the algebraic spaces are taken”.

> The standing data of Grothendieck's existence theorem for algebraic spaces in its derived
> form: an inverse system of rings `(Aₙ)` with surjective transitions whose kernels are locally
> nilpotent, an algebraic space `X` proper, flat and of finite presentation over `A = lim Aₙ`, and
> pseudo-coherent objects `Kₙ` of `D(𝒪_{Xₙ})` on the infinitesimal base changes
> `Xₙ = X ×_{Spec A} Spec Aₙ`, with maps `Liₙ^* Kₙ₊₁ ⟶ Kₙ` that are isomorphisms, `Liₙ^*` being
> the derived pullback along `Xₙ ⟶ Xₙ₊₁` constructed in `transitionDerivedPullback`.

```lean
structure DerivedExistenceSystem
```

## Tag 0DIL, a lemma

[Tag 0DIL](https://stacks.math.columbia.edu/tag/0DIL) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.derivedLimit_isBoundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceBoundedLimit.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceBoundedLimit.lean#L139). The attribute's comment: “K = R lim\_\{D\_QCoh} K\_n = DQ\_X(R lim\_\{D(O\_X)} K\_n) lies in D^-\_QCoh(O\_X), for every choice of coherator and of derived limits”.

> In Situation 0DIK the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right adjoint `DQ_X` and the
> tower `(Rjₙ,* Kₙ)` has a derived limit `L = R lim_{D(𝒪_X)} Kₙ`. For every coherator `DQ_X` and
> every such `L`, `K = DQ_X(L)` is a derived limit of the tower in `D_QCoh(𝒪_X)` whose cohomology
> sheaves vanish above some degree. Every derived limit of the tower in `D_QCoh(𝒪_X)` lies in
> `D⁻_QCoh(𝒪_X)`.

```lean
theorem derivedLimit_isBoundedAbove :
    (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.IsLeftAdjoint ∧
    (∃ L, IsDerivedLimit D.toSeparated.spaceTower L) ∧
    (∀ (DQ : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left ⥤
        (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
          D.X.left).FullSubcategory)
      (_ : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι ⊣ DQ)
      (L : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left),
      IsDerivedLimit D.toSeparated.spaceTower L →
        (∃ _ : HasProduct fun n : ℕ => D.toSeparated.quasicoherentTower.obj ⟨n⟩,
          IsDerivedLimit D.toSeparated.quasicoherentTower (DQ.obj L)) ∧
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B (limitBase D.system) D.containsLimitBase
          D.X.left c ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
            D.X.left).ι.obj (DQ.obj L))) ∧
    ∀ (_ : HasProduct fun n : ℕ => D.toSeparated.quasicoherentTower.obj ⟨n⟩)
      (K : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
        D.X.left).FullSubcategory),
      IsDerivedLimit D.toSeparated.quasicoherentTower K →
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B (limitBase D.system) D.containsLimitBase
          D.X.left c ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
            D.X.left).ι.obj K)
```

## Tag 0DIM, a lemma

[Tag 0DIM](https://stacks.math.columbia.edu/tag/0DIM) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceTensorSectionsBaseChange.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceTensorSectionsBaseChange.lean#L392). The attribute's comment: “the full statement: for every perfect E, M = RΓ(X, E ⊗^L K) is pseudo-coherent and the canonical map M ⊗^L\_A Aₙ ⟶ RΓ(Xₙ, Lpₙ^*E ⊗^L Kₙ) is an isomorphism in D(Aₙ) for every n. D is Situation 0DIK (DerivedExistenceSystem), whose fields are only the situation's data and hypotheses: the rings Aₙ with surjective transitions with locally nilpotent kernels, the fppf site containing Spec A and every Spec Aₙ, X proper, flat and of finite presentation over A, the pseudo-coherent Kₙ, and the comparison isomorphisms Liₙ^* Kₙ₊₁ ≅ Kₙ; no result is a field. K = DQ\_X(R lim Kₙ) is the object of 0DIL, built from the coherator (the right adjoint of D\_QCoh(𝒪\_X) ⥤ D(𝒪\_X)) and a derived limit, both constructed and not assumed”.

> **[Stacks, Tag 0DIM].** In Situation 0DIK let `K = DQ_X(R lim Kₙ)` be the object of
> [Stacks, Tag 0DIL] and `E` a perfect object of `D(𝒪_X)`. Then `M = RΓ(X, E ⊗^L K)` is a
> pseudo-coherent object of `D(A)`, and for every `n` the canonical map
> `cₙ : M ⊗^L_A Aₙ ⟶ RΓ(Xₙ, Lpₙ^*E ⊗^L Kₙ)` (the base change map of `RΓ`, then Stacks 07A4 and
> `Lpₙ^*E ⊗^L τₙ`, with `τₙ : Lpₙ^*K ⟶ Kₙ` adjoint to the projection) is an isomorphism in
> `D(Aₙ)`. Here `K` is `D.quasicoherentLimit`, with `R lim Kₙ = D.derivedLimit` and `DQ_X` the
> right adjoint `D.coherator` of the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`.

```lean
theorem isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange (D : DerivedExistenceSystem.{u})
    (E : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left)
    (hE : spaceIsPerfect D.B (limitBase D.system) D.containsLimitBase D.X.left E) :
    StacksDraft.PseudoCoherence.IsPseudoCoherent
        ((D.toSeparated.limitTensorSections E).obj ((spaceQuasicoherentProp D.B (limitBase D.system)
          D.containsLimitBase D.X.left).ι.obj D.toSeparated.quasicoherentLimit)) ∧
      ∀ n : ℕ, IsIso (D.toSeparated.stageTensorSectionsBaseChange D.toSeparated.coherator
        D.toSeparated.coheratorAdjunction E n)
```

## Tag 0DIN, a lemma

[Tag 0DIN](https://stacks.math.columbia.edu/tag/0DIN) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherentOnLimit_quasicoherentDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistencePseudoCoherent.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistencePseudoCoherent.lean#L243). The attribute's comment: “the full statement: a coherator DQ\_X and a derived limit R lim\_\{D(O\_X)} K\_n exist, and for every such choice K = DQ\_X(R lim\_\{D(O\_X)} K\_n) is a derived limit R lim\_\{D\_QCoh} K\_n and is pseudo-coherent on X; every derived limit of the tower in D\_QCoh(O\_X) is pseudo-coherent on X”.

> **[Stacks, Tag 0DIN].** In Situation 0DIK the inclusion `ι : D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right
> adjoint `DQ_X` and the tower `(Rjₙ,* Kₙ)` has a derived limit `L = R lim_{D(𝒪_X)} Kₙ`. For every
> coherator `adj : ι ⊣ DQ_X` and every such `L`, the object `K = DQ_X(L)` is a derived limit
> `R lim_{D_QCoh(𝒪_X)} Kₙ` of the tower in `D_QCoh(𝒪_X)` and is pseudo-coherent on `X`. Moreover every
> derived limit of the tower in `D_QCoh(𝒪_X)` is pseudo-coherent on `X`.

```lean
theorem isPseudoCoherentOnLimit_quasicoherentDerivedLimit (D : DerivedExistenceSystem.{u}) :
    (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.IsLeftAdjoint ∧
    (∃ L, IsDerivedLimit D.toSeparated.spaceTower L) ∧
    (∀ (DQ : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left ⥤
        (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
          D.X.left).FullSubcategory)
      (_ : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι ⊣ DQ)
      (L : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left),
      IsDerivedLimit D.toSeparated.spaceTower L →
        (∃ _ : HasProduct fun n : ℕ => D.toSeparated.quasicoherentTower.obj ⟨n⟩,
          IsDerivedLimit D.toSeparated.quasicoherentTower (DQ.obj L)) ∧
        D.IsPseudoCoherentOnLimit
          ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.obj
            (DQ.obj L))) ∧
    ∀ (_ : HasProduct fun n : ℕ => D.toSeparated.quasicoherentTower.obj ⟨n⟩)
      (K : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
        D.X.left).FullSubcategory),
      IsDerivedLimit D.toSeparated.quasicoherentTower K →
        D.IsPseudoCoherentOnLimit
          ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.obj
            K)
```

## Tag 0DIP, a lemma

[Tag 0DIP](https://stacks.math.columbia.edu/tag/0DIP) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isIso_etaleSectionsBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceEtaleSectionsHocolim.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceEtaleSectionsHocolim.lean#L157). The attribute's comment: “in Situation 0DIK with K = DQ\_X(R lim K\_n) as in 0DIL: for every étale U → X with U qcqs and every n, the canonical map RΓ(U, K) ⊗^L\_A A\_n → RΓ(U\_n, K\_n) is an isomorphism in D(A\_n), U\_n = U ×\_X X\_n; the full statement, with 0CRW and 0DIM proved in the library”.

> In Situation 0DIK let `K = DQ_X(R lim Kₙ)` be the object of [Stacks, Tag 0DIL]
> (`AlgebraicGeometry.Space.SeparatedDerivedExistenceSystem.quasicoherentLimit` of
> `D.toSeparated`, for the coherator `DQ_X`
> right adjoint to `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`). For every étale `j : U ⟶ X` with `U`
> quasi-compact and quasi-separated and every `n`, the canonical map
> `RΓ(U, K) ⊗^L_A Aₙ ⟶ RΓ(Uₙ, Kₙ)` in `D(Aₙ)`, with `Uₙ = U ×_X Xₙ` (the base change map of `RΓ`
> along `Spec Aₙ ⟶ Spec A`, then `RΓ(Uₙ, -)` of `τₙ|_{Uₙ}`, with `τₙ : Lpₙ^*K ⟶ Kₙ` adjoint to the
> projection), is an isomorphism.

```lean
theorem isIso_etaleSectionsBaseChangeMap (D : DerivedExistenceSystem.{u})
    {U : AlgebraicSpaces D.B (limitBase D.system) D.containsLimitBase} (j : U ⟶ D.X.left)
    (hj : IsEtale D.B (limitBase D.system) D.containsLimitBase j.hom)
    (hUqc : IsQuasiCompactSpace D.B (limitBase D.system) D.containsLimitBase U.1)
    (hUqs : IsAbsolutelyQuasiSeparated D.B (limitBase D.system) D.containsLimitBase
      D.B.contains_terminal U.1) (n : ℕ) :
    IsIso (D.toSeparated.etaleSectionsBaseChangeMap j D.toSeparated.coherator
      D.toSeparated.coheratorAdjunction n)
```

## Tag 0DIQ, a theorem

[Tag 0DIQ](https://stacks.math.columbia.edu/tag/0DIQ) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.exists_isPseudoCoherent_stageDerivedPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceGrothendieck.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceGrothendieck.lean#L289). The attribute's comment: “the full statement in Situation 0DIK with no further hypotheses: a pseudo-coherent K on X with isomorphisms Lj\_n^* K = K\_n for all n, compatible with the phi\_n through the composition isomorphism of derived pullbacks”.

> **The derived Grothendieck existence theorem.** In Situation 0DIK there is a
> pseudo-coherent `K` in `D(𝒪_X)` with `Kₙ = K ⊗^L_{𝒪_X} 𝒪_{Xₙ}` for all `n`, compatibly with the
> maps `φₙ`: isomorphisms `ψₙ : Ljₙ^* K ≅ Kₙ` (`Ljₙ^*` the derived pullback along `jₙ : Xₙ ⟶ X`) with
> `ψₙ = (Ljₙ^* ≅ Liₙ^* Ljₙ₊₁^*) ≫ Liₙ^* ψₙ₊₁ ≫ φₙ`, where `Ljₙ^* ≅ Liₙ^* Ljₙ₊₁^*` is the composition
> isomorphism of derived pullbacks along `iₙ ≫ jₙ₊₁ = jₙ`.
>
> Proof as in the source: `K = DQ_X(R lim Kₙ)` is pseudo-coherent by [Stacks, Tag 0DIN] (from both
> halves of [Stacks, Tag 0DIM]), and the maps `τₙ : Ljₙ^* K ⟶ Kₙ` are isomorphisms by
> [Stacks, Tag 0DIP] over affine `U` étale over `X`, compatible with the `φₙ`.

```lean
theorem exists_isPseudoCoherent_stageDerivedPullback_iso (D : DerivedExistenceSystem.{u}) :
    ∃ (K : D.limitDerivedCategory) (ψ : ∀ n : ℕ, (D.stageDerivedPullback n).obj K ≅ D.K n),
      D.IsPseudoCoherentOnLimit K ∧
        ∀ n : ℕ, (ψ n).hom = (D.stageDerivedPullbackCompIso n).inv.app K ≫
          (transitionDerivedPullback D.system D.B D.containsLimitBase D.containsBaseAt D.X n).map
            (ψ (n + 1)).hom ≫ D.φ n
```

## Tag 0DIR, a remark

[Tag 0DIR](https://stacks.math.columbia.edu/tag/0DIR) in the Stacks Project.

**`AlgebraicGeometry.Space.SupportedDerivedExistenceSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupported.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupported.lean#L84). The attribute's comment: “the setting of the corrected remark: A = lim A\_n with surjective transitions and locally nilpotent kernels, X separated, flat and of finite presentation over A, K\_n pseudo-coherent on X\_n supported on a closed subset proper over A\_n, phi\_n isomorphisms; flatness is necessary, see the errata entry 0DIR(flatness dropped)”.

> **The data of the generalized derived existence theorem (Stacks 0DIR, `X` flat).** An inverse
> system of rings `(Aₙ)` with surjective transitions whose kernels are locally nilpotent, an
> algebraic space `X` separated, flat and of finite presentation over `A = lim Aₙ`, and
> pseudo-coherent `Kₙ ∈ D(𝒪_{Xₙ})` with isomorphisms `Liₙ^* Kₙ₊₁ ≅ Kₙ`, each `Kₙ` supported on a
> closed subset `Zₙ` of `|Xₙ|` proper over `Spec Aₙ`.

```lean
structure SupportedDerivedExistenceSystem extends SeparatedDerivedExistenceSystem.{u}
```

**`AlgebraicGeometry.Space.SupportedDerivedExistenceSystem.exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso_isProperOver_supportOfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupportedPerDegree.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupportedPerDegree.lean#L134). The attribute's comment: “corrected form, X flat: K pseudo-coherent relative to A, Lj\_n^* K = K\_n compatibly with the phi\_n, and each cohomology sheaf of K supported on a closed subset proper over A; the one-subset support clause and the case of non-flat X are false (errata 0DIR)”.

> **Grothendieck's existence theorem in its derived form, with supports proper over the base
> (Stacks 0DIR, `X` flat over `A`, the per-degree support clause).** There is `K ∈ D(𝒪_X)`,
> pseudo-coherent relative to `A`, with isomorphisms `ψₙ : Ljₙ^* K ≅ Kₙ` such that
> `ψₙ = (Ljₙ^* ≅ Liₙ^* Ljₙ₊₁^*) ≫ Liₙ^* ψₙ₊₁ ≫ φₙ`, and such that for every `i` the support of the
> cohomology sheaf `Hⁱ(K)` lies in a closed subset of `|X|` proper over `Spec A`. The source's
> clause that the whole of `K` is supported on one closed subset proper over `A` fails (see the
> module `StacksFrontier.AlgebraicGeometry.Spaces.Deformations.DerivedExistenceSupported`); this is
> the per-degree form, which holds.

```lean
theorem exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso_isProperOver_supportOfSheaf :
    ∃ (K : D.limitDerivedCategory)
      (ψ : ∀ n : ℕ, (D.stageDerivedPullback n).obj K ≅ D.K n)
      (hK : QcohDerived D.B (limitBase D.system) D.containsLimitBase D.X.left K),
      IsRelativelyPseudoCoherent D.B (limitBase D.system) D.containsLimitBase D.X.left.1
          D.X.left.2 D.X.hom.hom
          (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
            D.containsLimitBase D.finitePresentation.1) ⟨K, hK⟩ ∧
        (∀ n : ℕ, (ψ n).hom = (D.stageDerivedPullbackCompIso n).inv.app K ≫
          (transitionDerivedPullback D.system D.B D.containsLimitBase D.containsBaseAt D.X n).map
            (ψ (n + 1)).hom ≫ D.φ n) ∧
        ∀ i : ℤ, ∃ (T : Set (points D.B (limitBase D.system) D.containsLimitBase D.X.left.1))
          (hT : IsClosed T),
          IsProperOver D.B (limitBase D.system) D.containsLimitBase D.X.left.2
              (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2 D.X.hom.hom
              (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
                D.containsLimitBase D.finitePresentation.1) T hT ∧
            supportOfSheaf D.B (limitBase D.system) D.containsLimitBase D.X.left.1
              ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf
                (smallEtaleRingedSite D.B (limitBase D.system) D.containsLimitBase D.X.left.1
                  D.X.left.2).O)).obj
                ((DerivedCategory.homologyFunctor (Modules.{u, u} D.B (limitBase D.system)
                  D.containsLimitBase D.X.left.1 D.X.left.2) i).obj K)) ⊆ T
```

**`AlgebraicGeometry.Space.RelativeDerivedExistenceSystem.exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso_isProperOver_supportOfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupportedPerDegree.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSupportedPerDegree.lean#L185). The attribute's comment: “corrected form on the remark's own data (X separated, of finite presentation, K\_n pseudo-coherent relative to A\_n, supported on closed subsets proper over A\_n) with X flat: K pseudo-coherent relative to A, Lj\_n^* K = K\_n compatibly, each cohomology sheaf of K supported on a closed subset proper over A; flatness is necessary and one closed subset for all of K fails (errata 0DIR)”.

> **The generalized derived existence theorem for the data of Stacks 0DIR, `X` flat over `A`,
> with the per-degree support clause.** Let `(Aₙ)`, `X` separated and of finite presentation over
> `A = lim Aₙ`, and `Kₙ ∈ D_QCoh(𝒪_{Xₙ})` pseudo-coherent relative to `Aₙ`, supported on closed
> subsets of `|Xₙ|` proper over `Aₙ`, with isomorphisms `φₙ : Liₙ^* Kₙ₊₁ ≅ Kₙ`, be as in the
> remark, and let `X` be flat over `A`. Then there is `K ∈ D_QCoh(𝒪_X)`, pseudo-coherent relative
> to `A`, with isomorphisms `ψₙ : Ljₙ^* K ≅ Kₙ` such that
> `ψₙ = (Ljₙ^* ≅ Liₙ^* Ljₙ₊₁^*) ≫ Liₙ^* ψₙ₊₁ ≫ φₙ`, and such that for every `i` the support of
> `Hⁱ(K)` lies in a closed subset of `|X|` proper over `Spec A`.

```lean
theorem exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso_isProperOver_supportOfSheaf
    (hflat : IsFlat D.B (limitBase D.system) D.containsLimitBase D.X.hom.hom) :
    ∃ (K : (D.toSupported hflat).limitDerivedCategory)
      (ψ : ∀ n : ℕ, ((D.toSupported hflat).stageDerivedPullback n).obj K ≅ D.K n)
      (hK : QcohDerived D.B (limitBase D.system) D.containsLimitBase D.X.left K),
      IsRelativelyPseudoCoherent D.B (limitBase D.system) D.containsLimitBase D.X.left.1
          D.X.left.2 D.X.hom.hom
          (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
            D.containsLimitBase D.finitePresentation.1) ⟨K, hK⟩ ∧
        (∀ n : ℕ, (ψ n).hom = ((D.toSupported hflat).stageDerivedPullbackCompIso n).inv.app K ≫
          (transitionDerivedPullback D.system D.B D.containsLimitBase D.containsBaseAt D.X n).map
            (ψ (n + 1)).hom ≫ D.φ n) ∧
        ∀ i : ℤ, ∃ (T : Set (points D.B (limitBase D.system) D.containsLimitBase D.X.left.1))
          (hT : IsClosed T),
          IsProperOver D.B (limitBase D.system) D.containsLimitBase D.X.left.2
              (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2 D.X.hom.hom
              (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
                D.containsLimitBase D.finitePresentation.1) T hT ∧
            supportOfSheaf D.B (limitBase D.system) D.containsLimitBase D.X.left.1
              ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf
                (smallEtaleRingedSite D.B (limitBase D.system) D.containsLimitBase D.X.left.1
                  D.X.left.2).O)).obj
                ((DerivedCategory.homologyFunctor (Modules.{u, u} D.B (limitBase D.system)
                  D.containsLimitBase D.X.left.1 D.X.left.2) i).obj K)) ⊆ T
```

**`Stacks.Examples.DerivedExistenceNotFlat.not_forall_exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DerivedExistenceNotFlat.lean, line 810](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DerivedExistenceNotFlat.lean#L810). The attribute's comment: “refutation of the remark with X separated and of finite presentation, not flat: X = Spec A/(f), K\_n = O\_\{X\_n} admits no K pseudo-coherent relative to A with Lj\_n^* K = K\_n (errata entry 0DIR(flatness dropped))”.

> **The generalization of the derived existence theorem proposed in Stacks 0DIR is false
> without flatness.** There is a system satisfying all of its hypotheses — `Aₙ = 𝔽₂ ⊕ 𝔽₂ⁿ`,
> `X = Spec A/(f)` closed in `Spec A`, `Kₙ = 𝒪_{Xₙ}` — admitting no `K ∈ D_QCoh(𝒪_X)`
> pseudo-coherent relative to `A` with `Ljₙ^* K ≅ Kₙ` for every `n` (not even for `n = 0`, and
> with no compatibility asked of the isomorphisms).

```lean
theorem not_forall_exists_isRelativelyPseudoCoherent_stageDerivedPullback_iso :
    ¬ ∀ D : RelativeDerivedExistenceSystem.{0},
      ∃ (K : DerivedCategory (SheafOfModules.{0}
          (ringedToposStructureRingSheaf D.B (limitBase D.system) D.containsLimitBase D.X.left)))
        (hK : QcohDerived D.B (limitBase D.system) D.containsLimitBase D.X.left K),
        IsRelativelyPseudoCoherent D.B (limitBase D.system) D.containsLimitBase D.X.left.1
            D.X.left.2 D.X.hom.hom
            (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
              D.containsLimitBase D.finitePresentation.1) ⟨K, hK⟩ ∧
          ∀ n : ℕ, Nonempty ((smallEtaleDerivedModulePullback D.B (limitBase D.system)
            D.containsLimitBase (spaceProjection D.system D.B D.containsLimitBase
              D.containsBaseAt D.X n)).obj K ≅ D.K n)
```

**`Stacks.Examples.DerivedExistenceSupportNotProper.not_forall_exists_isRelativelyPseudoCoherent_isProperOver_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DerivedExistenceSupportNotProper.lean, line 978](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DerivedExistenceSupportNotProper.lean#L978). The attribute's comment: “refutation of the clause that K is supported on one closed subset proper over A: A = Z\_2, X = A^1\_A, K\_n = sum\_i O\_\{X\_n}/(x - 2^\{i+1})[2i] (errata entry 0DIR(support of K))”.

> **The support clause of the generalized derived existence theorem proposed in Stacks 0DIR is
> false.** There is a system satisfying all of its hypotheses, with `X` moreover flat over `A` —
> `A = ℤ_2`, `X = 𝔸¹_A`, `Kₙ = ⊕ᵢ 𝒪_{Xₙ}/(x - 2^{i+1})[2i]`, each `Kₙ` supported on `V(x)`, finite
> over `Aₙ` — for which no `K ∈ D_QCoh(𝒪_X)` pseudo-coherent relative to `A` with `Ljₙ^* K ≅ Kₙ`
> for every `n` (with no compatibility asked of the isomorphisms) is supported on a closed subset
> of `|X|` proper over `A`.

```lean
theorem not_forall_exists_isRelativelyPseudoCoherent_isProperOver_cohomologySupportedOn :
    ¬ ∀ D : SupportedDerivedExistenceSystem.{0},
      ∃ (K : D.limitDerivedCategory)
        (hK : QcohDerived D.B (limitBase D.system) D.containsLimitBase D.X.left K),
        IsRelativelyPseudoCoherent D.B (limitBase D.system) D.containsLimitBase D.X.left.1
            D.X.left.2 D.X.hom.hom
            (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
              D.containsLimitBase D.finitePresentation.1) ⟨K, hK⟩ ∧
          (∀ n : ℕ, Nonempty ((D.stageDerivedPullback n).obj K ≅ D.K n)) ∧
          ∃ (T : Set (points D.B (limitBase D.system) D.containsLimitBase D.X.left.1))
            (hT : _root_.IsClosed T),
            IsProperOver D.B (limitBase D.system) D.containsLimitBase D.X.left.2
                (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2 D.X.hom.hom
                (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B (limitBase D.system)
                  D.containsLimitBase D.finitePresentation.1) T hT ∧
              ∀ i : ℤ, supportOfSheaf D.B (limitBase D.system) D.containsLimitBase D.X.left.1
                ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf
                  (smallEtaleRingedSite D.B (limitBase D.system) D.containsLimitBase D.X.left.1
                    D.X.left.2).O)).obj
                  ((DerivedCategory.homologyFunctor (Space.Modules.{0, 0} D.B (limitBase D.system)
                    D.containsLimitBase D.X.left.1 D.X.left.2) i).obj K)) ⊆ T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.13, Tag 0DIJ](https://stacks.math.columbia.edu/tag/0DIJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
