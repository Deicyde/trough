---
declaration: section
origin: cited
lean: Stacks.SectionRingVeroneseChart.twistComparison, Stacks.SectionRingVeroneseChart.twistComparison_mul, Stacks.SectionRingVeroneseChart.pbTwistUnit_twistComparison, Stacks.SectionRingProjGoodOpen.projHomOfIsAmple_preimage_whereInvertible, Stacks.SectionRingProjTwistIso.isIso_projTheta_app, Stacks.SectionRingVeroneseChart.isIso_twistComparison, Stacks.SectionRingProjQuasicoherent.pullbackComparison, Stacks.SectionRingProjQuasicoherent.pullbackTildeComparison_spec
statement: formalized
proof: formalized
---

# 28.29 Quasi-coherent sheaves and ample invertible sheaves

Section 28.29 of the Stacks Project, [Tag 01QG](https://stacks.math.columbia.edu/tag/01QG). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01QH, a situation

[Tag 01QH](https://stacks.math.columbia.edu/tag/01QH) in the Stacks Project.

**`Stacks.SectionRingVeroneseChart.twistComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean#L256). The attribute's comment: “the Z-graded O\_X-algebra map of the Situation, degreewise in every integer degree. The rest of the Situation's claim is what makes the family a map of graded algebras rather than a family of maps, and is in two further files: multiplicativity in an arbitrary integer bidegree (n, m) is Stacks.SectionRingVeroneseChart.twistComparison\_mul in StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebra.lean, where the graded O\_X-algebra structure on the source is pbTwistMul, and unit preservation -- the extra datum of GradedAlgebra.UnitalHom -- is Stacks.SectionRingVeroneseChart.pbTwistUnit\_twistComparison in StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebraUnit.lean. The three together are the Situation's map. See the 'What is not done here' section above”.

> **Stacks Situation 01QH's map, in degree `n`**: the component
> `f^*𝒪_Y(n) ⟶ 𝓛^{⊗ n}` of the `ℤ`-graded `𝒪_X`-algebra map the Situation equips the canonical
> morphism with. It is the forward map of `twistComparisonIso`, whose degree-one value is the
> comparison that Stacks Tag 01N8's uniqueness pins.

```lean
def twistComparison (hL : Stacks.Ample.IsAmple X L) (n : ℤ) :
    pbTwist L hL n ⟶ tensorPowModule X L n
```

**`Stacks.SectionRingVeroneseChart.twistComparison_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebra.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebra.lean#L488). The attribute's comment: “multiplicativity of the Situation's map in an arbitrary integer bidegree (n, m). With the degreewise family twistComparison this makes the family a homomorphism of sheaves of Z-graded algebras here (SheafOfModules.GradedAlgebra.Hom, registered for 0FQW), which is exactly a degreewise family plus multiplicativity in every bidegree; with unit preservation (pbTwistUnit\_twistComparison, the extra datum of GradedAlgebra.UnitalHom) the three jointly give the Z-graded O\_X-algebra map the Situation equips the canonical morphism with. The graded algebra structure on the source is pbTwistMul, Tag 01MO's multiplication of the twisting sheaves pulled back along the canonical morphism of Tag 01PZ and conjugated by Tag 01CD; on the target it is Tag 01CU's addition law”.

> **Situation [Stacks, Tag 01QH]'s map is multiplicative in an arbitrary integer bidegree.**  The
> graded `𝒪_X`-algebra structure `pbTwistMul` on `⨁_{n ∈ ℤ} f^*𝒪_Y(n)`, followed by the comparison
> in the degree `n + m`, is the comparisons in the degrees `n` and `m` on the two factors, followed
> by the addition law `Stacks.Ample.tensorPowModuleAddIso` of [Stacks, Tag 01CU] for the tensor
> powers of `𝓛`.
>
> Together with the degreewise family `twistComparison` this makes the family a homomorphism of
> sheaves of `ℤ`-graded algebras in this repository (`Stacks.SheafOfModules.GradedAlgebra.Hom`,
> registered for [Stacks, Tag 0FQW]), which is exactly a degreewise family together with
> multiplicativity in every bidegree; with unit preservation
> (`Stacks.SectionRingVeroneseChart.pbTwistUnit_twistComparison`) the three are the `ℤ`-graded
> `𝒪_X`-algebra map `⨁_{n ∈ ℤ} f^*𝒪_Y(n) ⟶ ⨁_{n ∈ ℤ} 𝓛^{⊗ n}` the Situation equips the canonical
> morphism with.
>
> The proof is the pasting `twistComparison_mul_aux` of the five legs' squares, read at the
> unfolding `twistComparison_eq` of the composite.

```lean
theorem twistComparison_mul (n m : ℤ) :
    pbTwistMul L hL n m ≫ twistComparison L hL (n + m) =
      (twistComparison L hL n ⊗ₘ twistComparison L hL m) ≫
        (tensorPowModuleAddIso X L n m).hom
```

**`Stacks.SectionRingVeroneseChart.pbTwistUnit_twistComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebraUnit.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistTensor/VeroneseChartGradedAlgebraUnit.lean#L359). The attribute's comment: “unit preservation: the degree-zero component of the Situation's map carries the unit pbTwistUnit of the source graded O\_X-algebra pbTwistMul -- Tag 01MO's multiplication of the twisting sheaves pulled back along the canonical morphism of Tag 01PZ and conjugated by Tag 01CD -- to the unit of Tag 01CU's addition law for the tensor powers of L, whose degree-zero piece is O\_X by tensorPowModuleZeroIso. This is the extra datum of SheafOfModules.GradedAlgebra.UnitalHom over GradedAlgebra.Hom (both registered for 0FQW). With the degreewise family twistComparison and the bidegree square twistComparison\_mul the three jointly give the Z-graded O\_X-algebra map the Situation equips the canonical morphism with. The source unit is unique (pbTwistUnit\_eq\_of\_mul), so no choice is made”.

> **Situation [Stacks, Tag 01QH]'s map preserves the unit.**  The degree-zero component of the
> map carries the unit `pbTwistUnit` of the source graded `𝒪_X`-algebra `pbTwistMul` — the
> multiplication of the twisting sheaves of [Stacks, Tag 01MO], pulled back along the canonical
> morphism of [Stacks, Tag 01PZ] and conjugated by [Stacks, Tag 01CD] — to the unit of
> [Stacks, Tag 01CU]'s addition law for the tensor powers of `𝓛`, whose degree-zero piece is `𝒪_X`
> by `Stacks.Ample.tensorPowModuleZeroIso`.
>
> Together with the degreewise family `twistComparison` and the bidegree square
> `twistComparison_mul` this is the `ℤ`-graded `𝒪_X`-algebra map
> `⨁_{n ∈ ℤ} f^*𝒪_Y(n) ⟶ ⨁_{n ∈ ℤ} 𝓛^{⊗ n}` the Situation equips the canonical morphism with,
> including the unit datum that distinguishes `Stacks.SheafOfModules.GradedAlgebra.UnitalHom` from
> `Stacks.SheafOfModules.GradedAlgebra.Hom` (both registered for [Stacks, Tag 0FQW]).
>
> `pbTwistUnit_eq_of_mul` says the source unit is unique, so no choice is being made here.

```lean
theorem pbTwistUnit_twistComparison :
    pbTwistUnit L hL ≫ twistComparison L hL 0 = (tensorPowModuleZeroIso X L).inv
```

## Tag 01QI, a lemma

[Tag 01QI](https://stacks.math.columbia.edu/tag/01QI) in the Stacks Project.

**`Stacks.SectionRingProjGoodOpen.projHomOfIsAmple_preimage_whereInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjGoodOpen/Basic.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjGoodOpen/Basic.lean#L163). The attribute's comment: “the canonical morphism lands in the good open W₁”.

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

**`Stacks.SectionRingProjTwistIso.isIso_projTheta_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTwistIso/Basic.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTwistIso/Basic.lean#L522). The attribute's comment: “second claim: the maps f^*O\_Y(n) -> L^\{tensor n} of clause (2) of Tag 01PZ are isomorphisms for every n in Z, positive, zero and negative”.

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

**`Stacks.SectionRingVeroneseChart.isIso_twistComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingVeroneseChart/IntegerDegree.lean#L265). The attribute's comment: “the second claim: the maps f^*O\_Y(n) -> L^\{(x)n} are all isomorphisms, in every integer degree. The first claim, that the canonical morphism maps X into W\_1, is Stacks.SectionRingProjGoodOpen.projHomOfIsAmple\_preimage\_whereInvertible”.

> **The second claim of Stacks Tag 01QI: the maps `f^*𝒪_Y(n) → 𝓛^{⊗ n}` are all
> isomorphisms.**

```lean
theorem isIso_twistComparison (hL : Stacks.Ample.IsAmple X L) (n : ℤ) :
    IsIso (twistComparison L hL n)
```

## Tag 01QJ, a lemma

[Tag 01QJ](https://stacks.math.columbia.edu/tag/01QJ) in the Stacks Project.

**`Stacks.SectionRingProjQuasicoherent.pullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Comparison.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Comparison.lean#L87). The attribute's comment: “clause (b): the comparison `f^*M̃ ⟶ ℱ` is functorial in `ℱ`, carrying Tag 0B5I's morphism `M̃ ⟶ f_*ℱ` for the twisted-section module as the hypothesis `c`”.

> **Clause (b) of Stacks Tag 01QJ: the comparison `f^* M̃ ⟶ ℱ` is functorial in `ℱ`.**
>
> Stacks Tag 0B5I supplies, for each `ℱ`, a morphism `M̃ ⟶ f_* ℱ` on `Proj Γ_*(X, L)` functorial
> in `ℱ`, where `M = Γ_*(X, L, ℱ)`; that family is the hypothesis `c`. Transposing it along the
> adjunction `f^* ⊣ f_*` gives a morphism `f^* M̃ ⟶ ℱ` for each `ℱ`, and transposition is natural,
> so the transposed family is again functorial in `ℱ`.

```lean
def pullbackComparison
    (c : tildeFunctor L ⟶ Scheme.Modules.pushforward (projHomOfIsAmple L hL)) :
    pullbackTildeFunctor L hL ⟶ 𝟭 X.Modules
```

**`Stacks.SectionRingProjQuasicoherent.pullbackTildeComparison_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Isomorphism.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjQuasicoherent/Isomorphism.lean#L323). The attribute's comment: “the natural transformation `f^*M̃ ⟶ ℱ` is an isomorphism for `ℱ` quasi-coherent and is the identity on `M_0`”.

> **Stacks Tag 01QJ.** In Situation 01QH — `X` a scheme, `L` an ample invertible `𝒪_X`-module,
> `S = Γ_*(X, L)` and `f : X ⟶ Proj S` the canonical morphism of Tag 01PZ — the comparison
> `pullbackTildeComparison : f^* M̃ ⟶ ℱ`, `M = Γ_*(X, L, ℱ)`, is a natural transformation in `ℱ`
> (functoriality), it is an isomorphism for every quasi-coherent `ℱ`, and
> `M_0 ⟶ Γ(Proj S, M̃) ⟶ Γ(X, ℱ)` is the identity.

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

**`Stacks.SectionRingProjTheta.projTheta_app_eq_twistThetaInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkNormalization.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkNormalization.lean#L759). The attribute's comment: “assertion (i): the isomorphism f^*O\_Y(n) -> L^n of Tag 01QI (the degree-n component of clause (2) of Tag 01PZ, defined on U(psi)) equals theta\_\{L^n}, theta being the constructed comparison of Tag 01QJ read on f^*O\_Y(n) through the obvious identification O\_Y(n) = (Gamma\_*(X, L, L^n))~, for every integer n”.

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

**`Stacks.SectionRingProjTheta.twistSquareInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkSquareInt.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistRemarkSquareInt.lean#L736). The attribute's comment: “assertion (ii): the square commutes -- theta\_F (x) theta\_\{L^n} is the pullback of the multiplication of Equation 01MQ followed by theta\_\{F (x) L^n}, read through the obvious identification M(n) = Gamma\_*(X, L, F (x) L^n), for every O\_X-module F and every integer n, theta being the constructed comparison of Tag 01QJ”.

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

**`Stacks.SectionRingProjTheta.pullbackComparison_tensorHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistSquare.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/TwistSquare.lean#L478). The attribute's comment: “assertion (ii): the Remark's square commutes, at the Tag 01QJ comparison `pullbackComparison`, with the top arrow CONSTRUCTED as `pullbackTwistTop` — the tensorator of restriction along `f` composed with `f^*` of Equation 01MQ's multiplication map — rather than left arbitrary, which is what distinguishes this from the sibling file `TwistCompatibility`'s `not_forall_twistSquare`. Three things are granted as named binders: (a) `hmul`, the compatibility of Tag 0B5I's family `c` with that multiplication map on `Proj Γ_*(X, L)`, which is the characterisation of `c` that `not_forall_twistSquare` proves to be necessary and `add_self_eq_zero_of_mulComm_neg` proves is not stable under its perturbation; (b) the multiplication map itself as the binder `mult`, Equation 01MQ's `moduleTwistMap` being stated for the other of this repository's two tensor-product sheaves; (c) a monoidal structure on restriction along `f` as an instance binder, which Mathlib does not provide for `Scheme.Modules.restrictFunctor`. Assertion (i), that Tag 01QI's map `f^*𝒪_Y(n) → 𝓛^{⊗n}` is `θ_{𝓛^{⊗n}}`, is NOT covered: that map does not exist in this repository”.

> **Assertion (ii) of Stacks Tag 01QK, at the Tag 01QJ comparison.**
>
> With `θ = Stacks.SectionRingProjQuasicoherent.pullbackComparison L hL c`, the natural
> transformation `f^* M̃ ⟶ 𝓕` that carries `@[stacks 01QJ]`, and with the top arrow
> `Stacks.SectionRingProjTheta.pullbackTwistTop` *built* from Equation 01MQ's multiplication map
> `mult`, Stacks Tag 01QK's square commutes:
>
> ```
>     θ_𝓕 ⊗ₘ θ_𝓖 = pullbackTwistTop mult ≫ θ_{𝓕 ⊗ 𝓖}.
> ```
>
> Both lower corners of the Remark's square are the single object `𝓕 ⊗ 𝓖` and its bottom arrow is
> the identity, so this equation is the whole of assertion (ii).
>
> The hypothesis `hmul` is the compatibility of Tag 0B5I's family `c` with `mult`, on
> `Proj Γ_*(X, L)`, mentioning no `θ`. It is the characterisation of `c` that
> `Stacks.SectionRingProjQuasicoherent.TwistCompatibility.not_forall_twistSquare` proves to be
> necessary; `mulComm_of_tensorHom_eq` shows it is equivalent to the conclusion across the
> adjunction, so nothing weaker would do, and `add_self_eq_zero_of_mulComm_neg` shows it is
> destroyed by the negation of `c` that defeats an unconstrained binder.

```lean
theorem pullbackComparison_tensorHom
    (c : tildeFunctor L ⟶ Scheme.Modules.pushforward (projHomOfIsAmple L hL))
    (F G : X.Modules)
    (mult : (tildeFunctor L).obj F ⊗ (tildeFunctor L).obj G ⟶ (tildeFunctor L).obj (F ⊗ G))
    (hmul : mult ≫ c.app (F ⊗ G) = (c.app F ⊗ₘ c.app G) ≫
      μ (Scheme.Modules.pushforward (projHomOfIsAmple L hL)) F G) :
    (pullbackComparison L hL c).app F ⊗ₘ (pullbackComparison L hL c).app G
      = pullbackTwistTop L hL F G mult ≫ (pullbackComparison L hL c).app (F ⊗ G)
```

## Tag 0AG5, a lemma

[Tag 0AG5](https://stacks.math.columbia.edu/tag/0AG5) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistComparisonCompact.isIso_integerComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean#L412). The attribute's comment: “the comparison `M̃ ⟶ ℱ` of Tag 0B5I is an isomorphism, for `Proj S` quasi-compact and `ℱ` quasi-coherent”. References: EGA II (8.14.8), “special case”.

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

**`Stacks.AlgebraicGeometry.ProjTwistComparisonCompact.twistSheafMap_integerComparison_degreeNToTwistedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonCompact.lean#L778). The attribute's comment: “part (2): if `Proj S` is covered by the standard opens `D₊(f)` with `deg f = 1` then the induced maps `M_n → Γ(X, ℱ(n))` are the identity maps”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
