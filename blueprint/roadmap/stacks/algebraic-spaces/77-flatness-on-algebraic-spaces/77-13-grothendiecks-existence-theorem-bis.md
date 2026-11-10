---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.DerivedExistenceSituation, AlgebraicGeometry.Space.DerivedExistenceSystem, AlgebraicGeometry.Space.DerivedExistenceSystem.derivedLimit_isBoundedAbove, AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange, AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherentOnLimit_coheratorObj, AlgebraicGeometry.Space.DerivedExistenceSystem.isIso_etaleSectionsBaseChangeMap, AlgebraicGeometry.Space.DerivedExistenceSystem.exists_isPseudoCoherent_stageDerivedPullback_iso, AlgebraicGeometry.Space.DerivedExistenceSituation.isSeparated_and_isFinitePresentation
statement: formalized
proof: formalized
---

# 77.13 Grothendieck's Existence Theorem, bis

Section 77.13 of the Stacks Project, [Tag 0DIJ](https://stacks.math.columbia.edu/tag/0DIJ). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DIK, a situation

[Tag 0DIK](https://stacks.math.columbia.edu/tag/0DIK) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistence.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistence.lean#L478).

> **Stacks 0DIK.** The standing data of Grothendieck's existence theorem for algebraic spaces
> in its derived form: an inverse system of rings with surjective, locally nilpotent transitions,
> a proper flat algebraic space of finite presentation over the inverse-limit ring, and a
> compatible system of pseudo-coherent objects on its infinitesimal base changes.

```lean
structure DerivedExistenceSituation
```

**`AlgebraicGeometry.Space.DerivedExistenceSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSystem.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceSystem.lean#L105). The attribute's comment: “the situation as stated, with the derived pullback along each Xₙ → Xₙ₊₁ constructed by Stacks 06YY rather than given; nothing is granted or assumed beyond the source's data and a big fppf site containing Spec A and every Spec Aₙ”.

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

**`AlgebraicGeometry.Space.DerivedExistenceSystem.derivedLimit_isBoundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceBoundedLimit.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceBoundedLimit.lean#L62). The attribute's comment: “K = R lim_{D_QCoh} K_n = DQ_X(R lim_{D(O_X)} K_n) lies in D^-_QCoh(O_X), for every choice of coherator and of derived limits”.

> The inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right adjoint `DQ_X` and the tower `(Rjₙ,* Kₙ)`
> has a derived limit `L = R lim_{D(𝒪_X)} Kₙ`. For every coherator `DQ_X` and every such `L`,
> `K = DQ_X(L)` is a derived limit of the tower in `D_QCoh(𝒪_X)` whose cohomology sheaves vanish
> above some degree. Every derived limit of the tower in `D_QCoh(𝒪_X)` lies in `D⁻_QCoh(𝒪_X)`.

```lean
theorem derivedLimit_isBoundedAbove :
    (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.IsLeftAdjoint ∧
    (∃ L, IsDerivedLimit D.spaceTower L) ∧
    (∀ (DQ : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left ⥤
        (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
          D.X.left).FullSubcategory)
      (_ : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι ⊣ DQ)
      (L : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left),
      IsDerivedLimit D.spaceTower L →
        (∃ _ : HasProduct fun n : ℕ => D.quasicoherentTower.obj ⟨n⟩,
          IsDerivedLimit D.quasicoherentTower (DQ.obj L)) ∧
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B (limitBase D.system) D.containsLimitBase
          D.X.left c ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
            D.X.left).ι.obj (DQ.obj L))) ∧
    ∀ (_ : HasProduct fun n : ℕ => D.quasicoherentTower.obj ⟨n⟩)
      (K : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
        D.X.left).FullSubcategory),
      IsDerivedLimit D.quasicoherentTower K →
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B (limitBase D.system) D.containsLimitBase
          D.X.left c ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
            D.X.left).ι.obj K)
```

## Tag 0DIM, a lemma

[Tag 0DIM](https://stacks.math.columbia.edu/tag/0DIM) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceTensorSectionsBaseChange.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceTensorSectionsBaseChange.lean#L365). The attribute's comment: “the full statement: for every perfect E, M = RΓ(X, E ⊗^L K) is pseudo-coherent and the canonical map M ⊗^L_A Aₙ ⟶ RΓ(Xₙ, Lpₙ^*E ⊗^L Kₙ) is an isomorphism in D(Aₙ) for every n. D is Situation 0DIK (DerivedExistenceSystem), whose fields are only the situation's data and hypotheses: the rings Aₙ with surjective transitions with locally nilpotent kernels, the fppf site containing Spec A and every Spec Aₙ, X proper, flat and of finite presentation over A, the pseudo-coherent Kₙ, and the comparison isomorphisms Liₙ^* Kₙ₊₁ ≅ Kₙ; no result is a field. K = DQ_X(R lim Kₙ) is the object of 0DIL, built from the coherator (the right adjoint of D_QCoh(𝒪_X) ⥤ D(𝒪_X)) and a derived limit, both constructed and not assumed”.

> **[Stacks, Tag 0DIM].** In Situation 0DIK let `K = DQ_X(R lim Kₙ)` be the object of
> [Stacks, Tag 0DIL] and `E` a perfect object of `D(𝒪_X)`. Then `M = RΓ(X, E ⊗^L K)` is a
> pseudo-coherent object of `D(A)`, and for every `n` the canonical map
> `cₙ : M ⊗^L_A Aₙ ⟶ RΓ(Xₙ, Lpₙ^*E ⊗^L Kₙ)` (the base change map of `RΓ`, then Stacks 07A4 and
> `Lpₙ^*E ⊗^L τₙ`, with `τₙ : Lpₙ^*K ⟶ Kₙ` adjoint to the projection) is an isomorphism in
> `D(Aₙ)`. Here `K` is `D.quasicoherentLimit`, with `R lim Kₙ = D.derivedLimit` and `DQ_X` the
> right adjoint `D.coherator` of the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`.

```lean
theorem isPseudoCoherent_and_isIso_stageTensorSectionsBaseChange
    (E : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left)
    (hE : spaceIsPerfect D.B (limitBase D.system) D.containsLimitBase D.X.left E) :
    StacksDraft.PseudoCoherence.IsPseudoCoherent
        ((D.limitTensorSections E).obj ((spaceQuasicoherentProp D.B (limitBase D.system)
          D.containsLimitBase D.X.left).ι.obj D.quasicoherentLimit)) ∧
      ∀ n : ℕ, IsIso (D.stageTensorSectionsBaseChange D.coherator D.coheratorAdjunction E n)
```

## Tag 0DIN, a lemma

[Tag 0DIN](https://stacks.math.columbia.edu/tag/0DIN) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isPseudoCoherentOnLimit_coheratorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistencePseudoCoherent.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistencePseudoCoherent.lean#L190). The attribute's comment: “K = R lim_{D_QCoh} K_n = DQ_X(R lim_{D(O_X)} K_n) is pseudo-coherent on X, for every choice of coherator and of derived limit; nothing is granted or assumed”.

> In Situation 0DIK let `K = R lim_{D_QCoh(𝒪_X)}(Kₙ) = DQ_X(L)` be the object of
> [Stacks, Tag 0DIL], for a coherator `adj : ι ⊣ DQ_X` and a derived limit `L = R lim_{D(𝒪_X)} Kₙ`
> of the tower `(Rjₙ,* Kₙ)`. Then `K` is pseudo-coherent on `X`.

```lean
theorem isPseudoCoherentOnLimit_coheratorObj
    (DQ : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left ⥤
      (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase
        D.X.left).FullSubcategory)
    (adj : (spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι ⊣ DQ)
    (L : spaceDerivedCategory D.B (limitBase D.system) D.containsLimitBase D.X.left)
    (hL : IsDerivedLimit D.spaceTower L) :
    D.IsPseudoCoherentOnLimit
      ((spaceQuasicoherentProp D.B (limitBase D.system) D.containsLimitBase D.X.left).ι.obj
        (DQ.obj L))
```

## Tag 0DIP, a lemma

[Tag 0DIP](https://stacks.math.columbia.edu/tag/0DIP) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.isIso_etaleSectionsBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceEtaleSectionsHocolim.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceEtaleSectionsHocolim.lean#L128). The attribute's comment: “for U → X étale with U qcqs, RΓ(U, K) ⊗^L_A A_n → RΓ(U_n, K_n) is an isomorphism in D(A_n), U_n = U ×_X X_n; nothing is granted or assumed”.

> In Situation 0DIK let `K = DQ_X(R lim Kₙ)` be the object of [Stacks, Tag 0DIL]
> (`AlgebraicGeometry.Space.DerivedExistenceSystem.quasicoherentLimit`, for the coherator `DQ_X`
> right adjoint to `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`). For every étale `j : U ⟶ X` with `U`
> quasi-compact and quasi-separated and every `n`, the canonical map
> `RΓ(U, K) ⊗^L_A Aₙ ⟶ RΓ(Uₙ, Kₙ)` in `D(Aₙ)`, with `Uₙ = U ×_X Xₙ` (the base change map of `RΓ`
> along `Spec Aₙ ⟶ Spec A`, then `RΓ(Uₙ, -)` of `τₙ|_{Uₙ}`, with `τₙ : Lpₙ^*K ⟶ Kₙ` adjoint to the
> projection), is an isomorphism.

```lean
theorem isIso_etaleSectionsBaseChangeMap
    (hj : IsEtale D.B (limitBase D.system) D.containsLimitBase j.hom)
    (hUqc : IsQuasiCompactSpace D.B (limitBase D.system) D.containsLimitBase U.1)
    (hUqs : IsAbsolutelyQuasiSeparated D.B (limitBase D.system) D.containsLimitBase
      D.B.contains_terminal U.1) (n : ℕ) :
    IsIso (D.etaleSectionsBaseChangeMap j D.coherator D.coheratorAdjunction n)
```

## Tag 0DIQ, a theorem

[Tag 0DIQ](https://stacks.math.columbia.edu/tag/0DIQ) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSystem.exists_isPseudoCoherent_stageDerivedPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceGrothendieck.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceGrothendieck.lean#L236). The attribute's comment: “the full statement: K pseudo-coherent on X, K_n = Lj_n^* K for all n compatibly with the phi_n through the composition isomorphism of derived pullbacks; nothing is granted or assumed beyond Situation 0DIK”.

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
theorem exists_isPseudoCoherent_stageDerivedPullback_iso :
    ∃ (K : D.limitDerivedCategory) (ψ : ∀ n : ℕ, (D.stageDerivedPullback n).obj K ≅ D.K n),
      D.IsPseudoCoherentOnLimit K ∧
        ∀ n : ℕ, (ψ n).hom = (D.stageDerivedPullbackCompIso n).inv.app K ≫
          (transitionDerivedPullback D.system D.B D.containsLimitBase D.containsBaseAt D.X n).map
            (ψ (n + 1)).hom ≫ D.φ n
```

## Tag 0DIR, a remark

[Tag 0DIR](https://stacks.math.columbia.edu/tag/0DIR) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedExistenceSituation.isSeparated_and_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceHypotheses.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceHypotheses.lean#L90). The attribute's comment: “comparison of hypotheses on X only; the generalization is merely probable in the source, which gives no precise statement of it, and is not proved here”.

> In a situation of Stacks 0DIK the structure morphism `X → Spec A` is separated, being
> proper, and is of finite presentation: the two conditions that the generalization proposed in
> Stacks 0DIR places on `X` hold.

```lean
theorem isSeparated_and_isFinitePresentation :
    IsSeparated D.B (limitBase D.system) D.containsLimitBase D.X.hom.hom ∧
      IsFinitePresentation D.B (limitBase D.system) D.containsLimitBase D.X.hom.hom
```

**`AlgebraicGeometry.Space.DerivedExistenceSituation.isProperOver_stageProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceHypotheses.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/DerivedExistenceHypotheses.lean#L100). The attribute's comment: “comparison of hypotheses on Xₙ only; the generalization is merely probable in the source, which gives no precise statement of it, and is not proved here”.

> In a situation of Stacks 0DIK every closed subset of the infinitesimal base change `Xₙ` is
> proper over `Spec Aₙ`, since `Xₙ → Spec Aₙ` is proper: the support condition that the
> generalization proposed in Stacks 0DIR places on `Kₙ` holds for every object of `D(𝒪_{Xₙ})`.

```lean
theorem isProperOver_stageProjection (n : ℕ)
    (T : Set (points D.B (limitBase D.system) D.containsLimitBase
      (spaceAt D.system D.B D.containsLimitBase D.containsBaseAt D.X n).1))
    (hT : _root_.IsClosed T) :
    IsProperOver D.B (limitBase D.system) D.containsLimitBase
      (spaceAt D.system D.B D.containsLimitBase D.containsBaseAt D.X n).2
      (schemeSpace
        (baseObjectAt D.system D.B D.containsLimitBase D.containsBaseAt n)).2
      (D.stageProjection n).hom (D.isLocallyOfFiniteType_stageProjection n) T hT
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.13, Tag 0DIJ](https://stacks.math.columbia.edu/tag/0DIJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
