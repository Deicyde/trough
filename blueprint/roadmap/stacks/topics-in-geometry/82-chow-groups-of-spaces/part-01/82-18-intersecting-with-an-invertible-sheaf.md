---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.canonicalFirstChernCap, AlgebraicGeometry.Space.canonicalFirstChernCap_integralCycle, AlgebraicGeometry.Space.firstChernClassCap, AlgebraicGeometry.Space.firstChernClassCap_integralCycle, AlgebraicGeometry.Space.canonicalFirstChernCap_picardTensorModule, AlgebraicGeometry.Space.canonicalFirstChernCap_tensorUnit_eq_zero, AlgebraicGeometry.Space.firstChernClassCap_tensor, AlgebraicGeometry.Space.firstChernClassCap_structureSheaf_eq_zero
statement: formalized
proof: formalized
---

# 82.18 Intersecting with an invertible sheaf

Section 82.18 of the Stacks Project, [Tag 0EQI](https://stacks.math.columbia.edu/tag/0EQI). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQJ, a definition

[Tag 0EQJ](https://stacks.math.columbia.edu/tag/0EQJ) in the Stacks Project.

**`AlgebraicGeometry.Space.canonicalFirstChernCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCap.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCap.lean#L122). The attribute's comment: “the cap product c\_1(N) ∩ - : Z\_\{k+1}(X) → CH\_k(X) with the first Chern class of an invertible O\_X-module N on a good algebraic space X/B, cases (1) and (2): the component cycle c\_1(N|\_W) ∩ [W] is the Weil divisor div\_\{N|\_W}(t\_W) of Stacks 0EQE at the canonical ratios of Stacks 0EPR for a regular meromorphic section given by Stacks 0EPQ (canonicalFirstChernRule), the target is the Chow group of Stacks 0EQ6 part (4), and the pushforward i\_* and the fundamental cycle [W] are the genuine ones; nothing is a parameter. Case (1) is canonicalFirstChernCap\_integralCycle and case (2) is the coefficientwise additive extension firstChernCapCycleMap. The source pushes the class of div\_\{N|\_W}(t\_W) forward, this pushes the cycle forward and takes the class afterwards”.

> *Intersection with the first Chern class of an invertible sheaf*: the cap product
> `c₁(𝒩) ∩ - : Z_{k+1}(X) → CH_k(X)` attached to an invertible `𝒪_X`-module `𝒩` on a good
> algebraic space `X/B`. It sends `α = ∑ n_W [W]` to the class of `∑_W n_W i_*(c₁(𝒩|_W) ∩ [W])`,
> where `i : W → X` is the inclusion and the component cycle `c₁(𝒩|_W) ∩ [W]` is
> `AlgebraicGeometry.Space.canonicalFirstChernRule`, the Weil divisor `div_{𝒩|_W}(t_W)` of
> Stacks 0EQE, part (1), at the canonical ratios of Stacks 0EPR for the regular meromorphic section
> of `𝒩|_W` given by Stacks 0EPQ. The target is the Chow group `CH_k(X) = Z_k(X)/∼_rat` of
> Stacks 0EQ6, part (4); the pushforward `i_*` is applied to the cycle and the class is taken in
> `CH_k(X)` afterwards.

```lean
def canonicalFirstChernCap (k : ℤ) : CycleGroup D sX (k + 1) →+ chowGroup.{v} D sX hX k
```

**`AlgebraicGeometry.Space.canonicalFirstChernCap_integralCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCap.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCap.lean#L135). The attribute's comment: “case (1): the value of the cap product on the fundamental cycle [W] of an integral closed subspace W of δ-dimension k+1 is the class of i\_*(c\_1(N|\_W) ∩ [W]), with the component cycle c\_1(N|\_W) ∩ [W] the Weil divisor div\_\{N|\_W}(t\_W) of Stacks 0EQE at the canonical ratios and the class taken in the Chow group of Stacks 0EQ6; i\_* is applied to the cycle and the class taken afterwards, the source applying it to the class”.

> On the fundamental cycle `[W]` of an integral closed subspace `i : W → X` of δ-dimension
> `k + 1` the cap product `AlgebraicGeometry.Space.canonicalFirstChernCap` is the class of
> `i_*(c₁(𝒩|_W) ∩ [W])`, the inner cycle being the Weil divisor `div_{𝒩|_W}(t_W)` of Stacks 0EQE at
> the canonical choices.

```lean
theorem canonicalFirstChernCap_integralCycle (k : ℤ)
    {W : IntegralClosedSubspace D.site D.base D.base_mem X}
    (hW : deltaDimension D sX W = k + 1) :
    canonicalFirstChernCap.{u, v} D sX hX N hN k (integralCycle D sX (k + 1) W hW) =
      chowClass.{v} D sX hX k (integralClosedSubspacePushforward D sX hX W k
        (canonicalFirstChernRule D sX hX N hN k W hW))
```

**`AlgebraicGeometry.Space.firstChernClassCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean#L458). The attribute's comment: “the cap product c\_1(L) ∩ - : Z\_\{k+1}(X) → CH\_k(X) with the first Chern class of an invertible sheaf L on a good algebraic space X/B, cases (1) and (2); the component cycle c\_1(L|\_W) ∩ [W] on an integral closed subspace W of δ-dimension k+1 and the Chow group CH\_k(X) are explicit parameters, standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)-(4), neither of which exists for algebraic spaces here; the pushforward i\_* and the fundamental cycle [W] are not parameters”.

> **Stacks 0EQJ.** *Intersection with the first Chern class of an invertible sheaf*: the cap
> product `c₁(ℒ) ∩ - : Z_{k+1}(X) ⟶ CH_k(X)` attached to an invertible sheaf `ℒ` on a good
> algebraic space `X/B`.
>
> On the cycle `[W]` of an integral closed subspace `W ⊆ X` of δ-dimension `k + 1` it is the
> class of `i_*(c₁(ℒ|_W) ∩ [W])`, which is case (1) of the source; see
> `AlgebraicGeometry.Space.firstChernClassCap_integralCycle`.  Case (2), the extension of that
> rule by linearity over an arbitrary `(k+1)`-cycle, is
> `AlgebraicGeometry.Space.firstChernCapCycleMap`, which is proved to land in `Z_k(X)` and to be
> additive.
>
> The component cycle `c₁(ℒ|_W) ∩ [W]` on `W` and the Chow group `CH_k(X)` are explicit
> parameters, standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)–(4), neither of which is
> available for algebraic spaces in this repository; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.FirstChernClassCap`.  The pushforward `i_*` and the
> fundamental cycle `[W]` are not parameters.

```lean
def firstChernClassCap (_hL : IsInvertibleSheaf D sX hX L)
    (chern : FirstChernComponentCycleRule D sX k)
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sX hX k CH) :
    CycleGroup D sX (k + 1) →+ CH
```

**`AlgebraicGeometry.Space.firstChernClassCap_integralCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean#L477). The attribute's comment: “case (1): the value of the cap product on the fundamental cycle [W] of an integral closed subspace W of δ-dimension k+1 is the class of i\_*(c\_1(L|\_W) ∩ [W]), with the component cycle c\_1(L|\_W) ∩ [W] and the Chow group CH\_k(X) as explicit parameters standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)-(4); the pushforward i\_* is applied to the cycle and the class taken afterwards, the source applying it to the class”.

> **Stacks 0EQJ, case (1).** On the cycle `[W]` of an integral closed subspace `W ⊆ X` of
> δ-dimension `k + 1` the cap product is the class of `i_*(c₁(ℒ|_W) ∩ [W])`, for the closed
> immersion `i : W → X`.
>
> The source applies the proper pushforward `i_* : CH_k(W) ⟶ CH_k(X)` to the *class* of
> `c₁(ℒ|_W) ∩ [W]`; the form below applies the pushforward of cycles and takes the class
> afterwards, which is the same statement once proper pushforward is known to respect rational
> equivalence.

```lean
theorem firstChernClassCap_integralCycle (hL : IsInvertibleSheaf D sX hX L)
    (chern : FirstChernComponentCycleRule D sX k)
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sX hX k CH)
    {W : IntegralClosedSubspace D.site D.base D.base_mem X}
    (hW : deltaDimension D sX W = k + 1) :
    firstChernClassCap D sX hX L k hL chern chow (integralCycle D sX (k + 1) W hW) =
      chow.cls (integralClosedSubspacePushforward D sX hX W k (chern W hW))
```

## Tag 0EQK, a lemma

[Tag 0EQK](https://stacks.math.columbia.edu/tag/0EQK) in the Stacks Project.

**`AlgebraicGeometry.Space.canonicalFirstChernCap_picardTensorModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCapAdditive.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCapAdditive.lean#L418). The attribute's comment: “first assertion: c\_1(L) ∩ α + c\_1(N) ∩ α = c\_1(L ⊗ N) ∩ α in CH\_k(X), for the cap product of Stacks 0EQJ at the canonical choices (canonicalFirstChernCap), the tensor product picardTensorModule and the Chow group of Stacks 0EQ6. DISCHARGED: the component cycle c\_1(L|\_W) ∩ [W] is the constructed canonicalFirstChernRule, not a parameter, and the tensor product and the product of meromorphic sections are constructed too, so nothing is carried. Proved from Stacks 0EPV at the canonical choices, Stacks 03EL for the restriction of a tensor product to W, Stacks 0EPT, and Stacks 0EQ6 parts (1), (2) and (4). CORRECTED: the source writes α ∈ Z\_\{k-1}(X), which cannot give an identity in CH\_k(X) for the operation Z\_\{k+1}(X) → CH\_k(X) of Stacks 0EQJ; stated here for α ∈ Z\_\{k+1}(X), as the identical scheme-side lemma Stacks 02SP does”.

> *Additivity of the first Chern class cap product.* For
> invertible `𝒪_X`-modules `ℒ` and `𝒩` on a good algebraic space `X/B` and every `α ∈ Z_{k+1}(X)`,
>
>   `c₁(ℒ) ∩ α + c₁(𝒩) ∩ α = c₁(ℒ ⊗_{𝒪_X} 𝒩) ∩ α`   in   `CH_k(X)`.
>
> The cap product is the one of Stacks 0EQJ at the canonical choices,
> `AlgebraicGeometry.Space.canonicalFirstChernCap`, the tensor product is
> `AlgebraicGeometry.Space.picardTensorModule`, and `CH_k(X)` is the Chow group of Stacks 0EQ6.

```lean
theorem canonicalFirstChernCap_picardTensorModule
    (L N : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hL : IsInvertibleModule (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) L)
    (hN : IsInvertibleModule (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) N)
    (k : ℤ) (α : CycleGroup D sX (k + 1)) :
    canonicalFirstChernCap.{u, u + 1} D sX hX L hL k α +
        canonicalFirstChernCap.{u, u + 1} D sX hX N hN k α =
      canonicalFirstChernCap.{u, u + 1} D sX hX
        (picardTensorModule D.site D.base D.base_mem hX.1 L N)
        (isInvertibleModule_picardTensorModule D.site D.base D.base_mem hX.1 L N hL hN) k α
```

**`AlgebraicGeometry.Space.canonicalFirstChernCap_tensorUnit_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCapAdditive.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CanonicalFirstChernCapAdditive.lean#L486). The attribute's comment: “second assertion: c\_1(O\_X) ∩ α = 0 in CH\_k(X), for the cap product of Stacks 0EQJ at the canonical choices (canonicalFirstChernCap) and the Chow group of Stacks 0EQ6; O\_X is the tensor unit of the modules on the small étale site, which is the structure sheaf viewed as a module over itself on the nose (modulesTensorUnit\_eq). DISCHARGED: the component cycle is the constructed canonicalFirstChernRule, not a parameter, and no section of O\_X|\_W is chosen; proved from the first assertion at L = N = O\_X, the invertibility of the tensor unit, the right unitor O\_X ⊗ O\_X ≅ O\_X and the isomorphism invariance canonicalFirstChernCap\_congr\_iso. CORRECTED: stated for α ∈ Z\_\{k+1}(X), the source's Z\_\{k-1}(X) being a slip”.

> `c₁(𝒪_X) ∩ α = 0` in `CH_k(X)` for every `α ∈ Z_{k+1}(X)`, the structure sheaf being the
> tensor unit of `AlgebraicGeometry.Space.Modules`, which is `𝒪_X` as a module over itself.

```lean
theorem canonicalFirstChernCap_tensorUnit_eq_zero (k : ℤ) (α : CycleGroup D sX (k + 1)) :
    canonicalFirstChernCap.{u, u + 1} D sX hX
      (𝟙_ (Modules.{u, u} D.site D.base D.base_mem X hX.1))
      (isInvertibleModule_tensorUnit hX) k α = 0
```

**`AlgebraicGeometry.Space.firstChernClassCap_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapAdditive.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapAdditive.lean#L543). The attribute's comment: “first assertion: c\_1(L) ∩ α + c\_1(N) ∩ α = c\_1(L ⊗ N) ∩ α in CH\_k(X), for the cap product of Stacks 0EQJ as carried in this repository — so the component cycle c\_1(L|\_W) ∩ [W] and the Chow group CH\_k(X) remain explicit parameters, standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)-(4), neither of which exists for algebraic spaces here. QUALIFIED: carried as explicit named hypotheses are (i) that each of the three component rules is the Weil divisor div\_\{L|\_W}(s) of a meromorphic section, which is the definition of Stacks 0EQE, and (ii) that the ratio of the third section at the generic point of every prime divisor is the product of the ratios of the first two, which stands in for `M = L ⊗ N` and `st = s·t` because this repository has neither the tensor product of sheaves of modules on an algebraic space nor the product of meromorphic sections — this is the hypothesis shape of the carried Stacks 0EPV. Proved on top of those: the additivity of the component cycles, from Stacks 0EPV, and the additivity of the cap product, from it. Neither side of the equality, and no conjunct of it, is a hypothesis. CORRECTED: the source writes α ∈ Z\_\{k-1}(X), which cannot give an identity in CH\_k(X) for the operation Z\_\{k+1}(X) → CH\_k(X) of Stacks 0EQJ; stated here for α ∈ Z\_\{k+1}(X), as the identical scheme-side lemma Stacks 02SP does”.

> **Stacks 0EQK, first assertion.** *Additivity of the first Chern class cap product.* For
> invertible sheaves `ℒ` and `𝒩` on a good algebraic space `X/B` and every `α ∈ Z_{k+1}(X)`,
>
>   `c₁(ℒ) ∩ α + c₁(𝒩) ∩ α = c₁(ℒ ⊗_{O_X} 𝒩) ∩ α`   in   `CH_k(X)`.
>
> The cap product is the carried Stacks 0EQJ,
> `AlgebraicGeometry.Space.firstChernClassCap`, whose component cycle and Chow group are explicit
> parameters; the three component rules here are its parameters for the three sheaves, and the
> Chow group `CH` is shared.
>
> Nothing about the conclusion is assumed.  Each of the three component rules is assumed only to
> be presented by the Weil divisor of a meromorphic section of its own sheaf, which is the
> definition Stacks 0EQE would supply, and the hypothesis `hst` is the source's own step that
> `s_ξ ⊗ t_ξ` generates `(ℒ ⊗ 𝒩)_ξ`, so that `st/(s_ξ t_ξ) = (s/s_ξ)(t/t_ξ)`.  Additivity of the
> component cycles is then Stacks 0EPV, and additivity of the cap product follows from it by the
> extension of Stacks 0EQJ, case (2).

```lean
theorem firstChernClassCap_tensor
    {L N M : Modules.{u, u} D.site D.base D.base_mem X hX.1}
    (hL : IsInvertibleSheaf D sX hX L) (hN : IsInvertibleSheaf D sX hX N)
    (hM : IsInvertibleSheaf D sX hX M)
    {chernL chernN chernM : FirstChernComponentCycleRule D sX k}
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sX hX k CH)
    (dL : ComponentDivisorData sX k setup chernL)
    (dN : ComponentDivisorData sX k setup chernN)
    (dM : ComponentDivisorData sX k setup chernM)
    (hst : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem X)
      (P : PrimeDivisor D.site D.base D.base_mem W.subspace.toFunctor),
      (dM.ratio W P (dM.sect W) :
          P.genericTotalFractionRing D.site D.base D.base_mem (setup.isSpace W)
            (setup.isDecent W)) =
        (dL.ratio W P (dL.sect W) :
            P.genericTotalFractionRing D.site D.base D.base_mem (setup.isSpace W)
              (setup.isDecent W)) *
          (dN.ratio W P (dN.sect W) :
            P.genericTotalFractionRing D.site D.base D.base_mem (setup.isSpace W)
              (setup.isDecent W)))
    (α : CycleGroup D sX (k + 1)) :
    firstChernClassCap D sX hX L k hL chernL chow α +
        firstChernClassCap D sX hX N k hN chernN chow α =
      firstChernClassCap D sX hX M k hM chernM chow α
```

**`AlgebraicGeometry.Space.firstChernClassCap_structureSheaf_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapAdditive.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapAdditive.lean#L596). The attribute's comment: “second assertion: c\_1(O\_X) ∩ α = 0 in CH\_k(X), for the cap product of Stacks 0EQJ as carried in this repository — so the component cycle and the Chow group CH\_k(X) remain explicit parameters, standing in for Stacks 0EQE and Stacks 0EQ6 parts (2)-(4). QUALIFIED: carried as explicit named hypotheses are (i) that the component rule is the Weil divisor div\_\{O\_X|\_W}(s) of a meromorphic section, the definition of Stacks 0EQE, and (ii) that the ratio of that section against the chosen generator is a unit of the henselian local ring at the generic point of every prime divisor, which is the source's `1` restricting to an everywhere nonzero section of O\_X|\_W — the structure sheaf itself is not named because this repository has no tensor-unit sheaf of modules on an algebraic space. Proved on top of those: that every component cycle vanishes, from the order of vanishing of a unit being zero, and that the cap product vanishes, from that. The conclusion is not a hypothesis”.

> **Stacks 0EQK, second assertion.** `c₁(O_X) ∩ α = 0` for every `α ∈ Z_{k+1}(X)`.
>
> The source's proof: the global section `1` of `O_X` restricts, on an integral closed subspace
> `W ⊆ X`, to an everywhere nonzero section of `O_X|_W`, so `c₁(O_X|_W) ∩ [W] = 0`.  Here the
> hypothesis `hunit` is that everywhere nonzero section: a nowhere vanishing section generates, so
> its ratio against the chosen generator at the generic point of a prime divisor is a unit of the
> henselian local ring there, and the order of vanishing of a unit is zero.  That the component
> cycles all vanish is then proved, not assumed, and the vanishing of the cap product follows
> from it.

```lean
theorem firstChernClassCap_structureSheaf_eq_zero
    {L : Modules.{u, u} D.site D.base D.base_mem X hX.1} (hL : IsInvertibleSheaf D sX hX L)
    {chern : FirstChernComponentCycleRule D sX k}
    {CH : Type w} [AddCommGroup CH] (chow : ChowTarget.{u, w, v} D sX hX k CH)
    (d : ComponentDivisorData sX k setup chern)
    (hunit : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem X)
      (P : PrimeDivisor D.site D.base D.base_mem W.subspace.toFunctor),
      ∃ vP : ↥(P.genericHenselianLocalRing D.site D.base D.base_mem (setup.isSpace W)
        (setup.isDecent W)), IsUnit vP ∧
        (d.ratio W P (d.sect W) :
            P.genericTotalFractionRing D.site D.base D.base_mem (setup.isSpace W)
              (setup.isDecent W)) =
          algebraMap
            ↥(P.genericHenselianLocalRing D.site D.base D.base_mem (setup.isSpace W)
              (setup.isDecent W))
            (P.genericTotalFractionRing D.site D.base D.base_mem (setup.isSpace W)
              (setup.isDecent W)) vP)
    (α : CycleGroup D sX (k + 1)) :
    firstChernClassCap D sX hX L k hL chern chow α = 0
```

## Tag 0EQL, a lemma

[Tag 0EQL](https://stacks.math.columbia.edu/tag/0EQL) in the Stacks Project.

**`AlgebraicGeometry.Space.componentZeroCycleSumCoeff`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean#L682). The attribute's comment: “RIGHT-HAND SIDE ONLY — the equality of 0EQM is NOT formalized here, see cycleCoeffOfClosedSubspace\_vanishingLocus\_eq\_componentZeroCycleSumCoeff: the sum ∑ n\_i [Z(s\_i)]\_k as a coefficient family on the integral closed subspaces of X, over the irreducible components X\_i of X of δ-dimension k+1, of the pushforward along X\_i → X of the cycle [Z(s|\_\{X\_i})]\_k of Stacks 0EE9, weighted by the coefficient n\_i of X\_i in [X]\_\{k+1} = [O\_X]\_\{k+1}; the restriction s|\_\{X\_i} is the inverse image of Stacks 03LU and Z(s|\_\{X\_i}) its zero scheme of Stacks 0845, both on X\_i; the geometric representatives of the generic points are the arguments γ and γW, as throughout this library, Lemma 0EE1 being absent from it”.

> **Stacks 0EQL, the right-hand side.** The coefficient family of the `k`-cycle
> `∑ n_i [Z(s|_{X_i})]_k` on `X`: the sum, over the irreducible components `X_i ⊆ X` of
> δ-dimension `k + 1`, of the pushforward along `X_i → X` of the cycle of the zero scheme of
> `s|_{X_i}`, weighted by the multiplicity `n_i` of `X_i` in the fundamental cycle
> `[X]_{k+1}`.
>
> The sum is a finite sum at every integral closed subspace of `X`, by
> `AlgebraicGeometry.Space.hasFiniteSupport_componentZeroCycleSumCoeff`.

```lean
def componentZeroCycleSumCoeff
    (γ : Space.points D.site D.base D.base_mem X →
      GeometricPoint D.site D.base D.base_mem X)
    (γW : ComponentGeometricRepresentatives D sX hX L s k)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) : ℤ
```

**`AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_zeroScheme_eq_componentZeroCycleSumCoeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroSchemeChartGeneralChart.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroSchemeChartGeneralChart.lean#L290). The attribute's comment: “equation 82.18.3.1, which is Stacks 0EQM, is the conclusion: the coefficient family of [Z(s)]\_k of Stacks 0EE9 equals componentZeroCycleSumCoeff, the sum over the irreducible components X\_i of X of δ-dimension k+1 of the pushforward along X\_i → X of [Z(s|\_\{X\_i})]\_k weighted by the coefficient n\_i of X\_i in [X]\_\{k+1}. The geometric representatives of the generic points are the parameters γ, γW, γZ, as throughout this library, Lemma 0EE1 being absent from it; the equality holds for every choice of them. The definition of the right-hand side is componentZeroCycleSumCoeff (StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCap.lean)”.

> **Stacks 0EQL.**  In Situation 0EDT let `X/B` be good, let `ℒ` be an invertible `𝒪_X`-module,
> let `s ∈ Γ(X, ℒ)` be a **regular** section and assume `dim_δ(X) ≤ k + 1`.  Write
> `[X]_{k+1} = ∑ n_i [X_i]` with `X_i` the irreducible components of `X` of δ-dimension `k + 1`, and
> `s_i = s|_{X_i}`.  Then
>
> `[Z(s)]_k = ∑ n_i [Z(s_i)]_k`
>
> as `k`-cycles on `X`.  This is equation 82.18.3.1, Stacks 0EQM.
>
> The two sides are the coefficient families of
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace` at the zero scheme `Z(s)` of Stacks 0845 and
> of `AlgebraicGeometry.Space.componentZeroCycleSumCoeff`; the geometric representatives `γ`, `γW`,
> `γZ` of the generic points are parameters throughout this library, Lemma 0EE1 being absent from
> it, and the equality holds for every choice of them.

```lean
theorem cycleCoeffOfClosedSubspace_zeroScheme_eq_componentZeroCycleSumCoeff
    (k : ℤ) (hL : IsInvertibleSheaf D sX hX L)
    (hsreg : AlgebraicGeometry.IsRegularSection
      (structureCommRings D.site D.base D.base_mem ⟨X, hX.1⟩)
      (structureRingSheaf D.site D.base D.base_mem ⟨X, hX.1⟩).property s)
    (hdim : deltaDimensionClosed D sX hX Set.univ isClosed_univ ≤ ((k + 1 : ℤ) : EInt))
    (γ : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγ : ∀ x, (γ x).image = x)
    (γW : ComponentGeometricRepresentatives D sX hX L s k)
    (hγW : ∀ (W : ComponentsOfDeltaDimension D sX hX (k + 1)) y, (γW W y).image = y)
    (γZ : points D.site D.base D.base_mem (vanishingLocus D sX hX L s).1.toFunctor →
      GeometricPoint D.site D.base D.base_mem (vanishingLocus D sX hX L s).1.toFunctor)
    (hγZ : ∀ y, (γZ y).image = y) :
    cycleCoeffOfClosedSubspace D sX hX (vanishingLocus D sX hX L s).1
        (vanishingLocus D sX hX L s).2 k γZ =
      componentZeroCycleSumCoeff D sX hX L s k γ γW
```

## Tag 0EQN, a lemma

[Tag 0EQN](https://stacks.math.columbia.edu/tag/0EQN) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_firstChernCapCycleMap_closedSubspaceCycle_eq_vanishingLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RegularSectionFirstChernCap.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RegularSectionFirstChernCap.lean#L535). The attribute's comment: “c₁(ℒ) ∩ [Y]\_\{k+1} = [Z(s)]\_k in CH\_k(X), for X/B good, ℒ invertible, Y ⊆ X a closed subspace with dim\_δ(Y) ≤ k + 1 and s ∈ Γ(Y, ℒ|\_Y) a regular section; c₁(ℒ) ∩ - is Stacks 0EQJ at the canonical choices, [Y]\_\{k+1} and [Z(s)]\_k are Stacks 0EE9 (the latter on Y, read on X through Y → X), Z(s) is Stacks 0845 and CH\_k(X) is Stacks 0EQ6; nothing carried”.

> **Stacks 0EQN.** In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible
> `𝒪_X`-module. Let `Y ⊆ X` be a closed subspace with `dim_δ(Y) ≤ k + 1` and let
> `s ∈ Γ(Y, ℒ|_Y)` be a regular section. Then
>
> `c₁(ℒ) ∩ [Y]_{k+1} = [Z(s)]_k`  in `CH_k(X)`.
>
> Here `[Y]_{k+1}` is the cycle of Stacks 0EE9 of `Y` on `X`,
> `AlgebraicGeometry.Space.closedSubspaceCycle`; `c₁(ℒ) ∩ -` is the cap product of Stacks 0EQJ,
> the cycle-level operation `AlgebraicGeometry.Space.firstChernCapCycleMap` at the canonical
> component rule `AlgebraicGeometry.Space.canonicalFirstChernRule`, its class taken afterwards;
> `Z(s) ⊆ Y` is the zero scheme of Stacks 0845, whose `k`-cycle (defined because `dim_δ(Z(s)) ≤ k`,
> `AlgebraicGeometry.Space.deltaDimensionSubspace_vanishingLocus_closedSubspaceModuleRestrict_le`) is
> read on `X` through the inclusion `Y → X`; and `CH_k(X)` is the Chow group of Stacks 0EQ6,
> `AlgebraicGeometry.Space.chowGroupCanonical`, whose rational equivalences are sums of principal
> divisors at the canonical embeddings of Stacks 0ENK.
>
> The proof is the source's. Write `[Y]_{k+1} = ∑ n_i [Y_i]` over the irreducible components `Y_i`
> of `Y` of δ-dimension `k + 1`. The restriction `s_i = s|_{Y_i}` is nonzero
> (`AlgebraicGeometry.Space.closedSubspaceComponentImageSection_ne_zero`), so by Stacks 0EQF the
> cycle `[Z(s_i)]_k` is the Weil divisor of `s_i`
> (`AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_vanishingLocus_eq_canonicalDivisorCycleAt`),
> which differs from the component cycle `c₁(ℒ|_{Y_i}) ∩ [Y_i]` of the cap product by a principal
> divisor on `Y_i` at the canonical embeddings (Stacks 0EPT,
> `AlgebraicGeometry.Space.isPrincipalDivisorCycleOfGood_zsmul_canonicalDivisorCycleAt_sub`). So
> `c₁(ℒ) ∩ [Y]_{k+1} = ∑ n_i [Z(s_i)]_k` in `CH_k(X)`, and the right side is `[Z(s)]_k` by
> Stacks 0EQL on `Y`
> (`cycleCoeffOfClosedSubspace_vanishingLocus_eq_componentZeroCycleSumCoeff_of_isRegularSection`),
> the zero schemes `Z(s_i)` being inverse images of `Z(s)` (Stacks 0846).

```lean
theorem chowClassCanonical_firstChernCapCycleMap_closedSubspaceCycle_eq_vanishingLocus
    (s : (closedSubspaceModuleRestrict D sX hX L Y).sections)
    (hs : AlgebraicGeometry.IsRegularSection
      (structureCommRings D.site D.base D.base_mem ⟨Y.1.toFunctor, Y.2.1⟩)
      (structureRingSheaf D.site D.base D.base_mem ⟨Y.1.toFunctor, Y.2.1⟩).property s) {k : ℤ}
    (hdim : deltaDimensionSubspace D sX hX Y.1 Y.2 ≤ ((k + 1 : ℤ) : EInt)) :
    chowClassCanonical.{max (u + 1) v} D sX hX k
        (firstChernCapCycleMap D sX hX k (canonicalFirstChernRule D sX hX L hL k)
          (closedSubspaceCycle D sX hX Y.1 Y.2 (k + 1) hdim)) =
      chowClassCanonical.{max (u + 1) v} D sX hX k (closedSubspaceCyclePushforward D sX hX Y k
        (closedSubspaceCycle D (Y.1.ι ≫ sX) (isGood_closedSubspace D sX hX Y)
          (vanishingLocus D (Y.1.ι ≫ sX) (isGood_closedSubspace D sX hX Y)
            (closedSubspaceModuleRestrict D sX hX L Y) s).1
          (vanishingLocus D (Y.1.ι ≫ sX) (isGood_closedSubspace D sX hX Y)
            (closedSubspaceModuleRestrict D sX hX L Y) s).2 k
          (deltaDimensionSubspace_vanishingLocus_closedSubspaceModuleRestrict_le D sX hX L Y hL s
            hs hdim)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.18, Tag 0EQI](https://stacks.math.columbia.edu/tag/0EQI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
