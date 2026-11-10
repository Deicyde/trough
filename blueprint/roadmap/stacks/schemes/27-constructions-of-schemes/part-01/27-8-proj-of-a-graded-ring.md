---
declaration: section
origin: cited
lean: Stacks.ProjStandardOpenStatement.tag01M4, ProjectiveSpectrum.IsStandardOpenCover, AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv_restrict, AlgebraicGeometry.ProjectiveSpectrum.Proj.coe_associatedModuleSheafStandardOpenEquiv_smul, AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheaf, AlgebraicGeometry.ProjectiveSpectrum.Proj.degreeZeroToSection_injective, AlgebraicGeometry.ProjectiveSpectrum.Proj.degreeZeroToSection_surjective, AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv
statement: formalized
proof: formalized
---

# 27.8 Proj of a graded ring

Section 27.8 of the Stacks Project, [Tag 01M3](https://stacks.math.columbia.edu/tag/01M3). 13 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01M4, a lemma

[Tag 01M4](https://stacks.math.columbia.edu/tag/01M4) in the Stacks Project.

**`Stacks.ProjStandardOpenStatement.tag01M4`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenStatement.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenStatement.lean#L89). The attribute's comment: “the ten assertions of the tag in one statement: part (1)(a)-(h) for a standard open D+(g) contained in D+(f), part (2) the finite refinement of an open covering of D+(f) by standard opens, part (3) the unit-ideal criterion”.

> **[Stacks, Tag 01M4].** For a graded ring `A` and `f ∈ 𝒜 d` homogeneous of positive degree:
>
> * part (1), for homogeneous `g` of positive degree with `D₊(g) ⊆ D₊(f)`, the eight assertions
>   (a)–(h) of the source, the module assertions (g) and (h) quantified over the graded module
>   inside their own conjuncts;
> * part (2), the finite refinement of an open covering of `D₊(f)` by standard opens;
> * part (3), the unit-ideal criterion for `D₊(f) ⊆ ⋃ D₊(gᵢ)`.

```lean
theorem tag01M4 (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] {f : A} {d : ℕ}
    (hfd : f ∈ 𝒜 d) (hd : 0 < d) :
    -- part (1)
    (∀ (g : A) (e : ℕ) (hge : g ∈ 𝒜 e) (he : 0 < e)
        (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f),
        -- (a) `f` is invertible in `A[1/g]`, and `f ^ deg g / g ^ deg f` is invertible in `A₍g₎`
        (IsUnit (algebraMap A (Localization.Away g) f) ∧
          IsUnit (Away.isLocalizationElem hge hfd)) ∧
        -- (b) a positive power of `g` is a homogeneous multiple of `f`
        (∃ k : ℕ, 1 ≤ k ∧ ∃ a : A, SetLike.IsHomogeneousElem 𝒜 a ∧ g ^ k = a * f) ∧
        -- (c) the canonical, and only, `A`-algebra map `A[1/f] → A[1/g]`
        ((∀ x : A,
            ProjectiveSpectrum.localizedRingMap 𝒜 f g ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg
                (algebraMap A (Localization.Away f) x) = algebraMap A (Localization.Away g) x) ∧
          Subsingleton (Localization.Away f →ₐ[A] Localization.Away g)) ∧
        -- (d) the canonical `𝒜 0`-algebra map `A₍f₎ → A₍g₎`, compatible with the map of (c),
        -- and the only `𝒜 0`-algebra map compatible with it
        ((∀ x : Away 𝒜 f,
            (ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg x).val =
              ProjectiveSpectrum.localizedRingMap 𝒜 f g ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg x.val) ∧
          ∀ ψ : Away 𝒜 f →ₐ[𝒜 0] Away 𝒜 g,
            (∀ x : Away 𝒜 f, (ψ x).val =
              ProjectiveSpectrum.localizedRingMap 𝒜 f g ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg x.val) →
            ψ = ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg) ∧
        -- (e) that map exhibits `A₍g₎` as `A₍f₎` localized at `g ^ deg f / f ^ deg g`
        (letI : Algebra (Away 𝒜 f) (Away 𝒜 g) :=
          (ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g
            ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).toRingHom.toAlgebra
         IsLocalization.Away
           (Away.mk 𝒜 hfd e (g ^ d) (by simpa [mul_comm] using SetLike.pow_mem_graded d hge))
           (Away 𝒜 g)) ∧
        -- (f) the commutative diagram of topological spaces, with horizontal arrows
        -- homeomorphisms and vertical arrows open immersions
        (letI := gradedRingTwistAway 𝒜 hfd
         letI := gradedRingTwistAway 𝒜 hge
         IsHomeomorph (gradedPrimeToBasicOpen 𝒜 hge he) ∧
           IsHomeomorph (gradedPrimesAwayToSpec 𝒜 hge) ∧
           IsHomeomorph (gradedPrimeToBasicOpen 𝒜 hfd hd) ∧
           IsHomeomorph (gradedPrimesAwayToSpec 𝒜 hfd) ∧
           Topology.IsOpenEmbedding (basicOpenInclusion 𝒜 hfg) ∧
           Topology.IsOpenEmbedding
             (gradedPrimesVertical 𝒜 hfd hge ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg) ∧
           Topology.IsOpenEmbedding (specDegreeZeroVertical 𝒜 f g d e hd he hfd hge hfg) ∧
           (∀ q : gradedPrimes (twistAway 𝒜 g e),
             basicOpenInclusion 𝒜 hfg (gradedPrimeToBasicOpen 𝒜 hge he q) =
               gradedPrimeToBasicOpen 𝒜 hfd hd
                 (gradedPrimesVertical 𝒜 hfd hge ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg q)) ∧
           (∀ q : gradedPrimes (twistAway 𝒜 g e),
             specDegreeZeroVertical 𝒜 f g d e hd he hfd hge hfg
                 (gradedPrimesAwayToSpec 𝒜 hge q) =
               gradedPrimesAwayToSpec 𝒜 hfd
                 (gradedPrimesVertical 𝒜 hfd hge ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg q))) ∧
        -- (g) and (h), for an arbitrary graded `A`-module `M`
        (∀ {M : Type w} {τ : Type t} [AddCommGroup M] [Module A M] [SetLike τ M]
            [AddSubgroupClass τ M] (𝒨 : ℤ → τ) [DirectSum.Decomposition 𝒨]
            [SetLike.GradedSMul 𝒜 𝒨],
          -- (g) compatible maps `M_f → M_g` and `M₍f₎ → M₍g₎`, induced by the identity of `M`,
          -- each the only such map
          ((∀ m : M,
              (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                    ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).localizedMap
                  (LocalizedModule.mkLinearMap (Submonoid.powers f) M m) =
                LocalizedModule.mkLinearMap (Submonoid.powers g) M m) ∧
            (∀ x : GradedModuleDegreeZeroLocalization 𝒜 𝒨 f,
              (((ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                      ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).degreeZeroMap x :
                    GradedModuleDegreeZeroLocalization 𝒜 𝒨 g) :
                  LocalizedModule.Away (R := A) g M) =
                (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                  ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).localizedMap x) ∧
            (∀ L :
                letI := Module.compHom (R := Localization.Away g) (S := Localization.Away f)
                  (LocalizedModule.Away (R := A) g M)
                  (ProjectiveSpectrum.localizedRingMap 𝒜 f g
                    ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).toRingHom
                LocalizedModule.Away (R := A) f M →ₗ[Localization.Away f]
                  LocalizedModule.Away (R := A) g M,
              (∀ m : M, L (LocalizedModule.mkLinearMap (Submonoid.powers f) M m) =
                LocalizedModule.mkLinearMap (Submonoid.powers g) M m) →
              L = (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).localizedMap) ∧
            (∀ N :
                letI := Module.compHom (R := Localization.Away f)
                  (LocalizedModule.Away (R := A) f M)
                  (algebraMap (Away 𝒜 f) (Localization.Away f))
                letI := Module.compHom (R := Localization.Away g)
                  (LocalizedModule.Away (R := A) g M)
                  (algebraMap (Away 𝒜 g) (Localization.Away g))
                letI := Module.compHom (R := Away 𝒜 g)
                  (GradedModuleDegreeZeroLocalization 𝒜 𝒨 g)
                  (ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g
                    ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).toRingHom
                GradedModuleDegreeZeroLocalization 𝒜 𝒨 f →ₗ[Away 𝒜 f]
                  GradedModuleDegreeZeroLocalization 𝒜 𝒨 g,
              (∀ x : GradedModuleDegreeZeroLocalization 𝒜 𝒨 f,
                (N x : LocalizedModule.Away (R := A) g M) =
                  (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                    ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).localizedMap x) →
              N = (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
                ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).degreeZeroMap)) ∧
          -- (h) `M₍g₎` is `M₍f₎` localized at `g ^ deg f / f ^ deg g`
          (letI : Algebra (Away 𝒜 f) (Away 𝒜 g) :=
             (ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g
               ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).toRingHom.toAlgebra
           letI := Module.compHom (R := Away 𝒜 g)
             (GradedModuleDegreeZeroLocalization 𝒜 𝒨 g)
             (ProjectiveSpectrum.degreeZeroRingMap 𝒜 f g
               ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).toRingHom
           IsLocalizedModule
             (Submonoid.powers
               (Away.mk 𝒜 hfd e (g ^ d) (by simpa [mul_comm] using SetLike.pow_mem_graded d hge)))
             (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
               ⟨d, hd, hfd⟩ ⟨e, he, hge⟩ hfg).degreeZeroMap))) ∧
    -- part (2)
    (∀ {ι : Type s} (U : ι → TopologicalSpace.Opens (ProjectiveSpectrum 𝒜)),
        ProjectiveSpectrum.basicOpen 𝒜 f ≤ ⨆ i, U i →
        ∃ (n : ℕ) (g : Fin n → A) (e : Fin n → ℕ),
          (∀ i, 0 < e i ∧ g i ∈ 𝒜 (e i)) ∧
          ProjectiveSpectrum.basicOpen 𝒜 f = ⨆ i, ProjectiveSpectrum.basicOpen 𝒜 (g i) ∧
          ∀ i, ∃ j, ProjectiveSpectrum.basicOpen 𝒜 (g i) ≤ U j) ∧
    -- part (3)
    (∀ {ι : Type s'} (g : ι → A) (e : ι → ℕ) (hg : ∀ i, g i ∈ 𝒜 (e i)) (_he : ∀ i, 0 < e i),
        AlgebraicGeometry.Proj.basicOpen 𝒜 f ≤ ⨆ i, AlgebraicGeometry.Proj.basicOpen 𝒜 (g i) ↔
          Ideal.span (Set.range fun i => Away.isLocalizationElem hfd (hg i)) = ⊤)
```

## Tag 01M5, a definition

[Tag 01M5](https://stacks.math.columbia.edu/tag/01M5) in the Stacks Project.

**`ProjectiveSpectrum.IsStandardOpenCover`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenCover.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenCover.lean#L61).

> A finite family of positive-degree homogeneous elements `gᵢ` gives a standard open
> covering of the projective standard open `D₊(f)` when their standard opens have union
> exactly `D₊(f)`.

```lean
public abbrev IsStandardOpenCover {A : Type u} {σ : Type v}
    [CommRing A] [SetLike σ A] [AddSubmonoidClass σ A] (𝒜 : ℕ → σ) [GradedRing 𝒜]
    (f : A) {n : ℕ} (g : Fin n → A) : Prop
```

## Tag 01M6, a definition

[Tag 01M6](https://stacks.math.columbia.edu/tag/01M6) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalRestriction.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalRestriction.lean#L67). The attribute's comment: “part (3), the standard-open identification intertwines the restriction map of the associated sheaf with the degree-zero restriction map of Tag 01M4”.

> The standard-open identification `Γ(D₊(f), M̃) = M₍f₎` intertwines the restriction map of
> `M̃` with the canonical degree-zero restriction map `M₍f₎ → M₍g₎`, for any two positive-degree
> homogeneous elements with `D₊(g) ⊆ D₊(f)`.

```lean
theorem associatedModuleSheafStandardOpenEquiv_restrict (f g : S) {d e : ℕ}
    (hf : f ∈ 𝒜 d) (hd : 0 < d) (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (associatedModuleSheaf 𝒜 𝒨).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    associatedModuleSheafStandardOpenEquiv 𝒜 𝒨 hg he
        ((associatedModuleSheaf 𝒜 𝒨).val.map (homOfLE hfg).op s) =
      (ProjectiveSpectrum.moduleRestrictionMaps 𝒜 𝒨 f g
          ⟨d, hd, hf⟩ ⟨e, he, hg⟩ hfg).degreeZeroMap
        (associatedModuleSheafStandardOpenEquiv 𝒜 𝒨 hf hd s)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.coe_associatedModuleSheafStandardOpenEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenScalars.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenScalars.lean#L82). The attribute's comment: “part (3), the scalar action in the standard-open identification, written out on the underlying elements of the localization”.

> The standard-open identification `Γ(D₊(f), M̃) = M₍f₎` is linear for the action of
> `Γ(P, D₊(f))` read through `AlgebraicGeometry.Proj.awayToSection`, the action on the target being
> multiplication by the fraction inside `M_f`.

```lean
theorem coe_associatedModuleSheafStandardOpenEquiv_smul {f : S} {d : ℕ} (hf : f ∈ 𝒜 d)
    (hd : 0 < d) (r : HomogeneousLocalization.Away 𝒜 f)
    (s : (associatedModuleSheaf 𝒜 𝒨).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((associatedModuleSheafStandardOpenEquiv 𝒜 𝒨 hf hd
          ((ProjectiveSpectrum.Proj.awayToSection 𝒜 f).hom r • s) :
        LocalizedModule.Away f M)) =
      HomogeneousLocalization.val r •
        ((associatedModuleSheafStandardOpenEquiv 𝒜 𝒨 hf hd s : LocalizedModule.Away f M))
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L221). The attribute's comment: “part (3), the sheaf associated to a graded module”. References: SGA 6 VI (2.3.2), “affine base”.

> The actual sheaf associated to a graded module. Its sections are locally homogeneous
> fractions of degree zero, and its restrictions are restrictions of dependent functions.

```lean
public noncomputable def associatedModuleSheaf :
    SheafOfModules.{max u v}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒜))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒜))
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.degreeZeroToSection_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L710). The attribute's comment: “part (3), injectivity of the standard-open comparison”.

> Distinct degree-zero fractions give distinct sections on a positive-degree standard open.

```lean
public theorem degreeZeroToSection_injective {f : S} {d : ℕ}
    (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    Function.Injective (degreeZeroToSection 𝒜 𝒨 f)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.degreeZeroToSection_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L729). The attribute's comment: “part (3), surjectivity of the standard-open comparison”.

> Every section on a positive-degree standard open comes from a degree-zero fraction.

```lean
public theorem degreeZeroToSection_surjective {f : S} {d : ℕ}
    (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    Function.Surjective (degreeZeroToSection 𝒜 𝒨 f)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 937](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L937). The attribute's comment: “part (3), canonical linear identification on standard opens”.

> The canonical linear identification of sections on `D₊(f)` with `M_(f)`.
> Its inverse is evaluation of a degree-zero fraction in every homogeneous-prime fiber.

```lean
public noncomputable def associatedModuleSheafStandardOpenEquiv {f : S} {d : ℕ}
    (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (associatedModuleSheaf 𝒜 𝒨).val.obj (.op (ProjectiveSpectrum.basicOpen 𝒜 f))
      ≃ₗ[HomogeneousLocalization.Away 𝒜 f]
        GradedModuleDegreeZeroLocalization 𝒜 𝒨 f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ProjectiveSpectrum.Proj.structureSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.ProjectiveSpectrum.Proj.structureSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L84) (StacksFrontier): “part (1), the structure sheaf”.
- [`AlgebraicGeometry.Proj.toLocallyRingedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Proj.toLocallyRingedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjStructureSheaf.lean#L87) (StacksFrontier): “part (2), the homogeneous spectrum as a locally ringed space”.

## Tag 01M7, a lemma

[Tag 01M7](https://stacks.math.columbia.edu/tag/01M7) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjSheafFunctoriality.shortExact_map_associatedModuleSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Exact.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Exact.lean#L167). The attribute's comment: “the functor M ↦ M~ is exact, in its categorical form: a short exact sequence of graded S-modules goes to a short exact sequence of sheaves of modules on Proj S”.

> **Stacks 01M7: the functor `M ↦ M̃` is exact**, in the form that it carries a short exact
> sequence of graded `S`-modules to a short exact sequence of sheaves of `𝒪_{Proj 𝒮}`-modules.
>
> Short exactness of sheaves of modules is short exactness on every stalk, the stalk of `M̃` at a
> homogeneous prime `𝔭` is the degree-zero part of the localization of `M` at `𝔭`, and that
> operation is exact.

```lean
public theorem shortExact_map_associatedModuleSheafFunctor
    (T : ShortComplex (GradedModuleCat.{u, u, w} 𝒮)) (hT : T.ShortExact) :
    (T.map (associatedModuleSheafFunctor 𝒮)).ShortExact
```

**`Stacks.AlgebraicGeometry.ProjSheafFunctoriality.sections_restriction_stalks_functorial_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Statement.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Statement.lean#L115). The attribute's comment: “the tag's assertions in one statement: the sections of the structure sheaf and of the associated sheaf over a positive-degree standard open are the degree-zero localizations `S₍f₎` and `M₍f₎`, the restriction maps between two standard opens are the canonical maps `S₍f₎ → S₍g₎` and `M₍f₎ → M₍g₎` of degree-zero localizations, the stalks at a homogeneous prime are `S₍𝔭₎` and `M₍𝔭₎`, there are canonical maps `S₀ → Γ(Proj S, 𝒪)` and `M₀ → Γ(Proj S, M̃)` fitting both descriptions, every one of these identifications is natural in the graded module, and `M ↦ M̃` is an exact functor”. References: EGA II (2.5.5), “special case”.

> **[Stacks, Tag 01M7].** Let `S` be a graded ring, let `M` be a graded `S`-module and let `M̃`
> be the sheaf of `𝒪_{Proj(S)}`-modules associated to `M`. Then all of the following hold.
>
> The conjuncts are, in order:
>
> 1. For `f` homogeneous of positive degree, `Γ(D₊(f), 𝒪_{Proj(S)})` is `S₍f₎`.
> 2. For `f` homogeneous of positive degree, `Γ(D₊(f), M̃)` is `M₍f₎` as an `S₍f₎`-module.
> 3. For `D₊(g) ⊆ D₊(f)` with `f`, `g` homogeneous of positive degree, the restriction map of
>   `𝒪_{Proj(S)}` is the map `S₍f₎ → S₍g₎` of Tag 01M4, and the restriction map of `M̃` is the
>   map `M₍f₎ → M₍g₎` of Tag 01M4.
> 4. At a point `x` of `Proj(S)`, with homogeneous prime `𝔭`, the stalk `𝒪_{Proj(S), x}` is `S₍𝔭₎`.
> 5. At the same point, the stalk `(M̃)_x` is `M₍𝔭₎` as an `S₍𝔭₎`-module.
> 6. There is a canonical ring map `S₀ → Γ(Proj(S), 𝒪_{Proj(S)})` and a canonical `S₀`-module map
>   `M₀ → Γ(Proj(S), M̃)`, each compatible with the description of the sections over a
>   positive-degree standard open and with the description of the stalks: the four equations say
>   that the restriction of the global section attached to `a`, resp. to `m`, is `a / 1`, resp.
>   `m / f ^ 0`, and that its germ at `x` is `a / 1`, resp. `m / 1`.
> 7. The identifications are functorial in the graded module. The identity map of `M` induces the
>   identity morphism of `M̃`; and for every graded `S`-module `N` and degree-preserving
>   `φ : M →ₗ[S] N`, with `M̃ ⟶ Ñ` the induced morphism: composition with a degree-preserving map
>   out of `N` is respected, and the identifications of (2), (5) and (6) are natural — over a
>   positive-degree standard open the induced morphism is the degree-zero part of the localized
>   map `M_f → N_f`, on the stalk at `x` it is the localization of `φ` at `𝔭`, and it takes the
>   global section attached to `m` to the global section attached to `φ m`.
> 8. In particular `M ↦ M̃` is an exact functor: a short exact sequence of graded `S`-modules with
>   degree-preserving maps goes to a short exact sequence of sheaves of `𝒪_{Proj(S)}`-modules.
>
> Every conjunct is the separate statement that proves it; the separate registrations of the tag
> are on those.

```lean
theorem sections_restriction_stalks_functorial_exact :
    (∀ (f : S) (d : ℕ), f ∈ 𝒮 d → 0 < d →
        Nonempty (CommRingCat.of (HomogeneousLocalization.Away 𝒮 f) ≅
          (AlgebraicGeometry.Proj 𝒮).presheaf.obj (op (Proj.basicOpen 𝒮 f)))) ∧
      (∀ (f : S) (d : ℕ), f ∈ 𝒮 d → 0 < d →
        Nonempty ((ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.obj
            (op (ProjectiveSpectrum.basicOpen 𝒮 f)) ≃ₗ[HomogeneousLocalization.Away 𝒮 f]
          GradedModuleDegreeZeroLocalization 𝒮 𝒨 f)) ∧
      (∀ (f g : S) (d e : ℕ) (hf : f ∈ 𝒮 d) (hd : 0 < d) (hg : g ∈ 𝒮 e) (he : 0 < e)
          (hfg : ProjectiveSpectrum.basicOpen 𝒮 g ≤ ProjectiveSpectrum.basicOpen 𝒮 f),
        CommRingCat.ofHom (ProjectiveSpectrum.degreeZeroRingMap 𝒮 f g
              ⟨d, hd, hf⟩ ⟨e, he, hg⟩ hfg).toRingHom ≫
            (Proj.basicOpenIsoAway 𝒮 g hg he).hom =
          (Proj.basicOpenIsoAway 𝒮 f hf hd).hom ≫
            (AlgebraicGeometry.Proj 𝒮).presheaf.map (homOfLE hfg).op) ∧
      (∀ (f g : S) (hf : ∃ d : ℕ, 0 < d ∧ f ∈ 𝒮 d) (hg : ∃ d : ℕ, 0 < d ∧ g ∈ 𝒮 d)
          (hfg : ProjectiveSpectrum.basicOpen 𝒮 g ≤ ProjectiveSpectrum.basicOpen 𝒮 f)
          (a : GradedModuleDegreeZeroLocalization 𝒮 𝒨 f),
        (ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.map (homOfLE hfg).op
            (ProjectiveSpectrum.Proj.degreeZeroToSection 𝒮 𝒨 f a) =
          ProjectiveSpectrum.Proj.degreeZeroToSection 𝒮 𝒨 g
            ((ProjectiveSpectrum.moduleRestrictionMaps 𝒮 𝒨 f g hf hg hfg).degreeZeroMap a)) ∧
      (∀ x : ProjectiveSpectrum.top 𝒮,
        Nonempty ((ProjectiveSpectrum.Proj.structureSheaf 𝒮).presheaf.stalk x ≃+*
          HomogeneousLocalization.AtPrime 𝒮 x.asHomogeneousIdeal.toIdeal)) ∧
      (∀ x : ProjectiveSpectrum.top 𝒮,
        Nonempty
          (letI : Module ((ProjectiveSpectrum.Proj.structureSheaf 𝒮).presheaf.stalk x)
              (ProjStalkGlobalSections.degreeZeroModuleAt 𝒮 𝒨 x) :=
            Module.compHom _ (Proj.stalkIso' 𝒮 x).toRingHom
          ProjStalkGlobalSections.associatedModuleSheafStalk 𝒮 𝒨 x ≃ₗ[
              (ProjectiveSpectrum.Proj.structureSheaf 𝒮).presheaf.stalk x]
            ProjStalkGlobalSections.degreeZeroModuleAt 𝒮 𝒨 x)) ∧
      Nonempty (𝒮 0 →+* (ProjectiveSpectrum.Proj.structureSheaf 𝒮).1.obj (op ⊤)) ∧
      (∀ (f : S) (a : 𝒮 0),
        (ProjectiveSpectrum.Proj.structureSheaf 𝒮).1.map (homOfLE le_top).op
            (ProjStalkGlobalSections.degreeZeroRingToGlobalSections 𝒮 a) =
          (ProjectiveSpectrum.Proj.awayToSection 𝒮 f).hom
            (HomogeneousLocalization.fromZeroRingHom 𝒮 (Submonoid.powers f) a)) ∧
      (∀ (x : ProjectiveSpectrum.top 𝒮) (a : 𝒮 0),
        Proj.stalkIso' 𝒮 x ((ProjectiveSpectrum.Proj.structureSheaf 𝒮).presheaf.germ ⊤ x trivial
            (ProjStalkGlobalSections.degreeZeroRingToGlobalSections 𝒮 a)) =
          HomogeneousLocalization.fromZeroRingHom 𝒮 x.asHomogeneousIdeal.toIdeal.primeCompl a) ∧
      Nonempty
        (letI : Module (𝒮 0)
            ((ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.obj (op ⊤)) :=
          Module.compHom _ (ProjStalkGlobalSections.degreeZeroRingToGlobalSections 𝒮)
        𝒨 0 →ₗ[𝒮 0] (ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.obj (op ⊤)) ∧
      (∀ (f : S) (d : ℕ) (hf : f ∈ 𝒮 d) (hd : 0 < d) (m : 𝒨 0),
        ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒨 hf hd
            ((ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.map (homOfLE le_top).op
              (ProjStalkGlobalSections.degreeZeroToGlobalSections 𝒮 𝒨 m)) =
          ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 𝒨 hf 0 m.1 (mem_zero_nsmul 𝒨 d m)) ∧
      (∀ (x : ProjectiveSpectrum.top 𝒮) (m : 𝒨 0),
        ((ProjStalkGlobalSections.associatedModuleSheafStalkEquiv 𝒮 𝒨 x
              (ProjStalkGlobalSections.associatedModuleSheafGerm 𝒮 𝒨 x ⊤ trivial
                (ProjStalkGlobalSections.degreeZeroToGlobalSections 𝒮 𝒨 m)) :
            ProjStalkGlobalSections.degreeZeroModuleAt 𝒮 𝒨 x) :
              ProjectiveSpectrum.Proj.ModuleFiber (M := M) 𝒮 x) =
          LocalizedModule.mk m.1 (1 : x.asHomogeneousIdeal.toIdeal.primeCompl)) ∧
      (associatedModuleSheafMap 𝒮 𝒨 𝒨 (LinearMap.id : M →ₗ[S] M) (fun _ _ hm => hm) = 𝟙 _) ∧
      (∀ (N : Type u) [AddCommGroup N] [Module S N] {υ : Type t'} [SetLike υ N]
          [AddSubgroupClass υ N] (𝒩 : ℤ → υ) [Decomposition 𝒩] [SetLike.GradedSMul 𝒮 𝒩]
          (φ : M →ₗ[S] N) (hφ : ∀ i (m : M), m ∈ 𝒨 i → φ m ∈ 𝒩 i),
        (∀ (P : Type u) [AddCommGroup P] [Module S P] {ρ : Type t''} [SetLike ρ P]
              [AddSubgroupClass ρ P] (𝒬 : ℤ → ρ) [Decomposition 𝒬] [SetLike.GradedSMul 𝒮 𝒬]
              (ψ : N →ₗ[S] P) (hψ : ∀ i (n : N), n ∈ 𝒩 i → ψ n ∈ 𝒬 i),
            associatedModuleSheafMap 𝒮 𝒨 𝒬 (ψ.comp φ) (fun i m hm => hψ i (φ m) (hφ i m hm)) =
              associatedModuleSheafMap 𝒮 𝒨 𝒩 φ hφ ≫ associatedModuleSheafMap 𝒮 𝒩 𝒬 ψ hψ) ∧
          (∀ (f : S) (d : ℕ) (hf : f ∈ 𝒮 d) (hd : 0 < d)
              (s : (ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨).val.obj
                (op (ProjectiveSpectrum.basicOpen 𝒮 f))),
            ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒩 hf hd
                  ((associatedModuleSheafMap 𝒮 𝒨 𝒩 φ hφ).val.app _ s) :
                GradedModuleDegreeZeroLocalization 𝒮 𝒩 f) :
                  LocalizedModule.Away (R := S) f N) =
              LocalizedModule.map (Submonoid.powers f) φ
                (ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒨 hf hd s :
                  GradedModuleDegreeZeroLocalization 𝒮 𝒨 f)) ∧
          (∀ (x : ProjectiveSpectrum.top 𝒮)
              (s : ProjStalkGlobalSections.associatedModuleSheafStalk 𝒮 𝒨 x),
            ((ProjStalkGlobalSections.associatedModuleSheafStalkEquiv 𝒮 𝒩 x
                  (colim.map (Functor.whiskerLeft (OpenNhds.inclusion x).op
                    ((PresheafOfModules.toPresheaf _).map
                      (associatedModuleSheafMap 𝒮 𝒨 𝒩 φ hφ).val)) s) :
                ProjStalkGlobalSections.degreeZeroModuleAt 𝒮 𝒩 x) :
                  ProjectiveSpectrum.Proj.ModuleFiber (M := N) 𝒮 x) =
              LocalizedModule.map x.asHomogeneousIdeal.toIdeal.primeCompl φ
                (ProjStalkGlobalSections.associatedModuleSheafStalkEquiv 𝒮 𝒨 x s :
                  ProjStalkGlobalSections.degreeZeroModuleAt 𝒮 𝒨 x)) ∧
          (∀ m : 𝒨 0,
            (associatedModuleSheafMap 𝒮 𝒨 𝒩 φ hφ).val.app (op ⊤)
                (ProjStalkGlobalSections.degreeZeroToGlobalSections 𝒮 𝒨 m) =
              ProjStalkGlobalSections.degreeZeroToGlobalSections 𝒮 𝒩
                ⟨φ m.1, hφ 0 m.1 m.2⟩)) ∧
      (∀ {X Y Z : GradedModuleCat.{u, u, w} 𝒮} (α : X ⟶ Y) (β : Y ⟶ Z),
        Function.Injective α.toLinearMap → Function.Surjective β.toLinearMap →
        ∀ hexact : Function.Exact α.toLinearMap β.toLinearMap,
          (ShortComplex.mk ((associatedModuleSheafFunctor 𝒮).map α)
            ((associatedModuleSheafFunctor 𝒮).map β)
            (associatedModuleSheafFunctor_map_comp_eq_zero α β
              fun m => (hexact (α.toLinearMap m)).mpr ⟨m, rfl⟩)).ShortExact)
```

## Tag 01MA, a lemma

[Tag 01MA](https://stacks.math.columbia.edu/tag/01MA) in the Stacks Project.

**`AlgebraicGeometry.Proj.exists_homogeneous_awayι_preimage_basicOpen_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjBasicOpen.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjBasicOpen.lean#L360).

> **Stacks Project, Tag 01MA.** Let `f` be a homogeneous element of positive degree `m` in a
> graded ring `A`, and let `g` be an element of the degree-zero localization `A₍f₎`, so that `D(g)`
> is a standard open of `Spec A₍f₎`. Then there is a homogeneous element `h` of positive degree
> `n • m` such that `g = h / f ^ n`, such that `D₊(h) ⊆ D₊(f)`, and such that `D(g)` and `D₊(h)`
> correspond under the open immersion `Spec A₍f₎ ⟶ Proj A` identifying `Spec A₍f₎` with `D₊(f)`:
> `D(g)` is the preimage of `D₊(h)`, and `D₊(h)` is the image of `D(g)`.

```lean
public theorem exists_homogeneous_awayι_preimage_basicOpen_eq {f : A} {m : ℕ} (hf : f ∈ 𝒜 m)
    (hm : 0 < m) (g : Away 𝒜 f) :
    ∃ (n : ℕ) (h : A) (hh : h ∈ 𝒜 (n • m)), 0 < n • m ∧
      Away.mk 𝒜 hf n h hh = g ∧
      AlgebraicGeometry.Proj.basicOpen 𝒜 h ≤ AlgebraicGeometry.Proj.basicOpen 𝒜 f ∧
      AlgebraicGeometry.Proj.awayι 𝒜 f hf hm ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 h =
        PrimeSpectrum.basicOpen g ∧
      AlgebraicGeometry.Proj.awayι 𝒜 f hf hm ''ᵁ PrimeSpectrum.basicOpen g =
        AlgebraicGeometry.Proj.basicOpen 𝒜 h
```

## Tag 01MB, a lemma

[Tag 01MB](https://stacks.math.columbia.edu/tag/01MB) in the Stacks Project.

**`AlgebraicGeometry.associatedModuleSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean#L454). The attribute's comment: “associated graded-module sheaves are quasi-coherent”. References: EGA II (3.2.1), “affine base”; EGA II (3.2.2), “affine base Y”.

> The sheaf of degree-zero local homogeneous fractions of a graded module on its projective
> spectrum is quasi-coherent.

```lean
instance associatedModuleSheaf_isQuasicoherent [Decomposition 𝒨] :
    SheafOfModules.IsQuasicoherent.{u, u, u}
      (ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.associatedModuleSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjGradedModuleQcoh/Quasicoherent.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjGradedModuleQcoh/Quasicoherent.lean#L247). The attribute's comment: “associated graded-module sheaves are quasi-coherent”. References: EGA II (3.2.1), “affine base”; EGA II (3.2.2), “affine base Y”.

> The sheaf of degree-zero local homogeneous fractions of a graded module on its projective
> spectrum is quasi-coherent.

```lean
public instance associatedModuleSheaf_isQuasicoherent :
    SheafOfModules.IsQuasicoherent.{u, u, u} (associatedModuleSheaf 𝒜 𝒨)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Proj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Proj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean#L74) (StacksFrontier): “the projective spectrum is a scheme”. References: EGA II (2.4.1), “(f)”; EGA II (3.1.1); EGA II (3.1.3), “special case”; EGA II (7.4.14), “more general”; EGA II (8.3.1), “special case”; EGA III (3.3.1), “special case”; EGA III (4.3.13); EGA IV (18.12.17).
- [`AlgebraicGeometry.Proj.basicOpenIsoSpec`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Proj.basicOpenIsoSpec#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean#L83) (StacksFrontier): “canonical standard-open identification”. References: EGA II (2.3.5); EGA II (2.3.6), “more general”; EGA II (2.4.1); EGA II (3.1.4), “special case”; EGA II (7.4.14), “partial”; SGA 6 VI (2.3.2), “(f), special case”.
- [`AlgebraicGeometry.Proj.isAffineOpen_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Proj.isAffineOpen_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjGradedRing/Basic.lean#L90) (StacksFrontier): “standard opens are affine”. References: EGA II (2.4.1), “(f)”; EGA II (3.1.4), “affineness of X_f over Y”; EGA II (5.5.7), “special case”; SGA 6 VI (2.3.2), “affineness of D₊(f)”.

## Tag 01MD, a lemma

[Tag 01MD](https://stacks.math.columbia.edu/tag/01MD) in the Stacks Project.

**`AlgebraicGeometry.Proj.compactSpace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjQuasiCompact.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjQuasiCompact.lean#L89). The attribute's comment: “quasi-compactness criterion”.

> The projective spectrum is quasi-compact exactly when finitely many
> positive-degree homogeneous elements generate an ideal whose radical contains
> the irrelevant ideal.

```lean
public theorem compactSpace_iff :
    CompactSpace (AlgebraicGeometry.Proj 𝒮) ↔
      ∃ s : Finset S,
        (∀ f ∈ s, ∃ d : ℕ, 0 < d ∧ f ∈ 𝒮 d) ∧
          (HomogeneousIdeal.irrelevant 𝒮).toIdeal ≤ (Ideal.span (s : Set S)).radical
```

**`AlgebraicGeometry.Proj.iSup_basicOpen_eq_top_of_irrelevant_le_radical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjQuasiCompact.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjQuasiCompact.lean#L124). The attribute's comment: “standard-open cover”. References: EGA II (2.3.14), “special case”.

> Elements whose span contains the irrelevant ideal up to radical have
> standard opens covering the projective spectrum.

```lean
public theorem iSup_basicOpen_eq_top_of_irrelevant_le_radical (s : Finset S)
    (h : (HomogeneousIdeal.irrelevant 𝒮).toIdeal ≤ (Ideal.span (s : Set S)).radical) :
    ⨆ f ∈ s, Proj.basicOpen 𝒮 f = ⊤
```

## Tag 01ME, a lemma

[Tag 01ME](https://stacks.math.columbia.edu/tag/01ME) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjToSpecZero.toSpecZero_base_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjToSpecZero.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjToSpecZero.lean#L85). The attribute's comment: “the canonical morphism Proj S → Spec S₀, equal on points to 𝔭 ↦ 𝔭 ∩ S₀”.

> **The canonical morphism `Proj 𝒜 ⟶ Spec 𝒜₀`** is `Proj.toSpecZero 𝒜`, glued from the ring
> maps `𝒜₀ → S_(f)` on the standard opens. On underlying topological spaces it is the map of the
> homogeneous spectrum: the inclusion `Proj 𝒜 ⊆ Spec S` followed by `Spec S → Spec 𝒜₀` induced by
> `𝒜₀ ⊆ S`, i.e. `𝔭 ↦ 𝔭 ∩ 𝒜₀`.

```lean
theorem toSpecZero_base_eq :
    ⇑(Proj.toSpecZero 𝒜) =
      PrimeSpectrum.comap (algebraMap (𝒜 0) A) ∘ _root_.Proj.toSpec 𝒜
```

## Tag 01MF, a lemma

[Tag 01MF](https://stacks.math.columbia.edu/tag/01MF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjToSpecZero.valuativeCriterion_toSpecZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjToSpecZero.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjToSpecZero.lean#L95). The attribute's comment: “existence and uniqueness parts of the valuative criterion for Proj S → Spec S₀”.

> **The valuative criterion for `Proj 𝒜 ⟶ Spec 𝒜₀`.** If `S` is finitely generated as an
> `𝒜₀`-algebra, then for every valuation ring `O` with fraction field `K` and every commutative
> square `Spec K ⟶ Proj 𝒜`, `Spec O ⟶ Spec 𝒜₀`, there exists a lift `Spec O ⟶ Proj 𝒜`
> (existence) and it is unique (uniqueness, from separatedness).

```lean
theorem valuativeCriterion_toSpecZero [Algebra.FiniteType (𝒜 0) A] :
    ValuativeCriterion (Proj.toSpecZero 𝒜)
```

## Tag 01MG, an example

[Tag 01MG](https://stacks.math.columbia.edu/tag/01MG) in the Stacks Project.

**`AlgebraicGeometry.FractionalExponentExample.exists_nonextendable_valuative_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjNonextendableValuativeMap.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjNonextendableValuativeMap.lean#L572).

> The specified valuative example: the canonical generic-fibre morphism induced by
> `polynomialMap` cannot be extended to the spectrum of the local valuation ring.

```lean
theorem exists_nonextendable_valuative_map :
    ∃ hm : positiveIdeal.IsPrime,
      letI : positiveIdeal.IsPrime := hm
      letI : GradedRing (MvPolynomial.homogeneousSubmodule ℕ ℂ) :=
        MvPolynomial.gradedAlgebra
      let A := Localization positiveIdeal.primeCompl
      let K := FractionRing A
      let φ : polynomialAlgebra →+* K :=
        (algebraMap fractionalExponentAlgebra K).comp polynomialMap.toRingHom
      let F : polynomialAlgebra →+* Γ(Spec (CommRingCat.of K), ⊤) :=
        (Scheme.ΓSpecIso (CommRingCat.of K)).inv.hom.comp φ
      (IsValuationRing A) ∧
        ∃ hf : (HomogeneousIdeal.irrelevant
            (MvPolynomial.homogeneousSubmodule ℕ ℂ)).toIdeal.map F = ⊤,
          ¬ ∃ g : Spec (CommRingCat.of A) ⟶
              Proj (MvPolynomial.homogeneousSubmodule ℕ ℂ),
            Spec.map (CommRingCat.ofHom (algebraMap A K)) ≫ g =
              Proj.fromOfGlobalSections
                (MvPolynomial.homogeneousSubmodule ℕ ℂ) F hf
```

## Tag 01MH, an example

[Tag 01MH](https://stacks.math.columbia.edu/tag/01MH) in the Stacks Project.

**`Stacks.IteratedSquareRootAlgebra.projCanonicalProperties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjIteratedSquareRootImage.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjIteratedSquareRootImage.lean#L367). The attribute's comment: “the example's six assertions in one statement”.

> **Stacks Project, Tag 01MH.** The worked example in a single statement, for the grading the
> source specifies on `S = ℂ[t][X₁, X₂, …]/(Xᵢ² - t Xᵢ₊₁)`, `deg Xᵢ = 2ⁱ⁻¹`. In order: the image
> of `t` lies in no point of `Proj S`; consecutive generators define the same standard open,
> `D₊(Xᵢ) = D₊(Xᵢ₊₁)`; `Proj S` is quasi-compact; it is affine, being the single standard open
> `D₊(X₁)`; the image of `Proj S → Spec ℂ[t]` is the distinguished open `D(t)`; and that morphism
> is therefore not closed.

```lean
public theorem projCanonicalProperties :
    (∀ p : ProjectiveSpectrum canonicalGrading.grading,
        algebraMap baseRing ring t ∉ p.asHomogeneousIdeal) ∧
      (∀ i : ℕ, ProjectiveSpectrum.basicOpen canonicalGrading.grading (x i) =
        ProjectiveSpectrum.basicOpen canonicalGrading.grading (x (i + 1))) ∧
      CompactSpace (AlgebraicGeometry.Proj canonicalGrading.grading) ∧
      Proj.basicOpen canonicalGrading.grading (x 0) = ⊤ ∧
      IsAffine (AlgebraicGeometry.Proj canonicalGrading.grading) ∧
      Set.range
          (Proj.toSpecZero canonicalGrading.grading ≫
            Spec.map (CommRingCat.ofHom
              ((GradedRing.projZeroRingHom' canonicalGrading.grading).comp
                (algebraMap baseRing ring)))).base =
        ((Spec (.of baseRing)).basicOpen
          ((Scheme.ΓSpecIso (.of baseRing)).inv t) : Set (Spec (.of baseRing))) ∧
      ¬ IsClosed (Set.range
        (Proj.toSpecZero canonicalGrading.grading ≫
          Spec.map (CommRingCat.ofHom
            ((GradedRing.projZeroRingHom' canonicalGrading.grading).comp
              (algebraMap baseRing ring)))).base)
```

## Tag 01MI, an example

[Tag 01MI](https://stacks.math.columbia.edu/tag/01MI) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpace.isIso_toSpecZero_oneVariable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfPolynomialOneVariable.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfPolynomialOneVariable.lean#L119).

> **`Proj` of a polynomial ring in one variable is the spectrum of the coefficient ring.** The
> canonical morphism `Proj A[T] ⟶ Spec A[T]₀` of a graded ring to the spectrum of its degree-zero
> part is an isomorphism when `A[T]` is the polynomial ring in one variable of degree one.

```lean
public theorem isIso_toSpecZero_oneVariable :
    IsIso (Proj.toSpecZero (homogeneousSubmodule (Fin 1) A))
```

## Tag 0G5W, an example

[Tag 0G5W](https://stacks.math.columbia.edu/tag/0G5W) in the Stacks Project.

**`AlgebraicGeometry.openProjAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L88). The attribute's comment: “the graded subring”.

> The subalgebra of `A[T]` generated by `A` and all `f Tⁿ` with `D(f) ⊆ U`.

```lean
public noncomputable def openProjAlgebra (U : (Spec (.of A)).Opens) :
    Subalgebra A (MvPolynomial (Fin 1) A)
```

**`AlgebraicGeometry.openProjGrading`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L95). The attribute's comment: “the homogeneous components”.

> The degree-`n` piece of the indicated subalgebra, inherited from polynomial degree.

```lean
public noncomputable def openProjGrading (U : (Spec (.of A)).Opens) (n : ℕ) :
    Submodule A (openProjAlgebra U)
```

**`AlgebraicGeometry.openProjGradedRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L238). The attribute's comment: “the grading”.

> The polynomial-degree decomposition restricts to the algebra of the open.

```lean
public noncomputable def openProjGradedRing (U : (Spec (.of A)).Opens) :
    GradedRing (openProjGrading U)
```

**`AlgebraicGeometry.openProjDegreeZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L265). The attribute's comment: “the degree-zero ring”.

> The canonical identification of the degree-zero part with the coefficient ring.

```lean
public noncomputable def openProjDegreeZeroEquiv (U : (Spec (.of A)).Opens) :
    letI := openProjGradedRing U
    A ≃+* openProjGrading U 0
```

**`AlgebraicGeometry.openProjDegreeZeroEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L306). The attribute's comment: “the canonical degree-zero identification”.

> The degree-zero identification sends a coefficient to its image in the subalgebra.

```lean
public theorem openProjDegreeZeroEquiv_apply (U : (Spec (.of A)).Opens) (a : A) :
    letI := openProjGradedRing U
    ((openProjDegreeZeroEquiv U a : openProjGrading U 0) : openProjAlgebra U) =
      algebraMap A (openProjAlgebra U) a
```

**`AlgebraicGeometry.projOpenIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L1033). The attribute's comment: “the isomorphism with the open subscheme”.

> The projective spectrum of the indicated algebra is the chosen open subscheme.

```lean
public noncomputable def projOpenIso (U : (Spec (.of A)).Opens) :
    letI := openProjGradedRing U
    AlgebraicGeometry.Proj (openProjGrading U) ≅ U.toScheme
```

**`AlgebraicGeometry.projOpenIso_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean, line 1043](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjOfOpenInAffine.lean#L1043). The attribute's comment: “compatibility with the structure morphism”.

> Under the isomorphism, the canonical morphism to `Spec A` is inclusion.

```lean
public theorem projOpenIso_hom_comp (U : (Spec (.of A)).Opens) :
    letI := openProjGradedRing U
    Proj.toSpecZero (openProjGrading U) ≫
      Spec.map (CommRingCat.ofHom (openProjDegreeZeroEquiv U).toRingHom) =
        (projOpenIso U).hom ≫ U.ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.8, Tag 01M3](https://stacks.math.columbia.edu/tag/01M3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
