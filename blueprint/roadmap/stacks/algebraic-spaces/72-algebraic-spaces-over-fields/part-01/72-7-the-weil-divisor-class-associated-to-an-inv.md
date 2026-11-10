---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PrimeDivisor.pullbacksMeromorphicSections_genericHenselianMorphism, AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio, AlgebraicGeometry.Space.PrimeDivisor.isUnit_canonicalGenericRatio, AlgebraicGeometry.Space.PrimeDivisor.canonicalLocalRatio, AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio_smul, AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio_smul_of_eval, AlgebraicGeometry.Space.canonicalLocalRatioFamily, AlgebraicGeometry.Space.PrimeDivisor.orderOfVanishingSection_canonicalLocalRatio_eq_length_sub_length
statement: formalized
proof: formalized
---

# 72.7 The Weil divisor class associated to an invertible module

Section 72.7 of the Stacks Project, [Tag 0ENV](https://stacks.math.columbia.edu/tag/0ENV). 7 tags here are carried by 43 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EPR, a definition

[Tag 0EPR](https://stacks.math.columbia.edu/tag/0EPR) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.pullbacksMeromorphicSections_genericHenselianMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianSpecMorphismFlat.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianSpecMorphismFlat.lean#L152). The attribute's comment: “the clause of the construction preceding the definition: c\_ξ is flat, so pullbacks of meromorphic functions and (regular) sections are defined for c\_ξ”.

> **Pullbacks of meromorphic functions and sections are defined for
> `c_ξ : Spec(𝒪^h_{X, ξ}) ⟶ X`.**
>
> This is the clause of the construction of Section 72.7 of the source preceding Definition
> 72.7.1: "Since `c_ξ` is flat, pullbacks of meromorphic functions and (regular) sections are
> defined for `c_ξ`".  It is what carries a regular meromorphic section `s` of `ℒ` to a
> meromorphic section of `ℒ_ξ = c_ξ^*ℒ` on `Spec(𝒪^h_{X, ξ})`, against which the ratio `s / s_ξ`
> is taken.

```lean
theorem PrimeDivisor.pullbacksMeromorphicSections_genericHenselianMorphism :
    PullbacksMeromorphicSections B S hS
      (Z.genericHenselianMorphism B S hS hX hdec R hR).hom
```

**`AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L84). The attribute's comment: “the ratio s/s\_ξ in Q(O^h\_\{X, ξ}) of a meromorphic section of an invertible module against the generator at the generic point of a prime divisor, read on the spectrum of the local ring of an affine elementary étale neighbourhood”.

> The ratio `s / s_ξ` of a meromorphic section of an invertible `𝒪_X`-module against the
> generator of `ℒ` at the generic point of a prime divisor, as an element of `Q(𝒪^h_{X, ξ})`: the
> coefficient of the section against the generator over `Spec(𝒪_{U, u})`, pushed along
> `Q(𝒪_{U, u}) → Q(𝒪^h_{X, ξ})`.

```lean
def PrimeDivisor.canonicalGenericRatio (t : MeromorphicSection.{u, u} B S hS X hX L) :
    Z.genericTotalFractionRing B S hS hX hdec
```

**`AlgebraicGeometry.Space.PrimeDivisor.isUnit_canonicalGenericRatio`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L91). The attribute's comment: “the ratio s/s\_ξ of a regular meromorphic section is a unit of Q(O^h\_\{X, ξ})”.

> The ratio `s / s_ξ` of a regular meromorphic section is a unit of `Q(𝒪^h_{X, ξ})`.

```lean
theorem PrimeDivisor.isUnit_canonicalGenericRatio
    (t : MeromorphicSection.{u, u} B S hS X hX L)
    (ht : IsRegularMeromorphicSection.{u, u} B S hS X hX L t) :
    IsUnit (Z.canonicalGenericRatio B S hS hX hdec L hL hInt hN t)
```

**`AlgebraicGeometry.Space.PrimeDivisor.canonicalLocalRatio`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L103). The attribute's comment: “the generator s\_ξ of an invertible module at the generic point of a prime divisor, read as the ratio family it assigns to meromorphic sections”.

> The choice of the generator `s_ξ`: the generator of `ℒ` at the generic
> point of a prime divisor, read as the ratio `t ↦ t / s_ξ` in the units of `Q(𝒪^h_{X, ξ})` that
> it assigns to a meromorphic section of `ℒ`. On a regular meromorphic section the value is the
> ratio `AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio`.

```lean
def PrimeDivisor.canonicalLocalRatio : LocalRatio.{u, u} B S hS hX hdec Z L
```

**`AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L152). The attribute's comment: “the ratio s/s\_ξ is multiplied by c when the section is, which is the step by which Stacks 0EPT and Stacks 0EPV compare two sections through one generator”.

> If the pullback of `t` to `Spec(𝒪_{U, u})` is `c` times the pullback of `t'` there, then the
> ratio of `t` is the image of `c` times the ratio of `t'`.

```lean
theorem PrimeDivisor.canonicalGenericRatio_smul
    (t t' : MeromorphicSection.{u, u} B S hS X hX L)
    (c : (meromorphicFunctionSheaf B S hS (Z.genericStalkSpace B S hS hX hdec).1
      (Z.genericStalkSpace B S hS hX hdec).2).obj.obj
        (op (Z.genericStalkChart B S hS hX hdec)))
    (hc : (pullbackMeromorphicSection B S hS (Z.genericStalkMorphism B S hS hX hdec) L
            (Z.pullbacksMeromorphicSections_genericStalkMorphism B S hS hX hdec) t).eval
          (op (Z.genericStalkChart B S hS hX hdec)) =
      (meromorphicChartRingEquiv B S hS (Z.genericStalkSpace B S hS hX hdec).1
          (Z.genericStalkSpace B S hS hX hdec).2
          (Z.genericStalkChart B S hS hX hdec)).symm c •
        (pullbackMeromorphicSection B S hS (Z.genericStalkMorphism B S hS hX hdec) L
              (Z.pullbacksMeromorphicSections_genericStalkMorphism B S hS hX hdec) t').eval
          (op (Z.genericStalkChart B S hS hX hdec))) :
    Z.canonicalGenericRatio B S hS hX hdec L hL hInt hN t =
      Z.genericStalkMeromorphicToGeneric B S hS hX hdec hInt hN c *
        Z.canonicalGenericRatio B S hS hX hdec L hL hInt hN t'
```

**`AlgebraicGeometry.Space.PrimeDivisor.canonicalGenericRatio_smul_of_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L217). The attribute's comment: “the ratio s/s\_ξ is multiplied by c when the section is, with the scaling read over the chart of X rather than over the spectrum of the local ring -- the step by which Stacks 0EPT and Stacks 0EPV compare two sections through one generator”.

> If `t` is `c` times `t'` over the chosen affine elementary étale neighbourhood `U` of the
> generic point, for `c` a meromorphic function on `U`, then the ratio of `t` is the image of the
> pullback of `c` to `Spec(𝒪_{U, u})` times the ratio of `t'`.

```lean
theorem PrimeDivisor.canonicalGenericRatio_smul_of_eval
    (t t' : MeromorphicSection.{u, u} B S hS X hX L)
    (c : (Stacks.SheafOfModules.Tensor.ringSheaf (meromorphicRingedSite B S hS X hX).O).obj.obj
      (op (Z.genericEtaleChart B S hS hX hdec)))
    (hc : t.eval (op (Z.genericEtaleChart B S hS hX hdec)) =
      c • t'.eval (op (Z.genericEtaleChart B S hS hX hdec))) :
    Z.canonicalGenericRatio B S hS hX hdec L hL hInt hN t =
      Z.genericStalkMeromorphicToGeneric B S hS hX hdec hInt hN
          (chartMeromorphicRingedSitePullbackHom B S hS (Z.genericStalkMorphism B S hS hX hdec)
            (Z.pullbacksMeromorphicSections_genericStalkMorphism B S hS hX hdec)
            (Z.genericStalkChartDiagram B S hS hX hdec) c) *
        Z.canonicalGenericRatio B S hS hX hdec L hL hInt hN t'
```

**`AlgebraicGeometry.Space.canonicalLocalRatioFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L242). The attribute's comment: “the generators s\_ξ at every prime divisor, read as the ratio family”.

> The family of canonical ratios over all prime divisors of `X`: the choice of a generator of
> `ℒ` at the generic point of every prime divisor.

```lean
def canonicalLocalRatioFamily : LocalRatioFamily.{u, u} B S hS hX hdec L
```

**`AlgebraicGeometry.Space.PrimeDivisor.orderOfVanishingSection_canonicalLocalRatio_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L251). The attribute's comment: “the length formula for ord\_\{Z,ℒ}(s) at the canonical ratio s/s\_ξ on a locally Noetherian integral algebraic space”.

> If the canonical ratio `s / s_ξ` of a meromorphic section is `a / b` with
> `a` and `b` nonzerodivisors of `𝒪^h_{X,ξ}`, then `ord_{Z,ℒ}(s)` is the difference of the lengths
> of the quotients of `𝒪^h_{X,ξ}` by `a` and by `b`.

```lean
theorem PrimeDivisor.orderOfVanishingSection_canonicalLocalRatio_eq_length_sub_length
    (t : MeromorphicSection.{u, u} B S hS X hX L)
    (a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hdec))
    (hab : (Z.canonicalLocalRatio B S hS hX hdec L hL hInt hN t :
        Z.genericTotalFractionRing B S hS hX hdec) =
      IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
        (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b) :
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hN
    orderOfVanishingSection.{u, u} B S hS hX hdec Z L t
        (Z.canonicalLocalRatio B S hS hX hdec L hL hInt hN) =
      ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ) -
        ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (b : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.PrimeDivisor.exists_orderOfVanishingSection_canonicalLocalRatio_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorCanonicalRatio.lean#L291). The attribute's comment: “existence of the presentation s/s\_ξ = a/b by nonzerodivisors at the canonical ratio, with the length formula, on a locally Noetherian integral algebraic space”.

> The canonical ratio `s / s_ξ` is a fraction `a / b` of nonzerodivisors of `𝒪^h_{X,ξ}`, and for
> one — hence for every — such presentation `ord_{Z,ℒ}(s)` is the difference of the lengths of the
> quotients.

```lean
theorem PrimeDivisor.exists_orderOfVanishingSection_canonicalLocalRatio_eq_length_sub_length
    (t : MeromorphicSection.{u, u} B S hS X hX L) :
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hN
    ∃ a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hdec),
      (Z.canonicalLocalRatio B S hS hX hdec L hL hInt hN t :
            Z.genericTotalFractionRing B S hS hX hdec) =
          IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
            (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b ∧
        orderOfVanishingSection.{u, u} B S hS hX hdec Z L t
            (Z.canonicalLocalRatio B S hS hX hdec L hL hInt hN) =
          ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
              (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ) -
            ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
              (b : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.orderOfVanishingSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 767](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L767). The attribute's comment: “ord\_\{Z,ℒ}(s), in the general form that takes the ratio s/s\_ξ as data, so that it is available for an arbitrary module over an arbitrary space. The tag's own definition is at the CONSTRUCTED ratio: PrimeDivisor.canonicalLocalRatio and canonicalLocalRatioFamily of StacksFrontier.AlgebraicGeometry.Spaces.Decent.PrimeDivisorCanonicalRatio build s/s\_ξ for an invertible module on a locally Noetherian integral algebraic space and carry no parameter”.

> **Stacks 0EPR.** The *order of vanishing of a meromorphic section `s` of `ℒ` along `Z`*:
> the order of vanishing of the ratio `s / s_ξ` in `Q(𝒪^h_{X,ξ})`, that is the difference
> `length (𝒪^h_{X,ξ} ⧸ a) - length (𝒪^h_{X,ξ} ⧸ b)` for `s / s_ξ = a / b` with `a` and `b`
> nonzerodivisors.

```lean
def orderOfVanishingSection (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatio.{u, z} B S hS hX hdec Z L) : ℤ
```

**`AlgebraicGeometry.Space.orderOfVanishingSection_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L794). The attribute's comment: “the length formula on any presentation, hence independence of the presentation”.

> **Stacks 0EPR.** If the ratio `s / s_ξ` is `a / b` with `a` and `b` nonzerodivisors of
> `𝒪^h_{X,ξ}`, then `ord_{Z,ℒ}(s)` is the difference of the lengths of the quotients of
> `𝒪^h_{X,ξ}` by `a` and by `b`. In particular it does not depend on the presentation.

```lean
theorem orderOfVanishingSection_eq_length_sub_length (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatio.{u, z} B S hS hX hdec Z L)
    (a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hdec))
    (hab : (ratio s : Z.genericTotalFractionRing B S hS hX hdec) =
      IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
        (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b) :
    orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratio =
      ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ) -
        ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (b : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.exists_orderOfVanishingSection_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 846](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L846). The attribute's comment: “existence of the presentation s/s\_ξ = a/b by nonzerodivisors, with the length formula; the ratio s/s\_ξ is the parameter `ratio`”.

> **Stacks 0EPR, well-definedness.** The ratio `s / s_ξ` *is* a fraction `a / b` of
> nonzerodivisors of `𝒪^h_{X,ξ}`, and for one — hence, by
> `AlgebraicGeometry.Space.orderOfVanishingSection_eq_length_sub_length`, for every — such
> presentation `ord_{Z,ℒ}(s)` is the difference
> `length (𝒪^h_{X,ξ} ⧸ a) - length (𝒪^h_{X,ξ} ⧸ b)`.
>
> This is the clause of the source's definition that fixes the integer: Definition 72.7.1 reads
> `ord_{Z,ℒ}(s)` off nonzerodivisors `a, b` of `𝒪^h_{X,ξ}` *such that* `s / s_ξ = a / b`, so the
> existence of such a pair is what makes the difference of lengths an admissible description of
> `ord_{Z,ℒ}(s)` at all. Regularity of the meromorphic section — carried, as throughout this
> module, by `ratio s` being a *unit* of `Q(𝒪^h_{X,ξ})` — is exactly what produces it: the
> numerator of an arbitrary presentation of a unit is again a nonzerodivisor.

```lean
theorem exists_orderOfVanishingSection_eq_length_sub_length
    (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatio.{u, z} B S hS hX hdec Z L) :
    ∃ a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hdec),
      (ratio s : Z.genericTotalFractionRing B S hS hX hdec) =
          IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
            (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b ∧
        orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratio =
          ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
              (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ) -
            ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
              (b : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.orderOfVanishingSection_unit_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 889](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L889). The attribute's comment: “independence of the choice of the generator s\_ξ”.

> **Stacks 0EPR, well-definedness.** Replacing the generator `s_ξ` of `ℒ` at the generic
> point of `Z` by `u · s_ξ` for a unit `u` of `𝒪^h_{X,ξ}` replaces the ratio `s / s_ξ` by
> `u · (s / s_ξ)` and does not change `ord_{Z,ℒ}(s)`.

```lean
theorem orderOfVanishingSection_unit_smul (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio ratio' : LocalRatio.{u, z} B S hS hX hdec Z L)
    {v : ↥(Z.genericHenselianLocalRing B S hS hX hdec)} (hv : IsUnit v)
    (hvr : (ratio' s : Z.genericTotalFractionRing B S hS hX hdec) =
      algebraMap ↥(Z.genericHenselianLocalRing B S hS hX hdec)
        (Z.genericTotalFractionRing B S hS hX hdec) v *
      (ratio s : Z.genericTotalFractionRing B S hS hX hdec)) :
    orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratio' =
      orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratio
```

## Tag 0EPS, a lemma

[Tag 0EPS](https://stacks.math.columbia.edu/tag/0EPS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_localRatioFamily_locallyFinite_divisorCoefficients_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericSectionRatioOrderZero.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericSectionRatioOrderZero.lean#L213). The attribute's comment: “the second set: the prime divisors with ord\_\{Z,ℒ}(s) ≠ 0 are locally finite, at the hypotheses of the source alone -- the proviso `hord` of locallyFinite\_divisorCoefficients\_ne\_zero\_of\_isIntegral is supplied here, by the canonical ratio of Stacks 0EPR, rather than assumed; the family of ratios is quantified existentially, over the choice of a free generator of ℒ\_ξ at each prime divisor and of the isomorphism across the universe gap that step (iii) of that construction is existential in, and its value at s is pinned to the ratio of s against that generator by the first clause of the conclusion”.

> **Stacks 0EPS, the second set, with `hord` supplied rather than assumed.**  Let `S` be a
> scheme, let `X` be a locally Noetherian integral algebraic space over `S`, let `ℒ` be an
> invertible `𝒪_X`-module and let `s` be a regular meromorphic section of `ℒ`.  Then there is a
> family of local ratios whose value at `s` is, at each prime divisor, the ratio of `s` against a
> free generator `t_ξ` of `ℒ_ξ` — the canonical ratio `s / s_ξ` of Stacks 0EPR, which is the first
> clause of the conclusion — for which `ord_{Z, ℒ}(s) = 0` at every prime divisor where `s`
> generates `ℒ_ξ`, and for which the prime divisors with `ord_{Z, ℒ}(s) ≠ 0` are locally finite
> in `|X|`.
>
> This carries no hypothesis beyond the source's.  It is
> `AlgebraicGeometry.Space.locallyFinite_divisorCoefficients_ne_zero_of_isIntegral`, whose single
> proviso `hord` is here a conclusion rather than an assumption, and it is existential over the
> choices the source also makes.  The first clause is load-bearing: without it `fun _ ↦ 1` would
> satisfy the other two vacuously.  See the implementation notes of this module for what the
> existential quantifier ranges over and why the family is canonical at `s` and not at every
> section.

```lean
theorem exists_localRatioFamily_locallyFinite_divisorCoefficients_ne_zero
    (L : Modules.{u, u} B S hS X hX)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible
      (structureCommRings B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS))
      (structureRingSheaf B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS)).property L)
    (s : MeromorphicSection.{u, u} B S hS X hX L)
    (hreg : IsRegularMeromorphicSection.{u, u} B S hS X hX L s) :
    ∃ ratio : LocalRatioFamily.{u, u} B S hS hX hdec L,
      (∀ Z : PrimeDivisor B S hS X,
          ∃ (t : Z.genericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L)
            (ψ : meromorphicChartRing B S hS
                (Z.genericHenselianSpace B S hS hX hdec (RR Z) (hRR Z)).obj
                (Z.genericHenselianSpace B S hS hX hdec (RR Z) (hRR Z)).property
                (Z.genericHenselianChart B S hS hX hdec (RR Z) (hRR Z)) ≃+*
              Z.genericTotalFractionRing B S hS hX hdec),
            (Function.Bijective fun r : RR Z ↦ r • t) ∧
              ψ.symm (ratio Z s : Z.genericTotalFractionRing B S hS hX hdec) •
                  toMeromorphicSectionValue B S hS
                    (Z.genericHenselianSpace B S hS hX hdec (RR Z) (hRR Z)).obj
                    (Z.genericHenselianSpace B S hS hX hdec (RR Z) (hRR Z)).property
                    (Z.genericHenselianPullback B S hS hX hdec (RR Z) (hRR Z) L)
                    (Z.genericHenselianChart B S hS hX hdec (RR Z) (hRR Z)) t =
                Z.genericMeromorphicGerm B S hS hX hdec (RR Z) (hRR Z) L s) ∧
        (∀ Z : PrimeDivisor B S hS X,
            Z.GeneratesGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s →
              divisorCoefficients.{u, u} B S hS hX hdec L s ratio Z = 0) ∧
          LocallyFinite fun Z : PrimeDivisor B S hS X ↦
            if divisorCoefficients.{u, u} B S hS hX hdec L s ratio Z = 0 then ∅
            else Z.support B S hS X
```

**`AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_memGenericModuleStalk_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteFirstSetOfRegularSection.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteFirstSetOfRegularSection.lean#L94). The attribute's comment: “the first set: the prime divisors whose generic point ξ has s ∉ ℒ\_ξ are locally finite -- unconditionally, at the hypotheses of the source, the nonempty open subspace of the source's first sentence being produced rather than assumed”.

> **Stacks 0EPS, the first set.**  Let `S` be a scheme, let `X` be a locally Noetherian
> integral algebraic space over `S`, let `ℒ` be an invertible `𝒪_X`-module and let `s` be a regular
> meromorphic section of `ℒ`.  Then the prime divisors `Z` of `X` whose generic point `ξ` satisfies
> `s ∉ ℒ_ξ` are locally finite in `|X|`.

```lean
theorem locallyFinite_primeDivisor_not_memGenericModuleStalk_of_isIntegral
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hint : IsIntegralSpace B S hS X) (L : Modules.{u, u} B S hS X hX)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible
      (structureCommRings B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS))
      (structureRingSheaf B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS)).property L)
    (s : MeromorphicSection.{u, u} B S hS X hX L)
    (hreg : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    [DecidablePred fun Z : PrimeDivisor B S hS X ↦
      ¬ Z.MemGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s] :
    LocallyFinite fun Z : PrimeDivisor B S hS X ↦
      if ¬ Z.MemGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s then
        Z.support B S hS X
      else ∅
```

**`AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_generatesGenericModuleStalk_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteSecondSetOfRegularSection.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteSecondSetOfRegularSection.lean#L102). The attribute's comment: “the generating set: the prime divisors whose generic point ξ has s not generating ℒ\_ξ are locally finite -- unconditionally, at the hypotheses of the source, the nonempty open subspace of the source's first sentence being produced rather than assumed; the second set of the source is contained in this one”.

> **Stacks 0EPS, the generating set.**  Let `S` be a scheme, let `X` be a locally Noetherian
> integral algebraic space over `S`, let `ℒ` be an invertible `𝒪_X`-module and let `s` be a regular
> meromorphic section of `ℒ`.  Then the prime divisors `Z` of `X` whose generic point `ξ` is such
> that `s` does **not** generate `ℒ_ξ` are locally finite in `|X|`.

```lean
theorem locallyFinite_primeDivisor_not_generatesGenericModuleStalk_of_isIntegral
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hint : IsIntegralSpace B S hS X) (L : Modules.{u, u} B S hS X hX)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible
      (structureCommRings B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS))
      (structureRingSheaf B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS)).property L)
    (s : MeromorphicSection.{u, u} B S hS X hX L)
    (hreg : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    [DecidablePred fun Z : PrimeDivisor B S hS X ↦
      ¬ Z.GeneratesGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s] :
    LocallyFinite fun Z : PrimeDivisor B S hS X ↦
      if ¬ Z.GeneratesGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s then
        Z.support B S hS X
      else ∅
```

**`AlgebraicGeometry.Space.locallyFinite_divisorCoefficients_ne_zero_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteSecondSetOfRegularSection.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallyFiniteSecondSetOfRegularSection.lean#L168). The attribute's comment: “the second set: the prime divisors with ord\_\{Z,ℒ}(s) ≠ 0 are locally finite, at the hypotheses of the source together with `hord`, the vanishing of ord\_\{Z,ℒ}(s) where s generates ℒ\_ξ -- which the ratio parameter of orderOfVanishingSection does not supply by itself”.

> **Stacks 0EPS, the second set.**  Let `S` be a scheme, let `X` be a locally Noetherian
> integral algebraic space over `S`, let `ℒ` be an invertible `𝒪_X`-module and let `s` be a regular
> meromorphic section of `ℒ`.  Then the prime divisors `Z` with `ord_{Z, ℒ}(s) ≠ 0` are locally
> finite in `|X|`, provided `ord_{Z, ℒ}(s) = 0` wherever `s` generates `ℒ_ξ`.
>
> That proviso, `hord`, is the only hypothesis beyond the source's.

```lean
theorem locallyFinite_divisorCoefficients_ne_zero_of_isIntegral
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hint : IsIntegralSpace B S hS X) (L : Modules.{u, u} B S hS X hX)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible
      (structureCommRings B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS))
      (structureRingSheaf B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS)).property L)
    (s : MeromorphicSection.{u, u} B S hS X hX L)
    (hreg : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    (ratio : LocalRatioFamily.{u, u} B S hS hX hdec L)
    (hord : ∀ Z : PrimeDivisor B S hS X,
      Z.GeneratesGenericModuleStalk B S hS hX hdec (RR Z) (hRR Z) L s →
        divisorCoefficients.{u, u} B S hS hX hdec L s ratio Z = 0) :
    LocallyFinite fun Z : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, u} B S hS hX hdec L s ratio Z = 0 then ∅
      else Z.support B S hS X
```

**`AlgebraicGeometry.Space.locallyFinite_primeDivisor_of_genericPoint_notMem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L683). The attribute's comment: “both sets: prime divisors whose generic points avoid a nonempty open”.

> **The Stacks 0EE5 step in the proof of Stacks 0EPS.** Any collection of prime divisors of a
> locally Noetherian integral algebraic space whose generic points all avoid one nonempty open
> subset of `|X|` is locally finite in `|X|`.
>
> Such a prime divisor is an irreducible component of `|X| ∖ U`, because a strictly larger
> irreducible closed subset of `|X| ∖ U` would make its codimension at least two, and the
> irreducible components of a closed subset are locally finite by Stacks 0EE5.
>
> This is the second and third sentences of the proof of Stacks 0EPS, in the generality that
> covers both of that lemma's sets at once, and it is the same step the proofs of Stacks 0ENN and
> Stacks 0EQU take. **It does not on its own prove Stacks 0EPS**: the nonempty open subset `U` is
> a hypothesis here, while Stacks 0EPS asserts local finiteness from regularity of the
> meromorphic section alone — its proof's first sentence, that `s` generates `ℒ` over some
> nonempty open subspace, is what produces `U`, and the attribute note below records that this
> statement carries it. Discharging `U` is the open part of Stacks 0EPS; the implementation notes
> of this module say exactly what is missing for each of the lemma's two sets.

```lean
theorem locallyFinite_primeDivisor_of_genericPoint_notMem
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X)) (P : PrimeDivisor B S hS X → Prop)
    [DecidablePred P]
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hP : ∀ Z : PrimeDivisor B S hS X, P Z → Z.genericPoint B S hS X ∈ Uᶜ) :
    LocallyFinite fun Z : PrimeDivisor B S hS X ↦ if P Z then Z.support B S hS X else ∅
```

**`AlgebraicGeometry.Space.locallyFinite_divisorCoefficients_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 1009](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L1009). The attribute's comment: “the second set: the prime divisors with ord\_\{Z,ℒ}(s) ≠ 0 are locally finite”.

> **The Stacks 0EE5 step in the proof of Stacks 0EPS, for its second set.** The prime divisors
> at which `ord_{Z,ℒ}(s)` is nonzero are locally finite in `|X|`, given a nonempty open subset of
> `|X|` containing the generic point of no such prime divisor — which in the source is the open
> subspace over which the regular meromorphic section `s` generates `ℒ`.
>
> This is `AlgebraicGeometry.Space.locallyFinite_primeDivisor_of_genericPoint_notMem` specialized
> to the predicate `ord_{Z,ℒ}(s) ≠ 0`. Like it, it **carries the hypothesis `hgen` that Stacks
> 0EPS proves rather than assumes**, which the attribute note records. For this set `hgen` cannot
> even be dropped: the order of vanishing is taken against the arbitrary parameter `ratio`, so
> the set of prime divisors with nonzero coefficient is not determined by `ℒ` and `s`, and
> without `hgen` the statement is false. See the implementation notes of this module.

```lean
theorem locallyFinite_divisorCoefficients_ne_zero
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X)) (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hgen : ∀ W : PrimeDivisor B S hS X,
      divisorCoefficients.{u, z} B S hS hX hdec L s ratio W ≠ 0 →
        W.genericPoint B S hS X ∈ Uᶜ) :
    LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s ratio W = 0 then ∅
      else W.support B S hS X
```

## Tag 0EPT, a lemma

[Tag 0EPT](https://stacks.math.columbia.edu/tag/0EPT) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_divisorCoefficients_canonicalLocalRatioFamily_sub_eq_ord_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionIso.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionIso.lean#L193). The attribute's comment: “the second conclusion for two ISOMORPHIC invertible modules: the Weil divisors of the chosen regular meromorphic sections of ℒ and of 𝒩 differ coefficientwise by div(f) for an invertible rational function f, at the canonical ratio s/s\_ξ of Stacks 0EPR and the embedding of Stacks 0ENK, with nothing assumed beyond X decent, locally Noetherian and integral”.

> **Stacks 0EPT in the form the construction of Stacks 0EPW uses, at the canonical choices.**
> On a decent, locally Noetherian, integral algebraic space the Weil divisors of the chosen
> regular meromorphic sections of two isomorphic invertible `𝒪_X`-modules differ coefficientwise
> by the divisor of an invertible rational function on `X`, the order of vanishing being read at
> the canonical ratio `s / s_ξ` of Stacks 0EPR and the embedding `R(X) → Q(𝒪^h_{X, ξ})` of
> Stacks 0ENK.
>
> The chosen section of `𝒩` is carried by the isomorphism `𝒦_X(𝒩) ≅ 𝒦_X(ℒ)` to a regular
> meromorphic section of `ℒ` with the same orders of vanishing
> (`AlgebraicGeometry.Space.PrimeDivisor.orderOfVanishingSection_canonicalLocalRatio_sectionsMap`),
> and two regular meromorphic sections of the one module `ℒ` differ by an invertible rational
> function, which is Stacks 0EPT in the form
> `AlgebraicGeometry.Space.exists_units_orderOfVanishingSection_canonicalLocalRatio_eq_add_ord`.

```lean
theorem exists_divisorCoefficients_canonicalLocalRatioFamily_sub_eq_ord_of_iso (e : L ≅ N) :
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    ∃ f : (rationalFunctions B S hS hX)ˣ, ∀ W : PrimeDivisor B S hS X,
      divisorCoefficients.{u, u} B S hS hX hdec L
            (regularMeromorphicSection B S hS hX hInt hNoeth L hL)
            (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hNoeth) W -
          divisorCoefficients.{u, u} B S hS hX hdec N
            (regularMeromorphicSection B S hS hX hInt hNoeth N hNinv)
            (canonicalLocalRatioFamily B S hS hX hdec N hNinv hInt hNoeth) W =
        (genericFractionEmbedding B S hS hX hdec hInt hNoeth).ord f W
```

**`AlgebraicGeometry.Space.exists_units_rationalFunctions_canonicalLocalRatio_eq_emb_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionRatio.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionRatio.lean#L63). The attribute's comment: “the first conclusion, that the ratio s/s' of two regular meromorphic sections of an invertible module is an element of R(X)^*, read on the canonical ratios s/s\_ξ of Stacks 0EPR through the embedding R(X) → Q(O^h\_\{X, ξ}) of Stacks 0ENK”.

> **The ratio of two regular meromorphic sections is an invertible rational function.** On a
> decent, locally Noetherian, integral algebraic space the ratio of two regular meromorphic sections
> `s`, `s'` of an invertible `𝒪_X`-module is an invertible rational function `f`: at the generic
> point of every prime divisor the canonical ratio `s / s_ξ` of Stacks 0EPR is the image of `f` under
> the embedding `R(X) → Q(𝒪^h_{X, ξ})` of Stacks 0ENK times the canonical ratio `s' / s_ξ`.

```lean
theorem exists_units_rationalFunctions_canonicalLocalRatio_eq_emb_mul
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s s' : MeromorphicSection.{u, u} B S hS X hX L)
    (hs : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    (hs' : IsRegularMeromorphicSection.{u, u} B S hS X hX L s') :
    ∃ f : (rationalFunctions B S hS hX)ˣ, ∀ W : PrimeDivisor B S hS X,
      (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hN W s :
          W.genericTotalFractionRing B S hS hX hdec) =
        (genericFractionEmbedding B S hS hX hdec hInt hN).emb W
            (f : rationalFunctions B S hS hX) *
          (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hN W s' :
            W.genericTotalFractionRing B S hS hX hdec)
```

**`AlgebraicGeometry.Space.exists_units_orderOfVanishingSection_canonicalLocalRatio_eq_add_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionRatio.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorMeromorphicSectionRatio.lean#L95). The attribute's comment: “the second conclusion, div\_ℒ(s) = div\_ℒ(s') + div(f) coefficientwise, at the canonical ratio s/s\_ξ of Stacks 0EPR and the embedding of Stacks 0ENK, with f = s/s' PRODUCED rather than assumed”.

> **The orders of vanishing of two regular meromorphic sections differ by `ord_Z` of their
> ratio.** On a decent, locally Noetherian, integral algebraic space the orders of vanishing of two
> regular meromorphic sections `s`, `s'` of an invertible `𝒪_X`-module along a prime divisor differ
> by `ord_Z(f)` for one invertible rational function `f`, namely their ratio. Summed over the prime
> divisors this is the identity `div_ℒ(s) = div_ℒ(s') + div(f)` of Weil divisors.

```lean
theorem exists_units_orderOfVanishingSection_canonicalLocalRatio_eq_add_ord
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s s' : MeromorphicSection.{u, u} B S hS X hX L)
    (hs : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    (hs' : IsRegularMeromorphicSection.{u, u} B S hS X hX L s') :
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hN
    ∃ f : (rationalFunctions B S hS hX)ˣ, ∀ W : PrimeDivisor B S hS X,
      orderOfVanishingSection.{u, u} B S hS hX hdec W L s
          (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hN W) =
        orderOfVanishingSection.{u, u} B S hS hX hdec W L s'
            (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hN W) +
          (genericFractionEmbedding B S hS hX hdec hInt hN).ord f W
```

**`AlgebraicGeometry.Space.orderOfVanishingSection_eq_add_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 919](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L919). The attribute's comment: “div\_ℒ(s) = div\_ℒ(s') + div(f) coefficientwise; f = s/s' is the argument `hs`, discharged at the canonical ratio of Stacks 0EPR by exists\_units\_orderOfVanishingSection\_canonicalLocalRatio\_eq\_add\_ord, which produces f”.

> **Stacks 0EPT, coefficientwise.** If `s` and `s'` are meromorphic sections of `ℒ` whose
> ratios at the generic point of `Z` differ by the image of a rational function `f`, then
> `ord_{Z,ℒ}(s) = ord_{Z,ℒ}(s') + ord_Z(f)`. Summing over all prime divisors this is the
> identity `div_ℒ(s) = div_ℒ(s') + div(f)` of Weil divisors.
>
> That such an `f` exists — the first assertion of Stacks 0EPT — is the argument `hs` here, and is
> proved at the canonical ratio of Stacks 0EPR by
> `AlgebraicGeometry.Space.exists_units_orderOfVanishingSection_canonicalLocalRatio_eq_add_ord`,
> which produces `f` rather than taking it.

```lean
theorem orderOfVanishingSection_eq_add_ord (L : Modules.{u, max u z} B S hS X hX)
    (s s' : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatio.{u, z} B S hS hX hdec Z L)
    (emb : rationalFunctions B S hS hX →+* Z.genericTotalFractionRing B S hS hX hdec)
    (f : rationalFunctions B S hS hX) (hf : IsUnit (emb f))
    (hs : (ratio s : Z.genericTotalFractionRing B S hS hX hdec) =
      emb f * (ratio s' : Z.genericTotalFractionRing B S hS hX hdec)) :
    orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratio =
      orderOfVanishingSection.{u, z} B S hS hX hdec Z L s' ratio +
        Z.ord B S hS hX hdec (emb f) hf
```

**`AlgebraicGeometry.Space.divisorOfSection_eq_add_principalDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSectionRatio.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSectionRatio.lean#L152). The attribute's comment: “the identity in Div(X); the coefficientwise form is orderOfVanishingSection\_eq\_add\_ord”.

> **Stacks 0EPT.** If `s` and `s'` are nonzero meromorphic sections of `ℒ` whose ratios at
> the generic point of every prime divisor differ by the invertible rational function
> `f = s/s' ∈ R(X)^*`, then their Weil divisors of Stacks 0EPU differ by the principal Weil
> divisor of `f`:
>
> `∑ ord_{Z,ℒ}(s) [Z] = ∑ ord_{Z,ℒ}(s') [Z] + div(f)`
>
> as an identity in the group `Div(X)` of Weil divisors on `X`. Coefficientwise at a single prime
> divisor this is
> `AlgebraicGeometry.Space.orderOfVanishingSection_eq_add_ord`, of which this statement is the
> sum over all prime divisors; that `div(f)` is itself a Weil divisor is what Stacks 0EPS gives
> in the source, and is here the hypothesis `hlf`, which
> `AlgebraicGeometry.Space.ord_mem_weilDivisor_of_ratio_eq` discharges from the local finiteness
> of the two divisors.

```lean
theorem divisorOfSection_eq_add_principalDivisor
    (hlf : ∀ g : (rationalFunctions B S hS hX)ˣ, E.ord g ∈ WeilDivisor B S hS X)
    (L : Modules.{u, max u z} B S hS X hX)
    (s s' : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (f : (rationalFunctions B S hS hX)ˣ)
    (hfin : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s ratio W = 0 then ∅
      else W.support B S hS X)
    (hfin' : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s' ratio W = 0 then ∅
      else W.support B S hS X)
    (hs : ∀ W : PrimeDivisor B S hS X,
      (ratio W s : W.genericTotalFractionRing B S hS hX hdec) =
        E.emb W (f : rationalFunctions B S hS hX) *
          (ratio W s' : W.genericTotalFractionRing B S hS hX hdec)) :
    divisorOfSection.{u, z} B S hS hX hdec L s ratio hfin =
      divisorOfSection.{u, z} B S hS hX hdec L s' ratio hfin' + E.principalDivisor hlf f
```

**`AlgebraicGeometry.Space.existsUnique_ratio_weilDivisorOfSection_eq_add_divRationalFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean#L208). The attribute's comment: “both conclusions at the source's hypotheses: for nonzero meromorphic sections s, s' of an invertible module on a locally Noetherian integral X, f = s/s' is THE element of R(X)^* with s = f s' (f read in Γ(X, 𝒦\_X) through the canonical comparison of Stacks 0ENA, for every presentation), and div\_ℒ(s) = div\_ℒ(s') + div(f) in Div(X), the sums being Weil divisors by Stacks 0EPS (proved) and div(f) the principal divisor of Stacks 0ENQ”.

> **Stacks 0EPT.** Let `X` be a locally Noetherian integral algebraic space over `S`, let `ℒ`
> be an invertible `𝒪_X`-module and let `s`, `s'` be nonzero meromorphic sections of `ℒ`. Then
> `f = s / s'` is an element of `R(X)^*` and
>
> `∑ ord_{Z,ℒ}(s) [Z] = ∑ ord_{Z,ℒ}(s') [Z] + div(f)`
>
> as Weil divisors.
>
> The ratio is stated as the source means it: `f` is **the** unit of `R(X)` with `s = f · s'`,
> `f` being read in `Γ(X, 𝒦_X)` through the canonical comparison `R(X) → Γ(X, 𝒦_X)` of Stacks
> 0ENA (`AlgebraicGeometry.Space.rationalToMeromorphic`), for every presentation the comparison
> is built from — it does not depend on it,
> `AlgebraicGeometry.Space.rationalToMeromorphic_eq_of_presentation` — and `f` is unique with this
> property. The two sums are `AlgebraicGeometry.Space.weilDivisorOfSection` (Stacks 0EPU, part (1)),
> which are Weil divisors by Stacks 0EPS, proved there; `div(f)` is the principal Weil divisor
> `AlgebraicGeometry.Space.divRationalFunction` of Stacks 0ENQ, a Weil divisor by Stacks 0ENN.
> Nothing is assumed beyond the hypotheses of the source.
>
> The ratio in `Γ(X, 𝒦_X)^*` is
> `AlgebraicGeometry.Space.existsUnique_units_smul_eq_of_isRegularMeromorphicSection` (nonzero
> sections being regular, `AlgebraicGeometry.Space.isRegularMeromorphicSection_of_ne_zero`); it
> comes from a unit of `R(X)` because the comparison is bijective; and at the generic point of every
> prime divisor the canonical ratio `s / s_ξ` of Stacks 0EPR is the image of `f` times `s' / s_ξ`,
> so that the orders of vanishing add up
> (`AlgebraicGeometry.Space.orderOfVanishingSection_eq_add_ord_of_ratio_eq`).

```lean
theorem existsUnique_ratio_weilDivisorOfSection_eq_add_divRationalFunction
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s s' : MeromorphicSection.{u, u} B S hS X hX L) (hs : s ≠ 0) (hs' : s' ≠ 0) :
    ∃! f : (rationalFunctions B S hS hX)ˣ,
      (∀ P : CodimensionZeroPresentation B S hS X,
        s = (id (rationalToMeromorphic (X := (⟨X, hX⟩ : AlgebraicSpaces B S hS)) P
              (fun _ hz => (weaklyAssociatedPointsOfSpace_eq_setOf_localRingDimension_eq_zero
                B S hS ⟨X, hX⟩ hInt.hasEtaleLocalProperty_isReduced).subset hz)
              (hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian B S hS X hX hN)
              (f : rationalFunctions B S hS hX)) :
            ↥(RingCat.sectionsSubring ((Stacks.SheafOfModules.Tensor.ringSheaf
              (meromorphicRingedSite B S hS X hX).O).obj))) • s') ∧
      weilDivisorOfSection B S hS hX hInt hN L hL s hs =
        weilDivisorOfSection B S hS hX hInt hN L hL s' hs' +
          divRationalFunction B S hS hX hInt hN f
```

**`AlgebraicGeometry.Space.existsUnique_units_smul_eq_of_isRegularMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionRatio.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionRatio.lean#L146). The attribute's comment: “the first conclusion, that the ratio s/s' of two regular meromorphic sections of an invertible module is invertible, read in Γ(X, 𝒦\_X) -- which is R(X) by the third conclusion of Stacks 0ENA; the ratio is also unique”.

> **Stacks 0EPT, the first conclusion; the algebraic-space analogue of Stacks 02SH.** On a
> locally Noetherian integral algebraic space over a scheme `S`, two regular meromorphic sections
> `s`, `s'` of an invertible `𝒪_X`-module differ by a unique **invertible** global meromorphic
> function: `s = g · s'` with `g ∈ Γ(X, 𝒦_X)^*`. Since `R(X) = Γ(X, 𝒦_X)` by the third conclusion
> of Stacks 0ENA, this says that the ratio `s / s'` lies in `R(X)^*`.
>
> The trivialisation `𝒦_X ≅ 𝒦_X(ℒ)` of Stacks 0EPQ writes both sections as multiples of one
> section `t`, the coefficients being global meromorphic functions; they are nonzero by
> regularity, hence invertible because `Γ(X, 𝒦_X)` is the function field; and uniqueness is
> injectivity of multiplication by the regular section `s'`.

```lean
theorem existsUnique_units_smul_eq_of_isRegularMeromorphicSection
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s s' : MeromorphicSection.{u, u} B S hS X hX L)
    (hs : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    (hs' : IsRegularMeromorphicSection.{u, u} B S hS X hX L s') :
    ∃! g : (↥(RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (meromorphicRingedSite B S hS X hX).O).obj)))ˣ,
      s = (g : ↥(RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (meromorphicRingedSite B S hS X hX).O).obj))) •
        s'
```

## Tag 0EPU, a definition

[Tag 0EPU](https://stacks.math.columbia.edu/tag/0EPU) in the Stacks Project.

**`AlgebraicGeometry.Space.divisorCoefficients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 966](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L966). The attribute's comment: “part (1): the coefficients ord\_\{Z,ℒ}(s) of div\_ℒ(s)”.

> **Stacks 0EPU, part (1).** The coefficients of the *Weil divisor associated to a
> meromorphic section `s` of `ℒ`*: the coefficient at a prime divisor `Z` is `ord_{Z,ℒ}(s)`.

```lean
def divisorCoefficients (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L) : PrimeDivisor B S hS X → ℤ
```

**`AlgebraicGeometry.Space.divisorOfSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 975](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L975). The attribute's comment: “part (1): div\_ℒ(s) = ∑ ord\_\{Z,ℒ}(s) [Z] as an element of Div(X)”.

> **Stacks 0EPU, part (1).** The *Weil divisor associated to a meromorphic section `s` of
> `ℒ`*, that is `div_ℒ(s) = ∑ ord_{Z,ℒ}(s) [Z]` in `Div(X)`. The prime divisors with nonzero
> coefficient are locally finite by Stacks 0EPS, which is the hypothesis `hfin`.

```lean
def divisorOfSection (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s ratio W = 0 then ∅
      else W.support B S hS X) :
    WeilDivisor B S hS X
```

**`AlgebraicGeometry.Space.divisorOfSectionOfGenerating`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 1038](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L1038). The attribute's comment: “part (1): div\_ℒ(s) in Div(X); the local finiteness that Stacks 0EPS supplies in the source comes from the hypothesis quadruple (U, hUopen, hUne, hgen), the open subspace over which s generates ℒ not being produced in this library”.

> **Stacks 0EPU, part (1).** The Weil divisor `div_ℒ(s) = ∑ ord_{Z,ℒ}(s) [Z]` of a
> meromorphic section `s` of `ℒ`, with the local finiteness of its support supplied by
> `AlgebraicGeometry.Space.locallyFinite_divisorCoefficients_ne_zero` from a nonempty open subset
> of `|X|` whose complement carries the generic point of every prime divisor with nonzero
> coefficient — in the source, the open subspace over which `s` generates `ℒ`. That open subset
> is a hypothesis: the first sentence of the proof of Stacks 0EPS, which produces it there, is
> not established in this library, for the reasons given in the implementation notes of this
> module.

```lean
def divisorOfSectionOfGenerating
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X)) (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hgen : ∀ W : PrimeDivisor B S hS X,
      divisorCoefficients.{u, z} B S hS hX hdec L s ratio W ≠ 0 →
        W.genericPoint B S hS X ∈ Uᶜ) :
    WeilDivisor B S hS X
```

**`AlgebraicGeometry.Space.weilDivisorOfSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisor.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisor.lean#L245). The attribute's comment: “part (1): div\_ℒ(s) = ∑ ord\_\{Z,ℒ}(s)[Z] ∈ Div(X) for a nonzero meromorphic section s of an invertible module, at the canonical ratio s/s\_ξ of Stacks 0EPR, with the local finiteness of Stacks 0EPS proved”.

> **Stacks 0EPU, part (1).** The *Weil divisor associated to a nonzero meromorphic section*
> `s` of an invertible `𝒪_X`-module `ℒ` on a locally Noetherian integral algebraic space:
>
> `div_ℒ(s) = ∑_Z ord_{Z,ℒ}(s) [Z] ∈ Div(X)`,
>
> the sum over the prime divisors of `X`. The coefficient `ord_{Z,ℒ}(s)` is the order of vanishing
> of Stacks 0EPR at the canonical ratio `s / s_ξ`
> (`AlgebraicGeometry.Space.canonicalLocalRatioFamily`), and the sum is a Weil divisor by Stacks
> 0EPS, which is `AlgebraicGeometry.Space.locallyFinite_ord_ne_zero_of_ne_zero`. Nothing beyond
> `X`, `ℒ` and `s` enters.

```lean
def weilDivisorOfSection
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s : MeromorphicSection.{u, u} B S hS X hX L) (hs : s ≠ 0) : ↥(WeilDivisor B S hS X)
```

**`AlgebraicGeometry.Space.weilDivisorClassOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean#L129). The attribute's comment: “part (2): the Weil divisor class of ℒ, the image of div\_ℒ(s) in the canonical Cl(X) of Stacks 0ENR for a nonzero meromorphic section s, which exists; independence of s is weilDivisorClassOfInvertible\_eq”.

> **Stacks 0EPU, part (2).** The *Weil divisor class associated to an invertible
> `𝒪_X`-module* `ℒ` on a locally Noetherian integral algebraic space: the image of `div_ℒ(s)` in
> the Weil divisor class group `Cl(X)` of Stacks 0ENR, for `s` a nonzero meromorphic section of
> `ℒ`.
>
> It is evaluated at the nonzero meromorphic section of
> `AlgebraicGeometry.Space.exists_meromorphicSection_ne_zero`, and it is the image of `div_ℒ(s)`
> for every nonzero `s` by `AlgebraicGeometry.Space.weilDivisorClassOfInvertible_eq`.

```lean
def weilDivisorClassOfInvertible
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L) :
    weilDivisorClassGroup B S hS hX hInt hN
```

**`AlgebraicGeometry.Space.weilDivisorClassOfInvertible_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean#L141). The attribute's comment: “part (2): well-definedness, the class of div\_ℒ(s) in Cl(X) is the same for every nonzero meromorphic section s, by Stacks 0EPT”.

> **Stacks 0EPU, part (2), well-definedness.** The Weil divisor class of `ℒ` is the image of
> `div_ℒ(s)` in `Cl(X)` for every nonzero meromorphic section `s` of `ℒ`: two nonzero meromorphic
> sections have Weil divisors differing by the principal divisor `div(s / s')`, by Stacks 0EPT.

```lean
theorem weilDivisorClassOfInvertible_eq
    (L : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (s : MeromorphicSection.{u, u} B S hS X hX L) (hs : s ≠ 0) :
    weilDivisorClassOfInvertible B S hS hX hInt hN L hL =
      (QuotientAddGroup.mk (weilDivisorOfSection B S hS hX hInt hN L hL s hs) :
        weilDivisorClassGroup B S hS hX hInt hN)
```

**`AlgebraicGeometry.Space.divisorClassOfSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean#L120). The attribute's comment: “part (2): the Weil divisor class of ℒ, the image of div\_ℒ(s) in Cl(X); the class group is Stacks 0ENR, relative to the embedding R(X) → Q(𝒪^h\_\{X,ξ}) of Stacks 0ENK, which is the parameter `E` inhabited by genericFractionEmbedding, and the ratio s/s\_ξ is the parameter `ratio` as in Stacks 0EPR and in part (1)”.

> **Stacks 0EPU, part (2).** The *Weil divisor class associated to `ℒ`*: the image in `Cl(X)`
> of the Weil divisor `div_ℒ(s) = ∑_Z ord_{Z,ℒ}(s) [Z]` of a nonzero meromorphic section `s` of
> `ℒ`.
>
> It depends only on `ℒ` and not on `s`, which is
> `AlgebraicGeometry.Space.divisorClassOfSection_eq` and is the use the source makes of Stacks
> 0EPT.

```lean
def divisorClassOfSection (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s ratio W = 0 then ∅
      else W.support B S hS X) :
    E.weilDivisorClassGroup
```

**`AlgebraicGeometry.Space.divisorClassOfSection_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean#L138). The attribute's comment: “part (2): well-definedness, the class of div\_ℒ(s) in Cl(X) is independent of the nonzero meromorphic section s; this is the appeal to Stacks 0EPT that the source makes, whose conclusion div\_ℒ(s) = div\_ℒ(s') + div(f) is read through the coefficientwise membership condition of the subgroup of principal Weil divisors of Stacks 0ENR”.

> **Stacks 0EPU, part (2), well-definedness.** The Weil divisor class of `ℒ` does not depend
> on the chosen nonzero meromorphic section: if the ratios of `s` and of `s'` at the generic point
> of every prime divisor differ by the image of an invertible rational function `f` — which is the
> assertion `f = s/s' ∈ R(X)^*` of Stacks 0EPT — then `div_ℒ(s)` and `div_ℒ(s')` differ by the
> principal divisor `div(f)`, hence have the same class in `Cl(X)`.

```lean
theorem divisorClassOfSection_eq (L : Modules.{u, max u z} B S hS X hX)
    (s s' : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s ratio W = 0 then ∅
      else W.support B S hS X)
    (hfin' : LocallyFinite fun W : PrimeDivisor B S hS X ↦
      if divisorCoefficients.{u, z} B S hS hX hdec L s' ratio W = 0 then ∅
      else W.support B S hS X)
    (f : (rationalFunctions B S hS hX)ˣ)
    (hs : ∀ W : PrimeDivisor B S hS X,
      (ratio W s : W.genericTotalFractionRing B S hS hX hdec) =
        E.emb W (f : rationalFunctions B S hS hX) *
          (ratio W s' : W.genericTotalFractionRing B S hS hX hdec)) :
    divisorClassOfSection.{u, z} B S hS hX hdec E L s ratio hfin =
      divisorClassOfSection.{u, z} B S hS hX hdec E L s' ratio hfin'
```

**`AlgebraicGeometry.Space.divisorClassOfSectionOfGenerating`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassOfSection.lean#L171). The attribute's comment: “part (2): the Weil divisor class of ℒ in Cl(X), with the local finiteness of the support of div\_ℒ(s) supplied by Stacks 0EPS from the open subspace U over which s generates ℒ”.

> **Stacks 0EPU, part (2).** The Weil divisor class of `ℒ`, with the local finiteness that
> makes `div_ℒ(s)` a Weil divisor supplied by Stacks 0EPS from a nonempty open subset of `|X|`
> containing the generic point of no prime divisor along which `s` has nonzero order — the open
> subspace over which the nonzero meromorphic section `s` generates `ℒ`.

```lean
def divisorClassOfSectionOfGenerating
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X)) (L : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (ratio : LocalRatioFamily.{u, z} B S hS hX hdec L)
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hgen : ∀ W : PrimeDivisor B S hS X,
      divisorCoefficients.{u, z} B S hS hX hdec L s ratio W ≠ 0 →
        W.genericPoint B S hS X ∈ Uᶜ) :
    E.weilDivisorClassGroup
```

## Tag 0EPV, a lemma

[Tag 0EPV](https://stacks.math.columbia.edu/tag/0EPV) in the Stacks Project.

**`AlgebraicGeometry.Space.orderOfVanishingSection_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean, line 938](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DivisorOfMeromorphicSection.lean#L938). The attribute's comment: “div\_\{ℒ⊗𝒩}(st) = div\_ℒ(s) + div\_𝒩(t) coefficientwise; ℒ⊗𝒩 is the module `M`”.

> **Stacks 0EPV, coefficientwise.** If the ratio of `st` at the generic point of `Z` is the
> product of the ratios of `s` and of `t`, then
> `ord_{Z,ℒ⊗𝒩}(st) = ord_{Z,ℒ}(s) + ord_{Z,𝒩}(t)`. Summing over all prime divisors this is the
> identity `div_{ℒ⊗𝒩}(st) = div_ℒ(s) + div_𝒩(t)` of Weil divisors.

```lean
theorem orderOfVanishingSection_mul (L N M : Modules.{u, max u z} B S hS X hX)
    (s : MeromorphicSection.{u, z} B S hS X hX L)
    (t : MeromorphicSection.{u, z} B S hS X hX N)
    (st : MeromorphicSection.{u, z} B S hS X hX M)
    (ratioL : LocalRatio.{u, z} B S hS hX hdec Z L)
    (ratioN : LocalRatio.{u, z} B S hS hX hdec Z N)
    (ratioM : LocalRatio.{u, z} B S hS hX hdec Z M)
    (hst : (ratioM st : Z.genericTotalFractionRing B S hS hX hdec) =
      (ratioL s : Z.genericTotalFractionRing B S hS hX hdec) *
        (ratioN t : Z.genericTotalFractionRing B S hS hX hdec)) :
    orderOfVanishingSection.{u, z} B S hS hX hdec Z M st ratioM =
      orderOfVanishingSection.{u, z} B S hS hX hdec Z L s ratioL +
        orderOfVanishingSection.{u, z} B S hS hX hdec Z N t ratioN
```

**`AlgebraicGeometry.Space.exists_ne_zero_weilDivisorOfSection_meromorphicSectionTensor_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleWeilDivisorClass.lean#L335). The attribute's comment: “the whole lemma at the source's hypotheses: for nonzero meromorphic sections s of ℒ and t of 𝒩 on a locally Noetherian integral X, the product st (meromorphicSectionTensor) is a nonzero meromorphic section of ℒ ⊗ 𝒩, div\_\{ℒ⊗𝒩}(st) = div\_ℒ(s) + div\_𝒩(t) in Div(X), and the Weil divisor class of ℒ ⊗ 𝒩 in the canonical Cl(X) of Stacks 0ENR is the sum of the classes of ℒ and 𝒩 (Stacks 0EPU part (2) evaluated at s, t and st)”.

> **Stacks 0EPV.** Let `X` be a locally Noetherian integral algebraic space over `S`, let `ℒ`,
> `𝒩` be invertible `𝒪_X`-modules and let `s`, resp. `t`, be a nonzero meromorphic section of `ℒ`,
> resp. `𝒩`. Then `st` is a nonzero meromorphic section of `ℒ ⊗_{𝒪_X} 𝒩` and
>
> `div_{ℒ⊗𝒩}(st) = div_ℒ(s) + div_𝒩(t)`
>
> in `Div(X)`. In particular the Weil divisor class of `ℒ ⊗_{𝒪_X} 𝒩` is the sum of the Weil divisor
> classes of `ℒ` and of `𝒩`, in the class group `Cl(X)` of Stacks 0ENR.
>
> The product `st` is `AlgebraicGeometry.Space.meromorphicSectionTensor`, the global product of
> the two sections (the chartwise product of their representatives over every affine chart), whose
> hypotheses (a) and (b) of Stacks 0EN6 are `X`'s own; the divisors are
> `AlgebraicGeometry.Space.weilDivisorOfSection` (Stacks 0EPU, part (1)). The product is regular,
> hence nonzero; at the generic point of every prime divisor its coefficient is a unit times the
> product of the coefficients of `s` and of `t`, so the orders of vanishing add up. The class
> statement is then the definition of the class
> (`AlgebraicGeometry.Space.weilDivisorClassOfInvertible`, Stacks 0EPU, part (2)) evaluated at `s`,
> `t` and `st`, by `AlgebraicGeometry.Space.weilDivisorClassOfInvertible_eq`, and additivity of the
> quotient map `Div(X) → Cl(X)`.

```lean
theorem exists_ne_zero_weilDivisorOfSection_meromorphicSectionTensor_eq_add
    (L N : Modules.{u, u} B S hS X hX) (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (hNinv : IsInvertibleModule (B := B) ⟨X, hX⟩ N)
    (s : MeromorphicSection.{u, u} B S hS X hX L) (t : MeromorphicSection.{u, u} B S hS X hX N)
    (hs : s ≠ 0) (ht : t ≠ 0) :
    ∃ hst : meromorphicSectionTensor B S hS hX
        (fun _ hz => (weaklyAssociatedPointsOfSpace_eq_setOf_localRingDimension_eq_zero
          B S hS ⟨X, hX⟩ hInt.hasEtaleLocalProperty_isReduced).subset hz)
        (hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian B S hS X hX hN) L N s t
        (isQuasicoherentOnSite_of_isInvertibleModule (⟨X, hX⟩ : AlgebraicSpaces B S hS) L hL)
        (isQuasicoherentOnSite_of_isInvertibleModule (⟨X, hX⟩ : AlgebraicSpaces B S hS) N
          hNinv) ≠ 0,
      weilDivisorOfSection B S hS hX hInt hN (picardTensorModule B S hS hX L N)
          (isInvertibleModule_picardTensorModule B S hS hX L N hL hNinv) _ hst =
        weilDivisorOfSection B S hS hX hInt hN L hL s hs +
          weilDivisorOfSection B S hS hX hInt hN N hNinv t ht ∧
      weilDivisorClassOfInvertible B S hS hX hInt hN (picardTensorModule B S hS hX L N)
          (isInvertibleModule_picardTensorModule B S hS hX L N hL hNinv) =
        weilDivisorClassOfInvertible B S hS hX hInt hN L hL +
          weilDivisorClassOfInvertible B S hS hX hInt hN N hNinv
```

**`AlgebraicGeometry.Space.PicardDivisorData.divisor_picardTensorModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClass.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClass.lean#L454). The attribute's comment: “the identity div\_\{ℒ⊗𝒩}(st) = div\_ℒ(s) + div\_𝒩(t) in Div(X), at the sections and ratio families chosen by PicardDivisorData; st/(s\_ξ t\_ξ) = (s/s\_ξ)(t/t\_ξ), the source's own computation, is the argument hst, as it is in the coefficientwise orderOfVanishingSection\_mul: the ratio s/s\_ξ is a parameter here as in Stacks 0EPR, and the generator chosen at ξ for ℒ⊗𝒩 differs from s\_ξ ⊗ t\_ξ by a unit that no choice pins to 1 (HasCanonicalTensorProductSection), so hst is not derivable. What the data gives with no extra input is the weaker exists\_ord\_sub\_eq\_tensorModule, used by divisorClass\_picardTensorModule”.

> **Stacks 0EPV, the identity in `Div(X)`.** The Weil divisor of the chosen section of
> `ℒ ⊗ 𝒩` is the sum of the Weil divisors of the chosen sections of `ℒ` and of `𝒩`, as soon as
> the ratio of the chosen section of the tensor product is the product of the ratios.
>
> This is `div_{ℒ⊗𝒩}(st) = div_ℒ(s) + div_𝒩(t)` as an identity of Weil divisors, on the nose
> rather than up to the divisor of a rational function;
> `AlgebraicGeometry.Space.orderOfVanishingSection_mul` is the same identity coefficientwise at a
> single prime divisor, of which this is the sum over all of them.
>
> The ratio identity `st/(s_ξ t_ξ) = (s/s_ξ)(t/t_ξ)` is the source's own computation, and it is
> the argument `hst` here rather than a field of `AlgebraicGeometry.Space.PicardDivisorData`,
> exactly as it is the argument `hst` of the coefficientwise
> `AlgebraicGeometry.Space.orderOfVanishingSection_mul`. It is not derivable from the data, and
> for two independent reasons. The generator chosen at `ξ` for `ℒ ⊗ 𝒩` and the product of the
> generators chosen for `ℒ` and for `𝒩` are two free generators of one invertible module, so they
> differ by a unit of the local ring that nothing pins to `1` — see the docstring of
> `AlgebraicGeometry.Space.HasCanonicalTensorProductSection`, which is why the canonical choices
> produce the identity only up to such a unit. And the section chosen for `ℒ ⊗ 𝒩` is a section of
> that module alone: it differs from the product of the chosen sections of `ℒ` and of `𝒩` by an
> element of `R(X)^*` whose divisor is in general nonzero. What the data does give, with no extra
> argument, is the weaker `exists_ord_sub_eq_tensorModule` — the two divisors differ by the
> divisor of an invertible rational function — and that is what
> `AlgebraicGeometry.Space.PicardDivisorData.divisorClass_picardTensorModule` uses, which is why
> only the *class* of the divisor of a tensor product is additive for an arbitrary
> `AlgebraicGeometry.Space.PicardDivisorData`.

```lean
theorem divisor_picardTensorModule (L N : Modules.{u, u} B S hS X hX)
    (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (hN : IsInvertibleModule (B := B) ⟨X, hX⟩ N)
    (hst : ∀ W : PrimeDivisor B S hS X,
      (D.ratio (picardTensorModule B S hS hX L N)
          (isInvertibleModule_picardTensorModule B S hS hX L N hL hN) W
          (D.sect _ (isInvertibleModule_picardTensorModule B S hS hX L N hL hN)) :
        W.genericTotalFractionRing B S hS hX hdec) =
        (D.ratio L hL W (D.sect L hL) : W.genericTotalFractionRing B S hS hX hdec) *
          (D.ratio N hN W (D.sect N hN) : W.genericTotalFractionRing B S hS hX hdec)) :
    D.divisor (picardTensorModule B S hS hX L N)
        (isInvertibleModule_picardTensorModule B S hS hX L N hL hN) =
      D.divisor L hL + D.divisor N hN
```

**`AlgebraicGeometry.Space.PicardDivisorData.divisorClass_picardTensorModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClass.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClass.lean#L493). The attribute's comment: “the in-particular clause: the Weil divisor class of ℒ ⊗ 𝒩 is the sum of the Weil divisor classes of ℒ and of 𝒩, from the field exists\_ord\_sub\_eq\_tensorModule and so with nothing assumed of the chosen sections; divisor\_picardTensorModule is the identity in Div(X), which needs the ratio identity. Cl(X) is Stacks 0ENR relative to the embedding R(X) → Q(𝒪^h\_\{X,ξ}) of Stacks 0ENK, which is the parameter E inhabited by genericFractionEmbedding”.

> **Stacks 0EPV, the clause in `Cl(X)`.** The Weil divisor class of a tensor product of
> invertible `𝒪_X`-modules is the sum of their Weil divisor classes: the Weil divisor of the
> chosen section of `ℒ ⊗ 𝒩` and the sum of the Weil divisors of the chosen sections of `ℒ` and of
> `𝒩` differ by `div(f)` for an invertible rational function `f`, which is zero in `Cl(X)`.
>
> This is the source's "in particular" clause.  It asks nothing of the three chosen sections, so
> unlike `AlgebraicGeometry.Space.PicardDivisorData.divisor_picardTensorModule` it is not an
> identity in `Div(X)`.

```lean
theorem divisorClass_picardTensorModule (L N : Modules.{u, u} B S hS X hX)
    (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L)
    (hN : IsInvertibleModule (B := B) ⟨X, hX⟩ N) :
    D.divisorClass (picardTensorModule B S hS hX L N)
        (isInvertibleModule_picardTensorModule B S hS hX L N hL hN) =
      D.divisorClass L hL + D.divisorClass N hN
```

**`AlgebraicGeometry.Space.exists_divisorOfSection_canonicalLocalRatioFamily_picardTensorModule_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassTensor.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassTensor.lean#L615). The attribute's comment: “the identity div\_\{ℒ⊗𝒩}(st) = div\_ℒ(s) + div\_𝒩(t) in Div(X), read through the ratio families of Stacks 0EPR, for arbitrary regular meromorphic sections s of ℒ and t of 𝒩 and for their product st, whose existence is the source's first clause and is asserted here too; nothing is assumed beyond X being decent, locally Noetherian and integral. The source's computation st/(s\_ξ t\_ξ) = (s/s\_ξ)(t/t\_ξ) holds up to a unit of 𝒪\_\{U,u}, the discrepancy between the generator chosen at ξ for ℒ⊗𝒩 and the product of those chosen for ℒ and for 𝒩, and that unit has order of vanishing zero. The whole lemma for nonzero sections, with the in-particular clause in the canonical Cl(X), is exists\_ne\_zero\_weilDivisorOfSection\_meromorphicSectionTensor\_eq\_add”.

> **Stacks 0EPV's identity in `Div(X)`.**  Let `X` be a decent, locally Noetherian, integral
> algebraic space over `S`, let `ℒ` and `𝒩` be invertible `𝒪_X`-modules, let `s` be a regular
> meromorphic section of `ℒ` and let `t` be one of `𝒩`.  Then there is a regular meromorphic
> section `st` of `ℒ ⊗ 𝒩` which is the product of `s` and of `t` — its coefficient of Stacks 0EPR
> at the generic point of every prime divisor is the product of the coefficients of `s` and of
> `t`, up to a unit of `𝒪_{U, u}` — and the Weil divisors read through the ratio families of
> Stacks 0EPR satisfy
>
> `div_{ℒ⊗𝒩}(st) = div_ℒ(s) + div_𝒩(t)`
>
> as an identity of elements of `Div(X)`, on the nose and not merely up to the divisor of a
> rational function.  Nothing is assumed beyond `X` itself.
>
> This is the source's statement: the existence of the product section is its first clause and is
> asserted here too, the identity in `Div(X)` its second, and `s` and `t` range over all regular
> meromorphic sections as they do there.  The unit in the product clause is unavoidable and is
> harmless: the generator chosen at `ξ` for `ℒ ⊗ 𝒩` and the product of the generators chosen for
> `ℒ` and for `𝒩` are two free generators of one invertible module, so they differ by a unit
> (`AlgebraicGeometry.Space.PrimeDivisor.exists_isUnit_smul_genericStalkGenerator`) whose order of
> vanishing is zero — the source's own computation `st/(s_ξ t_ξ) = (s/s_ξ)(t/t_ξ)` holds up to
> exactly that unit, and it is discarded by
> `AlgebraicGeometry.Space.PrimeDivisor.orderOfVanishingSection_canonicalLocalRatio_eq_add_of_genericStalkCoefficient_eq_unit_mul`.
>
> The product section is the chartwise product
> `AlgebraicGeometry.Space.meromorphicSectionTensorMul` amalgamated over an affine covering,
> `AlgebraicGeometry.Space.meromorphicSectionTensor`, and the local finiteness that makes each of
> the three divisors an element of `Div(X)` is
> `AlgebraicGeometry.Space.locallyFinite_divisorCoefficients_ne_zero_canonicalLocalRatioFamily`.
>
> `AlgebraicGeometry.Space.PicardDivisorData.divisor_picardTensorModule` is the same identity for
> the sections and ratio families that an arbitrary
> `AlgebraicGeometry.Space.PicardDivisorData` chooses, where the chosen section of `ℒ ⊗ 𝒩` has no
> relation to the chosen sections of `ℒ` and of `𝒩` and the ratio identity has to be supplied; at
> the canonical choices and for the product section, as here, it is proved.

```lean
theorem exists_divisorOfSection_canonicalLocalRatioFamily_picardTensorModule_eq_add
    (s : MeromorphicSection.{u, u} B S hS X hX L)
    (t : MeromorphicSection.{u, u} B S hS X hX N)
    (hs : IsRegularMeromorphicSection.{u, u} B S hS X hX L s)
    (ht : IsRegularMeromorphicSection.{u, u} B S hS X hX N t) :
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hNoeth
    ∃ (st : MeromorphicSection.{u, u} B S hS X hX (picardTensorModule B S hS hX L N))
      (_ : IsRegularMeromorphicSection.{u, u} B S hS X hX
        (picardTensorModule B S hS hX L N) st),
      (∀ W : PrimeDivisor B S hS X,
          ∃ w : (structurePresheaf B S hS (W.genericStalkSpace B S hS hX hdec).1).obj
            (op (W.genericStalkChart B S hS hX hdec)),
            IsUnit w ∧
              W.genericStalkCoefficient B S hS hX hdec (picardTensorModule B S hS hX L N)
                  (isInvertibleModule_picardTensorModule B S hS hX L N hL hNinv) st =
                algebraMap ((structurePresheaf B S hS
                      (W.genericStalkSpace B S hS hX hdec).1).obj
                    (op (W.genericStalkChart B S hS hX hdec)))
                  ((meromorphicFunctionSheaf B S hS (W.genericStalkSpace B S hS hX hdec).1
                    (W.genericStalkSpace B S hS hX hdec).2).obj.obj
                      (op (W.genericStalkChart B S hS hX hdec))) w *
                  (W.genericStalkCoefficient B S hS hX hdec L hL s *
                    W.genericStalkCoefficient B S hS hX hdec N hNinv t)) ∧
        ∃ (hfinst : LocallyFinite fun W : PrimeDivisor B S hS X =>
              if divisorCoefficients.{u, u} B S hS hX hdec
                  (picardTensorModule B S hS hX L N) st
                  (canonicalLocalRatioFamily B S hS hX hdec
                    (picardTensorModule B S hS hX L N)
                    (isInvertibleModule_picardTensorModule B S hS hX L N hL hNinv)
                    hInt hNoeth) W = 0 then ∅
              else W.support B S hS X)
          (hfins : LocallyFinite fun W : PrimeDivisor B S hS X =>
              if divisorCoefficients.{u, u} B S hS hX hdec L s
                  (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hNoeth) W = 0 then ∅
              else W.support B S hS X)
          (hfint : LocallyFinite fun W : PrimeDivisor B S hS X =>
              if divisorCoefficients.{u, u} B S hS hX hdec N t
                  (canonicalLocalRatioFamily B S hS hX hdec N hNinv hInt hNoeth) W = 0 then ∅
              else W.support B S hS X),
          divisorOfSection.{u, u} B S hS hX hdec (picardTensorModule B S hS hX L N) st
                (canonicalLocalRatioFamily B S hS hX hdec (picardTensorModule B S hS hX L N)
                  (isInvertibleModule_picardTensorModule B S hS hX L N hL hNinv) hInt hNoeth)
                hfinst =
            divisorOfSection.{u, u} B S hS hX hdec L s
                (canonicalLocalRatioFamily B S hS hX hdec L hL hInt hNoeth) hfins +
              divisorOfSection.{u, u} B S hS hX hdec N t
                (canonicalLocalRatioFamily B S hS hX hdec N hNinv hInt hNoeth) hfint
```

## Tag 0EPW, an equation

[Tag 0EPW](https://stacks.math.columbia.edu/tag/0EPW) in the Stacks Project.

**`AlgebraicGeometry.Space.canonicalPicardToWeilDivisorClassHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassHom.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassHom.lean#L107). The attribute's comment: “the homomorphism Pic(X) → Cl(X) assigning to an invertible module its Weil divisor class, on a locally Noetherian integral algebraic space X over a scheme S — the hypotheses of Lemma 72.7.5 and no others, decency coming from integrality by `IsIntegralSpace.isDecentSpace`”.

> The homomorphism of abelian groups
>
> `Pic(X) ⟶ Cl(X)`
>
> which assigns to an invertible `𝒪_X`-module its Weil divisor class, on a locally Noetherian
> integral algebraic space `X` over a scheme `S`.
>
> It is
> `AlgebraicGeometry.Space.PicardDivisorData.picardToWeilDivisorClassGroup` at the canonical
> choices: the embedding `R(X) → Q(𝒪^h_{X, ξ})` of Stacks 0ENK, the regular meromorphic sections
> of Stacks 0EPQ and the ratio family of Stacks 0EPR.  Its value on the class of an invertible
> module is that module's Weil divisor class
> (`AlgebraicGeometry.Space.canonicalPicardToWeilDivisorClassHom_picardClass`), well defined on
> isomorphism classes by Stacks 0EPT, and additivity is Stacks 0EPV, addition in `Pic(X)` being
> tensor product.

```lean
def canonicalPicardToWeilDivisorClassHom :
    haveI hdec : IsDecentSpace B S hS X := hInt.isDecentSpace B S hS X
    picardGroup (B := B) (S := S) (hS := hS) ⟨X, hX⟩ →+
      (genericFractionEmbedding B S hS hX hdec hInt hN).weilDivisorClassGroup
```

**`AlgebraicGeometry.Space.canonicalPicardToWeilDivisorClassHom_picardClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassHom.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassHom.lean#L135). The attribute's comment: “the value of the homomorphism Pic(X) → Cl(X) on the class of an invertible module, which characterizes it, on a locally Noetherian integral algebraic space X over a scheme S — the hypotheses of Lemma 72.7.5 and no others, decency coming from integrality by `IsIntegralSpace.isDecentSpace`”.

> The homomorphism `Pic(X) ⟶ Cl(X)` sends the class of an invertible `𝒪_X`-module to its Weil
> divisor class — the class of the Weil divisor of the regular meromorphic section of Stacks 0EPQ
> read through the ratio family of Stacks 0EPR.  This characterizes the homomorphism, because every
> class in `Pic(X)` is the class of an invertible module.

```lean
theorem canonicalPicardToWeilDivisorClassHom_picardClass (L : Modules.{u, u} B S hS X hX)
    (hL : IsInvertibleModule (B := B) ⟨X, hX⟩ L) :
    haveI hdec : IsDecentSpace B S hS X := hInt.isDecentSpace B S hS X
    haveI : ∀ W : PrimeDivisor B S hS X,
        Nontrivial ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.nontrivial_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        IsNoetherianRing ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.isNoetherianRing_genericHenselianLocalRing B S hS hX hdec hInt hN
    haveI : ∀ W : PrimeDivisor B S hS X,
        Ring.KrullDimLE 1 ↥(W.genericHenselianLocalRing B S hS hX hdec) := fun W =>
      W.krullDimLE_genericHenselianLocalRing B S hS hX hdec hInt hN
    canonicalPicardToWeilDivisorClassHom B S hS hX hInt hN
          (picardClass (B := B) ⟨X, hX⟩ L hL) =
        (canonicalPicardDivisorData B S hS hX hdec hInt hN
          (canonicalRatioIsUnitOnGeneratingChart B S hS hX hdec hInt hN)
          (canonicalTensorDivisorIdentity_of_exists_product B S hS hX hdec hInt hN
            (hasCanonicalTensorProductSection B S hS hX hdec hInt hN))).divisorClass L hL
```

## Tag 0EPX, a lemma

[Tag 0EPX](https://stacks.math.columbia.edu/tag/0EPX) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_canonicalPicardToWeilDivisorClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassInjective.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PicardWeilDivisorClassInjective.lean#L324). The attribute's comment: “injectivity of Pic(X) → Cl(X) — the homomorphism of Stacks 0EPW at the canonical choices, which takes no auxiliary data — on a normal, locally Noetherian, integral algebraic space over a scheme. No hypothesis beyond the source's: decency comes from integrality by `IsIntegralSpace.isDecentSpace`, the claim of the source is `picardClass_eq_zero_of_forall_isUnit_canonicalGenericRatio`, the rescaling t = f⁻¹ s is `exists_isRegularMeromorphicSection_canonicalLocalRatio_eq_genericEmb_mul`, and the three instance hypotheses on the henselian local rings at the generic points of the prime divisors are conclusions of Stacks 0ENK”.

> **Stacks 0EPX.** On a normal, locally Noetherian, integral algebraic space `X` over a scheme
> `S`, the homomorphism
>
> `Pic(X) ⟶ Cl(X)`
>
> of Stacks 0EPW — `AlgebraicGeometry.Space.canonicalPicardToWeilDivisorClassHom`, which takes no
> auxiliary data — is injective.
>
> The binders are the source's and nothing else: `X` an algebraic space over the scheme `S`
> (`hX`), integral (`hInt`), locally Noetherian (`hN`) and normal (`hNormal`). There is no
> auxiliary embedding, no divisor data, no decency hypothesis — Stacks 0AD4 puts decency *inside*
> integrality, so `AlgebraicGeometry.Space.IsIntegralSpace.isDecentSpace` supplies it — no instance
> hypotheses on the henselian local rings at the generic points of the prime divisors, and nothing
> left of the claim the source makes and calls the whole content of the lemma: that is
> `AlgebraicGeometry.Space.picardClass_eq_zero_of_forall_isUnit_canonicalGenericRatio`, passed
> below. See the module docstring for what each of those discharges is.
>
> Triviality of `ℒ` is written as the vanishing of its class in `Pic(X)`, which by
> `AlgebraicGeometry.Space.picardClass_eq_zero_iff` says that `ℒ` is isomorphic to `𝒪_X`.

```lean
theorem injective_canonicalPicardToWeilDivisorClassHom (hNormal : IsNormal B S hS X) :
    Function.Injective (canonicalPicardToWeilDivisorClassHom B S hS hX hInt hN)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.7, Tag 0ENV](https://stacks.math.columbia.edu/tag/0ENV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
