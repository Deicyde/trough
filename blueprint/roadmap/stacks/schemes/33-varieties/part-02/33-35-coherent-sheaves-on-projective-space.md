---
declaration: section
origin: cited
lean: Stacks.ProjectiveSpace.exists_iso_projectiveSpace_hyperplane, Stacks.ProjectiveSpace.exists_iso_projectiveSpace_hyperplaneOfSection, Stacks.AlgebraicGeometry.ProjectiveSpaceHyperplaneSection.exists_homogeneousSection_nonvanishing, Stacks.AlgebraicGeometry.ProjectiveSpaceHyperplaneSection.shortExact_hyperplaneUnit_of_nonvanishing, AlgebraicGeometry.exists_section_shortExact_hyperplaneUnit, Stacks.AlgebraicGeometry.ProjectiveSpaceSectionFiniteFamily.exists_section_forall_shortExact_coherent, Stacks.AlgebraicGeometry.HyperplaneTwistSequence.pullbackTwistModuleIso, Stacks.AlgebraicGeometry.HyperplaneTwistSequence.pushforwardTwistModuleIso
statement: formalized
proof: formalized
---

# 33.35 Coherent sheaves on projective space

Section 33.35 of the Stacks Project, [Tag 089X](https://stacks.math.columbia.edu/tag/089X). 14 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 089Z, a lemma

[Tag 089Z](https://stacks.math.columbia.edu/tag/089Z) in the Stacks Project.

**`Stacks.ProjectiveSpace.exists_iso_projectiveSpace_hyperplane`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneIsProjectiveSpace.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneIsProjectiveSpace.lean#L530). The attribute's comment: “for the hyperplane presented by a nonzero degree-one form”.

> **A hyperplane in `ℙⁿ_k` is `ℙ^{n-1}_k`, and `𝒪(1)` pulls back to `𝒪(1)`.**
>
> For a nonzero homogeneous form `l` of degree one on `ℙⁿ_k = Proj k[T₀, …, Tₙ]` with `n = m + 1`,
> there is an isomorphism `φ : ℙ^{n-1}_k ⟶ H` onto the hyperplane `H = Z(l)` under which the
> pullback of `𝒪(1)` along `φ` composed with the inclusion `i : H ⟶ ℙⁿ_k` is `𝒪(1)`.
>
> The last clause says that `φ` composed with the inclusion is a morphism **over `Spec k`**: it
> carries the structure morphism of `ℙⁿ_k` to that of `ℙ^{n-1}_k`, both written as
> `AlgebraicGeometry.Proj.toSpecZero` followed by `Spec` of the inclusion of the constants. This is
> `Stacks.ProjectiveCohomology.projModelToSpec` in the spelling of that file, unfolded here so that
> no import of it is needed; it holds because `φ.hom` composed with the inclusion *is* `Proj` of the
> graded surjection of `Stacks.ProjectiveSpace.exists_gradedHom_ker_span_degreeOne`, which is a
> `k`-algebra map. Without it the identification of the hyperplane with `ℙ^{n-1}_k` says nothing
> about `k`-vector-space dimensions of cohomology, so no Euler characteristic can be transported
> across it.

```lean
theorem exists_iso_projectiveSpace_hyperplane
    (l : MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k 1)
    (hl : (l : MvPolynomial (Fin (m + 2)) k) ≠ 0) :
    ∃ φ : AlgebraicGeometry.Proj (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k)
        ≅ (hyperplane l).subscheme,
      Nonempty ((Scheme.Modules.pullback (φ.hom ≫ (hyperplane l).subschemeι)).obj
          (twistingSheafModule (MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k) ((1 : ℕ) : ℤ))
        ≅ twistingSheafModule
            (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k) ((1 : ℕ) : ℤ)) ∧
      φ.hom ≫ (hyperplane l).subschemeι ≫
          Proj.toSpecZero (MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k) ≫
            Spec.map (CommRingCat.ofHom (algebraMap k
              ↥(MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k 0))) =
        Proj.toSpecZero (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k) ≫
          Spec.map (CommRingCat.ofHom (algebraMap k
            ↥(MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k 0)))
```

**`Stacks.ProjectiveSpace.exists_iso_projectiveSpace_hyperplaneOfSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneIsProjectiveSpace.lean, line 575](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneIsProjectiveSpace.lean#L575).

> **A hyperplane in `ℙⁿ_k` is `ℙ^{n-1}_k`, and `𝒪(1)` pulls back to `𝒪(1)`.**
>
> A hyperplane in `ℙⁿ_k = Proj k[T₀, …, Tₙ]`, with `n = m + 1`, is the zero scheme `H = Z(s)` of a
> nonzero global section `s` of `𝒪(1)`. There is an isomorphism `φ : ℙ^{n-1}_k ⟶ H` under which the
> pullback of `𝒪(1)` along `φ` composed with the inclusion `i : H ⟶ ℙⁿ_k` is `𝒪(1)`, and `φ`
> composed with that inclusion is a morphism over `Spec k`.
>
> Such an `s` is the section of a nonzero homogeneous form of degree one, by
> `Stacks.ProjectiveSpace.Cohomology.exists_degreeSection_eq`, so this is
> `Stacks.ProjectiveSpace.exists_iso_projectiveSpace_hyperplane` with the form produced from the
> section.
>
> The over-`Spec k` clause is carried because the consumers of this tag in the hyperplane
> restriction data of [Stacks, Tag 08A7] need the identification to respect the base: without it
> the pushforward along `H ⟶ ℙⁿ_k` cannot be compared with one over `Spec k`.

```lean
theorem exists_iso_projectiveSpace_hyperplaneOfSection
    (s : twistGlobalSections (MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k) 1)
    (hs : s ≠ 0) :
    ∃ φ : AlgebraicGeometry.Proj (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k)
        ≅ (hyperplaneOfSection s).subscheme,
      Nonempty ((Scheme.Modules.pullback (φ.hom ≫ (hyperplaneOfSection s).subschemeι)).obj
          (twistingSheafModule (MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k) ((1 : ℕ) : ℤ))
        ≅ twistingSheafModule
            (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k) ((1 : ℕ) : ℤ)) ∧
        φ.hom ≫ (hyperplaneOfSection s).subschemeι ≫
            Proj.toSpecZero (MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k) ≫
              Spec.map (CommRingCat.ofHom (algebraMap k
                ↥(MvPolynomial.homogeneousSubmodule (Fin (m + 2)) k 0))) =
          Proj.toSpecZero (MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k) ≫
            Spec.map (CommRingCat.ofHom (algebraMap k
              ↥(MvPolynomial.homogeneousSubmodule (Fin (m + 1)) k 0)))
```

## Tag 08A0, a lemma

[Tag 08A0](https://stacks.math.columbia.edu/tag/08A0) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHyperplaneSection.exists_homogeneousSection_nonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceHyperplaneSection.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceHyperplaneSection.lean#L106). The attribute's comment: “the choice of the hyperplane section — a nonzero `s` vanishing at no associated point of `ℱ`, which is the one step needing `k` infinite; not the exact sequence”.

> Let `k` be an infinite field and let `ℱ` be a coherent module on `ℙⁿ_k = Proj k[T₀, …, Tₙ]`.
> Then some nonzero linear form `f` gives a nonzero global section `f / 1` of `𝒪(1)` whose
> nonvanishing locus contains every associated point of `ℱ`.

```lean
theorem exists_homogeneousSection_nonvanishing [Infinite k]
    (F : (AlgebraicGeometry.Proj (polyGrading k n)).Modules) [F.IsCoherent] :
    ∃ (f : MvPolynomial (Fin (n + 1)) k) (hf : f ∈ polyGrading k n 1), f ≠ 0 ∧
      (homogeneousSection (polyGrading k n) f hf).eval (op ⊤) ≠ 0 ∧
      Stacks.Divisors.associatedPoints F ⊆
        (Stacks.SheafOfModules.nonvanishingOpen
          (X := (AlgebraicGeometry.Proj (polyGrading k n)).toRingedSpace)
          (twistingModule (polyGrading k n) 1)
          (homogeneousSection (polyGrading k n) f hf) :
            Set ↥(AlgebraicGeometry.Proj (polyGrading k n)))
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHyperplaneSection.shortExact_hyperplaneUnit_of_nonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceHyperplaneSection.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceHyperplaneSection.lean#L218). The attribute's comment: “the short exact sequence for an arbitrary coherent module”.

> Let `S` be a scheme with `ℙⁿ_S` locally Noetherian, let `ℱ` be an `𝒪`-module on `ℙⁿ_S` with
> `ℱ(-1)` and `ℱ(-1) ⊗ 𝒪(1)` quasi-coherent, and let `s` be a global section of `𝒪(1)` that does
> not vanish near any associated point of `ℱ(-1)`. Writing `i : H ⟶ ℙⁿ_S` for the hyperplane cut
> out by `s`, the sequence
>
> `0 ⟶ ℱ(-1) ⟶ ℱ ⟶ i_* i^* ℱ ⟶ 0`
>
> is short exact, the first arrow being multiplication by `s` and the second the restriction to
> `H`.

```lean
theorem shortExact_hyperplaneUnit_of_nonvanishing (S : Scheme.{u})
    [IsLocallyNoetherian (projectiveSpaceOver n S)]
    (F : (projectiveSpaceOver n S).Modules) (s : (twistOver n S 1).sections)
    [(tensorModules (projectiveSpaceOver n S) F (twistOver n S (-1))).IsQuasicoherent]
    [(tensorModules (projectiveSpaceOver n S) F (twistOver n S (-1)) ⊗
        twistOver n S 1).IsQuasicoherent]
    (hW : ∀ x ∈ Stacks.Divisors.associatedPoints
        (tensorModules (projectiveSpaceOver n S) F (twistOver n S (-1))),
      ∃ W : (projectiveSpaceOver n S).Opens, x ∈ W ∧ ∀ y ∈ W,
        y ∈ Stacks.SheafOfModules.nonvanishingLocus
          (X := (projectiveSpaceOver n S).toRingedSpace) (twistOver n S 1) s) :
    ∃ h : twistSectionMulNegOne n S F s ≫ hyperplaneUnit n S F s = 0,
      (CategoryTheory.ShortComplex.mk (twistSectionMulNegOne n S F s)
        (hyperplaneUnit n S F s) h).ShortExact
```

**`AlgebraicGeometry.exists_section_shortExact_hyperplaneUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneSequenceCoherent.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneSequenceCoherent.lean#L128).

> **[Stacks, Tag 08A0].** Let `k` be an infinite field and let `ℱ` be a coherent sheaf on
> `ℙⁿ_k`. Then there is a nonzero global section `s` of `𝒪(1)` such that, with `i : H ⟶ ℙⁿ_k` the
> hyperplane cut out by `s`, the sequence
>
> `0 ⟶ ℱ(-1) ⟶ ℱ ⟶ i_* i^* ℱ ⟶ 0`
>
> is short exact — the first arrow being multiplication by `s`
> (`…ProjectiveSpaceSectionMultiplication.twistSectionMulNegOne`) and the second the restriction
> to `H` (`…ProjectiveSpaceSectionMultiplication.hyperplaneUnit`).
>
> The section is produced by `AlgebraicGeometry.exists_form_section_nonvanishing` applied to the
> coherent module `ℱ(-1)`, which is the only step at which `k` has to be infinite, and the
> sequence is `…ProjectiveSpaceHyperplaneSection.shortExact_hyperplaneUnit_of_nonvanishing`; the
> quasi-coherence that the latter asks of `ℱ(-1)` and of `ℱ(-1) ⊗ 𝒪(1)` holds for every coherent
> `ℱ`, by [Stacks, Tag 0GQM].

```lean
theorem exists_section_shortExact_hyperplaneUnit (k : Type u) [Field k] [Infinite k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (CommRingCat.of k)).Modules) [F.IsCoherent] :
    ∃ s : (twistOver n (Spec (CommRingCat.of k)) 1).sections,
      PresheafOfModules.sections.eval s (op ⊤) ≠ 0 ∧
      ∃ w : twistSectionMulNegOne n (Spec (CommRingCat.of k)) F s ≫
          hyperplaneUnit n (Spec (CommRingCat.of k)) F s = 0,
        (ShortComplex.mk (twistSectionMulNegOne n (Spec (CommRingCat.of k)) F s)
          (hyperplaneUnit n (Spec (CommRingCat.of k)) F s) w).ShortExact
```

## Tag 08A1, a remark

[Tag 08A1](https://stacks.math.columbia.edu/tag/08A1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceSectionFiniteFamily.exists_section_forall_shortExact_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneSequenceFiniteFamily.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneSequenceFiniteFamily.lean#L116). The attribute's comment: “one section of O(1) works for a whole finite family of coherent modules”.

> **[Stacks, Tag 08A1].** Let `k` be an infinite field, let `n ≥ 1` and let `ℱ_i` be a finite
> family of coherent `𝒪`-modules on `ℙⁿ_k`. Then a single nonzero global section `s` of `𝒪(1)`
> serves all of them: with `i : H ⟶ ℙⁿ_k` the hyperplane cut out by `s`, the sequence
>
> `0 ⟶ ℱ_i(-1) ⟶ ℱ_i ⟶ i_* i^* ℱ_i ⟶ 0`
>
> of [Stacks, Tag 08A0] is short exact for every member of the family, the first arrow being
> multiplication by `s` and the second the restriction to `H`.
>
> This is the source's argument: [Stacks, Tag 08A0]
> (`AlgebraicGeometry.exists_section_shortExact_hyperplaneUnit`) is applied to the coherent module
> `⨁ ℱ_i`, and the resulting conditions descend to each summand by
> `sectionWorksFor_of_retract`.

```lean
theorem exists_section_forall_shortExact_coherent {k : Type u} [Field k] [Infinite k]
    (_hn : 1 ≤ n) {ι : Type*} [Finite ι]
    (F : ι → (projectiveSpaceOver n (Spec (CommRingCat.of k))).Modules)
    (hF : ∀ i, (F i).IsCoherent) :
    ∃ s : (twistOver n (Spec (CommRingCat.of k)) 1).sections,
      PresheafOfModules.sections.eval s (op ⊤) ≠ 0 ∧ ∀ i : ι,
      ∃ hz : twistSectionMulNegOne n (Spec (CommRingCat.of k)) (F i) s ≫
          hyperplaneUnit n (Spec (CommRingCat.of k)) (F i) s = 0,
        (ShortComplex.mk (twistSectionMulNegOne n (Spec (CommRingCat.of k)) (F i) s)
          (hyperplaneUnit n (Spec (CommRingCat.of k)) (F i) s) hz).ShortExact
```

## Tag 0EGK, a remark

[Tag 0EGK](https://stacks.math.columbia.edu/tag/0EGK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.HyperplaneTwistSequence.pullbackTwistModuleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneTwistSequence.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneTwistSequence.lean#L362). The attribute's comment: “the twist of a module restricted to the hyperplane: i^*(F(d)) = (i^*F)(d)”.

> **[Stacks, Tag 0EGK], the twist of a module restricted to the closed subscheme.**
> `i^*(ℱ(d)) ≅ (i^*ℱ)(d)`, the twist on `H` being taken with respect to `i^*L`.  This is
> [Stacks, Tag 01CD] for the tensor product followed by `pullbackTensorPowModuleIntIso` for the
> tensor power.

```lean
def pullbackTwistModuleIso (d : ℤ) :
    (Scheme.Modules.pullback i).obj (twistModule X L F d) ≅
      twistModule Hy ((Scheme.Modules.pullback i).obj L)
        ((Scheme.Modules.pullback i).obj F) d
```

**`Stacks.AlgebraicGeometry.HyperplaneTwistSequence.pushforwardTwistModuleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneTwistSequence.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/HyperplaneTwistSequence.lean#L379). The attribute's comment: “the projection formula clause: i\_*(G(d)) = i\_*G ⊗ O(d), by [Stacks, Tag 01E8] at a closed immersion”.

> **[Stacks, Tag 0EGK], the projection formula clause.**
> `i_*𝒢 ⊗_{𝒪_X} L^{⊗ d} ≅ i_*(𝒢(d))`, which is what makes the third term of the twisted sequence
> the direct image of a twist on `H`.
>
> This is [Stacks, Tag 01E8] at a closed immersion — available with no quasi-coherence hypothesis
> as `Stacks.AffineProjectionFormula.closedImmersionProjectionFormulaIso` — followed by
> `pullbackTensorPowModuleIntIso`, which rewrites `i^*(L^{⊗ d})` as `(i^*L)^{⊗ d}` so that the
> twist on `H` is taken with respect to `i^*L`.

```lean
def pushforwardTwistModuleIso (d : ℤ) :
    (tensorRightModules X (tensorPowModule X L d)).obj
        ((Scheme.Modules.pushforward i).obj G) ≅
      (Scheme.Modules.pushforward i).obj
        (twistModule Hy ((Scheme.Modules.pullback i).obj L) G d)
```

**`AlgebraicGeometry.exists_iso_pullbackTwistOver_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneTwistUnconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneTwistUnconditional.lean#L121). The attribute's comment: “the Serre twists on the hyperplane in every degree, the degree-one case being this chapter's own [Stacks, Tag 089Z] on the base-change model”.

> **[Stacks, Tag 0EGK], the Serre twists on a hyperplane of `ℙ^{m+1}_k`, in every integer
> degree.**
>
> Let `v` be a global section of `𝒪(1)` on `ℙ^{m+1}_k` corresponding to a nonzero degree-one form
> `f` on `Proj k[T₀, …, T_{m+1}]`. Then the zero scheme `H = Z(v)` admits an isomorphism
> `φ : ℙᵐ_k ≅ H` along which, for **every** `d ∈ ℤ`, the pullback of `𝒪_{ℙ^{m+1}}(d)` is
> `𝒪_{ℙᵐ}(d)`.
>
> The degree-one case is [Stacks, Tag 089Z] on the base-change model,
> `AlgebraicGeometry.exists_iso_zeroScheme_projectiveSpaceOverRing`; the passage from it to every
> degree is `Stacks.AlgebraicGeometry.HyperplaneTwistSequence.pullbackTwistOverIso`.

```lean
theorem exists_iso_pullbackTwistOver_zeroScheme (k : Type u) [Field k] (m : ℕ)
    (f : MvPolynomial (Fin (m + 2)) k) (hf : f ∈ polyGrading k (m + 1) 1) (hf0 : f ≠ 0)
    (v : Γ(twistOver (m + 1) (Spec (CommRingCat.of k)) 1, ⊤))
    (hv : ConcreteCategory.hom (twistGammaTopIso k (m + 1)).hom v
      = degreeSection (polyGrading k (m + 1)) 1 ⟨f, hf⟩) :
    ∃ φ : projectiveSpaceOverRing m (CommRingCat.of k) ≅
        (AlgebraicGeometry.zeroScheme (projectiveSpaceOverRing (m + 1) (CommRingCat.of k))
          (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) v).subscheme,
      ∀ d : ℤ, Nonempty ((Scheme.Modules.pullback (φ.hom ≫
          (AlgebraicGeometry.zeroScheme (projectiveSpaceOverRing (m + 1) (CommRingCat.of k))
            (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) v).subschemeι)).obj
        (twistOver (m + 1) (Spec (CommRingCat.of k)) d)
          ≅ twistOver m (Spec (CommRingCat.of k)) d)
```

**`AlgebraicGeometry.exists_hyperplane_twistedSequence_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneTwistUnconditional.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneTwistUnconditional.lean#L434). The attribute's comment: “the whole remark in the situation of Tags 089Z and 08A0: the hyperplane is P^m\_k with O\_H(d) = i^*O(d) in every degree, the twisted sequence 0 → F(d-1) → F(d) → i\_*(G(d)) → 0 is short exact for every d, and its long exact cohomology sequence has H^j(H, G(d)) as its third term”.

> **[Stacks, Tag 0EGK] in full.** Let `k` be an infinite field and let `ℱ` be a coherent sheaf
> on `ℙ^{m+1}_k`. Then there are a nonzero global section `s` of `𝒪(1)`, an isomorphism
> `φ : ℙᵐ_k ≅ H` of `ℙᵐ_k` with the hyperplane `H = Z(s)` and, writing `i : H ⟶ ℙ^{m+1}_k` for the
> inclusion and `𝒢 = i^*ℱ`, a short exact sequence
>
> `0 ⟶ ℱ(-1) ⟶ ℱ ⟶ i_*𝒢 ⟶ 0`
>
> such that
>
> * `𝒪_H(d) = i^*𝒪_{ℙ^{m+1}}(d)` along `φ`, for every `d ∈ ℤ`;
> * for every `d ∈ ℤ` the twisted sequence `0 ⟶ ℱ(d-1) ⟶ ℱ(d) ⟶ i_*(𝒢(d)) ⟶ 0` is short exact;
> * and for every `d ∈ ℤ` and every `j` the four-term sequence
>
>   `H^j(ℙ^{m+1}_k, ℱ(d-1)) ⟶ H^j(ℙ^{m+1}_k, ℱ(d)) ⟶ H^j(H, 𝒢(d)) ⟶ H^{j+1}(ℙ^{m+1}_k, ℱ(d-1))`
>
>   is exact at each of its three inner spots, its third term being cohomology on `H` and its
>   connecting map the canonical one of the cohomological `δ`-functor of [Stacks, Tag 071H] read
>   through the comparison of [Stacks, Tag 089W].
>
> The index is written `m + 1` rather than `n` with `1 ≤ n` so that the hyperplane is `ℙᵐ_k` with
> no truncated subtraction. The first clause is `exists_iso_pullbackTwistOver_zeroScheme`, the
> untwisted sequence is [Stacks, Tag 08A0] and the two remaining clauses are
> `Stacks.AlgebraicGeometry.HyperplaneTwistSequence.shortExact_twistedSequence` and
> `…HyperplaneTwistSequence.exact_cohomology_twistedSequence`, whose quasi-coherence input is
> `isQuasicoherent_twistModule_pullback`.

```lean
theorem exists_hyperplane_twistedSequence_cohomology (k : Type u) [Field k] [Infinite k]
    (m : ℕ) (F : (projectiveSpaceOverRing (m + 1) (CommRingCat.of k)).Modules)
    [F.IsCoherent] :
    ∃ (s : (twistOver (m + 1) (Spec (CommRingCat.of k)) 1).sections)
      (φ : projectiveSpaceOverRing m (CommRingCat.of k) ≅
        (hyperplane (m + 1) (Spec (CommRingCat.of k)) s).subscheme)
      (a : twistModule (projectiveSpaceOverRing (m + 1) (CommRingCat.of k))
          (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F (-1) ⟶ F)
      (w : a ≫ hyperplaneUnit (m + 1) (Spec (CommRingCat.of k)) F s = 0)
      (hS : (ShortComplex.mk a
        (hyperplaneUnit (m + 1) (Spec (CommRingCat.of k)) F s) w).ShortExact),
      let X := projectiveSpaceOverRing (m + 1) (CommRingCat.of k)
      let G := (Scheme.Modules.pullback
        (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)).obj F
      let g := hyperplaneUnit (m + 1) (Spec (CommRingCat.of k)) F s
      let hG := fun d : ℤ => isQuasicoherent_twistModule_pullback
        (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
        (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F (isQuasicoherent_of_isCoherent F) d
      PresheafOfModules.sections.eval s (op ⊤) ≠ 0 ∧
      (∀ d : ℤ, Nonempty ((Scheme.Modules.pullback
            (φ.hom ≫ hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)).obj
          (twistOver (m + 1) (Spec (CommRingCat.of k)) d)
            ≅ twistOver m (Spec (CommRingCat.of k)) d)) ∧
      ∀ d : ℤ,
        (twistedSequence (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
          (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w d).ShortExact ∧
        ∀ j : ℕ,
          Function.Exact (((cohomologyDeltaFunctor X).functor j).map
              (twistedSequence (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
                (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w d).f)
            (cohomologyToHyperplaneMap (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
              (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w d (hG d) j) ∧
          Function.Exact
              (cohomologyToHyperplaneMap (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
                (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w d (hG d) j)
              (cohomologyConnectingMap (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
                (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w hS d (hG d) j) ∧
          Function.Exact
              (cohomologyConnectingMap (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
                (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w hS d (hG d) j)
              (((cohomologyDeltaFunctor X).functor (j + 1)).map
                (twistedSequence (hyperplaneι (m + 1) (Spec (CommRingCat.of k)) s)
                  (twistOver (m + 1) (Spec (CommRingCat.of k)) 1) F G a g w d).f)
```

## Tag 08A3, a definition

[Tag 08A3](https://stacks.math.columbia.edu/tag/08A3) in the Stacks Project.

**`AlgebraicGeometry.IsMRegular`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/Regularity.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/Regularity.lean#L53).

> A coherent sheaf on projective `n`-space over `k` is `m`-regular if its
> cohomology in degree `i` vanishes after the twist by `m - i`, for `1 ≤ i ≤ n`.

```lean
public noncomputable abbrev IsMRegular (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] (m : ℤ) : Prop
```

## Tag 08A4, a lemma

[Tag 08A4](https://stacks.math.columbia.edu/tag/08A4) in the Stacks Project.

**`AlgebraicGeometry.isMRegular_iff_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceBaseChange/FieldExtension.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceBaseChange/FieldExtension.lean#L267).

> **[Stacks, Tag 08A4].** Let `k ⊆ K` be an extension of fields and let `ℱ` be a coherent sheaf
> on `ℙⁿ_k`. Then `ℱ` is `m`-regular if and only if its pullback to `ℙⁿ_K` is `m`-regular.

```lean
public theorem isMRegular_iff_fieldExtension (k K : Type u) [Field k] [Field K] [Algebra k K]
    (n : ℕ) (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] (m : ℤ) :
    letI : IsLocallyNoetherian (projectiveSpaceOverRing n (.of K)) :=
      projectiveSpaceOver_isLocallyNoetherian n (Spec (.of K))
    letI : ((Scheme.Modules.pullback
      (projectiveSpaceFieldExtensionMap k K n)).obj F).IsCoherent :=
      isCoherent_pullback (projectiveSpaceFieldExtensionMap k K n) F
    IsMRegular k n F m ↔
      IsMRegular K n
        ((Scheme.Modules.pullback (projectiveSpaceFieldExtensionMap k K n)).obj F) m
```

## Tag 08A5, a lemma

[Tag 08A5](https://stacks.math.columbia.edu/tag/08A5) in the Stacks Project.

**`AlgebraicGeometry.isMRegular_hyperplaneRestriction_of_nonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneRestrictionRegularity.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneRestrictionRegularity.lean#L304). The attribute's comment: “in the situation of Tag 08A0, for every nonzero section s of O(1) avoiding the associated points of F: the sequence of Tag 08A0 is short exact, H(s) ≅ P^\{n-1}\_k as in Tag 089Z, and along every such identification the restriction of an m-regular F is m-regular”.

> **[Stacks, Tag 08A5].** Let `k` be a field, `n ≥ 1`, `ℱ` a coherent sheaf on `ℙⁿ_k`, and let
> `s` be a **nonzero** global section of `𝒪(1)` vanishing at no associated point of `ℱ` — the
> hyperplane section of [Stacks, Tag 08A0], which over an infinite field always exists
> (`AlgebraicGeometry.exists_hyperplane_isMRegular_pullback`). Write `i : H ⟶ ℙⁿ_k` for its
> hyperplane and `𝒢 = i^*ℱ`. Then
>
> * the sequence `0 ⟶ ℱ(-1) ⟶ ℱ ⟶ i_*𝒢 ⟶ 0` of Tag 08A0 is short exact, its arrows being
>   multiplication by `s` and restriction to `H`;
> * `H ≅ ℙ^{n-1}_k` as in [Stacks, Tag 089Z]: there is an identification `φ : ℙ^{n-1}_k ≅ H`, over
>   `Spec k`, along which `𝒪(1)` restricts to `𝒪(1)`;
> * and, for **every** such identification `φ` (one along which `𝒪(1)` restricts to `𝒪(1)`) and
>   every `m`, if `ℱ` is `m`-regular then `𝒢` is `m`-regular on `H ≅ ℙ^{n-1}_k`, that is
>   `φ^*𝒢 = (φ ≫ i)^*ℱ` is `m`-regular on `ℙ^{n-1}_k`.
>
> The identification of Tag 089Z is not unique — it depends on a choice of coordinates on the
> hyperplane — so the regularity is asserted for all of them rather than for one. The field need
> not be infinite once `s` is given: that hypothesis of Tag 08A0 is used only to choose `s`.
>
> The sequence is `…ProjectiveSpaceHyperplaneSection.shortExact_hyperplaneUnit_of_nonvanishing`;
> the identification is `AlgebraicGeometry.exists_iso_zeroScheme_projectiveSpaceOverRing` applied
> to the degree-one form presenting
> `s` (`Stacks.ProjectiveSpace.Cohomology.exists_degreeSection_eq`); the regularity is
> `AlgebraicGeometry.isMRegular_pullback_hyperplaneι_of_nonvanishing`.

```lean
theorem isMRegular_hyperplaneRestriction_of_nonvanishing (k : Type u) [Field k] (n : ℕ)
    (hn : 1 ≤ n) (F : (projectiveSpaceOverRing n (CommRingCat.of k)).Modules) [F.IsCoherent]
    (s : (twistOver n (Spec (CommRingCat.of k)) 1).sections)
    (hs0 : PresheafOfModules.sections.eval s (op ⊤) ≠ 0)
    (hs : Stacks.Divisors.associatedPoints F ⊆
      Stacks.SheafOfModules.nonvanishingLocus (twistOver n (Spec (CommRingCat.of k)) 1) s) :
    (∃ w : twistSectionMulNegOne n (Spec (CommRingCat.of k)) F s ≫
          hyperplaneUnit n (Spec (CommRingCat.of k)) F s = 0,
        (ShortComplex.mk (twistSectionMulNegOne n (Spec (CommRingCat.of k)) F s)
          (hyperplaneUnit n (Spec (CommRingCat.of k)) F s) w).ShortExact) ∧
      (∃ φ : projectiveSpaceOverRing (n - 1) (CommRingCat.of k) ≅
          (hyperplane n (Spec (CommRingCat.of k)) s).subscheme,
        Nonempty ((Scheme.Modules.pullback
            (φ.hom ≫ hyperplaneι n (Spec (CommRingCat.of k)) s)).obj
              (twistOver n (Spec (CommRingCat.of k)) 1) ≅
            twistOver (n - 1) (Spec (CommRingCat.of k)) 1) ∧
          φ.hom ≫ hyperplaneι n (Spec (CommRingCat.of k)) s ≫
              (projectiveSpaceOverRing n (CommRingCat.of k) ↘ Spec (CommRingCat.of k)) =
            projectiveSpaceOverRing (n - 1) (CommRingCat.of k) ↘ Spec (CommRingCat.of k)) ∧
      ∀ φ : projectiveSpaceOverRing (n - 1) (CommRingCat.of k) ≅
          (hyperplane n (Spec (CommRingCat.of k)) s).subscheme,
        Nonempty ((Scheme.Modules.pullback
            (φ.hom ≫ hyperplaneι n (Spec (CommRingCat.of k)) s)).obj
              (twistOver n (Spec (CommRingCat.of k)) 1) ≅
            twistOver (n - 1) (Spec (CommRingCat.of k)) 1) →
        ∀ m : ℤ, IsMRegular k n F m →
          haveI := projectiveSpaceOver_isLocallyNoetherian (n - 1) (Spec (CommRingCat.of k))
          haveI := isCoherent_pullback (φ.hom ≫ hyperplaneι n (Spec (CommRingCat.of k)) s) F
          IsMRegular k (n - 1)
            ((Scheme.Modules.pullback
              (φ.hom ≫ hyperplaneι n (Spec (CommRingCat.of k)) s)).obj F) m
```

## Tag 08A6, a lemma

[Tag 08A6](https://stacks.math.columbia.edu/tag/08A6) in the Stacks Project.

**`AlgebraicGeometry.isMRegular_add_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneRegularity.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/HyperplaneRegularity.lean#L276). The attribute's comment: “an m-regular coherent sheaf on projective space is (m+1)-regular”.

> **[Stacks, Tag 08A6].** Let `k` be a field, let `n ≥ 0` and let `ℱ` be a coherent sheaf on
> `ℙⁿ_k`. If `ℱ` is `m`-regular then `ℱ` is `(m + 1)`-regular.
>
> The argument is an induction on `n`, vacuous for `n = 0`. Passing to `k(t)`, which is infinite,
> changes nothing by [Stacks, Tag 08A4]; there a hyperplane `j : ℙ^{n-1} ⟶ ℙⁿ` is available, the
> restriction `𝒢` of `ℱ` to it is `m`-regular by [Stacks, Tag 08A5] and hence `(m+1)`-regular by
> induction, and the segment
> `H^i(ℙⁿ, ℱ(m-i)) ⟶ H^i(ℙⁿ, ℱ(m+1-i)) ⟶ H^i(ℙ^{n-1}, 𝒢(m+1-i))` of the long exact sequence has
> both ends zero — the right one by `(m+1)`-regularity of `𝒢` for `i ≤ n-1`, and by vanishing
> above the dimension for `i = n`.

```lean
public theorem isMRegular_add_one
    (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] (m : ℤ)
    (hF : IsMRegular k n F m) :
    IsMRegular k n F (m + 1)
```

## Tag 08A7, a lemma

[Tag 08A7](https://stacks.math.columbia.edu/tag/08A7) in the Stacks Project.

**`AlgebraicGeometry.span_mulSections_eq_top_of_isMRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularitySectionMultiplication.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularitySectionMultiplication.lean#L386). The attribute's comment: “for an arbitrary field, with the hyperplane restriction data of Tags 08A0, 0EGK and 089Z carried in `HyperplaneRestrictionPackage`; the induction on `n`, the base case and the use of `m`-regularity to lift a section off the hyperplane are proved. Over an infinite field every clause of that package but `liftSection` is proved too -- see `AlgebraicGeometry.exists_hyperplaneRestrictionData`. Surjectivity out of the tensor product is stated as the `k`-span of the products being `⊤`.”.

> **[Stacks, Tag 08A7].** Let `k` be a field, `n ≥ 0` and `ℱ` a coherent sheaf on `ℙⁿ_k`. If
> `ℱ` is `m`-regular then the multiplication map
>
> `H⁰(ℙⁿ_k, ℱ(m)) ⊗_k H⁰(ℙⁿ_k, 𝒪(1)) ⟶ H⁰(ℙⁿ_k, ℱ(m+1))`
>
> is surjective — equivalently, the `k`-span of the products is everything.
>
> The proof is the source's induction on `n`. For `n = 0` multiplication by a generator of the
> trivial sheaf `𝒪(1)` is already an isomorphism. For the step, the inductive hypothesis writes the
> restriction of a class `t ∈ H⁰(ℱ(m+1))` to the hyperplane as a combination of products
> `σ · g`; each `g` lifts to `ℙ^{n+1}_k` because `m`-regularity makes `H¹(ℱ(m-1))` vanish, each `σ`
> lifts by [Stacks, Tag 089Z], and subtracting the lifted combination leaves a class restricting to
> zero, which by exactness of the restriction sequence is `s` times a class in `H⁰(ℱ(m))`.

```lean
theorem span_mulSections_eq_top_of_isMRegular (k : Type u) [Field k]
    (pkg : ∀ (n : ℕ) (F : (projectiveSpaceOverRing (n + 1) (.of k)).Modules),
      F.IsCoherent → Nonempty (HyperplaneRestrictionPackage k n F)) :
    ∀ (n : ℕ) (F : (projectiveSpaceOverRing n (.of k)).Modules) (hFc : F.IsCoherent) (m : ℤ),
      @IsMRegular k _ n F hFc m → mulSectionsSpan k n F m = ⊤
```

**`AlgebraicGeometry.span_mulSections_eq_top_of_isMRegular_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularitySectionMultiplicationArbitraryField.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularitySectionMultiplicationArbitraryField.lean#L65). References: SGA 6 XIII (1.3), “(ii), special case”.

> **[Stacks, Tag 08A7] over an arbitrary field.** Let `k` be a field, `n ≥ 0`, and let `ℱ` be a
> coherent sheaf on `ℙⁿ_k` which is `m`-regular. Then the `k`-span of the products of global
> sections of `ℱ(m)` with global sections of `𝒪(1)` is all of `H⁰(ℙⁿ_k, ℱ(m+1))`, i.e. the
> multiplication map out of `H⁰(ℱ(m)) ⊗_k H⁰(𝒪(1))` is surjective.
>
> `AlgebraicGeometry.span_mulSections_eq_top_of_isMRegular` proves this from the hyperplane
> restriction data of [Stacks, Tag 08A7], which
> `AlgebraicGeometry.nonempty_hyperplaneRestrictionPackage` supplies over an infinite field;
> `AlgebraicGeometry.span_mulSections_eq_top_of_isMRegular_of_infinite` is the source's reduction to
> that case.
>
> Surjectivity of a `k`-bilinear multiplication out of a tensor product is the same statement as the
> span of the products being everything — the image of the induced linear map on
> `H⁰(ℱ(m)) ⊗_k H⁰(𝒪(1))` is generated by the images of the pure tensors — so the conclusion below
> is the source's, not a weakening of it. The field is arbitrary, as in the source: `[Infinite k]`
> appears only inside the proof.

```lean
theorem span_mulSections_eq_top_of_isMRegular_field (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] (m : ℤ)
    (hF : IsMRegular k n F m) :
    mulSectionsSpan k n F m = ⊤
```

## Tag 08A8, a lemma

[Tag 08A8](https://stacks.math.columbia.edu/tag/08A8) in the Stacks Project.

**`AlgebraicGeometry.isGeneratedByGlobalSections_projectiveTwist_of_isMRegular_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularityGlobalGenerationUnconditional.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/RegularityGlobalGenerationUnconditional.lean#L97). The attribute's comment: “an m-regular coherent sheaf on projective space over a field is globally generated after the twist by m. Everything the source's proof uses is proved: that `ℱ(d)` is globally generated for all `d ≫ 0` is `Stacks.ProjectiveSpace.exists_isGeneratedByGlobalSections_projectiveTwist_of_isCoherent`, clause (7) of Tag 01Q3 read through the comparison of `projectiveTwist` with the tensor powers of the hyperplane sheaf; the surjectivity of the multiplication map on global sections is Tag 08A7 over an arbitrary field, `AlgebraicGeometry.span_mulSections_eq_top_of_isMRegular_field`; and the regularity at each twist the descent passes through is Tag 08A6, `AlgebraicGeometry.isMRegular_add_one`. The descent is organized as a sequence of single-twist steps rather than the source's one-shot use of degree-`d-m` forms, so that only the degree-one multiplication of Tag 08A7 is needed. Globally generated is `SheafOfModules.IsGeneratedByGlobalSections`, Stacks 03DE (3).”. References: SGA 6 XIII (1.3), “(iii), special case”.

> Let `k` be a field, let `n ≥ 0`, and let `ℱ` be a coherent sheaf on `ℙⁿ_k`. If `ℱ` is
> `m`-regular then `ℱ(m)` is globally generated.

```lean
theorem isGeneratedByGlobalSections_projectiveTwist_of_isMRegular_field (k : Type u) [Field k]
    (n : ℕ) (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] (m : ℤ)
    (hF : IsMRegular k n F m) :
    SheafOfModules.IsGeneratedByGlobalSections (projectiveTwist n F m)
```

## Tag 08AC, a lemma

[Tag 08AC](https://stacks.math.columbia.edu/tag/08AC) in the Stacks Project.

**`AlgebraicGeometry.exists_polynomial_eval_eq_hilbertPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialFiniteDetermination.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialFiniteDetermination.lean#L234).

> **[Stacks, Tag 08AC].** Let `k` be a field, let `n ≥ 0` and let `ℱ` be a coherent sheaf on
> `ℙⁿ_k`. Then the function `d ↦ χ(ℙⁿ_k, ℱ(d))` is a polynomial: there is a `P ∈ ℚ[X]` with
> `χ(ℙⁿ_k, ℱ(d)) = P(d)` for **every** `d ∈ ℤ`. **No hypothesis.**
>
> The `n`-th backward difference of the Hilbert polynomial is constant
> (`AlgebraicGeometry.isDifferenceBounded_hilbertPolynomial`, the source's induction on `n`), and a
> function on `ℤ` with a constant iterated backward difference is a polynomial at every integer
> (`exists_polynomial_of_isDifferenceBounded`, the every-integer form of [Stacks, Tag 00JZ] the
> source's proof ends with).
>
> The weaker eventual reading of "is a polynomial", [Stacks, Tag 00JX]'s `IsNumericalPolynomial`,
> is `AlgebraicGeometry.isNumericalPolynomial_hilbertPolynomial'`.

```lean
theorem exists_polynomial_eval_eq_hilbertPolynomial (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] :
    ∃ P : Polynomial ℚ, ∀ d : ℤ, (hilbertPolynomial k n F d : ℚ) = P.eval (d : ℚ)
```

**`AlgebraicGeometry.isNumericalPolynomial_hilbertPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialNumerical.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialNumerical.lean#L369). The attribute's comment: “the induction on n of the source's proof together with its base case, the triviality of the twists on P^0; its one geometric input is the hypothesis hstep, the hyperplane difference formula of Stacks 0EGK, 08A0, 089Z and 08AA, which is discharged by AlgebraicGeometry.exists\_coherent\_hilbertPolynomial\_sub\_eq”.

> **[Stacks, Tag 08AC], granted the hyperplane difference formula.** For a field `k`, an
> integer `n ≥ 0` and a coherent sheaf `ℱ` on `ℙⁿ_k`, the function `d ↦ χ(ℙⁿ_k, ℱ(d))` is a
> numerical polynomial.
>
> The one hypothesis is the geometric fact the source's inductive step consumes, for the given
> field: for a coherent sheaf on `ℙ^{m+1}_k` there is a coherent sheaf on `ℙ^m_k` whose Hilbert
> polynomial is the first difference of the given one — the displayed equation of the source's
> proof, read through the identification of the hyperplane with `ℙ^m_k`. Everything else is proved:
> the base case is constant because the twists on `ℙ⁰_k` are trivial
> (`AlgebraicGeometry.projectiveTwistZeroIso`), the induction on `n` is carried out, and
> [Stacks, Tag 00JZ] in the form `main_00JZ` turns each difference back into the function.
>
> `hstep` is itself a theorem, `AlgebraicGeometry.exists_coherent_hilbertPolynomial_sub_eq`; the
> hypothesis-free form of the tag is
> `AlgebraicGeometry.isNumericalPolynomial_hilbertPolynomial'`.

```lean
public theorem isNumericalPolynomial_hilbertPolynomial
    (hstep : ∀ (m : ℕ) (G : (projectiveSpaceOverRing (m + 1) (.of k)).Modules)
      (_ : G.IsCoherent), ∃ (H : (projectiveSpaceOverRing m (.of k)).Modules)
        (hH : H.IsCoherent), ∀ d : ℤ,
          hilbertPolynomial k (m + 1) G d - hilbertPolynomial k (m + 1) G (d - 1) =
            @hilbertPolynomial k _ m H hH d)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] :
    IsNumericalPolynomial (hilbertPolynomial k n F)
```

**`AlgebraicGeometry.isNumericalPolynomial_hilbertPolynomial'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialPolynomial.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomialPolynomial.lean#L243). The attribute's comment: “the conclusion in the eventual reading of Tag 00JX: the Hilbert polynomial agrees with a sum of binomial coefficients for d >> 0; the tag's own every-integer reading is AlgebraicGeometry.exists\_polynomial\_eval\_eq\_hilbertPolynomial”.

> **[Stacks, Tag 08AC] in its eventual reading.** For a field `k`, an integer `n ≥ 0` and a
> coherent sheaf `ℱ` on `ℙⁿ_k`, the function `d ↦ χ(ℙⁿ_k, ℱ(d))` is a numerical polynomial.
> **No hypothesis.**
>
> The source reduces to an infinite base field by [Stacks, Tag 08AB], and so does this proof: the
> extension is `RatFunc k`, the Hilbert polynomial is unchanged by it
> (`AlgebraicGeometry.hilbertPolynomial_pullback_fieldExtension`), and over an infinite field the
> statement is `AlgebraicGeometry.isNumericalPolynomial_hilbertPolynomial_of_infinite`.
>
> `IsNumericalPolynomial` is [Stacks, Tag 00JX]'s notion, which constrains the function only for
> `d ≫ 0`. The tag as stated — a polynomial identity at every `d ∈ ℤ` — is
> `AlgebraicGeometry.exists_polynomial_eval_eq_hilbertPolynomial`.

```lean
public theorem isNumericalPolynomial_hilbertPolynomial' (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (CommRingCat.of k)).Modules) [F.IsCoherent] :
    IsNumericalPolynomial (hilbertPolynomial k n F)
```

## Tag 08AD, a definition

[Tag 08AD](https://stacks.math.columbia.edu/tag/08AD) in the Stacks Project.

**`AlgebraicGeometry.hilbertPolynomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomial.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/HilbertPolynomial.lean#L43). References: SGA 6 XIII (6.1), “partial”.

> The Hilbert polynomial, viewed as an integer-valued function of the twist
> degree, of a coherent sheaf on projective space over a field.

```lean
noncomputable def hilbertPolynomial (k : Type u) [Field k] (n : ℕ)
    (F : (projectiveSpaceOverRing n (.of k)).Modules) [F.IsCoherent] : ℤ → ℤ
```

## Tag 08AE, a lemma

[Tag 08AE](https://stacks.math.columbia.edu/tag/08AE) in the Stacks Project.

**`Stacks.ProjectiveSpace.Cohomology.exists_eval_eq_finrank_cohomologyOverField_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/HilbertPolynomial.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/HilbertPolynomial.lean#L126).

> **[Stacks, Tag 08AE].** Let `k` be a field, let `n ≥ 0`, let `ℱ` be a coherent sheaf on
> `ℙⁿ_k = Proj k[T₀, …, Tₙ]` and let `P ∈ ℚ[t]` be its Hilbert polynomial, that is, a polynomial
> agreeing at every integer `d` with the Euler characteristic `χ(ℙⁿ_k, ℱ(d))` of the `d`-th twist.
> Then
>
> `P(d) = dim_k H⁰(ℙⁿ_k, ℱ(d))`
>
> for all `d` large enough.
>
> The proof is the source's one sentence: the higher cohomology of a high enough twist vanishes
> ([Stacks, Tag 01YS] clause (4),
> `Stacks.ProjectiveSpace.SerreVanishing.exists_isZero_Hgroup_twist_of_isCoherent`), so the
> alternating sum defining the Euler characteristic collapses to its degree-zero term. The
> hypothesis `hP` is the definition of the Hilbert polynomial, [Stacks, Tag 08AD]; see the module
> docstring for why it is written out here rather than cited as
> `AlgebraicGeometry.hilbertPolynomial`.

```lean
public theorem exists_eval_eq_finrank_cohomologyOverField_zero (k : Type u) [Field k] (n : ℕ)
    (F : (AlgebraicGeometry.Proj (polyGrading k n)).Modules)
    (hF : _root_.SheafOfModules.IsCoherent F) (P : Polynomial ℚ)
    (hP : ∀ d : ℤ, P.eval (d : ℚ) = (((∑ᶠ i : ℕ, (-1 : ℤ) ^ i *
      (Module.finrank k (cohomologyOverField k (projModelToSpec k n)
        (twistSheafOfModules (polyGrading k n) F d) i) : ℤ) : ℤ)) : ℚ)) :
    ∃ d₀ : ℤ, ∀ d : ℤ, d₀ ≤ d →
      P.eval (d : ℚ) = (Module.finrank k (cohomologyOverField k (projModelToSpec k n)
        (twistSheafOfModules (polyGrading k n) F d) 0) : ℚ)
```

## Tag 08AG, a lemma

[Tag 08AG](https://stacks.math.columbia.edu/tag/08AG) in the Stacks Project.

**`AlgebraicGeometry.exists_isMRegular_kernel_free_of_hilbertPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/KernelRegularityInduction.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Projective/KernelRegularityInduction.lean#L273). The attribute's comment: “with the free sheaf of the source, the short exact sequence read as an epimorphism from it, and the Hilbert polynomial of Tag 08AD compared with a rational polynomial at every integer”.

> **[Stacks, Tag 08AG].** Let `n ≥ 0`, `r ≥ 1` and `P ∈ ℚ[t]`. There is a single integer `m`
> such that for **every** field `k`, every coherent sheaf `𝒬` on `ℙⁿ_k` with Hilbert polynomial `P`
> and every epimorphism `q : 𝒪^{⊕r} ⟶ 𝒬`, the kernel of `q` is `m`-regular.
>
> The quantifier order is the statement: `m` is produced from `n`, `r` and `P` alone, before the
> field and before the sequence.
>
> Over an infinite field this is
> `AlgebraicGeometry.exists_isMRegular_kernel_free_of_hilbertPolynomial_of_infinite`, the source's
> induction on the dimension. An arbitrary field is reduced to that case by base change to the
> rational function field `k(t)`, which is infinite (`AlgebraicGeometry.infinite_ratFunc`):
> `ℙⁿ_{k(t)} ⟶ ℙⁿ_k` is flat, so the kernel sequence base-changes to the kernel sequence of a
> surjection of `𝒪^{⊕r}` onto the base change of `𝒬`; the Hilbert polynomial is unchanged
> ([Stacks, Tag 08AB], `AlgebraicGeometry.hilbertPolynomial_pullback_fieldExtension`); and
> `m`-regularity descends along the extension by [Stacks, Tag 08A4],
> `AlgebraicGeometry.isMRegular_iff_fieldExtension`.

```lean
theorem exists_isMRegular_kernel_free_of_hilbertPolynomial (n r : ℕ) (hr : 1 ≤ r)
    (P : Polynomial ℚ) :
    ∃ m : ℤ, ∀ (k : Type u) [Field k]
      (Q : (projectiveSpaceOverRing n (.of k)).Modules) [Q.IsCoherent]
      (q : freeModules k n r ⟶ Q) [Epi q],
      (∀ d : ℤ, (hilbertPolynomial k n Q d : ℚ) = P.eval (d : ℚ)) →
      @IsMRegular k _ n (kernel q) (CoherentAbelian.isCoherent_kernel q) m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.35, Tag 089X](https://stacks.math.columbia.edu/tag/089X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
