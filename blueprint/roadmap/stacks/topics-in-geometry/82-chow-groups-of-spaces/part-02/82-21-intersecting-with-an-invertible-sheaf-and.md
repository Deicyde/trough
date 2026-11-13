---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.firstChernClassCap_comm_iff_isRationallyEquivalentToZero, AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm, AlgebraicGeometry.Space.isRationallyEquivalentToZeroCanonical_firstChernCapCycleMap_canonicalFirstChernRule, AlgebraicGeometry.Space.canonicalFirstChernCapCanonicalChowMap, AlgebraicGeometry.Space.canonicalFirstChernCapCanonicalChowMap_chowClassCanonical, AlgebraicGeometry.Space.chowClassCanonical_firstChernCapCycleMap_firstChernCapCycleMap_comm
statement: formalized
proof: formalized
---

# 82.21 Intersecting with an invertible sheaf and rational equivalence

Section 82.21 of the Stacks Project, [Tag 0EQW](https://stacks.math.columbia.edu/tag/0EQW). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EQX, a lemma

[Tag 0EQX](https://stacks.math.columbia.edu/tag/0EQX) in the Stacks Project.

**`AlgebraicGeometry.Space.firstChernClassCap_comm_iff_isRationallyEquivalentToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapCommutativity.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassCapCommutativity.lean#L188). The attribute's comment: “not the lemma itself but its equivalence form: the equality c\_1(N) ∩ div\_L(s) = c\_1(L) ∩ div\_N(t) in CH\_\{n-2}(X) is shown to hold if and only if the first cycle of the key formula 0EQV is rationally equivalent to zero, for an arbitrary component rule chern of 0EQJ. The lemma's own statement is PROVED ELSEWHERE, unconditionally and at the hypotheses of 0EQX: canonicalFirstChernCap\_divisor\_comm of StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline, at the canonical component rule and the canonical divisors, registered under 0EQX as well. The equivalence is kept for its generality in chern, at which the key formula is the open predicate KeyFormula”.

> **The conclusion of Stacks 0EQX, reduced to the key formula of Stacks 0EQV, for an arbitrary
> component rule.**  In Situation 0EDT let `X/B` be good and integral with `dim_δ(X) = n`, let `ℒ`
> and `𝒩` be invertible with nonzero meromorphic sections `s` and `t`, and set `α = div_ℒ(s)`,
> `β = div_𝒩(t)`.  Then
>
> `c₁(𝒩) ∩ α = c₁(ℒ) ∩ β` in `CH_{n-2}(X)`
>
> holds if and only if the first cycle of the key formula of Section 0EQU is rationally equivalent
> to zero, where that cycle is
> `∑_i (Z_i → X)_*(ord_{B_i}(f_i) div_{𝒩|Z_i}(t_i|Z_i) - ord_{B_i}(g_i) div_{ℒ|Z_i}(s_i|Z_i))`.
>
> This is an equivalence, so it does not by itself prove the equality; what proves it is the key
> formula, which gives the right hand side.  **Stacks 0EQX itself is proved**, unconditionally and
> at its own hypotheses, by `AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline`, which is where the tag's
> mathematical content lives.  What this statement adds is the generality: the component cycle
> `c₁(ℒ|_W) ∩ [W]` of Stacks 0EQE is the explicit parameter `chern` of Stacks 0EQJ and the
> equivalence holds for every value of it, so it is the form that converts the open predicate
> `AlgebraicGeometry.Space.KeyFormula` — the key formula quantified over component rules and
> tame-symbol divisors — into the equality at that generality.  `CH_{n-2}(X)` is the Chow group of
> Stacks 0EQ6 constructed in `AlgebraicGeometry.Space.chowGroup`.

```lean
theorem firstChernClassCap_comm_iff_isRationallyEquivalentToZero
    (hL : IsInvertibleSheaf D sX hX L) (hN : IsInvertibleSheaf D sX hX N)
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L)
    (t : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 N)
    (ratioL : LocalRatioFamily.{u, u} D.site D.base D.base_mem hX.1 hdec L)
    (ratioN : LocalRatioFamily.{u, u} D.site D.base D.base_mem hX.1 hdec N)
    (hfinL : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdec L s ratioL W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hfinN : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdec N t ratioN W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (dim : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, dim x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hk : k + 1 = n - 1)
    (hZinj : Function.Injective Z)
    (hZfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X (Z i).subspace)
    (hdim : ∀ i, deltaDimension D sX
      ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) = k + 1)
    (hcoverL : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdec L s ratioL W ≠ 0 →
        ∃ i, Z i = W)
    (hcoverN : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdec N t ratioN W ≠ 0 →
        ∃ i, Z i = W) :
    firstChernClassCap D sX hX N k hN chernN (chowTarget.{v} D sX hX k)
          (divisorCycleAt.{u, u} D sX hX hdec L s ratioL hfinL hint dim hd hn hk) =
        firstChernClassCap D sX hX L k hL chernL (chowTarget.{v} D sX hX k)
          (divisorCycleAt.{u, u} D sX hX hdec N t ratioN hfinN hint dim hd hn hk) ↔
      IsRationallyEquivalentToZero.{v} D sX hX k
        (cycleFamilySum D sX hX
          (fun i => (Z i).toIntegralClosedSubspace D.site D.base D.base_mem) hZfin k
          (keyFormulaDivisorTerm.{u, u} D sX hX hdec L N chernL chernN Z s t ratioL ratioN
            hdim))
```

**`AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean#L137). The attribute's comment: “Lemma 82.21.1 itself: for X good and integral with δ-dimension n, L and N invertible and s, t nonzero meromorphic sections, c\_1(N) ∩ div\_L(s) = c\_1(L) ∩ div\_N(t) in CH\_\{n-2}(X). Unconditional at the source's hypotheses: integrality and goodness are the section variables, regularity of s and t is derived from s ≠ 0, t ≠ 0 rather than assumed, and the cap product of 0EQJ, the divisors of 0EQE and the Chow group of 0EQ6 are the constructed ones, not carried”.

> **Section 0EQU, the key formula: `c₁(𝒩) ∩ div_ℒ(s) = c₁(ℒ) ∩ div_𝒩(t)` in `CH_{n-2}(X)`.**
> In Situation 0EDT let `X/B` be good, `X` integral with `dim_δ(X) = n`, let `ℒ` and `𝒩` be
> invertible `𝒪_X`-modules, and let `s`, `t` be nonzero meromorphic sections of `ℒ`, `𝒩`.  Then
> `c₁(𝒩) ∩ div_ℒ(s) = c₁(ℒ) ∩ div_𝒩(t)` in the Chow group `CH_{n-2}(X)` of Stacks 0EQ6, the cap
> products being those of Stacks 0EQJ and the divisors those of Stacks 0EQE, all at the canonical
> choices.
>
> The proof is the section's: the family `{Z_i}` of prime divisors where `s` or `t` fails to
> generate is locally finite (Stacks 0EPS), the two cap products are the sums over it of
> `ord_{B_i}(f_i) (Z_i → X)_* div(t_i|_{Z_i})` and `ord_{B_i}(g_i) (Z_i → X)_* div(s_i|_{Z_i})`, and
> the key formula (Stacks 0EQV) makes their difference a locally finite sum of principal divisors of
> tame symbols on the `Z_i`.

```lean
theorem canonicalFirstChernCap_divisor_comm
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L) (hs : s ≠ 0)
    (t : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 N) (ht : t ≠ 0)
    {n : ℤ} (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    canonicalFirstChernCap.{u, u + 1} D sX hX N hN (n - 2)
        (canonicalDivisorCycleAt D sX hX hint L hL s
          (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint L hL hs)
          (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn)) =
      canonicalFirstChernCap.{u, u + 1} D sX hX L hL (n - 2)
        (canonicalDivisorCycleAt D sX hX hint N hN t
          (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint N hN ht)
          (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn))
```

## Tag 0EQY, a lemma

[Tag 0EQY](https://stacks.math.columbia.edu/tag/0EQY) in the Stacks Project.

**`AlgebraicGeometry.Space.isRationallyEquivalentToZeroCanonical_firstChernCapCycleMap_canonicalFirstChernRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean#L567). The attribute's comment: “the cap product with the first Chern class is compatible with rational equivalence, at the level of cycles: it carries a cycle rationally equivalent to zero to a cycle rationally equivalent to zero, both read at the canonical embeddings of Stacks 0ENK”.

> **Stacks 0EQY at the level of cycles.**  For `X/B` good and `𝒩` an invertible `𝒪_X`-module,
> the cap product `c₁(𝒩) ∩ - : Z_{k+1}(X) ⟶ Z_k(X)` of Stacks 0EQJ carries a `(k+1)`-cycle
> rationally equivalent to zero to a `k`-cycle rationally equivalent to zero, both in the sense of
> part (2) of Stacks 0EQ6 read at the canonical embeddings `R(W) → Q(𝒪^h_{W,ξ})` of Stacks 0ENK.
>
> Nothing is assumed.  The reassembly over the presenting family of the rational equivalence is
> `isRationallyEquivalentToZeroCanonical_firstChernCapCycleMap_of_pushforwardDivisor`, and the
> summand statement it asks for is the previous theorem.

```lean
theorem isRationallyEquivalentToZeroCanonical_firstChernCapCycleMap_canonicalFirstChernRule
    {α : CycleGroup D sX (k + 1)}
    (hα : IsRationallyEquivalentToZeroCanonical.{u + 1} D sX hX (k + 1) α) :
    IsRationallyEquivalentToZeroCanonical.{u + 1} D sX hX k
      (firstChernCapCycleMap D sX hX k (canonicalFirstChernRule D sX hX N hN k) α)
```

**`AlgebraicGeometry.Space.canonicalFirstChernCapCanonicalChowMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean, line 589](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean#L589). The attribute's comment: “the descended operation CH\_\{k+1}(X) -> CH\_k(X), the Chow groups being those of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK on both sides”.

> **Stacks 0EQY.**  The cap product of Stacks 0EQJ descends to
>
> `c₁(𝒩) ∩ - : CH_{k+1}(X) ⟶ CH_k(X)`,
>
> with `CH_*(X)` the Chow group `AlgebraicGeometry.Space.chowGroupCanonical` of Stacks 0EQ6 at the
> canonical embeddings of Stacks 0ENK on both sides.
>
> The descent is `AlgebraicGeometry.Space.chowGroupCanonicalLift` and the hypothesis it needs is
> the previous theorem.

```lean
def canonicalFirstChernCapCanonicalChowMap :
    chowGroupCanonical.{u + 1} D sX hX (k + 1) →+ chowGroupCanonical.{u + 1} D sX hX k
```

**`AlgebraicGeometry.Space.canonicalFirstChernCapCanonicalChowMap_chowClassCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernCapRationalEquivalenceCanonicalSummand.lean#L601). The attribute's comment: “the descended operation agrees with the cap product of Stacks 0EQJ on the class of a cycle, which is the factorization through rational equivalence”.

> **Stacks 0EQY.**  The descended operation agrees with the cap product of Stacks 0EQJ on the
> class of a cycle, which is what it means for the cap product to factor through rational
> equivalence.

```lean
theorem canonicalFirstChernCapCanonicalChowMap_chowClassCanonical
    (α : CycleGroup D sX (k + 1)) :
    canonicalFirstChernCapCanonicalChowMap D sX hX k N hN
        (chowClassCanonical.{u + 1} D sX hX (k + 1) α) =
      canonicalFirstChernCapCanonical.{u + 1} D sX hX N hN k α
```

## Tag 0EQZ, a lemma

[Tag 0EQZ](https://stacks.math.columbia.edu/tag/0EQZ) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_firstChernCapCycleMap_firstChernCapCycleMap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IteratedFirstChernCapCommutativity.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IteratedFirstChernCapCommutativity.lean#L766). The attribute's comment: “c₁(ℒ) ∩ c₁(𝒩) ∩ α = c₁(𝒩) ∩ c₁(ℒ) ∩ α in CH\_k(X), for every (k+2)-cycle α on X representing a class of CH\_\{k+2}(X); both cap products are the cycle-level operations of Stacks 0EQJ at the canonical choices, the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical); nothing carried”.

> **Stacks 0EQZ: the two iterated cap products with first Chern classes commute.** In
> Situation 0EDT let `X/B` be good and let `ℒ`, `𝒩` be invertible `𝒪_X`-modules. For every
> `(k + 2)`-cycle `α` on `X`,
>
> `c₁(ℒ) ∩ c₁(𝒩) ∩ α = c₁(𝒩) ∩ c₁(ℒ) ∩ α` in `CH_k(X)`.
>
> The cap products are those of Stacks 0EQJ at the canonical choices
> (`AlgebraicGeometry.Space.canonicalFirstChernRule`): the inner one is the cycle-level operation
> `Z_{k+2}(X) → Z_{k+1}(X)` defining `c₁(-) ∩ -` on representatives, and so is the outer one
> `Z_{k+1}(X) → Z_k(X)`, the class being taken afterwards in the Chow group `CH_k(X)` of
> Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`, whose rational equivalences are sums of
> principal divisors at the canonical embeddings of Stacks 0ENK. As every class of `CH_{k+2}(X)` is
> the class of a cycle, this is the identity of the source on representatives.

```lean
theorem chowClassCanonical_firstChernCapCycleMap_firstChernCapCycleMap_comm (k : ℤ)
    (α : CycleGroup D sX (k + 1 + 1)) :
    chowClassCanonical.{max (u + 1) v} D sX hX k
        (firstChernCapCycleMap D sX hX k (canonicalFirstChernRule D sX hX L hL k)
          (firstChernCapCycleMap D sX hX (k + 1) (canonicalFirstChernRule D sX hX N hN (k + 1))
            α)) =
      chowClassCanonical.{max (u + 1) v} D sX hX k
        (firstChernCapCycleMap D sX hX k (canonicalFirstChernRule D sX hX N hN k)
          (firstChernCapCycleMap D sX hX (k + 1) (canonicalFirstChernRule D sX hX L hL (k + 1))
            α))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.21, Tag 0EQW](https://stacks.math.columbia.edu/tag/0EQW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
