---
declaration: section
origin: cited
lean: Stacks.AlmostBlowUp.surjective_Γ_modificationToBase, Stacks.AlmostBlowUp.isZero_hgroup_structureSheaf, Stacks.AlmostBlowUp.modificationToBase_ker_sq_eq_bot, AlgebraicGeometry.BigHOver.existsUnique_iso_frobeniusColimitSections, AlgebraicGeometry.BigHOver.isSheaf_frobeniusLimitSections, AlgebraicGeometry.isSheaf_absoluteWeakNormalizationSections, AlgebraicGeometry.existsUnique_hom_absoluteWeakNormalizationSections, AlgebraicGeometry.BigHOver.isSheaf_absoluteWeakNormalizationSections
statement: formalized
proof: formalized
---

# 38.38 Absolute weak normalization and h coverings

Section 38.38 of the Stacks Project, [Tag 0EVS](https://stacks.math.columbia.edu/tag/0EVS). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EVJ, a lemma

[Tag 0EVJ](https://stacks.math.columbia.edu/tag/0EVJ) in the Stacks Project.

**`Stacks.AlmostBlowUp.surjective_Γ_modificationToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorCohomology.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorCohomology.lean#L222). The attribute's comment: “surjectivity”.

> **Stacks Project, Tag 0EVJ.** For the two-generator almost blowup square the ring map
> `Γ(X, 𝒪_X) ⟶ Γ(X', 𝒪_{X'})` is surjective.
>
> A global function on `X'` has a value on each of the two standard charts; the two agree on the
> overlap, so `Stacks.AlmostBlowUp.exists_chartAwayMap_eq` produces an element of `A` with those
> two values, and a global function is determined by its chart values.

```lean
theorem surjective_Γ_modificationToBase :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    Function.Surjective (Scheme.Γ.map (modificationToBase A f₁ f₂).op).hom
```

**`Stacks.AlmostBlowUp.isZero_hgroup_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorCohomology.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorCohomology.lean#L364). The attribute's comment: “higher cohomology vanishing”.

> **Stacks Project, Tag 0EVJ.** `Hᵖ(X', 𝒪_{X'}) = 0` for `p > 0`.
>
> The modification of the two-generator almost blowup square is covered by the two standard affine
> opens `D₊(T₀)` and `D₊(T₁)`, whose intersection `D₊(T₀T₁)` is affine too. Mayer--Vietoris
> therefore reduces positive-degree cohomology over the whole space to positive-degree cohomology
> over those three affines, which vanishes by Serre, plus — in degree one — the surjectivity of
> `Stacks.AlmostBlowUp.exists_restrict_add_restrict_eq`.

```lean
theorem isZero_hgroup_structureSheaf (p : ℕ) (hp : 0 < p) :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    IsZero (Hgroup (AlgebraicGeometry.Proj (modificationGrading A f₁ f₂)).ringCatSheaf ⊤ p
      (SheafOfModules.unit
        (AlgebraicGeometry.Proj (modificationGrading A f₁ f₂)).ringCatSheaf))
```

**`Stacks.AlmostBlowUp.modificationToBase_ker_sq_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorKernel.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/TwoGeneratorKernel.lean#L221). The attribute's comment: “kernel\_square\_zero”.

> **Stacks Project, Tag 0EVJ.** The global functions on `Spec A` killed by the modification
> of the two-generator almost blowup square form an ideal of square zero.

```lean
theorem modificationToBase_ker_sq_eq_bot (A : Type u) [CommRing A] (f₁ f₂ : A) :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    RingHom.ker (Scheme.Γ.map (modificationToBase A f₁ f₂).op).hom ^ 2 = ⊥
```

## Tag 0EVK, a lemma

[Tag 0EVK](https://stacks.math.columbia.edu/tag/0EVK) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.existsUnique_iso_frobeniusColimitSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitHSheaf.lean, line 957](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitHSheaf.lean#L957).

> **Stacks 0EVK.** Let `p` be a prime number, let `S` be a scheme over `𝔽_p` (that is, `p`
> vanishes in `Γ(S, 𝒪_S)`), and let `(Sch/S)_h` be a big h site over `S` as in Stacks 0EU1.  There
> is a unique sheaf `ℱ` on `(Sch/S)_h` such that `ℱ(X) = colim_F Γ(X, 𝒪_X)` for every quasi-compact
> quasi-separated object `X`.
>
> The identification is a morphism of presheaves `colim_F Γ(-, 𝒪) ⟶ ℱ` that is bijective on
> quasi-compact quasi-separated objects, so naturality in `X` expresses compatibility with
> restriction.  The first conjunct is existence and the second is uniqueness: two such sheaves are
> isomorphic, by a unique isomorphism compatible with the identifications.
>
> The sheaf constructed is `X ↦ Γ(Xᵃʷⁿ, 𝒪)`, global functions on the absolute weak normalization.
> The proof does not use the criterion of Stacks 0EVI, whose sufficiency direction this
> development lacks; it uses the absolute weak normalization instead.  The sheaf property comes
> from the descent statements behind Stacks 0EVT and the h-sheaf criterion Stacks 0EU5.  The
> comparison `colim_F Γ(X, 𝒪_X) ⟶ Γ(Xᵃʷⁿ, 𝒪)` is bijective on quasi-compact quasi-separated `X`.
> On an affine open this is Stacks 0EVW, and the affine pieces glue over a finite affine covering
> because the overlaps are quasi-compact.

```lean
public theorem existsUnique_iso_frobeniusColimitSections (p : ℕ) (hp : p.Prime)
    (hSp : Stacks.Frobenius.IsInCharacteristic S p) :
    (∃ (F : (BigHOver B S hS)ᵒᵖ ⥤ Type u) (φ : frobeniusColimitSections B S hS p ⟶ F),
      Presheaf.IsSheaf (BigHOver.topology B S hS) F ∧
        ∀ X : BigHOver B S hS, CompactSpace ((BigHOver.toScheme B S hS).obj X) →
          QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj X) →
            Function.Bijective (φ.app (op X))) ∧
    ∀ {F G : (BigHOver B S hS)ᵒᵖ ⥤ Type u}
      (φ : frobeniusColimitSections B S hS p ⟶ F) (ψ : frobeniusColimitSections B S hS p ⟶ G),
      Presheaf.IsSheaf (BigHOver.topology B S hS) F →
      Presheaf.IsSheaf (BigHOver.topology B S hS) G →
      (∀ X : BigHOver B S hS, CompactSpace ((BigHOver.toScheme B S hS).obj X) →
        QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj X) →
          Function.Bijective (φ.app (op X))) →
      (∀ X : BigHOver B S hS, CompactSpace ((BigHOver.toScheme B S hS).obj X) →
        QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj X) →
          Function.Bijective (ψ.app (op X))) →
      ∃! e : F ≅ G, φ ≫ e.hom = ψ
```

## Tag 0EVL, a lemma

[Tag 0EVL](https://stacks.math.columbia.edu/tag/0EVL) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.isSheaf_frobeniusLimitSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusLimitHSheafCriterion.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusLimitHSheafCriterion.lean#L69).

> **Stacks 0EVL.** Let `p` be a prime number and let `S` be a scheme over `𝔽_p`, contained in a
> big h site `B`.  Then `X ↦ lim_F Γ(X, 𝒪_X)`, the limit of the `p`-power map on global functions,
> is a sheaf on the big h site `(Sch/S)_h`.
>
> The four conditions of the h sheaf criterion Stacks 0EVI hold for this presheaf; the sufficiency
> direction of that criterion is `AlgebraicGeometry.affineAlmostBlowUpHSheafCriterion` together with
> `AlgebraicGeometry.generatorAlmostBlowUpSquaresSuffice`.

```lean
public theorem isSheaf_frobeniusLimitSections
    (p : ℕ) (hp : p.Prime) (hChar : Stacks.Frobenius.IsInCharacteristic S p) :
    Presheaf.IsSheaf (BigHOver.topology B S hS) (frobeniusLimitSections B S hS p)
```

## Tag 0EVT, a lemma

[Tag 0EVT](https://stacks.math.columbia.edu/tag/0EVT) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_absoluteWeakNormalizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/PhSheafOfSections.lean, line 866](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/PhSheafOfSections.lean#L866).

> On a big ph site, global functions on absolute weak normalizations form a sheaf.
>
> Together with `AlgebraicGeometry.existsUnique_hom_absoluteWeakNormalizationSections`, this shows
> that the canonical map from the structure sheaf exhibits this sheaf as its ph sheafification.

```lean
theorem isSheaf_absoluteWeakNormalizationSections (B : BigPHSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    Presheaf.IsSheaf (BigPHOver.topology B S hS) (absoluteWeakNormalizationSections B S hS)
```

## Tag 0EVU, a lemma

[Tag 0EVU](https://stacks.math.columbia.edu/tag/0EVU) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_absoluteWeakNormalizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/PhSheafOfSections.lean, line 866](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/PhSheafOfSections.lean#L866). The attribute's comment: “ph topology, the sheaf property”.

> On a big ph site, global functions on absolute weak normalizations form a sheaf.
>
> Together with `AlgebraicGeometry.existsUnique_hom_absoluteWeakNormalizationSections`, this shows
> that the canonical map from the structure sheaf exhibits this sheaf as its ph sheafification.

```lean
theorem isSheaf_absoluteWeakNormalizationSections (B : BigPHSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    Presheaf.IsSheaf (BigPHOver.topology B S hS) (absoluteWeakNormalizationSections B S hS)
```

**`AlgebraicGeometry.existsUnique_hom_absoluteWeakNormalizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean#L661). The attribute's comment: “ph topology”.

> **Stacks Project, Tag 0EVU**, the ph case. On a big ph site over `S`, global functions on
> absolute weak normalizations are the sheafification of the structure sheaf: every map from the
> structure sheaf to a sheaf of rings factors uniquely through the canonical map. The other half
> of the statement, that the target is a sheaf, is Stacks 0EVT.

```lean
theorem existsUnique_hom_absoluteWeakNormalizationSections
    (G : (BigPHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u})
    (hG : Presheaf.IsSheaf (BigPHOver.topology B S hS) G)
    (α : (BigPHOver.toScheme B S hS).op ⋙ Scheme.Γ ⟶ G) :
    ∃! χ : absoluteWeakNormalizationSections B S hS ⟶ G,
      absoluteWeakNormalizationSectionsMap (BigPHOver.toScheme B S hS) ≫ χ = α
```

**`AlgebraicGeometry.BigHOver.isSheaf_absoluteWeakNormalizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean, line 722](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean#L722). The attribute's comment: “h topology, the sheaf property”.

> **Stacks Project, Tag 0EVU**, the sheaf property in the h case. On a big h site over `S`,
> global functions on absolute weak normalizations form a sheaf for the h topology.
>
> This is the h analogue of Stacks 0EVT, and is proved from the same two descent statements —
> Zariski descent and descent along a proper surjection onto an affine — through the h sheaf
> criterion of Stacks 0EU5, whose second condition carries the extra hypothesis that the proper
> surjection is of finite presentation.

```lean
theorem isSheaf_absoluteWeakNormalizationSections :
    Presheaf.IsSheaf (BigHOver.topology B S hS)
      (absoluteWeakNormalizationSectionsOver (BigHOver.toScheme B S hS))
```

**`AlgebraicGeometry.BigHOver.existsUnique_hom_absoluteWeakNormalizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/StructureSheafSheafification.lean#L758). The attribute's comment: “h topology, the universal property of the sheafification”.

> **Stacks Project, Tag 0EVU**, the h case. On a big h site over `S`, global functions on
> absolute weak normalizations are the sheafification of the structure sheaf: every map from the
> structure sheaf to a sheaf of rings factors uniquely through the canonical map. Together with
> `AlgebraicGeometry.BigHOver.isSheaf_absoluteWeakNormalizationSections`, which is the other half
> of the statement, this says that the rule `X ↦ Γ(Xᵃʷⁿ, 𝒪)` is the sheafification of the
> structure sheaf on the big h site.

```lean
theorem existsUnique_hom_absoluteWeakNormalizationSections
    (G : (BigHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u})
    (hG : Presheaf.IsSheaf (BigHOver.topology B S hS) G)
    (α : (BigHOver.toScheme B S hS).op ⋙ Scheme.Γ ⟶ G) :
    ∃! χ : absoluteWeakNormalizationSectionsOver (BigHOver.toScheme B S hS) ⟶ G,
      absoluteWeakNormalizationSectionsMap (BigHOver.toScheme B S hS) ≫ χ = α
```

## Tag 0EVV, a lemma

[Tag 0EVV](https://stacks.math.columbia.edu/tag/0EVV) in the Stacks Project.

**`isAbsolutelyWeaklyNormalRing_iff_perfectRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/AbsolutelyWeaklyNormalPerfect.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/AbsolutelyWeaklyNormalPerfect.lean#L56).

> An algebra over `𝐅_p`, for `p` prime, is absolutely weakly normal if and only if its
> Frobenius endomorphism is bijective.

```lean
lemma isAbsolutelyWeaklyNormalRing_iff_perfectRing
    (p : ℕ) (hp : p.Prime) (A : Type*) [CommRing A] [Algebra (ZMod p) A] :
    IsAbsolutelyWeaklyNormalRing A ↔ PerfectRing A p
```

## Tag 0EVW, a lemma

[Tag 0EVW](https://stacks.math.columbia.edu/tag/0EVW) in the Stacks Project.

**`Algebra.existsUnique_frobeniusColimit_iso_absoluteWeakNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimit.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimit.lean#L229). The attribute's comment: “frobenius\_colimit”.

> For `p` prime and `A` an algebra over `ZMod p`, the colimit of the Frobenius sequence of `A`
> is the absolute weak normalization of `A`, by a unique isomorphism compatible with the canonical
> maps out of `A`.

```lean
theorem existsUnique_frobeniusColimit_iso_absoluteWeakNormalization
    (p : ℕ) (hp : p.Prime) (A : Type u) [CommRing A] [Algebra (ZMod p) A] :
    letI : Fact p.Prime := ⟨hp⟩
    ∃! e : colimit (frobeniusDiagram p A) ≅
        CommRingCat.of (AbsoluteWeakNormalization A),
      colimit.ι (frobeniusDiagram p A) 0 ≫ e.hom =
        CommRingCat.ofHom (algebraMap A (AbsoluteWeakNormalization A))
```

**`AlgebraicGeometry.BigHOver.exists_bijective_hom_frobeniusColimitSections_of_isSheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitSheafification.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitSheafification.lean#L86). The attribute's comment: “the h sheafification of the structure sheaf on qcqs objects”.

> **Part (2) of Stacks Project, Tag 0EVW.** Let `p` be a prime number and let `S` be a scheme
> over `𝔽_p`, that is, a scheme in which `p` vanishes on global functions.  Let `(Sch/S)_h` be a
> big h site over `S` as in Stacks 0EU1.  Let `G` be the h sheafification of the structure sheaf
> `𝒪`: a sheaf of rings together with a map `α : 𝒪 ⟶ G` initial among the maps from `𝒪` to sheaves
> of rings.  Then the sections of `G` over a quasi-compact quasi-separated object `X` are
> `colim_F Γ(X, 𝒪_X)`.
>
> The identification is given by a map of presheaves `colim_F Γ(-, 𝒪) ⟶ G` which agrees with `α`
> on the stage `0` of the Frobenius tower and is bijective over every quasi-compact quasi-separated
> object; naturality is compatibility with restriction.

```lean
public theorem exists_bijective_hom_frobeniusColimitSections_of_isSheafification (p : ℕ)
    (hp : p.Prime) (hSp : Stacks.Frobenius.IsInCharacteristic S p)
    (G : (BigHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u})
    (hG : Presheaf.IsSheaf (BigHOver.topology B S hS) G)
    (α : (BigHOver.toScheme B S hS).op ⋙ Scheme.Γ.{u} ⟶ G)
    (hα : ∀ H : (BigHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u},
      Presheaf.IsSheaf (BigHOver.topology B S hS) H →
      ∀ β : (BigHOver.toScheme B S hS).op ⋙ Scheme.Γ.{u} ⟶ H, ∃! χ : G ⟶ H, α ≫ χ = β) :
    ∃ φ : frobeniusColimitSections B S hS p ⟶ G ⋙ CategoryTheory.forget CommRingCat.{u},
      (∀ (X : BigHOver B S hS) (a : Γ((BigHOver.toScheme B S hS).obj X, ⊤)),
        φ.app (op X) (colimitStage B S hS p 0 X a) = α.app (op X) a) ∧
      ∀ X : BigHOver B S hS, CompactSpace ((BigHOver.toScheme B S hS).obj X) →
        QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj X) →
          Function.Bijective (φ.app (op X))
```

**`AlgebraicGeometry.frobeniusColimit_absoluteWeakNormalization_and_hSheafificationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitSheafification.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/FrobeniusColimitSheafification.lean#L176).

> **Stacks Project, Tag 0EVW.** Let `p` be a prime number.
>
> (1) If `A` is an algebra over `𝔽_p`, then `colim_F A = A^{awn}`: the colimit of the Frobenius
> tower of `A` is the absolute weak normalization of `A`, by a unique isomorphism compatible with
> the canonical maps out of `A`.
>
> (2) If `S` is a scheme over `𝔽_p` and `(Sch/S)_h` is a big h site over `S` as in Stacks 0EU1,
> then the h sheafification of the structure sheaf `𝒪` — a sheaf of rings `G` with a map
> `α : 𝒪 ⟶ G` initial among the maps from `𝒪` to sheaves of rings — sends a quasi-compact
> quasi-separated object `X` to `colim_F Γ(X, 𝒪_X)`, by an identification agreeing with `α` on the
> stage `0` of the Frobenius tower.

```lean
public theorem frobeniusColimit_absoluteWeakNormalization_and_hSheafificationSections (p : ℕ)
    (hp : p.Prime) :
    letI : Fact p.Prime := ⟨hp⟩
    (∀ (A : Type u) [CommRing A] [Algebra (ZMod p) A],
      ∃! e : colimit (Algebra.frobeniusDiagram p A) ≅
          CommRingCat.of (Algebra.AbsoluteWeakNormalization A),
        colimit.ι (Algebra.frobeniusDiagram p A) 0 ≫ e.hom =
          CommRingCat.ofHom (algebraMap A (Algebra.AbsoluteWeakNormalization A))) ∧
    (∀ (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S),
      Stacks.Frobenius.IsInCharacteristic S p →
      ∀ (G : (BigHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u}),
        Presheaf.IsSheaf (BigHOver.topology B S hS) G →
      ∀ α : (BigHOver.toScheme B S hS).op ⋙ Scheme.Γ.{u} ⟶ G,
        (∀ H : (BigHOver B S hS)ᵒᵖ ⥤ CommRingCat.{u},
          Presheaf.IsSheaf (BigHOver.topology B S hS) H →
          ∀ β : (BigHOver.toScheme B S hS).op ⋙ Scheme.Γ.{u} ⟶ H, ∃! χ : G ⟶ H, α ≫ χ = β) →
        ∃ φ : BigHOver.frobeniusColimitSections B S hS p ⟶
            G ⋙ CategoryTheory.forget CommRingCat.{u},
          (∀ (X : BigHOver B S hS) (a : Γ((BigHOver.toScheme B S hS).obj X, ⊤)),
            φ.app (op X) (BigHOver.colimitStage B S hS p 0 X a) = α.app (op X) a) ∧
          ∀ X : BigHOver B S hS, CompactSpace ((BigHOver.toScheme B S hS).obj X) →
            QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj X) →
              Function.Bijective (φ.app (op X)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.38, Tag 0EVS](https://stacks.math.columbia.edu/tag/0EVS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
