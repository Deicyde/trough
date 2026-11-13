---
declaration: section
origin: cited
lean: Stacks.Chow.existsUnique_isChernClassFundamentalFamilyOfRank, Stacks.Chow.chernClassFundamentalOfRank, Stacks.Chow.totalChernClassFundamentalOfRank, ProjectiveBundleChernRelation, Stacks.Chow.chernClassCapFundamental_one_eq_firstChernClassCapFundamental, Stacks.Chow.chernClassFundamentalOfRank_one_eq_firstChernClassCapFundamental
statement: formalized
proof: formalized
---

# 42.37 The Chern classes of a vector bundle

Section 42.37 of the Stacks Project, [Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02U0, a definition

[Tag 02U0](https://stacks.math.columbia.edu/tag/02U0) in the Stacks Project.

**`Stacks.Chow.existsUnique_isChernClassFundamentalFamilyOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean#L189). The attribute's comment: “part (1)”.

> **Stacks 02U0, part (1).** For a module `ℰ` of rank `r` on `X` and an integer `n`, there are
> classes `c_i ∈ A_{n-i}(X)`, `0 ≤ i ≤ r`, with `c_0 = [X]` and
> `∑_{i=0}^{r} (-1)^i c₁(𝒪_{𝐏(ℰ)}(1))^i ∩ π^*c_{r-i} = 0`, and exactly one such family. Here
> `[X] = [X]_n` is the fundamental cycle of Stacks 02QU; the source takes `X` integral and
> `n = dim_δ(X)`, which is not needed.

```lean
theorem existsUnique_isChernClassFundamentalFamilyOfRank (n : ℤ) :
    ∃! c : ∀ i : Fin (r + 1), chowGroup C sX (n - (i : ℤ)),
      IsChernCapFamilyOfRank E r C sX n
        (QuotientAddGroup.mk' (rationalEquivalences C sX n)
          (cycleAssociatedToClosedSubscheme C sX (𝟙 X) n)) c
```

**`Stacks.Chow.chernClassFundamentalOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean#L199). The attribute's comment: “part (2)”.

> **Stacks 02U0, part (2).** The `i`-th Chern class of a module `ℰ` of rank `r` on `X`,
> `c_i(ℰ) ∩ [X] = c_i ∈ A_{n-i}(X)`: the `i`-th member of the family of part (1).

```lean
def chernClassFundamentalOfRank (n : ℤ) (i : Fin (r + 1)) : chowGroup C sX (n - (i : ℤ))
```

**`Stacks.Chow.totalChernClassFundamentalOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassesOfRank.lean#L221). The attribute's comment: “part (3)”.

> **Stacks 02U0, part (3).** The total Chern class of a module of rank `r` on `X`,
> `c(ℰ) ∩ [X] = c_0(ℰ) ∩ [X] + … + c_r(ℰ) ∩ [X]` in `A_*(X) = ⊕_k A_k(X)`.

```lean
def totalChernClassFundamentalOfRank (n : ℤ) : ⨁ k : ℤ, chowGroup C sX k
```

## Tag 02U1, an equation

[Tag 02U1](https://stacks.math.columbia.edu/tag/02U1) in the Stacks Project.

Declarations registered for the tag:

- [`ProjectiveBundleChernRelation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ProjectiveBundleChernRelation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean#L294) (StacksFrontier): “Equation 42.37.1.1, the displayed relation of clause (1) of Definition 02U0: `∑_{i=0}^{r} (-1)^i c₁(O_P(1))^i ∩ π^*c_{r-i} = 0`, the condition on a family of Chow classes that Definition 02U0 solves to define the Chern classes of a rank-`r` finite locally free module. The tag labels the displayed equation, which is this condition, so it is carried by the definition naming it; `Stacks.Chow.IsChernCapFamily` conjoins it with `c₀ = α`.”.

## Tag 02U2, a lemma

[Tag 02U2](https://stacks.math.columbia.edu/tag/02U2) in the Stacks Project.

**`Stacks.Chow.chernClassCapFundamental_one_eq_firstChernClassCapFundamental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDivisorClass.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDivisorClass.lean#L314). The attribute's comment: “the projective bundle of the rank-one module L is the pair (X, 𝟙 X) and its twist O\_P(1) is L itself, so the twist operator is CONSTRUCTED from L rather than assumed. The family of clause (1) of Stacks 02U0 is quantified over as a datum, its existence needing the surjectivity half of Stacks 02TX; it is not an assumption about the classes compared”.

> **Stacks 02U2.** Let `(S, δ)` be the base situation of chapter 42, let `X` be locally of
> finite type over `S`, integral and of delta-dimension `n`, and let `L` be an invertible
> `𝒪_X`-module. Then the first Chern class of `L` in the sense of Stacks 02U0 — the member `c_1` of
> the family of clause (1), read on the projective bundle of `L`, which is `X` itself with
> projection `𝟙 X` and twist `L` — equals the Weil divisor class of `L` of Stacks 02SJ (2).
>
> The proof is the source's. At `r = 1` the relation 02U1 reads
> `c₁(L) ∩ π^*c_0 = π^*c_1` on the bundle; the bundle is `X` and `π` is the identity, so its flat
> pullback is the identity (`Stacks.Chow.flatPullbackChow_id`) and the relation says
> `c_1 = c₁(L) ∩ c_0`. The normalisation `c_0 = [X]` turns the right-hand side into the cap product
> of Stacks 02SO on the fundamental cycle, which is the Weil divisor class by
> `Stacks.Chow.firstChernClassCapOfInvertible_fundamentalCycle_eq_firstChernClassCapFundamental`.
>
> The twist operator is `Stacks.Chow.invertibleChernCapOperator` of `L`, the source's
> `O_{𝐏(L)}(1) = L`, built from Stacks 02TI for `L`
> (`Stacks.Chow.firstChernClassCap_factors`); the family `D` of clause (1)
> of Stacks 02U0 is a datum, quantified over rather than chosen. It is not an assumption
> about the two classes being compared.

```lean
theorem chernClassCapFundamental_one_eq_firstChernClassCapFundamental
    (D : ChernClassFundamentalFamily C p p (𝟙 X) (Category.id_comp p) 1
      (relativeDimension_identity X) (flatPullbackFactorsThroughRationalEquivalence_id C p)
      (invertibleChernCapOperator C p L (firstChernClassCap_factors C p L)) n) :
    chernClassCapFundamental C p p (𝟙 X) (Category.id_comp p) 1
        (relativeDimension_identity X) (flatPullbackFactorsThroughRationalEquivalence_id C p)
        (invertibleChernCapOperator C p L (firstChernClassCap_factors C p L)) n D ⟨1, by omega⟩ =
      firstChernClassCapFundamental C p n hn L
```

**`Stacks.Chow.chernClassFundamentalOfRank_one_eq_firstChernClassCapFundamental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassRankOne.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/ChernClassRankOne.lean#L58).

> **Stacks 02U2.** Let `X` be locally of finite type over the base of a Chow situation, integral
> of delta-dimension `n`, and let `ℒ` be an invertible `𝒪_X`-module, so of rank one. The first Chern
> class `c_1(ℒ) ∩ [X] ∈ A_{n-1}(X)` of Stacks 02U0, defined by the relation
> `c₁(𝒪_{𝐏(ℒ)}(1)) ∩ π^*c_0 = π^*c_1` with `c_0 = [X]` on the projective bundle of `ℒ`, is the
> Weil divisor class `c₁(ℒ) ∩ [X]` of Stacks 02SJ.

```lean
theorem chernClassFundamentalOfRank_one_eq_firstChernClassCapFundamental :
    letI := Stacks.ModuleDescent.isFiniteLocallyFreeOfRank_one_of_isInvertible X L inferInstance
    chowGroupCast C p (show n - ((1 : Fin (1 + 1)) : ℤ) = n - 1 by simp)
        (chernClassFundamentalOfRank L 1 C p n 1) =
      firstChernClassCapFundamental C p n hn L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.37, Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
