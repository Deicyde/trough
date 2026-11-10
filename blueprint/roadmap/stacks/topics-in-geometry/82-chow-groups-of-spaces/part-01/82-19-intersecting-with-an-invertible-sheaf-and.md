---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.orderOfVanishingSection_eq_multiplicity_mul, AlgebraicGeometry.Space.flatPullbackMap_sectionWeilDivisor_eq_componentDivisorSum, AlgebraicGeometry.Space.flatCyclePullback_firstChernCapCycleMap, AlgebraicGeometry.Space.flatPullback_firstChernClassCap, AlgebraicGeometry.Space.flatPullbackChowMapCanonical_canonicalFirstChernCapCanonical, AlgebraicGeometry.Space.properPushforward_divisorCycleOfSection_eq_iff, AlgebraicGeometry.Space.properPushforward_divisorCycleOfSection, AlgebraicGeometry.Space.properPushforward_firstChernClassCapFundamental_of_normRule
statement: formalized
proof: formalized
---

# 82.19 Intersecting with an invertible sheaf and push and pull

Section 82.19 of the Stacks Project, [Tag 0EQP](https://stacks.math.columbia.edu/tag/0EQP). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQQ, a lemma

[Tag 0EQQ](https://stacks.math.columbia.edu/tag/0EQQ) in the Stacks Project.

**`AlgebraicGeometry.Space.orderOfVanishingSection_eq_multiplicity_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean#L439). The attribute's comment: “coefficientwise at a prime divisor Z of X with generic point ξ lying over a prime divisor Z' of Y with generic point ξ': the order of vanishing of a meromorphic section pulls back with the multiplicity, ord_{Z,f^*L}(f^*s) = m · ord_{Z',L}(s), where m is the colength of the extended maximal ideal — the multiplicity with which Z occurs in f^{-1}(Z'), hence the coefficient the flat pullback of Stacks 0EP8 attaches to Z. PROVED, not assumed: that the order of vanishing multiplies by the multiplicity, from Stacks 02M1 (length_baseChange_eq_length_mul_length_quotient) applied to the cyclic modules O^h/a and O^h/b. For X integral this is the source's identity f^* div_L(s) = ∑ n_i div_{f^*L|_{X_i}}(s_i) in Z_{n+r-1}(X) read at the coefficient of Z, the one component having multiplicity one; the statement is coefficientwise because the flat pullback of cycles is Stacks 0EP8, which this repository does not have, and for the same reason Stacks 0EPV is already carried coefficientwise here. NOT COVERED: for X with several irreducible components, the step from this identity to the cycle identity, namely the additivity over the components of the multiplicities n_i = m_{X_i,X} of Stacks 0EE2 and Stacks 0EE9; the statement applies to X and to each component X_i separately, with m read in each, but no additivity of those multiplicities is proved in this repository. RESTRICTED: carried as explicit named hypotheses are (i) the flat local homomorphism φ of the henselian local rings at the generic points, with hloc and hflat; (ii) the module N and the meromorphic section fs standing for f^*L and f^*s, this repository having no pullback of a meromorphic section along a morphism of algebraic spaces, together with hfs, that the ratio of fs at ξ against the pulled-back generator is the image under φ of the ratio of s at ξ' — which is the source's own step of writing s/s_{ξ'} = a/b and pulling the fraction back, the chartwise rule a/b ↦ f-sharp a / f-sharp b of Stacks 0ENC; (iii) the ratios of Stacks 0EPR at the two generic points as the parameters ratioY and ratioX, exactly as Stacks 0EPR and 0EPV carry them; and (iv) finiteness of the multiplicity, as hm naming the natural number m it equals. The source's reduction through the multiplicative torsor of Stacks 0EQG is not used: the length computation is the same one and is carried out directly on the ratio”.

> **Stacks 0EQQ, coefficientwise.** *The order of vanishing of a meromorphic section pulls
> back with multiplicities.* Let `f : X ⟶ Y` be flat, let `ℒ` be an `𝒪_Y`-module and `𝒩` an
> `𝒪_X`-module standing for `f^*ℒ`, let `Z' ⊆ Y` and `Z ⊆ X` be prime divisors with `Z` over `Z'`,
> and let `m` be the multiplicity of `Z` over `Z'` along the induced flat local homomorphism `φ`.
> For a nonzero meromorphic section `s` of `ℒ` whose ratio `s / s_{ξ'}` at `ξ'` is `a / b`, and for
> a meromorphic section `fs` of `𝒩` standing for `f^*s`, whose ratio at `ξ` against the
> pulled-back generator is therefore `φ(a) / φ(b)`,
>
>   `ord_{Z,𝒩}(fs) = m · ord_{Z',ℒ}(s)`.
>
> The multiplicity `m` is the one with which `Z` occurs in `f^{-1}(Z')`, so for `X` integral this
> is the source's identity `f^* div_ℒ(s) = ∑ n_i div_{f^*ℒ|_{X_i}}(s_i)` read at the coefficient
> of `Z`; for `X` with several components it is each of the two readings of that identity, as the
> implementation notes explain. The source proves it by passing to the multiplicative torsor
> `q : T ⟶ Y`, where the section becomes a rational function, and then invoking Stacks 0EQA; here
> the two are the same length computation, read on the ratio parameter of Stacks 0EPR rather than
> on an embedding of the function field.

```lean
theorem orderOfVanishingSection_eq_multiplicity_mul
    (hloc : IsLocalHom φ) (hflat : φ.Flat) {m : ℕ}
    (hm : primeDivisorFlatMultiplicity B S hS hX hdecX ZX hY hdecY ZY φ = (m : ℕ∞))
    (L : Modules.{u, max u z} B S hS Y hY) (N : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS Y hY L)
    (fs : MeromorphicSection.{u, z} B S hS X hX N)
    (ratioY : LocalRatio.{u, z} B S hS hY hdecY ZY L)
    (ratioX : LocalRatio.{u, z} B S hS hX hdecX ZX N)
    (a b : nonZeroDivisors ↥(ZY.genericHenselianLocalRing B S hS hY hdecY))
    (hs : (ratioY s : ZY.genericTotalFractionRing B S hS hY hdecY) =
      IsLocalization.mk' (ZY.genericTotalFractionRing B S hS hY hdecY)
        (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)) b)
    (hfs : (ratioX fs : ZX.genericTotalFractionRing B S hS hX hdecX) =
      IsLocalization.mk' (ZX.genericTotalFractionRing B S hS hX hdecX)
        (φ (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)))
        (⟨φ (b : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)),
          Ring.map_mem_nonZeroDivisors_of_flatHom hflat b.2⟩ :
          nonZeroDivisors ↥(ZX.genericHenselianLocalRing B S hS hX hdecX))) :
    orderOfVanishingSection.{u, z} B S hS hX hdecX ZX N fs ratioX =
      (m : ℤ) * orderOfVanishingSection.{u, z} B S hS hY hdecY ZY L s ratioY
```

**`AlgebraicGeometry.Space.flatPullbackMap_sectionWeilDivisor_eq_componentDivisorSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackSectionWeilDivisor.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackSectionWeilDivisor.lean#L85).

> In Situation 0EDT let `X/B` and `Y/B` be good, let `f : X ⟶ Y` be a morphism over `B` which
> is flat of relative dimension `r`, let `ℒ` be an invertible `𝒪_Y`-module, assume `Y` is integral
> with `n = dim_δ(Y)`, and let `s` be a nonzero meromorphic section of `ℒ`. Then
>
>   `f^* div_ℒ(s) = ∑ n_i div_{f^*ℒ|_{X_i}}(s_i)`
>
> in `Z_{n + r - 1}(X)`: the left-hand side is the flat pullback (Stacks 0EP8) of the Weil divisor
> `div_ℒ(s)` (Stacks 0EQE); on the right the sum runs over the irreducible components `X_i ⊂ X`
> of δ-dimension `n + r`, `s_i = f|_{X_i}^*(s)` is the pullback of `s` (Stacks 0ENC), a nonzero
> meromorphic section of the invertible module `f^*ℒ|_{X_i} = f|_{X_i}^*ℒ`,
> `div_{f^*ℒ|_{X_i}}(s_i)` is its Weil divisor on `X_i` pushed forward to `X`, and
> `n_i = m_{X_i, X}` is the multiplicity of `X_i` in `X` (Stacks 0EE9).

```lean
theorem flatPullbackMap_sectionWeilDivisor_eq_componentDivisorSum :
    flatPullbackMap D sX hX sY hY f hbase r hflat hr (n - 1) (n + r - 1) (by ring)
        (sectionWeilDivisor D sY hY hintY L hL hn s hs) =
      componentDivisorSum D sX hX sY hY f r hflat hintY (n := n) L hL s hs
```

## Tag 0EQR, a lemma

[Tag 0EQR](https://stacks.math.columbia.edu/tag/0EQR) in the Stacks Project.

**`AlgebraicGeometry.Space.flatCyclePullback_firstChernCapCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCap.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCap.lean#L783). The attribute's comment: “as an identity of cycles in Z_{k+r}(X) rather than of classes in CH, which is the finer statement and implies the source's once the class maps are known compatible — see flatPullback_firstChernClassCap, which states the source's own grading. The cap product is the cap product of Stacks 0EQJ as carried in this repository, firstChernCapCycleMap, so the component cycle c_1(L|_W) ∩ [W] remains an explicit parameter standing in for Stacks 0EQE, which does not exist for algebraic spaces here. PROVED, not assumed: the commutation itself. At a single integral closed subspace W both coefficients collapse to one term and those terms are equal by the pointwise Stacks 0EQQ (orderOfVanishingSection_eq_multiplicity_mul); the passage to a general cycle is the locally finite bookkeeping the source performs by appealing to Remark 0EQ8, and it is carried out here by exchanging two double sums. No additive map is assumed to commute with the cap product and no conjunct of the conclusion is a hypothesis. RESTRICTED: carried as explicit named hypotheses are (i) the flat pullback of cycles of Stacks 0EP8, which this repository does not construct, carried as FlatCyclePullback, that is TOGETHER WITH ITS DEFINING FORMULA: a multiplicity mult W T for each pair of integral closed subspaces, the maps Z_m(Y) → Z_n(X) for m + r = n, the statement that the coefficient of f^*α at T is ∑ α_W · mult W T, and that f^*[W] is carried by f^{-1}(W); (ii) the Weil divisor presentations of Stacks 0EQE for the two component rules, exactly as Stacks 0EQK carries them, with the sheaves L|_W and f^*L|_{f^{-1}(W)} and the sections s and f^*s as unconstrained parameters identified by their ratios at the generic points, as in the carried Stacks 0EQQ, this repository having no pullback of a sheaf of modules or of a meromorphic section along a morphism of algebraic spaces; (iii) at each prime divisor of f^{-1}(W) the flat local homomorphism of henselian local rings over the prime divisor of W beneath it, with its locality and flatness, as in the carried Stacks 0EQA and 0EQQ; and (iv) the identification of the multiplicity Stacks 0EP8 attaches to that prime divisor with the colength primeDivisorFlatMultiplicity, which is Stacks 0EE9 read along a flat morphism and is not proved here. The inverse image of each integral closed subspace occurring in α is assumed INTEGRAL, which is the case i = 1, n_1 = 1 of the source's sum over the irreducible components of f^{-1}(W); the step to several components is the additivity over them of the multiplicities of Stacks 0EE2 and Stacks 0EE9, which is NOT COVERED by Stacks 0EQA and 0EQQ as stated here, and it is NOT COVERED here either”.

> **Stacks 0EQR, as an identity of cycles.** In Situation 0EDT let `X/B` and `Y/B` be good,
> let `f : X ⟶ Y` be flat of relative dimension `r`, let `ℒ` be an invertible `O_Y`-module and let
> `α` be a `(k+1)`-cycle on `Y`.  Then
>
>   `f^*(c₁(ℒ) ∩ α) = c₁(f^*ℒ) ∩ f^*α`
>
> in `Z_{k+r}(X)`.
>
> The cap product is the carried Stacks 0EQJ at the level of cycles,
> `AlgebraicGeometry.Space.firstChernCapCycleMap`, whose component rule is an explicit parameter;
> the flat pullback is the carried Stacks 0EP8, whose defining formula is the field
> `AlgebraicGeometry.Space.FlatCyclePullback.coeff`.  The identity of cycles is finer than the
> source's identity of classes in `CH_{k+r-1}(X)`, which it implies; see
> `AlgebraicGeometry.Space.flatPullback_firstChernClassCap`.
>
> Nothing about either side of the equality is assumed.  At a single integral closed subspace the
> identity is `AlgebraicGeometry.Space.flatCyclePullback_mult_firstChernComponentCycle`, whose
> content is the pointwise Stacks 0EQQ; the passage to a general cycle exchanges two locally
> finite double sums, which is the bookkeeping the source performs through Remark 0EQ8.

```lean
theorem flatCyclePullback_firstChernCapCycleMap
    (_hflat : IsFlat D.site D.base D.base_mem f)
    (_hr : HasRelativeDimension r D.site D.base D.base_mem f)
    (cmp : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem Y)
      (hW : deltaDimension D sY W = k + 1),
      FlatChernDivisorComparison D sX hX sY hY f r k pb setupY setupX chernY chernX W hW)
    (α : CycleGroup D sY (k + 1)) :
    pb.map k (k + (r : ℤ)) rfl (firstChernCapCycleMap D sY hY k chernY α) =
      firstChernCapCycleMap D sX hX (k + (r : ℤ)) chernX
        (pb.map (k + 1) (k + (r : ℤ) + 1) (by ring) α)
```

**`AlgebraicGeometry.Space.flatPullback_firstChernClassCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCap.lean, line 902](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCap.lean#L902). The attribute's comment: “the source's own grading: f^*(c_1(L) ∩ α) = c_1(f^*L) ∩ f^*α in the Chow groups, for the cap product of Stacks 0EQJ as carried here, so the component cycle c_1(L|_W) ∩ [W] and the Chow groups CH of Stacks 0EQ6 remain explicit parameters, standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)-(4). PROVED, not assumed: the commutation, which is flatCyclePullback_firstChernCapCycleMap — the identity of cycles whose content is the pointwise Stacks 0EQQ — read through the two class maps. RESTRICTED: in addition to the hypotheses of flatCyclePullback_firstChernCapCycleMap, which are listed on it (the flat pullback of cycles of Stacks 0EP8 with its defining formula; the Weil divisor presentations of Stacks 0EQE; the flat local homomorphisms of henselian local rings; the identification of the multiplicity of Stacks 0EP8 with the colength; and the inverse image of each integral closed subspace occurring in α assumed integral), the flat pullback on the Chow groups is the parameter fstarCH together with hclass, that it is induced by the flat pullback of cycles — which is Stacks 0EQ9, that flat pullback respects rational equivalence, and says nothing about the cap product. The invertible sheaves L on Y and N on X, the latter standing for f^*L, are unconstrained parameters as they are in the carried Stacks 0EQQ and as they are for firstChernClassCap itself, which does not consume them”.

> **Stacks 0EQR.** In Situation 0EDT let `X/B` and `Y/B` be good, let `f : X ⟶ Y` be flat of
> relative dimension `r`, let `ℒ` be an invertible `O_Y`-module and let `α` be a `(k+1)`-cycle on
> `Y`.  Then
>
>   `f^*(c₁(ℒ) ∩ α) = c₁(f^*ℒ) ∩ f^*α`
>
> in `CH_{k+r}(X)`, for the cap product of Stacks 0EQJ as carried in this repository.
>
> This is `AlgebraicGeometry.Space.flatCyclePullback_firstChernCapCycleMap` composed with the class
> maps of the two Chow groups.  The flat pullback on Chow groups is the parameter `fstarCH`, and
> all that is asked of it is that it be induced by the flat pullback of cycles, which is the
> content of Stacks 0EQ9 — that flat pullback respects rational equivalence — and is the
> hypothesis `hclass`.  That hypothesis says nothing about the cap product.

```lean
theorem flatPullback_firstChernClassCap
    (_hflat : IsFlat D.site D.base D.base_mem f)
    (_hr : HasRelativeDimension r D.site D.base D.base_mem f)
    (cmp : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem Y)
      (hW : deltaDimension D sY W = k + 1),
      FlatChernDivisorComparison D sX hX sY hY f r k pb setupY setupX chernY chernX W hW)
    (L : Modules.{u, u} D.site D.base D.base_mem Y hY.1)
    (hL : IsInvertibleSheaf D sY hY L)
    (N : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hN : IsInvertibleSheaf D sX hX N)
    {CHY : Type w} [AddCommGroup CHY] (chowY : ChowTarget.{u, w, v} D sY hY k CHY)
    {CHX : Type w} [AddCommGroup CHX]
    (chowX : ChowTarget.{u, w, v} D sX hX (k + (r : ℤ)) CHX)
    (fstarCH : CHY →+ CHX)
    (hclass : ∀ β : CycleGroup D sY k,
      chowX.cls (pb.map k (k + (r : ℤ)) rfl β) = fstarCH (chowY.cls β))
    (α : CycleGroup D sY (k + 1)) :
    fstarCH (firstChernClassCap D sY hY L k hL chernY chowY α) =
      firstChernClassCap D sX hX N (k + (r : ℤ)) hN chernX chowX
        (pb.map (k + 1) (k + (r : ℤ) + 1) (by ring) α)
```

**`AlgebraicGeometry.Space.flatPullbackChowMapCanonical_canonicalFirstChernCapCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCapCanonical.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackFirstChernCapCanonical.lean#L222).

> **Stacks 0EQR.**  In Situation 0EDT let `X, Y/B` be good, let `f : X ⟶ Y` be flat of relative
> dimension `r`, let `ℒ` be an invertible `𝒪_Y`-module and let `α` be a `(k+1)`-cycle on `Y`.  Then
>
>   `f^*(c₁(ℒ) ∩ α) = c₁(f^*ℒ) ∩ f^*α`
>
> in `CH_{k+r}(X)`.  Here `c₁(ℒ) ∩ - : Z_{k+1}(Y) → CH_k(Y)` is the cap product of Stacks 0EQJ
> (`canonicalFirstChernCapCanonical`) into the Chow group `CH_k(Y)` of Stacks 0EQ6 at the canonical
> embeddings of Stacks 0ENK, `f^* : CH_k(Y) → CH_{k+r}(X)` is the flat pullback on Chow groups of
> Stacks 0EQB (`flatPullbackChowMapCanonical`), `f^*α` is the flat pullback of cycles of Stacks 0EP8
> (`flatPullbackMap`) and `f^*ℒ` is the inverse image of Stacks 03LU (`modulePullback`).  The
> source's `k`-cycle and `CH_{k+r-1}` are this statement's `(k+1)`-cycle and `CH_{k+r}`.

```lean
theorem flatPullbackChowMapCanonical_canonicalFirstChernCapCanonical
    (α : CycleGroup D sY (k + 1)) :
    flatPullbackChowMapCanonical.{u + 1} D sX hX sY hY f hbase r hflat hr k (k + (r : ℤ)) rfl
        (canonicalFirstChernCapCanonical.{u + 1} D sY hY L hL k α) =
      canonicalFirstChernCapCanonical.{u + 1} D sX hX
        ((modulePullback D.site D.base D.base_mem
          (ObjectProperty.homMk f : (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
            ⟨Y, hY.1⟩)).obj L)
        (modulePullbackInvertible
          (ObjectProperty.homMk f : (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
            ⟨Y, hY.1⟩) L hL) (k + (r : ℤ))
        (flatPullbackMap D sX hX sY hY f hbase r hflat hr (k + 1) (k + (r : ℤ) + 1) (by ring)
          α)
```

## Tag 0EQS, a lemma

[Tag 0EQS](https://stacks.math.columbia.edu/tag/0EQS) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushforward_divisorCycleOfSection_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean#L528). The attribute's comment: “first conclusion REDUCED, not proved: f_*(div_{f^*L}(f^*s)) = [R(X):R(Y)] div_L(s) in Z_{n-1}(Y) IF AND ONLY IF it holds at every prime divisor of Y; proved away from them, using dim_δ(X) = dim_δ(Y); f^*L and f^*s are the unconstrained parameters LX and σX”.

> **Stacks 0EQS, the identity in `Z_{n-1}(Y)`, reduced to its coefficients at the prime
> divisors of `Y`.** In Situation 0EDT let `X/B` and `Y/B` be good, let `f : X ⟶ Y` be dominant
> and quasi-compact over `B`, let `X` and `Y` be integral with `dim_δ(X) = dim_δ(Y) = n`, let `ℒ`
> be an invertible `𝒪_Y`-module and let `s` be a nonzero meromorphic section of `ℒ`. Then
>
> `f_*(div_{f^*ℒ}(f^*s)) = [R(X) : R(Y)] div_ℒ(s)` in `Z_{n-1}(Y)`
>
> holds exactly when it holds coefficientwise at every prime divisor of `Y`, that is when
>
> `∑_Z ord_{Z, f^*ℒ}(f^*s) · deg(Z/Z') = [R(X) : R(Y)] · ord_{Z', ℒ}(s)`
>
> for every prime divisor `Z' ⊆ Y`, the sum being over the integral closed subspaces `Z ⊆ X`.
>
> Both sides are coefficient families on the integral closed subspaces of `Y`, and away from the
> prime divisors of `Y` both vanish: the coefficient of `div_ℒ(s)` at an integral closed subspace
> whose point set does not have codimension one is zero by Stacks 0EQE, part (1), and the
> pushforward has no contribution there by
> `AlgebraicGeometry.Space.properPushforwardCoeff_divisorCycleCoefficients_eq_zero`, which is
> where the equality of the δ-dimensions is used. That is the whole content of the reduction; the
> coefficient identity at a prime divisor of `Y` is *not* proved here.

```lean
theorem properPushforward_divisorCycleOfSection_eq_iff (_hL : IsInvertibleSheaf D sY hY L)
    {f : X ⟶ Y} (hfB : f ≫ sY = sX) (hf : IsQuasiCompact D.site D.base D.base_mem f)
    (_hdom : IsDominant D.site D.base D.base_mem f)
    (hDvX : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdecX LX σX ratioX W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hDvY : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem Y =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hY.1 hdecY L σ ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem Y) :
    properCyclePushforward D sX hX sY hY hfB hf (n - 1)
          (divisorCycleOfSection D sX hX hdecX LX σX ratioX hDvX hintX dX hdX hnX) =
        (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
          divisorCycleOfSection D sY hY hdecY L σ ratio hDvY hintY dY hdY hnY ↔
      ∀ W : PrimeDivisor D.site D.base D.base_mem Y,
        (∑ᶠ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
            divisorCycleCoefficients D sX hX hdecX LX σX ratioX Z *
              properCycleMult D sX hX sY hY f Z
                (W.toIntegralClosedSubspace D.site D.base D.base_mem)) =
          (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) *
            divisorCoefficients.{u, u} D.site D.base D.base_mem hY.1 hdecY L σ ratio W
```

**`AlgebraicGeometry.Space.properPushforward_divisorCycleOfSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean#L622). The attribute's comment: “first conclusion: f_*(div_{f^*L}(f^*s)) = [R(X):R(Y)] div_L(s) in Z_{n-1}(Y), resting on the single carried input ProperPushforwardNormRule — Stacks 0EQ4 at the prime divisors of Y, which this repository does not have; f^*L and f^*s are the parameters LX, σX”.

> **Stacks 0EQS, first conclusion.** In Situation 0EDT let `X/B` and `Y/B` be good, let
> `f : X ⟶ Y` be dominant and quasi-compact over `B`, let `X` and `Y` be integral with
> `dim_δ(X) = dim_δ(Y) = n`, let `ℒ` be an invertible `𝒪_Y`-module and let `s` be a nonzero
> meromorphic section of `ℒ`. Then
>
> `f_*(div_{f^*ℒ}(f^*s)) = [R(X) : R(Y)] div_ℒ(s)` in `Z_{n-1}(Y)`.
>
> This is the plain equality the source asserts, resting on the single carried input
> `AlgebraicGeometry.Space.ProperPushforwardNormRule`, which is Stacks 0EQ4 at the prime divisors
> of `Y`. Everything else — that the two coefficient families agree away from the prime divisors
> of `Y`, which is where `dim_δ(X) = dim_δ(Y)` is used — is proved, in
> `AlgebraicGeometry.Space.properPushforward_divisorCycleOfSection_eq_iff`.

```lean
theorem properPushforward_divisorCycleOfSection (hL : IsInvertibleSheaf D sY hY L)
    {f : X ⟶ Y} (hfB : f ≫ sY = sX) (hf : IsQuasiCompact D.site D.base D.base_mem f)
    (hdom : IsDominant D.site D.base D.base_mem f)
    (hDvX : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdecX LX σX ratioX W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hDvY : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem Y =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hY.1 hdecY L σ ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem Y)
    (hnorm : ProperPushforwardNormRule D sX hX sY hY hdecX hdecY LX σX ratioX L σ ratio
      hintX f) :
    properCyclePushforward D sX hX sY hY hfB hf (n - 1)
        (divisorCycleOfSection D sX hX hdecX LX σX ratioX hDvX hintX dX hdX hnX) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
        divisorCycleOfSection D sY hY hdecY L σ ratio hDvY hintY dY hdY hnY
```

**`AlgebraicGeometry.Space.properPushforward_firstChernClassCapFundamental_of_normRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean#L653). The attribute's comment: “second conclusion: f_*(c_1(f^*L) ∩ [X]) = c_1(L) ∩ f_*[X] in CH_{n-1}(Y), resting on the same carried ProperPushforwardNormRule; the right side is [R(X):R(Y)] · (c_1(L) ∩ [Y]) by the proved f_*[X] = [R(X):R(Y)][Y], the left the class on Y of the pushforward cycle”.

> **Stacks 0EQS, second conclusion.** In the situation above,
>
> `f_*(c₁(f^*ℒ) ∩ [X]) = c₁(ℒ) ∩ f_*[X]` in `CH_{n-1}(Y)`,
>
> the right side being `[R(X) : R(Y)] · (c₁(ℒ) ∩ [Y])` by
> `AlgebraicGeometry.Space.properPushforward_integralCycle_integralClosedSubspaceUniv`, which is
> `f_*[X] = [R(X) : R(Y)] [Y]`.
>
> This rests on the same single carried input as the first conclusion; it is not conditional on
> the first conclusion, which is proved from that input.

```lean
theorem properPushforward_firstChernClassCapFundamental_of_normRule
    (hL : IsInvertibleSheaf D sY hY L)
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sY hY (n - 1) CH)
    {f : X ⟶ Y} (hfB : f ≫ sY = sX) (hf : IsQuasiCompact D.site D.base D.base_mem f)
    (hdom : IsDominant D.site D.base D.base_mem f)
    (hDvX : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdecX LX σX ratioX W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hDvY : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem Y =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hY.1 hdecY L σ ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem Y)
    (hnorm : ProperPushforwardNormRule D sX hX sY hY hdecX hdecY LX σX ratioX L σ ratio
      hintX f) :
    chow.cls (properCyclePushforward D sX hX sY hY hfB hf (n - 1)
        (divisorCycleOfSection D sX hX hdecX LX σX ratioX hDvX hintX dX hdX hnX)) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
        firstChernClassCapFundamental D sY hY hdecY L chow σ ratio hDvY hintY dY hdY hnY
```

**`AlgebraicGeometry.Space.properPushforward_firstChernClassCapFundamental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean#L697). The attribute's comment: “second conclusion, DERIVED from the first (the hypothesis heq): f_*(c_1(f^*L) ∩ [X]) = c_1(L) ∩ f_*[X] in CH_{n-1}(Y), right side read as [R(X):R(Y)] · (c_1(L) ∩ [Y]) via f_*[X] = [R(X):R(Y)][Y], left side as the class on Y of the pushforward CYCLE”.

> **Stacks 0EQS, the identity in `CH_{n-1}(Y)`, from the identity in `Z_{n-1}(Y)`.** In the
> situation above, if
>
> `f_*(div_{f^*ℒ}(f^*s)) = [R(X) : R(Y)] div_ℒ(s)` in `Z_{n-1}(Y)`,
>
> which is the first conclusion of the source and the hypothesis `heq`, then
>
> `f_*(c₁(f^*ℒ) ∩ [X]) = c₁(ℒ) ∩ f_*[X]` in `CH_{n-1}(Y)`,
>
> the right side being `[R(X) : R(Y)] · (c₁(ℒ) ∩ [Y])` by `f_*[X] = [R(X) : R(Y)] [Y]`.
>
> This is the source's own derivation of its second conclusion from its first. On the left,
> `c₁(f^*ℒ) ∩ [X]` is by Stacks 0EQE, part (2), the class of `div_{f^*ℒ}(f^*s)`, and proper
> pushforward on Chow groups is not available here, only on cycles, so the left side is the class
> on `Y` of the pushforward cycle — the same reading the carried Stacks 0EQJ, case (1), uses for
> `i_*`. On the right, `c₁(ℒ) ∩ [Y]` is again Stacks 0EQE, part (2),
> `AlgebraicGeometry.Space.firstChernClassCapFundamental`, a class independent of the chosen
> nonzero meromorphic section by
> `AlgebraicGeometry.Space.firstChernClassCapFundamental_eq`, so the second identity is the image
> of the first under the class map of the Chow group.

```lean
theorem properPushforward_firstChernClassCapFundamental (_hL : IsInvertibleSheaf D sY hY L)
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sY hY (n - 1) CH)
    {f : X ⟶ Y} (hfB : f ≫ sY = sX) (hf : IsQuasiCompact D.site D.base D.base_mem f)
    (_hdom : IsDominant D.site D.base D.base_mem f)
    (hDvX : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdecX LX σX ratioX W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hDvY : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem Y =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hY.1 hdecY L σ ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem Y)
    (heq : properCyclePushforward D sX hX sY hY hfB hf (n - 1)
        (divisorCycleOfSection D sX hX hdecX LX σX ratioX hDvX hintX dX hdX hnX) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
        divisorCycleOfSection D sY hY hdecY L σ ratio hDvY hintY dY hdY hnY) :
    chow.cls (properCyclePushforward D sX hX sY hY hfB hf (n - 1)
        (divisorCycleOfSection D sX hX hdecX LX σX ratioX hDvX hintX dX hdX hnX)) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
        firstChernClassCapFundamental D sY hY hdecY L chow σ ratio hDvY hintY dY hdY hnY
```

**`AlgebraicGeometry.Space.properCyclePushforward_canonicalDivisorCycle_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorCanonical.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorCanonical.lean#L435). The attribute's comment: “first conclusion: f_*(div_{f^*L}(f^*s)) = [R(X):R(Y)] div_L(s) in Z_{n-1}(Y), for f : X → Y proper and dominant of good integral spaces with dim_δ X = dim_δ Y = n, L invertible on Y, s a nonzero meromorphic section; f^*L, f^*s, div (0EQE (1) at the canonical generators of 0EPR), f_* and [R(X):R(Y)] all constructed; nothing carried”. References: EGA IV (21.10.19), “special case”.

> In Situation 0EDT let `X/B` and `Y/B` be good, let `f : X ⟶ Y` be a proper morphism, let `ℒ`
> be an invertible `𝒪_Y`-module, assume `X` and `Y` integral, `f` dominant and
> `dim_δ(X) = dim_δ(Y) = n`, and let `s` be a nonzero meromorphic section of `ℒ`. Then
>
> `f_*(div_{f^*ℒ}(f^*s)) = [R(X) : R(Y)] div_ℒ(s)` in `Z_{n-1}(Y)`.
>
> Here `f^*ℒ` is the inverse image `AlgebraicGeometry.Space.modulePullback` (invertible by
> `AlgebraicGeometry.Space.modulePullbackInvertible`), `f^*s` is the pullback of meromorphic
> sections, defined because `f` carries the generic point of `X` to the generic point of `Y`
> (`AlgebraicGeometry.Space.pullbacksMeromorphicSections_of_genericPoint`, from dominance), and it
> is nonzero because `f^*` preserves regular meromorphic sections; `div` is the Weil divisor of
> Stacks 0EQE, part (1), at the canonical generators of Stacks 0EPR, `f_*` is proper pushforward
> of cycles (Stacks 0EP2) and `[R(X) : R(Y)]` is the degree of the extension of function fields
> (Stacks 0ENY).

```lean
theorem properCyclePushforward_canonicalDivisorCycle_pullback {f : X ⟶ Y} (hfB : f ≫ sY = sX)
    (hf : IsProper D.site D.base D.base_mem f) (hdom : IsDominant D.site D.base D.base_mem f)
    {n : ℤ} (hnX : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hnY : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (n : EInt)) (hσ : σ ≠ 0) :
    properCyclePushforward D sX hX sY hY hfB hf.2.1.2 (n - 1)
        (canonicalDivisorCycle D sX hX hintX
          ((modulePullback D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f)).obj L)
          (modulePullbackInvertible (goodSpacesHom D sX hX sY hY f) L hL)
          (pullbackMeromorphicSection D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f) L
            (pullbacksMeromorphicSections_of_genericPoint D.site D.base D.base_mem (Z := ⟨X, hX.1⟩)
              (Y := ⟨Y, hY.1⟩) hintX hintY f
              (pointsMap_genericPoint_of_isDominant D.site D.base D.base_mem hX.1 hY.1 hintX hintY
                f hdom)) σ)
          (isRegularMeromorphicSection_pullbackMeromorphicSection D.site D.base D.base_mem
            (goodSpacesHom D sX hX sY hY f)
            (pullbacksMeromorphicSections_of_genericPoint D.site D.base D.base_mem (Z := ⟨X, hX.1⟩)
              (Y := ⟨Y, hY.1⟩) hintX hintY f
              (pointsMap_genericPoint_of_isDominant D.site D.base D.base_mem hX.1 hY.1 hintX hintY
                f hdom)) L
            (Stacks.SheafOfModules.IsInvertible.toAlgebraicGeometry _ _ _ hL) σ
            ((isRegularMeromorphicSection_iff_ne_zero D.site D.base D.base_mem hY.1 hintY
              (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sY hY) L hL σ).2 hσ)) hnX) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
        canonicalDivisorCycle D sY hY hintY L hL σ
          ((isRegularMeromorphicSection_iff_ne_zero D.site D.base D.base_mem hY.1 hintY
            (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sY hY) L hL σ).2 hσ) hnY
```

**`AlgebraicGeometry.Space.properCyclePushforward_sectionWeilDivisor_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorCanonical.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorCanonical.lean#L553). The attribute's comment: “both conclusions: f_*(div_{f^*L}(f^*s)) = [R(X):R(Y)] div_L(s) in Z_{n-1}(Y), and f_*(c_1(f^*L) ∩ [X]) = c_1(L) ∩ f_*[X] = [R(X):R(Y)] (c_1(L) ∩ [Y]) in CH_{n-1}(Y), for f : X → Y proper and dominant of good integral spaces with dim_δ X = dim_δ Y = n, L invertible on Y, s a nonzero meromorphic section; div and c_1(-) ∩ [-] are Stacks 0EQE (1) and (2), f^*L, f^*s, f_* and [R(X):R(Y)] constructed; the left side of the second identity is the class of the pushforward of the cycle div_{f^*L}(f^*s) representing c_1(f^*L) ∩ [X]; nothing carried”.

> In Situation 0EDT let `X/B` and `Y/B` be good, let `f : X ⟶ Y` be a proper morphism, let `ℒ`
> be an invertible `𝒪_Y`-module, assume `X` and `Y` integral, `f` dominant and
> `dim_δ(X) = dim_δ(Y) = n`, and let `s` be a nonzero meromorphic section of `ℒ`. Then
>
> `f_*(div_{f^*ℒ}(f^*s)) = [R(X) : R(Y)] div_ℒ(s)` as cycles on `Y`, in `Z_{n-1}(Y)`,
>
> and in particular
>
> `f_*(c₁(f^*ℒ) ∩ [X]) = c₁(ℒ) ∩ f_*[X]` in `CH_{n-1}(Y)`.
>
> `div` is the Weil divisor `AlgebraicGeometry.Space.sectionWeilDivisor` of Stacks 0EQE, part
> (1), `f^*ℒ` the inverse image `AlgebraicGeometry.Space.modulePullback`, `f^*s` the pullback of
> meromorphic sections (defined by
> `AlgebraicGeometry.Space.pullbacksMeromorphicSections_of_isDominant_of_isIntegralSpace` and
> nonzero by `AlgebraicGeometry.Space.pullbackMeromorphicSection_ne_zero_of_isDominant`), `f_*`
> proper pushforward of cycles (Stacks 0EP2) and `[R(X) : R(Y)]` the degree of the extension of
> function fields (Stacks 0ENY).
>
> In the second identity `c₁(f^*ℒ) ∩ [X]` is represented by the class of `div_{f^*ℒ}(f^*s)` in
> `CH_{n-1}(X)` (Stacks 0EQE, part (2)), and `c₁(ℒ) ∩ f_*[X]` is written as
> `[R(X) : R(Y)] (c₁(ℒ) ∩ [Y])`, since `f_*[X] = [R(X) : R(Y)] [Y]` (Stacks 0EP1), with
> `c₁(ℒ) ∩ [Y]` the class `AlgebraicGeometry.Space.weilDivisorOfInvertibleSheaf`.

```lean
theorem properCyclePushforward_sectionWeilDivisor_pullback (hL : IsInvertibleSheaf D sY hY L)
    {f : X ⟶ Y} (hfB : f ≫ sY = sX) (hf : IsProper D.site D.base D.base_mem f)
    (hdom : IsDominant D.site D.base D.base_mem f) {n : ℤ}
    (hnX : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hnY : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (n : EInt)) (hσ : σ ≠ 0) :
    properCyclePushforward D sX hX sY hY hfB hf.2.1.2 (n - 1)
        (sectionWeilDivisor D sX hX hintX
          ((modulePullback D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f)).obj L)
          (Stacks.SheafOfModules.IsInvertible.toAlgebraicGeometry _ _ _
            (modulePullbackInvertible (goodSpacesHom D sX hX sY hY f) L
              (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _ hL))) hnX
          (pullbackMeromorphicSection D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f) L
            (pullbacksMeromorphicSections_of_isDominant_of_isIntegralSpace D sX hX sY hY hintX
              hintY hdom) σ)
          (pullbackMeromorphicSection_ne_zero_of_isDominant D sX hX sY hY hintX hintY L
            (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _ hL) σ hdom hσ)) =
        (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
          sectionWeilDivisor D sY hY hintY L hL hnY σ hσ ∧
      chowClass.{v} D sY hY (n - 1) (properCyclePushforward D sX hX sY hY hfB hf.2.1.2 (n - 1)
        (sectionWeilDivisor D sX hX hintX
          ((modulePullback D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f)).obj L)
          (Stacks.SheafOfModules.IsInvertible.toAlgebraicGeometry _ _ _
            (modulePullbackInvertible (goodSpacesHom D sX hX sY hY f) L
              (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _ hL))) hnX
          (pullbackMeromorphicSection D.site D.base D.base_mem (goodSpacesHom D sX hX sY hY f) L
            (pullbacksMeromorphicSections_of_isDominant_of_isIntegralSpace D sX hX sY hY hintX
              hintY hdom) σ)
          (pullbackMeromorphicSection_ne_zero_of_isDominant D sX hX sY hY hintX hintY L
            (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _ hL) σ hdom hσ))) =
        (functionFieldDegreeAtGenericPoint D sX hX sY hY hintX f : ℤ) •
          weilDivisorOfInvertibleSheaf.{v} D sY hY hintY L hL hnY
```

## Tag 0EQT, a lemma

[Tag 0EQT](https://stacks.math.columbia.edu/tag/0EQT) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushforward_firstChernCapCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCap.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCap.lean#L636). The attribute's comment: “at the level of cycles: p_*(c_1(p^*L) ∩ α) = c_1(L) ∩ p_*α in Z_k(Y) for α in Z_{k+1}(X), with the cap product of Stacks 0EQJ and the pushforward of Stacks 0EP1; on the two carried inputs of ProperPushforwardChernComparison — Stacks 0EP2 for the closed-immersion square of the source's reduction, and Stacks 0EQS along the component morphism p|_W of Stacks 0EEG, which is proper because p is; the component rule of p^*L is the parameter chernX, the repository having no pullback of sheaves of modules; the reduction to a single subspace is PROVED”.

> **Stacks 0EQT, at the level of cycles.** In Situation 0EDT let `X/B` and `Y/B` be good, let
> `p : X ⟶ Y` be a proper morphism over `B`, let `ℒ` be an invertible `𝒪_Y`-module and let
> `α ∈ Z_{k+1}(X)`. Then
>
> `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α` in `Z_k(Y)`,
>
> an identity of `k`-cycles, hence also of classes in `CH_k(Y)`.
>
> The cap products are the cycle-level cap product of Stacks 0EQJ, with the component rule of
> `p^*ℒ` on `X` and of `ℒ` on `Y`, and the pushforwards are those of Stacks 0EP1, taken along the
> quasi-compactness that properness of `p` supplies. The two carried inputs are the fields of
> `AlgebraicGeometry.Space.ProperPushforwardChernComparison`, both of them statements about the
> pushforward along the component morphism `p|_W : W ⟶ W'` of Stacks 0EEG, which is proper
> because `p` is: Stacks 0EP2 for the square of the source's reduction, and Stacks 0EQS along
> `p|_W`, which is the source's final step. The passage from a single integral closed subspace to
> an arbitrary cycle is proved.

```lean
theorem properPushforward_firstChernCapCycleMap
    (cmp : ProperPushforwardChernComparison D hX hY hpB hp k chernX chernY)
    (α : CycleGroup D sX (k + 1)) :
    properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k
        (firstChernCapCycleMap D sX hX k chernX α) =
      firstChernCapCycleMap D sY hY k chernY
        (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 (k + 1) α)
```

**`AlgebraicGeometry.Space.properPushforward_firstChernClassCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCap.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCap.lean#L664). The attribute's comment: “p_*(c_1(p^*L) ∩ α) = c_1(L) ∩ p_*α in CH_k(Y) for α in Z_{k+1}(X), the right side being the cap product firstChernClassCap of Stacks 0EQJ at the invertible L, the left the class on Y of the pushforward CYCLE, proper pushforward of Chow classes being unavailable here; on the two carried inputs of ProperPushforwardChernComparison — Stacks 0EP2 for the closed-immersion square of the source's reduction and Stacks 0EQS along the component morphism of Stacks 0EEG, proper because p is; the component rule of p^*L is the parameter chernX”.

> **Stacks 0EQT.** In Situation 0EDT let `X/B` and `Y/B` be good, let `p : X ⟶ Y` be a proper
> morphism over `B`, let `α ∈ Z_{k+1}(X)` and let `ℒ` be an invertible sheaf on `Y`. Then
>
> `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α` in `CH_k(Y)`.
>
> The right side is the cap product of Stacks 0EQJ on `Y`,
> `AlgebraicGeometry.Space.firstChernClassCap` at `ℒ`, applied to the pushforward of cycles
> `p_*α`. Proper pushforward on Chow groups is not available in this repository, only on cycles,
> so the left side is the class on `Y` of the pushforward of the cycle representing
> `c₁(p^*ℒ) ∩ α`, which is the reading Stacks 0EQS and Stacks 0EQJ, case (1), already
> use. The identity holds already at the level of cycles, which is
> `AlgebraicGeometry.Space.properPushforward_firstChernCapCycleMap`.

```lean
theorem properPushforward_firstChernClassCap
    (L : Modules.{u, u} D.site D.base D.base_mem Y hY.1) (hL : IsInvertibleSheaf D sY hY L)
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sY hY k CH)
    (cmp : ProperPushforwardChernComparison D hX hY hpB hp k chernX chernY)
    (α : CycleGroup D sX (k + 1)) :
    chow.cls (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k
        (firstChernCapCycleMap D sX hX k chernX α)) =
      firstChernClassCap D sY hY L k hL chernY chow
        (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 (k + 1) α)
```

**`AlgebraicGeometry.Space.chowGroupCanonicalProperPushforward_canonicalFirstChernCapCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapChowGroup.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapChowGroup.lean#L100).

> **Stacks 0EQT.** In Situation 0EDT let `X/B` and `Y/B` be good, let `p : X ⟶ Y` be a proper
> morphism over `B`, let `α ∈ Z_{k+1}(X)` and let `ℒ` be an invertible `𝒪_Y`-module. Then
>
> `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α`   in `CH_k(Y)`.
>
> Every object is the constructed one, nothing is a parameter:
>
> * `p^*ℒ` is the inverse image `(modulePullback p).obj ℒ` of Stacks 03LU, invertible by Stacks
>   0B8P (`AlgebraicGeometry.Space.modulePullbackInvertible`);
> * `c₁(-) ∩ -` is the cap product of Stacks 0EQJ, `Z_{k+1} → CH_k`, at the canonical component
>   rule (`AlgebraicGeometry.Space.canonicalFirstChernCapCanonical`), on `X` for `p^*ℒ` and on `Y`
>   for `ℒ`;
> * on the left `p_*` is proper pushforward on Chow groups, `CH_k(X) → CH_k(Y)`, of Stacks 0EQC
>   (`AlgebraicGeometry.Space.chowGroupCanonicalProperPushforward`); on the right it is proper
>   pushforward of cycles `Z_{k+1}(X) → Z_{k+1}(Y)` of Stacks 0EP1;
> * `CH_k` is the Chow group of Stacks 0EQ6 (`AlgebraicGeometry.Space.chowGroupCanonical`).
>
> The proof is the source's: the formula is reduced to a single integral closed subspace `W` and
> its image `W'`, where it is Stacks 0EQS for `W ⟶ W'` when the δ-dimension is preserved; the case
> where it drops, which the source passes over, is
> `properCyclePushforward_canonicalDivisorCycleAt_pullback_eq_zero_of_deltaValue_drop`.

```lean
theorem chowGroupCanonicalProperPushforward_canonicalFirstChernCapCanonical
    (α : CycleGroup D sX (k + 1)) :
    chowGroupCanonicalProperPushforward.{u + 1} D sX hX sY hY hqB hq k
        (canonicalFirstChernCapCanonical.{u + 1} D sX hX
          ((modulePullback D.site D.base D.base_mem q).obj L) (modulePullbackInvertible q L hL) k
          α) =
      canonicalFirstChernCapCanonical.{u + 1} D sY hY L hL k
        (properCyclePushforward D sX hX sY hY hqB hq.2.1.2 (k + 1) α)
```

**`AlgebraicGeometry.Space.properPushforward_firstChernCapCycleMap_iff_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapReduction.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapReduction.lean#L309). The attribute's comment: “REDUCED, not proved: p_*(c_1(p^*L) ∩ α) = c_1(L) ∩ p_*α in Z_k(Y) for every α in Z_{k+1}(X) IF AND ONLY IF it holds on the fundamental cycle [W] of every integral closed subspace W of X. BOTH directions are proved and nothing is assumed, with the cap product of Stacks 0EQJ and the pushforward of Stacks 0EP1. The remaining clause, at a single W, is Stacks 0EQS along the component morphism p|_W of Stacks 0EEG, which rests on Stacks 0EQ4 and is open in this repository”.

> **Stacks 0EQT, reduced to the source's final step, in both directions.** In Situation 0EDT
> let `X/B` and `Y/B` be good, let `p : X ⟶ Y` be a proper morphism over `B`, let `ℒ` be an
> invertible `𝒪_Y`-module and let `α` range over `Z_{k+1}(X)`. Then the projection formula
>
> `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α` in `Z_k(Y)`
>
> holds for every `α` **exactly when** it holds on the fundamental cycle `[W]` of every integral
> closed subspace `W ⊆ X`, that is when
>
> `p_*(c₁(p^*ℒ) ∩ [W]) = deg(W/W') · (c₁(ℒ) ∩ [W'])`
>
> for `W'` the closure of the image of `|W|` and `deg(W/W')` the degree of Stacks 0EP1, part (1).
>
> Both directions are proved and nothing is assumed: the forward direction is
> `AlgebraicGeometry.Space.properPushforward_firstChernComponentCycle_of_firstChernCapCycleMap`,
> the reverse the source's steps (2)–(4),
> `AlgebraicGeometry.Space.properPushforward_firstChernCapCycleMap_of_component`.
>
> The cap products are the cycle-level cap product of Stacks 0EQJ and the pushforwards those of
> Stacks 0EP1, taken along the quasi-compactness that properness of `p` supplies. The component
> rules of `p^*ℒ` and of `ℒ` are the parameters `chernX` and `chernY`; the instance at the
> canonical rules, where `c₁(p^*ℒ)` is the first Chern class of the genuine inverse image `p^*ℒ`
> of Stacks 03LU, is
> `AlgebraicGeometry.Space.properPushforward_canonicalFirstChernCapCycleMap_iff_component`.
>
> The right-hand clause is Stacks 0EQS along the component morphism `p|_W : W ⟶ W'` of Stacks
> 0EEG, and it is open here; see the implementation notes.

```lean
theorem properPushforward_firstChernCapCycleMap_iff_component :
    (∀ α : CycleGroup D sX (k + 1),
        properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k
            (firstChernCapCycleMap D sX hX k chernX α) =
          firstChernCapCycleMap D sY hY k chernY
            (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 (k + 1) α)) ↔
      ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
        properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k
            (firstChernComponentCycle D sX hX k chernX W) =
          properCycleDegree D sX hX sY hY p W •
            firstChernComponentCycle D sY hY k chernY
              (IntegralClosedSubspace.closureImage D.site D.base D.base_mem hY.1
                (D.isDecentSpace_of_isGood sY hY) p W)
```

**`AlgebraicGeometry.Space.properPushforward_canonicalFirstChernCapCycleMap_iff_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapReduction.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardFirstChernCapReduction.lean#L376). The attribute's comment: “REDUCED, not proved, with BOTH component rules tied to L rather than parametric: p_*(c_1(p^*L) ∩ α) = c_1(L) ∩ p_*α in Z_k(Y) for every α in Z_{k+1}(X) IF AND ONLY IF it holds on the fundamental cycle [W] of every integral closed subspace W of X. BOTH directions are proved and nothing is assumed. c_1(p^*L) is the canonical rule of Stacks 0EQJ at the genuine inverse image p^*L of Stacks 03LU, invertible by Stacks 0B8P, and c_1(L) the canonical rule at L. The remaining clause, at a single W, is Stacks 0EQS along the component morphism p|_W of Stacks 0EEG, which rests on Stacks 0EQ4 and is open in this repository”.

> **Stacks 0EQT, reduced to the source's final step, with both component rules tied to `ℒ`.**
> In Situation 0EDT let `X/B` and `Y/B` be good, let `p : X ⟶ Y` be a proper morphism over `B`,
> let `ℒ` be an invertible `𝒪_Y`-module and let `α` range over `Z_{k+1}(X)`. Then
>
> `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α` in `Z_k(Y)`
>
> holds for every `α` **exactly when** it holds on the fundamental cycle `[W]` of every integral
> closed subspace `W ⊆ X`. Both directions are proved and nothing is assumed; this is
> `AlgebraicGeometry.Space.properPushforward_firstChernCapCycleMap_iff_component` at the canonical
> component rules of Stacks 0EQJ.
>
> Here `c₁(p^*ℒ)` is the first Chern class of the *genuine* inverse image `p^*ℒ` of Stacks 03LU,
> through `AlgebraicGeometry.Space.canonicalPullbackFirstChernRule`, and `c₁(ℒ)` that of `ℒ`,
> through `AlgebraicGeometry.Space.canonicalFirstChernRule`; neither is a parameter, and both are
> the rule `W ↦ div(t_W)` of Stacks 0EQJ at the canonical ratios of Stacks 0EPR.
>
> The remaining clause, at a single `W`, is Stacks 0EQS along the component morphism
> `p|_W : W ⟶ W'` of Stacks 0EEG, and is open here: Stacks 0EQS rests on the coefficient identity
> of Stacks 0EQ4, which this repository does not prove. See the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.ProperPushforwardOfDivisor`.

```lean
theorem properPushforward_canonicalFirstChernCapCycleMap_iff_component (hqB : q.hom ≫ sY = sX)
    (hq : IsProper D.site D.base D.base_mem q.hom) (k : ℤ) :
    (∀ α : CycleGroup D sX (k + 1),
        properCyclePushforward D sX hX sY hY hqB hq.2.1.2 k
            (firstChernCapCycleMap D sX hX k
              (canonicalPullbackFirstChernRule D hX hY q L hL k) α) =
          firstChernCapCycleMap D sY hY k (canonicalFirstChernRule D sY hY L hL k)
            (properCyclePushforward D sX hX sY hY hqB hq.2.1.2 (k + 1) α)) ↔
      ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
        properCyclePushforward D sX hX sY hY hqB hq.2.1.2 k
            (firstChernComponentCycle D sX hX k
              (canonicalPullbackFirstChernRule D hX hY q L hL k) W) =
          properCycleDegree D sX hX sY hY q.hom W •
            firstChernComponentCycle D sY hY k (canonicalFirstChernRule D sY hY L hL k)
              (IntegralClosedSubspace.closureImage D.site D.base D.base_mem hY.1
                (D.isDecentSpace_of_isGood sY hY) q.hom W)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.19, Tag 0EQP](https://stacks.math.columbia.edu/tag/0EQP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
