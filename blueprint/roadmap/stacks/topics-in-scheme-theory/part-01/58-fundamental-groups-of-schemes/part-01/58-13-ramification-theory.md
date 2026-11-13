---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleFundamentalGroupMap_inertiaSquare, AlgebraicGeometry.etaleFundamentalGroupMap_fractionField_strictHenselization_to_henselization, Stacks.RamificationTheory.surjective_and_ker_absoluteGaloisToFundamentalGroup, Stacks.RamificationTheory.inertiaDiagram_translation, AlgebraicGeometry.normalClosure_iUnion_ker_topologicalClosure_le_ker, AlgebraicGeometry.ker_etaleFundamentalGroupMap_stalk_eq_normalClosure_topologicalClosure, AlgebraicGeometry.normalClosure_range_topologicalClosure_le_ker, AlgebraicGeometry.comap_normalClosure_iUnion_ker_le_ker_galoisToFundamentalGroup
statement: formalized
proof: formalized
---

# 58.13 Ramification theory

Section 58.13 of the Stacks Project, [Tag 0BSD](https://stacks.math.columbia.edu/tag/0BSD). 7 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BSV, an equation

[Tag 0BSV](https://stacks.math.columbia.edu/tag/0BSV) in the Stacks Project.

**`AlgebraicGeometry.etaleFundamentalGroupMap_inertiaSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean#L387). The attribute's comment: “right-hand square”.

> **Stacks Project, Tag 0BSV.** The square formed by the generic and local spectra of a ring
> extension commutes on fundamental groups. In the inertia diagram the extension is `A → Ah`, with
> fraction fields `K → Kh`. The heterogeneous equality accounts for the two propositionally equal
> induced geometric points of `Spec A`.

```lean
theorem etaleFundamentalGroupMap_inertiaSquare
    (A Ah K Kh : Type u)
    [CommRing A] [CommRing Ah] [Algebra A Ah]
    [Field K] [Algebra A K]
    [Field Kh] [Algebra Ah Kh] [Algebra K Kh] [Algebra A Kh]
    [IsScalarTower A Ah Kh] [IsScalarTower A K Kh]
    [ConnectedSpace (Spec (.of Ah))] [ConnectedSpace (Spec (.of A))]
    [ConnectedSpace (Spec (.of Kh))] [ConnectedSpace (Spec (.of K))]
    (x : GeometricPoint (Spec (.of Kh)))
    (σ : EtaleFundamentalGroup (Spec (.of Kh)) x) :
    HEq
      (etaleFundamentalGroupMap
        (Spec.map (CommRingCat.ofHom (algebraMap A K)))
        (x.map (Spec.map (CommRingCat.ofHom (algebraMap K Kh))))
        (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom (algebraMap K Kh))) x σ))
      (etaleFundamentalGroupMap
        (Spec.map (CommRingCat.ofHom (algebraMap A Ah)))
        (x.map (Spec.map (CommRingCat.ofHom (algebraMap Ah Kh))))
        (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom (algebraMap Ah Kh))) x σ))
```

**`AlgebraicGeometry.etaleFundamentalGroupMap_fractionField_strictHenselization_to_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean#L423). The attribute's comment: “trivial diagonal”.

> **Stacks Project, Tag 0BSV.** The diagonal of the inertia diagram is the trivial map: it
> factors through the fundamental group of the strictly henselian spectrum of `Ash`, which is
> trivial.

```lean
theorem etaleFundamentalGroupMap_fractionField_strictHenselization_to_henselization
    (A Ah Ash Ksh κsep : Type u)
    [CommRing A] [IsLocalRing A] [IsDomain A] [IsIntegrallyClosed A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash] [Algebra Ah Ash]
    [IsScalarTower A Ah Ash]
    [Field κsep] [Algebra (IsLocalRing.ResidueField A) κsep]
    [IsSepClosure (IsLocalRing.ResidueField A) κsep]
    [IsLocalRing.IsHenselization A κsep Ash]
    [Field Ksh] [Algebra Ash Ksh] [Algebra A Ksh] [IsFractionRing Ash Ksh]
    [Algebra Ah Ksh]
    [IsScalarTower Ah Ash Ksh] [IsScalarTower A Ash Ksh]
    [ConnectedSpace (Spec (.of Ksh))] [ConnectedSpace (Spec (.of Ah))]
    (x : GeometricPoint (Spec (.of Ksh))) :
    etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap Ah Ksh))) x = 1
```

## Tag 0BSW, a lemma

[Tag 0BSW](https://stacks.math.columbia.edu/tag/0BSW) in the Stacks Project.

**`Stacks.RamificationTheory.surjective_and_ker_absoluteGaloisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L388). The attribute's comment: “the lower right corner π₁(X) = Gal(M/K) of the translated diagram, M the maximal subextension unramified with respect to X: the right vertical arrow, from the absolute Galois group of the function field, is surjective with kernel Gal(K^sep/M), for a general integral normal X. The other objects and arrows of the diagram, the square and the kernels are Stacks.RamificationTheory.inertiaDiagram\_translation, which also proves that its right vertical arrow, for X = Spec A, is this one”.

> **Stacks Project, Tag 0BSW.** The right vertical arrow `π₁(U) → π₁(X)` of the diagram is
> surjective, and its kernel is the subgroup fixing the maximal subextension `M` unramified with
> respect to `X` — that is, `Gal(K^sep/M)`.
>
> Both come from Stacks Tag 0BQM, where the arrow is identified with restriction to `M`
> (`AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension_apply`) and `M/K` is shown to be
> Galois (`AlgebraicGeometry.normal_maximalEtaleExtension`): restriction onto a normal
> subextension is surjective with kernel its fixing subgroup.
>
> This is the lower right corner `π₁(X) = Gal(M/K)` of the translated diagram, with the right
> vertical arrow read as restriction to `M`; the rest of the lemma — every other object and arrow,
> the square, and both kernels — is `Stacks.RamificationTheory.inertiaDiagram_translation`, which
> also shows that for `X = Spec A` its right vertical arrow agrees with the one here
> (`exists_absoluteGaloisToFundamentalGroup_eq_etaleFundamentalGroupMap`).

```lean
theorem surjective_and_ker_absoluteGaloisToFundamentalGroup
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    let _ : Normal (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar) :=
      normal_maximalEtaleExtension X sbar hs
    Function.Surjective (absoluteGaloisToFundamentalGroup X sbar) ∧
      (absoluteGaloisToFundamentalGroup X sbar).toMonoidHom.ker =
        (maximalEtaleExtension X sbar).fixingSubgroup
```

**`Stacks.RamificationTheory.inertiaDiagram_translation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 1296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L1296). The attribute's comment: “the whole translated diagram: π₁(U^h) = D with the top arrow the inclusion, the image I of π₁(U^sh), the left vertical arrow D → Gal(κ(𝔪^sh)/κ) surjective with kernel I and identified with π₁(U^h) → π₁(X^h) through an isomorphism Gal(κ(𝔪^sh)/κ) ≅ π₁(X^h), the bottom arrow and the commutative square, and the right vertical arrow surjective with kernel the smallest closed normal subgroup containing I and equal to absoluteGaloisToFundamentalGroup, the arrow which Tag 0BQM identifies with restriction Gal(K^sep/K) → Gal(M/K)”.

> **Stacks Project, Tag 0BSW.** Let `(A, 𝔪, κ)` be a normal local domain with fraction field
> `K`, let `K^sep = L` be a separable closure of `K` inside an algebraically closed algebraic
> extension `Ω`, let `A^sep` be the integral closure of `A` in `K^sep` and `𝔪^sep = q` a maximal
> ideal of `A^sep` over `𝔪`, with decomposition group `D` and inertia group `I` in
> `G = Gal(K^sep/K)`. Let `A^h` be a henselization of `A` with fraction field `K^h`, embedded in
> `K^sep` through the canonical local map `A^h → (A^sep)_{𝔪^sep}` (`hcompat`), let `κ(𝔪^sh)` be a
> separable algebraic closure of `κ` inside `κ(𝔪^sep)`, and write `U = Spec K`, `U^h = Spec K^h`,
> `X = Spec A`, `X^h = Spec A^h`. Then, via the isomorphism `π₁(U) = Gal(K^sep/K)` of Stacks Tag
> 0BNE, the diagram
>
> ```
> π₁(U^sh) → π₁(U^h) → π₁(U)
>              ↓         ↓
>           π₁(X^h) →  π₁(X)
> ```
>
> translates into
>
> ```
> I → D → Gal(K^sep/K)
>     ↓        ↓
>  Gal(κ(𝔪^sh)/κ) → π₁(X)
> ```
>
> in the following sense, objects and arrows alike:
>
> * the top arrow `π₁(U^h) → π₁(U)` is injective with image `D` (so `π₁(U^h) = D`, the arrow
>   being the inclusion), and the image of `π₁(U^sh)` in `π₁(U)` is `I`, for
>   `U^sh = Spec (K^sep)^I` the spectrum of the fraction field of the strict henselization
>   `A^sh = ((A^sep)_{𝔪^sep})^I`;
> * the left vertical arrow `D → Gal(κ(𝔪^sh)/κ)` (`decompositionResidueHom`) is surjective with
>   kernel `I`, so the diagonal `I → Gal(κ(𝔪^sh)/κ)` is trivial;
> * there is an isomorphism `e : Gal(κ(𝔪^sh)/κ) ≅ π₁(X^h)` carrying the left vertical arrow to the
>   arrow `π₁(U^h) → π₁(X^h)`: for `γ ∈ π₁(U^h)` corresponding to `τ ∈ D`, `e(τ̄) = γ|_{X^h}`;
>   this is the identification `π₁(X^h) = Gal(κ(𝔪^sh)/κ)` of the lower left corner, and `e` is
>   determined by this property since the left arrow is surjective;
> * under `e` the bottom arrow `π₁(X^h) → π₁(X)` becomes the bottom arrow `Gal(κ(𝔪^sh)/κ) → π₁(X)`
>   of the translated diagram, i.e. the square commutes: for `τ ∈ D`, the image of `e(τ̄)` in
>   `π₁(X)` is the image of `τ` under the right vertical arrow (a heterogeneous equality, the two
>   geometric points of `X` being equal only propositionally);
> * the right vertical arrow `Gal(K^sep/K) = π₁(U) → π₁(X)` is surjective, and its kernel is the
>   smallest closed normal subgroup of `Gal(K^sep/K)` containing `I`.
> * the right vertical arrow is the arrow `absoluteGaloisToFundamentalGroup` of Stacks Tag 0BQM:
>   every `σ ∈ Gal(K^sep/K)` lifts to an automorphism `τ` of `Ω` over the residue field of `X` at
>   the generic point, and both arrows send them to the same element of `π₁(X)`.
>
> The lower right corner `π₁(X)` is `Gal(M/K)` for `M` the maximal subextension of `K^sep/K`
> unramified with respect to `A` by Stacks Tag 0BQM, which in this library is
> `AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension`, carrying
> `absoluteGaloisToFundamentalGroup` to restriction to `M`
> (`Stacks.RamificationTheory.surjective_and_ker_absoluteGaloisToFundamentalGroup`); the last
> clause on the right vertical arrow identifies it with that arrow, so under Tag 0BQM the right
> vertical arrow is restriction `Gal(K^sep/K) → Gal(M/K)`.
>
> The hypotheses are the source's: `A` a normal local domain, `K^sep` a separable closure of `K`,
> `𝔪^sep` a maximal ideal over `𝔪`, `A^h` a henselization, `κ(𝔪^sh)` a separable closure of `κ`;
> `K^sep` being separably closed, which the canonical map `A^h → (A^sep)_{𝔪^sep}` needs, is derived
> from it being a separable closure.

```lean
theorem inertiaDiagram_translation [q.IsMaximal]
    (hcompat : letI : IsSepClosed L := IsSepClosure.sep_closed K
      ∀ x : Ah, algebraMap Kh L (algebraMap Ah Kh x) =
        IsIntegralClosure.henselizationToField A K L q Ah x)
    (κ : Type uk) [Field κ] [Algebra (A ⧸ maximalIdeal A) κ]
      [IsFractionRing (A ⧸ maximalIdeal A) κ]
    (κmsep : Type ul) [Field κmsep] [Algebra (integralClosure A L ⧸ q) κmsep]
      [IsFractionRing (integralClosure A L ⧸ q) κmsep]
      [Algebra (A ⧸ maximalIdeal A) κmsep]
      [IsScalarTower (A ⧸ maximalIdeal A) (integralClosure A L ⧸ q) κmsep]
      [Algebra κ κmsep] [IsScalarTower (A ⧸ maximalIdeal A) κ κmsep]
    (κmsh : Type us) [Field κmsh] [Algebra κ κmsh] [IsSepClosure κ κmsh]
      [Algebra κmsh κmsep] [IsScalarTower κ κmsh κmsep] :
    letI : ConnectedSpace (Spec (.of A)) := connectedSpace_spec_of_isLocalRing A
    letI : ConnectedSpace (Spec (.of Ah)) := connectedSpace_spec_of_isLocalRing Ah
    letI := IsIntegralClosure.isFractionRing_integralClosure A K L
    letI := IsIntegralClosure.galAction A K L
    letI := IsIntegralClosure.galSMulCommClass A K L
    ∃ hx : (algebraicClosureGeometricPoint Kh Ω).map
        (Spec.map (CommRingCat.ofHom (algebraMap K Kh))) = algebraicClosureGeometricPoint K Ω,
      -- the top row: `π₁(U^h) = D`, the top arrow being the inclusion
      (galoisEquivEtaleFundamentalGroup K L Ω) ⁻¹'
          Set.range (fun γ : EtaleFundamentalGroup (Spec (.of Kh))
              (algebraicClosureGeometricPoint Kh Ω) =>
            hx ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K Kh)))
              (algebraicClosureGeometricPoint Kh Ω) γ) =
        (MulAction.stabilizer Gal(L/K) q : Set Gal(L/K)) ∧
      Function.Injective (fun γ : EtaleFundamentalGroup (Spec (.of Kh))
          (algebraicClosureGeometricPoint Kh Ω) =>
        hx ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K Kh)))
          (algebraicClosureGeometricPoint Kh Ω) γ) ∧
      -- the top row: the image of `π₁(U^sh)` is `I`
      (∃ hx' : (algebraicClosureGeometricPoint
            (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω).map
            (Spec.map (CommRingCat.ofHom (algebraMap K
              (IsIntegralClosure.inertiaFixedField A K L q : Type u)))) =
          algebraicClosureGeometricPoint K Ω,
        (galoisEquivEtaleFundamentalGroup K L Ω) ⁻¹'
            Set.range (fun τ : EtaleFundamentalGroup
                (Spec (.of (IsIntegralClosure.inertiaFixedField A K L q : Type u)))
                (algebraicClosureGeometricPoint
                  (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω) =>
              hx' ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K
                  (IsIntegralClosure.inertiaFixedField A K L q : Type u))))
                (algebraicClosureGeometricPoint
                  (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω) τ) =
          (q.inertia Gal(L/K) : Set Gal(L/K))) ∧
      -- the left vertical arrow `D → Gal(κ(𝔪^sh)/κ)`: surjective with kernel `I`
      Function.Surjective (decompositionResidueHom A K L (integralClosure A L) q κ κmsep κmsh) ∧
      (decompositionResidueHom A K L (integralClosure A L) q κ κmsep κmsh).ker =
        q.inertia (MulAction.stabilizer Gal(L/K) q) ∧
      -- the right vertical arrow: surjective, kernel the closed normal subgroup generated by `I`
      Function.Surjective (fun σ : Gal(L/K) =>
        etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A K)))
          (algebraicClosureGeometricPoint K Ω) (galoisEquivEtaleFundamentalGroup K L Ω σ)) ∧
      Subgroup.comap (galoisEquivEtaleFundamentalGroup K L Ω).toMonoidHom
          (MonoidHom.ker (etaleFundamentalGroupMap
            (Spec.map (CommRingCat.ofHom (algebraMap A K)))
            (algebraicClosureGeometricPoint K Ω)).toMonoidHom) =
        (Subgroup.normalClosure
          ((q.inertia Gal(L/K) : Subgroup Gal(L/K)) : Set Gal(L/K))).topologicalClosure ∧
      -- the right vertical arrow is the arrow `absoluteGaloisToFundamentalGroup` of Tag 0BQM,
      -- whose target is `Gal(M/K)` through `fundamentalGroupIsoGalMaximalEtaleExtension`
      (∀ σ : Gal(L/K), ∃ τ : Gal(((algebraicClosureGeometricPoint K Ω).map
            (Spec.map (CommRingCat.ofHom (algebraMap A K)))).residueField /
          (Spec (.of A)).residueField (((algebraicClosureGeometricPoint K Ω).map
            (Spec.map (CommRingCat.ofHom (algebraMap A K)))).hom default)),
        (∀ y : L, τ (algebraMap L Ω y) = algebraMap L Ω (σ y)) ∧
        absoluteGaloisToFundamentalGroup (Spec (.of A))
            ((algebraicClosureGeometricPoint K Ω).map
              (Spec.map (CommRingCat.ofHom (algebraMap A K)))) τ =
          etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A K)))
            (algebraicClosureGeometricPoint K Ω) (galoisEquivEtaleFundamentalGroup K L Ω σ)) ∧
      -- `π₁(X^h) = Gal(κ(𝔪^sh)/κ)`, carrying the left arrows to each other, and the square
      ∃ e : Gal(κmsh/κ) ≃* EtaleFundamentalGroup (Spec (.of Ah))
          ((algebraicClosureGeometricPoint Kh Ω).map
            (Spec.map (CommRingCat.ofHom (algebraMap Ah Kh)))),
        ∀ (γ : EtaleFundamentalGroup (Spec (.of Kh)) (algebraicClosureGeometricPoint Kh Ω))
          (τ : MulAction.stabilizer Gal(L/K) q),
          galoisEquivEtaleFundamentalGroup K L Ω τ =
              hx ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K Kh)))
                (algebraicClosureGeometricPoint Kh Ω) γ →
            e (decompositionResidueHom A K L (integralClosure A L) q κ κmsep κmsh τ) =
                etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap Ah Kh)))
                  (algebraicClosureGeometricPoint Kh Ω) γ ∧
              HEq (etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A Ah)))
                  ((algebraicClosureGeometricPoint Kh Ω).map
                    (Spec.map (CommRingCat.ofHom (algebraMap Ah Kh))))
                  (e (decompositionResidueHom A K L (integralClosure A L) q κ κmsep κmsh τ)))
                (etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A K)))
                  (algebraicClosureGeometricPoint K Ω)
                  (galoisEquivEtaleFundamentalGroup K L Ω τ))
```

## Tag 0BTD, a lemma

[Tag 0BTD](https://stacks.math.columbia.edu/tag/0BTD) in the Stacks Project.

**`AlgebraicGeometry.normalClosure_iUnion_ker_topologicalClosure_le_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L335). The attribute's comment: “the inclusion of subgroup (3) in subgroup (1), and only that inclusion: subgroup (1) is the kernel of π₁(Spec K) → π₁(X) rather than the subgroup fixing the maximal unramified subextension, so no Noetherian hypothesis is needed, and subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪\_\{X,x}) as generators; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

> **Stacks Project, Tag 0BTD, the inclusion of subgroup (3) in subgroup (1).** Let `X` be an
> integral scheme with function field `K`. The smallest closed normal subgroup of `π₁(Spec K)`
> containing the kernel of `π₁(Spec K) → π₁(Spec 𝒪_{X,x})` for every point `x` of `X` is contained
> in the kernel of `π₁(Spec K) → π₁(X)`.
>
> For `X` normal the generating kernels are exactly the closed normal subgroups generated by the
> images of the `π₁(Spec K_x^sh)`, by
> `AlgebraicGeometry.ker_etaleFundamentalGroupMap_stalk_eq_normalClosure_topologicalClosure`
> together with
> `Stacks.FundamentalGroup.normalClosure_iUnion_topologicalClosure_eq`, so the subgroup on the left
> is the third subgroup of the source and the one on the right is the first.

```lean
theorem normalClosure_iUnion_ker_topologicalClosure_le_ker [IsIntegral X]
    (p : GeometricPoint (Spec (X.residueField (genericPoint X)))) :
    (Subgroup.normalClosure (⋃ x : X,
          (((etaleFundamentalGroupMap (Spec.map (stalkToGenericResidueField X x))
            p).toMonoidHom.ker : Subgroup (EtaleFundamentalGroup
              (Spec (X.residueField (genericPoint X))) p)) : Set _))).topologicalClosure ≤
      (etaleFundamentalGroupMap (X.fromSpecResidueField (genericPoint X))
        p).toMonoidHom.ker
```

**`AlgebraicGeometry.ker_etaleFundamentalGroupMap_stalk_eq_normalClosure_topologicalClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L362). The attribute's comment: “that each generator of subgroup (3) used here — the kernel of π₁(Spec K) → π₁(Spec 𝒪\_\{X,x}) — is the smallest closed normal subgroup containing the image of π₁(Spec K\_x^sh) = Gal(K^sep/K\_x^sh), which is how the source presents subgroup (3); this is Tag 0BSM applied to the local rings of X”.

> **Stacks Project, Tag 0BTD, the generators of subgroup (3).** Let `X` be a normal integral
> scheme with function field `K`, let `x` be a point of `X`, let `Ash` be a strict henselization of
> `𝒪_{X,x}` and let `Ksh = K_x^sh` be its fraction field. The kernel of
> `π₁(Spec K) → π₁(Spec 𝒪_{X,x})` is the smallest closed normal subgroup of `π₁(Spec K)`
> containing the image of `π₁(Spec Ksh) = Gal(K^sep/K_x^sh)`.
>
> This is the local exact sequence of Stacks Tag 0BSM applied to the local ring at `x`, whose
> fraction field is the function field of `X` by
> `AlgebraicGeometry.isFractionRing_stalk_genericResidueField`.

```lean
theorem ker_etaleFundamentalGroupMap_stalk_eq_normalClosure_topologicalClosure
    [IsIntegral X] [IsNormal X] (x : X) (κsep Ash Ksh : Type u)
    [CommRing Ash] [IsLocalRing Ash] [Algebra (X.presheaf.stalk x) Ash]
    [Field κsep] [Algebra (ResidueField (X.presheaf.stalk x)) κsep]
    [IsSepClosure (ResidueField (X.presheaf.stalk x)) κsep]
    [IsHenselization (X.presheaf.stalk x) κsep Ash]
    [Field Ksh] [Algebra Ash Ksh] [IsFractionRing Ash Ksh]
    [Algebra (X.presheaf.stalk x) Ksh]
    [Algebra (X.residueField (genericPoint X)) Ksh]
    [IsScalarTower (X.presheaf.stalk x) (X.residueField (genericPoint X)) Ksh]
    [IsScalarTower (X.presheaf.stalk x) Ash Ksh]
    (q : GeometricPoint (Spec (.of Ksh))) :
    (etaleFundamentalGroupMap (Spec.map (stalkToGenericResidueField X x))
        (q.map (Spec.map (CommRingCat.ofHom
          (algebraMap (X.residueField (genericPoint X)) Ksh))))).toMonoidHom.ker =
      (Subgroup.normalClosure (Set.range (etaleFundamentalGroupMap
        (Spec.map (CommRingCat.ofHom
          (algebraMap (X.residueField (genericPoint X)) Ksh))) q))).topologicalClosure
```

**`AlgebraicGeometry.normalClosure_range_topologicalClosure_le_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L397). The attribute's comment: “that each generator Gal(K^sep/K\_x^sh) of subgroup (3) generates a closed normal subgroup contained in subgroup (1), one point x of X at a time; subgroup (1) is the kernel of π₁(Spec K) → π₁(X), so no Noetherian hypothesis is needed; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

> **Stacks Project, Tag 0BTD, one generator of subgroup (3) lies in subgroup (1).** Let `X` be
> a normal integral scheme with function field `K`, let `x` be a point of `X`, let `Ash` be a
> strict henselization of `𝒪_{X,x}` and let `Ksh = K_x^sh` be its fraction field. The smallest
> closed normal subgroup of `π₁(Spec K)` containing the image of
> `π₁(Spec K_x^sh) = Gal(K^sep/K_x^sh)` is contained in the kernel of `π₁(Spec K) → π₁(X)`.
>
> This is the first paragraph of the source's proof, one point of `X` at a time: the image is
> killed already by `π₁(Spec K) → π₁(Spec 𝒪_{X,x})`, by the local exact sequence of Stacks Tag
> 0BSM, and that homomorphism is a factor of `π₁(Spec K) → π₁(X)`.

```lean
theorem normalClosure_range_topologicalClosure_le_ker
    [IsIntegral X] [IsNormal X] (x : X) (κsep Ash Ksh : Type u)
    [CommRing Ash] [IsLocalRing Ash] [Algebra (X.presheaf.stalk x) Ash]
    [Field κsep] [Algebra (ResidueField (X.presheaf.stalk x)) κsep]
    [IsSepClosure (ResidueField (X.presheaf.stalk x)) κsep]
    [IsHenselization (X.presheaf.stalk x) κsep Ash]
    [Field Ksh] [Algebra Ash Ksh] [IsFractionRing Ash Ksh]
    [Algebra (X.presheaf.stalk x) Ksh]
    [Algebra (X.residueField (genericPoint X)) Ksh]
    [IsScalarTower (X.presheaf.stalk x) (X.residueField (genericPoint X)) Ksh]
    [IsScalarTower (X.presheaf.stalk x) Ash Ksh]
    (q : GeometricPoint (Spec (.of Ksh))) :
    (Subgroup.normalClosure (Set.range (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom
            (algebraMap (X.residueField (genericPoint X)) Ksh))) q))).topologicalClosure ≤
      (etaleFundamentalGroupMap (X.fromSpecResidueField (genericPoint X))
        (q.map (Spec.map (CommRingCat.ofHom
          (algebraMap (X.residueField (genericPoint X)) Ksh))))).toMonoidHom.ker
```

**`AlgebraicGeometry.comap_normalClosure_iUnion_ker_le_ker_galoisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L449). The attribute's comment: “the inclusion of subgroup (3) in subgroup (1) read inside Gal(K^sep/K) through the identification of Tag 0BNE; subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪\_\{X,x}) as generators; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

> **Stacks Project, Tag 0BTD, the inclusion of subgroup (3) in subgroup (1), inside
> `Gal(K^sep/K)`.** Transporting along the identification `Gal(K^sep/K) = π₁(Spec K)` of Stacks Tag
> 0BNE, the smallest closed normal subgroup of `Gal(K^sep/K)` containing the kernel of
> `Gal(K^sep/K) → π₁(Spec 𝒪_{X,x})` for every point `x` of `X` is contained in the kernel of
> `Gal(K^sep/K) → π₁(X)`.

```lean
theorem comap_normalClosure_iUnion_ker_le_ker_galoisToFundamentalGroup :
    Subgroup.comap (galoisEquivEtaleFundamentalGroup
        (X.residueField (genericPoint X)) L Ω).toMonoidHom
      ((Subgroup.normalClosure (⋃ x : X,
          (((etaleFundamentalGroupMap (Spec.map (stalkToGenericResidueField X x))
            (algebraicClosureGeometricPoint
              (X.residueField (genericPoint X)) Ω)).toMonoidHom.ker : Subgroup
                (EtaleFundamentalGroup (Spec (X.residueField (genericPoint X)))
                  (algebraicClosureGeometricPoint
                    (X.residueField (genericPoint X)) Ω))) : Set _))).topologicalClosure) ≤
      (galoisToFundamentalGroup X L Ω).toMonoidHom.ker
```

**`AlgebraicGeometry.inertiaClosedNormalSubgroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 589](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L589). The attribute's comment: “subgroup (2): the smallest closed normal subgroup of Gal(K^sep/K) containing the inertia group I\_y for every point y of the normalization X^sep of X in K^sep, with the points of X^sep over a nonempty affine open U of X presented as the primes of the integral closure of Γ(X, U) in K^sep”.

> **Subgroup (2) of Stacks Tag 0BTD.** The smallest closed normal subgroup of
> `Gal(K^sep/K) = π₁(Spec K)` containing the inertia group `I_y` for every point `y` of the
> normalization `X^sep` of `X` in `K^sep`.

```lean
def inertiaClosedNormalSubgroup : Subgroup Gal(L / X.residueField (genericPoint X))
```

**`AlgebraicGeometry.isFinite_etale_fromNormalization_of_inertiaGenerators_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 723](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L723). The attribute's comment: “the second paragraph of the proof: triviality of the inertia groups I\_y on a finite Galois subextension F of K^sep/K makes X unramified in F”. References: SGA 1 V (2.2), “(ii)”; SGA 1 V (2.3), “special case”.

> **Stacks Tag 0BTD, the inertia criterion for unramifiedness.** Let `X` be a normal integral
> scheme with function field `K` and let `F` be a finite Galois subextension of `K^sep / K` whose
> fixing subgroup contains every inertia group `I_y` for `y` a point of `X^sep` — equivalently,
> with `F` inside the fixed field of subgroup (2). Then the normalization of `X` in `F` is finite
> étale over `X`, that is, `X` is unramified in `F`.
>
> This is the second paragraph of the source's proof. The points of `X^sep` over a nonempty affine
> open `U` of `X` are the primes of the integral closure `C` of `Γ(X, U)` in `K^sep`, and the
> points of the normalization of `X` in `F` over `U` are the primes of the integral closure `B` of
> `Γ(X, U)` in `F`. Every prime of `B` is the contraction of a prime of `C`, and restriction
> carries the inertia group at a prime of `C` onto the inertia group at its contraction, which is
> Stacks Tag 0BSX. The hypothesis makes every element of the former restrict to the identity, so
> all the latter are trivial and the normalization is unramified by Stacks Tag 0BTF.

```lean
theorem isFinite_etale_fromNormalization_of_inertiaGenerators_subset
    (F : IntermediateField (X.residueField (genericPoint X)) L)
    [FiniteDimensional (X.residueField (genericPoint X)) F]
    [IsGalois (X.residueField (genericPoint X)) F]
    (hF : inertiaGenerators X L ⊆
      (F.fixingSubgroup : Set Gal(L/X.residueField (genericPoint X)))) :
    let f : Spec (.of (F : Type u)) ⟶ X :=
      Spec.map (CommRingCat.ofHom
        (algebraMap (X.residueField (genericPoint X)) (F : Type u))) ≫
        X.fromSpecResidueField (genericPoint X)
    IsFinite f.fromNormalization ∧ Etale f.fromNormalization
```

**`AlgebraicGeometry.ker_galoisToFundamentalGroup_le_inertiaClosedNormalSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L851). The attribute's comment: “the inclusion of subgroup (1) in subgroup (2), and only that inclusion: subgroup (1) is the kernel of Gal(K^sep/K) → π₁(X) and subgroup (2) is the closed normal subgroup generated by the inertia groups I\_y; the reverse inclusion (2) ⊆ (3) needs the conjugacy of I\_y with Gal(K^sep/K\_x^sh) from Tag 0BSW, is AlgebraicGeometry.inertiaClosedNormalSubgroup\_le\_stalkKerClosedNormalSubgroup below”.

> **Stacks Tag 0BTD, the reverse inclusion `(1) ⊆ (2)`.** Let `X` be a normal integral scheme
> with function field `K`. The kernel of the surjection `Gal(K^sep/K) → π₁(X)` is contained in the
> smallest closed normal subgroup of `Gal(K^sep/K)` containing the inertia group `I_y` for every
> point `y` of the normalization `X^sep` of `X` in `K^sep`.
>
> This is the second half of the source's proof. Subgroup `(2)` is closed and normal, so it is the
> subgroup fixing its fixed field `F`, and `F` is normal over `K`; hence it suffices to see that
> every element of the kernel fixes each element `x` of `F`. The finite Galois subextension
> generated by `x` lies in `F`, so every inertia group restricts to the identity on it, so `X` is
> unramified in it by
> `AlgebraicGeometry.isFinite_etale_fromNormalization_of_inertiaGenerators_subset`, so every
> element of the kernel fixes it by
> `AlgebraicGeometry.mem_fixingSubgroup_of_galoisToFundamentalGroup_eq_one`.

```lean
theorem ker_galoisToFundamentalGroup_le_inertiaClosedNormalSubgroup
    (Ω : Type u) [Field Ω] [Algebra L Ω] [Algebra (X.residueField (genericPoint X)) Ω]
    [IsScalarTower (X.residueField (genericPoint X)) L Ω]
    [IsAlgClosed Ω] [Algebra.IsAlgebraic (X.residueField (genericPoint X)) Ω] :
    (galoisToFundamentalGroup X L Ω).toMonoidHom.ker ≤ inertiaClosedNormalSubgroup X L
```

**`AlgebraicGeometry.inertiaClosedNormalSubgroup_le_stalkKerClosedNormalSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 969](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L969). The attribute's comment: “the inclusion of subgroup (2) in subgroup (3), which together with the inclusions (3) ⊆ (1) and (1) ⊆ (2) above gives the equality of the three subgroups; subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪\_\{X,x}) as generators and is read inside Gal(K^sep/K) through the identification of Tag 0BNE”.

> **Stacks Tag 0BTD, the inclusion `(2) ⊆ (3)`.** Let `X` be a normal integral scheme with
> function field `K`. The smallest closed normal subgroup of `Gal(K^sep/K)` containing the inertia
> group `I_y` for every point `y` of the normalization `X^sep` of `X` in `K^sep` is contained in the
> smallest closed normal subgroup containing the kernel of `π₁(Spec K) → π₁(Spec 𝒪_{X,x})` for
> every point `x` of `X`.
>
> This is the inclusion the source gets from the conjugacy of `I_y` with `Gal(K^sep/K_x^sh)`. A
> point `y` of `X^sep` over a nonempty affine open `U` of `X` is a prime `r` of the integral closure
> `C` of `Γ(X, U)` in `K^sep`; the point `x` of `U` it lies over is the prime `r ∩ Γ(X, U)`, and
> `𝒪_{X,x}` is the localization of `Γ(X, U)` there. Taking the integral closure commutes with that
> localization and the inertia group is insensitive to it
> (`IsIntegralClosure.exists_isMaximal_inertia_eq_of_isLocalization`), so `I_y` is the inertia group
> at a maximal ideal of the integral closure of `𝒪_{X,x}` in `K^sep`; by
> `Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia` that
> inertia group lies in the kernel of `π₁(Spec K) → π₁(Spec 𝒪_{X,x})`.
>
> With `AlgebraicGeometry.comap_normalClosure_iUnion_ker_le_ker_galoisToFundamentalGroup` and
> `AlgebraicGeometry.ker_galoisToFundamentalGroup_le_inertiaClosedNormalSubgroup` this closes the
> cycle `(3) ⊆ (1) ⊆ (2) ⊆ (3)`, so the three subgroups of the source are equal.

```lean
theorem inertiaClosedNormalSubgroup_le_stalkKerClosedNormalSubgroup :
    inertiaClosedNormalSubgroup X L ≤ stalkKerClosedNormalSubgroup X L Ω
```

**`AlgebraicGeometry.ker_galoisToFundamentalGroup_eq_inertiaClosedNormalSubgroup_and_stalkKer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 1068](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L1068). The attribute's comment: “the equality of the three subgroups, assembled from the cycle (3) ⊆ (1) ⊆ (2) ⊆ (3); subgroup (1) is the kernel of Gal(K^sep/K) → π₁(X) rather than the subgroup fixing the maximal unramified subextension, so no Noetherian hypothesis is needed, and subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪\_\{X,x}) as generators”.

> **Stacks Tag 0BTD.** Let `X` be a normal integral scheme with function field `K`. The three
> subgroups of `Gal(K^sep/K)` of the source are equal: the kernel of `Gal(K^sep/K) → π₁(X)`, the
> smallest closed normal subgroup containing the inertia group `I_y` at every point `y` of the
> normalization of `X` in `K^sep`, and the smallest closed normal subgroup containing the kernel of
> `π₁(Spec K) → π₁(Spec 𝒪_{X,x})` for every point `x` of `X`.
>
> The three inclusions `(3) ⊆ (1)`, `(1) ⊆ (2)` and `(2) ⊆ (3)` proved above close into a cycle.

```lean
theorem ker_galoisToFundamentalGroup_eq_inertiaClosedNormalSubgroup_and_stalkKer :
    (galoisToFundamentalGroup X L Ω).toMonoidHom.ker = inertiaClosedNormalSubgroup X L ∧
      (galoisToFundamentalGroup X L Ω).toMonoidHom.ker =
        stalkKerClosedNormalSubgroup X L Ω
```

## Tag 0BTE, an example

[Tag 0BTE](https://stacks.math.columbia.edu/tag/0BTE) in the Stacks Project.

**`MvPolynomial.mem_evenSubalgebra_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L190). The attribute's comment: “the invariant subring k[tᵢtⱼ]”.

> The subring `k[tᵢtⱼ]` consists of the polynomials all of whose monomials have even degree.

```lean
theorem mem_evenSubalgebra_iff {f : MvPolynomial σ k} :
    f ∈ evenSubalgebra k σ ↔ ∀ m ∈ f.support, Even (Finsupp.degree m)
```

**`MvPolynomial.mem_evenSubalgebra_iff_negVars_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L206). The attribute's comment: “the invariant subring k[tᵢtⱼ]”.

> The subring `k[tᵢtⱼ]` is the ring of invariants of the `±1`-action, provided `2 ≠ 0`.

```lean
theorem mem_evenSubalgebra_iff_negVars_eq (h2 : (2 : k) ≠ 0) {f : MvPolynomial σ k} :
    f ∈ evenSubalgebra k σ ↔ negVars k σ f = f
```

**`MvPolynomial.finite_evenSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L297). The attribute's comment: “the degree two morphism”.

> The polynomial ring in finitely many variables is a finite module over `k[tᵢtⱼ]`: the morphism
> `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is finite.

```lean
theorem finite_evenSubalgebra [Finite σ] :
    Module.Finite (evenSubalgebra k σ) (MvPolynomial σ k)
```

**`MvPolynomial.rank_evenSubalgebra_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L337). The attribute's comment: “the degree two morphism”.

> The polynomial ring has rank two as a module over `k[tᵢtⱼ]`: the morphism
> `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` has degree two.

```lean
theorem rank_evenSubalgebra_eq_two (h2 : (2 : k) ≠ 0) [Nonempty σ] :
    Module.rank (evenSubalgebra k σ) (MvPolynomial σ k) = 2
```

**`MvPolynomial.finrank_evenSubalgebra_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L372). The attribute's comment: “the degree two morphism”.

> The polynomial ring in finitely many variables has rank two as a module over `k[tᵢtⱼ]`.

```lean
theorem finrank_evenSubalgebra_eq_two (h2 : (2 : k) ≠ 0) [Nonempty σ] :
    Module.finrank (evenSubalgebra k σ) (MvPolynomial σ k) = 2
```

**`MvPolynomial.isUnramifiedAt_of_under_ne_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L580). The attribute's comment: “unramified away from the vertex”.

> The morphism `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is unramified at every point of `𝐀ⁿ_k` which does not
> lie over the vertex `𝔪 = (tᵢtⱼ)`.

```lean
theorem isUnramifiedAt_of_under_ne_vertexIdeal (h2 : (2 : k) ≠ 0) (q : Ideal (MvPolynomial σ k))
    [q.IsPrime] (hq : q.under (evenSubalgebra k σ) ≠ vertexIdeal k σ) :
    Algebra.IsUnramifiedAt (evenSubalgebra k σ) q
```

**`MvPolynomial.not_isUnramifiedAt_idealOfVars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L639). The attribute's comment: “ramified at the vertex”.

> The morphism `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is ramified at the vertex `(t₁, …, tₙ)` of `𝐀ⁿ_k`, which
> lies over the vertex `𝔪 = (tᵢtⱼ)`.

```lean
theorem not_isUnramifiedAt_idealOfVars [Nonempty σ] :
    ¬ Algebra.IsUnramifiedAt (evenSubalgebra k σ) (idealOfVars σ k)
```

**`MvPolynomial.height_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 744](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L744). The attribute's comment: “the vertex has codimension n”.

> The vertex `𝔪 = (tᵢtⱼ)` has height `n` in `k[tᵢtⱼ]` for `n` variables: it is a point of
> codimension `n` of the quotient.

```lean
theorem height_vertexIdeal (n : ℕ) : (vertexIdeal k (Fin n)).height = n
```

**`MvPolynomial.one_lt_height_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L759). The attribute's comment: “ramification in codimension greater than one”.

> For at least two variables the vertex `𝔪 = (tᵢtⱼ)` has codimension greater than one, so the
> ramification of `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is not visible in codimension one.

```lean
theorem one_lt_height_vertexIdeal {n : ℕ} (hn : 2 ≤ n) : 1 < (vertexIdeal k (Fin n)).height
```

## Tag 0BTF, a lemma

[Tag 0BTF](https://stacks.math.columbia.edu/tag/0BTF) in the Stacks Project.

**`AlgebraicGeometry.normalization_unramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean, line 2218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean#L2218). The attribute's comment: “conditions (1)–(8)”.

> **Unramifiedness of the normalization of a normal integral scheme in a finite extension of
> its function field.** For `X` integral and normal with function field `K`, a finite extension
> `L / K` and `f : Y ⟶ X` the normalization of `X` in `L`, the following are equivalent: `f` is
> unramified (which is the definition of `X` being unramified in `L`); `f` is étale; `f` is finite
> étale; `f` becomes unramified over `Spec` of every local ring of `X`; the same over every
> henselization of a local ring of `X`; the same over every strict henselization; and every
> scheme-theoretic fibre of `f` is étale and finite locally free of some rank at least
> `[L : K]`.

```lean
public theorem normalization_unramified_tfae
    (X : Scheme.{u}) [IsIntegral X] [IsNormal X]
    (L : Type u) [Field L] [Algebra X.functionField L]
    [FiniteDimensional X.functionField L]
    (i : Spec (.of L) ⟶ X)
    (hi : i = Spec.map (CommRingCat.ofHom
      (algebraMap X.functionField L)) ≫ X.fromSpecStalk (genericPoint X))
    [QuasiCompact i] [QuasiSeparated i] :
    let f : i.normalization ⟶ X := i.fromNormalization
    List.TFAE [
      Unramified f,
      Etale f,
      IsFinite f ∧ Etale f,
      (∀ x : X, Unramified
        (pullback.snd f (X.fromSpecStalk x))),
      (∀ (x : X) (R : Type u) [CommRing R] [IsLocalRing R]
        [Algebra (X.presheaf.stalk x) R]
        [IsLocalRing.IsHenselization (X.presheaf.stalk x)
          (ResidueField (X.presheaf.stalk x)) R],
        Unramified
          (pullback.snd f
            (Spec.map (CommRingCat.ofHom
              (algebraMap (X.presheaf.stalk x) R)) ≫ X.fromSpecStalk x))),
      (∀ (x : X) (κsep : Type u) [Field κsep]
        [Algebra (ResidueField (X.presheaf.stalk x)) κsep]
        [IsSepClosure (ResidueField (X.presheaf.stalk x)) κsep]
        (R : Type u) [CommRing R] [IsLocalRing R]
        [Algebra (X.presheaf.stalk x) R]
        [IsLocalRing.IsHenselization (X.presheaf.stalk x) κsep R],
        Unramified
          (pullback.snd f
            (Spec.map (CommRingCat.ofHom
              (algebraMap (X.presheaf.stalk x) R)) ≫ X.fromSpecStalk x))),
      (∀ x : X, ∃ d : ℕ, Module.finrank X.functionField L ≤ d ∧
        Stacks.Morphisms.IsFiniteLocallyFreeOfRank (f.fiberToSpecResidueField x) d ∧
        Etale (f.fiberToSpecResidueField x))]
```

**`AlgebraicGeometry.normalization_unramified_iff_trivialInertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean, line 2415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean#L2415). The attribute's comment: “condition (9)”.

> **The Galois case: unramifiedness of the normalization is triviality of every inertia
> group.** For `X` integral and normal with function field `K` and `L / K` finite Galois with
> group `G = Gal(L/K)`, the normalization of `X` in `L` is unramified exactly when, on every
> nonempty affine open `U` of `X` and for every prime `q` of the integral closure of `Γ(X, U)` in
> `L`, the only `σ ∈ G` fixing `q` elementwise and inducing the identity modulo `q` is the
> identity; that is, exactly when every inertia group
> `I_q = {σ ∈ G | σ(q) = q and σ ≡ id mod q}` is trivial.

```lean
public theorem normalization_unramified_iff_trivialInertia
    (X : Scheme.{u}) [IsIntegral X] [IsNormal X]
    (L : Type u) [Field L] [Algebra X.functionField L]
    [FiniteDimensional X.functionField L] [IsGalois X.functionField L]
    (i : Spec (.of L) ⟶ X)
    (hi : i = Spec.map (CommRingCat.ofHom
      (algebraMap X.functionField L)) ≫ X.fromSpecStalk (genericPoint X))
    [QuasiCompact i] [QuasiSeparated i] :
    Unramified i.fromNormalization ↔
      ∀ (U : X.Opens) (hU : IsAffineOpen U) [Nonempty U],
        letI : Algebra Γ(X, U) L :=
          ((algebraMap X.functionField L).comp
            (X.germToFunctionField U).hom).toAlgebra
        letI : IsScalarTower Γ(X, U) X.functionField L :=
          .of_algebraMap_eq' rfl
        letI : IsFractionRing Γ(X, U) X.functionField :=
          functionField_isFractionRing_of_isAffineOpen X U hU
        ∀ (q : Ideal (integralClosure Γ(X, U) L)) (_hq : q.IsPrime)
          (σ : L ≃ₐ[X.functionField] L),
          ((∀ y, y ∈ q ↔
              galRestrict Γ(X, U) X.functionField L
                (integralClosure Γ(X, U) L) σ y ∈ q) ∧
            (∀ y, galRestrict Γ(X, U) X.functionField L
              (integralClosure Γ(X, U) L) σ y - y ∈ q)) →
          σ = 1
```

## Tag 0BUA, a lemma

[Tag 0BUA](https://stacks.math.columbia.edu/tag/0BUA) in the Stacks Project.

**`Stacks.FundamentalGroup.exists_tameInertiaCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 1208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L1208). The attribute's comment: “the wild–tame exact sequence and canonical character”. References: SGA 1 XIII (2.0), “inertia structure”; SGA 7 I (0.3), “I/P ≅ Ẑ(1), P pro-p”.

> The canonical tame character has a pro-primary kernel and maps onto all compatible
> families of prime-to-residue-characteristic roots of unity.

```lean
public theorem exists_tameInertiaCharacter
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsGalois K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    let I := P.inertia Gal(L/K)
    let D := MulAction.stabilizer Gal(L/K) P
    let p := ringChar (IsLocalRing.ResidueField A)
    ∃ S : Set ℕ,
      1 ∈ S ∧
      (∀ n ∈ S, 0 < n) ∧
      (p ≠ 0 → ∀ n ∈ S, Nat.Coprime n p) ∧
      (∀ n ∈ S, ∃ z : B ⧸ P, IsPrimitiveRoot z n) ∧
      (∀ n ∈ S, ∀ m ∈ S, ∃ k ∈ S, n ∣ k ∧ m ∣ k) ∧
      (∀ n ∈ S, ∃ (F : FiniteGaloisIntermediateField K L),
        let C := integralClosure A F
        letI : IsScalarTower A F L :=
          IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
        let f : C →ₐ[A] B :=
          (IsScalarTower.toAlgHom A F L).mapIntegralClosure
        let q := P.comap f.toRingHom
        ∃ hq : q.IsMaximal,
          letI : q.IsMaximal := hq
          n ∣ IsDiscreteValuationRing.tameRamificationIndex A F q) ∧
      ∃ θ : I →* (∀ _ : S, (B ⧸ P)ˣ),
        (∀ σ : I, ∀ n : S, (θ σ n) ^ n.1 = 1) ∧
        (∀ σ : I, ∀ n m : S, n.1 ∣ m.1 →
          (θ σ m) ^ (m.1 / n.1) = θ σ n) ∧
        (∀ f : ∀ _ : S, (B ⧸ P)ˣ,
          (∀ n : S, (f n) ^ n.1 = 1) →
          (∀ n m : S, n.1 ∣ m.1 → (f m) ^ (m.1 / n.1) = f n) →
          ∃ σ : I, θ σ = f) ∧
        (∀ τ : D, ∀ σ : I,
          ∃ ρ : I,
            (ρ : Gal(L/K)) = (τ : Gal(L/K)) * (σ : Gal(L/K)) *
              (τ : Gal(L/K))⁻¹ ∧
            ∀ n : S, θ ρ n =
              (Ideal.quotientEquiv P P
                ((MulSemiringAction.toRingEquiv Gal(L/K) B) (τ : Gal(L/K)))
                τ.property.symm).toMulEquiv (θ σ n)) ∧
        (∀ τ : D, ∀ σ : I, σ ∈ θ.ker →
          ∃ ρ : I,
            (ρ : Gal(L/K)) = (τ : Gal(L/K)) * (σ : Gal(L/K)) *
              (τ : Gal(L/K))⁻¹ ∧ ρ ∈ θ.ker) ∧
        (∀ (F : FiniteGaloisIntermediateField K L),
          let C := integralClosure A F
          letI : IsScalarTower A F L :=
            IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
          letI : MulSemiringAction Gal(F/K) C :=
            IsIntegralClosure.MulSemiringAction A K F C
          let f : C →ₐ[A] B :=
            (IsScalarTower.toAlgHom A F L).mapIntegralClosure
          let q := P.comap f.toRingHom
          ∀ [q.IsMaximal],
            ∃ hF : IsDiscreteValuationRing.tameRamificationIndex A F q ∈ S,
              ∀ σ : I,
                ∃ σF : q.inertia Gal(F/K),
                  (σF : Gal(F/K)) =
                    AlgEquiv.restrictNormal (σ : Gal(L/K))
                      (F : IntermediateField K L) ∧
                  ((θ σ ⟨IsDiscreteValuationRing.tameRamificationIndex A F q, hF⟩ :
                    (B ⧸ P)ˣ) : B ⧸ P) =
                    (Ideal.quotientMap P f.toRingHom le_rfl)
                      ((IsDiscreteValuationRing.canonicalInertiaCharacter A K F q σF).1.1)) ∧
        (∀ σ : I, σ ∈ θ.ker ↔
          ∀ (F : FiniteGaloisIntermediateField K L),
            let C := integralClosure A F
            letI : IsScalarTower A F L :=
              IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
            letI : MulSemiringAction Gal(F/K) C :=
              IsIntegralClosure.MulSemiringAction A K F C
            let f : C →ₐ[A] B :=
              (IsScalarTower.toAlgHom A F L).mapIntegralClosure
            let q := P.comap f.toRingHom
            ∀ [q.IsMaximal],
              ∃ σF : q.inertia Gal(F/K),
                (σF : Gal(F/K)) =
                  AlgEquiv.restrictNormal (σ : Gal(L/K))
                    (F : IntermediateField K L) ∧
                σF ∈ IsDiscreteValuationRing.wildInertiaGroup A K F q) ∧
        (p = 0 → θ.ker = ⊥) ∧
        (0 < p →
          ∀ (H : Type*) [Group H] [Finite H] (f : θ.ker →* H),
            IsOpen (f.ker : Set θ.ker) → Function.Surjective f → IsPGroup p H)
```

Declarations registered for the tag:

- [`Ideal.Quotient.ker_stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.ker_stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L49) (StacksFrontier): “the kernel of the decomposition-group residue action”.
- [`Ideal.Quotient.stabilizerHom_surjective_of_profinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.stabilizerHom_surjective_of_profinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L52) (StacksFrontier): “surjectivity of the decomposition-group residue action”. References: SGA 1 V (1.1), “closed points”; SGA 1 V (1.3), “special case”.

## Tag 0BUB, a lemma

[Tag 0BUB](https://stacks.math.columbia.edu/tag/0BUB) in the Stacks Project.

**`Stacks.FundamentalGroup.isAlgClosure_quotient_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean#L132). The attribute's comment: “the residue field is an algebraic closure of the residue field of `A`”.

> **Stacks 0BUB**, first assertion.  The residue field of the integral closure of a discrete
> valuation ring in a separable closure of its fraction field is an algebraic closure of the
> residue field of the discrete valuation ring.

```lean
public theorem isAlgClosure_quotient_integralClosure
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsSepClosure K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    IsAlgClosure (A ⧸ P.under A) (integralClosure A L ⧸ P)
```

**`Stacks.FundamentalGroup.exists_residueSeparableClosureHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean#L149). The attribute's comment: “the exact sequence `1 → I → D → Gal(κ^sep/κ) → 1`”.

> **Stacks 0BUB**, the first exact sequence.  Write `κ = A ⧸ (P.under A)` for the residue
> field of `A` and `κ̄` for the residue field at `P`, an algebraic closure of `κ`, and let
> `κ^sep ⊆ κ̄` be the separable closure of `κ`.  The decomposition group `D` at `P` maps to
> `Gal(κ^sep/κ)` by restricting the residue action, the inertia group `I` is contained in `D`,
> the map is surjective, and the image in `Gal(L/K)` of its kernel is exactly `I`: the sequence
> `1 → I → D → Gal(κ^sep/κ) → 1` is exact.

```lean
public theorem exists_residueSeparableClosureHom
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsSepClosure K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    letI := IsIntegralClosure.MulSemiringAction A K L (integralClosure A L)
    letI : SMulCommClass Gal(L/K) A (integralClosure A L) :=
      ⟨fun σ a b ↦ by
        simp only [Algebra.smul_def, smul_mul']
        congr 1
        exact (galRestrict A K L (integralClosure A L) σ).commutes a⟩
    let κsep := separableClosure (A ⧸ P.under A) (integralClosure A L ⧸ P)
    IsSepClosure (A ⧸ P.under A) κsep ∧
    P.inertia Gal(L/K) ≤ MulAction.stabilizer Gal(L/K) P ∧
    ∃ θ : MulAction.stabilizer Gal(L/K) P →* (κsep ≃ₐ[A ⧸ P.under A] κsep),
      (∀ (σ : MulAction.stabilizer Gal(L/K) P) (x : κsep),
        (θ σ x : integralClosure A L ⧸ P) =
          Ideal.Quotient.stabilizerHom P (P.under A) Gal(L/K) σ (x : integralClosure A L ⧸ P)) ∧
      Function.Surjective θ ∧
      θ.ker.map (MulAction.stabilizer Gal(L/K) P).subtype = P.inertia Gal(L/K)
```

**`Stacks.FundamentalGroup.isAlgClosed_quotient_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L57). The attribute's comment: “the algebraically closed residue field”.

> The residue field of the integral closure in a separable closure is
> algebraically closed.

```lean
public theorem isAlgClosed_quotient_integralClosure
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsSepClosure K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    letI : Field (integralClosure A L ⧸ P) := Ideal.Quotient.field P
    IsAlgClosed (integralClosure A L ⧸ P)
```

**`Stacks.FundamentalGroup.primeToChar_divides_tameRamificationIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L131). The attribute's comment: “cofinality of prime-to-characteristic orders”.

> Every positive order prime to the residue characteristic divides a tame
> ramification index at a finite Galois subextension.

```lean
public theorem primeToChar_divides_tameRamificationIndex
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsSepClosure K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal]
    (n : ℕ) (hn : 0 < n)
    (hcoprime : ringChar (IsLocalRing.ResidueField A) = 0 ∨
      Nat.Coprime n (ringChar (IsLocalRing.ResidueField A))) :
    ∃ (F : FiniteGaloisIntermediateField K L),
      let C := integralClosure A F
      letI : IsScalarTower A F L :=
        IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
      let f : C →ₐ[A] integralClosure A L :=
        (IsScalarTower.toAlgHom A F L).mapIntegralClosure
      let q := P.comap f.toRingHom
      ∃ hq : q.IsMaximal,
        letI : q.IsMaximal := hq
        n ∣ IsDiscreteValuationRing.tameRamificationIndex A F q
```

**`Stacks.FundamentalGroup.exists_primeToChar_tameInertiaCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L325). The attribute's comment: “the wild–tame exact sequence and canonical character”. References: SGA 1 XIII (2.0), “inertia structure”; SGA 7 I (0.3), “I/P ≅ Ẑ(1), P pro-p”; SGA 7 XV (2.2.5), “partial”.

> The canonical tame inertia character at a separable closure has wild kernel
> and reaches every compatible family of prime-to-characteristic roots of unity.
> Its finite-level formula specifies the character independently of choices.

```lean
public theorem exists_primeToChar_tameInertiaCharacter
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra K L] [IsSepClosure K L]
    [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    let I := P.inertia Gal(L/K)
    let D := MulAction.stabilizer Gal(L/K) P
    let p := ringChar (IsLocalRing.ResidueField A)
    let N := {n : ℕ // 0 < n ∧ (p = 0 ∨ Nat.Coprime n p)}
    ∃ θ : I →* (∀ _ : N, (B ⧸ P)ˣ),
      (∀ σ : I, ∀ n : N, (θ σ n) ^ n.1 = 1) ∧
      (∀ σ : I, ∀ n m : N, n.1 ∣ m.1 →
        (θ σ m) ^ (m.1 / n.1) = θ σ n) ∧
      (∀ f : ∀ _ : N, (B ⧸ P)ˣ,
        (f ∈ θ.range ↔
          ((∀ n : N, (f n) ^ n.1 = 1) ∧
           (∀ n m : N, n.1 ∣ m.1 → (f m) ^ (m.1 / n.1) = f n)))) ∧
      (∀ τ : D, ∀ σ : I,
        ∃ ρ : I,
          (ρ : Gal(L/K)) = (τ : Gal(L/K)) * (σ : Gal(L/K)) *
            (τ : Gal(L/K))⁻¹ ∧
          (∀ n : N, θ ρ n =
            (Ideal.quotientEquiv P P
              ((MulSemiringAction.toRingEquiv Gal(L/K) B) (τ : Gal(L/K)))
              τ.property.symm).toMulEquiv (θ σ n))) ∧
      (∀ τ : D, ∀ σ : I, σ ∈ θ.ker →
        ∃ ρ : I,
          (ρ : Gal(L/K)) = (τ : Gal(L/K)) * (σ : Gal(L/K)) *
            (τ : Gal(L/K))⁻¹ ∧ ρ ∈ θ.ker) ∧
      (∀ (F : FiniteGaloisIntermediateField K L),
        let C := integralClosure A F
        letI : IsScalarTower A F L :=
          IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
        letI : MulSemiringAction Gal(F/K) C :=
          IsIntegralClosure.MulSemiringAction A K F C
        let f : C →ₐ[A] B :=
          (IsScalarTower.toAlgHom A F L).mapIntegralClosure
        let q := P.comap f.toRingHom
        ∀ [q.IsMaximal], ∀ n : N,
          n.1 ∣ IsDiscreteValuationRing.tameRamificationIndex A F q →
          ∀ σ : I,
            ∃ σF : q.inertia Gal(F/K),
              (σF : Gal(F/K)) =
                AlgEquiv.restrictNormal (σ : Gal(L/K))
                  (F : IntermediateField K L) ∧
              ((θ σ n : (B ⧸ P)ˣ) : B ⧸ P) =
                (Ideal.quotientMap P f.toRingHom le_rfl)
                  (((IsDiscreteValuationRing.canonicalInertiaCharacter A K F q σF).1.1) ^
                    (IsDiscreteValuationRing.tameRamificationIndex A F q / n.1))) ∧
      (p = 0 → θ.ker = ⊥) ∧
      (0 < p →
        ∀ (H : Type*) [Group H] [Finite H] (f : θ.ker →* H),
          IsOpen (f.ker : Set θ.ker) → Function.Surjective f → IsPGroup p H)
```

Declarations registered for the tag:

- [`Ideal.Quotient.ker_stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.ker_stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L48) (StacksFrontier): “the kernel in the decomposition exact sequence”.
- [`Ideal.Quotient.stabilizerHom_surjective_of_profinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.stabilizerHom_surjective_of_profinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L51) (StacksFrontier): “surjectivity in the decomposition exact sequence”. References: SGA 1 V (1.1), “closed points”; SGA 1 V (1.3), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.13, Tag 0BSD](https://stacks.math.columbia.edu/tag/0BSD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
