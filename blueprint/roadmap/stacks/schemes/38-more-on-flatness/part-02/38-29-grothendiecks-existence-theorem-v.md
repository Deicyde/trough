---
declaration: section
origin: cited
lean: AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation, AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_coherator_obj, AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject_spec, AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isPseudoCoherent_cohomology_and_isIso, AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isPseudoCoherent_limitObject, AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isIso_derivedBaseChangeComparison_derivedSections, AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.exists_isPseudoCoherent_derivedPullback_iso
statement: formalized
proof: formalized
---

# 38.29 Grothendieck's Existence Theorem, V

Section 38.29 of the Stacks Project, [Tag 0DIA](https://stacks.math.columbia.edu/tag/0DIA). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DIB, a situation

[Tag 0DIB](https://stacks.math.columbia.edu/tag/0DIB) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/Basic.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/Basic.lean#L99).

> **Stacks Project, Tag 0DIB.** The standing data of Grothendieck's existence theorem in its
> derived form: an inverse system of rings with surjective, locally nilpotent transitions, a
> proper flat scheme of finite presentation over the inverse-limit ring, and a compatible system
> of pseudo-coherent objects on its base changes.

```lean
public structure DerivedExistenceSituation
```

## Tag 0DIC, a lemma

[Tag 0DIC](https://stacks.math.columbia.edu/tag/0DIC) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_coherator_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBounded.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBounded.lean#L164). The attribute's comment: “the displayed equality only; the coherator of Stacks 0CR0 is an argument, as in Stacks 0CSA and 0CR2, and the tower is an arbitrary inverse system in D(O\_X) rather than the system Ri\_n,* K\_n of Situation 0DIB, which this library cannot yet form at the locally small model the coherator lives at”.

> **The displayed equality of [Stacks, Tag 0DIC]**: `Rlim_{D_QCoh(𝒪_X)}(Kₙ)` and
> `DQ_X(Rlim_{D(𝒪_X)} Kₙ)` agree. Precisely, if `K` is a derived limit of an inverse system `(Kₙ)`
> in `D(𝒪_X)` then `DQ_X(K)` is a derived limit of the system `(DQ_X(Kₙ))` in `D_QCoh(𝒪_X)`; the
> existence of the product of the images is part of the conclusion.
>
> This is the source's reason for the equality: `DQ_X` is a right adjoint, so it commutes with
> products, and it is exact because the adjunction `ι ⊣ DQ_X` is triangulated, so it carries the
> derived-limit triangle of `(Kₙ)` to the derived-limit triangle of `(DQ_X(Kₙ))`.

```lean
theorem isDerivedLimit_coherator_obj (adj : quasiCoherentι X ⊣ DQ) [DQ.CommShift ℤ]
    [adj.IsTriangulated] (L : ℕᵒᵖ ⥤ DerivedCategory X.Modules)
    [HasProduct fun n : ℕ => L.obj ⟨n⟩] (K : DerivedCategory X.Modules)
    (hK : IsDerivedLimit L K) :
    ∃ h : HasProduct fun n : ℕ => DQ.obj (L.obj ⟨n⟩),
      @IsDerivedLimit (quasiCoherentDerivedCategory X) _ _ _ _ _ _ (L ⋙ DQ) h (DQ.obj K)
```

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBoundedAbove.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBoundedAbove.lean#L183).

> **Stacks Project, Tag 0DIC.** In Situation [Stacks, Tag 0DIB] consider
> `K = R lim_{D_QCoh(𝒪_X)}(Kₙ) = DQ_X(R lim_{D(𝒪_X)} Kₙ)`. Then `K` is in `D^-_QCoh(𝒪_X)`.
>
> Here `R lim_{D(𝒪_X)} Kₙ` is a chosen derived limit
> (`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.derivedLimit`) of the system
> `(R(iₙ)_* Kₙ)` whose transition maps are the adjoints of the `φₙ`, and `DQ_X` is the coherator of
> [Stacks, Tag 0CR0]. The three conjuncts are:
>
> * the displayed equality: `DQ_X(R lim_{D(𝒪_X)} Kₙ)` is a derived limit `R lim_{D_QCoh(𝒪_X)}(Kₙ)`
>   of the system in `D_QCoh(𝒪_X)`;
> * `K`, read at the model of the situation
>   (`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject`), has
>   quasi-coherent cohomology sheaves;
> * `K` is bounded above.
>
> The proof is the source's, see the module documentation and that of
> `StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitObject.lean`.

```lean
theorem limitObject_spec :
    (∃ _ : HasProduct fun n : ℕ => S.qcohTower.obj (op n),
      IsDerivedLimit S.qcohTower S.coheratorLimit) ∧
    letI := HasDerivedCategory.standard
      (StrictlyPerfect.OXMod.{u, u, u} S.X.left.toRingedSpace)
    (∀ j : ℤ, ((DerivedCategory.homologyFunctor _ j).obj S.limitObject).IsQuasicoherent) ∧
      ∃ c : ℤ, S.limitObject.IsLE c
```

## Tag 0DID, a lemma

[Tag 0DID](https://stacks.math.columbia.edu/tag/0DID) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isPseudoCoherent_cohomology_and_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/CohomologyAgainstPerfect.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/CohomologyAgainstPerfect.lean#L617).

> **[Stacks, Tag 0DID].** In Situation [Stacks, Tag 0DIB] let `K` be as in
> [Stacks, Tag 0DIC]. For any perfect object `E` of `D(𝒪_X)` the cohomology
> `M = RΓ(X, K ⊗^L E)` is a pseudo-coherent object of `D(A)` and there is a canonical isomorphism
> `RΓ(X_n, K_n ⊗^L E|_{X_n}) = M ⊗^L_A A_n` in `D(A_n)`, where `E|_{X_n}` is the derived pullback
> of `E` to `X_n`.
>
> Here `K` is `AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject`, `M`
> is `AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.cohomology`, and the
> canonical isomorphism is the base change map `M ⊗^L_A A_n ⟶ RΓ(X_n, K_n ⊗^L E|_{X_n})` adjoint to
> the canonical map `M ⟶ RΓ(X_n, K_n ⊗^L E|_{X_n})`
> (`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.cohomologyMap`): pull back
> along `X_n ⟶ X`, identify `(K ⊗^L E)|_{X_n} = K|_{X_n} ⊗^L E|_{X_n}`, and apply the canonical map
> `K|_{X_n} ⟶ K_n`.
>
> The proof is the source's. `RΓ(X, - ⊗^L E)` carries the derived-limit triangle of
> `K = DQ_X(R lim K_n)` to a triangle presenting `M` as `R lim M_n` for `M_n = RΓ(X_n, K_n ⊗^L E_n)`
> (`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.exists_distTriang_cohomology`);
> the `M_n` are pseudo-coherent ([Stacks, Tag 0CSD]) with `M_{n+1} ⊗^L A_n = M_n` by flat base
> change; and [Stacks, Tag 0CQF] concludes.

```lean
theorem isPseudoCoherent_cohomology_and_isIso
    (hE : RingedSpace.IsPerfect (X := S.X.left.toRingedSpace) E) :
    StacksDraft.PseudoCoherence.IsPseudoCoherent (S.cohomology E) ∧
      ∀ n : ℕ, IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison.{u, u, u}
        (limit.π S.system (op n)).hom (S.cohomologyMap E n))
```

## Tag 0DIE, a lemma

[Tag 0DIE](https://stacks.math.columbia.edu/tag/0DIE) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isPseudoCoherent_limitObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/LimitObjectPseudoCoherent.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/LimitObjectPseudoCoherent.lean#L77).

> **Stacks Project, Tag 0DIE.** In Situation [Stacks, Tag 0DIB] let `K` be as in
> [Stacks, Tag 0DIC]. Then `K` is pseudo-coherent on `X`.
>
> Here `K = DQ_X(R lim Kₙ)` is
> `AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject`, an object of
> `D(𝒪_X)` at the model at which the `Kₙ` are given. By [Stacks, Tag 0DID] (its first assertion,
> `DerivedExistenceSituation.isPseudoCoherent_cohomology_and_isIso`)
> `RΓ(X, K ⊗^𝐋 E)` is pseudo-coherent for every perfect `E`; [Stacks, Tag 0GES] (which is
> [Stacks, Tags 0CSH and 0CSL] together, `X` being separated and of finite presentation over `A`
> and `K` lying in `D_QCoh(𝒪_X)` by [Stacks, Tag 0DIC]) makes `K` pseudo-coherent relative to `A`,
> and [Stacks, Tag 09UU] (for schemes, [Stacks, Tag 0DII]) turns that into pseudo-coherence on `X`,
> `X` being flat and of finite presentation over `A`.

```lean
theorem isPseudoCoherent_limitObject (S : DerivedExistenceSituation.{u}) :
    letI := HasDerivedCategory.standard (StrictlyPerfect.OXMod.{u, u, u} S.X.left.toRingedSpace)
    RingedSpace.IsPseudoCoherent (X := S.X.left.toRingedSpace) S.limitObject
```

## Tag 0DIF, a lemma

[Tag 0DIF](https://stacks.math.columbia.edu/tag/0DIF) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.isIso_derivedBaseChangeComparison_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedSectionsBaseChange.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedSectionsBaseChange.lean#L155).

> In Situation [Stacks, Tag 0DIB] let `K` be as in [Stacks, Tag 0DIC]. For any quasi-compact
> open `U ⊆ X` we have `RΓ(U, K) ⊗^𝐋_A Aₙ = RΓ(Uₙ, Kₙ)` in `D(Aₙ)`, where `Uₙ = U ∩ Xₙ`.
>
> Here `K` is `AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.limitObject`,
> `RΓ(U, K)` is the `A`-linear derived global sections of `K|_U`, `RΓ(Uₙ, Kₙ)` the `Aₙ`-linear
> derived global sections of `Kₙ|_{Uₙ}`, and the identification is the canonical map
> `RΓ(U, K) ⊗^𝐋_A Aₙ ⟶ RΓ(Uₙ, Kₙ)`: the adjoint of
> `AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.openRestrictionMap`, which pulls
> derived sections back along `Uₙ ⟶ U` and applies the canonical map `K|_{Xₙ} ⟶ Kₙ` adjoint to the
> projection `K ⟶ R(iₙ)_* Kₙ`.

```lean
theorem isIso_derivedBaseChangeComparison_derivedSections (hU : IsCompact (U : Set S.X.left)) :
    IsIso (derivedBaseChangeComparison (limit.π S.system (op n)).hom
      (S.openRestrictionMap U n S.limitObject (S.restrictionMap n)))
```

## Tag 0DIG, a theorem

[Tag 0DIG](https://stacks.math.columbia.edu/tag/0DIG) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.DerivedExistenceSituation.exists_isPseudoCoherent_derivedPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedExistenceTheorem.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedExistenceTheorem.lean#L66).

> **[Stacks, Tag 0DIG], Grothendieck's existence theorem in its derived form.** In Situation
> [Stacks, Tag 0DIB] there is a pseudo-coherent `K ∈ D(𝒪_X)` together with isomorphisms
> `βₙ : K ⊗ᴸ_{𝒪_X} 𝒪_{Xₙ} = L(iₙ)^* K ≅ Kₙ` compatible with the maps `φₙ`: the composite
> `L(jₙ)^* L(iₙ₊₁)^* K ≅ L(iₙ)^* K ⟶ Kₙ` of the composition isomorphism with `βₙ` is
> `L(jₙ)^* βₙ₊₁` followed by `φₙ`.

```lean
theorem exists_isPseudoCoherent_derivedPullback_iso :
    ∃ K : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} S.X.left.toRingedSpace),
      RingedSpace.IsPseudoCoherent (X := S.X.left.toRingedSpace) K ∧
        ∃ β : ∀ n : ℕ, (derivedPullback (S.levelInclusion n)).obj K ≅ S.K n,
          ∀ n : ℕ,
            (Stacks.DerivedPullback.Composition.derivedPullbackCompIsoCanonical
                (S.levelTransition n) (S.levelInclusion (n + 1))).hom.app K ≫
              eqToHom (congrArg (fun t : (schemeAt S.system S.X n).toRingedSpace ⟶
                  S.X.left.toRingedSpace => (derivedPullback t).obj K)
                (S.levelTransition_comp_levelInclusion n)) ≫ (β n).hom =
            (derivedPullback (S.levelTransition n)).map (β (n + 1)).hom ≫ S.φ n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.29, Tag 0DIA](https://stacks.math.columbia.edu/tag/0DIA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
