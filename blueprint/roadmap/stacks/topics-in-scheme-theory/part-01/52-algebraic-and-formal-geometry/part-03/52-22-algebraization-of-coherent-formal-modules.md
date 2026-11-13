---
declaration: section
origin: cited
lean: Stacks.Algebraization.canonicallyExtends_of_cd_one_of_proIso_depthThree, Stacks.Algebraization.extendsToX_of_cd_one_of_satisfiesDepthInequalities, Stacks.Algebraization.isCompletion_of_cd_one_of_satisfiesDepthInequalities, Stacks.Algebraization.extendsToX_of_blowUp_fiber_dim_lt, Stacks.Algebraization.algebraization_of_zeroLocus_eq_range_of_depthBound, Stacks.Algebraization.extendsToX_and_essImage_of_isCohenMacaulay_of_span_eq_range
statement: formalized
proof: formalized
---

# 52.22 Algebraization of coherent formal modules, V

Section 52.22 of the Stacks Project, [Tag 0EJH](https://stacks.math.columbia.edu/tag/0EJH). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EJI, a lemma

[Tag 0EJI](https://stacks.math.columbia.edu/tag/0EJI) in the Stacks Project.

**`Stacks.Algebraization.canonicallyExtends_of_cd_one_of_proIso_depthThree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/CanonicalExtensionCdOneDepthThree.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/CanonicalExtensionCdOneDepthThree.lean#L102).

> **Stacks Project, Tag 0EJI.** In Situation 0EHC let `(ℱₙ)` be an object of
> `Coh(U, I𝒪_U)`. Assume (1) `A` has a dualizing complex and `cd(A, I) = 1`, and (2) `(ℱₙ)` is
> pro-isomorphic to an inverse system `(ℱ''ₙ)` of coherent `𝒪_U`-modules with
> `depth(ℱ''_{n,y}) + δ^Y_Z(y) ≥ 3` for all `y ∈ U ∩ Y`. Then `(ℱₙ)` extends canonically to `X`.
>
> A point of `U ∩ Y` is a point `y` of `U` together with a point `z` of `Y` with the same image in
> `X`; the depth is that of the stalk over the local ring of `U` at `y`, and `δ^Y_Z` is evaluated
> at `z`.

```lean
theorem canonicallyExtends_of_cd_one_of_proIso_depthThree
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (G : ℕᵒᵖ ⥤ S.U.toScheme.Modules) [∀ n : ℕᵒᵖ, (G.obj n).IsCoherent]
    (e : InverseSequence.ProIso F.obj G)
    (hdepth : ∀ n : ℕ, ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
      3 ≤ depthOfStalkOnOpen S (G.obj (op n)) y + S.distanceToZ z) :
    CanonicallyExtends S F
```

## Tag 0EJJ, a proposition

[Tag 0EJJ](https://stacks.math.columbia.edu/tag/0EJJ) in the Stacks Project.

**`Stacks.Algebraization.extendsToX_of_cd_one_of_satisfiesDepthInequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationCdOneTheorem.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationCdOneTheorem.lean#L80). The attribute's comment: “(ℱₙ) extends to X”.

> **Stacks Project, Tag 0EJJ (algebraization in cohomological dimension one).** In Situation
> 0EHC let `(ℱₙ)` be an object of `Coh(U, I𝒪_U)`. Assume (1) `A` has a dualizing complex and
> `cd(A, I) = 1`, and (2) `(ℱₙ)` satisfies the `(2, 3)`-inequalities. Then `(ℱₙ)` extends to `X`.

```lean
public theorem extendsToX_of_cd_one_of_satisfiesDepthInequalities
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (hineq : SatisfiesDepthInequalities S F 2 3) :
    ExtendsToX S (toKerSystem S F)
```

**`Stacks.Algebraization.isCompletion_of_cd_one_of_satisfiesDepthInequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationCdOneTheorem.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationCdOneTheorem.lean#L100). The attribute's comment: “in particular, for I-adically complete A, (ℱₙ) is the completion of a coherent 𝒪\_U-module”.

> **Stacks Project, Tag 0EJJ, the final clause.** In the situation of Tag 0EJJ, if moreover `A`
> is `I`-adically complete, then `(ℱₙ)` is the completion of a coherent `𝒪_U`-module.

```lean
public theorem isCompletion_of_cd_one_of_satisfiesDepthInequalities [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (hineq : SatisfiesDepthInequalities S F 2 3) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (toKerSystem S F)
```

## Tag 0EJK, a lemma

[Tag 0EJK](https://stacks.math.columbia.edu/tag/0EJK) in the Stacks Project.

**`Stacks.Algebraization.extendsToX_of_blowUp_fiber_dim_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationBlowupFibres.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationBlowupFibres.lean#L410). The attribute's comment: “the whole statement: under (1) a dualizing complex, (2) fibres of the blowup of I of dimension ≤ d - 1, (3) the (d + 1, d + 2)-inequalities or the bound depth + dim + δ > d + 2, the object (ℱₙ) of Coh(U, I𝒪\_U) extends to X”.

> **Stacks Project, Tag 0EJK.** In Situation [Stacks, Tag 0EHC] let `(ℱₙ)` be an object of
> `Coh(U, I𝒪_U)`. Assume
>
> 1. `A` has a dualizing complex,
> 2. all fibres of the blowing up `b : X' → X` of `I` have dimension `≤ d - 1`, and
> 3. one of the following is true:
>    (a) `(ℱₙ)` satisfies the `(d + 1, d + 2)`-inequalities ([Stacks, Tag 0EJ3]), or
>    (b) for `y ∈ U ∩ Y` and a prime `𝔭 ⊆ 𝒪^∧_{X,y}` with `𝔭 ∉ V(I𝒪^∧_{X,y})` we have
>    `depth((ℱ^∧_y)_𝔭) + dim(𝒪^∧_{X,y}/𝔭) + δ^Y_Z(y) > d + 2`.
>
> Then `(ℱₙ)` extends to `X`.
>
> Here `d` is an integer and the fibre condition `dim ≤ d - 1` is written `dim < d` for the natural
> number `d.toNat`, which is the same condition (for `d ≤ 0` both say every fibre is empty). The
> dualizing complex lives in the derived category `HasDerivedCategory.standard`, as in
> [Stacks, Tag 0EJJ].

```lean
theorem extendsToX_of_blowUp_fiber_dim_lt (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (d : ℤ)
    (hdual : ∃ K : @DerivedCategory (ModuleCat.{u} S.A) _ _
      (HasDerivedCategory.standard (ModuleCat.{u} S.A)),
      @Dualizing.IsDualizingComplex S.A _ _ (HasDerivedCategory.standard (ModuleCat.{u} S.A)) K)
    (hfib : ∀ y : Spec (CommRingCat.of S.A), topologicalKrullDim ((AlgebraicGeometry.blowUpToBase
      (Stacks.LocalCohomology.specIdealSheaf S.A S.I)).fiber y) < ((d.toNat : ℕ) : WithBot ℕ∞))
    (h3 : SatisfiesDepthInequalities S F (d + 1) (d + 2) ∨
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          depthAddDimAddDistance S F y z p > ((d + 2 : ℤ) : EInt)) :
    ExtendsToX S (toKerSystem S F)
```

## Tag 0EJN, a proposition

[Tag 0EJN](https://stacks.math.columbia.edu/tag/0EJN) in the Stacks Project.

**`Stacks.Algebraization.algebraization_of_zeroLocus_eq_range_of_depthBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationFewGenerators.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationFewGenerators.lean#L131). The attribute's comment: “the whole statement: (F\_n) extends to X, and over an I-adically complete A it is the completion of a coherent O\_U-module”.

> **Stacks Project, Tag 0EJN (Algebraization for ideals with few generators).** In Situation
> 0EHC let `(ℱₙ)` be an object of `Coh(U, I𝒪_U)`. Assume (1) `A` has a dualizing complex, (2)
> `V(I) = V(f₁, …, f_d)` for some `d ≥ 1`, and (3) `(ℱₙ)` satisfies the `(d + 1, d + 2)`-inequalities
> or `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) + δ^Y_Z(y) > d + 2` at every `y ∈ U ∩ Y` and every prime
> `𝔭 ∉ V(I𝒪_{X,y}^∧)`. Then `(ℱₙ)` extends to `X`, and if `A` is `I`-adically complete then `(ℱₙ)`
> is the completion of a coherent `𝒪_U`-module.

```lean
public theorem algebraization_of_zeroLocus_eq_range_of_depthBound
    (S : AlgebraizationSituation.{u}) [HasDerivedCategory.{w} (ModuleCat.{u} S.A)]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (d : ℕ) (hd : 1 ≤ d) (f : Fin d → S.A)
    (hV : PrimeSpectrum.zeroLocus (S.I : Set S.A) = PrimeSpectrum.zeroLocus (Set.range f))
    (h3 : SatisfiesDepthInequalities S F (d + 1) (d + 2) ∨
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          depthAddDimAddDistance S F y z p > ((d + 2 : ℤ) : EInt)) :
    ExtendsToX S (toKerSystem S F) ∧
      (IsAdicComplete S.I S.A →
        (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (toKerSystem S F))
```

## Tag 0EJP, a lemma

[Tag 0EJP](https://stacks.math.columbia.edu/tag/0EJP) in the Stacks Project.

**`Stacks.Algebraization.extendsToX_and_essImage_of_isCohenMacaulay_of_span_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationFewGeneratorsCohenMacaulay.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/AlgebraizationFewGeneratorsCohenMacaulay.lean#L94). The attribute's comment: “the whole statement: under hypotheses (1)-(6) the system extends to X, and over an I-adically complete A it is the completion of a coherent O\_U-module; the example in (6) is free\_localizedModule\_completedStalk\_of\_isFiniteLocallyFreeAdic”.

> **Stacks Project, Tag 0EJP.** In Situation 0EHC let `(ℱₙ)` be an object of `Coh(U, I𝒪_U)`.
> Assume
>
> 1. `A` is a local ring which has a dualizing complex,
> 2. all irreducible components of `X` have the same dimension,
> 3. the scheme `X \ Y` is Cohen–Macaulay,
> 4. `I` is generated by `d` elements,
> 5. `dim(X) - dim(Z) > d + 2`, and
> 6. for `y ∈ U ∩ Y` the module `ℱ_y^∧` is finite locally free outside `V(I𝒪_{X,y}^∧)` (for
>    example if `ℱₙ` is a finite locally free `𝒪_U/Iⁿ𝒪_U`-module, see
>    `free_localizedModule_completedStalk_of_isFiniteLocallyFreeAdic`).
>
> Then `(ℱₙ)` extends to `X`. In particular if `A` is `I`-adically complete, then `(ℱₙ)` is the
> completion of a coherent `𝒪_U`-module.

```lean
public theorem extendsToX_and_essImage_of_isCohenMacaulay_of_span_eq_range
    (S : AlgebraizationSituation.{u}) [HasDerivedCategory.{w} (ModuleCat.{u} S.A)]
    [IsLocalRing S.A] (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hequi : Equidimensional (PrimeSpectrum S.A))
    (hCM : ∀ q : PrimeSpectrum S.A, ¬ S.I ≤ q.asIdeal →
      IsCohenMacaulayLocalRing (Localization.AtPrime q.asIdeal))
    (d : ℕ) (f : Fin d → S.A) (hI : S.I = Ideal.span (Set.range f))
    (hdim : ringKrullDim (S.A ⧸ S.a) + ((d + 2 : ℕ) : WithBot ℕ∞) < ringKrullDim S.A)
    (hfree : ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
      ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
        ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
        Module.Free (Localization.AtPrime p.asIdeal)
          (LocalizedModule p.asIdeal.primeCompl (completedStalk (idealOnOpen S) F y))) :
    ExtendsToX S (toKerSystem S F) ∧
      (IsAdicComplete S.I S.A →
        (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (toKerSystem S F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.22, Tag 0EJH](https://stacks.math.columbia.edu/tag/0EJH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
