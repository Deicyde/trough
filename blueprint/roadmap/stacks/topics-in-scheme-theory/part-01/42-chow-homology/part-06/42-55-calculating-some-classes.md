---
declaration: section
origin: cited
lean: Stacks.Chow.homComponent_exteriorPowerChernAltProd, Stacks.Chow.homPart_altExteriorTotalChern, Stacks.Chow.altExteriorChernProduct_apply, Stacks.Chow.ProjectiveCompletion.bivariantClass_zeroSecObject, Stacks.Chow.ProjectiveCompletion.chernClasses_zeroSecObject, Stacks.Chow.chernClass_pushforward_zeroSection, Stacks.Chow.isRegularImmersionChernFormula_regularImmersionStructureSheafSituation, Stacks.Chow.regularImmersionStructureSheafSituation_capFundamentalClass
statement: formalized
proof: formalized
---

# 42.55 Calculating some classes

Section 42.55 of the Stacks Project, [Tag 0FED](https://stacks.math.columbia.edu/tag/0FED). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FEE, a lemma

[Tag 0FEE](https://stacks.math.columbia.edu/tag/0FEE) in the Stacks Project.

**`Stacks.Chow.homComponent_exteriorPowerChernAltProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernAlternatingProduct.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernAlternatingProduct.lean#L184). The attribute's comment: “the whole lemma, for the library's Chern classes: c(wedge^n E) is the total Chern class totalChern of Stacks 0B7H, the product is the ordered product of units in the ring TotalChowClass = prod\_\{p >= 0} A^p(Y) of total Chow cohomology classes, and '= 1 - (r-1)! c\_r(E) + ...' is the equality of homogeneous components in every degree <= r. The splitting principle is proved, not assumed: Stacks 02UL via exists\_splittingMorphism\_basechange\_unconditional, the Chern roots of the exterior powers via 02UI and 02UJ (totalChern\_exteriorPower\_of\_hasQuotients)”.

> **Stacks 0FEE.** For a finite locally free module `ℰ` of rank `r ≥ 1` on `Y`, the alternating
> product `∏_{n = 0}^{r} c(⋀ⁿ ℰ)^{(-1)ⁿ}` of the total Chern classes of its exterior powers, in the
> ring `∏_{p ≥ 0} A^p(Y)` of total Chow cohomology classes, agrees with `1 - (r - 1)! c_r(ℰ)` in
> every degree `≤ r`. The `+ …` of the source is the part in degrees `> r`, on which nothing is
> asserted.

```lean
theorem homComponent_exteriorPowerChernAltProd (hr : r ≠ 0) {t : ℕ} (ht : t ≤ r) :
    TotalChowClass.homComponent t (exteriorPowerChernAltProd C sY V r : TotalChowClass C sY) =
      TotalChowClass.homComponent t
        (1 - (r - 1).factorial • TotalChowClass.homComponent r (totalChern C sY V r))
```

**`Stacks.Chow.homPart_altExteriorTotalChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernClasses.lean, line 723](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernClasses.lean#L723). The attribute's comment: “the lemma as stated, for every X locally of finite type over S and every finite locally free E of rank r >= 1, with no further hypothesis. The alternating product is altExteriorTotalChern C sX E r, the ordered product of the units totalChernUnit of the exterior powers in the ring TotalChowClass C sX of total Chow cohomology classes; c\_i(E) is TotalChowClass.homComponent i (totalChern C sX E r). The + ... of the source is read as asserting nothing above degree r, as its proof does”.

> **Stacks 0FEE.** Let `ℰ` be a finite locally free `𝒪_X`-module of rank `r ≥ 1`. Then
>
>   `∏_{n = 0}^{r} c(⋀ⁿ ℰ)^{(-1)ⁿ} = 1 - (r-1)! c_r(ℰ) + ⋯`,
>
> that is, the alternating product of the total Chern classes of the exterior powers of `ℰ` has
> vanishing parts in the degrees `1, …, r - 1` and the part `-(r-1)! c_r(ℰ)` in degree `r`; the part
> in degree `0` is `1`, and the `⋯` of the source asserts nothing about the higher degrees. Here
> `c_i(ℰ) = TotalChowClass.homComponent i (totalChern C sX ℰ r)` is the bivariant Chern class of
> Stacks 0B7H in the ring `∏_p A^p(X)` of total Chow cohomology classes.
>
> By the splitting principle (Stacks 02UL,
> `Stacks.Chow.TotalChowClass.eq_of_res_eq_of_hasInvertibleFiltration`) it suffices to prove the
> identities after restriction along every `h : T ⟶ X` along which `h^*ℰ` has a filtration with
> invertible quotients. There `c(⋀ⁿ h^*ℰ) = ∏_{#I = n} (1 + ∑_{i ∈ I} x_i)` for the Chern roots
> `x_i` (`Stacks.Chow.exists_chernRoots_exteriorPower`), and the alternating product of these is
> computed by `Stacks.Chow.homPart_alternatingProd_of_roots`.

```lean
theorem homPart_altExteriorTotalChern (E : X.Modules) {r : ℕ}
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (hr : r ≠ 0) :
    (∀ n, 0 < n → n < r →
      TotalChowClass.homComponent n (altExteriorTotalChern C sX E r : TotalChowClass C sX) = 0) ∧
      TotalChowClass.homComponent r (altExteriorTotalChern C sX E r : TotalChowClass C sX) =
        -(Nat.factorial (r - 1) • TotalChowClass.homComponent r (totalChern C sX E r))
```

**`Stacks.Chow.altExteriorChernProduct_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernProduct.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ExteriorPowerChernProduct.lean#L306). The attribute's comment: “the whole lemma, in the carried ring A^*(X)^∧ of Stacks 0FE0 where the inverses c(E)^\{-1} exist. CARRIED: the Chern roots, i.e. the display c(wedge^n E) = prod\_\{i\_1 < ... < i\_n} (1 + x\_\{i\_1} + ... + x\_\{i\_n}) of the source proof, i.e. the splitting principle: Stacks 02UK, 02UL and the product form of 02UJ; see the module doc. The computation is proved”.

> **Stacks 0FEE.** For `ℰ` locally free of rank `r ≥ 1` with Chern roots `t`, the alternating
> product `∏_{n = 0}^{r} c(⋀ⁿ ℰ)^{(-1)ⁿ}` has vanishing components in the degrees `1, …, r-1` and
> the component `-(r-1)! c_r(ℰ)` in degree `r`; nothing is asserted in higher degrees, which is the
> `+ …` of the source.

```lean
theorem altExteriorChernProduct_apply (D : TotalChernClassSeries C G sX R) (E : X.Modules)
    {r : ℕ} [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    (hr : r ≠ 0) (t : Fin r → chowCohomologyComponent C G sX 1)
    (hE : D.ch E = (∏ i, oneAddDegreeOne R (t i) : UnitalSeries R).1)
    (hwedge : ∀ n ≤ r, D.ch (Scheme.Modules.exteriorPower E (n : ℤ))
      = (rootTotalChern R t ((Finset.univ : Finset (Fin r)).powersetCard n)).1) :
    (∀ n, 0 < n → n < r → (altExteriorChernProduct D E r).1 n = 0) ∧
      (altExteriorChernProduct D E r).1 r
        = -(Nat.factorial (r - 1) • D.ch E r)
```

## Tag 0FEF, a lemma

[Tag 0FEF](https://stacks.math.columbia.edu/tag/0FEF) in the Stacks Project.

**`Stacks.Chow.ProjectiveCompletion.bivariantClass_zeroSecObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveCompletionChern/ZeroSectionBivariant.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveCompletionChern/ZeroSectionBivariant.lean#L573). The attribute's comment: “clause (2), as an equality of bivariant classes after composing with any c ∈ A^*(E → X₀)”.

> **Stacks 0FEF (2), as an equality of bivariant classes.** Let `π : E ⟶ X` be the projective
> completion of a locally free module `𝒞` of rank `r`, `i : X ⟶ E` its zero section,
> `j : C ⟶ E` and `p : C ⟶ X` the inclusion and the structure morphism of the vector bundle
> `C = Spec_X(Sym^*(𝒞))`. For every `s : X ⟶ X₀` and every bivariant class `c ∈ A^q(E ⟶ X₀)`,
>
>   `p^* ∘ π_* ∘ (c_r(i_*𝒪_X) ∘ c) = (-1)^{r-1} (r-1)! (j^* ∘ c)`  in `A^q(C ⟶ X₀)`.
>
> Here `c_r(i_*𝒪_X) ∈ A^r(E)` is the Chern class of Stacks 0F9E, `∘` the composition of Stacks
> 0B75, `π_*` the pushforward of Stacks 0EPK and `p^* ∈ A^{-r}(C ⟶ X)`, `j^* ∈ A^0(C ⟶ E)` the
> flat pullback classes of Stacks 0B78; the two sides are classes for the equal morphisms
> `p ≫ s = j ≫ π ≫ s` and of the equal degrees `-r + (r + q) = -0 + q`, compared through the
> transport `Stacks.Chow.BivariantClass.copy`. This is the form in which the source composes the
> identity `p^* ∘ π_* ∘ c_r(i_*𝒪_X) = (-1)^{r-1} (r-1)! j^*` with a class on its right (Stacks 0FEG);
> by the extensionality of Stacks 0B76 it is checked on the caps, which are classes on the base
> changes `E ×_{X₀} T = E ×_X (X ×_{X₀} T)`, where it is the cartesian-square form
> `flatPullbackChow_properChowPushforward_perfectChernClass_of_isPullback` of the second conclusion.

```lean
theorem bivariantClass_zeroSecObject {X₀ : Scheme.{u}} (sX₀ : X₀ ⟶ C.S) [LocallyOfFiniteType sX₀]
    (s : X ⟶ X₀) [LocallyOfFiniteType s] (hs : s ≫ sX₀ = sX) :
    haveI := locallyOfFiniteType_proj 𝒞 r
    haveI := flat_proj 𝒞 r
    haveI := locallyOfFiniteType_vectorBundleToBase 𝒞 r
    haveI := flat_vectorBundleToBase 𝒞 r
    ∀ {q : ℤ} (c : BivariantClass C (gysinSystemOfInvertible C) (proj 𝒞 ≫ sX) sX₀
      (proj 𝒞 ≫ s) (comp_comp_structureMorphism_eq rfl hs) q),
      bivariantCompositeOfInvertible C _ sX sX₀ _ s rfl hs (-(r : ℤ)) ((r : ℤ) + q)
          (flatPullbackBivariantClassOfInvertible C
            (Scheme.Modules.vectorBundleToBase X 𝒞 ≫ sX) sX _ rfl r
            (relativeDimension_vectorBundleToBase 𝒞 r))
          (canonicalBivariantProperPushforward C (proj 𝒞 ≫ sX) sX sX₀ (proj 𝒞) s rfl hs
            ((r : ℤ) + q)
            (BivariantClass.copy C (gysinSystemOfInvertible C) (proj 𝒞 ≫ sX) sX₀
              (Category.id_comp (proj 𝒞 ≫ s)) _ _ rfl
              (bivariantCompositeOfInvertible C (proj 𝒞 ≫ sX) (proj 𝒞 ≫ sX) sX₀ (𝟙 _)
                (proj 𝒞 ≫ s) (Category.id_comp _) (comp_comp_structureMorphism_eq rfl hs)
                (r : ℤ) q
                (perfectChernClass C (proj 𝒞 ≫ sX) (hasDefinedChernClasses_zeroSecObject 𝒞 r)
                  r) c))) =
        BivariantClass.copy C (gysinSystemOfInvertible C) _ sX₀ (incl_proj_comp 𝒞 r s) _
          (comp_comp_structureMorphism_eq rfl hs)
          (show -((0 : ℕ) : ℤ) + q = -(r : ℤ) + ((r : ℤ) + q) by push_cast; ring)
          ((((-1 : ℤ) ^ (r - 1) * ((r - 1).factorial : ℤ)) •
            bivariantCompositeOfInvertible C _ (proj 𝒞 ≫ sX) sX₀ (vectorBundleIncl 𝒞 r)
              (proj 𝒞 ≫ s) (vectorBundleIncl_comp_structure 𝒞 r C sX)
              (comp_comp_structureMorphism_eq rfl hs) (-((0 : ℕ) : ℤ)) q
              (flatPullbackBivariantClassOfInvertible C _ _ _
                (vectorBundleIncl_comp_structure 𝒞 r C sX) 0
                (relativeDimension_of_isOpenImmersion _)) c))
```

**`Stacks.Chow.ProjectiveCompletion.chernClasses_zeroSecObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveCompletionChern/ZeroSectionProjection.lean, line 834](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveCompletionChern/ZeroSectionProjection.lean#L834). The attribute's comment: “both conclusions: (1) c\_t(i\_*O\_X) = 0 for t = 1, ..., r - 1; (2) p^* o pi\_* o c\_r(i\_*O\_X) = (-1)^(r-1) (r-1)! j^*, as an identity of operations at every test scheme E' -> E on which the left side is defined, namely every base change E' = E x\_X X' of pi along f : X' -> X locally of finite type (any cartesian square), with C' = C x\_E E' any cartesian square: p'^* pi'\_* (c\_r(i\_*O\_X) cap alpha) = (-1)^(r-1) (r-1)! j'^* alpha for alpha in A\_k(E'). In the bivariant conventions c\_r(i\_*O\_X) lies in A^r(E -> E) and the pushforward of 0EPK needs a class over a morphism factoring through pi, so the left side is not a composite of bivariant classes in A^0(C -> E); its operation exists exactly on these test schemes, which are those on which the source's proof compares the two sides”.

> **Stacks 0FEF.** Let `𝒞` be a locally free `𝒪_X`-module of rank `r` on `X` locally of finite
> type over the base of chapter 42, `π : E = Proj_X(Sym^*(𝒞)[T]) ⟶ X` its projective completion with
> zero section `i : X ⟶ E`, and `j : C = Spec_X(Sym^*(𝒞)) ⟶ E`, `p : C ⟶ X` the inclusion and the
> structure morphism of the vector bundle. Then
>
> 1. `c_t(i_*𝒪_X) = 0` for `t = 1, …, r - 1`, and
> 2. `p^* ∘ π_* ∘ c_r(i_*𝒪_X) = (-1)^{r-1} (r-1)! j^*`, as operations on every test scheme
>    `g : E' ⟶ E` on which the left-hand side is defined: for every cartesian square
>    `E' = E ×_X X'` over `f : X' ⟶ X` locally of finite type, with `π' : E' ⟶ X'`, every
>    cartesian square `C' = C ×_E E'` with `j' : C' ⟶ E'`, and every `α ∈ A_k(E')`,
>    `p'^* π'_*(c_r(i_*𝒪_X) ∩ α) = (-1)^{r-1} (r-1)! j'^* α` in `A_k(C')`, where `p' = π' ∘ j'`.
>
> The Chern classes are those of Stacks 0F9E of the perfect object `i_*𝒪_X` of `D(𝒪_E)`, and
> `c_r(i_*𝒪_X) ∩ α` is the operation of `c_r(i_*𝒪_X) ∈ A^r(E)` on the test scheme `g`.
>
> On the reading of (2). In the conventions of bivariant classes, `c_r(i_*𝒪_X) ∈ A^r(E ⟶ E)` and the
> pushforward `π_* ∘ -` of Stacks 0EPK applies to a class of `A^*(E ⟶ Z)` for a morphism `E ⟶ Z`
> factoring through `π`, so `p^* ∘ π_* ∘ c_r(i_*𝒪_X)` is not a composite of bivariant classes landing
> in `A⁰(C ⟶ E)`. The operation it names is defined on those test schemes `E' ⟶ E` that are base
> changes of `π`, where `π'_*` exists, and these are the test schemes on which the proof of the
> source compares the two sides ("after replacing `X` by a scheme locally of finite type over
> `X` ... both sides have the same effect on `α ∈ CH_*(E)`"). Statement (2) is the identity of the
> two operations at every such test scheme.

```lean
theorem chernClasses_zeroSecObject :
    (letI := locallyOfFiniteType_proj_comp 𝒞 r C sX
      ∀ t : ℕ, 0 < t → t < r →
        perfectChernClass C (proj 𝒞 ≫ sX) (hasDefinedChernClasses_zeroSecObject 𝒞 r) t = 0) ∧
    ∀ {X' E' C' : Scheme.{u}} (f : X' ⟶ X) [LocallyOfFiniteType f] (g : E' ⟶ space 𝒞)
      (π' : E' ⟶ X') (hsq : IsPullback g π' (proj 𝒞) f)
      (q : C' ⟶ Scheme.Modules.vectorBundle X 𝒞) (j' : C' ⟶ E')
      (hsqC : IsPullback q j' (vectorBundleIncl 𝒞 r) g) (k : ℤ),
      haveI := locallyOfFiniteType_proj 𝒞 r
      haveI := flat_proj 𝒞 r
      haveI : LocallyOfFiniteType g := MorphismProperty.of_isPullback hsq.flip inferInstance
      haveI : LocallyOfFiniteType π' := MorphismProperty.of_isPullback hsq inferInstance
      haveI : Flat π' := MorphismProperty.of_isPullback hsq inferInstance
      haveI : IsProper π' := MorphismProperty.of_isPullback hsq inferInstance
      haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback hsqC inferInstance
      ∀ α : chowGroup C (g ≫ proj 𝒞 ≫ sX) k,
      flatPullbackChow C (j' ≫ g ≫ proj 𝒞 ≫ sX) (f ≫ sX) (j' ≫ π')
          (incl_snd_comp_eq 𝒞 C sX hsq j') r (relativeDimension_incl_snd 𝒞 r hsq j') (k - r)
          (flatPullbackFactorsThroughRationalEquivalence_general C _ _ _
            (incl_snd_comp_eq 𝒞 C sX hsq j') r (relativeDimension_incl_snd 𝒞 r hsq j') (k - r))
          (properChowPushforward C (g ≫ proj 𝒞 ≫ sX) (f ≫ sX) π' (snd_comp_eq 𝒞 C sX hsq) (k - r)
            (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ _ _
              (snd_comp_eq 𝒞 C sX hsq) (k - r))
            ((perfectChernClass C (proj 𝒞 ≫ sX) (hasDefinedChernClasses_zeroSecObject 𝒞 r)).op
              g k r α)) =
        chowGroupCast C _ (show k + ((0 : ℕ) : ℤ) = k - r + r by push_cast; ring)
          (((-1 : ℤ) ^ (r - 1) * ((r - 1).factorial : ℤ)) •
            flatPullbackChow C _ (g ≫ proj 𝒞 ≫ sX) j' rfl 0
              (relativeDimension_of_isOpenImmersion _) k
              (flatPullbackFactorsThroughRationalEquivalence_general C _ _ _ rfl 0
                (relativeDimension_of_isOpenImmersion _) k) α)
```

**`Stacks.Chow.chernClass_pushforward_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSectionKoszul/ChernClassZeroSection.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ZeroSectionKoszul/ChernClassZeroSection.lean#L260). The attribute's comment: “the whole lemma, for r ≥ 1 (the source's (r-1)! presupposes it): c\_t(i\_*O\_X) = 0 for 0 < t < r, and p^* ∘ π\_* ∘ c\_r(i\_*O\_X) = (-1)^\{r-1}(r-1)! j^* on every test scheme X' ×\_X E ⟶ E, which are the test schemes on which the composite p^* ∘ π\_* ∘ c\_r is defined”.

> **Stacks 0FEF.** Let `X` be locally of finite type over the base `S` of chapter 42, `𝒞` a
> finite locally free `𝒪_X`-module of rank `r ≥ 1`, `π : E = 𝐏(𝒞 ⊕ 𝒪_X) ⟶ X` the projective
> completion, `i : X = 𝐏(𝒪_X) ⟶ E` the zero section, `C = Spec_X(Sym(𝒞)) = V ⊆ E` the complement
> of the divisor at infinity with its inclusion `j` and projection `p : V ⟶ X`. Then
>
> * `c_t(i_*𝒪_X) = 0` for `t = 1, …, r - 1`, and
> * `p^* ∘ π_* ∘ c_r(i_*𝒪_X) = (-1)^{r-1} (r-1)! j^*` in `A^0(C → E)`: for every test scheme
>   `q : X' ×_X E ⟶ E` obtained from a morphism `g : X' ⟶ X` locally of finite type, with
>   `π' : X' ×_X E ⟶ X'`, `V' = q⁻¹(V)` and `p' : V' ⟶ X'`, and every `α ∈ CH_*(X' ×_X E)`,
>   `p'^*(π'_*(c_r(i_*𝒪_X) ∩ α)) = (-1)^{r-1} (r-1)! α|_{V'}`; the test scheme `𝟙_E` is stated
>   separately.
>
> The Chern classes of `i_*𝒪_X` are defined because it is resolved by the Koszul complex of
> `π^*𝒞 ⊗ 𝒪_E(-1) ⟶ 𝒪_E` (`Stacks.ProjectiveCompletion.koszulResolutionZeroSection`). The rank is
> taken positive, as the factor `(r-1)!` of the source presupposes.
>
> *Why the test schemes `X' ×_X E` are the whole of the second clause.* The composite
> `p^* ∘ π_* ∘ c_r(i_*𝒪_X)` is not a composite of bivariant classes for `C ⟶ E`: `π_*` is proper
> pushforward along `π' : E' ⟶ X'`, which exists only for a test scheme `E'` over `E` that is the
> pullback `X' ×_X E` of a scheme `X'` over `X`, and `p^*` is flat pullback along the bundle
> `p' : X' ×_X C ⟶ X'`. So the composite is an operation `CH_*(X' ×_X E) ⟶ CH_*(X' ×_X C)` for
> each `X' ⟶ X` locally of finite type, and the equality "in `A^0(C → E)`" with
> `(-1)^{r-1}(r-1)! j^*` asserts exactly that these operations agree with `(-1)^{r-1}(r-1)!` times
> restriction to `X' ×_X C`, for every such `X'`. This is the reduction the source makes in its proof
> ("after replacing `X` by a scheme locally of finite type over `X`, it suffices to prove that both
> sides have the same effect on an element `α ∈ CH_*(E)`"), and it is the third conjunct; the second
> is the case `X' = X` read on `E` itself rather than on `X ×_X E`.

```lean
theorem chernClass_pushforward_zeroSection (C : ChowSituation.{u}) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (𝒞 : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒞 r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} 𝒞] (hr : r ≠ 0) :
    haveI := flat_projectiveCompletionProj 𝒞 r
    haveI := locallyOfFiniteType_projectiveCompletionProj 𝒞 r
    (∀ t : ℕ, 0 < t → t < r →
      perfectChernClass C (projectiveCompletionProj 𝒞 ≫ sX)
        (hasDefinedChernClasses_pushforward_zeroSection 𝒞 r) t = 0) ∧
    (∀ (k : ℤ) (α : chowGroup C (𝟙 _ ≫ projectiveCompletionProj 𝒞 ≫ sX) (k + r)),
      chowGroupCast C ((complementOpen 𝒞).ι ≫ 𝟙 _ ≫ projectiveCompletionProj 𝒞 ≫ sX) (by ring)
        (bundlePullback C sX ((complementOpen 𝒞).ι ≫ 𝟙 _ ≫ projectiveCompletionProj 𝒞 ≫ sX)
        ((complementOpen 𝒞).ι ≫ projectiveCompletionProj 𝒞) (by simp) r
        (relativeDimension_complementOpen_ι_comp 𝒞 r) (k + r - r)
        (properChowPushforward C (𝟙 _ ≫ projectiveCompletionProj 𝒞 ≫ sX) sX
          (projectiveCompletionProj 𝒞) (by simp) (k + r - r)
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ sX _ (by simp) _)
          ((perfectChernClass C (projectiveCompletionProj 𝒞 ≫ sX)
            (hasDefinedChernClasses_pushforward_zeroSection 𝒞 r)).op (𝟙 _) (k + r) r α))) =
        ((-1 : ℤ) ^ (r - 1) * (Nat.factorial (r - 1) : ℤ)) •
          chowGroupOpensRestrictOfIsOpenImmersion C (𝟙 _ ≫ projectiveCompletionProj 𝒞 ≫ sX)
            (complementOpen 𝒞) (k + r) α) ∧
    (∀ {X' : Scheme.{u}} (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (g : X' ⟶ X)
      [LocallyOfFiniteType g] (hg : g ≫ sX = sX') (k : ℤ)
      (α : chowGroup C (pullback.snd g (projectiveCompletionProj 𝒞) ≫
        projectiveCompletionProj 𝒞 ≫ sX) (k + r)),
      chowGroupCast C _ (by ring) (bundlePullback C sX'
        ((complementOpenBaseChange g 𝒞).ι ≫ pullback.snd g (projectiveCompletionProj 𝒞) ≫
          projectiveCompletionProj 𝒞 ≫ sX)
        ((complementOpenBaseChange g 𝒞).ι ≫ pullback.fst g (projectiveCompletionProj 𝒞))
        (by rw [Category.assoc, pullback_fst_comp_eq_pullback_snd_comp C sX sX' g hg 𝒞]) r
        (relativeDimension_complementOpenBaseChange g 𝒞 r) (k + r - r)
        (properChowPushforward C
          (pullback.snd g (projectiveCompletionProj 𝒞) ≫ projectiveCompletionProj 𝒞 ≫ sX) sX'
          (pullback.fst g (projectiveCompletionProj 𝒞))
          (pullback_fst_comp_eq_pullback_snd_comp C sX sX' g hg 𝒞) (k + r - r)
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ sX' _
            (pullback_fst_comp_eq_pullback_snd_comp C sX sX' g hg 𝒞) _)
          ((perfectChernClass C (projectiveCompletionProj 𝒞 ≫ sX)
            (hasDefinedChernClasses_pushforward_zeroSection 𝒞 r)).op
            (pullback.snd g (projectiveCompletionProj 𝒞)) (k + r) r α))) =
        ((-1 : ℤ) ^ (r - 1) * (Nat.factorial (r - 1) : ℤ)) •
          chowGroupOpensRestrictOfIsOpenImmersion C
            (pullback.snd g (projectiveCompletionProj 𝒞) ≫ projectiveCompletionProj 𝒞 ≫ sX)
            (complementOpenBaseChange g 𝒞) (k + r) α)
```

## Tag 0FEG, a lemma

[Tag 0FEG](https://stacks.math.columbia.edu/tag/0FEG) in the Stacks Project.

**`Stacks.Chow.isRegularImmersionChernFormula_regularImmersionStructureSheafSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/RegularImmersionChernFormula.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/RegularImmersionChernFormula.lean#L111). The attribute's comment: “the whole lemma: c\_t(Z → X, i\_*O\_Z) = 0 for 0 < t < r and c\_r(Z → X, i\_*O\_Z) = (-1)^\{r-1}(r-1)! c(Z → X, N), for X quasi-compact or with quasi-compact irreducible components and r ≥ 1 (presupposed by (r-1)!)”.

> Let `i : Z ⟶ X` be a regular closed immersion of codimension `r ≥ 1` of schemes locally of
> finite type over the base of chapter 42, with `X` quasi-compact or with quasi-compact irreducible
> components, and `𝒩 = 𝒞_{Z/X}^∨` its normal sheaf. Then `c_t(Z ⟶ X, i_*𝒪_Z) = 0` for
> `t = 1, …, r - 1` and `c_r(Z ⟶ X, i_*𝒪_Z) = (-1)^{r-1}(r-1)! c(Z ⟶ X, 𝒩)` in `A^r(Z ⟶ X)`, the
> localized Chern classes being those of Definition 0FB5
> (`Stacks.Chow.LocalizedSituation.IsRegularImmersionChernFormula` for the situation
> `Stacks.Chow.regularImmersionStructureSheafSituation` of `i_*𝒪_Z`). The codimension is positive, as
> the factor `(r-1)!` of the source presupposes.

```lean
theorem isRegularImmersionChernFormula_regularImmersionStructureSheafSituation (hr : 0 < r) :
    (regularImmersionStructureSheafSituation C sX i hreg hX 0).IsRegularImmersionChernFormula
      (isZeroOnComplement_regularImmersionStructureSheafSituation C sX i hreg hX 0) hreg hr
```

## Tag 0FEH, a lemma

[Tag 0FEH](https://stacks.math.columbia.edu/tag/0FEH) in the Stacks Project.

**`Stacks.Chow.regularImmersionStructureSheafSituation_capFundamentalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/RegularImmersionChernFormula.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/RegularImmersionChernFormula.lean#L146). The attribute's comment: “all four parts, for X quasi-compact or with quasi-compact irreducible components, r ≥ 1 and dim\_δ(X) ≤ n (the source's dim\_δ(X) = n)”.

> Let `i : Z ⟶ X` be a regular closed immersion of codimension `r ≥ 1` of schemes locally of
> finite type over the base, `X` quasi-compact or with quasi-compact irreducible components, and
> `dim_δ(X) ≤ n` (the source's `dim_δ(X) = n`). Then
>
> 1. `c_t(Z ⟶ X, i_*𝒪_Z) ∩ [X]_n = 0` for `1 ≤ t < r`,
> 2. `c_r(Z ⟶ X, i_*𝒪_Z) ∩ [X]_n = (-1)^{r-1}(r-1)! [Z]_{n-r}`,
> 3. `ch_t(Z ⟶ X, i_*𝒪_Z) ∩ [X]_n = 0` for `0 ≤ t < r`, and
> 4. `ch_r(Z ⟶ X, i_*𝒪_Z) ∩ [X]_n = [Z]_{n-r}`,
>
> with `c_t(Z ⟶ X, i_*𝒪_Z)` the class of Stacks 0FB2 for the situation in degree `t`.

```lean
theorem regularImmersionStructureSheafSituation_capFundamentalClass (hr : 0 < r) (n : ℤ)
    (hXn : schemeDeltaDimension C sX ≤ (n : EInt)) :
    (∀ (t : ℕ) (ht : 0 < t), t < r →
      capFundamentalClassAt C (gysinSystemOfInvertible C) (i ≫ sX) sX i rfl t n
        ((regularImmersionStructureSheafSituation C sX i hreg hX t).localizedChern
          (isFiniteLocallyFreeOfRankLTOnComplement_regularImmersionStructureSheafSituation C sX
            i hreg hX ht)) = 0) ∧
    capFundamentalClassAt C (gysinSystemOfInvertible C) (i ≫ sX) sX i rfl r n
        ((regularImmersionStructureSheafSituation C sX i hreg hX r).localizedChern
          (isFiniteLocallyFreeOfRankLTOnComplement_regularImmersionStructureSheafSituation C sX
            i hreg hX hr)) =
      ((-1 : ℤ) ^ (r - 1) * ((r - 1).factorial : ℤ)) • fundamentalChowClass C (i ≫ sX) (n - r) ∧
    (∀ t : ℕ, t < r →
      (capFundamentalClassAt C (gysinSystemOfInvertible C) (i ≫ sX) sX i rfl t
          n).toIntLinearMap.lTensor ℚ
        ((regularImmersionStructureSheafSituation C sX i hreg hX 0).localizedChernChar
          (isZeroOnComplement_regularImmersionStructureSheafSituation C sX i hreg hX 0) t) = 0) ∧
    (capFundamentalClassAt C (gysinSystemOfInvertible C) (i ≫ sX) sX i rfl r
        n).toIntLinearMap.lTensor ℚ
        ((regularImmersionStructureSheafSituation C sX i hreg hX 0).localizedChernChar
          (isZeroOnComplement_regularImmersionStructureSheafSituation C sX i hreg hX 0) r) =
      (1 : ℚ) ⊗ₜ[ℤ] fundamentalChowClass C (i ≫ sX) (n - r)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.55, Tag 0FED](https://stacks.math.columbia.edu/tag/0FED)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
