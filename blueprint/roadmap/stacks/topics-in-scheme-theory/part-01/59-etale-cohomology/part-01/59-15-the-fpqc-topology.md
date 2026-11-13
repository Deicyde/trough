---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.fpqcPrecoverage, AlgebraicGeometry.QuasiCompactCover, AlgebraicGeometry.QuasiCompactCover.exists_isAffineOpen_of_isCompact, AlgebraicGeometry.singleton_specMap_mem_fpqcPrecoverage_iff_faithfullyFlat, AlgebraicGeometry.presieve₀_affinePlanePowerSeriesCover_mem_fpqcPrecoverage, AlgebraicGeometry.presieve₀_affinePlaneLocalRingCover_mem_fpqcPrecoverage, AlgebraicGeometry.flat_sigmaFromSpecStalk, AlgebraicGeometry.surjective_sigmaFromSpecStalk
statement: formalized
proof: formalized
---

# 59.15 The fpqc topology

Section 59.15 of the Stacks Project, [Tag 03NV](https://stacks.math.columbia.edu/tag/03NV). 8 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03NW, a definition

[Tag 03NW](https://stacks.math.columbia.edu/tag/03NW) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L306) (StacksFrontier): “fpqc coverings”. References: SGA 3 IV (4.7); SGA 4 VII (4.2); SGA 4 XVII (0.10), “partial”.
- [`AlgebraicGeometry.QuasiCompactCover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompactCover#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L307) (StacksFrontier): “condition (2)”.
- [`AlgebraicGeometry.QuasiCompactCover.exists_isAffineOpen_of_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompactCover.exists_isAffineOpen_of_isCompact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L308) (StacksFrontier): “condition (2) with affine opens”. References: EGA IV (1.8.1), “more general”.

## Tag 03NY, an example

[Tag 03NY](https://stacks.math.columbia.edu/tag/03NY) in the Stacks Project.

**`AlgebraicGeometry.singleton_specMap_mem_fpqcPrecoverage_iff_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean#L63). The attribute's comment: “affine\_singleton”.

> **Stacks Project, Tag 03NY.** The singleton family of affine schemes induced by a
> ring homomorphism is an fpqc covering if and only if the homomorphism is faithfully flat.

```lean
public theorem singleton_specMap_mem_fpqcPrecoverage_iff_faithfullyFlat
    {A B : Type u} [CommRing A] [CommRing B] (f : A →+* B) :
    Presieve.singleton (Spec.map (CommRingCat.ofHom f)) ∈
      Scheme.fpqcPrecoverage (Spec (.of A)) ↔ f.FaithfullyFlat
```

**`AlgebraicGeometry.presieve₀_affinePlanePowerSeriesCover_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Examples.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Examples.lean#L169). The attribute's comment: “power\_series\_covering”.

> **Stacks Project, Tag 03NY.** The family `\{D(x) ⟶ 𝐀²\_k, D(y) ⟶ 𝐀²\_k,
> Spec k[[x, y]] ⟶ 𝐀²\_k}` is an fpqc covering of the affine plane.

```lean
theorem presieve₀_affinePlanePowerSeriesCover_mem_fpqcPrecoverage :
    (affinePlaneCover k ⟨Spec (CommRingCat.of (MvPowerSeries (Fin 2) k)),
        Spec.map (CommRingCat.ofHom
          (algebraMap (MvPolynomial (Fin 2) k) (MvPowerSeries (Fin 2) k)))⟩).presieve₀ ∈
      Scheme.fpqcPrecoverage (Spec (CommRingCat.of (MvPolynomial (Fin 2) k)))
```

**`AlgebraicGeometry.presieve₀_affinePlaneLocalRingCover_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Examples.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Examples.lean#L191). The attribute's comment: “local\_ring\_covering”.

> **Stacks Project, Tag 03NY.** The family `\{D(x) ⟶ 𝐀²\_k, D(y) ⟶ 𝐀²\_k,
> Spec 𝒪\_\{𝐀²\_k, 0} ⟶ 𝐀²\_k}` is an fpqc covering of the affine plane.

```lean
theorem presieve₀_affinePlaneLocalRingCover_mem_fpqcPrecoverage :
    (affinePlaneCover k
        ⟨Spec ((Spec (CommRingCat.of (MvPolynomial (Fin 2) k))).presheaf.stalk
            (affineOrigin k 2)),
          (Spec (CommRingCat.of (MvPolynomial (Fin 2) k))).fromSpecStalk
            (affineOrigin k 2)⟩).presieve₀ ∈
      Scheme.fpqcPrecoverage (Spec (CommRingCat.of (MvPolynomial (Fin 2) k)))
```

**`AlgebraicGeometry.flat_sigmaFromSpecStalk`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean#L63). The attribute's comment: “local\_spectra\_counterexample”.

> `∐_{x ∈ X} Spec 𝒪_{X, x} ⟶ X` is flat, since each `Spec 𝒪_{X, x} ⟶ X` is.

```lean
instance flat_sigmaFromSpecStalk (X : Scheme.{u}) : Flat (sigmaFromSpecStalk X)
```

**`AlgebraicGeometry.surjective_sigmaFromSpecStalk`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean#L70). The attribute's comment: “local\_spectra\_counterexample”.

> `∐_{x ∈ X} Spec 𝒪_{X, x} ⟶ X` is surjective, since `x` is in the image of the component
> at `x`.

```lean
instance surjective_sigmaFromSpecStalk (X : Scheme.{u}) : Surjective (sigmaFromSpecStalk X)
```

**`AlgebraicGeometry.flat_and_surjective_sigmaFromSpecStalk_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean#L99). The attribute's comment: “local\_spectra\_counterexample”.

> **Stacks Project, Tag 03NY.** The morphism `φ : ∐_{x ∈ 𝐀¹_k} Spec 𝒪_{𝐀¹_k, x} ⟶ 𝐀¹_k`,
> where `k` is a field, is flat and surjective. This is the positive half of the example; the
> morphism is nevertheless not quasi-compact and `{φ}` is not an fpqc covering.

```lean
theorem flat_and_surjective_sigmaFromSpecStalk_polynomial :
    Flat (sigmaFromSpecStalk (Spec (.of (Polynomial k)))) ∧
      Surjective (sigmaFromSpecStalk (Spec (.of (Polynomial k))))
```

**`AlgebraicGeometry.singleton_sigmaFromSpecStalk_notMem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean#L179). The attribute's comment: “local\_spectra\_counterexample”.

> **Stacks Project, Tag 03NY.** Over the affine line, the family consisting of the single
> morphism `∐_{x ∈ 𝐀¹_k} Spec 𝒪_{𝐀¹_k, x} ⟶ 𝐀¹_k` is not an fpqc covering, although that
> morphism is flat and surjective.

```lean
theorem singleton_sigmaFromSpecStalk_notMem_fpqcPrecoverage :
    Presieve.singleton (sigmaFromSpecStalk (Spec (.of (Polynomial k)))) ∉
      Scheme.fpqcPrecoverage (Spec (.of (Polynomial k)))
```

**`AlgebraicGeometry.not_quasiCompact_sigmaFromSpecStalk_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/NotFpqc.lean#L211). The attribute's comment: “local\_spectra\_counterexample”.

> **Stacks Project, Tag 03NY.** The morphism `∐_{x ∈ 𝐀¹_k} Spec 𝒪_{𝐀¹_k, x} ⟶ 𝐀¹_k` is not
> quasi-compact: it is flat and surjective, so a quasi-compact such morphism would give an fpqc
> covering.

```lean
theorem not_quasiCompact_sigmaFromSpecStalk_polynomial :
    ¬ QuasiCompact (sigmaFromSpecStalk (Spec (.of (Polynomial k))))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.zariskiPrecoverage_le_fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.zariskiPrecoverage_le_fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean#L42) (StacksFrontier): “zariski\_coverings”. References: SGA 4 VII (4.2), “partial”.
- [`AlgebraicGeometry.Scheme.Hom.singleton_mem_fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.singleton_mem_fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Basic.lean#L46) (StacksFrontier): “qc\_flat\_surjective”. References: SGA 3 III (3.3), “quasi-compact branch”; SGA 3 IV (6.3.2), “partial”; SGA 3 VIIA (8.1.4), “Converse clause”; SGA 3 XI (6.8), “Fpqc covering step”; SGA 4 VII (4.2), “partial”; SGA 4½ Arcata (1.6.4), “special case”.

## Tag 03NZ, a lemma

[Tag 03NZ](https://stacks.math.columbia.edu/tag/03NZ) in the Stacks Project.

Declarations registered for the tag:

- [`Scheme.fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L45) (StacksFrontier): “the collection of fpqc coverings, whose site axioms are its Precoverage.HasIsos, Precoverage.IsStableUnderBaseChange and Precoverage.IsStableUnderComposition instances”.

## Tag 03O1, a lemma

[Tag 03O1](https://stacks.math.columbia.edu/tag/03O1) in the Stacks Project.

**`Stacks.EtaleCohomology.isSheaf_fpqc_iff_zariski_and_affine_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/SheafCriterion.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/SheafCriterion.lean#L403). References: SGA 3 IV (6.3.1), “(ii) fpqc only”.

> **Stacks Project, Tag 03O1.** A presheaf on schemes over `S` is an fpqc
> sheaf if and only if it is a Zariski sheaf and satisfies the singleton sheaf
> condition for faithfully flat morphisms between affine schemes over `S`.

```lean
public theorem isSheaf_fpqc_iff_zariski_and_affine_singleton
    (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F ↔
      (Presheaf.IsSheaf (Scheme.zariskiTopology.over S) F ∧
        ∀ {R T : CommRingCat.{u}} (f : R ⟶ T) (g : Spec R ⟶ S)
          [Flat (Spec.map f)] [Surjective (Spec.map f)],
          Presieve.IsSheafFor F
            (.singleton (Over.homMk (Spec.map f) rfl :
              Over.mk (Spec.map f ≫ g) ⟶ Over.mk g)))
```

## Tag 03O2, an example

[Tag 03O2](https://stacks.math.columbia.edu/tag/03O2) in the Stacks Project.

**`AlgebraicGeometry.relativeDifferentialsPresheaf_not_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Differentials.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/Differentials.lean#L242). The attribute's comment: “not\_fpqc\_sheaf”.

> **Stacks Project, Tag 03O2.** The presheaf on schemes over `Spec (ZMod p)` sending a scheme
> to the global sections of its sheaf of relative differentials is not a sheaf for the fpqc
> topology.

```lean
theorem relativeDifferentialsPresheaf_not_isSheaf_fpqc (p : ℕ) [Fact p.Prime] :
    ¬ Presheaf.IsSheaf (Scheme.fpqcTopology.over (Spec (.of (ZMod p))))
      (relativeDifferentialsPresheaf (Spec (.of (ZMod p)))).functor
```

**`AlgebraicGeometry.relativeDifferentialsPresheaf_isSheaf_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiDifferentialsSheaf.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiDifferentialsSheaf.lean#L325). The attribute's comment: “zariski\_sheaf”.

> The presheaf on schemes over `S` sending a scheme to the global sections of its sheaf of
> relative differentials is a sheaf for the Zariski topology.

```lean
theorem relativeDifferentialsPresheaf_isSheaf_zariski (S : Scheme.{u}) :
    Presheaf.IsSheaf (Scheme.zariskiTopology.{u}.over S)
      (relativeDifferentialsPresheaf S).functor
```

## Tag 03O3, a lemma

[Tag 03O3](https://stacks.math.columbia.edu/tag/03O3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.instSubcanonicalFpqcTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instSubcanonicalFpqcTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L311) (StacksFrontier): “on the category of all schemes”. References: SGA 1 VIII (5.2), “more general”; SGA 3 IV (4.7), “special case”; SGA 3 IV (6.1.1), “more general”; SGA 3 IV (6.3.1), “more general”; SGA 3 VIII (1.7.1), “special case”; SGA 3 XV (8.10), “(i)”; SGA 4 VII (4.2), “special case”; SGA 7 VII (1.3.8), “special case”.
- [`CategoryTheory.GrothendieckTopology.subcanonical_over`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.subcanonical_over#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L313) (StacksFrontier): “passage to Sch/S”. References: SGA 3 IV (4.5.3).

## Tag 03O4, a remark

[Tag 03O4](https://stacks.math.columbia.edu/tag/03O4) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_smallEtale_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean#L109). The attribute's comment: “representables on the small étale site”.

> **Stacks 03O4.** A representable presheaf on the small étale site of a scheme is a
> sheaf.

```lean
public theorem isSheaf_smallEtale_of_isRepresentable (S : Scheme.{u})
    (F : (S.Etale)ᵒᵖ ⥤ Type v) [F.IsRepresentable] :
    Presheaf.IsSheaf (Scheme.smallEtaleTopology S) F
```

**`AlgebraicGeometry.isSheaf_bigEtale_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean#L119). The attribute's comment: “representables on the big étale site”.

> **Stacks 03O4.** A representable presheaf on the big étale site over a scheme is a
> sheaf.

```lean
public theorem isSheaf_bigEtale_of_isRepresentable (S : Scheme.{u})
    (F : (Over S)ᵒᵖ ⥤ Type v) [F.IsRepresentable] :
    Presheaf.IsSheaf (Scheme.etaleTopology.over S) F
```

**`AlgebraicGeometry.isSheaf_smallEtale_of_isRepresentable_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/RepresentableSheaves.lean#L129). The attribute's comment: “big representables on the small étale site”.

> **Stacks 03O4.** A representable presheaf on the schemes over `S` restricts to a sheaf on
> the small étale site of `S`.

```lean
public theorem isSheaf_smallEtale_of_isRepresentable_restrict (S : Scheme.{u})
    (F : (Over S)ᵒᵖ ⥤ Type v) [F.IsRepresentable] :
    Presheaf.IsSheaf (Scheme.smallEtaleTopology S) ((Scheme.Etale.forget S).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigAffineZariski_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/AffineZariskiSheaves.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/AffineZariskiSheaves.lean#L88). The attribute's comment: “chosen big affine Zariski sheaves”.

> **Stacks Project, Tag 03O4.** Restriction of an fpqc sheaf on the schemes over `S` to a
> chosen big affine Zariski site of `S` is a sheaf.

```lean
public theorem isSheaf_bigAffineZariski_of_isSheaf_fpqc
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigAffineZariski.topology B S hS)
      ((BigAffineZariski.inclusion B S hS ⋙
        Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_smallAffineZariski_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/AffineZariskiSheaves.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/AffineZariskiSheaves.lean#L112). The attribute's comment: “chosen small affine Zariski sheaves”.

> **Stacks Project, Tag 03O4.** Restriction of an fpqc sheaf on the schemes over `S` to a
> chosen small affine Zariski site of `S` is a sheaf.

```lean
public theorem isSheaf_smallAffineZariski_of_isSheaf_fpqc
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (SmallAffineZariski.topology B S hS)
      ((SmallAffineZariski.inclusion B S hS ⋙ SmallZariski.inclusion B S hS ⋙
        Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_chosenBigEtale_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L255). The attribute's comment: “chosen big étale sheaves”.

> Restriction of an fpqc sheaf to a chosen big étale site of `S` is a sheaf.

```lean
public theorem isSheaf_chosenBigEtale_of_isSheaf_fpqc
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigEtaleOver.topology B S hS)
      ((Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigZariski_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L287). The attribute's comment: “chosen big Zariski sheaves”.

> Restriction of an fpqc sheaf to a chosen big Zariski site of `S` is a sheaf.

```lean
public theorem isSheaf_bigZariski_of_isSheaf_fpqc
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigZariskiOver.topology B S hS)
      ((Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_smallZariski_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L323). The attribute's comment: “chosen small Zariski sheaves”.

> Restriction of an fpqc sheaf to a chosen small Zariski site of `S` is a sheaf.

```lean
public theorem isSheaf_smallZariski_of_isSheaf_fpqc
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (SmallZariski.topology B S hS)
      ((SmallZariski.inclusion B S hS ⋙
        Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigAffineEtale_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L412). The attribute's comment: “chosen big affine étale sheaves”.

> Restriction of an fpqc sheaf to a chosen big affine étale site is a sheaf.

```lean
public theorem isSheaf_bigAffineEtale_of_isSheaf_fpqc
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigAffineEtale.topology B S hS)
      ((BigAffineEtale.inclusion B S hS ⋙
        Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_smallAffineEtale_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L423). The attribute's comment: “chosen small affine étale sheaves”.

> Restriction of an fpqc sheaf to a chosen small affine étale site is a sheaf.

```lean
public theorem isSheaf_smallAffineEtale_of_isSheaf_fpqc
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (SmallAffineEtale.topology B S hS)
      ((SmallAffineEtale.inclusion B S hS ⋙ SmallEtale.inclusion B S hS ⋙
        Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigFppf_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L548). The attribute's comment: “chosen big fppf sheaves”.

> Restriction of an fpqc sheaf to a chosen big fppf site is a sheaf.

```lean
public theorem isSheaf_bigFppf_of_isSheaf_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      ((Over.post (X := B.obj hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigAffineFppf_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 669](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L669). The attribute's comment: “chosen big affine fppf sheaves”.

> Restriction of an fpqc sheaf to a chosen big affine fppf site is a sheaf.

```lean
public theorem isSheaf_bigAffineFppf_of_isSheaf_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigAffineFppf.topology B S hS)
      ((BigAffineFppf.inclusion B S hS ⋙
        Over.post (X := B.obj hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigSmooth_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L680). The attribute's comment: “chosen big smooth sheaves”.

> Restriction of an fpqc sheaf to a chosen big smooth site is a sheaf.

```lean
public theorem isSheaf_bigSmooth_of_isSheaf_fpqc
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigSmoothOver.topology B S hS)
      ((Over.post (X := (⟨S, hS⟩ : B.category))
        (ObjectProperty.ι _)).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigAffineSmooth_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 691](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L691). The attribute's comment: “chosen big affine smooth sheaves”.

> Restriction of an fpqc sheaf to a chosen big affine smooth site is a sheaf.

```lean
public theorem isSheaf_bigAffineSmooth_of_isSheaf_fpqc
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigAffineSmooth.topology B S hS)
      ((BigAffineSmooth.inclusion B S hS ⋙
        Over.post (X := (⟨S, hS⟩ : B.category))
          (ObjectProperty.ι _)).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigSyntomic_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L703). The attribute's comment: “chosen big syntomic sheaves”.

> Restriction of an fpqc sheaf to a chosen big syntomic site is a sheaf.

```lean
public theorem isSheaf_bigSyntomic_of_isSheaf_fpqc
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigSyntomicOver.topology B S hS)
      ((Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.isSheaf_bigAffineSyntomic_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 713](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L713). The attribute's comment: “chosen big affine syntomic sheaves”.

> Restriction of an fpqc sheaf to a chosen big affine syntomic site is a sheaf.

```lean
public theorem isSheaf_bigAffineSyntomic_of_isSheaf_fpqc
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (BigAffineSyntomic.topology B S hS)
      ((BigAffineSyntomic.inclusion B S hS ⋙
        Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`AlgebraicGeometry.Scheme.smoothTopology_le_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L91). The attribute's comment: “smooth topology”.

> **The smooth comparison of Tag 03O4.** The fpqc topology is finer than the smooth
> topology.

```lean
public theorem smoothTopology_le_fpqcTopology :
    Scheme.grothendieckTopology (@Smooth : MorphismProperty Scheme.{u}) ≤
      Scheme.fpqcTopology.{u}
```

**`AlgebraicGeometry.Scheme.syntomicTopology_le_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L99). The attribute's comment: “syntomic topology”.

> **The syntomic comparison of Tag 03O4.** The fpqc topology is finer than the syntomic
> topology.

```lean
public theorem syntomicTopology_le_fpqcTopology :
    Scheme.grothendieckTopology (@Syntomic : MorphismProperty Scheme.{u}) ≤
      Scheme.fpqcTopology.{u}
```

**`AlgebraicGeometry.isSheaf_zariski_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L108). The attribute's comment: “Zariski sheaves”. References: SGA 3 XI (3.4), “fpqc example”.

> **Stacks 03O4.** An fpqc sheaf on the schemes over `S` is a Zariski sheaf.

```lean
public theorem isSheaf_zariski_of_isSheaf_fpqc (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (Scheme.zariskiTopology.over S) F
```

**`AlgebraicGeometry.isSheaf_etale_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L115). The attribute's comment: “étale sheaves”.

> **Stacks 03O4.** An fpqc sheaf on the schemes over `S` is an étale sheaf.

```lean
public theorem isSheaf_etale_of_isSheaf_fpqc (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (Scheme.etaleTopology.over S) F
```

**`AlgebraicGeometry.isSheaf_smooth_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L123). The attribute's comment: “smooth sheaves”.

> **Stacks 03O4.** An fpqc sheaf on the schemes over `S` is a smooth sheaf.

```lean
public theorem isSheaf_smooth_of_isSheaf_fpqc (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf
      ((Scheme.grothendieckTopology (@Smooth : MorphismProperty Scheme.{u})).over S) F
```

**`AlgebraicGeometry.isSheaf_syntomic_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L131). The attribute's comment: “syntomic sheaves”.

> **Stacks 03O4.** An fpqc sheaf on the schemes over `S` is a syntomic sheaf.

```lean
public theorem isSheaf_syntomic_of_isSheaf_fpqc (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf
      ((Scheme.grothendieckTopology (@Syntomic : MorphismProperty Scheme.{u})).over S) F
```

**`AlgebraicGeometry.isSheaf_fppf_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L139). The attribute's comment: “fppf sheaves”.

> **Stacks 03O4.** An fpqc sheaf on the schemes over `S` is an fppf sheaf.

```lean
public theorem isSheaf_fppf_of_isSheaf_fpqc (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (Scheme.fppfTopology.over S) F
```

**`AlgebraicGeometry.isSheaf_chosenSmallEtale_of_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcSmallEtaleSheaf.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcSmallEtaleSheaf.lean#L152). The attribute's comment: “chosen small étale sheaves”.

> **Stacks 03O4.** Restriction of an fpqc sheaf to a chosen small étale site is a sheaf.

```lean
public theorem isSheaf_chosenSmallEtale_of_isSheaf_fpqc
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (Over S)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (Scheme.fpqcTopology.over S) F) :
    Presheaf.IsSheaf (SmallEtale.topology B S hS)
      ((SmallEtale.inclusion B S hS ⋙
        Over.post (X := B.obj S hS) B.inclusion).op ⋙ F)
```

**`Stacks.Sites.etaleTopology_le_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleGlobalFunctions.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleGlobalFunctions.lean#L203). The attribute's comment: “étale topology”. References: SGA 4 VII (4.2), “étale ≤ fpqc”; SGA 3 IV (6.6), “(6.6.1) ét ≤ fpqc”.

> The étale topology is coarser than the fpqc topology.

```lean
public theorem etaleTopology_le_fpqcTopology :
    Scheme.etaleTopology.{u} ≤ Scheme.fpqcTopology.{u}
```

Declarations registered for the tag:

- [`Scheme.zariskiTopology_le_fpqcTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.zariskiTopology_le_fpqcTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L211) (StacksFrontier): “Zariski topology”.
- [`Scheme.fppfTopology_le_fpqcTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.fppfTopology_le_fpqcTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Comparison.lean#L216) (StacksFrontier): “fppf topology”.

## Tag 03O5, an example

[Tag 03O5](https://stacks.math.columbia.edu/tag/03O5) in the Stacks Project.

**`AlgebraicGeometry.additiveGroupBaseChangeYonedaIsoBigStructurePresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean#L157). The attribute's comment: “functor of points”.

> **Stacks 03O5.** The natural bijection `Mor_S(T, 𝐆_{a,S}) ≃ Γ(T, 𝒪_T)`, as an isomorphism
> of presheaves of sets on the schemes over `S`: the presheaf represented by the additive group
> scheme over `S` is the presheaf of global regular functions.

```lean
noncomputable def additiveGroupBaseChangeYonedaIsoBigStructurePresheaf (S : Scheme.{u}) :
    yoneda.obj (Scheme.asOver (additiveGroupBaseChange S) S) ≅
      Scheme.bigStructurePresheaf S ⋙ forget CommRingCat
```

**`AlgebraicGeometry.isSheaf_fpqc_bigStructurePresheaf_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean#L166). The attribute's comment: “fpqc sheaf of sets”.

> **Stacks 03O5.** The presheaf of sets `T/S ↦ Γ(T, 𝒪_T)` on the schemes over `S` satisfies
> the sheaf condition for the fpqc topology: it is represented by the additive group scheme over
> `S`, and the fpqc topology on the schemes over `S` is subcanonical.

```lean
theorem isSheaf_fpqc_bigStructurePresheaf_forget (S : Scheme.{u}) :
    Presieve.IsSheaf (Scheme.fpqcTopology.{u}.over S)
      (Scheme.bigStructurePresheaf S ⋙ forget CommRingCat)
```

**`AlgebraicGeometry.Scheme.isSheaf_fpqc_bigStructurePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/BigStructureSheaf.lean#L179). The attribute's comment: “fpqc sheaf of rings”. References: SGA 4 VII (4.2), “special case”.

> **Stacks 03O5.** The presheaf of *rings* `𝒪 : (Sch/S)ᵒᵖ ⥤ Rings`, `T/S ↦ Γ(T, 𝒪_T)`,
> satisfies the sheaf condition for the fpqc topology on the schemes over `S`.
>
> This is `AlgebraicGeometry.Scheme.isSheaf_fpqcTopology_Γ` restricted along the forgetful functor
> `Sch/S ⥤ Sch`, which is continuous from the localized fpqc topology to the fpqc topology.

```lean
theorem Scheme.isSheaf_fpqc_bigStructurePresheaf (S : Scheme.{u}) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.{u}.over S) (Scheme.bigStructurePresheaf S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.15, Tag 03NV](https://stacks.math.columbia.edu/tag/03NV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
