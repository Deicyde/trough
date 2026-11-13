---
declaration: section
origin: cited
lean: AlgebraicGeometry.connectedSpace_of_isIso_globalSections, AlgebraicGeometry.isCohenMacaulay_of_isIso_globalSections_of_dimension_one, AlgebraicGeometry.equidimensional_of_isIso_globalSections_of_dimension_one, AlgebraicGeometry.CohenMacaulayCurveSituation, AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField, AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField_of_supp_dim_le_zero, AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_dualizingSheafOverField_tensor, AlgebraicGeometry.CohenMacaulayCurveSituation.epi_globalSectionsHom_comp
statement: formalized
proof: formalized
---

# 53.6 Some vanishing results

Section 53.6 of the Stacks Project, [Tag 0B5C](https://stacks.math.columbia.edu/tag/0B5C). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BY5, a lemma

[Tag 0BY5](https://stacks.math.columbia.edu/tag/0BY5) in the Stacks Project.

**`AlgebraicGeometry.connectedSpace_of_isIso_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean#L378). The attribute's comment: “connectedness”. References: SGA 3 VIB (12.3), “connectedness of N”.

> **Stacks Project, Tag 0BY5.** A scheme over a field whose only global regular functions
> are constants is connected.

```lean
theorem connectedSpace_of_isIso_globalSections
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] :
    ConnectedSpace X
```

**`AlgebraicGeometry.isCohenMacaulay_of_isIso_globalSections_of_dimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean#L430). The attribute's comment: “Cohen–Macaulayness”.

> **Stacks Project, Tag 0BY5.** A proper one-dimensional scheme over a field whose only
> global regular functions are constants is Cohen–Macaulay.

```lean
theorem isCohenMacaulay_of_isIso_globalSections_of_dimension_one
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] :
    IsCohenMacaulay X
```

**`AlgebraicGeometry.equidimensional_of_isIso_globalSections_of_dimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean, line 648](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/AutomaticProperties.lean#L648). The attribute's comment: “equidimensionality”.

> **Stacks Project, Tag 0BY5.** A proper one-dimensional scheme over a field whose only
> global regular functions are constants is equidimensional.

```lean
theorem equidimensional_of_isIso_globalSections_of_dimension_one
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] :
    TopologicalSpace.Equidimensional X
```

## Tag 0B5D, a situation

[Tag 0B5D](https://stacks.math.columbia.edu/tag/0B5D) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/Situation.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/Situation.lean#L40).

> **Stacks Project, Tag 0B5D.** The standing situation of a proper one-dimensional scheme
> over a field whose canonical ring of global sections is the base field.

```lean
structure CohenMacaulayCurveSituation
```

## Tag 0B5E, a lemma

[Tag 0B5E](https://stacks.math.columbia.edu/tag/0B5E) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafExtension.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafExtension.lean#L78).

> **Stacks Project, Tag 0B5E.** In Situation [Stacks, Tag 0B5D], let
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` be the dualizing sheaf of `X` ([Stacks, Tag 0BS2]) and let
> `ω_X ⟶ ℱ ⟶ 𝒬 ⟶ 0` be an exact sequence of `𝒪_X`-modules with `H¹(X, 𝒬) = 0`. Then either
> `H¹(X, ℱ) = 0`, or `ℱ ≅ ω_X ⊕ 𝒬` compatibly with both arrows of the sequence.
>
> The source asks `ℱ` and `𝒬` to be coherent; only the quasi-coherence of `ℱ` is used. This is
> `isZero_firstCohomology_or_iso_biprod` at `ω_X`, whose three inputs — clause (5) of
> [Stacks, Tag 0BS2], `dim_k H¹(X, ω_X) = 1` and the vanishing of `H²(X, -)` — are proved; see
> the module documentation.

```lean
public theorem isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField {F Q : S.X.Modules}
    (hFq : F.IsQuasicoherent) (α : Stacks.Duality.dualizingSheafOverField S.f ⟶ F) (β : F ⟶ Q)
    (hαβ : α ≫ β = 0) (hex : (ShortComplex.mk α β hαβ).Exact) [Epi β]
    (hQ : IsZero (cohomologyOverField S.k S.f Q 1)) :
    IsZero (cohomologyOverField S.k S.f F 1) ∨
      ∃ e : F ≅ Stacks.Duality.dualizingSheafOverField S.f ⊞ Q,
        α ≫ e.hom = biprod.inl ∧ e.hom ≫ biprod.snd = β
```

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField_of_supp_dim_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafExtension.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafExtension.lean#L98). The attribute's comment: “the parenthetical example: Q coherent with dim(Supp(Q)) = 0, where H¹(X, Q) = 0 by Tag 0B3J”.

> **Stacks Project, Tag 0B5E, the parenthetical example.** In Situation [Stacks, Tag 0B5D],
> for an exact sequence `ω_X ⟶ ℱ ⟶ 𝒬 ⟶ 0` of `𝒪_X`-modules with `𝒬` coherent and
> `dim(Supp(𝒬)) ≤ 0`, either `H¹(X, ℱ) = 0` or `ℱ ≅ ω_X ⊕ 𝒬` compatibly with both arrows.
>
> The vanishing `H¹(X, 𝒬) = 0` is [Stacks, Tag 0B3J], as the source says, and the rest is
> `isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField`.

```lean
public theorem isZero_firstCohomology_or_iso_biprod_dualizingSheafOverField_of_supp_dim_le_zero
    {F Q : S.X.Modules} (hFq : F.IsQuasicoherent) (hQ : Q.IsCoherent)
    (hQdim : topologicalKrullDim (SheafOfModules.supp Q) ≤ 0)
    (α : Stacks.Duality.dualizingSheafOverField S.f ⟶ F) (β : F ⟶ Q)
    (hαβ : α ≫ β = 0) (hex : (ShortComplex.mk α β hαβ).Exact) [Epi β] :
    IsZero (cohomologyOverField S.k S.f F 1) ∨
      ∃ e : F ≅ Stacks.Duality.dualizingSheafOverField S.f ⊞ Q,
        α ≫ e.hom = biprod.inl ∧ e.hom ≫ biprod.snd = β
```

## Tag 0B62, a lemma

[Tag 0B62](https://stacks.math.columbia.edu/tag/0B62) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_firstCohomology_dualizingSheafOverField_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingTwistCanonical.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingTwistCanonical.lean#L109). The attribute's comment: “at the dualizing sheaf H^\{-1}(f^×(𝒪\_\{Spec k})) of Tag 0BS2, nothing carried”.

> **Stacks Project, Tag 0B62**, at the dualizing sheaf `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` of
> [Stacks, Tag 0BS2]. In Situation [Stacks, Tag 0B5D], if `ℒ` is an invertible `𝒪_X`-module which
> is generated by its global sections and is not isomorphic to `𝒪_X`, then `H¹(X, ω_X ⊗ ℒ) = 0`.
>
> By duality (`dualityVanishing_dualizingSheafOverField`) the tag reduces to
> `H⁰(X, ℒ^{⊗ -1}) = 0`, which is `subsingleton_globalSections_inverse_of_generatingSections`.

```lean
public theorem isZero_firstCohomology_dualizingSheafOverField_tensor
    (L : S.X.Modules) [IsInvertible S.X.presheaf S.X.ringCatSheaf.property L]
    (σ : L.GeneratingSections)
    (hne : ¬ IsTrivial S.X.presheaf S.X.ringCatSheaf.property L) :
    IsZero (cohomologyOverField S.k S.f
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
          (S.X.ringCatSheaf.property)⟩).obj
        (Stacks.Duality.dualizingSheafOverField S.f)).obj L)) 1)
```

## Tag 0B5F, a lemma

[Tag 0B5F](https://stacks.math.columbia.edu/tag/0B5F) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.epi_globalSectionsHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalSectionsGeneration.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalSectionsGeneration.lean#L388). The attribute's comment: “two properties of ω are arguments, neither of them an assertion of this tag, because the library has no dualizing sheaf of a proper curve over a field: clause (5) of Tag 0BS2 is hdual and dim\_k H¹(X, ω) = 1 of Section 0B5B is hone. The rest is proved here: both clauses of Tag 0B3J are applied to the zero-dimensional support of Q, as the source does, and the vanishing of H²(X, -) of Tag 02UZ comes from secondCohomologyVanishing”.

> In Situation [Stacks, Tag 0B5D], let `ω` be the dualizing sheaf of `X` and let
> `ω ⟶ ℱ ⟶ 𝒬 ⟶ 0` be an exact sequence of coherent `𝒪_X`-modules such that the support of `𝒬` has
> dimension at most zero, `dim_k H⁰(X, 𝒬) ≥ 2`, and no nonzero submodule of `ℱ` maps injectively
> to `𝒬`. Then the submodule of `ℱ` generated by the global sections of `ℱ` surjects onto `𝒬`.

```lean
public theorem epi_globalSectionsHom_comp {ω F Q : S.X.Modules}
    (hωq : ω.IsQuasicoherent) (hFq : F.IsQuasicoherent) (hFft : F.IsFiniteType)
    (hQq : Q.IsQuasicoherent) (hdual : S.FirstCohomologyDuality ω)
    (hone : Module.finrank S.k (cohomologyOverField S.k S.f ω 1) = 1)
    (α : ω ⟶ F) (β : F ⟶ Q) (hαβ : α ≫ β = 0)
    (hex : (ShortComplex.mk α β hαβ).Exact) [Epi β]
    (hQdim : topologicalKrullDim (SheafOfModules.supp Q) ≤ 0)
    (htwo : 2 ≤ Module.finrank S.k (cohomologyOverField S.k S.f Q 0))
    (hnosub : ∀ (M : S.X.Modules) (u : M ⟶ F), Mono u → Mono (u ≫ β) → IsZero M) :
    Epi (globalSectionsHom F ≫ β)
```

**`AlgebraicGeometry.CohenMacaulayCurveSituation.epi_globalSectionsHom_comp_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalSectionsGenerationDualizing.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalSectionsGenerationDualizing.lean#L52).

> **Stacks Project, Tag 0B5F.** In Situation [Stacks, Tag 0B5D], let
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` be the dualizing sheaf of `X` ([Stacks, Tag 0BS2]) and let
> `ω_X ⟶ ℱ ⟶ 𝒬 ⟶ 0` be an exact sequence of coherent `𝒪_X`-modules such that the support of `𝒬`
> has dimension at most zero, `dim_k H⁰(X, 𝒬) ≥ 2`, and no nonzero submodule of `ℱ` maps
> injectively to `𝒬`. Then the submodule of `ℱ` generated by the global sections of `ℱ` surjects
> onto `𝒬`, i.e. the composite of `AlgebraicGeometry.globalSectionsHom ℱ` with `ℱ ⟶ 𝒬` is an
> epimorphism.
>
> Coherence of `ℱ` enters as quasi-coherence and finite type; of `𝒬` only quasi-coherence is used.
> This is `epi_globalSectionsHom_comp` at the dualizing sheaf, whose two properties are proved.

```lean
public theorem epi_globalSectionsHom_comp_dualizingSheafOverField {F Q : S.X.Modules}
    (hFq : F.IsQuasicoherent) (hFft : F.IsFiniteType) (hQq : Q.IsQuasicoherent)
    (α : Stacks.Duality.dualizingSheafOverField S.f ⟶ F) (β : F ⟶ Q) (hαβ : α ≫ β = 0)
    (hex : (ShortComplex.mk α β hαβ).Exact) [Epi β]
    (hQdim : topologicalKrullDim (SheafOfModules.supp Q) ≤ 0)
    (htwo : 2 ≤ Module.finrank S.k (cohomologyOverField S.k S.f Q 0))
    (hnosub : ∀ (M : S.X.Modules) (u : M ⟶ F), Mono u → Mono (u ≫ β) → IsZero M) :
    Epi (globalSectionsHom F ≫ β)
```

## Tag 0B5G, a lemma

[Tag 0B5G](https://stacks.math.columbia.edu/tag/0B5G) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.nonempty_generatingSections_of_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafGenericStalk.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafGenericStalk.lean#L175).

> **Stacks Project, Tag 0B5G.** In Situation [Stacks, Tag 0B5D] assume that `X` is integral,
> let `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` be the dualizing sheaf of [Stacks, Tag 0BS2], and let
> `0 ⟶ ω_X ⟶ ℱ ⟶ 𝒬 ⟶ 0` be a short exact sequence of coherent `𝒪_X`-modules with `ℱ` torsion free
> ([Stacks, Tag 0AVR]), `dim Supp 𝒬 ≤ 0` and `dim_k H⁰(X, 𝒬) ≥ 2`. Then `ℱ` is globally generated.
>
> The generic stalk of `ω_X` is one-dimensional over the function field
> (`isSimpleModule_genericStalk_dualizingSheafOverField`, from [Stacks, Tags 0FVV, 0AWF, 0A7R]),
> and `epi_globalSectionsHom_of_isSimpleModule_genericStalk` runs the source's argument from there:
> [Stacks, Tag 0B5F], the duality of clause (5) of [Stacks, Tag 0BS2], and the finiteness of
> [Stacks, Tag 02O6].

```lean
public theorem nonempty_generatingSections_of_isTorsionFree [IsIntegral S.X] {F Q : S.X.Modules}
    (hFc : F.IsCoherent) (hQc : Q.IsCoherent)
    (α : Stacks.Duality.dualizingSheafOverField S.f ⟶ F) (β : F ⟶ Q) (hαβ : α ≫ β = 0)
    (hS : (ShortComplex.mk α β hαβ).ShortExact)
    (hTF : Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionFree F)
    (hQdim : topologicalKrullDim (SheafOfModules.supp Q) ≤ 0)
    (htwo : 2 ≤ Module.finrank S.k (cohomologyOverField S.k S.f Q 0)) :
    Nonempty (F : SheafOfModules S.X.ringCatSheaf).GeneratingSections
```

## Tag 0B5H, a lemma

[Tag 0B5H](https://stacks.math.columbia.edu/tag/0B5H) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.nonempty_generatingSections_dualizingSheafOverField_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafCoherence.lean, line 790](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafCoherence.lean#L790).

> **[Stacks, Tag 0B5H].** In Situation [Stacks, Tag 0B5D] — a field `k`, a proper scheme `X` of
> dimension one over `k` with `H⁰(X, 𝒪_X) = k` — let `ℒ` be a very ample invertible `𝒪_X`-module
> with `deg(ℒ) ≥ 2`. Then `ω_X ⊗ ℒ` is globally generated, where
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` is the dualizing sheaf of [Stacks, Tag 0BS2].
>
> This is the source's proof: over `k̄` it is
> `nonempty_generatingSections_dualizing_tensorSheaf_of_isAlgClosed_of_isCoherent`, and the general
> case is the reduction `nonempty_generatingSections_dualizing_tensorSheaf_of_isoAlgebraicClosure`,
> whose two inputs are supplied here — the coherence of `ω_X` by
> `isCoherent_dualizingSheafOverField`, and the identification of the inverse image of `ω_X` with
> `ω_{X_{k̄}}` (part (2) of [Stacks, Tag 0E32] at the dualizing sheaf) by
> `pullbackDualizingSheafOverFieldIso`. Nothing is assumed beyond the source's hypotheses.

```lean
theorem nonempty_generatingSections_dualizingSheafOverField_tensorSheaf (L : S.X.Modules)
    [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L]
    (hL : Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple S.f L)
    (hd : 2 ≤ invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    Nonempty ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
      Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
      (S.X.ringCatSheaf.property)⟩).obj
      ((Stacks.Duality.dualizingSheafOverField S.f))).obj (L))).GeneratingSections
```

**`AlgebraicGeometry.CohenMacaulayCurveSituation.nonempty_generatingSections_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingTwistGeneration.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingTwistGeneration.lean#L389). The attribute's comment: “k algebraically closed; hsec carries Tag 0B58's section and the count of global sections of the twisted quotient, duality is hdual/hone/hH2, Nakayama is proved”.

> **Stacks Project, Tag 0B5H.** In Situation [Stacks, Tag 0B5D], let `ω` be the dualizing sheaf
> of `X` and let `ℒ` be an invertible `𝒪_X`-module with `deg(ℒ) ≥ 2`. Then `ω ⊗ ℒ` is generated by
> its global sections.
>
> Global generation is surjectivity of the map from the free module on all global sections of
> `ω ⊗ ℒ`, and `epi_globalSectionsHom_of_forall_isClosed` proves it from a section of `ℒ` vanishing
> at each closed point: [Stacks, Tag 0B5F] makes the global sections generate the quotient of
> `ω ⊗ ℒ` by `ω`, and Nakayama upgrades that to generation at the point.
>
> The section is [Stacks, Tag 0B58] and its global-section count is the degree theory of Section
> [Stacks, Tag 0B5B], both of which `hsec` supplies; the source uses very ampleness of `ℒ` only to
> invoke them, so that hypothesis is absent here. Duality for `ω` is `hdual`, `hone` and `hH2`, and
> its Cohen--Macaulayness is `hnosub`.

```lean
public theorem nonempty_generatingSections_tensorSheaf (ω L : S.X.Modules)
    [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L] (hωq : ω.IsQuasicoherent)
    (hdual : S.FirstCohomologyDuality ω) (hH2 : S.SecondCohomologyVanishing)
    (hone : Module.finrank S.k (cohomologyOverField S.k S.f ω 1) = 1)
    (hFq : ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
      Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
      (S.X.ringCatSheaf.property)⟩).obj (ω)).obj (L))).IsQuasicoherent)
    (hFft : ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
      Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
      (S.X.ringCatSheaf.property)⟩).obj (ω)).obj (L))).IsFiniteType)
    (hnosub : S.NoSubmoduleOfZeroDimensionalSupport
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
        (S.X.ringCatSheaf.property)⟩).obj (ω)).obj (L))))
    (hd : 2 ≤ invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L)
    (hsec : ∀ x : S.X, IsClosed ({x} : Set S.X) →
      S.VanishingSectionData ω ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
        (S.X.ringCatSheaf.property)⟩).obj (ω)).obj (L)))
        (invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) x) :
    Nonempty ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf,
      Presheaf.isSheaf_of_isSheaf_comp _ (S.X.presheaf) (forget₂ CommRingCat RingCat)
      (S.X.ringCatSheaf.property)⟩).obj (ω)).obj (L))).GeneratingSections
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.6, Tag 0B5C](https://stacks.math.columbia.edu/tag/0B5C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
