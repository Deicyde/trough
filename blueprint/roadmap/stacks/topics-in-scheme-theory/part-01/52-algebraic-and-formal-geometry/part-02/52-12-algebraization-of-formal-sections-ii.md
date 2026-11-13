---
declaration: section
origin: cited
lean: Stacks.Algebraization.isIso_comparisonMap_first_of_middle_and_third, Stacks.Algebraization.isIso_comparisonMap_middle_of_ends, Stacks.Algebraization.isIso_comparisonMap_of_formalSectionsHypotheses, Stacks.Algebraization.isIso_comparisonMap_iff_realized, Stacks.Algebraization.isIso_comparisonMap, Stacks.Algebraization.isIso_comparisonMap_of_associatedPointsClosureDimensionBound, Stacks.Algebraization.FormalSectionsII.globalToFormalSections_proj, Stacks.Algebraization.FormalSectionsII.isIso_globalToFormalSections
statement: formalized
proof: formalized
---

# 52.12 Algebraization of formal sections, II

Section 52.12 of the Stacks Project, [Tag 0EG1](https://stacks.math.columbia.edu/tag/0EG1). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H48, a lemma

[Tag 0H48](https://stacks.math.columbia.edu/tag/0H48) in the Stacks Project.

**`Stacks.Algebraization.isIso_comparisonMap_first_of_middle_and_third`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ComparisonShortExact.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ComparisonShortExact.lean#L281). The attribute's comment: “first comparison”.

> For a short exact sequence `0 → F' → F → F'' → 0` of
> coherent modules on `U = Spec(A) ∖ V(𝔞)` with `A` Noetherian, if the comparison maps of
> `Stacks.Algebraization.comparisonMap` for `F` and `F''` are isomorphisms, so is that for `F'`.

```lean
theorem isIso_comparisonMap_first_of_middle_and_third
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I a : Ideal A)
    (S : ShortComplex (complementZeroLocus A a : Scheme).Modules) (hS : S.ShortExact)
    [S.X₁.IsCoherent] [S.X₂.IsCoherent] [S.X₃.IsCoherent]
    (h₂ : IsIso (comparisonMap A I a S.X₂)) (h₃ : IsIso (comparisonMap A I a S.X₃)) :
    IsIso (comparisonMap A I a S.X₁)
```

**`Stacks.Algebraization.isIso_comparisonMap_middle_of_ends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ComparisonShortExactMiddle.lean, line 1037](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ComparisonShortExactMiddle.lean#L1037). The attribute's comment: “middle comparison”.

> **Stacks 0H48, the middle comparison.** For a short exact sequence `0 → F' → F → F'' → 0` of
> coherent modules on `U = Spec(A) ∖ V(𝔞)` with `A` Noetherian, if the comparison maps of
> `Stacks.Algebraization.comparisonMap` for `F'` and `F''` are isomorphisms, so is that for `F`.

```lean
theorem isIso_comparisonMap_middle_of_ends (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I a : Ideal A) (S : ShortComplex (complementZeroLocus A a : Scheme).Modules)
    (hS : S.ShortExact) [S.X₁.IsCoherent] [S.X₂.IsCoherent] [S.X₃.IsCoherent]
    (h₁ : IsIso (comparisonMap A I a S.X₁)) (h₃ : IsIso (comparisonMap A I a S.X₃)) :
    IsIso (comparisonMap A I a S.X₂)
```

## Tag 0EIF, a lemma

[Tag 0EIF](https://stacks.math.columbia.edu/tag/0EIF) in the Stacks Project.

**`Stacks.Algebraization.isIso_comparisonMap_of_formalSectionsHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationTheorem.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationTheorem.lean#L78).

> **Stacks 0EIF.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let `F` be a coherent
> module on `U = Spec(A) ∖ V(𝔞)`. Assume that `A` is `I`-adically complete and has a dualizing
> complex; that every associated point `x` of `F` outside `V(I)` whose closure meets `V(I)`
> outside `V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1` at every `z ∈ closure {x} ∩ V(𝔞)`;
> and that either `F|_{U ∖ V(I)}` satisfies `(S₁)` or the values on `V(𝔞)` of a dimension function
> on `Spec(A)` differ by at most `2` (`Stacks.Algebraization.FormalSectionsHypotheses`). Then the
> map `colim_V H⁰(V, F) ⟶ lim_n H⁰(U, F/IⁿF)`, the colimit over the opens `V ⊆ U` containing
> `U ∩ V(I)`, is an isomorphism.

```lean
public theorem isIso_comparisonMap_of_formalSectionsHypotheses {A : Type u} [CommRing A]
    [IsNoetherianRing A] (I a : Ideal A) (hIa : I ≤ a)
    (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent]
    (h : FormalSectionsHypotheses A I a F) :
    IsIso (comparisonMap A I a F)
```

**`Stacks.Algebraization.isIso_comparisonMap_iff_realized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsSerreOneAlternative.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsSerreOneAlternative.lean#L142). The attribute's comment: “REDUCED, not proved: the conclusion holds exactly when every formal section is realized on one neighbourhood. Injectivity is proved outright here; the realization half is NOT proved and NOT assumed — it is the right-hand side of this equivalence. See the coverage note”.

> The comparison map is an isomorphism exactly when every compatible family of sections of
> `F / Iⁿ F` on `U` is the comparison of a section of `F` over a single open `V ⊆ U` containing
> `U ∩ V(I)`.

```lean
public theorem isIso_comparisonMap_iff_realized [IsNoetherianRing A] [F.IsCoherent] :
    IsIso (comparisonMap A I a F) ↔
      ∀ s : ToType (limit (formalSections A I a F)),
        ∃ (V : OpensNearVanishing A I a) (t : ToType ((sectionsNearVanishing A I a F).obj V)),
          ConcreteCategory.hom (comparisonAt A I a F V) t = s
```

## Tag 0EG2, a proposition

[Tag 0EG2](https://stacks.math.columbia.edu/tag/0EG2) in the Stacks Project.

**`Stacks.Algebraization.isIso_comparisonMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AssociatedPointInductionComparison.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AssociatedPointInductionComparison.lean#L384). The attribute's comment: “the third condition of Stacks 0EIF removed, by induction on the associated points off V(I). Carried, each in its own generality and none of them this conclusion: Stacks 0EIF (SerreOneAlternativeComparison), the middle clause of Stacks 0H48 (MiddleComparisonOfShortExact), and the short exact sequence the source builds from Stacks 0BK0, 0DX3 and 0AW0 (AssociatedPointSplitting, in which no comparison map occurs). Proved here: the induction, the base case, and the descent of the measure and of conditions (1) and (2) to a submodule”.

> **Stacks 0EG2.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let `F` be a coherent
> module on `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex, and
> 2. whenever `x` is an associated point of `F` outside `V(I)` whose closure meets `V(I)` outside
>    `V(𝔞)`, every `z ∈ closure {x} ∩ V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1`.
>
> Then the comparison map `Stacks.Algebraization.comparisonMap A I 𝔞 F`, from the sections of `F`
> on arbitrarily small open neighbourhoods of `U ∩ V(I)` to the compatible families of sections of
> `F / Iⁿ F` on all of `U`, is an isomorphism.
>
> The source's third condition, present in Stacks 0EIF, is absent here; that is the whole content
> of this proposition, and it is obtained by induction on the number of associated points of `F`
> off `V(I)` over Stacks 0EIF, the middle clause of Stacks 0H48, and the splitting the source
> assembles from Stacks 0BK0, 0DX3 and 0AW0.

```lean
public theorem isIso_comparisonMap [IsNoetherianRing A]
    (F : (complementZeroLocus A a : Scheme).Modules) [hFc : F.IsCoherent]
    (hF : BootstrapHypotheses A I a F)
    (hEIF : SerreOneAlternativeComparison.{u}) (h48 : MiddleComparisonOfShortExact.{u})
    (hsplit : AssociatedPointSplitting A I a) :
    IsIso (comparisonMap A I a F)
```

**`Stacks.Algebraization.isIso_comparisonMap_of_associatedPointsClosureDimensionBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAssociatedPointInduction.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAssociatedPointInduction.lean#L78).

> **Stacks 0EG2.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let `F` be a coherent
> module on `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex, and
> 2. whenever `x` is an associated point of `F` outside `V(I)` whose closure meets `V(I)` outside
>    `V(𝔞)`, every `z ∈ closure {x} ∩ V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1`.
>
> Then the comparison map `colim_V H⁰(V, F) ⟶ lim_n H⁰(U, F/IⁿF)`, where the colimit is over the
> opens `V ⊆ U` containing `U ∩ V(I)`, is an isomorphism.

```lean
public theorem isIso_comparisonMap_of_associatedPointsClosureDimensionBound
    {A : Type u} [CommRing A] [IsNoetherianRing A] (I a : Ideal A) (hIa : I ≤ a)
    (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent]
    (hdim : AssociatedPointsClosureDimensionBound A I a F) :
    IsIso (comparisonMap A I a F)
```

## Tag 0EIG, a lemma

[Tag 0EIG](https://stacks.math.columbia.edu/tag/0EIG) in the Stacks Project.

**`Stacks.Algebraization.FormalSectionsII.globalToFormalSections_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationII.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationII.lean#L252). The attribute's comment: “canonicality of the displayed arrow: its n-th component is reduction mod I^n”.

> **The arrow of Stacks 0EIG is canonical**: its `n`-th component is reduction modulo `Iⁿ` of
> a global section of `F` on `U`, not an arbitrary arrow into the limit.

```lean
theorem globalToFormalSections_proj (n : ℕ) :
    globalToFormalSections A I a F ≫ limit.π (formalSections A I a F) (op n) =
      (adicProj (idealSheafNearVanishing A I a) F (op n)).app ⊤
```

**`Stacks.Algebraization.FormalSectionsII.isIso_globalToFormalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationII.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsAlgebraizationII.lean#L312). The attribute's comment: “H^0(U,F) = lim H^0(U,F/I^nF); 0EG2 applied, its 3 hypotheses passed through”.

> **Stacks 0EIG.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let `F` be a coherent
> module on `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex,
> 2. whenever `x` is an associated point of `F` outside `V(I)` whose closure meets `V(I)` outside
>    `V(𝔞)`, every `z ∈ closure {x} ∩ V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1`, and
> 3. `depth(F_x) ≥ 2` for every `x ∈ U` whose closure meets `V(I)` only inside `V(𝔞)`.
>
> Then `H⁰(U, F) ⟶ lim H⁰(U, F / Iⁿ F)` is an isomorphism.
>
> What is proved here is the content of Stacks 0EIG over Stacks 0EG2: a point of `U` missed by a
> neighbourhood `V` of the formal locus has its closure meeting `V(I)` only inside `V(𝔞)`, so
> condition (3) bounds the depth of `F` below by `2` on all of `U ∖ V`, Hartogs extension for
> coherent modules — Stacks 0E9I — makes every restriction `Γ(U, F) ⟶ Γ(V, F)` an isomorphism,
> and the colimit therefore collapses onto its value at `U`.
>
> Conditions (1) and (2) are consumed only by `Stacks.Algebraization.isIso_comparisonMap`, the
> library's Stacks 0EG2, which is *applied* here: they assemble into its
> `Stacks.Algebraization.BootstrapHypotheses` on the nose. The three remaining arguments are that
> statement's own carried hypotheses, passed through unchanged and granting nothing about
> Stacks 0EIG:
>
> * `Stacks.Algebraization.SerreOneAlternativeComparison` grants Stacks 0EIF — the comparison map
>   is an isomorphism for a coherent module that additionally satisfies the third condition of
>   that lemma, the condition Stacks 0EG2 removes;
> * `Stacks.Algebraization.MiddleComparisonOfShortExact` grants the middle clause of
>   Stacks 0H48 — the middle comparison of a short exact sequence is an isomorphism once the
>   outer two are;
> * `Stacks.Algebraization.AssociatedPointSplitting` grants the short exact sequence the source
>   assembles from Stacks 0BK0, 0DX3 and 0AW0, in which no comparison map occurs at all.
>
> None of the three mentions the global sections `Γ(U, F)`, so none of them is this conclusion;
> and since they are exactly the hypotheses the library's Stacks 0EG2 already carries, this
> statement adds no assumption of its own beyond conditions (1), (2) and (3).

```lean
theorem isIso_globalToFormalSections [IsNoetherianRing A] [F.IsCoherent]
    (hIa : I ≤ a) (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdim : AssociatedPointsClosureDimensionBound A I a F)
    (hdepth : DepthTwoOffFormalLocus A I a F)
    (hEIF : SerreOneAlternativeComparison.{u}) (h48 : MiddleComparisonOfShortExact.{u})
    (hsplit : AssociatedPointSplitting A I a) :
    IsIso (globalToFormalSections A I a F)
```

**`Stacks.Algebraization.FormalSectionsII.isIso_globalToFormalSections_of_depthTwoOffFormalLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsGlobalAlgebraization.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalSectionsGlobalAlgebraization.lean#L75).

> **Stacks 0EIG.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let `F` be a coherent
> module on `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex,
> 2. whenever `x` is an associated point of `F` outside `V(I)` whose closure meets `V(I)` outside
>    `V(𝔞)`, every `z ∈ closure {x} ∩ V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1`, and
> 3. `depth(F_x) ≥ 2` for every `x ∈ U` whose closure meets `V(I)` only inside `V(𝔞)`.
>
> Then the arrow `H⁰(U, F) ⟶ lim H⁰(U, F / Iⁿ F)`, whose `n`-th component is reduction
> modulo `Iⁿ`, is an isomorphism.
>
> Conditions (1) and (2) make the comparison map of Stacks 0EG2 an isomorphism; condition (3) and
> Stacks 0E9I identify `H⁰(V, F)` with `H⁰(U, F)` for every open `V ⊆ U` containing `U ∩ V(I)`.

```lean
theorem isIso_globalToFormalSections_of_depthTwoOffFormalLocus
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I a : Ideal A)
    (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent]
    (hIa : I ≤ a) (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdim : AssociatedPointsClosureDimensionBound A I a F)
    (hdepth : DepthTwoOffFormalLocus A I a F) :
    IsIso (globalToFormalSections A I a F)
```

## Tag 0EIH, a lemma

[Tag 0EIH](https://stacks.math.columbia.edu/tag/0EIH) in the Stacks Project.

**`Stacks.Algebraization.mono_principalComparisonMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusTagInjectivity.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusTagInjectivity.lean#L219). The attribute's comment: “injectivity”.

> **Stacks 0EIH, the injectivity half.** Let `A` be a Noetherian ring, let `f ∈ A`, let
> `𝔞 ⊆ A` be an ideal and let `M` be a finite `A`-module. Then the map
>
> `colim_V Γ(V, M̃) ⟶ lim Γ(U, (M/fⁿM)~)`
>
> of the source, the colimit being over the opens `V ⊆ U = Spec(A) ∖ V(𝔞)` containing
> `U ∩ V(f)`, is a monomorphism.
>
> None of the three hypotheses of the source is needed for this half: `A` is not assumed
> `f`-adically complete, `f` is not assumed a nonzerodivisor on `M`, `H¹_𝔞(M/fM)` is not assumed
> finite, and `f` is not assumed to lie in `𝔞`.

```lean
theorem mono_principalComparisonMap (A : Type u) [CommRing A] [IsNoetherianRing A] (f : A)
    (a : Ideal A) (M : ModuleCat.{u} A) [Module.Finite A M] :
    Mono (principalComparisonMap A f a M)
```

**`Stacks.Algebraization.FormalSections.isIso_formalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalSections/Algebraization.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalSections/Algebraization.lean#L607).

> Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` be an element of an ideal of `A`, and let `M`
> be a finite `A`-module. Assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor on `M`,
> 3. `H¹_𝔞(M/fM)` is a finite `A`-module.
>
> Then, with `U = Spec(A) ∖ V(𝔞)`, the canonical map
>
> `colim_V Γ(V, M̃) ⟶ lim_n Γ(U, (M/fⁿM)~)`
>
> is an isomorphism, the colimit being over the opens `V ⊆ U` containing `U ∩ V(f)`.
>
> The map is `Stacks.Algebraization.FormalSections.formalComparison`: on a neighbourhood `V` of
> the formal locus it reduces a section of `M̃` modulo `fⁿ` and extends the result back to `U`,
> which is legitimate because `(M/fⁿM)~` vanishes on `D(f) ⊇ U ∖ V`. The quotient `M/fM` is
> written `Stacks.Algebraization.FormalSections.Quot f M 1`, which is `M` modulo the submodule
> `fM`; see `Stacks.Algebraization.FormalSections.powSmul_one`.
>
> The membership `f ∈ 𝔞` is carried but not consumed: the proof below uses only the other three
> hypotheses, so the conclusion holds for every `f` and every ideal `𝔞`.

```lean
theorem isIso_formalComparison (A : Type u) [CommRing A] [IsNoetherianRing A] (f : A)
    (a : Ideal A) (hfa : f ∈ a) (M : ModuleCat.{u} A) [Module.Finite A (M : Type u)]
    [IsAdicComplete (Ideal.span {f}) A] (hf : IsSMulRegular (M : Type u) f)
    (hH1 : Module.Finite A
      (localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a) (Quot f M 1) 1)) :
    IsIso (ModuleCat.ofHom (formalComparison A a f M))
```

## Tag 0H49, a proposition

[Tag 0H49](https://stacks.math.columbia.edu/tag/0H49) in the Stacks Project.

**`Stacks.Algebraization.isIso_comparisonMap_span_singleton_of_two_lt_closureLocalDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusAlgebraization.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusAlgebraization.lean#L260).

> **Stacks Project, Tag 0H49.** Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` and let `ℱ` be
> a coherent module on `U = Spec(A) ∖ V(𝔞)`. Assume `A` is `f`-adically complete and has a
> dualizing complex, and that whenever `x` is an associated point of `ℱ` with `f ∉ 𝔭_x`, whose
> closure meets `V(f)` outside `V(𝔞)`, and `z ∈ closure{x} ∩ V(𝔞)`, the local ring of
> `closure{x}` at `z` has dimension greater than two. Then the comparison map
>
> `colim_V Γ(V, ℱ) ⟶ lim Γ(U, ℱ / fⁿ ℱ)`
>
> is an isomorphism, the colimit being over the opens `V ⊆ U` containing `U ∩ V(f)`.
>
> The closure of `x` in `Spec(A)` is `V(𝔭_x)`, so "`closure{x} ∩ V(f) ⊄ V(𝔞)`" is the existence
> of a prime `y ⊇ 𝔭_x` with `f ∈ y` and `𝔞 ⊄ y`, and "`z ∈ closure{x} ∩ V(𝔞)`" is `𝔭_x ≤ z` and
> `𝔞 ≤ z`. The dimension of `𝒪_{closure{x}, z}` is the Krull dimension of the primes of `A`
> between `𝔭_x` and `z`, which is `Stacks.Algebraization.closureLocalDimension A 𝔭_x z`. No
> hypothesis supplying the surjectivity half of Stacks 0EG2
> (`Stacks.Algebraization.ComparisonSurjectivity`) is assumed.
>
> The dualizing complex enters through its two consequences used by the source, universal
> catenarity (Stacks 0A80) and Gorenstein, hence `(S₁)`, formal fibres (Stacks 0AWY); see the
> module documentation for the rest of the argument.

```lean
theorem isIso_comparisonMap_span_singleton_of_two_lt_closureLocalDimension
    (A : Type u) [CommRing A] [IsNoetherianRing A] (a : Ideal A) (f : A) (_hf : f ∈ a)
    (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent]
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{v} A), Dualizing.IsDualizingComplex K)
    (hdimension : ∀ x : (complementZeroLocus A a : Scheme),
      x ∈ Stacks.Divisors.associatedPoints F → f ∉ x.1.asIdeal →
      (∃ y : PrimeSpectrum A,
        x.1.asIdeal ≤ y.asIdeal ∧ f ∈ y.asIdeal ∧ ¬ a ≤ y.asIdeal) →
      ∀ z : PrimeSpectrum A, x.1.asIdeal ≤ z.asIdeal → a ≤ z.asIdeal →
        (2 : WithBot ℕ∞) < closureLocalDimension A x.1 z) :
    IsIso (comparisonMap A (Ideal.span {f}) a F)
```

**`Stacks.Algebraization.mono_comparisonMap_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusDimensionCriterion.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusDimensionCriterion.lean#L136). The attribute's comment: “injectivity”.

> **Stacks 0H49, the injectivity half.** For a coherent module `ℱ` on
> `U = Spec(A) ∖ V(𝔞)` over a Noetherian ring `A` and an element `f ∈ A`, the map
>
> `colim_V Γ(V, ℱ) ⟶ lim Γ(U, ℱ / fⁿ ℱ)`
>
> of the tag, the colimit being over the opens `V ⊆ U` containing `U ∩ V(f)`, is a monomorphism.
>
> None of the tag's hypotheses is needed: `A` is not assumed `f`-adically complete, no dualizing
> complex is assumed, `f` is not assumed to lie in `𝔞`, and no bound on the local dimensions along
> the associated points of `ℱ` is assumed. This is
> `Stacks.Algebraization.mono_comparisonMap` at the principal ideal `(f)`.

```lean
theorem mono_comparisonMap_span_singleton (A : Type u) [CommRing A] [IsNoetherianRing A]
    (a : Ideal A) (f : A) (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent] :
    Mono (comparisonMap A (Ideal.span {f}) a F)
```

## Tag 0EII, a lemma

[Tag 0EII](https://stacks.math.columbia.edu/tag/0EII) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Algebraization.ComplementTower.sectionsToLimit_isIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ComplementFormalFunctions.lean#L603), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocus.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocus.lean#L236) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.12, Tag 0EG1](https://stacks.math.columbia.edu/tag/0EG1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
