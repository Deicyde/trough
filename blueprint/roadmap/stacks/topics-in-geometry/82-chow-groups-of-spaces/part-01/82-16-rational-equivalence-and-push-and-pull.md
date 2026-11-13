---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.flatPullbackMap_rationalFunctionPrincipalDivisorCycle_eq_finsum_components, AlgebraicGeometry.Space.rationallyEquivalentCanonical_flatPullbackMap, AlgebraicGeometry.Space.rationallyEquivalentCanonical_properCyclePushforward
statement: formalized
proof: formalized
---

# 82.16 Rational equivalence and push and pull

Section 82.16 of the Stacks Project, [Tag 0EQ9](https://stacks.math.columbia.edu/tag/0EQ9). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EQA, a lemma

[Tag 0EQA](https://stacks.math.columbia.edu/tag/0EQA) in the Stacks Project.

**`AlgebraicGeometry.Space.flatPullbackMap_rationalFunctionPrincipalDivisorCycle_eq_finsum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackPrincipalDivisorComponents.lean, line 719](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackPrincipalDivisorComponents.lean#L719). The attribute's comment: “the displayed identity of (k + r - 1)-cycles on X, at every integral closed subspace of X; the sum is over the irreducible components X' of X (a locally finite family), m\_\{X',X} is the length of O\_X at the generic point of X' (0EE9 part (1) for the space X), g ∘ f|\_\{X'} is the image of g under the extension of function fields of the dominant f|\_\{X'} (0EML), and every cycle is the one of this chapter: f^* is 0EP8, div is 0EQ1 at the canonical embeddings of 0ENK, (X' → X)\_* is 0EP1; the hypotheses are exactly the tag's”.

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

**`AlgebraicGeometry.Space.rationallyEquivalentCanonical_flatPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackRationalEquivalenceCanonical.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackRationalEquivalenceCanonical.lean#L466). The attribute's comment: “f^*α ∼\_rat f^*β in Z\_\{m+r}(X) for α ∼\_rat β in Z\_m(Y), f flat of relative dimension r between good spaces over B; rational equivalence at the canonical embeddings of 0ENK, the presenting family on X indexed in max v (u+1) when the one on Y is indexed in v”.

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

**`AlgebraicGeometry.Space.rationallyEquivalentCanonical_properCyclePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardRationalEquivalence.lean, line 708](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardRationalEquivalence.lean#L708).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
