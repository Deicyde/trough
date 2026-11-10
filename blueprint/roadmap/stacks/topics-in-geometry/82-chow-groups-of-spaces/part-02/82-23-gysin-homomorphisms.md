---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_canonicalDivisorCycleAt, AlgebraicGeometry.Space.exists_sectionGysinChowGroupMap, AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_firstChernCapCycleMap, AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_gysinCycleMap_comm
statement: formalized
proof: formalized
---

# 82.23 Gysin homomorphisms

Section 82.23 of the Stacks Project, [Tag 0ER8](https://stacks.math.columbia.edu/tag/0ER8). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ER9, a lemma

[Tag 0ER9](https://stacks.math.columbia.edu/tag/0ER9) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_canonicalDivisorCycleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinDivisorKeyFormula.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinDivisorKeyFormula.lean#L457). The attribute's comment: “i^*div\_N(t) = c\_1(N) ∩ [D]\_\{n-1} in CH\_\{n-2}(D), at the hypotheses of 0ER9 itself: X good and integral of δ-dimension n, i : D → X the effective Cartier divisor presented by an invertible L with a nonzero global section σ (so D = Z(σ), as in the proof's own 'Set L = O\_X(D)'), N invertible and t a nonzero meromorphic section of N. The Gysin map is 0ER1's, the cap product 0EQJ's formed on D, [D]\_\{n-1} is 0EE9's and div\_N(t) is 0EQE's at the canonical ratios of 0EPR; CH\_\{n-2}(D) is chowGroupCanonical, the quotient by the rational equivalences of 0EQ6 read at the canonical 0ENK embeddings. Unconditional: the family \{Z\_i} is constructed by 0EPS, the choice s\_i = σ off D by 0845, and the rational equivalence is the key formula 0EQV carried inside |D| and descended along i”.

> **Stacks 0ER9 (Lemma 82.23.1).**  In Situation 0EDT let `X/B` be good, `X` integral with
> `n = dim_δ(X) = k + 2`, let `ℒ` be an invertible `𝒪_X`-module with a nonzero global section `σ`
> and let `i : D = Z(σ) → X` be the closed immersion of its vanishing locus (Stacks 0845) — the
> effective Cartier divisor of the source, presented by the pair `(𝒪_X(D), s)` the source
> immediately passes to.  Let `𝒩` be an invertible `𝒪_X`-module and let `t` be a nonzero
> meromorphic section of `𝒩`.  Then
>
> `i^*div_𝒩(t) = c₁(𝒩) ∩ [D]_{n-1}`  in  `CH_{n-2}(D)`,
>
> the Chow group being `AlgebraicGeometry.Space.chowGroupCanonical`, which is the source's
> `CH_{n-2}(D)`: the embeddings `R(W) → Q(𝒪^h_{W,ξ})` of Stacks 0ENK presenting the rational
> equivalences are the canonical ones.
>
> The refined Gysin map is the one of Stacks 0ER1, `AlgebraicGeometry.Space.gysinCycleMap` at the
> component rule `AlgebraicGeometry.Space.canonicalGysinComponentRule`, whose free clause (1)(b) is
> here the generator rule of the source's own choice `s_i = σ` off `D`; the cap product is the one
> of Stacks 0EQJ formed on `D` at the generator rule of an arbitrary family of generators `t_W` of
> the `𝒩_{ξ_W}`, which is the choice Section 0EQU leaves free; `[D]_{n-1}` is the cycle of
> Stacks 0EE9; and `div_𝒩(t)` is the Weil divisor of Stacks 0EQE at the canonical ratios of
> Stacks 0EPR.  Regularity of `t` is derived from `t ≠ 0` rather than assumed.

```lean
theorem chowClassCanonical_gysinCycleMap_canonicalDivisorCycleAt
    (t : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 N) (ht : t ≠ 0)
    (w : GenericUnitFamily D sX hX) :
    chowClassCanonical.{u + 1} D ((vanishingLocus D sX hX L σ).1.ι ≫ sX)
        (isGood_vanishingLocus D sX hX L σ) k
        (gysinCycleMap D sX (vanishingLocus D sX hX L σ) (isGood_vanishingLocus D sX hX L σ) k
          (canonicalGysinComponentRule D sX hX (vanishingLocus D sX hX L σ)
            (isGood_vanishingLocus D sX hX L σ) k
            (generatorChernRule D sX hX hint L hL hn (sectionGeneratorUnit D sX hX hint L hL σ)))
          (canonicalDivisorCycleAt D sX hX hint N hN t
            (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint N hN ht) hn)) =
      chowClassCanonical.{u + 1} D ((vanishingLocus D sX hX L σ).1.ι ≫ sX)
        (isGood_vanishingLocus D sX hX L σ) k
        (firstChernCapCycleMap D ((vanishingLocus D sX hX L σ).1.ι ≫ sX)
          (isGood_vanishingLocus D sX hX L σ) k
          (closedSubspaceChernRule D sX hX (vanishingLocus D sX hX L σ).1
            (vanishingLocus D sX hX L σ).2 k (generatorChernRule D sX hX hint N hN hn w))
          (vanishingLocusTopCycleAt D sX hX hint L hL hσ hn))
```

## Tag 0ERA, a lemma

[Tag 0ERA](https://stacks.math.columbia.edu/tag/0ERA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_sectionGysinChowGroupMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinChowGroupMapOfSection.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinChowGroupMapOfSection.lean#L255). The attribute's comment: “i^* : CH\_\{k+1}(X) → CH\_k(D) for X/B good and (L, s, i : D → X) as in 0ER1 (L invertible, s a global section, D = Z(s)): the Gysin cycle map of 0ER1 at its own constructed rule sectionGysinRule descends through the Chow groups chowGroupCanonical of 0EQ6 (div(f\_j) at the canonical 0ENK embeddings). Unconditional: the member cases are 0EQY on V ⊆ D and the key formula 0EQV (the content of 0ER9 at N = O\_V) on V ⊄ D, both carried inside D; 0ER5 and 0EQC are replaced by the carrier-respecting reassembly”.

> **Stacks 0ERA.**  In Situation 0EDT let `X/B` be good and let `(ℒ, σ, i : E → X)` be as in
> Definition 0ER1: `ℒ` an invertible `𝒪_X`-module, `σ ∈ Γ(X, ℒ)` and `i : E = Z(σ) → X` the closed
> immersion of its vanishing locus.  The Gysin homomorphism `i^* : Z_{k+1}(X) → CH_k(E)` of
> Definition 0ER1 factors through rational equivalence: there is a homomorphism
>
> `i^* : CH_{k+1}(X) ⟶ CH_k(E)`
>
> sending the class of every `(k+1)`-cycle `α` to `i^*α`, i.e. to the class of the cycle
> `∑ n_W i^*[W]` of Stacks 0ER1(2).
>
> The Gysin map on cycles is `AlgebraicGeometry.Space.gysinCycleMap` at
> `AlgebraicGeometry.Space.sectionGysinRule`, the component rule of Stacks 0ER1(1) with every
> ingredient constructed, which is the rule of `AlgebraicGeometry.Space.sectionRefinedGysin`; the
> Chow groups are `AlgebraicGeometry.Space.chowGroupCanonical`, Stacks 0EQ6 with `div(f_j)` read at
> the canonical embeddings of Stacks 0ENK.  The map is
> `AlgebraicGeometry.Space.sectionGysinChowGroupMap`; nothing is assumed.

```lean
theorem exists_sectionGysinChowGroupMap :
    ∃ F : chowGroupCanonical.{u + 1} D p hp (k + 1) →+
        chowGroupCanonical.{u + 1} D ((vanishingLocus D p hp L σ).1.ι ≫ p)
          (isGood_vanishingLocus D p hp L σ) k,
      ∀ α : CycleGroup D p (k + 1),
        F (chowClassCanonical.{u + 1} D p hp (k + 1) α) =
          chowClassCanonical.{u + 1} D ((vanishingLocus D p hp L σ).1.ι ≫ p)
            (isGood_vanishingLocus D p hp L σ) k
            (gysinCycleMap D p (vanishingLocus D p hp L σ) (isGood_vanishingLocus D p hp L σ) k
              (sectionGysinRule D p hp L σ k hL) α)
```

## Tag 0ERB, a lemma

[Tag 0ERB](https://stacks.math.columbia.edu/tag/0ERB) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_firstChernCapCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinFirstChernCap.lean, line 1319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinFirstChernCap.lean#L1319). The attribute's comment: “i^*(c₁(N) ∩ α) = c₁(i^*N) ∩ i^*α in CH\_k(E), for every (k+2)-cycle α on X representing a class of CH\_\{k+2}(X); i^* is the refined Gysin map of Stacks 0ER1 on cycles (gysinCycleMap at sectionGysinRule), both cap products the cycle-level operations of Stacks 0EQJ at the canonical choices, the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical); nothing carried”.

> **Stacks 0ERB.** In Situation 0EDT let `X/B` be good, let `(ℒ, s, i : E → X)` be a triple as
> in Stacks 0ER1 and let `𝒩` be an invertible `𝒪_X`-module. For every `(k+2)`-cycle `α` on `X`,
>
> `i^*(c₁(𝒩) ∩ α) = c₁(i^*𝒩) ∩ i^*α` in `CH_k(E)`.
>
> Here `i^*` is the refined Gysin map of Stacks 0ER1 on cycles,
> `AlgebraicGeometry.Space.gysinCycleMap` at the rule `AlgebraicGeometry.Space.sectionGysinRule`;
> both cap products are the cycle-level operations of Stacks 0EQJ at the canonical choices,
> `AlgebraicGeometry.Space.firstChernCapCycleMap` at
> `AlgebraicGeometry.Space.canonicalFirstChernRule`; and the classes are taken in `CH_k(E)` of
> Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`, whose rational equivalences are sums of
> principal divisors at the canonical embeddings of Stacks 0ENK. As every class of `CH_{k+2}(X)` is
> the class of a cycle, this is the identity of the source on representatives.
>
> The two composites are cycle maps of kernels, and on each `[W]` their difference is a sum of
> canonical principal divisors lying over `|W|`
> (`isRationallyEquivalentToZeroWithin_gysinCycleMap_firstChernComponentCycle_sub`); the general
> case is Stacks 0EQ8 (`AlgebraicGeometry.Space.isCycleFamilySumWithin_sub_of_isCycleMapOfKernel`).

```lean
theorem chowClassCanonical_gysinCycleMap_firstChernCapCycleMap (k : ℤ)
    (α : CycleGroup D sX (k + 1 + 1)) :
    chowClassCanonical.{max (u + 1) v} D ((vanishingLocus D sX hX L s).1.ι ≫ sX)
        (isGood_vanishingLocus D sX hX L s) k
        (gysinCycleMap D sX (vanishingLocus D sX hX L s) (isGood_vanishingLocus D sX hX L s) k
          (sectionGysinRule D sX hX L s k hL)
          (firstChernCapCycleMap D sX hX (k + 1) (canonicalFirstChernRule D sX hX N hN (k + 1))
            α)) =
      chowClassCanonical.{max (u + 1) v} D ((vanishingLocus D sX hX L s).1.ι ≫ sX)
        (isGood_vanishingLocus D sX hX L s) k
        (firstChernCapCycleMap D ((vanishingLocus D sX hX L s).1.ι ≫ sX)
          (isGood_vanishingLocus D sX hX L s) k
          (canonicalFirstChernRule D _ (isGood_vanishingLocus D sX hX L s)
            ((modulePullback D.site D.base D.base_mem (vanishingLocusInclusion D sX hX L s)).obj N)
            (modulePullbackInvertible (vanishingLocusInclusion D sX hX L s) N hN) k)
          (gysinCycleMap D sX (vanishingLocus D sX hX L s) (isGood_vanishingLocus D sX hX L s)
            (k + 1) (sectionGysinRule D sX hX L s (k + 1) hL) α))
```

## Tag 0ERC, a lemma

[Tag 0ERC](https://stacks.math.columbia.edu/tag/0ERC) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_gysinCycleMap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinCommutativity.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinCommutativity.lean#L536). The attribute's comment: “j^* i^* α = (j')^* (i')^* α in CH\_k(D ∩ D') for every (k+2)-cycle α on X representing a class of CH\_\{k+2}(X), all four maps the refined Gysin maps of Stacks 0ER1 on cycles at the canonical component cycles, D ∩ D' being Z(s'|\_D) identified with Z(s|\_\{D'}), the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical); nothing carried”.

> **Stacks 0ERC: the two refined Gysin maps of a pair of sections commute.** In Situation 0EDT
> let `X/B` be good and let `(ℒ, s, i : E → X)`, `(ℒ', s', i' : E' → X)` be two triples as in
> Stacks 0ER1. Let `j : Z(s'|_E) → E` and `j' : Z(s|_{E'}) → E'` be the closed immersions of the
> triples `(ℒ'|_E, s'|_E)` on `E` and `(ℒ|_{E'}, s|_{E'})` on `E'`, both vanishing loci being
> `E ∩ E'` (`AlgebraicGeometry.Space.vanishingLocusIntersectionComparison`). For every
> `(k + 2)`-cycle `α` on `X`,
>
> `j^* (i^* α) = (j')^* ((i')^* α)` in `CH_k(E ∩ E')`.
>
> All four Gysin maps are the cycle-level maps of Stacks 0ER1, parts (1) and (2), at the canonical
> component cycles (`AlgebraicGeometry.Space.gysinCycleMap` at
> `AlgebraicGeometry.Space.sectionGysinRule`); the left side is carried to `Z(s|_{E'})` by the
> identification of the two vanishing loci, and the classes are taken in the Chow group of
> Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`, whose rational equivalences are sums of
> principal divisors at the canonical embeddings of Stacks 0ENK. As every class of `CH_{k+2}(X)` is
> the class of a cycle, this is the identity of the source on representatives.
>
> The proof is the source's: the case `α = [W]` is the key formula on `W`
> (`isRationallyEquivalentToZeroWithin_comparisonPushforward_gysinCycleMap_sub_integralCycle`),
> a sum of canonical principal divisors lying over `|W|`, and the general case follows by
> Stacks 0EQ8 (`AlgebraicGeometry.Space.isCycleFamilySumWithin_closedPushforward_gysin_gysin_sub`).

```lean
theorem chowClassCanonical_gysinCycleMap_gysinCycleMap_comm (k : ℤ)
    (α : CycleGroup D p (k + 1 + 1)) :
    chowClassCanonical.{max (u + 1) v} D
        ((closedSubspaceVanishingLocus D p hp L s (vanishingLocus D p hp L' s')).1.ι ≫
          (vanishingLocus D p hp L' s').1.ι ≫ p)
        (isGood_vanishingLocus D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L' s')) _ _)
        k
        (comparisonPushforward D p (vanishingLocus D p hp L s) (vanishingLocus D p hp L' s') k
          (closedSubspaceVanishingLocus D p hp L' s' (vanishingLocus D p hp L s))
          (closedSubspaceVanishingLocus D p hp L s (vanishingLocus D p hp L' s'))
          (isGood_vanishingLocus D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L s)) _ _)
          (isGood_vanishingLocus D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L' s'))
            _ _)
          (isClosedImmersion_vanishingLocusIntersectionComparison D p hp s s' hL hL')
          (vanishingLocusIntersectionComparison_comp_ι D p hp s s' hL hL')
          (gysinCycleMap D _ (closedSubspaceVanishingLocus D p hp L' s' (vanishingLocus D p hp L s))
            (isGood_vanishingLocus D _
              (isGood_closedSubspace D p hp (vanishingLocus D p hp L s)) _ _)
            k (sectionGysinRule D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L s)) _
              (closedSubspaceModuleRestrictSection D p hp L' s' (vanishingLocus D p hp L s)) k
              (isInvertibleSheaf_closedSubspaceModuleRestrict D p hp (vanishingLocus D p hp L s)
                hL'))
            (gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s)
              (k + 1) (sectionGysinRule D p hp L s (k + 1) hL) α))) =
      chowClassCanonical.{max (u + 1) v} D
        ((closedSubspaceVanishingLocus D p hp L s (vanishingLocus D p hp L' s')).1.ι ≫
          (vanishingLocus D p hp L' s').1.ι ≫ p)
        (isGood_vanishingLocus D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L' s')) _ _)
        k
        (gysinCycleMap D _ (closedSubspaceVanishingLocus D p hp L s (vanishingLocus D p hp L' s'))
          (isGood_vanishingLocus D _
            (isGood_closedSubspace D p hp (vanishingLocus D p hp L' s')) _ _)
          k (sectionGysinRule D _ (isGood_closedSubspace D p hp (vanishingLocus D p hp L' s')) _
            (closedSubspaceModuleRestrictSection D p hp L s (vanishingLocus D p hp L' s')) k
            (isInvertibleSheaf_closedSubspaceModuleRestrict D p hp (vanishingLocus D p hp L' s')
              hL))
          (gysinCycleMap D p (vanishingLocus D p hp L' s') (isGood_vanishingLocus D p hp L' s')
            (k + 1) (sectionGysinRule D p hp L' s' (k + 1) hL') α))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.23, Tag 0ER8](https://stacks.math.columbia.edu/tag/0ER8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
