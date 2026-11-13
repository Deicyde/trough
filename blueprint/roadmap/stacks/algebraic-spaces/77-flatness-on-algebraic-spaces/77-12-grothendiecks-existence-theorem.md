---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FlatSheafExistenceSituation, AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded, AlgebraicGeometry.Space.FlatSheafExistenceSituation.ringIsPerfect_limitSections_and_isIso_baseChangeMap, AlgebraicGeometry.Space.FlatSheafExistenceSituation.isRelativelyPseudoCoherent_coheratorObj, AlgebraicGeometry.Space.FlatSheafExistenceSituation.isIso_etaleStageBaseChangeMap, AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood, AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood_hasProperSupport_coheratorObj, AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_algebraization
statement: formalized
proof: formalized
---

# 77.12 Grothendieck's Existence Theorem

Section 77.12 of the Stacks Project, [Tag 0CX3](https://stacks.math.columbia.edu/tag/0CX3). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CX4, a situation

[Tag 0CX4](https://stacks.math.columbia.edu/tag/0CX4) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafSystem.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafSystem.lean#L85). The attribute's comment: “the situation as stated, with exactly the source's data and hypotheses; the two containment fields say that Spec A and Spec Aₙ are schemes of the chosen big fppf site”.

> **Situation [Stacks, Tag 0CX4].** An inverse system of rings `(Aₙ)` with surjective
> transition maps whose kernels are locally nilpotent; an algebraic space `X` separated and of finite
> presentation over `A = lim Aₙ`; and a system `(Fₙ, φₙ)` of finitely presented `𝒪_{Xₙ}`-modules on
> the infinitesimal base changes `Xₙ = X ×_{Spec A} Spec Aₙ`, each flat over `Aₙ` with support proper
> over `Aₙ`, together with isomorphisms `φₙ` from the restriction of `Fₙ₊₁` to `Xₙ` to `Fₙ`.

```lean
structure FlatSheafExistenceSituation
```

## Tag 0CX5, a lemma

[Tag 0CX5](https://stacks.math.columbia.edu/tag/0CX5) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafDerivedLimit.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafDerivedLimit.lean#L59). The attribute's comment: “the full statement: DQ\_X exists and R lim F\_n exists in D(O\_X); for every coherator DQ\_X and every such derived limit L, K = DQ\_X(L) is a derived limit of (F\_n) in D\_QCoh(O\_X), and every derived limit K of (F\_n) in D\_QCoh(O\_X) lies in D^b with cohomology sheaves only in degrees at least 0; proved with no hypothesis beyond Situation 0CX4”.

> **[Stacks, Tag 0CX5].** In Situation [Stacks, Tag 0CX4] consider
> `K = R lim_{D_QCoh(𝒪_X)}(Fₙ) = DQ_X(R lim_{D(𝒪_X)} Fₙ)`. Then `K` is in `D^b_QCoh(𝒪_X)` and in fact
> `K` has nonzero cohomology sheaves only in degrees `≥ 0`.
>
> Formally: the coherator `DQ_X`, the right adjoint of `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`, exists; the system
> `(Fₙ)` (that is, `(iₙ,* Fₙ)` placed in degree `0`) has a derived limit `L = R lim_{D(𝒪_X)} Fₙ`; and
> for every coherator `DQ_X` and every such `L`, `K = DQ_X(L)` is a derived limit of `(Fₙ)` in
> `D_QCoh(𝒪_X)`, its cohomology sheaves vanish in negative degrees, and they vanish above some
> degree; and every derived limit `K` of `(Fₙ)` in `D_QCoh(𝒪_X)` has the same two properties.

```lean
theorem derivedLimit_bounded :
    (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.IsLeftAdjoint ∧
    (∃ L, IsDerivedLimit D.derivedSystem L) ∧
    (∀ (DQ : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left ⥤
        (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory)
      (_ : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι ⊣ DQ)
      (L : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left),
      IsDerivedLimit D.derivedSystem L →
        (∃ _ : HasProduct fun n : ℕ => D.quasicoherentSystem.obj ⟨n⟩,
          IsDerivedLimit D.quasicoherentSystem (DQ.obj L)) ∧
        SpaceCohomologyVanishesBelow D.X.left 0
          ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj (DQ.obj L)) ∧
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B D.S D.containsLimitBase D.X.left c
          ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj (DQ.obj L))) ∧
    ∀ (_ : HasProduct fun n : ℕ => D.quasicoherentSystem.obj ⟨n⟩)
      (K : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory),
      IsDerivedLimit D.quasicoherentSystem K →
        SpaceCohomologyVanishesBelow D.X.left 0
          ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj K) ∧
        ∃ c : ℤ, SpaceCohomologyVanishesAbove D.B D.S D.containsLimitBase D.X.left c
          ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj K)
```

## Tag 0CX6, a lemma

[Tag 0CX6](https://stacks.math.columbia.edu/tag/0CX6) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.ringIsPerfect_limitSections_and_isIso_baseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/PerfectSectionsOfLimitTheorem.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/PerfectSectionsOfLimitTheorem.lean#L102). The attribute's comment: “both parts in full, for every perfect E on X and every n, with K = DQ\_X(R lim\_\{D(O\_X)} F\_n) the object of 0CX5, whose coherator and derived limit exist by derivedLimit\_bounded: (1) RΓ(X, K ⊗^L E) is perfect in D(A) and the canonical map RΓ(X, K ⊗^L E) ⊗^L\_A A\_n → RΓ(X\_n, F\_n ⊗^L E|\_\{X\_n}) is an isomorphism; (2) RHom\_X(E, K) is perfect in D(A) and the canonical map RHom\_X(E, K) ⊗^L\_A A\_n → RHom\_\{X\_n}(E|\_\{X\_n}, F\_n) is an isomorphism”.

> **[Stacks, Tag 0CX6].** In Situation [Stacks, Tag 0CX4] let
> `K = R lim_{D_QCoh(𝒪_X)} Fₙ = DQ_X(R lim_{D(𝒪_X)} Fₙ)` be the object of [Stacks, Tag 0CX5]
> (`DQ_X` is `AlgebraicGeometry.Space.FlatSheafExistenceSituation.coherator` and
> `R lim_{D(𝒪_X)} Fₙ` is `AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit`, both of
> which exist by `AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded`). Then for
> every perfect object `E` of `D(𝒪_X)` and every `n`:
>
> 1. `M = RΓ(X, K ⊗^𝐋 E)` (written `RΓ(X, E ⊗^𝐋 K)`) is a perfect object of `D(A)` and the
>    canonical map `M ⊗^𝐋_A Aₙ ⟶ RΓ(Xₙ, E|_{Xₙ} ⊗^𝐋 Fₙ)` is an isomorphism in `D(Aₙ)`;
> 2. `N = RHom_X(E, K)` is a perfect object of `D(A)` and the canonical map
>    `N ⊗^𝐋_A Aₙ ⟶ RHom_{Xₙ}(E|_{Xₙ}, Fₙ)` is an isomorphism in `D(Aₙ)`.
>
> Here `E|_{Xₙ}` is the derived pullback of `E` along `iₙ : Xₙ ⟶ X`. The same holds for every other
> choice of coherator and of derived limit triangle
> (`AlgebraicGeometry.Space.FlatSheafExistenceSituation.perfectSections_of_derivedLimit`).

```lean
theorem ringIsPerfect_limitSections_and_isIso_baseChangeMap
    (E : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left)
    (hE : spaceIsPerfect D.B D.S D.containsLimitBase D.X.left E) (n : ℕ) :
    (StacksDraft.ringIsPerfect (D.limitTensorSections D.coherator D.derivedLimit E) ∧
      IsIso (D.limitTensorSectionsBaseChangeMap D.coheratorAdjunction D.derivedLimit E
        D.derivedLimitToProduct n)) ∧
    (StacksDraft.ringIsPerfect (D.limitSheafHomSections D.coherator D.derivedLimit E) ∧
      IsIso (D.limitSheafHomSectionsBaseChangeMap D.coheratorAdjunction D.derivedLimit E hE
        D.derivedLimitToProduct n))
```

## Tag 0CX7, a lemma

[Tag 0CX7](https://stacks.math.columbia.edu/tag/0CX7) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.isRelativelyPseudoCoherent_coheratorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/RelativePseudoCoherenceOfLimit.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/RelativePseudoCoherenceOfLimit.lean#L43). The attribute's comment: “the full statement: for every coherator DQ\_X and every derived limit L of (F\_n) in D(O\_X), the K = DQ\_X(L) of 0CX5 is pseudo-coherent relative to A, with no hypotheses beyond Situation 0CX4; 0CX6, 0CWH and 0CTT are all proved in the library”.

> **[Stacks, Tag 0CX7].** In Situation [Stacks, Tag 0CX4] let `K = DQ_X(L)` be as in
> [Stacks, Tag 0CX5]: `DQ_X` is a coherator (`adj : ι ⊣ DQ_X`, the right adjoint of the inclusion
> `D_QCoh(𝒪_X) ⟶ D(𝒪_X)`) and `L` is a derived limit `R lim_{D(𝒪_X)} Fₙ` of the system `(iₙ,* Fₙ)`.
> Then `K` is pseudo-coherent relative to `A`.

```lean
theorem isRelativelyPseudoCoherent_coheratorObj
    {DQ : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left ⥤
      (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory}
    (adj : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι ⊣ DQ)
    (L : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left)
    (hL : IsDerivedLimit D.derivedSystem L) :
    IsRelativelyPseudoCoherent D.B D.S D.containsLimitBase D.X.left.1 D.X.left.2 D.X.hom.hom
      D.isLocallyOfFiniteType_structureMorphism (D.coheratorObj DQ L)
```

## Tag 0CX8, a lemma

[Tag 0CX8](https://stacks.math.columbia.edu/tag/0CX8) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.isIso_etaleStageBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EtaleStageBaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EtaleStageBaseChange.lean#L60). The attribute's comment: “the full statement: for every coherator DQ\_X and every presentation of L = R lim F\_n in D(O\_X), every n and every etale U → X with U quasi-compact and quasi-separated, the canonical map RΓ(U, K) ⊗^L\_A A\_n → RΓ(U\_n, F\_n) in D(A\_n) induced by K = DQ\_X(L) → F\_n is an isomorphism, U\_n = U ×\_X X\_n, under exactly the source's hypotheses”.

> **[Stacks, Tag 0CX8].** In Situation [Stacks, Tag 0CX4] let `K = DQ_X(L)` be as in
> [Stacks, Tag 0CX5]: `DQ_X` is a coherator (`adj : ι ⊣ DQ_X`) and
> `L ⟶ ∏ Fₙ ⟶ ∏ Fₙ ⟶ L[1]` (first map `p`) presents `L` as `R lim_{D(𝒪_X)} Fₙ`, with
> canonical maps `φₙ : K ⟶ Fₙ` the counit followed by the projections. For every `n` and every
> étale morphism `j : U ⟶ X` with `U` quasi-compact and quasi-separated, the canonical map
> `RΓ(U, K) ⊗^𝐋_A Aₙ ⟶ RΓ(Uₙ, Fₙ)` of `D(Aₙ)` induced by `φₙ`, `Uₙ = U ×_X Xₙ`, is an
> isomorphism.

```lean
theorem isIso_etaleStageBaseChangeMap
    {DQ : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left ⥤
      (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory}
    (adj : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι ⊣ DQ)
    {L : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left}
    (p : L ⟶ ∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩)
    (hp : ∃ δ : (∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ => Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) (n + 1) ≫
          D.derivedSystem.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left))
    (n : ℕ) {U : AlgebraicSpaces D.B D.S D.containsLimitBase} (j : U ⟶ D.X.left)
    (hj : IsEtale D.B D.S D.containsLimitBase j.hom)
    (hUqc : IsQuasiCompactSpace D.B D.S D.containsLimitBase U.1)
    (hUqs : IsAbsolutelyQuasiSeparated D.B D.S D.containsLimitBase D.B.contains_terminal U.1) :
    IsIso (D.etaleStageBaseChangeMap n j
      (D.isQuasiCompact_isQuasiSeparated_of_isEtale j hj hUqc hUqs).1
      (D.isQuasiCompact_isQuasiSeparated_of_isEtale j hj hUqc hUqs).2 adj p)
```

## Tag 0CX9, a lemma

[Tag 0CX9](https://stacks.math.columbia.edu/tag/0CX9) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodExists.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodExists.lean#L56). The attribute's comment: “the full statement: for every coherator DQ\_X and every presentation of L = R lim F\_n in D(O\_X), K = DQ\_X(L) has an open subspace W containing X\_0 with H^i(K)|\_W = 0 for i ≠ 0, H^0(K)|\_W of finite presentation, and F\_n = H^0(K)|\_W ⊗ O\_\{X\_n} through the canonical maps K → F\_n”.

> In Situation [Stacks, Tag 0CX4] let `K = DQ_X(L)` be as in [Stacks, Tag 0CX5]: `DQ_X` is a
> coherator (`adj : ι ⊣ DQ_X`) and `L ⟶ ∏ Fₙ ⟶ ∏ Fₙ ⟶ L[1]` (first map `p`) presents `L` as
> `R lim_{D(𝒪_X)} Fₙ`, with canonical maps `K ⟶ Fₙ` the counit followed by the projections. Then
> there is an open subspace `W ⊂ X` containing the points `X₀` lying over `Spec(A₁)` such that
> `Hⁱ(K)|_W = 0` for `i ≠ 0`, `H⁰(K)|_W` is of finite presentation, and
> `H⁰(K)|_W ⊗_{𝒪_X} 𝒪_{Xₙ} ⟶ Fₙ` induced by `K ⟶ Fₙ` is an isomorphism on `W ×_X Xₙ` for every `n`.

```lean
theorem exists_isExistenceNeighbourhood
    {DQ : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left ⥤
      (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory}
    (adj : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι ⊣ DQ)
    {L : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left}
    (p : L ⟶ ∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩)
    (hp : ∃ δ : (∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ => Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) (n + 1) ≫
          D.derivedSystem.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left)) :
    ∃ (W : Subfunctor D.X.left.1) (hW : IsOpenSubspace D.B D.S D.containsLimitBase W),
      D.IsExistenceNeighbourhood
        ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj (DQ.obj L))
        (D.derivedLimitProjection adj p) W hW
```

## Tag 0CXA, a lemma

[Tag 0CXA](https://stacks.math.columbia.edu/tag/0CXA) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood_hasProperSupport_coheratorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodProperSupport.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodProperSupport.lean#L237). The attribute's comment: “the full statement: for every coherator DQ\_X and every presentation of L = R lim F\_n in D(O\_X), K = DQ\_X(L) with its canonical maps K → F\_n, and every open W as in 0CX9 for that K, there is a smaller open W', again as in 0CX9, on which the support of H^0(K)|\_W' is proper over A”.

> **Stacks 0CXA.** In Situation 0CX4 let `K = DQ_X(L)` be as in Stacks 0CX5: `DQ_X` is a
> coherator (`adj : ι ⊣ DQ_X`) and `L ⟶ ∏ Fₙ ⟶ ∏ Fₙ ⟶ L[1]` (first map `p`) presents `L` as
> `R lim_{D(𝒪_X)} Fₙ`, with the canonical maps `K ⟶ Fₙ`. Let `W ⊂ X` be as in Stacks 0CX9: an
> open subspace containing `X₀` with `Hⁱ(K)|_W = 0` for `i ≠ 0`, `H⁰(K)|_W` of finite
> presentation and `Fₙ = H⁰(K)|_W ⊗ 𝒪_{Xₙ}`. Then after shrinking `W` to an open subspace `W'`
> (which again is as in Stacks 0CX9) the support of `F = H⁰(K)|_{W'}` is proper over `A`.

```lean
theorem exists_isExistenceNeighbourhood_hasProperSupport_coheratorObj
    {DQ : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left ⥤
      (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).FullSubcategory}
    (adj : (spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι ⊣ DQ)
    {L : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left}
    (p : L ⟶ ∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩)
    (_ : ∃ δ : (∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ => Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) (n + 1) ≫
          D.derivedSystem.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left))
    {W : Subfunctor D.X.left.1} {hW : IsOpenSubspace D.B D.S D.containsLimitBase W}
    (hN : D.IsExistenceNeighbourhood
      ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj (DQ.obj L))
      (D.derivedLimitProjection adj p) W hW) :
    ∃ (W' : Subfunctor D.X.left.1) (hW' : IsOpenSubspace D.B D.S D.containsLimitBase W')
      (_ : W' ≤ W), D.IsExistenceNeighbourhood
        ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj (DQ.obj L))
        (D.derivedLimitProjection adj p) W' hW' ∧
      ∃ hlft : IsLocallyOfFiniteType D.B D.S D.containsLimitBase (W'.ι ≫ D.X.hom.hom),
        HasProperSupport D.B D.S D.containsLimitBase hW'.1
          (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2
          (W'.ι ≫ D.X.hom.hom) hlft
          ((SheafOfModules.toSheaf _).obj
            ((modulePullback D.B D.S D.containsLimitBase
              (openSubspaceHom D.B D.S D.containsLimitBase W' hW')).obj
                ((spaceDerivedHomology D.B D.S D.containsLimitBase D.X.left 0).obj
                  ((spaceQuasicoherentProp D.B D.S D.containsLimitBase D.X.left).ι.obj
                    (DQ.obj L)))))
```

## Tag 0CXB, a theorem

[Tag 0CXB](https://stacks.math.columbia.edu/tag/0CXB) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatExistenceTheorem.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatExistenceTheorem.lean#L50).

> **Grothendieck's existence theorem, [Stacks, Tag 0CXB].** In Situation [Stacks, Tag 0CX4]
> there exists a finitely presented `𝒪_X`-module `F`, flat over `A`, whose support is closed and
> proper over `A`, with identifications `αₙ : F ⊗_{𝒪_X} 𝒪_{Xₙ} = iₙ^* F ≅ Fₙ` for all `n`,
> compatible with the maps `φₙ : Fₙ₊₁ ⊗ 𝒪_{Xₙ} ≅ Fₙ` through `tₙ^* iₙ₊₁^* = iₙ^*`.

```lean
theorem exists_algebraization :
    ∃ F : Modules.{u, u} D.B D.S D.containsLimitBase D.X.left.1 D.X.left.2,
      F.IsFinitePresentationOnSite ∧
        IsFlatOver D.B D.S D.containsLimitBase D.X.left.2 D.X.hom.hom F ∧
        ∃ hcl : IsClosed (supportOfSheaf D.B D.S D.containsLimitBase D.X.left.1
            ((SheafOfModules.toSheaf _).obj F)),
          IsProperOver D.B D.S D.containsLimitBase D.X.left.2
            (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2 D.X.hom.hom
            (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation D.B D.S
              D.containsLimitBase D.finitePresentation.1)
            (supportOfSheaf D.B D.S D.containsLimitBase D.X.left.1
              ((SheafOfModules.toSheaf _).obj F)) hcl ∧
          ∃ α : ∀ n : ℕ, (modulePullback D.B D.S D.containsLimitBase
              (D.closedImmersion n)).obj F ≅ D.F n,
            ∀ n : ℕ,
              (modulePullback D.B D.S D.containsLimitBase (D.transition n)).map
                  (α (n + 1)).hom ≫ (D.φ n).hom =
                (modulePullbackCompIso D.B D.S D.containsLimitBase (D.transition n)
                    (D.closedImmersion (n + 1))).hom.app F ≫
                  eqToHom (congrArg (fun g => (modulePullback D.B D.S
                    D.containsLimitBase g).obj F) (D.transition_closedImmersion n)) ≫
                  (α n).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.12, Tag 0CX3](https://stacks.math.columbia.edu/tag/0CX3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
