---
declaration: section
origin: cited
lean: Proj, gradedPrimesComparison_isHomeomorph, ProjectiveSpectrum.exists_homeomorph_awayGradedPrimes, ProjectiveSpectrum.exists_not_compactSpace, ProjectiveSpectrum.isOpen_basicOpen_of_mem, ProjectiveSpectrum.basicOpen_mul_of_mem, ProjectiveSpectrum.basicOpen_eq_basicOpen_proj_zero_sup_iSup, ProjectiveSpectrum.basicOpen_eq_iSup_basicOpen_mul_of_mem_zero
statement: formalized
proof: formalized
---

# 10.57 Proj of a graded ring

Section 10.57 of the Stacks Project, [Tag 00JM](https://stacks.math.columbia.edu/tag/00JM). 10 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00JN, a definition

[Tag 00JN](https://stacks.math.columbia.edu/tag/00JN) in the Stacks Project.

**`Proj`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean#L51). References: EGA II (2.3.1), “set of graded primes”; EGA III (4.3.13).

> The homogeneous spectrum `Proj 𝒜` of a graded ring: the set of homogeneous prime
> ideals `𝔭` of `A` with `𝒜₊ ⊄ 𝔭`, topologized by the subspace topology from `Spec A`.

```lean
abbrev Proj : Type _
```

## Tag 00JO, a lemma

[Tag 00JO](https://stacks.math.columbia.edu/tag/00JO) in the Stacks Project.

**`gradedPrimesComparison_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean, line 467](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean#L467).

> Let `S` be a `ℤ`-graded ring containing a homogeneous invertible
> element of positive degree. Then the comparison map `Φ : G → Spec(S₀)`,
> `q ↦ q ∩ S₀`, from the space of `ℤ`-graded primes of `S` (with the subspace topology) to
> `Spec(S₀)`, is a homeomorphism.

```lean
theorem gradedPrimesComparison_isHomeomorph
    (hf : HasHomogeneousUnitOfPosDegree 𝒜) :
    IsHomeomorph (gradedPrimesComparison 𝒜)
```

## Tag 00JP, a lemma

[Tag 00JP](https://stacks.math.columbia.edu/tag/00JP) in the Stacks Project.

**`ProjectiveSpectrum.exists_homeomorph_awayGradedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/AwayGradedPrimes.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/AwayGradedPrimes.lean#L203). The attribute's comment: “Assertion (6): for `f` homogeneous of positive degree, `S → S_f ← S_(f)` induce homeomorphisms `D₊(f) ← {ℤ-graded primes of S_f} → Spec(S_(f))`; the second is the first composed with Mathlib's `AlgebraicGeometry.projIsoSpecTopComponent`.”.

> For `f` homogeneous of positive degree, the ring maps `A → A_f ← A₍f₎` induce homeomorphisms
> `D₊(f) ← {ℤ-graded primes of A_f} → Spec A₍f₎`, each sending a prime to its pullback.

```lean
theorem exists_homeomorph_awayGradedPrimes {f : A} {m : ℕ} (f_deg : f ∈ 𝒜 m) (hm : 0 < m) :
    ∃ (e₁ : awayGradedPrimes 𝒜 f m ≃ₜ basicOpen 𝒜 f)
      (e₂ : awayGradedPrimes 𝒜 f m ≃ₜ PrimeSpectrum (HomogeneousLocalization.Away 𝒜 f)),
      (∀ q, (e₁ q).1.asHomogeneousIdeal.toIdeal = q.1.asIdeal.comap (algebraMap A (Away f))) ∧
      ∀ q, (e₂ q).asIdeal =
        q.1.asIdeal.comap (algebraMap (HomogeneousLocalization.Away 𝒜 f) (Away f))
```

**`ProjectiveSpectrum.exists_not_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/NotQuasiCompact.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/NotQuasiCompact.lean#L110). The attribute's comment: “Assertion (7): there is a graded ring `S` with `Proj(S)` not quasi-compact, namely `S = ℤ[X₁, X₂, …]` (`not_compactSpace_mvPolynomial`).”.

> **Stacks 00JP (7).** There is a graded ring `S` whose homogeneous spectrum `Proj S` is not
> quasi-compact, namely `ℤ[X₀, X₁, …]` graded by total degree.

```lean
theorem exists_not_compactSpace :
    ∃ (S : Type) (_ : CommRing S) (𝒜 : ℕ → Submodule ℤ S) (_ : GradedRing 𝒜),
      ¬ CompactSpace (ProjectiveSpectrum 𝒜)
```

**`ProjectiveSpectrum.isOpen_basicOpen_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L120). The attribute's comment: “Assertion (1): the sets `D₊(f)`, `f` homogeneous of positive degree, are open (Mathlib's `ProjectiveSpectrum.isOpen_basicOpen`).”.

> A standard open `D₊(f)`, for `f` homogeneous of positive degree, is open in `Proj 𝒜`.

```lean
theorem isOpen_basicOpen_of_mem {f : A} {d : ℕ} (_hf : f ∈ 𝒜 d) (_hd : 0 < d) :
    IsOpen (basicOpen 𝒜 f : Set (ProjectiveSpectrum 𝒜))
```

**`ProjectiveSpectrum.basicOpen_mul_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L127). The attribute's comment: “Assertion (2): `D₊(ff') = D₊(f) ∩ D₊(f')` (Mathlib's `ProjectiveSpectrum.basicOpen_mul`).”.

> For `f`, `f'` homogeneous of positive degree, `D₊(ff') = D₊(f) ∩ D₊(f')`.

```lean
theorem basicOpen_mul_of_mem {f f' : A} {d d' : ℕ} (_hf : f ∈ 𝒜 d) (_hd : 0 < d)
    (_hf' : f' ∈ 𝒜 d') (_hd' : 0 < d') :
    basicOpen 𝒜 (f * f') = basicOpen 𝒜 f ⊓ basicOpen 𝒜 f'
```

**`ProjectiveSpectrum.basicOpen_eq_basicOpen_proj_zero_sup_iSup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L137). The attribute's comment: “Assertion (3): `D(g) ∩ Proj(S) = (D(g₀) ∩ Proj(S)) ∪ ⋃_{i ≥ 1} D₊(gᵢ)` for `g = ∑ gᵢ` with `gᵢ ∈ Sᵢ`; derived from Mathlib's `ProjectiveSpectrum.basicOpen_eq_union_of_projection`.”.

> For `g ∈ A` with homogeneous components `gᵢ = proj i g`, the set `D(g) ∩ Proj 𝒜` of relevant
> homogeneous primes not containing `g` is `(D(g₀) ∩ Proj 𝒜) ∪ ⋃_{i ≥ 1} D₊(gᵢ)`.

```lean
theorem basicOpen_eq_basicOpen_proj_zero_sup_iSup (g : A) :
    basicOpen 𝒜 g = basicOpen 𝒜 (GradedRing.proj 𝒜 0 g) ⊔
      ⨆ (i : ℕ) (_ : 0 < i), basicOpen 𝒜 (GradedRing.proj 𝒜 i g)
```

**`ProjectiveSpectrum.basicOpen_eq_iSup_basicOpen_mul_of_mem_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L152). The attribute's comment: “Assertion (4): `D(g₀) ∩ Proj(S) = ⋃_{f ∈ S_d, d ≥ 1} D₊(g₀ f)` for `g₀ ∈ S₀`.”.

> For `g₀` homogeneous of degree `0`, `D(g₀) ∩ Proj 𝒜 = ⋃_{f ∈ 𝒜 d, d ≥ 1} D₊(g₀ f)`.

```lean
theorem basicOpen_eq_iSup_basicOpen_mul_of_mem_zero {g₀ : A} (_hg₀ : g₀ ∈ 𝒜 0) :
    basicOpen 𝒜 g₀ = ⨆ (d : ℕ) (_ : 0 < d) (f : A) (_ : f ∈ 𝒜 d), basicOpen 𝒜 (g₀ * f)
```

**`ProjectiveSpectrum.isTopologicalBasis_basicOpen_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L169). The attribute's comment: “Assertion (5): the opens `D₊(f)`, `f` homogeneous of positive degree, form a basis of the topology of `Proj(S)`.”.

> The standard opens `D₊(f)`, for `f` homogeneous of positive degree, form a basis of the
> topology of `Proj 𝒜`.

```lean
theorem isTopologicalBasis_basicOpen_of_pos :
    TopologicalSpace.IsTopologicalBasis
      {U : Set (ProjectiveSpectrum 𝒜) |
        ∃ (d : ℕ) (f : A), 0 < d ∧ f ∈ 𝒜 d ∧ U = basicOpen 𝒜 f}
```

**`ProjectiveSpectrum.isClosed_zeroLocus_homogeneousIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L202). The attribute's comment: “Assertion (8): the sets `V₊(I)`, `I` homogeneous, are closed (Mathlib's `ProjectiveSpectrum.isClosed_zeroLocus`).”.

> For a homogeneous ideal `I`, the set `V₊(I)` is closed in `Proj 𝒜`.

```lean
theorem isClosed_zeroLocus_homogeneousIdeal (I : HomogeneousIdeal 𝒜) :
    IsClosed (zeroLocus 𝒜 (I : Set A))
```

**`ProjectiveSpectrum.exists_homogeneousIdeal_eq_zeroLocus_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L210). The attribute's comment: “Assertion (9): every closed `T ⊆ Proj(S)` is `V₊(I)` for a homogeneous ideal `I`, namely `I = ProjectiveSpectrum.vanishingIdeal T` (Mathlib's `ProjectiveSpectrum.zeroLocus_vanishingIdeal_eq_closure`).”.

> Every closed subset of `Proj 𝒜` is `V₊(I)` for some homogeneous ideal `I`.

```lean
theorem exists_homogeneousIdeal_eq_zeroLocus_of_isClosed {T : Set (ProjectiveSpectrum 𝒜)}
    (hT : IsClosed T) : ∃ I : HomogeneousIdeal 𝒜, T = zeroLocus 𝒜 (I : Set A)
```

**`ProjectiveSpectrum.zeroLocus_empty_iff_irrelevant_le_radical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpectrum/Topology.lean#L243). The attribute's comment: “Assertion (10): for a homogeneous ideal `I`, `V₊(I) = ∅` if and only if `S₊ ⊆ √I`.”. References: EGA II (2.3.16); EGA II (2.3.13), “more general”; EGA II (2.3.2), “V₊(S₊)=∅”; EGA II (8.3.4), “partial”.

> The projective zero locus `V₊(I)` of a homogeneous ideal `I` of a graded ring `A` is empty if
> and only if the irrelevant ideal `𝒜₊` is contained in the radical of `I`.

```lean
theorem zeroLocus_empty_iff_irrelevant_le_radical (I : HomogeneousIdeal 𝒜) :
    zeroLocus 𝒜 (I : Set A) = ∅ ↔ HomogeneousIdeal.irrelevant 𝒜 ≤ I.radical
```

## Tag 00JQ, an example

[Tag 00JQ](https://stacks.math.columbia.edu/tag/00JQ) in the Stacks Project.

**`projToSpec_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/Defs.lean#L623). References: EGA II (3.1.7), “partial”.

> The natural map `Proj(R[X]) → Spec(R)` is a bijection and a homeomorphism.

```lean
theorem projToSpec_isHomeomorph : IsHomeomorph (projToSpec R)
```

## Tag 00JR, a lemma

[Tag 00JR](https://stacks.math.columbia.edu/tag/00JR) in the Stacks Project.

**`HomogeneousLocalization.isLocalizedModule_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/AtPrime.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/AtPrime.lean#L521). The attribute's comment: “The module equality `M_(𝔭) = (M_(f))_{𝔭'}`; the ring equality `S_(𝔭) = (S_(f))_{𝔭'}` is `AlgebraicGeometry.ProjectiveSpectrum.Proj.isLocalization_atPrime`.”.

> Let `A` be a graded ring, let `M` be a graded `A`-module, let `𝔭` be a homogeneous prime ideal
> of `A`, and let `f ∈ A` be homogeneous of positive degree with `f ∉ 𝔭`. Let `𝔭'` be the prime of the
> degree-zero localization `A⁰_f` consisting of the fractions `a/fⁿ` with `a ∈ 𝔭`. Then the
> `A⁰_f`-module `M_(𝔭)` of degree-zero fractions `y/g` with `g ∉ 𝔭` homogeneous is the localization of
> the `A⁰_f`-module `M_(f)` of degree-zero fractions `y/fⁿ` at `𝔭'`.

```lean
public theorem isLocalizedModule_atPrime {σ τ A M : Type*} [CommRing A] [SetLike σ A]
    [AddSubgroupClass σ A] [AddCommGroup M] [Module A M] [SetLike τ M] [AddSubmonoidClass τ M]
    (𝒜 : ℕ → σ) [GradedRing 𝒜] (ℳ : ℤ → τ) [DirectSum.Decomposition ℳ]
    (hℳ : ∀ (i : ℕ) (j : ℤ) (a : A) (y : M), a ∈ 𝒜 i → y ∈ ℳ j → a • y ∈ ℳ (i + j)) (𝔭 : Ideal A)
    [𝔭.IsPrime] (h𝔭 : 𝔭.IsHomogeneous 𝒜) {f : A} {m : ℕ} (hf : f ∈ 𝒜 m) (hm : 0 < m) (hf𝔭 : f ∉ 𝔭)
    (𝔭' : Ideal (Away 𝒜 f)) [𝔭'.IsPrime]
    (h𝔭' : ∀ z : NumDenSameDeg 𝒜 (Submonoid.powers f), mk z ∈ 𝔭' ↔ (z.num : A) ∈ 𝔭) :
    letI : Module (Away 𝒜 f) (LocalizedModule (Submonoid.powers f) M) :=
      Module.compHom _ (algebraMap (Away 𝒜 f) (Localization (Submonoid.powers f)))
    letI : Module (Away 𝒜 f) (LocalizedModule 𝔭.primeCompl M) :=
      Module.compHom _
        ((algebraMap (AtPrime 𝒜 𝔭) (Localization 𝔭.primeCompl)).comp
          (mapId 𝒜 (Submonoid.powers_le.mpr hf𝔭)))
    ∃ φ :
      ↥(Submodule.span (Away 𝒜 f)
            {z : LocalizedModule (Submonoid.powers f) M |
              ∃ (i : ℕ) (y : M) (g : Submonoid.powers f),
                y ∈ ℳ (i : ℤ) ∧ (g : A) ∈ 𝒜 i ∧ z = .mk y g}) →ₗ[Away 𝒜 f]
        ↥(Submodule.span (Away 𝒜 f)
            {z : LocalizedModule 𝔭.primeCompl M |
              ∃ (i : ℕ) (y : M) (g : 𝔭.primeCompl), y ∈ ℳ (i : ℤ) ∧ (g : A) ∈ 𝒜 i ∧ z = .mk y g}),
      (∀ z,
          (φ z : LocalizedModule 𝔭.primeCompl M) =
            LocalizedModule.liftOfLE _ _ (Submonoid.powers_le.mpr hf𝔭) (z : _)) ∧
        IsLocalizedModule 𝔭'.primeCompl φ
```

## Tag 00JS, a lemma

[Tag 00JS](https://stacks.math.columbia.edu/tag/00JS) in the Stacks Project.

**`graded_silly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/PrimeAvoidance.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/PrimeAvoidance.lean#L255). References: SGA 3 V (7.2), “partial”.

> Graded prime avoidance: if `p₁, …, p_r` are homogeneous prime ideals of a graded ring and
> `I` is a homogeneous ideal contained in the irrelevant ideal with `¬ I ≤ pᵢ` for every `i`,
> then `I` contains a homogeneous element of positive degree lying outside every `pᵢ`.

```lean
theorem graded_silly
    {r : ℕ} (p : Fin r → HomogeneousIdeal 𝒜) (hp : ∀ i, (p i).toIdeal.IsPrime)
    (I : HomogeneousIdeal 𝒜) (hI : I ≤ HomogeneousIdeal.irrelevant 𝒜)
    (hIp : ∀ i, ¬ I ≤ p i) :
    ∃ x : S, x ∈ I.toIdeal ∧ (∃ d : ℕ, 1 ≤ d ∧ x ∈ 𝒜 d) ∧ ∀ i, x ∉ (p i).toIdeal
```

## Tag 00JT, a lemma

[Tag 00JT](https://stacks.math.columbia.edu/tag/00JT) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.IsPrime.homogeneousCore`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsPrime.homogeneousCore#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean#L51) (StacksFrontier). References: EGA II (8.3.7), “graded prime q exists”.
- [`Ideal.homogeneousCore`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.homogeneousCore#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean#L53) (StacksFrontier): “the homogeneous ideal generated by the homogeneous elements of `𝔭`”.

## Tag 00JU, a lemma

[Tag 00JU](https://stacks.math.columbia.edu/tag/00JU) in the Stacks Project.

**`Ideal.IsHomogeneous.isHomogeneous_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean#L65). The attribute's comment: “part (2)”.

> Part (2): Given a homogeneous ideal `I`, any minimal prime over `I` is
> homogeneous.

```lean
theorem Ideal.IsHomogeneous.isHomogeneous_of_mem_minimalPrimes
    {I p : Ideal A} (hI : I.IsHomogeneous 𝒜) (hp : p ∈ I.minimalPrimes) :
    p.IsHomogeneous 𝒜
```

**`GradedRing.isHomogeneous_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Proj/HomogeneousPrimes.lean#L78). The attribute's comment: “part (1)”.

> Part (1): Any minimal prime of a graded ring is a homogeneous ideal. This
> is the special case of part (2) where `I = ⊥`.

```lean
theorem GradedRing.isHomogeneous_of_mem_minimalPrimes
    {p : Ideal A} (hp : p ∈ minimalPrimes A) :
    p.IsHomogeneous 𝒜
```

## Tag 07Z2, a lemma

[Tag 07Z2](https://stacks.math.columbia.edu/tag/07Z2) in the Stacks Project.

**`homogeneousLocalization_away_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/Finiteness.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/Finiteness.lean#L43). The attribute's comment: “(1)”.

> **Tag 07Z2, part 1.**
> Let `S` be a graded `R`-algebra of finite type over `R`, and let `f ∈ S_d` be
> homogeneous with `d ≥ 1`.  Then the degree-`0` localization `S_(f)` is of finite
> type over `R` (a finitely generated `R`-algebra).

```lean
theorem homogeneousLocalization_away_finiteType (hf : f ∈ 𝒜 d) [Algebra.FiniteType R S] :
    Algebra.FiniteType R (SLoc 𝒜 f)
```

**`moduleLocalization_away_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/Finiteness.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/HomogeneousLocalization/DegreeZero/Finiteness.lean#L716). The attribute's comment: “(2)”.

> **Tag 07Z2, part 2.**
> Under the same hypotheses, if moreover `M` is a finite (finitely generated)
> graded `S`-module — with grading `ℳ` satisfying `M = ⨁_n ℳ n`
> (`DirectSum.Decomposition ℳ`) and the compatibility `𝒜 i · ℳ j ⊆ ℳ (i + j)`
> (`SetLike.GradedSMul 𝒜 ℳ`) — then the degree-`0` localization `M_(f)` is a
> finite `S_(f)`-module.

```lean
theorem moduleLocalization_away_finite (hf : f ∈ 𝒜 d) (hd : 1 ≤ d) [Algebra.FiniteType R S]
    [Module.Finite S M] : Module.Finite (SLoc 𝒜 f) (MLoc 𝒜 ℳ f d)
```

## Tag 052N, a lemma

[Tag 052N](https://stacks.math.columbia.edu/tag/052N) in the Stacks Project.

**`exists_gradedAlgebra_degZeroPart_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/ReesModel.lean, line 2290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/ReesModel.lean#L2290).

> **Stacks Tag 052N (Lemma 10.57.10).**
> Let `R` be a ring, `R'` a finite type `R`-algebra, and `M` a finite `R'`-module.
> Then there exist a graded `R`-algebra `S`, a graded `S`-module `N`, and a
> degree-`1` element `f ∈ S₁` such that `R' ≅ S_(f)` as `R`-algebras, `M ≅ N_(f)`
> as modules (compatibly), `S₀ = R`, `S` is generated by finitely many degree-`1`
> elements over `R`, and `N` is a finite `S`-module.  Here `S_(f)` is
> `HomogeneousLocalization.Away 𝒜 f` and `N_(f)` is `degZeroPart f N ℬ`, the
> degree-`0` part of the localization induced from the grading `ℬ`.

```lean
theorem exists_gradedAlgebra_degZeroPart_equiv
    (R : Type uR) [CommRing R]
    (R' : Type uB) [CommRing R'] [Algebra R R'] [Algebra.FiniteType R R']
    (M : Type uM) [AddCommGroup M] [Module R' M] [Module.Finite R' M] :
    ∃ (S : Type (max uR uB)) (_ : CommRing S) (_ : Algebra R S)
      -- `𝒜` is the family of homogeneous pieces; `GradedAlgebra 𝒜` makes `S` a
      -- graded `R`-algebra graded by `ℕ = ℤ_{≥0}`.
      (𝒜 : ℕ → Submodule R S) (_ : GradedAlgebra 𝒜)
      -- `N` is an `S`-module with `ℤ`-graded homogeneous pieces `ℬ`.
      (N : Type uM) (_ : AddCommGroup N) (_ : Module S N)
      (ℬ : ℤ → AddSubgroup N) (_ : SetLike.GradedSMul 𝒜 ℬ) (_ : DirectSum.Decomposition ℬ)
      -- `f` is homogeneous of degree `1`.
      (f : S) (_ : f ∈ 𝒜 1),
      -- (2) `S₀ = R`: the structure map `R → S` is injective with range `𝒜 0`;
      -- and `S` is generated over `R` by finitely many degree-`1` elements.
      (Function.Injective (algebraMap R S) ∧
        Set.range (algebraMap R S) = (𝒜 0 : Set S)) ∧
      (∃ (gs : Finset S), (∀ g ∈ gs, g ∈ 𝒜 1) ∧
        Algebra.adjoin R (gs : Set S) = ⊤) ∧
      -- (3) `N` is a finite `S`-module.
      Module.Finite S N ∧
      -- (1) `R' ≅ S_(f)` as `R`-algebras and `M ≅ N_(f)` as modules.
      --
      -- `eR` is a ring isomorphism `R' ≃+* S_(f)`; it is an `R`-algebra
      -- isomorphism because it is compatible with the structure maps: the image
      -- of `r : R` in `R'` is sent to the image of `r` in `S_f` (which lies in the
      -- degree-`0` part `S_(f)`).  Since `S₀ = R` by (2), this is exactly the
      -- `R`-algebra compatibility `eR ∘ (R → R') = (R → S_(f))`.
      --
      -- `eM` is an additive isomorphism `M ≃+ N_(f)` to the faithfully-defined
      -- degree-`0` part `N_(f) = degZeroPart f N ℬ`.  It is semilinear over `eR`:
      -- `eM (r • m) = (eR r).val • eM m` inside `N_f`, where `S_(f)` acts via the
      -- embedding `HomogeneousLocalization.val : S_(f) → S_f`.  Together with the
      -- `R`-compatibility of `eR`, this expresses `M ≅ N_(f)` as `R' ≅ S_(f)`-modules.
      (∃ (eR : R' ≃+* HomogeneousLocalization.Away 𝒜 f)
         (eM : M ≃+ (degZeroPart f N ℬ)),
         (∀ r : R, (eR (algebraMap R R' r)).val
            = algebraMap S (Localization (Submonoid.powers f)) (algebraMap R S r)) ∧
         (∀ (r : R') (m : M),
           (eM (r • m) : LocalizedModule (Submonoid.powers f) N)
             = (eR r).val • (eM m : LocalizedModule (Submonoid.powers f) N)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.57, Tag 00JM](https://stacks.math.columbia.edu/tag/00JM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
