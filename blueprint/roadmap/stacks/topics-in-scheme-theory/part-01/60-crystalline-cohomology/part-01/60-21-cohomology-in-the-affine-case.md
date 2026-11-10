---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.wholeSpaceSystemDerivedIso, Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07LF, Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairDeRhamComplex_computesCohomology, Crystalline.GlobalCrystallineSituation.SmallSite.crystalRetractPair_computesCohomology, Crystalline.GlobalCrystallineSituation.SmallSite.smoothPresentationPair_computesCohomology
statement: formalized
proof: formalized
---

# 60.21 Cohomology in the affine case

Section 60.21 of the Stacks Project, [Tag 07LE](https://stacks.math.columbia.edu/tag/07LE). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07JN, a proposition

[Tag 07JN](https://stacks.math.columbia.edu/tag/07JN) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.wholeSpaceSystemDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/WholeSpaceSystemDerived.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/WholeSpaceSystemDerived.lean#L226). The attribute's comment: “the complex M(0) → M(1) → M(2) → ⋯ of the system (X, T(n)_e, δ(n)) computes RΓ(Cris(X/S), F): an isomorphism M(•) ≅ RΓ(Cris(X/S), F) in D⁺(Ab), the Čech comparison through an injective resolution, for F locally quasi-coherent with c_f locally surjective along closed immersions, X and S affine”.

> **[Stacks, Proposition 60.20.1, Tag 07JN]: the complex `M(0) → M(1) → M(2) → ⋯` computes
> `RΓ(Cris(X/S), F)`**, as an isomorphism in the bounded below derived category `D⁺(Ab)`:
>
> `M(•) ≅ RΓ(Cris(X/S), F)`,
>
> for a sheaf `F` of `𝒪_{X/S}`-modules on `Cris(X/S)`, over an affine situation (`X` and `S`
> affine, `p` nilpotent on `Γ(X, ⊤)`), satisfying the two hypotheses of the tag:
>
> 1. `F` is locally quasi-coherent, and
> 2. for every morphism of `Cris(X/S)` whose map of ambient schemes is a closed immersion, the
>    comparison map `c_f` is locally surjective.
>
> Here `M(n) = lim_e Γ((X, T(n)_e, δ(n)), F)` for the system `(X, T(n)_e, δ(n))` of the proof
> (`...SmallSite.wholeSpaceSystem`, built from the presentation of the
> `...SmallSite.WholeSpacePresentation` instance), the complex being extended by zero to `ℤ`, and
> `RΓ(Cris(X/S), -)` is `...SmallSite.derivedGlobalSections`, the right derived functor of global
> sections.  The isomorphism is the canonical comparison of the proof: the Čech zigzag
> `M(•) ⟶ Tot(lim_e I^•(T(•)_e)) ⟵ Γ(Cris(X/S), I^•)` through the Čech double complex of an
> injective resolution `I^•` of `F` (`...SmallSite.wholeSpaceSystemDerivedIsoOfAbelian_hom`).
> Hypothesis (1) gives the vanishing of [Stacks, Tag 07JJ] at the objects of the system, and (1) and
> (2) the surjectivity of the restrictions along its towers; these are what make both arrows of the
> zigzag quasi-isomorphisms.

```lean
def wholeSpaceSystemDerivedIso :
    DerivedCategory.Plus.Q.obj
        (Stacks.Cohomology.extendPlusObj
          (sectionsComplex (wholeSpaceSystem S hp) (abelianSheaf F).obj)) ≅
      (derivedGlobalSections S).obj (abelianSheaf F)
```

## Tag 07LF, a lemma

[Tag 07LF](https://stacks.math.columbia.edu/tag/07LF) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07LF`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LevelFormsCosimplicialIso.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LevelFormsCosimplicialIso.lean#L390). The attribute's comment: “the vanishing of the cohomology of F ⊗ Ω^i for i > 0, X and S affine”.

> **[Stacks, Lemma 60.19.3, Tag 07LF].**  Let `(p, (S, I, γ), X)` be a global crystalline
> situation with `X` and `S` affine, and let `F` be a sheaf of `𝒪_{X/S}`-modules on the small
> crystalline site which is locally quasi-coherent and whose comparison morphisms along closed
> immersions are surjective — the two hypotheses of [Stacks, Tag 07JN].  Then
>
> `H^j(Cris(X/S), F ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0`  for every `i > 0` and every `j ≥ 0`.
>
> The proof is the source's own.  `...SmallSite.vanishing07LF_of_levelCosimplicialSectionsIso`
> reduces the statement to the existence, at every `p`-adic level `e`, of a cosimplicial
> `D(*)`-module `L_*` and an isomorphism `M(•)_e ≅ L_* ⊗_{D(*)} ⋀^i Ω_{D(*)}` of cosimplicial
> abelian groups with the tensor product **uncompleted**; `L_*` is
> `...SmallSite.levelSectionsCosimplicialModule` and the isomorphism is
> `...SmallSite.levelCosimplicialSectionsFormsIso`.

```lean
theorem vanishing07LF (S : GlobalCrystallineSituation.{u}) : Vanishing07LF S
```

## Tag 07LG, a proposition

[Tag 07LG](https://stacks.math.columbia.edu/tag/07LG) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairDeRhamComplex_computesCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalDeRhamComputesCohomology.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalDeRhamComputesCohomology.lean#L90). The attribute's comment: “for any surjective polynomial presentation g : A[x_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (the default instance is the tautological one): the complex M ⊗^∧_D Ω*_D of the pair (M, ∇) of a crystal in quasi-coherent modules computes RΓ(Cris(X/S), F): its cohomology in every degree j is H^j(Cris(X/S), F)”.

> **[Stacks, Proposition 60.21.3, Tag 07LG]**: in the situation of
> [Stacks, Proposition 60.20.1, Tag 07JN] (`X` and `S` affine, `p` nilpotent on `X`, and `D` the
> completed envelope of any surjective polynomial presentation `A[x_i : i ∈ ι] → C`, supplied as the
> instance `...SmallSite.WholeSpacePresentation S hp`, by default the tautological one), let `ℱ` be a
> crystal in quasi-coherent `𝒪_{X/S}`-modules and `(M, ∇)` the module with connection over `D`
> corresponding to it under [Stacks, Lemma 60.17.3, Tag 07JG] (`...SmallSite.crystalPairFunctor`).
> Then the complex `M ⊗^∧_D Ω^*_D` (`...SmallSite.crystalPairDeRhamComplex`) computes
> `RΓ(Cris(X/S), ℱ)`: for every `j`, `H^j(M ⊗^∧_D Ω^*_D) ≅ H^j(Cris(X/S), ℱ)`
> (`...SmallSite.crystalPairDeRhamCohomologyIso`).

```lean
theorem crystalPairDeRhamComplex_computesCohomology :
    ∀ j : ℕ, Nonempty (AddCommGrpCat.uliftFunctor.{u + 1, u}.obj
        ((crystalPairDeRhamComplex hp Fc).homology j) ≅
      (cohomologyFunctor S j).obj (abelianSheaf Fc.obj))
```

## Tag 07LH, a lemma

[Tag 07LH](https://stacks.math.columbia.edu/tag/07LH) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalRetractPair_computesCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalRetractPairCohomology07LH.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalRetractPairCohomology07LH.lean#L456). The attribute's comment: “in 07L5's reading: for A -> P' smooth and P' -> C surjective, D' the p-adically completed divided power envelope, the data A[x_i] ->> P' -> C of 07L5 presenting the system, a retract a : D -> D', b : D' -> D of 07L5 compatible with the augmentations, and (M', nabla') the pair over D' of 07L5 corresponding to F (crystalRetractPairFunctor), the complex M' ⊗^∧_{D'} Ω*_{D'} (crystalRetractConnModule: module M', connection nabla' read in the completed one-forms of the envelope of P') computes RΓ(Cris(X/S), F): its cohomology in every degree j is H^j(Cris(X/S), F)”.

> **[Stacks, Lemma 60.21.4, Tag 07LH], for the pair of [Stacks, Lemma 60.17.5, Tag 07L5]**:
> in the situation of [Stacks, Proposition 60.21.3, Tag 07LG] (`X` and `S` affine, `p` nilpotent on
> `X`), let `ℱ` be a crystal in quasi-coherent `𝒪_{X/S}`-modules, `A → P' → C` ring maps with
> `A → P'` smooth and `P' → C` surjective, `D'` the `p`-adic completion of `D_{P', γ}(J')`,
> `P = A[x_i] → P' → C` the data of [Stacks, Tag 07L5] (`q : P ↠ P'`, the composite being the
> presentation of the system), `a : D → D'`, `b : D' → D` a retract of [Stacks, Tag 07L5] compatible
> with the augmentations, and
> `(M', ∇') = (crystalRetractPairFunctor hp D' a b ha hb hab hρ).obj ℱ` the pair over `D'`
> corresponding to `ℱ` (the base change along `a` of the pair of [Stacks, Tag 07JG]).  Then the
> complex `M' ⊗^∧_{D'} Ω^*_{D'}` computes `RΓ(Cris(X/S), ℱ)`: the module with connection
> `...SmallSite.crystalRetractConnModule` has module `M'`
> (`...SmallSite.crystalRetractConnModule_carrier`) and connection `∇'` read in the completed
> one-forms `Ω̂¹_{E'/A,δ}` (`...SmallSite.crystalRetractConnModule_nabla`), and the cohomology of its
> de Rham complex in every degree `j` is `H^j(Cris(X/S), ℱ)`.  Here `D` is the completed envelope of
> the presentation of the system (`...SmallSite.WholeSpacePresentation S hp`), as in
> `...SmallSite.exists_presentation_retract_crystalPairEquivalence`.

```lean
theorem crystalRetractPair_computesCohomology
    [Algebra.Smooth ((affineSituation S hp).A : Type u) P']
    (q : MvPolynomial (wholeSpaceIndex S hp) (affineSituation S hp).A →ₐ[(affineSituation S hp).A]
      P') (hq : Function.Surjective q) (hgq : f'.comp q = wholeSpacePresentation S hp)
    (haug : (completedEnvelopeAugmentation (affineSituation S hp) f' hf').comp a.toRingHom =
      completedEnvelopeAugmentation (affineSituation S hp)
        (tensorPowerPresentation (affineSituation S hp) (wholeSpacePresentation S hp) 0)
        (tensorPowerPresentation_surjective (affineSituation S hp) _
          (wholeSpacePresentation_surjective S hp) 0)) :
    ((crystalRetractConnModule hp Fc f' hf' a ha).carrier =
        ((crystalRetractPairFunctor hp _ a b ha hb hab hρ).obj Fc).carrier) ∧
      (∀ x : (crystalRetractConnModule hp Fc f' hf' a ha).carrier,
        (crystalRetractConnModule hp Fc f' hf' a ha).nabla x =
          AdicCompletion.map (pAdicIdeal (A := (presentationFormsData (affineSituation S hp)
              f').ring) (affineSituation S hp).p)
            (LinearMap.lTensor (crystalRetractConnModule hp Fc f' hf' a ha).carrier
              (retractTargetFormsEquiv hp f' hf').toLinearMap)
            (((crystalRetractPairFunctor hp _ a b ha hb hab hρ).obj Fc).nabla x)) ∧
      ∀ j : ℕ, Nonempty (AddCommGrpCat.uliftFunctor.{u + 1, u}.obj
          ((crystalRetractConnModule hp Fc f' hf' a ha).complex.homology j) ≅
        (cohomologyFunctor S j).obj (abelianSheaf Fc.obj))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.smoothPresentationPair_computesCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothPresentationCohomology07LH.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothPresentationCohomology07LH.lean#L650). The attribute's comment: “for A -> P' smooth and P' -> C surjective, D' the p-adically completed divided power envelope and (M', nabla') the pair over D' corresponding to F (the base change of the pair of 07JG, for any polynomial presentation A[x_i] -> C of the system with a variable (WholeSpacePresentation S hp, by default the tautological one), along any augmentation-compatible divided power map D -> D'), the complex M' ⊗^∧_{D'} Ω*_{D'} computes RΓ(Cris(X/S), F): its cohomology in every degree j is H^j(Cris(X/S), F)”.

> **[Stacks, Lemma 60.21.4, Tag 07LH]**: in the situation of
> [Stacks, Proposition 60.21.3, Tag 07LG] (`X` and `S` affine, `p` nilpotent on `X`), let
> `ℱ` be a crystal in quasi-coherent `𝒪_{X/S}`-modules, `A → P' → C` ring maps with `A → P'`
> smooth and `P' → C` surjective with kernel `J'`, `D'` the `p`-adic completion of
> `D_{P', γ}(J')` and `(M', ∇')` the pair over `D'` corresponding to `ℱ`: the base change of the
> pair `(M, ∇)` of `ℱ` along any divided power `A`-algebra map `a : D → D'` compatible with the
> augmentations to `C` (one exists, `Crystalline.exists_smoothPresentationMap`).  Here `D` is the
> completed envelope of the presentation `A[x_i : i ∈ ι] → C` of the system, any one with a variable
> (the instance `...SmallSite.WholeSpacePresentation S hp`, by default the tautological
> `A[x_c : c ∈ C] → C`).  Then the complex
> `M' ⊗^∧_{D'} Ω^*_{D'}` computes `RΓ(Cris(X/S), ℱ)`: its cohomology in every degree `j` is
> `H^j(Cris(X/S), ℱ)`, in the graded sense in which [Stacks, Tag 07LG] is stated
> (`...SmallSite.crystalPairDeRhamComplex_computesCohomology`).

```lean
theorem smoothPresentationPair_computesCohomology [Nonempty (wholeSpaceIndex S hp)]
    [Algebra.Smooth ((affineSituation S hp).A : Type u) P']
    (haug : (completedEnvelopeAugmentation (affineSituation S hp) f' hf').comp a.toRingHom =
      completedEnvelopeAugmentation (affineSituation S hp)
        (tensorPowerPresentation (affineSituation S hp)
          (wholeSpacePresentation S hp) 0)
        (tensorPowerPresentation_surjective (affineSituation S hp) _
          (wholeSpacePresentation_surjective S hp) 0)) :
    ∀ j : ℕ, Nonempty (AddCommGrpCat.uliftFunctor.{u + 1, u}.obj
        ((smoothPresentationPair hp Fc f' hf' a ha).complex.homology j) ≅
      (cohomologyFunctor S j).obj (abelianSheaf Fc.obj))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.21, Tag 07LE](https://stacks.math.columbia.edu/tag/07LE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
