---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleFundamentalGroupMap_inertiaSquare, AlgebraicGeometry.etaleFundamentalGroupMap_fractionField_strictHenselization_to_henselization, Stacks.RamificationTheory.surjective_decompositionResidueHom, Stacks.RamificationTheory.ker_decompositionResidueHom, Stacks.RamificationTheory.map_ker_decompositionResidueHom, Stacks.RamificationTheory.decompositionResidueHom_comp_inertia_subtype, Stacks.RamificationTheory.surjective_and_ker_absoluteGaloisToFundamentalGroup, Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia
statement: formalized
proof: formalized
---

# 58.13 Ramification theory

Section 58.13 of the Stacks Project, [Tag 0BSD](https://stacks.math.columbia.edu/tag/0BSD). 7 tags here are carried by 40 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BSV, an equation

[Tag 0BSV](https://stacks.math.columbia.edu/tag/0BSV) in the Stacks Project.

**`AlgebraicGeometry.etaleFundamentalGroupMap_inertiaSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean#L387). The attribute's comment: “right-hand square”.

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

**`AlgebraicGeometry.etaleFundamentalGroupMap_fractionField_strictHenselization_to_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagram.lean#L423). The attribute's comment: “trivial diagonal”.

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

**`Stacks.RamificationTheory.surjective_decompositionResidueHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L277). The attribute's comment: “surjectivity of the left vertical arrow D → Gal(κ(𝔪^sh)/κ)”.

> **Stacks Project, Tag 0BSW.** The left vertical arrow `D → Gal(κ(𝔪^sh)/κ)` of the diagram is
> surjective.
>
> The decomposition group surjects onto `Aut(κ(𝔪^sep)/κ)` by Stacks Tag 0BRK, and restriction
> `Aut(κ(𝔪^sep)/κ) → Gal(κ(𝔪^sh)/κ)` is surjective because `κ(𝔪^sep)/κ` is normal.

```lean
theorem surjective_decompositionResidueHom :
    letI := galAction A K Ksep Asep
    letI := galSMulCommClass A K Ksep Asep
    Function.Surjective (decompositionResidueHom A K Ksep Asep msep κ κmsep κmsh)
```

**`Stacks.RamificationTheory.ker_decompositionResidueHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L295). The attribute's comment: “the kernel of the left vertical arrow is the inertia group I”.

> **Stacks Project, Tag 0BSW.** The kernel of the left vertical arrow `D → Gal(κ(𝔪^sh)/κ)` is
> the inertia group `I`, viewed as a subgroup of the decomposition group `D`.
>
> The residue action of `D` has kernel `I` by Mathlib's `IsFractionRing.ker_stabilizerHom`, and
> restriction to `κ(𝔪^sh)` is injective because `κ(𝔪^sep)/κ(𝔪^sh)` is purely inseparable.

```lean
theorem ker_decompositionResidueHom :
    letI := galAction A K Ksep Asep
    letI := galSMulCommClass A K Ksep Asep
    (decompositionResidueHom A K Ksep Asep msep κ κmsep κmsh).ker =
      msep.inertia (MulAction.stabilizer Gal(Ksep/K) msep)
```

**`Stacks.RamificationTheory.map_ker_decompositionResidueHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L316). The attribute's comment: “the kernel of the left vertical arrow is the inertia group I, as a subgroup of Gal(K^sep/K)”.

> **Stacks Project, Tag 0BSW.** The kernel of the left vertical arrow, pushed forward into
> `Gal(K^sep/K)`, is the inertia group `I` as the source defines it — a subgroup of
> `Gal(K^sep/K)`.

```lean
theorem map_ker_decompositionResidueHom :
    letI := galAction A K Ksep Asep
    letI := galSMulCommClass A K Ksep Asep
    (decompositionResidueHom A K Ksep Asep msep κ κmsep κmsh).ker.map
        (MulAction.stabilizer Gal(Ksep/K) msep).subtype =
      msep.inertia Gal(Ksep/K)
```

**`Stacks.RamificationTheory.decompositionResidueHom_comp_inertia_subtype`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L331). The attribute's comment: “triviality of the diagonal arrow I → Gal(κ(𝔪^sh)/κ) labelled 1 in the diagram”.

> **Stacks Project, Tag 0BSW.** The diagonal arrow of the diagram, from the inertia group `I`
> to `Gal(κ(𝔪^sh)/κ)`, is trivial — the arrow labelled `1` in the source.

```lean
theorem decompositionResidueHom_comp_inertia_subtype :
    letI := galAction A K Ksep Asep
    letI := galSMulCommClass A K Ksep Asep
    (decompositionResidueHom A K Ksep Asep msep κ κmsep κmsh).comp
        (msep.inertia (MulAction.stabilizer Gal(Ksep/K) msep)).subtype = 1
```

**`Stacks.RamificationTheory.surjective_and_ker_absoluteGaloisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L364). The attribute's comment: “surjectivity of the right vertical arrow π₁(U) → π₁(X) and the identification of its kernel with Gal(K^sep/M), for a general integral normal X; that this kernel is the smallest closed normal subgroup of Gal(K^sep/K) containing I is Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia, for X = Spec A”.

> **Stacks Project, Tag 0BSW.** The right vertical arrow `π₁(U) → π₁(X)` of the diagram is
> surjective, and its kernel is the subgroup fixing the maximal subextension `M` unramified with
> respect to `X` — that is, `Gal(K^sep/M)`.
>
> Both come from Stacks Tag 0BQM, where the arrow is identified with restriction to `M`
> (`AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension_apply`) and `M/K` is shown to be
> Galois (`AlgebraicGeometry.normal_maximalEtaleExtension`): restriction onto a normal
> subextension is surjective with kernel its fixing subgroup.

```lean
theorem surjective_and_ker_absoluteGaloisToFundamentalGroup
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    let _ : Normal (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar) :=
      normal_maximalEtaleExtension X sbar hs hgeneric
    Function.Surjective (absoluteGaloisToFundamentalGroup X sbar) ∧
      (absoluteGaloisToFundamentalGroup X sbar).toMonoidHom.ker =
        (maximalEtaleExtension X sbar).fixingSubgroup
```

**`Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L429). The attribute's comment: “the kernel of the right vertical arrow π₁(U) → π₁(X) is the smallest closed normal subgroup of Gal(K^sep/K) containing the inertia group I, the kernel being read inside Gal(K^sep/K) through the identification of Tag 0BNE”.

> **Stacks Project, Tag 0BSW.** The kernel of the right vertical arrow `π₁(U) → π₁(X)` of the
> diagram, read inside `Gal(K^sep/K)` through the identification of Stacks Tag 0BNE, is the
> smallest closed normal subgroup containing the inertia group `I` at `𝔪^sep`.
>
> Here `A` is a normal local domain with fraction field `K`, `L = K^sep` is a separable closure of
> `K`, `q = 𝔪^sep` is a prime of the integral closure `A^sep` of `A` in `K^sep` lying over the
> maximal ideal, `U = Spec K` and `X = Spec A`. "Smallest closed normal subgroup containing `I`" is
> written, as in `Stacks.FundamentalGroup.IsExactSequence`, as the topological closure of the
> normal subgroup generated by `I`;
> `Stacks.RamificationTheory.isLeast_ker_etaleFundamentalGroupMap_inertia` records the minimality
> itself.
>
> The strict henselization `A^sh = ((A^sep)_{𝔪^sep})^I` has `(K^sep)^I` as its fraction field, so
> the local exact sequence of Stacks Tag 0BSM describes the kernel as the closed normal subgroup
> generated by the image of `π₁(Spec (K^sep)^I)`; by naturality of Stacks Tag 0BNE that image is
> the subgroup of `Gal(K^sep/K)` fixing `(K^sep)^I`, which is `I`.

```lean
theorem comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia
    (A K L Ω : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [IsLocalRing A]
    [Field K] [Field L] [Field Ω]
    [Algebra A K] [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsFractionRing A K]
    [IsSepClosure K L]
    [Algebra L Ω] [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (q : Ideal (integralClosure A L)) [q.IsPrime]
    [q.LiesOver (maximalIdeal A)] :
    letI : ConnectedSpace (Spec (.of A)) := connectedSpace_spec_of_isLocalRing A
    letI := IsIntegralClosure.galAction A K L
    Subgroup.comap (galoisEquivEtaleFundamentalGroup K L Ω).toMonoidHom
        (MonoidHom.ker (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom (algebraMap A K)))
          (algebraicClosureGeometricPoint K Ω)).toMonoidHom) =
      (Subgroup.normalClosure
        ((q.inertia Gal(L/K) : Subgroup Gal(L/K)) : Set Gal(L/K))).topologicalClosure
```

**`Stacks.RamificationTheory.isLeast_ker_etaleFundamentalGroupMap_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L474). The attribute's comment: “the minimality form of the previous statement: the kernel of the right vertical arrow is the least closed normal subgroup of Gal(K^sep/K) containing the inertia group I”.

> **Stacks Project, Tag 0BSW.** The kernel of the right vertical arrow `π₁(U) → π₁(X)`, read
> inside `Gal(K^sep/K)`, is the least closed normal subgroup containing the inertia group `I` —
> the minimality assertion of the source, read off from
> `Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia`.

```lean
theorem isLeast_ker_etaleFundamentalGroupMap_inertia
    (A K L Ω : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [IsLocalRing A]
    [Field K] [Field L] [Field Ω]
    [Algebra A K] [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsFractionRing A K]
    [IsSepClosure K L]
    [Algebra L Ω] [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (q : Ideal (integralClosure A L)) [q.IsPrime]
    [q.LiesOver (maximalIdeal A)] :
    letI : ConnectedSpace (Spec (.of A)) := connectedSpace_spec_of_isLocalRing A
    letI := IsIntegralClosure.galAction A K L
    IsLeast {N : Subgroup Gal(L/K) |
        N.Normal ∧ IsClosed (N : Set Gal(L/K)) ∧ q.inertia Gal(L/K) ≤ N}
      (Subgroup.comap (galoisEquivEtaleFundamentalGroup K L Ω).toMonoidHom
        (MonoidHom.ker (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom (algebraMap A K)))
          (algebraicClosureGeometricPoint K Ω)).toMonoidHom))
```

**`Stacks.RamificationTheory.existsUnique_bottomArrow_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L540). The attribute's comment: “commutativity of the square of the diagram: the bottom arrow Gal(κ(𝔪^sh)/κ) → π₁(X) exists and is unique, the right vertical arrow being the map induced by Spec K → Spec A read in Gal(K^sep/K) through the identification of Tag 0BNE and the lower right corner being π₁(X), which is Gal(M/K) by Tag 0BQM”.

> **Stacks Project, Tag 0BSW: the square of the diagram commutes.** With `A` a normal local
> domain with fraction field `K`, `L = K^sep` a separable closure of `K` inside an algebraically
> closed algebraic extension `Ω`, `q = 𝔪^sep` a maximal ideal of the integral closure `A^sep` of
> `A` in `K^sep` lying over `𝔪`, `U = Spec K` and `X = Spec A`, there is exactly one homomorphism
> `Gal(κ(𝔪^sh)/κ) → π₁(X)` making the square
>
> ```
> D ─────────────→ Gal(K^sep/K) = π₁(U)
> │                          │
> ↓                          ↓
> Gal(κ(𝔪^sh)/κ) ───────→ π₁(X)
> ```
>
> commute: the top arrow is the inclusion of the decomposition group, the left vertical arrow is
> `Stacks.RamificationTheory.decompositionResidueHom`, and the right vertical arrow is the map
> induced by `Spec K → Spec A` read on `Gal(K^sep/K)` through the identification of Stacks Tag
> 0BNE. By Stacks Tag 0BQM the target `π₁(X)` is `Gal(M/K)` for `M` the maximal subextension of
> `K^sep/K` unramified with respect to `A`
> (`AlgebraicGeometry.isQuotientMap_absoluteGaloisToFundamentalGroup`), which is how the source
> labels the lower right corner.
>
> Existence and uniqueness are the exactness of `1 → I → D → Gal(κ(𝔪^sh)/κ) → 1` recorded in
> `Stacks.RamificationTheory.surjective_decompositionResidueHom` and
> `Stacks.RamificationTheory.ker_decompositionResidueHom`, together with the fact that `I` dies in
> `π₁(X)`, which is
> `Stacks.RamificationTheory.comap_ker_etaleFundamentalGroupMap_eq_normalClosure_inertia`. So the
> bottom arrow of the source's diagram exists, is determined by the square, and the square is the
> one the source draws.

```lean
theorem existsUnique_bottomArrow_square
    (A K L Ω : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [IsLocalRing A]
    [Field K] [Field L] [Field Ω]
    [Algebra A K] [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsFractionRing A K]
    [IsSepClosure K L]
    [Algebra L Ω] [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (q : Ideal (integralClosure A L)) [q.IsMaximal] [q.LiesOver (maximalIdeal A)]
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
    letI := IsIntegralClosure.isFractionRing_integralClosure A K L
    letI := IsIntegralClosure.galAction A K L
    letI := IsIntegralClosure.galSMulCommClass A K L
    ∃! h : Gal(κmsh/κ) →*
        EtaleFundamentalGroup (Spec (.of A))
          ((algebraicClosureGeometricPoint K Ω).map
            (Spec.map (CommRingCat.ofHom (algebraMap A K)))),
      ∀ σ : MulAction.stabilizer Gal(L/K) q,
        h (decompositionResidueHom A K L (integralClosure A L) q κ κmsep κmsh σ) =
          etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A K)))
            (algebraicClosureGeometricPoint K Ω)
            (galoisEquivEtaleFundamentalGroup K L Ω (σ : Gal(L/K)))
```

**`Stacks.RamificationTheory.exists_continuousMulEquiv_etaleFundamentalGroup_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L634). The attribute's comment: “the identification π₁(X^h) = Gal(κ(𝔪^sh)/κ) of the lower left corner of the diagram, stated for the spectrum of an arbitrary henselian local ring and its residue field, of which X^h = Spec A^h is the case of the henselization of A”. References: SGA 3 X (4.0), “Recall 4.0, special case”.

> **Stacks Project, Tag 0BSW: `π₁(X^h) = Gal(κ(𝔪^sh)/κ)`.** For a henselian local ring `A^h`
> with residue field `κ` and a separable algebraic closure `κ(𝔪^sh)` of `κ` inside an algebraically
> closed algebraic extension `Ω`, the étale fundamental group of `X^h = Spec A^h` at the geometric
> point coming from `Ω` is `Gal(κ(𝔪^sh)/κ)`, by the canonical map induced by the closed immersion
> `Spec κ → Spec A^h`.
>
> This is the identification the source quotes from Stacks Tag 09ZS: base change along
> `Spec κ → Spec A^h` is an equivalence on finite étale schemes for the henselian pair
> `(A^h, 𝔪^h)` (`AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_henselianPair`), hence an
> isomorphism of fundamental groups by Stacks Tag 0BQA
> (`AlgebraicGeometry.fundamentalGroupContinuousMulEquivOfFiniteEtaleBaseChange`), and
> `π₁(Spec κ) = Gal(κ(𝔪^sh)/κ)` by Stacks Tag 0BNE
> (`AlgebraicGeometry.galoisEquivEtaleFundamentalGroup`).
>
> In the situation of the source `A^h` is the henselization of the normal local ring `(A, 𝔪, κ)`,
> whose residue field is `κ` itself — that is a defining condition on
> `IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) A^h` — and `κ(𝔪^sh)`, the residue
> field of a strict henselization, is a separable algebraic closure of `κ`; so this is the
> statement the source makes about the lower left corner of its diagram. The identification is
> recorded with the side condition that the underlying map is the canonical one, so that the
> statement is not merely an abstract isomorphism of two groups.

```lean
theorem exists_continuousMulEquiv_etaleFundamentalGroup_henselianLocalRing
    (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [HenselianLocalRing Ah]
    (κsh Ω : Type u) [Field κsh] [Field Ω]
    [Algebra (ResidueField Ah) κsh] [IsSepClosure (ResidueField Ah) κsh]
    [Algebra κsh Ω] [Algebra (ResidueField Ah) Ω]
    [IsScalarTower (ResidueField Ah) κsh Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic (ResidueField Ah) Ω] :
    letI : ConnectedSpace (Spec (.of Ah)) := connectedSpace_spec_of_isLocalRing Ah
    letI : ConnectedSpace (Spec (.of (ResidueField Ah))) :=
      connectedSpace_spec_of_isLocalRing (ResidueField Ah)
    ∃ e : Gal(κsh / ResidueField Ah) ≃ₜ*
        EtaleFundamentalGroup (Spec (.of Ah))
          ((algebraicClosureGeometricPoint (ResidueField Ah) Ω).map
            (Spec.map (CommRingCat.ofHom (residue Ah)))),
      ∀ σ : Gal(κsh / ResidueField Ah),
        e σ = etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (residue Ah)))
            (algebraicClosureGeometricPoint (ResidueField Ah) Ω)
            (galoisEquivEtaleFundamentalGroup (ResidueField Ah) κsh Ω σ)
```

**`Stacks.RamificationTheory.galoisEquiv_preimage_range_etaleFundamentalGroupMap_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L692). The attribute's comment: “the identification π₁(U^h) = D of the top row of the diagram: the image of π₁(Spec K^h) in π₁(Spec K) is the decomposition group D, read in Gal(K^sep/K) through the identification of Tag 0BNE, for the embedding K^h ⊆ K^sep induced by the canonical local map from the henselization to (A^sep)_{𝔪^sep}”.

> **Stacks Project, Tag 0BSW: `π₁(U^h) = D`.** In the situation of the source, with
> `U^h = Spec K^h` for `K^h` the fraction field of a henselization `A^h` of `A` and
> `K^h ⊆ K^sep` the embedding induced by the chosen local map `A^h → (A^sep)_{𝔪^sep}`, the image of
> `π₁(U^h)` in `π₁(U) = Gal(K^sep/K)` is exactly the decomposition group
> `D = {σ | σ 𝔪^sep = 𝔪^sep}`.
>
> This is the middle of the top row of the diagram of Tag 0BSV, read through the identification of
> Tag 0BNE. It combines
> `IsIntegralClosure.exists_algHom_fieldRange_eq_fixedField_stabilizer` — the source's step
> `K^h = (K^sep)^D` — with the naturality of Tag 0BNE
> (`AlgebraicGeometry.galoisEquiv_preimage_range_etaleFundamentalGroupMap`), which says that the
> image of `π₁(Spec E)` in `π₁(Spec K)` is the subgroup of `Gal(K^sep/K)` fixing `E`.
>
> The embedding `K^h → K^sep` is data, as it is in the source, where it comes from the chosen
> `κ`-embedding `κ(𝔪^sh) → κ(𝔪^sep)` and the resulting map `A^sh → (A^sep)_{𝔪^sep}`; the
> hypothesis `hcompat` says that it is the one induced by the canonical local map `A^h → B_q`, and
> `IsIntegralClosure.exists_algHom_fieldRange_eq_fixedField_stabilizer` provides such an
> embedding.

```lean
theorem galoisEquiv_preimage_range_etaleFundamentalGroupMap_decomposition
    (A K L Ω : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [IsLocalRing A]
    [Field K] [Field L] [Field Ω]
    [Algebra A K] [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsFractionRing A K]
    [IsSepClosure K L] [IsSepClosed L]
    [Algebra L Ω] [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω] [Algebra.IsAlgebraic K Ω]
    (q : Ideal (integralClosure A L)) [q.IsPrime] [q.LiesOver (maximalIdeal A)]
    (Ah Kh : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (ResidueField A) Ah]
    [Field Kh] [Algebra Ah Kh] [IsFractionRing Ah Kh]
    [Algebra A Kh] [IsScalarTower A Ah Kh] [Algebra K Kh] [IsScalarTower A K Kh]
    [Algebra Kh L] [IsScalarTower K Kh L] [Algebra Kh Ω] [IsScalarTower Kh L Ω]
    (hcompat : ∀ x : Ah, algebraMap Kh L (algebraMap Ah Kh x) =
      IsIntegralClosure.henselizationToField A K L q Ah x) :
    letI := IsIntegralClosure.galAction A K L
    ∃ hx : (algebraicClosureGeometricPoint Kh Ω).map
        (Spec.map (CommRingCat.ofHom (algebraMap K Kh))) = algebraicClosureGeometricPoint K Ω,
      (galoisEquivEtaleFundamentalGroup K L Ω) ⁻¹'
          Set.range (fun τ : EtaleFundamentalGroup (Spec (.of Kh))
              (algebraicClosureGeometricPoint Kh Ω) =>
            hx ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K Kh)))
              (algebraicClosureGeometricPoint Kh Ω) τ) =
        (MulAction.stabilizer Gal(L/K) q : Set Gal(L/K))
```

**`Stacks.RamificationTheory.galoisEquiv_preimage_range_etaleFundamentalGroupMap_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/InertiaDiagramTranslation.lean#L750). The attribute's comment: “the identification π₁(U^sh) = I of the top row of the diagram: the image of π₁(Spec K^sh) in π₁(Spec K) is the inertia group I, read in Gal(K^sep/K) through the identification of Tag 0BNE, with K^sh presented as the fixed field (K^sep)^I”.

> **Stacks Project, Tag 0BSW: `π₁(U^sh) = I`.** With `U^sh = Spec K^sh` for
> `K^sh = (K^sep)^I` the fraction field of the strict henselization
> `A^sh = ((A^sep)_{𝔪^sep})^I`, the image of `π₁(U^sh)` in `π₁(U) = Gal(K^sep/K)` is exactly the
> inertia group `I` at `𝔪^sep`.
>
> This is the left end of the top row of the diagram of Tag 0BSV, read through the identification
> of Tag 0BNE. The strictly henselized fraction field is presented as the fixed field
> `IsIntegralClosure.inertiaFixedField`, which is a fraction field of
> `((A^sep)_{𝔪^sep})^I` by `IsIntegralClosure.isFractionRing_inertiaFixedField`, that ring being a
> strict henselization of `A` by `IsIntegralClosure.isHenselization_inertiaInvariants`; its fixing
> subgroup is `I` by `IsIntegralClosure.fixingSubgroup_inertiaFixedField`, and the naturality of
> Tag 0BNE (`AlgebraicGeometry.galoisEquiv_preimage_range_etaleFundamentalGroupMap`) turns that
> into the assertion about fundamental groups.

```lean
theorem galoisEquiv_preimage_range_etaleFundamentalGroupMap_inertia
    (A K L Ω : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [IsLocalRing A]
    [Field K] [Field L] [Field Ω]
    [Algebra A K] [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsFractionRing A K]
    [IsSepClosure K L]
    [Algebra L Ω] [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω] [Algebra.IsAlgebraic K Ω]
    (q : Ideal (integralClosure A L)) [q.IsPrime] :
    letI := IsIntegralClosure.galAction A K L
    ∃ hx : (algebraicClosureGeometricPoint
          (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω).map
          (Spec.map (CommRingCat.ofHom (algebraMap K
            (IsIntegralClosure.inertiaFixedField A K L q : Type u)))) =
        algebraicClosureGeometricPoint K Ω,
      (galoisEquivEtaleFundamentalGroup K L Ω) ⁻¹'
          Set.range (fun τ : EtaleFundamentalGroup
              (Spec (.of (IsIntegralClosure.inertiaFixedField A K L q : Type u)))
              (algebraicClosureGeometricPoint
                (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω) =>
            hx ▸ etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K
                (IsIntegralClosure.inertiaFixedField A K L q : Type u))))
              (algebraicClosureGeometricPoint
                (IsIntegralClosure.inertiaFixedField A K L q : Type u) Ω) τ) =
        (q.inertia Gal(L/K) : Set Gal(L/K))
```

**`IsIntegralClosure.exists_algHom_fieldRange_eq_fixedField_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/DecompositionFixedField.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/DecompositionFixedField.lean#L440). The attribute's comment: “the identification K^h = (K^sep)^D of the middle of the top row of the diagram: the fixed field of the decomposition group D is the fraction field of a henselization of A, embedded in K^sep compatibly with the canonical local map to (A^sep)_{𝔪^sep}”.

> **Stacks Project, Tag 0BSW: `K^h = (K^sep)^D`.** Let `(A, 𝔪, κ)` be a normal local domain
> with fraction field `K`, let `K^sep` be a separable closure of `K`, let `𝔪^sep = q` be a prime of
> the integral closure `A^sep` of `A` in `K^sep` lying over `𝔪`, let `A^h` be a henselization of
> `A` and let `K^h` be its fraction field. Then `K^h` embeds in `K^sep` over `K`, compatibly with
> the canonical local map `A^h → (A^sep)_{𝔪^sep}`, in such a way that the subgroup of
> `Gal(K^sep/K)` fixing its image is exactly the decomposition group
> `D = {σ | σ 𝔪^sep = 𝔪^sep}`; equivalently the image of `K^h` is the fixed field `(K^sep)^D`.
>
> Together with Stacks Tag 0BNE — under which the image of `π₁(Spec K^h)` in `π₁(Spec K)` is the
> subgroup of `Gal(K^sep/K)` fixing `K^h` — this is the identification `π₁(U^h) = D` of the top
> row of the diagram of Tag 0BSV.

```lean
theorem exists_algHom_fieldRange_eq_fixedField_stabilizer
    (Kh : Type u) [Field Kh] [Algebra Ah Kh] [IsFractionRing Ah Kh]
    [Algebra A Kh] [IsScalarTower A Ah Kh] [Algebra K Kh] [IsScalarTower A K Kh] :
    ∃ j : Kh →ₐ[K] L,
      (∀ x : Ah, j (algebraMap Ah Kh x) = henselizationToField A K L q Ah x) ∧
      j.fieldRange.fixingSubgroup = MulAction.stabilizer Gal(L/K) q ∧
      j.fieldRange = IntermediateField.fixedField (MulAction.stabilizer Gal(L/K) q)
```

## Tag 0BTD, a lemma

[Tag 0BTD](https://stacks.math.columbia.edu/tag/0BTD) in the Stacks Project.

**`AlgebraicGeometry.normalClosure_iUnion_ker_topologicalClosure_le_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L335). The attribute's comment: “the inclusion of subgroup (3) in subgroup (1), and only that inclusion: subgroup (1) is the kernel of π₁(Spec K) → π₁(X) rather than the subgroup fixing the maximal unramified subextension, so no Noetherian hypothesis is needed, and subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪_{X,x}) as generators; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

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

**`AlgebraicGeometry.ker_etaleFundamentalGroupMap_stalk_eq_normalClosure_topologicalClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L362). The attribute's comment: “that each generator of subgroup (3) used here — the kernel of π₁(Spec K) → π₁(Spec 𝒪_{X,x}) — is the smallest closed normal subgroup containing the image of π₁(Spec K_x^sh) = Gal(K^sep/K_x^sh), which is how the source presents subgroup (3); this is Tag 0BSM applied to the local rings of X”.

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

**`AlgebraicGeometry.normalClosure_range_topologicalClosure_le_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L397). The attribute's comment: “that each generator Gal(K^sep/K_x^sh) of subgroup (3) generates a closed normal subgroup contained in subgroup (1), one point x of X at a time; subgroup (1) is the kernel of π₁(Spec K) → π₁(X), so no Noetherian hypothesis is needed; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

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

**`AlgebraicGeometry.comap_normalClosure_iUnion_ker_le_ker_galoisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L449). The attribute's comment: “the inclusion of subgroup (3) in subgroup (1) read inside Gal(K^sep/K) through the identification of Tag 0BNE; subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪_{X,x}) as generators; subgroup (2) is AlgebraicGeometry.inertiaClosedNormalSubgroup below”.

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

**`AlgebraicGeometry.inertiaClosedNormalSubgroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L586). The attribute's comment: “subgroup (2): the smallest closed normal subgroup of Gal(K^sep/K) containing the inertia group I_y for every point y of the normalization X^sep of X in K^sep, with the points of X^sep over a nonempty affine open U of X presented as the primes of the integral closure of Γ(X, U) in K^sep”.

> **Subgroup (2) of Stacks Tag 0BTD.** The smallest closed normal subgroup of
> `Gal(K^sep/K) = π₁(Spec K)` containing the inertia group `I_y` for every point `y` of the
> normalization `X^sep` of `X` in `K^sep`.

```lean
def inertiaClosedNormalSubgroup : Subgroup Gal(L / X.residueField (genericPoint X))
```

**`AlgebraicGeometry.isFinite_etale_fromNormalization_of_inertiaGenerators_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L713). The attribute's comment: “the second paragraph of the proof: triviality of the inertia groups I_y on a finite Galois subextension F of K^sep/K makes X unramified in F”. References: SGA 1 V (2.2), “(ii)”; SGA 1 V (2.3), “special case”.

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
      (F.fixingSubgroup : Set Gal(L / X.residueField (genericPoint X)))) :
    let f : Spec (.of (F : Type u)) ⟶ X :=
      Spec.map (CommRingCat.ofHom
        (algebraMap (X.residueField (genericPoint X)) (F : Type u))) ≫
        X.fromSpecResidueField (genericPoint X)
    IsFinite f.fromNormalization ∧ Etale f.fromNormalization
```

**`AlgebraicGeometry.ker_galoisToFundamentalGroup_le_inertiaClosedNormalSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 841](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L841). The attribute's comment: “the inclusion of subgroup (1) in subgroup (2), and only that inclusion: subgroup (1) is the kernel of Gal(K^sep/K) → π₁(X) and subgroup (2) is the closed normal subgroup generated by the inertia groups I_y; the reverse inclusion (2) ⊆ (3) needs the conjugacy of I_y with Gal(K^sep/K_x^sh) from Tag 0BSW, is AlgebraicGeometry.inertiaClosedNormalSubgroup_le_stalkKerClosedNormalSubgroup below”.

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

**`AlgebraicGeometry.inertiaClosedNormalSubgroup_le_stalkKerClosedNormalSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L959). The attribute's comment: “the inclusion of subgroup (2) in subgroup (3), which together with the inclusions (3) ⊆ (1) and (1) ⊆ (2) above gives the equality of the three subgroups; subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪_{X,x}) as generators and is read inside Gal(K^sep/K) through the identification of Tag 0BNE”.

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

**`AlgebraicGeometry.ker_galoisToFundamentalGroup_eq_inertiaClosedNormalSubgroup_and_stalkKer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean, line 1058](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalKernelLocalRings.lean#L1058). The attribute's comment: “the equality of the three subgroups, assembled from the cycle (3) ⊆ (1) ⊆ (2) ⊆ (3); subgroup (1) is the kernel of Gal(K^sep/K) → π₁(X) rather than the subgroup fixing the maximal unramified subextension, so no Noetherian hypothesis is needed, and subgroup (3) is written with the kernels of π₁(Spec K) → π₁(Spec 𝒪_{X,x}) as generators”.

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

**`MvPolynomial.mem_evenSubalgebra_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L190). The attribute's comment: “the invariant subring k[tᵢtⱼ]”.

> The subring `k[tᵢtⱼ]` consists of the polynomials all of whose monomials have even degree.

```lean
theorem mem_evenSubalgebra_iff {f : MvPolynomial σ k} :
    f ∈ evenSubalgebra k σ ↔ ∀ m ∈ f.support, Even (Finsupp.degree m)
```

**`MvPolynomial.mem_evenSubalgebra_iff_negVars_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L206). The attribute's comment: “the invariant subring k[tᵢtⱼ]”.

> The subring `k[tᵢtⱼ]` is the ring of invariants of the `±1`-action, provided `2 ≠ 0`.

```lean
theorem mem_evenSubalgebra_iff_negVars_eq (h2 : (2 : k) ≠ 0) {f : MvPolynomial σ k} :
    f ∈ evenSubalgebra k σ ↔ negVars k σ f = f
```

**`MvPolynomial.finite_evenSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L297). The attribute's comment: “the degree two morphism”.

> The polynomial ring in finitely many variables is a finite module over `k[tᵢtⱼ]`: the morphism
> `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is finite.

```lean
theorem finite_evenSubalgebra [Finite σ] :
    Module.Finite (evenSubalgebra k σ) (MvPolynomial σ k)
```

**`MvPolynomial.rank_evenSubalgebra_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L337). The attribute's comment: “the degree two morphism”.

> The polynomial ring has rank two as a module over `k[tᵢtⱼ]`: the morphism
> `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` has degree two.

```lean
theorem rank_evenSubalgebra_eq_two (h2 : (2 : k) ≠ 0) [Nonempty σ] :
    Module.rank (evenSubalgebra k σ) (MvPolynomial σ k) = 2
```

**`MvPolynomial.finrank_evenSubalgebra_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L372). The attribute's comment: “the degree two morphism”.

> The polynomial ring in finitely many variables has rank two as a module over `k[tᵢtⱼ]`.

```lean
theorem finrank_evenSubalgebra_eq_two (h2 : (2 : k) ≠ 0) [Nonempty σ] :
    Module.finrank (evenSubalgebra k σ) (MvPolynomial σ k) = 2
```

**`MvPolynomial.isUnramifiedAt_of_under_ne_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L580). The attribute's comment: “unramified away from the vertex”.

> The morphism `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is unramified at every point of `𝐀ⁿ_k` which does not
> lie over the vertex `𝔪 = (tᵢtⱼ)`.

```lean
theorem isUnramifiedAt_of_under_ne_vertexIdeal (h2 : (2 : k) ≠ 0) (q : Ideal (MvPolynomial σ k))
    [q.IsPrime] (hq : q.under (evenSubalgebra k σ) ≠ vertexIdeal k σ) :
    Algebra.IsUnramifiedAt (evenSubalgebra k σ) q
```

**`MvPolynomial.not_isUnramifiedAt_idealOfVars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L639). The attribute's comment: “ramified at the vertex”.

> The morphism `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is ramified at the vertex `(t₁, …, tₙ)` of `𝐀ⁿ_k`, which
> lies over the vertex `𝔪 = (tᵢtⱼ)`.

```lean
theorem not_isUnramifiedAt_idealOfVars [Nonempty σ] :
    ¬ Algebra.IsUnramifiedAt (evenSubalgebra k σ) (idealOfVars σ k)
```

**`MvPolynomial.height_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L744). The attribute's comment: “the vertex has codimension n”.

> The vertex `𝔪 = (tᵢtⱼ)` has height `n` in `k[tᵢtⱼ]` for `n` variables: it is a point of
> codimension `n` of the quotient.

```lean
theorem height_vertexIdeal (n : ℕ) : (vertexIdeal k (Fin n)).height = n
```

**`MvPolynomial.one_lt_height_vertexIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/QuadraticConeRamification.lean#L759). The attribute's comment: “ramification in codimension greater than one”.

> For at least two variables the vertex `𝔪 = (tᵢtⱼ)` has codimension greater than one, so the
> ramification of `𝐀ⁿ_k → Spec(k[tᵢtⱼ])` is not visible in codimension one.

```lean
theorem one_lt_height_vertexIdeal {n : ℕ} (hn : 2 ≤ n) : 1 < (vertexIdeal k (Fin n)).height
```

## Tag 0BTF, a lemma

[Tag 0BTF](https://stacks.math.columbia.edu/tag/0BTF) in the Stacks Project.

**`AlgebraicGeometry.normalization_unramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean, line 2218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean#L2218). The attribute's comment: “conditions (1)–(8)”.

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

**`AlgebraicGeometry.normalization_unramified_iff_trivialInertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean, line 2415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalUnramifiedTFAE.lean#L2415). The attribute's comment: “condition (9)”.

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

**`Stacks.FundamentalGroup.exists_tameInertiaCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 1208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L1208). The attribute's comment: “the wild–tame exact sequence and canonical character”. References: SGA 1 XIII (2.0), “inertia structure”; SGA 7 I (0.3), “I/P ≅ Ẑ(1), P pro-p”.

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

- [`Ideal.Quotient.ker_stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.ker_stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L49) (StacksFrontier): “the kernel of the decomposition-group residue action”.
- [`Ideal.Quotient.stabilizerHom_surjective_of_profinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.stabilizerHom_surjective_of_profinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/InfiniteInertia.lean#L52) (StacksFrontier): “surjectivity of the decomposition-group residue action”. References: SGA 1 V (1.1), “closed points”; SGA 1 V (1.3), “special case”.

## Tag 0BUB, a lemma

[Tag 0BUB](https://stacks.math.columbia.edu/tag/0BUB) in the Stacks Project.

**`Stacks.FundamentalGroup.isAlgClosure_quotient_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean#L132). The attribute's comment: “the residue field is an algebraic closure of the residue field of `A`”.

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

**`Stacks.FundamentalGroup.exists_residueSeparableClosureHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureDecomposition.lean#L149). The attribute's comment: “the exact sequence `1 → I → D → Gal(κ^sep/κ) → 1`”.

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

**`Stacks.FundamentalGroup.isAlgClosed_quotient_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L57). The attribute's comment: “the algebraically closed residue field”.

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

**`Stacks.FundamentalGroup.primeToChar_divides_tameRamificationIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L131). The attribute's comment: “cofinality of prime-to-characteristic orders”.

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

**`Stacks.FundamentalGroup.exists_primeToChar_tameInertiaCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L325). The attribute's comment: “the wild–tame exact sequence and canonical character”. References: SGA 1 XIII (2.0), “inertia structure”; SGA 7 I (0.3), “I/P ≅ Ẑ(1), P pro-p”; SGA 7 XV (2.2.5), “partial”.

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

- [`Ideal.Quotient.ker_stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.ker_stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L48) (StacksFrontier): “the kernel in the decomposition exact sequence”.
- [`Ideal.Quotient.stabilizerHom_surjective_of_profinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.stabilizerHom_surjective_of_profinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/SeparableClosureInertia.lean#L51) (StacksFrontier): “surjectivity in the decomposition exact sequence”. References: SGA 1 V (1.1), “closed points”; SGA 1 V (1.3), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.13, Tag 0BSD](https://stacks.math.columbia.edu/tag/0BSD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
