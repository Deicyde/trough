---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PrimeDivisor.ord_eq_multiplicity_mul_ord, AlgebraicGeometry.Space.flatPullbackMap_rationalFunctionPrincipalDivisorCycle_eq_finsum_components, AlgebraicGeometry.Space.rationallyEquivalentCanonical_flatPullbackMap, AlgebraicGeometry.Space.rationallyEquivalentCanonical_properCyclePushforward
statement: formalized
proof: formalized
---

# 82.16 Rational equivalence and push and pull

Section 82.16 of the Stacks Project, [Tag 0EQ9](https://stacks.math.columbia.edu/tag/0EQ9). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQA, a lemma

[Tag 0EQA](https://stacks.math.columbia.edu/tag/0EQA) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.ord_eq_multiplicity_mul_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean#L375). The attribute's comment: “coefficientwise at a prime divisor Z of X with generic point ξ lying over a prime divisor Z' of Y with generic point ξ': the order of vanishing of a rational function pulls back with the multiplicity, ord\_Z(g ∘ f) = m · ord\_\{Z'}(g), where m is the colength of the extended maximal ideal — the multiplicity with which Z occurs in the closed subspace f^\{-1}(Z'), hence the coefficient the flat pullback of Stacks 0EP8 attaches to Z. PROVED, not assumed: that the order of vanishing multiplies by the multiplicity, from Stacks 02M1 (length\_baseChange\_eq\_length\_mul\_length\_quotient) applied to the cyclic modules O^h/a and O^h/b, which is how Stacks 02M1 computes with a multiplicity. For X integral this is the source's identity f^* div\_Y(g) = ∑ m\_\{X',X} (X' → X)\_* div\_\{X'}(g ∘ f|\_\{X'}) read at the coefficient of Z, the one component having multiplicity one; the statement is coefficientwise because neither side exists in this repository — the flat pullback of cycles is Stacks 0EP8 and the principal divisor div(g) is Stacks 0ENP — and for that same reason Stacks 0EPT and 0EPV are already carried coefficientwise here. NOT COVERED: for X with several irreducible components, the step from this identity to the cycle identity, namely the additivity over the components of the multiplicities of Stacks 0EE2 and Stacks 0EE9; the statement applies to X and to each component X' separately, with m read in each, but no additivity of those multiplicities is proved in this repository. RESTRICTED: carried as explicit named hypotheses are (i) the flat local homomorphism φ of the henselian local rings at the generic points, the map of henselian local rings induced by a morphism of decent algebraic spaces not being available here, with its locality and flatness as the hypotheses hloc and hflat; (ii) the embeddings R(Y) → Q(O^h\_\{Y,ξ'}) and R(X) → Q(O^h\_\{X,ξ}) of Stacks 0ENK as embY and embX, exactly as Stacks 0EPT carries them; (iii) the composite g ∘ f|\_X as the parameter gf together with hgf, that its ratio at ξ is the image under φ of the ratio of g at ξ' — this repository has no pullback of a rational function along a morphism of algebraic spaces, only the chartwise fraction rule a/b ↦ f-sharp a / f-sharp b of Stacks 0ENC, which is what hgf states; and (iv) finiteness of the multiplicity, as hm naming the natural number m it equals. Locality, Noetherianness and the dimension bound on the henselian local rings are instance arguments, as they are for PrimeDivisor.ord and orderOfVanishingSection themselves”.

> **Stacks 0EQA, coefficientwise.** *The order of vanishing of a rational function pulls back
> with multiplicities.* Let `f : X ⟶ Y` be flat, let `Z' ⊆ Y` and `Z ⊆ X` be prime divisors with
> `Z` lying over `Z'`, let `φ : 𝒪^h_{Y,ξ'} ⟶ 𝒪^h_{X,ξ}` be the induced flat local homomorphism and
> let `m` be the multiplicity of `Z` over `Z'`. For a rational function `g` on `Y` whose ratio at
> `ξ'` is `a / b` with `a` and `b` nonzerodivisors, and for the composite `g ∘ f|_X`, whose ratio
> at `ξ` is therefore `φ(a) / φ(b)`,
>
>   `ord_Z(g ∘ f|_X) = m · ord_{Z'}(g)`.
>
> The multiplicity `m` is the one with which `Z` occurs in `f^{-1}(Z')`, so for `X` integral this
> is the source's identity `f^* div_Y(g) = ∑ m_{X',X} (X' ⟶ X)_* div_{X'}(g ∘ f|_{X'})` read at
> the coefficient of `Z`; for `X` with several components it is each of the two readings of that
> identity, as the implementation notes explain.
>
> Nothing about the conclusion is assumed. The multiplicity enters as the colength `hm` and the
> whole content — that the order of vanishing multiplies by it — is `Ring.ord_map_of_flatHom`,
> which is Stacks 02M1 applied to `𝒪^h_{Y,ξ'} / a` and to `𝒪^h_{Y,ξ'} / b`.

```lean
theorem PrimeDivisor.ord_eq_multiplicity_mul_ord
    (hloc : IsLocalHom φ) (hflat : φ.Flat) {m : ℕ}
    (hm : primeDivisorFlatMultiplicity B S hS hX hdecX ZX hY hdecY ZY φ = (m : ℕ∞))
    (embY : rationalFunctions B S hS hY →+* ZY.genericTotalFractionRing B S hS hY hdecY)
    (embX : rationalFunctions B S hS hX →+* ZX.genericTotalFractionRing B S hS hX hdecX)
    (g : rationalFunctions B S hS hY) (gf : rationalFunctions B S hS hX)
    (a b : nonZeroDivisors ↥(ZY.genericHenselianLocalRing B S hS hY hdecY))
    (hg : embY g = IsLocalization.mk' (ZY.genericTotalFractionRing B S hS hY hdecY)
      (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)) b)
    (hgf : embX gf = IsLocalization.mk' (ZX.genericTotalFractionRing B S hS hX hdecX)
      (φ (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)))
      (⟨φ (b : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)),
        Ring.map_mem_nonZeroDivisors_of_flatHom hflat b.2⟩ :
        nonZeroDivisors ↥(ZX.genericHenselianLocalRing B S hS hX hdecX)))
    (hgu : IsUnit (embY g)) (hgfu : IsUnit (embX gf)) :
    ZX.ord B S hS hX hdecX (embX gf) hgfu =
      (m : ℤ) * ZY.ord B S hS hY hdecY (embY g) hgu
```

**`AlgebraicGeometry.Space.flatPullbackMap_rationalFunctionPrincipalDivisorCycle_eq_finsum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackPrincipalDivisorComponents.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackPrincipalDivisorComponents.lean#L719). The attribute's comment: “the displayed identity of (k + r - 1)-cycles on X, at every integral closed subspace of X; the sum is over the irreducible components X' of X (a locally finite family), m\_\{X',X} is the length of O\_X at the generic point of X' (0EE9 part (1) for the space X), g ∘ f|\_\{X'} is the image of g under the extension of function fields of the dominant f|\_\{X'} (0EML), and every cycle is the one of this chapter: f^* is 0EP8, div is 0EQ1 at the canonical embeddings of 0ENK, (X' → X)\_* is 0EP1”.

> **Stacks 0EQA.** *Flat pullback of a principal divisor.* In Situation 0EDT let `X, Y/B` be
> good, assume `Y` integral with `dim_δ(Y) = k`, and let `f : X ⟶ Y` be a flat morphism over `B`
> of relative dimension `r`. Then for `g ∈ R(Y)^*`
>
>   `f^* div_Y(g) = ∑_{X'} m_{X', X} (X' → X)_* div_{X'}(g ∘ f|_{X'})`
>
> as `(k + r - 1)`-cycles on `X`: at every integral closed subspace `Z ⊆ X` the coefficient of the
> flat pullback (Stacks 0EP8) of `div_Y(g)` (Stacks 0EQ1) is the sum over the irreducible
> components `X'` of `X` of `m_{X', X}`, the multiplicity of `X'` in `X` (Stacks 0EE9), times the
> coefficient at `Z` of the pushforward along `X' → X` (Stacks 0EP1) of the principal divisor of
> `g ∘ f|_{X'} ∈ R(X')^*`. The sum is a locally finite one, which is why the identity of cycles is
> stated at each coefficient.

```lean
theorem flatPullbackMap_rationalFunctionPrincipalDivisorCycle_eq_finsum_components {k : ℤ}
    (hk : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (k : EInt))
    (g : (rationalFunctions D.site D.base D.base_mem hY.1)ˣ)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) :
    (flatPullbackMap D sX hX sY hY f hbase r hflat hr (k - 1) (k + r - 1) (by ring)
        (rationalFunctionPrincipalDivisorCycle D sY hY hintY hk g)).1 Z =
      ∑ᶠ W : IrreducibleComponentSubspace D.site D.base D.base_mem hX.1,
        spaceMultiplicity D X hX.1 W.1 *
          (W.flatPullbackDivisorPushforward D sX hX sY hY f hbase r hr hflat hintY hk g).1 Z
```

## Tag 0EQB, a lemma

[Tag 0EQB](https://stacks.math.columbia.edu/tag/0EQB) in the Stacks Project.

**`AlgebraicGeometry.Space.rationallyEquivalentCanonical_flatPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackRationalEquivalenceCanonical.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackRationalEquivalenceCanonical.lean#L466). The attribute's comment: “f^*α ∼\_rat f^*β in Z\_\{m+r}(X) for α ∼\_rat β in Z\_m(Y), f flat of relative dimension r between good spaces over B; rational equivalence at the canonical embeddings of 0ENK, the presenting family on X indexed in max v (u+1) when the one on Y is indexed in v”.

> In Situation 0EDT let `X, Y/B` be good and let `f : X ⟶ Y` be a morphism over `B` which is
> flat of relative dimension `r`. If `α ∼_rat β` are rationally equivalent `m`-cycles on `Y`, then
> `f^*α ∼_rat f^*β` as `n`-cycles on `X`, where `m + r = n`.
>
> Rational equivalence is that of Stacks 0EQ6 with `div(g)` read at the canonical embeddings of
> Stacks 0ENK (`AlgebraicGeometry.Space.RationallyEquivalentCanonical`), and `f^*` is the flat
> pullback of cycles of Stacks 0EP8 (`AlgebraicGeometry.Space.flatPullbackMap`). The family
> presenting `α - β` is indexed in a universe `v`, the one presenting `f^*α - f^*β` in
> `max v (u + 1)`.

```lean
theorem rationallyEquivalentCanonical_flatPullbackMap (m n : ℤ) (hmn : m + (r : ℤ) = n)
    {α β : CycleGroup D sY m} (h : RationallyEquivalentCanonical.{v} D sY hY m α β) :
    RationallyEquivalentCanonical.{max v (u + 1)} D sX hX n
      (flatPullbackMap D sX hX sY hY f hbase r hflat hr m n hmn α)
      (flatPullbackMap D sX hX sY hY f hbase r hflat hr m n hmn β)
```

## Tag 0EQC, a lemma

[Tag 0EQC](https://stacks.math.columbia.edu/tag/0EQC) in the Stacks Project.

**`AlgebraicGeometry.Space.rationallyEquivalentCanonical_properCyclePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardRationalEquivalence.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardRationalEquivalence.lean#L708).

> **Stacks 0EQC.** In Situation 0EDT let `X/B` and `Y/B` be good and let `p : X ⟶ Y` be a
> proper morphism over the base. If `α, β ∈ Z_k(X)` are rationally equivalent, then `p_*α` is
> rationally equivalent to `p_*β`.
>
> Rational equivalence is that of Stacks 0EQ6 with the summands `div(f_j)` read at the canonical
> embeddings `R(W_j) → Q(𝒪^h_{W_j,ξ})` of Stacks 0ENK
> (`AlgebraicGeometry.Space.RationallyEquivalentCanonical`), and `p_*` is the proper pushforward of
> cycles of Stacks 0EP1.

```lean
theorem rationallyEquivalentCanonical_properCyclePushforward (sX : X ⟶ D.space)
    (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY) {p : X ⟶ Y} (hpB : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p) (k : ℤ) {α β : CycleGroup D sX k}
    (h : RationallyEquivalentCanonical.{v} D sX hX k α β) :
    RationallyEquivalentCanonical.{v} D sY hY k
      (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k α)
      (properCyclePushforward D sX hX sY hY hpB hp.2.1.2 k β)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.16, Tag 0EQ9](https://stacks.math.columbia.edu/tag/0EQ9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
