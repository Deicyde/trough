---
declaration: section
origin: cited
lean: AlgebraicGeometry.frobeniusColimitVectModelEquivalence, AlgebraicGeometry.exists_frobeniusColimitVect_obj_eq, AlgebraicGeometry.frobeniusColimitVectModelHomIsColimit, AlgebraicGeometry.frobeniusColimitVectHomEquiv, AlgebraicGeometry.frobeniusColimitVectModelShiftIso, AlgebraicGeometry.frobeniusColimitVect, AlgebraicGeometry.frobeniusColimitVectEquivalence, AlgebraicGeometry.colimVectComparison_isEquivalence
statement: formalized
proof: formalized
---

# 38.39 Descent vector bundles in positive characteristic

Section 38.39 of the Stacks Project, [Tag 0EXA](https://stacks.math.columbia.edu/tag/0EXA). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EXA, the section

[Tag 0EXA](https://stacks.math.columbia.edu/tag/0EXA) in the Stacks Project.

**`AlgebraicGeometry.frobeniusColimitVectModelEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean#L78). The attribute's comment: “colim_F Vect(S) is the category of pairs (E, n) described in the tag”.

> **Stacks Tag 0EXA: the explicit category is the colimit.** The category
> `frobeniusColimitVectModel`, whose objects are the pairs `(ℰ, n)` and whose Hom-sets are the
> colimits `colim_N Hom_S(F^{N - n, *}ℰ, F^{N - m, *}𝒢)`, is equivalent to the colimit
> `colim_F Vect(S)` of `Vect(S) →F* Vect(S) →F* ⋯` in `Cat`.

```lean
noncomputable def frobeniusColimitVectModelEquivalence :
    frobeniusColimitVectModel X p hX ≌ frobeniusColimitVect X p hX
```

**`AlgebraicGeometry.exists_frobeniusColimitVect_obj_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean#L101). The attribute's comment: “an object of colim_F Vect(S) is a pair (E, n)”.

> **Stacks Tag 0EXA: the objects of `colim_F Vect(S)` are the pairs `(ℰ, n)`.** Every object of
> the colimit in `Cat` is the image of a finite locally free `𝒪_S`-module `ℰ` under the stage-`n`
> coprojection, for some `n`.

```lean
theorem exists_frobeniusColimitVect_obj_eq (Y : frobeniusColimitVect X p hX) :
    ∃ (n : ℕ) (E : X.Vect),
      (EndoColim.catStage.{u + 1} (frobeniusPullback X p hX) n).obj E = Y
```

**`AlgebraicGeometry.frobeniusColimitVectModelHomIsColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean#L133). The attribute's comment: “Hom((E, n), (G, m)) = colim_N Hom_S(F^{N - n, *}E, F^{N - m, *}G)”.

> **Stacks Tag 0EXA: the Hom-sets of `colim_F Vect(S)`.** In the explicit category,
> `Hom((ℰ, n), (𝒢, m))` is the colimit `colim_N Hom_S(F^{N - n, *}ℰ, F^{N - m, *}𝒢)` over the
> `N ≥ n, m` along `F^*`, the colimit maps taking a morphism of `Vect(S)` to the morphism it
> presents.

```lean
noncomputable def frobeniusColimitVectModelHomIsColimit (E G : X.Vect) (n m : ℕ) :
    IsColimit (EndoColim.homCocone (⟨E, n⟩ : frobeniusColimitVectModel X p hX) ⟨G, m⟩)
```

**`AlgebraicGeometry.frobeniusColimitVectHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean#L142). The attribute's comment: “Hom((E, n), (G, m)) = colim_N Hom_S(F^{N - n, *}E, F^{N - m, *}G), for the colimit in Cat”.

> **Stacks Tag 0EXA: the Hom-sets of `colim_F Vect(S)`, in the colimit in `Cat`.** The
> morphisms between the images of `ℰ` and `𝒢` under the stage-`n` and stage-`m` coprojections are
> in bijection with `colim_N Hom_S(F^{N - n, *}ℰ, F^{N - m, *}𝒢)`.

```lean
noncomputable def frobeniusColimitVectHomEquiv (E G : X.Vect) (n m : ℕ) :
    ((EndoColim.catStage.{u + 1} (frobeniusPullback X p hX) n).obj E ⟶
        (EndoColim.catStage.{u + 1} (frobeniusPullback X p hX) m).obj G) ≃
      colimit (EndoColim.homDiagram (⟨E, n⟩ : frobeniusColimitVectModel X p hX) ⟨G, m⟩)
```

**`AlgebraicGeometry.frobeniusColimitVectModelShiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectExplicit.lean#L170). The attribute's comment: “the object (E, n) is isomorphic to the object (F^* E, n + 1)”.

> **Stacks Tag 0EXA: `(ℰ, n) ≅ (F^*ℰ, n + 1)`** in `colim_F Vect(S)`.

```lean
noncomputable def frobeniusColimitVectModelShiftIso (E : X.Vect) (n : ℕ) :
    (⟨E, n⟩ : frobeniusColimitVectModel X p hX) ≅ ⟨(frobeniusPullback X p hX).obj E, n + 1⟩
```

**`AlgebraicGeometry.frobeniusColimitVect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundles.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundles.lean#L274).

> **The category `colim_F Vect(X)` of Stacks Tag 0EXA.** It is the colimit of the sequential
> diagram of categories of finite locally free `𝒪_X`-modules whose transition functors are all
> pullback along the absolute Frobenius.

```lean
noncomputable def frobeniusColimitVect : Cat.{u + 1, u + 1}
```

## Tag 0EXB, a lemma

[Tag 0EXB](https://stacks.math.columbia.edu/tag/0EXB) in the Stacks Project.

**`AlgebraicGeometry.frobeniusColimitVectEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectEssSurj.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectEssSurj.lean#L186). The attribute's comment: “the category colim_F Vect(X) of Tag 0EXA is equivalent to the category of finite locally free modules over the sheaf of rings colim_F O_X”.

> **Stacks Project, Tag 0EXB.** The category `colim_F Vect(X)` of Stacks Tag 0EXA is equivalent
> to the category of finite locally free modules over the sheaf of rings `colim_F 𝒪_X`, the
> equivalence being the comparison functor of the tag.

```lean
noncomputable def frobeniusColimitVectEquivalence [CompactSpace X] [QuasiSeparatedSpace X] :
    frobeniusColimitVectModel X p hX ≌ frobeniusColimitVectorBundles X p hX
```

## Tag 0EXC, a lemma

[Tag 0EXC](https://stacks.math.columbia.edu/tag/0EXC) in the Stacks Project.

**`AlgebraicGeometry.colimVectComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/OneGeneratorColimVectCornerCompat.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/OneGeneratorColimVectCornerCompat.lean#L268).

> Let `p` be a prime, let `A` be a ring with `p = 0`, let `f ∈ A` and let `J ⊆ A` be an ideal
> annihilated by `f ^ n`, so that
>
> ```
> A ⧸ (J + fA) <--- A ⧸ J
>       ^             ^
>       |             |
>    A ⧸ fA   <---    A
> ```
>
> is the almost blowup square of More on Flatness, Example 0EVG. Then the comparison functor
>
> `colim_F Vect(Spec A) ⟶ colim_F Vect(Spec (A ⧸ fA)) ×_{colim_F Vect(Spec (A ⧸ (J + fA)))}
>   colim_F Vect(Spec (A ⧸ J))`
>
> of Frobenius-colimit categories of vector bundles **is an equivalence.**

```lean
theorem colimVectComparison_isEquivalence (A : Type u) [CommRing A] (f : A) (J : Ideal A)
    (n : ℕ) (hann : ∀ x ∈ J, f ^ n * x = 0) (p : ℕ) [Fact p.Prime] (hp : (p : A) = 0) :
    (colimVectComparison A f J p hp).IsEquivalence
```

## Tag 0EXD, a lemma

[Tag 0EXD](https://stacks.math.columbia.edu/tag/0EXD) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_twoGeneratorColimVectComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitTwoGeneratorColimVect.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitTwoGeneratorColimVect.lean#L136). The attribute's comment: “for the categories colim_F Vect of Tag 0EXA”.

> **[Stacks, Tag 0EXD], for the categories `colim_F Vect` of [Stacks, Tag 0EXA].**  Let `p` be
> a prime, `A` a ring in which `p` vanishes and `f₁, f₂ ∈ A`.  For the almost blowup square
> `X = Spec A`, `Z = Spec (A/(f₁,f₂))`, `X' = Proj (A[T₀,T₁]/(f₂T₀ - f₁T₁))`, `E = 𝐏¹_Z` of
> [Stacks, Example 0EVH], the functor
> `colim_F Vect(X) ⟶ colim_F Vect(Z) ×_{colim_F Vect(E)} colim_F Vect(X')`
> built from the transition functors of the models `colim_F Vect(-)` is an equivalence.
>
> It is `AlgebraicGeometry.isEquivalence_twoGeneratorFrobeniusColimitComparison` carried back along
> the comparison functors of [Stacks, Tag 0EXB]
> (`AlgebraicGeometry.isEquivalence_colimVectSquare_of_frobeniusColimitVectorBundlesComparison`):
> the base is affine, the modification and the exceptional line are `Proj` of finitely generated
> graded rings, so all four corners are quasi-compact and quasi-separated.

```lean
theorem isEquivalence_twoGeneratorColimVectComparison :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    ((CategoricalPullback.CatCommSqOver.toFunctorToCategoricalPullback _ _ _).obj
      (colimVectSquareCatCommSqOver p (modificationToBase A f₁ f₂) (centerToBase A f₁ f₂)
        (exceptionalToModification A f₁ f₂) (exceptionalToCenter A f₁ f₂)
        (isInCharacteristic_spec A p hpA)
        (isInCharacteristic_twoGeneratorModification A f₁ f₂ p hpA)
        (isInCharacteristic_twoGeneratorCenter A f₁ f₂ p hpA)
        (isInCharacteristic_twoGeneratorExceptional A f₁ f₂ p hpA)
        (twoGenerator_isPullback A f₁ f₂).w)).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_twoGeneratorFrobeniusColimitComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitTwoGeneratorEquivalence.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitTwoGeneratorEquivalence.lean#L128).

> **[Stacks, Tag 0EXD].** Let `p` be a prime and consider the almost blowup square `X, X', Z, E`
> of [Stacks, Example 0EVH] in characteristic `p`, i.e. over a ring `A` in which `p` vanishes, with
> arbitrary `f₁, f₂ ∈ A`.  Then the functor
> `G : colim_F Vect(X) ⟶ colim_F Vect(Z) ×_{colim_F Vect(E)} colim_F Vect(X')`
> is an equivalence.

```lean
theorem isEquivalence_twoGeneratorFrobeniusColimitComparison :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    (twoGeneratorFrobeniusColimitComparison A f₁ f₂ p hpA).IsEquivalence
```

## Tag 0EXE, a proposition

[Tag 0EXE](https://stacks.math.columbia.edu/tag/0EXE) in the Stacks Project.

**`AlgebraicGeometry.frobeniusVectorBundleGroupoidFiberEquivCoreColimitVect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundleGroupoidColimitVect.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundleGroupoidColimitVect.lean#L98). The attribute's comment: “moreover: if U is quasi-compact and quasi-separated, then the fibre S_U of the category fibred in groupoids S over (Sch/S)_h is colim_F Vect(U), as its maximal subgroupoid”.

> **Stacks Tag 0EXE, the "moreover" clause.** Let `S` be a scheme in characteristic `p` and let
> `U` be an object of `(Sch/S)_h` whose underlying scheme is quasi-compact and quasi-separated.
> Then the fibre `𝒮_U` over `U` of the category fibred in groupoids `𝒮 ⟶ (Sch/S)_h` of finite
> locally free `colim_F 𝒪`-modules is `colim_F Vect(U)`, read as a groupoid: it is equivalent to the
> maximal subgroupoid of the colimit `colim_F Vect(U)` in `Cat` of Stacks Tag 0EXA.
>
> The fibre is the groupoid of finite locally free modules over `colim_F 𝒪_U`
> (`AlgebraicGeometry.frobeniusVectorBundleGroupoidFiberEquiv`), which is the core of the category
> of such modules (`CategoryTheory.ObjectProperty.coreFullSubcategoryEquiv`); Stacks Tag 0EXB
> (`AlgebraicGeometry.frobeniusColimitVectEquivalence`) and Stacks Tag 0EXA
> (`AlgebraicGeometry.frobeniusColimitVectModelEquivalence`) identify that category with
> `colim_F Vect(U)`, and the identification passes to cores.

```lean
def frobeniusVectorBundleGroupoidFiberEquivCoreColimitVect (U : BigHOver B S hS)
    [CompactSpace ((BigHOver.toScheme B S hS).obj U)]
    [QuasiSeparatedSpace ((BigHOver.toScheme B S hS).obj U)] :
    (frobeniusVectorBundleGroupoidFibration B S hS p hpS).Fiber U ≌
      Core (frobeniusColimitVect ((BigHOver.toScheme B S hS).obj U) p
        (isInCharacteristic_bigHOver B S hS p hpS U))
```

**`AlgebraicGeometry.frobeniusVectorBundleGroupoidFibration_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundleStack.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusColimitVectorBundleStack.lean#L67). The attribute's comment: “stack in groupoids”.

> **Stacks Project, Tag 0EXE.** Let `p` be a prime number and let `S` be a scheme in
> characteristic `p`. Then the category fibred in groupoids `p : 𝒮 ⟶ (Sch/S)_h` whose fibre category
> over `U` is the category of finite locally free `colim_F 𝒪_U`-modules over `U` (with its
> isomorphisms) is a stack in groupoids.
>
> Here `(Sch/S)_h` is the big h site `AlgebraicGeometry.BigHOver B S hS` of an arbitrary big h site
> `B` containing `S`, and "stack in groupoids" is Stacks 02ZI for its h topology.

```lean
theorem frobeniusVectorBundleGroupoidFibration_isStackInGroupoids
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (p : ℕ) [Fact p.Prime]
    (hpS : IsInCharacteristic S p) :
    (frobeniusVectorBundleGroupoidFibration B S hS p hpS).IsStackInGroupoids.{u + 1}
      (BigHOver.topology B S hS)
```

## Tag 0EXF, a lemma

[Tag 0EXF](https://stacks.math.columbia.edu/tag/0EXF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FreenessOverDVR.exists_thickening_exponent_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FreenessOverDVR/FreenessCriterion.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FreenessOverDVR/FreenessCriterion.lean#L190). The attribute's comment: “without the hypothesis that the fibres are geometrically connected, which the proof does not use”.

> **Stacks, Tag 0EXF.** Let `f : X ⟶ S` be a proper morphism where `S = Spec A` is the
> spectrum of a discrete valuation ring. Denote `η ∈ S` the generic point and `Xₙ ⊆ X` the closed
> subscheme cut out by the `n`-th power of a uniformizer. Then there exists an integer `n` such
> that any finite locally free `𝒪_X`-module `𝓔` such that `𝓔|_{X_η}` and `𝓔|_{Xₙ}` are free, is
> free.
>
> The integer is `n = k + 1 + e`. Here `k` bounds the `π`-power torsion of the local rings of `X`
> (`exists_forall_germ_pow_mul_eq_zero`), and `e` bounds the `π`-power torsion of
> `H¹(X, πᵏ 𝒪_X^r)` for every rank `r` at once (`exists_pow_smul_cohomology_adicSub_free_eq_zero`).
> Comparing the lengths of `H⁰(X, πᵏ (𝓔 / πᵏ⁺ᵐ 𝓔))` and `H⁰(X, πᵏ (𝒪_X^r / πᵏ⁺ᵐ 𝒪_X^r))` at
> `m = e` and `m = e + 1`, which agree because `𝓔 / πⁿ 𝓔 ≅ 𝒪_X^r / πⁿ 𝒪_X^r`, transfers that
> bound to `H¹(X, πᵏ 𝓔)` (`torsionBy_cohomology_eq_bot_of_adicQuotientIso`); the free ranks of the
> two `H⁰` agree by the generic fibre. The basis sections of `𝒪_X^r / πⁿ 𝒪_X^r` then lift, modulo
> `πᵏ⁺¹`, to global sections of `𝓔` (`exists_sections_lift`), and the resulting
> `𝒪_X^r ⟶ 𝓔` is an isomorphism modulo `πᵏ⁺¹`, hence an isomorphism since `f` is proper over a
> local base (`isIso_of_comp_adicProj`).
>
> The source's hypothesis that the fibres of `f` be geometrically connected is not used: the
> source needs it only to reduce to the case where `f` has a section, and the argument above does
> not pass through a section.

```lean
theorem exists_thickening_exponent_free (A : Type u) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsProper f] :
    ∃ n : ℕ, 0 < n ∧ ∀ E : X.Modules, E.IsFiniteLocallyFree →
      IsFreeOfFiniteRank (genericFibreRestrict A f E) →
      IsFreeOfFiniteRank (thickeningRestrict A f n E) →
      IsFreeOfFiniteRank E
```

**`Stacks.AlgebraicGeometry.FreenessOverDVR.exists_thickening_exponent_free_of_free_generic_and_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FreenessOverDVR/Triviality.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FreenessOverDVR/Triviality.lean#L308). The attribute's comment: “conditional on `TrivialityInput`, which carries the source's cited input [Stacks, Tag 02O6] (finiteness of the cohomology of a proper morphism, open in this library), the reduction to the case of a section — whose last step, invertibility of a determinant invertible at one point of each fibre, the source itself leaves to the reader — and the derived comparison `RΓ(X, 𝓔) ⊗^L A/π^m ≅ RΓ(X, 𝒪_X^r) ⊗^L A/π^m` read on cohomology. Of the inputs of that comparison the library does carry the subsheaf of sections supported on the special fibre ([Stacks, Tag 084L]), the quotients `𝓔/π^j 𝓔`, the Artin-Rees exponent ([Stacks, Tag 01YA]), the two-term complex `(𝓔 --π^m--> 𝓔)` in `D(𝒪_X)` with its distinguished triangle, and `RΓ(X, -) : D(𝒪_X) ⥤ D(A)`; what it lacks is the reduction formula `Hⁱ(K ⊗^L A/π^m) = Hⁱ(K)/π^m ⊕ Hⁱ⁺¹(K)[π^m]`, which is a step of the source's proof and not a tag. Proved here: the construction of both exponents and hence of `n`, the summand-counting transfer of the exponent bound from `𝒪_X` to `𝓔` (`torsionExponentTransfer`), and the two Nakayama steps that turn surjectivity modulo `π^{e+1}` into freeness. The hypotheses are satisfiable: `exists_thickening_exponent_free_specPowerSeries` discharges all of them over `k⟦X⟧`”.

> **Stacks, Tag 0EXF.** Let `f : X ⟶ Spec A` be proper with geometrically connected fibres over
> a discrete valuation ring `A`, let `η` be the generic point of `Spec A` and let `X_n ⊆ X` be the
> closed subscheme cut out by the `n`-th power of a uniformizer `π`. There is an integer `n`,
> independent of the module, such that every finite locally free `𝒪_X`-module which is free on
> `X_η` and on `X_n` is free.
>
> The integer produced is `e + 1 + k`, which is the source's `k + e + 1`: `k` is the Artin-Rees
> exponent carried by `TrivialityInput.comparison`, and `e` is an exponent annihilating the
> `π`-power torsion of `H⁰(X, 𝒪_X)` and `H¹(X, 𝒪_X)`, both of which depend only on `X`.

```lean
theorem exists_thickening_exponent_free_of_free_generic_and_thickening
    {π : A} (hπ : Irreducible π) (h : TrivialityInput A f π) :
    ∃ n : ℕ, 0 < n ∧ ∀ E : X.Modules, E.IsFiniteLocallyFree →
      IsFreeOfFiniteRank (genericFibreRestrict A f E) →
      IsFreeOfFiniteRank (thickeningRestrict A f n E) →
      IsFreeOfFiniteRank E
```

## Tag 0EXG, a lemma

[Tag 0EXG](https://stacks.math.columbia.edu/tag/0EXG) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleCodimensionOne.exists_isFiniteLocallyFree_pullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/VectorBundleCodimensionOne/FreeOverLocalBase.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/VectorBundleCodimensionOne/FreeOverLocalBase.lean#L61). The attribute's comment: “corrected: freeness is also required at generic points of S with no codimension-1 specialization; as stated the lemma fails for X = ℙ¹_k over Spec k with ℰ = 𝒪(1)”.

> Let `f : X ⟶ S` be flat and proper with `𝒪_S = f_*𝒪_X`, let `S` be a normal Noetherian
> scheme, and let `ℰ` be a finite locally free `𝒪_X`-module whose pullback to `X ×_S Spec 𝒪_{S,s}`
> is free for every point `s ∈ S` of codimension one, and also for every point `s` of codimension
> zero that does not specialize to a point of codimension one. Then `ℰ` is isomorphic to the
> pullback of a finite locally free `𝒪_S`-module.
>
> The two conditions `hfree` and `hfree₀` together are equivalent to freeness over the local scheme
> at every point of codimension at most one. The condition `hfree₀` is not in the source, and the
> statement is false without it (`not_forall_exists_isFiniteLocallyFree_pullback_iso_of_codimOne`):
> for a field `k`, take `S = Spec k`, `X = ℙ¹_k` and `ℰ = 𝒪(1)`; then `S` has no point of
> codimension one, but `𝒪(1)` is not the pullback of a `k`-vector space. When every irreducible
> component of `S` has a point of codimension one, `hfree₀` is vacuous.
>
> Codimension of a point is the Krull dimension of its local ring, and freeness after base change
> to the local scheme at `s` means an isomorphism with some free module `𝒪^{(I)}`, the index set
> being arbitrary. The hypothesis `𝒪_S = f_*𝒪_X` is invertibility of the comparison map
> `f.toLRSHom.toHom.c`.

```lean
public theorem exists_isFiniteLocallyFree_pullback_iso {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [IsProper f] [IsNoetherian S] [IsNormal S] (E : X.Modules)
    [SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] (hO : IsIso f.toLRSHom.toHom.c)
    (hfree : ∀ s : S, ringKrullDim (S.presheaf.stalk s) = 1 →
      ∃ I : Type u, Nonempty
        ((Scheme.Modules.pullback (pullback.fst f (S.fromSpecStalk s))).obj E ≅
          SheafOfModules.free I))
    (hfree₀ : ∀ s : S, ringKrullDim (S.presheaf.stalk s) = 0 →
      (∀ t : S, s ⤳ t → ringKrullDim (S.presheaf.stalk t) ≠ 1) →
      ∃ I : Type u, Nonempty
        ((Scheme.Modules.pullback (pullback.fst f (S.fromSpecStalk s))).obj E ≅
          SheafOfModules.free I)) :
    ∃ M : S.Modules, SheafOfModules.IsFiniteLocallyFree.{u, u, u} M ∧
      Nonempty ((Scheme.Modules.pullback f).obj M ≅ E)
```

## Tag 0EXH, a theorem

[Tag 0EXH](https://stacks.math.columbia.edu/tag/0EXH) in the Stacks Project.

**`AlgebraicGeometry.frobeniusColimitVectModelPullback_full_faithful_and_descends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FrobeniusDescentVectorBundles.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FrobeniusDescentVectorBundles.lean#L48).

> **Descent of vector bundles in positive characteristic** (Stacks Tag 0EXH). Let `p` be a
> prime, `Y` a quasi-compact quasi-separated scheme over `𝐅_p` and `f : X ⟶ Y` a proper surjective
> morphism of finite presentation with geometrically connected fibres. Then the pullback functor
> `colim_F Vect(Y) ⥤ colim_F Vect(X)` is fully faithful, and if `ℰ` is a finite locally free
> `𝒪_X`-module such that for all `y ∈ Y` there are `n_y, r_y ≥ 0` with
> `F^{n_y,*}ℰ|_{X_{y,red}} ≅ 𝒪_{X_{y,red}}^{⊕ r_y}`, then for some `n ≥ 0` the Frobenius power
> pullback `F^{n,*}ℰ` is the pullback of a finite locally free `𝒪_Y`-module.

```lean
theorem frobeniusColimitVectModelPullback_full_faithful_and_descends (p : ℕ) [Fact p.Prime]
    {X Y : Scheme.{u}} (hY : IsInCharacteristic Y p) (f : X ⟶ Y) [CompactSpace Y]
    [QuasiSeparatedSpace Y] [IsProper f] [Surjective f] [LocallyOfFinitePresentation f]
    [GeometricallyConnected f] :
    ((frobeniusColimitVectModelPullback f p (isInCharacteristic_of_hom f p hY) hY).Full ∧
      (frobeniusColimitVectModelPullback f p (isInCharacteristic_of_hom f p hY) hY).Faithful) ∧
    ∀ E : X.Vect,
      (∀ y : Y, ∃ n r : ℕ, Nonempty
        ((Scheme.Modules.pullback ((f.fiber y).reductionι ≫ f.fiberι y)).obj
            ((frobeniusPullbackIter X p (isInCharacteristic_of_hom f p hY) n).obj E).obj ≅
          SheafOfModules.free (ULift.{u} (Fin r)))) →
      ∃ (n : ℕ) (G : Y.Vect), Nonempty
        ((frobeniusPullbackIter X p (isInCharacteristic_of_hom f p hY) n).obj E ≅
          (Scheme.Vect.pullback f).obj G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.39, Tag 0EXA](https://stacks.math.columbia.edu/tag/0EXA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
