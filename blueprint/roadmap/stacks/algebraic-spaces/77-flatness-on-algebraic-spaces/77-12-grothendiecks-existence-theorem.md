---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.InverseSystemExistenceSituation, AlgebraicGeometry.Space.FlatSheafExistenceSituation, AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded, AlgebraicGeometry.Space.FlatSheafExistenceSituation.perfectSections_of_derivedLimit, AlgebraicGeometry.Space.FlatSheafExistenceSituation.isRelativelyPseudoCoherent_coheratorObj, AlgebraicGeometry.Space.FlatSheafExistenceSituation.isIso_etaleStageBaseChangeMap, AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood, AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood_hasProperSupport
statement: formalized
proof: formalized
---

# 77.12 Grothendieck's Existence Theorem

Section 77.12 of the Stacks Project, [Tag 0CX3](https://stacks.math.columbia.edu/tag/0CX3). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CX4, a situation

[Tag 0CX4](https://stacks.math.columbia.edu/tag/0CX4) in the Stacks Project.

**`AlgebraicGeometry.Space.InverseSystemExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Existence.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Existence.lean#L120).

> **Stacks 0CX4.** The standing data of Grothendieck's existence theorem for algebraic spaces:
> an inverse system of rings with surjective, locally nilpotent transitions, a separated algebraic
> space of finite presentation over the inverse-limit ring, and a compatible system of finitely
> presented quasi-coherent modules on its infinitesimal base changes which are flat over, and have
> support proper over, the affine base at their level.

```lean
structure InverseSystemExistenceSituation
```

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafSystem.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafSystem.lean#L86). The attribute's comment: “the situation as stated: nothing is granted or assumed beyond the source's data and hypotheses; the two containment fields only say that Spec A and Spec Aₙ are schemes of the chosen big fppf site”.

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

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafDerivedLimit.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatSheafDerivedLimit.lean#L59). The attribute's comment: “the full statement: DQ_X exists and R lim F_n exists in D(O_X); for every coherator DQ_X and every such derived limit L, K = DQ_X(L) is a derived limit of (F_n) in D_QCoh(O_X), and every derived limit K of (F_n) in D_QCoh(O_X) lies in D^b with cohomology sheaves only in degrees at least 0; nothing is granted or assumed”.

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

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.perfectSections_of_derivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/PerfectSectionsOfLimitCarrier.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/PerfectSectionsOfLimitCarrier.lean#L76). The attribute's comment: “both parts in full, for every perfect E on X and every n, with K = DQ_X(L) for every coherator DQ_X and every L presented as R lim (i_n,* F_n) by the IsDerivedLimit triangle hp (as in derivedLimit_bounded, 0CX5): (1) RΓ(X, E ⊗^L K) is perfect in D(A) and the canonical map RΓ(X, E ⊗^L K) ⊗^L_A A_n → RΓ(X_n, E|_{X_n} ⊗^L F_n) is an isomorphism; (2) RHom_X(E, K) is perfect in D(A) and the canonical map RHom_X(E, K) ⊗^L_A A_n → RHom_{X_n}(E|_{X_n}, F_n), the map induced from (1) at E^∨ by 08JJ / 21.48.4, is an isomorphism; nothing is granted or assumed”.

> **[Stacks, Tag 0CX6].** In Situation [Stacks, Tag 0CX4] let `K = DQ_X(L)` be as in
> [Stacks, Tag 0CX5] (`AlgebraicGeometry.Space.FlatSheafExistenceSituation.derivedLimit_bounded`):
> `DQ_X` is a coherator (`adj : ι ⊣ DQ_X`) and `p : L ⟶ ∏ (iₙ,* Fₙ)[0]` is the first map of a
> distinguished triangle `L ⟶ ∏ Fₙ ⟶ ∏ Fₙ ⟶ L[1]` whose middle map is `1 - transition`
> (`hp` is exactly the triangle of `CategoryTheory.Pretriangulated.IsDerivedLimit` with `p` bound),
> so `L = R lim Fₙ`. Then for every perfect `E` on `X` and every `n`:
>
> 1. `RΓ(X, E ⊗^𝐋 K)` is a perfect object of `D(A)` and the canonical map
>    `RΓ(X, E ⊗^𝐋 K) ⊗^𝐋_A Aₙ ⟶ RΓ(Xₙ, E|_{Xₙ} ⊗^𝐋 Fₙ)` is an isomorphism in `D(Aₙ)`;
> 2. `RHom_X(E, K)` is a perfect object of `D(A)` and the canonical map
>    `RHom_X(E, K) ⊗^𝐋_A Aₙ ⟶ RHom_{Xₙ}(E|_{Xₙ}, Fₙ)` is an isomorphism in `D(Aₙ)`; this map is
>    the one induced from (1) at `E^∨` by Cohomology on Sites, Lemma 21.48.4 (Stacks 08JJ).
>
> Here `E|_{Xₙ}` is the derived pullback of `E` along `iₙ : Xₙ ⟶ X`.

```lean
theorem perfectSections_of_derivedLimit
    (p : L ⟶ ∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩)
    (hp : ∃ δ : (∏ᶜ fun n : ℕ => D.derivedSystem.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ => Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ => D.derivedSystem.obj ⟨n⟩) (n + 1) ≫
          D.derivedSystem.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left))
    (E : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left)
    (hE : spaceIsPerfect D.B D.S D.containsLimitBase D.X.left E) (n : ℕ) :
    (StacksDraft.ringIsPerfect (D.limitTensorSections DQ L E) ∧
      IsIso (D.limitTensorSectionsBaseChangeMap adj L E p n)) ∧
    (StacksDraft.ringIsPerfect (D.limitSheafHomSections DQ L E) ∧
      IsIso (D.limitSheafHomSectionsBaseChangeMap adj L E hE p n))
```

## Tag 0CX7, a lemma

[Tag 0CX7](https://stacks.math.columbia.edu/tag/0CX7) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.isRelativelyPseudoCoherent_coheratorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/RelativePseudoCoherenceOfLimit.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/RelativePseudoCoherenceOfLimit.lean#L42). The attribute's comment: “the full statement: for every coherator DQ_X and every derived limit L of (F_n) in D(O_X), the K = DQ_X(L) of 0CX5 is pseudo-coherent relative to A; nothing is granted or assumed”.

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

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.isIso_etaleStageBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EtaleStageBaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EtaleStageBaseChange.lean#L60). The attribute's comment: “the full statement: for every coherator DQ_X and every presentation of L = R lim F_n in D(O_X), every n and every etale U → X with U quasi-compact and quasi-separated, the canonical map RΓ(U, K) ⊗^L_A A_n → RΓ(U_n, F_n) in D(A_n) induced by K = DQ_X(L) → F_n is an isomorphism, U_n = U ×_X X_n; nothing is granted or assumed”.

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

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodExists.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodExists.lean#L56). The attribute's comment: “the full statement: for every coherator DQ_X and every presentation of L = R lim F_n in D(O_X), K = DQ_X(L) has an open subspace W containing X_0 with H^i(K)|_W = 0 for i ≠ 0, H^0(K)|_W of finite presentation, and F_n = H^0(K)|_W ⊗ O_{X_n} through the canonical maps K → F_n; nothing is granted or assumed”.

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

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isExistenceNeighbourhood_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodProperSupport.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/ExistenceNeighbourhoodProperSupport.lean#L148). The attribute's comment: “the full statement: for every K with maps to the Fₙ (in particular the K of 0CX5 with its canonical maps) and every W with the three conclusions of 0CX9, a smaller open W', still with those conclusions, on which the support of H⁰(K)|_W' is proper over A; nothing is granted or assumed”.

> **Stacks 0CXA.** In Situation 0CX4 let `K` be an object of `D(𝒪_X)` with maps
> `πₙ : K ⟶ Fₙ`, and let `W ⊆ X` be an open subspace with the conclusions of Stacks 0CX9
> (`D.IsExistenceNeighbourhood K π W hW`). Then, after shrinking `W` to an open subspace `W'` which
> still has the conclusions of Stacks 0CX9, the support of `F = H⁰(K)|_{W'}` is proper over `A`.
>
> This covers the source's statement as written: its `K` is that of Stacks 0CX5,
> `K = DQ_X(R lim Fₙ)`, here `(spaceQuasicoherentProp _ _ _ _).ι.obj (DQ.obj L)` with the maps
> `D.derivedLimitProjection adj p` for a coherator `adj : ι ⊣ DQ` and a triangle `p` presenting
> `L = R lim_{D(𝒪_X)} Fₙ`, and its `W` is any open subspace with the conclusions of Stacks 0CX9
> for that `K`, which is what `D.IsExistenceNeighbourhood K π W hW` says; the statement below is
> the special case of the one for every `K` and every such `W`.
>
> The source's proof, at the first level: `F` restricted to `X₁` is `F₁` by part (3) of
> Stacks 0CX9, since `W` contains `X₀ = |X₁|`; so the support of `F` meets `X₁` in the support of
> `F₁`, proper over `A₁`, and
> `AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_isOpenSubspace_hasProperSupport`
> (the henselian pair `(A, Ker(A → A₁))` and Stacks 0CWI) shrinks `W`.

```lean
theorem exists_isExistenceNeighbourhood_hasProperSupport
    {K : spaceDerivedCategory D.B D.S D.containsLimitBase D.X.left}
    {π : ∀ n : ℕ, K ⟶ D.derivedSystem.obj (op n)} {W : Subfunctor D.X.left.1}
    {hW : IsOpenSubspace D.B D.S D.containsLimitBase W}
    (hN : D.IsExistenceNeighbourhood K π W hW) :
    ∃ (W' : Subfunctor D.X.left.1) (hW' : IsOpenSubspace D.B D.S D.containsLimitBase W')
      (_ : W' ≤ W), D.IsExistenceNeighbourhood K π W' hW' ∧
      ∃ hlft : IsLocallyOfFiniteType D.B D.S D.containsLimitBase (W'.ι ≫ D.X.hom.hom),
        HasProperSupport D.B D.S D.containsLimitBase hW'.1
          (schemeSpace (limitBaseObject D.system D.B D.containsLimitBase)).2
          (W'.ι ≫ D.X.hom.hom) hlft
          ((SheafOfModules.toSheaf _).obj
            ((modulePullback D.B D.S D.containsLimitBase
              (openSubspaceHom D.B D.S D.containsLimitBase W' hW')).obj
                ((spaceDerivedHomology D.B D.S D.containsLimitBase D.X.left 0).obj K)))
```

## Tag 0CXB, a theorem

[Tag 0CXB](https://stacks.math.columbia.edu/tag/0CXB) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatSheafExistenceSituation.exists_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatExistenceTheorem.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/FlatExistenceTheorem.lean#L50).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
