---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.properPushforward_principalDivisorCycle_eq_iff, AlgebraicGeometry.Space.properCyclePushforward_rationalFunctionPrincipalDivisorCycle, Stacks.Norm.norm_baseChange_eq_prod_quotient
statement: formalized
proof: formalized
---

# 82.14 Principal divisors and pushforward

Section 82.14 of the Stacks Project, [Tag 0EQ3](https://stacks.math.columbia.edu/tag/0EQ3). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EQ4, a lemma

[Tag 0EQ4](https://stacks.math.columbia.edu/tag/0EQ4) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushforward_principalDivisorCycle_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardPrincipalDivisor.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardPrincipalDivisor.lean#L403). The attribute's comment: “REDUCED, not proved: p\_*div(f) = div(g) in Z\_\{n-1}(Y) IF AND ONLY IF it holds at every prime divisor of Y; proved away from them, using dim\_δ(X) = dim\_δ(Y). Take g to be rationalFunctionNorm, the norm Nm\_\{R(X)/R(Y)} constructed here, for the source's statement”.

> **Stacks 0EQ4, reduced to its coefficients at the prime divisors of `Y`.** In Situation
> 0EDT let `X/B` and `Y/B` be good, let `p : X ⟶ Y` be quasi-compact over `B`, let `X` and `Y` be
> integral with `dim_δ(X) = dim_δ(Y) = n`, and let `f ∈ R(X)^*` and `g ∈ R(Y)^*`. Then
>
> `p_* div(f) = div(g)` in `Z_{n-1}(Y)`
>
> holds exactly when it holds coefficientwise at every prime divisor of `Y`, that is when
>
> `∑_Z ord_Z(f) · deg(Z/Z') = ord_{Z'}(g)`
>
> for every prime divisor `Z' ⊆ Y`, the sum being over the integral closed subspaces `Z ⊆ X`.
>
> Both sides are coefficient families on the integral closed subspaces of `Y`, and away from the
> prime divisors of `Y` both vanish: the coefficient of `div(g)` at an integral closed subspace
> whose point set does not have codimension one is zero by Stacks 0ENP, and the pushforward has no
> contribution there by
> `AlgebraicGeometry.Space.properPushforwardCoeff_principalDivisorCycleCoefficients_eq_zero`,
> which is where the equality of the δ-dimensions is used. That is the whole content of the
> reduction; the coefficient identity at a prime divisor of `Y` — which is the mathematical
> content of Stacks 0EQ4 — is *not* proved here, and is not assumed either. Taking
> `g = Nm_{R(X)/R(Y)}(f)`, that is
> `AlgebraicGeometry.Space.rationalFunctionNorm D.site D.base D.base_mem … p hgen f`, gives the
> source's statement.

```lean
theorem properPushforward_principalDivisorCycle_eq_iff
    (hfinX : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if principalDivisorCoefficients D.site D.base D.base_mem hX.1 hdecX embX f hf W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hfinY : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem Y =>
      if principalDivisorCoefficients D.site D.base D.base_mem hY.1 hdecY embY g hg W = 0 then ∅
      else W.support D.site D.base D.base_mem Y)
    {p : X ⟶ Y} (hpB : p ≫ sY = sX) (hp : IsQuasiCompact D.site D.base D.base_mem p) :
    properCyclePushforward D sX hX sY hY hpB hp (n - 1)
          (principalDivisorCycle D sX hX hdecX embX f hf hfinX hintX dX hdX hnX) =
        principalDivisorCycle D sY hY hdecY embY g hg hfinY hintY dY hdY hnY ↔
      ∀ W : PrimeDivisor D.site D.base D.base_mem Y,
        (∑ᶠ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
            principalDivisorCycleCoefficients D sX hX hdecX embX f hf Z *
              properCycleMult D sX hX sY hY p Z
                (W.toIntegralClosedSubspace D.site D.base D.base_mem)) =
          principalDivisorCoefficients D.site D.base D.base_mem hY.1 hdecY embY g hg W
```

**`AlgebraicGeometry.Space.properCyclePushforward_rationalFunctionPrincipalDivisorCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardPrincipalDivisorCanonical.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardPrincipalDivisorCanonical.lean#L641). The attribute's comment: “p\_* div(f) = div(Nm\_\{R(X)/R(Y)}(f)) in Z\_\{n-1}(Y), for X/B, Y/B good and integral with dim\_δ X = dim\_δ Y = n, p : X → Y dominant and proper, f ∈ R(X)^*; div is 0EQ1 at the canonical embeddings, p\_* is 0EP2, the norm is constructed; nothing carried”.

> **Stacks 0EQ4.** In Situation 0EDT let `X/B` and `Y/B` be good, let `X` and `Y` be integral
> with `n = dim_δ(X) = dim_δ(Y)`, let `p : X ⟶ Y` be a dominant proper morphism, let `f ∈ R(X)^*`
> and set `g = Nm_{R(X)/R(Y)}(f)`. Then
>
> `p_* div(f) = div(g)` in `Z_{n-1}(Y)`.
>
> Here `div` is the principal divisor of Stacks 0EQ1
> (`AlgebraicGeometry.Space.rationalFunctionPrincipalDivisorCycle`, at the canonical embeddings of
> Stacks 0ENK), `p_*` is proper pushforward of cycles (Stacks 0EP2) and `g` is the norm
> `AlgebraicGeometry.Space.rationalFunctionNorm` along the extension of function fields `p`
> induces, as a unit of `R(Y)` (`AlgebraicGeometry.Space.rationalFunctionNormUnit`); `R(X)/R(Y)`
> is finite (Stacks 0AD5, from `dim_δ(X) = dim_δ(Y)`). Both sides are `(n-1)`-cycles on `Y`,
> determined by their coefficients at the prime divisors of `Y`, where they agree by
> `AlgebraicGeometry.Space.finsum_rationalFunctionPrincipalDivisorCycle_mul_properCycleMult_eq`.

```lean
theorem properCyclePushforward_rationalFunctionPrincipalDivisorCycle {p : X ⟶ Y}
    (hpB : p ≫ sY = sX) (hproper : IsProper D.site D.base D.base_mem p)
    (hdom : IsDominant D.site D.base D.base_mem p) {n : ℤ}
    (hnX : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hnY : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (n : EInt))
    (f : (rationalFunctions D.site D.base D.base_mem hX.1)ˣ) :
    properCyclePushforward D sX hX sY hY hpB hproper.2.1.2 (n - 1)
        (rationalFunctionPrincipalDivisorCycle D sX hX hintX hnX f) =
      rationalFunctionPrincipalDivisorCycle D sY hY hintY hnY
        (rationalFunctionNormUnit D.site D.base D.base_mem hX.1 hY.1 hintX hintY p
          (pointsMap_genericPoint_of_isDominant D.site D.base D.base_mem hX.1 hY.1 hintX hintY
            p hdom) f)
```

**`Stacks.Norm.norm_baseChange_eq_prod_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Norm/BaseChangeProduct.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Norm/BaseChangeProduct.lean#L154). The attribute's comment: “the field-theoretic norm compatibility at the end of the proof, for which the source says 'we omit the proof': for L/K finite and M/K finite separable, M ⊗\_K L = ∏ M\_i and Nm\_\{L/K}(t) = ∏ Nm\_\{M\_i/M}(t\_i)”.

> **The field-theoretic step of Stacks 0EQ4, whose proof the source omits.** Let `K` be a
> field, `L/K` a finite extension and `M/K` a finite *separable* extension. Then `M ⊗_K L` is a
> finite product of fields `∏ᵢ Mᵢ` — concretely, the product of its quotients by its maximal
> ideals — and for `t ∈ L` the image in `M` of `Nm_{L/K}(t)` is the product of the norms over `M`
> of the images `tᵢ` of `1 ⊗ t`:
>
> `Nm_{L/K}(t) = ∏ᵢ Nm_{Mᵢ/M}(tᵢ)` in `M`.
>
> Separability of `M/K` is what makes `M ⊗_K L` reduced, and being also finite-dimensional over
> `M` it is then the product of its residue fields. The identity itself is base change of the norm
> followed by multiplicativity over the factors.

```lean
theorem norm_baseChange_eq_prod_quotient {K L M : Type*} [Field K] [Field L] [Field M]
    [Algebra K L] [Algebra K M] [FiniteDimensional K L] [FiniteDimensional K M]
    [Algebra.IsSeparable K M] [Fintype (MaximalSpectrum (M ⊗[K] L))] (t : L) :
    algebraMap K M (Algebra.norm K t) =
      ∏ p : MaximalSpectrum (M ⊗[K] L),
        Algebra.norm M (Ideal.Quotient.mk p.asIdeal (1 ⊗ₜ[K] t))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.14, Tag 0EQ3](https://stacks.math.columbia.edu/tag/0EQ3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
