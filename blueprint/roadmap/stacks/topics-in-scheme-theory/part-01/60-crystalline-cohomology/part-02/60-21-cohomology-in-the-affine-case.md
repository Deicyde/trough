---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.wholeSpaceSystemDerivedIso, Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07LF, Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairDeRhamDerivedPlusIso, Crystalline.GlobalCrystallineSituation.SmallSite.smoothPresentationPairDerivedPlusIso
statement: formalized
proof: formalized
---

# 60.21 Cohomology in the affine case

Section 60.21 of the Stacks Project, [Tag 07LE](https://stacks.math.columbia.edu/tag/07LE). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07JN, a proposition

[Tag 07JN](https://stacks.math.columbia.edu/tag/07JN) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.wholeSpaceSystemDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/WholeSpaceSystemDerived.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/WholeSpaceSystemDerived.lean#L226). The attribute's comment: “the complex M(0) → M(1) → M(2) → ⋯ of the system (X, T(n)\_e, δ(n)) computes RΓ(Cris(X/S), F): an isomorphism M(•) ≅ RΓ(Cris(X/S), F) in D⁺(Ab), the Čech comparison through an injective resolution, for F locally quasi-coherent with c\_f locally surjective along closed immersions, X and S affine”.

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

**`Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07LF`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LevelFormsCosimplicialIso.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LevelFormsCosimplicialIso.lean#L486). The attribute's comment: “the vanishing of the cohomology of F ⊗ Ω^i for i > 0, X and S affine”.

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

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairDeRhamDerivedPlusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalDeRhamDerived07LG.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalDeRhamDerived07LG.lean#L133). The attribute's comment: “for any surjective polynomial presentation A[x\_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (by default the tautological one): an isomorphism M ⊗^∧\_D Ω*\_D ≅ RΓ(Cris(X/S), F) in D⁺(Ab), through the double complex M(b) ⊗^∧\_\{D(b)} Ω^a\_\{D(b)} and the comparison of 07JN, for F a crystal in quasi-coherent modules and (M, ∇) its module with connection”.

> **[Stacks, Proposition 60.21.3, Tag 07LG]: the complex `M ⊗^∧_D Ω^*_D` computes
> `RΓ(Cris(X/S), ℱ)`**, as an isomorphism in the bounded below derived category `D⁺(Ab)`:
>
> `M ⊗^∧_D Ω^*_D ≅ RΓ(Cris(X/S), ℱ)`.
>
> The situation is that of [Stacks, Proposition 60.20.1, Tag 07JN]: `X` and `S` affine, `p`
> nilpotent on `X`, and `D` the completed envelope of a surjective polynomial presentation
> `A[x_i : i ∈ ι] → C`, supplied as the instance `...SmallSite.WholeSpacePresentation S hp`, by
> default the tautological one.  `ℱ` is a crystal in quasi-coherent `𝒪_{X/S}`-modules and `(M, ∇)`
> the module with connection over `D` corresponding to it under [Stacks, Lemma 60.17.3, Tag 07JG]
> (`...SmallSite.crystalPairFunctor`); the complex `M ⊗^∧_D Ω^*_D` is
> `...SmallSite.crystalPairDeRhamComplex`, lifted to the universe of the abelian sheaves on
> `Cris(X/S)` and extended by zero to `ℤ`, and `RΓ(Cris(X/S), -)` is
> `...SmallSite.derivedGlobalSections`, the right derived functor of global sections.  Read in
> `D(Ab)` it is `...SmallSite.crystalPairDeRhamDerivedIso`, the comparison of the proof.

```lean
def crystalPairDeRhamDerivedPlusIso :
    DerivedCategory.Plus.Q.obj
        (Stacks.Cohomology.extendPlusObj
          ((AddCommGrpCat.uliftFunctor.{u + 1, u}.mapHomologicalComplex (ComplexShape.up ℕ)).obj
            (crystalPairDeRhamComplex hp Fc))) ≅
      (derivedGlobalSections S).obj (abelianSheaf Fc.obj)
```

## Tag 07LH, a lemma

[Tag 07LH](https://stacks.math.columbia.edu/tag/07LH) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.smoothPresentationPairDerivedPlusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothPresentationDerived07LH.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothPresentationDerived07LH.lean#L171). The attribute's comment: “for A -> P' smooth and P' -> C surjective, D' the p-adically completed divided power envelope and (M', nabla') the pair over D' corresponding to F (the base change of the pair of 07JG, for any polynomial presentation A[x\_i] -> C of the system with a variable (WholeSpacePresentation S hp, by default the tautological one), along any augmentation-compatible divided power map D -> D'), the complex M' ⊗^∧\_\{D'} Ω*\_\{D'} computes RΓ(Cris(X/S), F): an isomorphism M' ⊗^∧\_\{D'} Ω*\_\{D'} ≅ RΓ(Cris(X/S), F) in D⁺(Ab), the base change to D inverted followed by 07LG in the derived category”.

> **[Stacks, Lemma 60.21.4, Tag 07LH]**: in the situation of
> [Stacks, Proposition 60.21.3, Tag 07LG] (`X` and `S` affine, `p` nilpotent on `X`), let `ℱ` be a
> crystal in quasi-coherent `𝒪_{X/S}`-modules, `A → P' → C` ring maps with `A → P'` smooth and
> `P' → C` surjective with kernel `J'`, `D'` the `p`-adic completion of `D_{P', γ}(J')` and
> `(M', ∇')` the pair over `D'` corresponding to `ℱ` (`...SmallSite.smoothPresentationPair`): the
> base change of the pair `(M, ∇)` of `ℱ` along any divided power `A`-algebra map `a : D → D'`
> compatible with the augmentations to `C` (one exists, `Crystalline.exists_smoothPresentationMap`).
> Here `D` is the completed envelope of the presentation `A[x_i : i ∈ ι] → C` of the system, any one
> with a variable (the instance `...SmallSite.WholeSpacePresentation S hp`, by default the
> tautological `A[x_c : c ∈ C] → C`).  Then the complex `M' ⊗^∧_{D'} Ω^*_{D'}` computes
> `RΓ(Cris(X/S), ℱ)`: there is an isomorphism
>
> `M' ⊗^∧_{D'} Ω^*_{D'} ≅ RΓ(Cris(X/S), ℱ)`
>
> in the bounded below derived category `D⁺(Ab)`, the complex lifted to the universe of the
> abelian sheaves on `Cris(X/S)` and extended by zero to `ℤ`, and `RΓ(Cris(X/S), -)` being
> `...SmallSite.derivedGlobalSections`, the right derived functor of global sections.  Read in
> `D(Ab)` it is `...SmallSite.smoothPresentationPairDerivedIso`: the base change
> `M ⊗^∧_D Ω^*_D → M' ⊗^∧_{D'} Ω^*_{D'}` inverted, followed by [Stacks, Tag 07LG].

```lean
def smoothPresentationPairDerivedPlusIso :
    DerivedCategory.Plus.Q.obj (Stacks.Cohomology.extendPlusObj
        ((AddCommGrpCat.uliftFunctor.{u + 1, u}.mapHomologicalComplex (ComplexShape.up ℕ)).obj
          (smoothPresentationPair hp Fc f' hf' a ha).complex)) ≅
      (derivedGlobalSections S).obj (abelianSheaf Fc.obj)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.21, Tag 07LE](https://stacks.math.columbia.edu/tag/07LE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
