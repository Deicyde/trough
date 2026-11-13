---
declaration: section
origin: cited
lean: Stacks.SectionRingProjMorphism.Theta.projThetaUnital, Stacks.SectionRingProjMorphism.Theta.coveringOpen_eq_top_and_ι_comp_projHomOfIsAmple, Stacks.SectionRingProjGoodOpen.projHomOfIsAmple_preimage_whereInvertible, Stacks.SectionRingProjTwistIso.isIso_projTheta_app, Stacks.SectionRingVeroneseChart.isIso_twistComparison, Stacks.SectionRingProjQuasicoherent.pullbackTildeComparison_spec, Stacks.SectionRingProjTheta.projTheta_app_eq_twistThetaInt, Stacks.SectionRingProjTheta.twistSquareInt
statement: formalized
proof: formalized
---

# 28.29 Quasi-coherent sheaves and ample invertible sheaves

Section 28.29 of the Stacks Project, [Tag 01QG](https://stacks.math.columbia.edu/tag/01QG). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01QH, a situation

[Tag 01QH](https://stacks.math.columbia.edu/tag/01QH) in the Stacks Project.

**`Stacks.SectionRingProjMorphism.Theta.projThetaUnital`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L173). The attribute's comment: “the Z-graded O\_X-algebra map sum\_n f^*O\_Y(n) -> sum\_n L^\{tensor n} the Situation equips the canonical morphism with: theta of Tag 01NK at psi the identity of Gamma\_*(X, L), along f = r\_\{L,psi}, multiplicative and unital, on the source U(psi) of r\_\{L,psi}; in the Situation U(psi) = X and r\_\{L,psi} is the canonical morphism of Tag 01PZ, which is coveringOpen\_eq\_top\_and\_ι\_comp\_projHomOfIsAmple”.

> **The `ℤ`-graded `𝒪_X`-algebra map `⨁ f^*𝒪_Y(n) ⟶ ⨁ L^{⊗ n}` of Situation
> [Stacks, Tag 01QH]**: `projTheta`, i.e. `θ` of [Stacks, Tag 01NK] at `ψ` the identity map of
> `Γ_*(X, L)`, taken along `f = r_{L, ψ}`, together with its preservation of the unit
> (`Stacks.AlgebraicGeometry.ProjChartGradedTriple.theta_map_one`). Its degreewise components are
> the maps of clause (2) of [Stacks, Tag 01PZ] and its `map_mul` is their compatibility with the
> multiplication maps.
>
> It is stated on the source `U(ψ) = ⋃_a X_a` of `r_{L, ψ}`, with no hypothesis on `L`. In the
> Situation, where `L` is ample, `U(ψ)` is all of `X` and `r_{L, ψ}` is the canonical morphism
> `f : X ⟶ Proj S` of [Stacks, Tag 01PZ] restricted to it:
> `Stacks.SectionRingProjMorphism.Theta.coveringOpen_eq_top_and_ι_comp_projHomOfIsAmple`.

```lean
def projThetaUnital : SheafOfModules.GradedAlgebra.UnitalHom
    (Stacks.Conormal.gradedPullback (canonicalSections L).glued
      (Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebra (grading L)))
    (laurentRestrict (grading L) (canonicalSections L))
```

**`Stacks.SectionRingProjMorphism.Theta.coveringOpen_eq_top_and_ι_comp_projHomOfIsAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L190). The attribute's comment: “the canonical morphism of the Situation: for L ample, U(psi) = X and r\_\{L,psi} = (U(psi) -> X) followed by the canonical morphism f : X -> Proj S of Tag 01PZ, so projThetaUnital is the graded algebra map along f”.

> **In Situation [Stacks, Tag 01QH] the map `θ` lives on all of `X` and along the canonical
> morphism**: for `L` ample, the source `U(ψ) = ⋃_a X_a` of `r_{L, ψ}` (at `ψ` the identity of
> `Γ_*(X, L)`) is all of `X`, and `r_{L, ψ}` is the inclusion `U(ψ) ⟶ X` followed by the canonical
> morphism `f : X ⟶ Proj S` of [Stacks, Tag 01PZ]. So `projThetaUnital` is the Situation's map
> `⨁ f^*𝒪_Y(n) ⟶ ⨁ L^{⊗ n}`.

```lean
theorem coveringOpen_eq_top_and_ι_comp_projHomOfIsAmple (hL : Stacks.Ample.IsAmple X L) :
    (canonicalSections L).coveringOpen = ⊤ ∧
      (canonicalSections L).coveringOpen.ι ≫ Stacks.SectionRingProjMorphism.projHomOfIsAmple L hL
        = (canonicalSections L).glued
```

## Tag 01QI, a lemma

[Tag 01QI](https://stacks.math.columbia.edu/tag/01QI) in the Stacks Project.

**`Stacks.SectionRingProjGoodOpen.projHomOfIsAmple_preimage_whereInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjGoodOpen/Basic.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjGoodOpen/Basic.lean#L163). The attribute's comment: “the canonical morphism lands in the good open W₁”.

> **Stacks Tag 01QI, first claim: the canonical morphism of Stacks Tag 01PZ maps `X` into the
> good open `W_1`.** In the situation of Stacks Tag 01QH — `L` ample on `X`, `S = Γ_*(X, L)`,
> `Y = Proj S` — the morphism `f : X ⟶ Y` of Stacks Tag 01PZ pulls the open `W_1 ⊆ Y` of Stacks
> Tag 01MU back to all of `X`.
>
> The proof is pointwise. Stacks Tag 01MU's identity
> `Stacks.AlgebraicGeometry.GoodOpenClose.whereInvertible_eq_ratioLocus` turns `W_1` into the union
> of the standard opens `D₊(a b)` with `deg a = deg b + 1`; ampleness provides at each point a pair
> of homogeneous sections of consecutive degrees `e + 1` and `e` not vanishing there
> (`Stacks.SectionRingProjGoodOpen.exists_consecutive_mem_nvLocus`); their product is a homogeneous
> element of degree `(e + 1) + e` not vanishing there
> (`Stacks.AmpleFiniteAvoidance.nvLocus_mul`); and clause (1) of Stacks Tag 01PZ
> (`Stacks.SectionRingProjMorphism.projHomOfIsAmple_preimage_projBasicOpen`) identifies the
> preimage of `D₊` of that product with the nonvanishing open, which therefore contains the
> point.

```lean
public theorem projHomOfIsAmple_preimage_whereInvertible (hL : Stacks.Ample.IsAmple X L) :
    Stacks.SectionRingProjMorphism.projHomOfIsAmple L hL ⁻¹ᵁ
        Stacks.AlgebraicGeometry.ProjInvertibleLocus.whereInvertible (grading L) 1 = ⊤
```

**`Stacks.SectionRingProjTwistIso.isIso_projTheta_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTwistIso/Basic.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjTwistIso/Basic.lean#L522). The attribute's comment: “second claim: the maps f^*O\_Y(n) -> L^\{tensor n} of clause (2) of Tag 01PZ are isomorphisms for every n in Z, positive, zero and negative”.

> **The second claim of Stacks Tag 01QI: the maps `f^*𝒪_Y(n) ⟶ L^{⊗ n}` are isomorphisms for
> every `n : ℤ`.** In Situation Stacks Tag 01QH — `X` a scheme, `L` an ample invertible
> `𝒪_X`-module, `S = Γ_*(X, L)`, `Y = Proj S` and `f : X ⟶ Y` the canonical morphism of Stacks Tag
> 01PZ — these maps are the components of clause (2) of that tag
> (`Stacks.SectionRingProjMorphism.Theta.projTheta`), and every one of them, in every integer
> degree, is an isomorphism.
>
> Both sides are invertible modules on `U(ψ) = ⋃_a X_a` in every degree: the target by Stacks Tag
> 01CU, the source because the *first* claim of Stacks Tag 01QI puts the image of `f` in the good
> open `W₁` of Stacks Tag 01MU, where `𝒪_Y(n)` is invertible
> (`isInvertibleModule_pullback_twistM`). So `isIso_theta_app_of_epi` reduces the claim to `θ_n`
> being an epimorphism, which is `epi_projTheta_app_int`.

```lean
theorem isIso_projTheta_app (hL : Stacks.Ample.IsAmple X L) (n : ℤ) :
    IsIso ((projTheta L).app n)
```

**`Stacks.SectionRingVeroneseChart.isIso_twistComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean#L270). The attribute's comment: “the second claim: the maps f^*O\_Y(n) -> L^\{(x)n} are all isomorphisms, in every integer degree. The first claim, that the canonical morphism maps X into W\_1, is Stacks.SectionRingProjGoodOpen.projHomOfIsAmple\_preimage\_whereInvertible”.

> **The second claim of Stacks Tag 01QI: the maps `f^*𝒪_Y(n) → 𝓛^{⊗ n}` are all
> isomorphisms.**

```lean
theorem isIso_twistComparison (hL : Stacks.Ample.IsAmple X L) (n : ℤ) :
    IsIso (twistComparison L hL n)
```

## Tag 01QJ, a lemma

[Tag 01QJ](https://stacks.math.columbia.edu/tag/01QJ) in the Stacks Project.

**`Stacks.SectionRingProjQuasicoherent.pullbackTildeComparison_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Isomorphism.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Isomorphism.lean#L328). The attribute's comment: “the comparison `f^*M̃ ⟶ ℱ`, `M = Γ_*(X, L, ℱ)`, is natural in `ℱ`, an isomorphism for every quasi-coherent `ℱ`, and the identity on `M_0 ⟶ Γ(Proj S, M̃) ⟶ Γ(X, ℱ)`”.

> **Stacks Tag 01QJ.** In Situation 01QH — `X` a scheme, `L` an ample invertible `𝒪_X`-module,
> `S = Γ_*(X, L)` and `f : X ⟶ Proj S` the canonical morphism of Tag 01PZ — the comparison
> `pullbackTildeComparison : f^* M̃ ⟶ ℱ`, `M = Γ_*(X, L, ℱ)`, is a natural transformation in `ℱ`
> (functoriality), it is an isomorphism for every quasi-coherent `ℱ`, and
> `M_0 ⟶ Γ(Proj S, M̃) ⟶ Γ(X, ℱ)` is the identity.
>
> The comparison is the transpose across `f^* ⊣ f_*` of the family `M̃ ⟶ f_* ℱ` constructed as
> `Stacks.SectionRingProjQuasicoherent.tildeToPushforward`; read through the binder form
> `Stacks.SectionRingProjQuasicoherent.pullbackComparison`, this is
> `Stacks.SectionRingProjQuasicoherent.pullbackComparison_tildeToPushforward`.

```lean
theorem pullbackTildeComparison_spec :
    (∀ (F : X.Modules) [F.IsQuasicoherent], IsIso ((pullbackTildeComparison L hL).app F)) ∧
      ∀ (F : X.Modules) (t : twistSections F L 0),
        ((pullbackTildeComparison L hL).app F).app (projHomOfIsAmple L hL ⁻¹ᵁ ⊤)
            (Stacks.Tag01VSPullbackTensor.modulesPullbackUnit (projHomOfIsAmple L hL)
              ((tildeFunctor L).obj F) ⊤
              (Stacks.AlgebraicGeometry.ProjStalkGlobalSections.degreeZeroToGlobalSections
                (grading L) (Stacks.TwistedSections.moduleGrading F L) (degreeZeroElem L F t))) =
          F.presheaf.map (homOfLE le_top).op (globalSection X F t)
```

## Tag 01QK, a remark

[Tag 01QK](https://stacks.math.columbia.edu/tag/01QK) in the Stacks Project.

**`Stacks.SectionRingProjTheta.projTheta_app_eq_twistThetaInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkNormalization.lean, line 760](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkNormalization.lean#L760). The attribute's comment: “assertion (i), with no extra hypothesis: the isomorphism f^*O\_Y(n) -> L^n of Tag 01QI (the degree-n component of clause (2) of Tag 01PZ, defined on U(psi)) equals theta\_\{L^n}, theta being the constructed comparison pullbackTildeComparison of Tag 01QJ read on f^*O\_Y(n) through the obvious identification O\_Y(n) = (Gamma\_*(X, L, L^n))~, for every integer n”.

> In Situation Stacks Tag 01QH, the map `f^*𝒪_Y(n) ⟶ 𝓛^{⊗ n}` of Stacks Tag 01QI — the
> degree-`n` component of clause (2) of Stacks Tag 01PZ, `projTheta`, which lives on
> `U(ψ) = ⋃_a X_a` — is `θ_{𝓛^{⊗ n}}`: Tag 01QJ's comparison for `𝓛^{⊗ n}`, read on `f^*𝒪_Y(n)`
> through the obvious identification `𝒪_Y(n) ≅ (Γ_*(X, 𝓛, 𝓛^{⊗ n}))~` (`twistThetaInt`), for every
> integer `n`. Since `projTheta` lives on `U(ψ)`, the right side is `θ_{𝓛^{⊗ n}}` pulled back along
> the inclusion `U(ψ) ⟶ X`, with `r_{L, ψ} : U(ψ) ⟶ Y` identified with `U(ψ) ⟶ X ⟶ Y` and the
> pullback along an open immersion with the restriction.

```lean
theorem projTheta_app_eq_twistThetaInt (n : ℤ) :
    (Stacks.SectionRingProjMorphism.Theta.projTheta L).app n =
      ((Scheme.Modules.pullbackCongr (ι_comp_projHom_eq_glued L hL)).inv.app (twistY L n) ≫
    (Scheme.Modules.pullbackComp (canonicalSections L).coveringOpen.ι
      (projHomOfIsAmple L hL)).inv.app (twistY L n) ≫
    (Scheme.Modules.pullback (canonicalSections L).coveringOpen.ι).map (twistThetaInt L hL n) ≫
    (Scheme.Modules.restrictFunctorIsoPullback (canonicalSections L).coveringOpen.ι).inv.app
      (tensorPowerModule X L n))
```

**`Stacks.SectionRingProjTheta.twistSquareInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkSquareInt.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkSquareInt.lean#L737). The attribute's comment: “assertion (ii), with no extra hypothesis: the square commutes -- theta\_F (x) theta\_\{L^n} is the pullback of the multiplication of Equation 01MQ followed by theta\_\{F (x) L^n}, read through the obvious identification M(n) = Gamma\_*(X, L, F (x) L^n), for every O\_X-module F and every integer n, theta being the constructed comparison pullbackTildeComparison of Tag 01QJ, so no compatibility of a binder family is assumed (contrast pullbackComparison\_tensorHom)”.

> **The twist square commutes**, for every `𝒪_X`-module `𝓕` and every integer `n`:
> `θ_𝓕 ⊗ θ_{𝓛^{⊗ n}}` is the pullback of the multiplication `M̃ ⊗ 𝒪_Y(n) ⟶ M(n)~` of Equation 01MQ
> (`twistTop`) followed by `θ_{𝓕 ⊗ 𝓛^{⊗ n}}`, read through `twistModuleIdent`.

```lean
theorem twistSquareInt (F : X.Modules) (n : ℤ) :
    ((pullbackTildeComparison L hL).app F ⊗ₘ twistThetaInt L hL n) =
      twistTop L hL F n ≫
        (Scheme.Modules.pullback (projHomOfIsAmple L hL)).map (twistModuleIdent L F n).hom ≫
        (pullbackTildeComparison L hL).app (F ⊗ tensorPowerModule X L n)
```

## Tag 0AG5, a lemma

[Tag 0AG5](https://stacks.math.columbia.edu/tag/0AG5) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistComparisonCompact.isIso_integerComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean#L412). The attribute's comment: “the comparison `M̃ ⟶ ℱ` of Tag 0B5I is an isomorphism, for `Proj S` quasi-compact and `ℱ` quasi-coherent”. References: EGA II (8.14.8), “special case”.

> **[Stacks, Tag 0AG5].** Let `S` be a graded ring such that `X = Proj S` is quasi-compact and
> let `ℱ` be a quasi-coherent `𝒪_X`-module.  Set `M = ⨁_{n ∈ ℤ} Γ(X, ℱ(n))`, the graded
> `S`-module of Section 01MM with its canonical graded module structure
> `Stacks.AlgebraicGeometry.ProjTwistedSections.twistedGlobalSectionsModule` of Tag 03GK.  Then
> the comparison map `M̃ ⟶ ℱ` of Tag 0B5I is an isomorphism.
>
> This is `isIso_integerComparison_of_compactSpace` at the canonical graded module structure, so
> nothing is quantified over beyond the graded ring and the sheaf: the hypotheses are exactly the
> source's, quasi-compactness of `Proj S` and quasi-coherence of `ℱ`.

```lean
public theorem isIso_integerComparison
    [CompactSpace (_root_.AlgebraicGeometry.Proj 𝒮)]
    (hqc : SheafOfModules.IsQuasicoherent
      (R := (_root_.AlgebraicGeometry.Proj 𝒮).ringCatSheaf) F) :
    IsIso (ProjTwistIntegerComparison.integerComparison 𝒮 F
      (ProjTwistedSections.twistedGlobalSectionsModule 𝒮 F))
```

**`Stacks.AlgebraicGeometry.ProjTwistComparisonCompact.twistSheafMap_integerComparison_degreeNToTwistedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean, line 778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean#L778). The attribute's comment: “part (2): if `Proj S` is covered by the standard opens `D₊(f)` with `deg f = 1` then the induced maps `M_n → Γ(X, ℱ(n))` are the identity maps”.

> **[Stacks, Tag 0AG5], second assertion**, for the canonical graded module structure of
> Tag 03GK: if `Proj S` is covered by the standard opens of the degree-one elements then the
> induced maps `M_n → Γ(X, ℱ(n))` are the identity maps.
>
> This is `twistSheafMap_integerComparison_degreeNToTwistedGlobalSections_of_module` at the
> canonical graded module structure
> `Stacks.AlgebraicGeometry.ProjTwistedSections.twistedGlobalSectionsModule`, so nothing is
> quantified over beyond the graded ring, the sheaf and the source's own hypotheses.

```lean
public theorem twistSheafMap_integerComparison_degreeNToTwistedGlobalSections
    [CompactSpace (_root_.AlgebraicGeometry.Proj 𝒮)]
    (hqc : SheafOfModules.IsQuasicoherent
      (R := (_root_.AlgebraicGeometry.Proj 𝒮).ringCatSheaf) F)
    (hcover : DegreeOneCover 𝒮) (n : ℤ) (s : twistedSectionsComponent 𝒮 F n) :
    letI := (ProjTwistedSections.twistedGlobalSectionsModule 𝒮 F).moduleInst
    letI := (ProjTwistedSections.twistedGlobalSectionsModule 𝒮 F).gradedSMul
    (twistSheafMap 𝒮
          (integerComparison 𝒮 F (ProjTwistedSections.twistedGlobalSectionsModule 𝒮 F))
          n).val.app (op ⊤)
        (degreeNToTwistedGlobalSections 𝒮 (twistedGlobalSectionsGrading 𝒮 F) hcover n
          (ofTwistedSection 𝒮 F n s)) = s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.29, Tag 01QG](https://stacks.math.columbia.edu/tag/01QG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
