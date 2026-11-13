---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.cycleFamilySumCoeff_mem_cyclesOfDimension, AlgebraicGeometry.Space.cycleFamilySum, AlgebraicGeometry.Space.IsRationallyEquivalentToZero, AlgebraicGeometry.Space.rationalEquivalences, AlgebraicGeometry.Space.RationallyEquivalent, AlgebraicGeometry.Space.rationallyEquivalent_equivalence, AlgebraicGeometry.Space.chowGroup, AlgebraicGeometry.Space.chowClass
statement: formalized
proof: formalized
---

# 82.15 Rational equivalence

Section 82.15 of the Stacks Project, [Tag 0EQ5](https://stacks.math.columbia.edu/tag/0EQ5). 3 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EQ6, a definition

[Tag 0EQ6](https://stacks.math.columbia.edu/tag/0EQ6) in the Stacks Project.

**`AlgebraicGeometry.Space.cycleFamilySumCoeff_mem_cyclesOfDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceFamilySums.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceFamilySums.lean#L185). The attribute's comment: “part (1)”.

> **Stacks 0EQ6, part (1).** The coefficientwise sum `∑ (i_j)_* c_j` of the pushforwards of a
> family of `k`-cycles along the inclusions of a locally finite collection of integral closed
> subspaces is a `k`-cycle on `X`.
>
> Local finiteness of the collection gives local finiteness of the support: a neighbourhood of a
> point meeting only finitely many of the `|W_j|` is shrunk, using the pushforwards from those
> finitely many, to one meeting only finitely many point sets of subspaces with a nonzero
> coefficient. The δ-dimension of each such subspace is `k` because that holds for the summand
> it comes from.

```lean
theorem cycleFamilySumCoeff_mem_cyclesOfDimension (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (W : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hWfin : LocallyFinite fun j : J =>
      subspacePointSet D.site D.base D.base_mem X (W j).subspace)
    (k : ℤ) (c : ∀ j, CycleGroup D ((W j).subspace.ι ≫ sX) k) :
    cycleFamilySumCoeff D sX hX W k c ∈ cyclesOfDimension D sX k
```

**`AlgebraicGeometry.Space.cycleFamilySum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceFamilySums.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceFamilySums.lean#L221). The attribute's comment: “part (1)”.

> **Stacks 0EQ6, part (1).** The element `∑ (i_j)_* c_j` of `Z_k(X)` determined by a locally
> finite collection `{W_j ⊆ X}` of integral closed subspaces and a family of `k`-cycles `c_j` on
> them; taking `c_j = div(f_j)` for `f_j ∈ R(W_j)^*` on subspaces of δ-dimension `k + 1` gives
> the cycle of the source.

```lean
def cycleFamilySum (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (W : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hWfin : LocallyFinite fun j : J =>
      subspacePointSet D.site D.base D.base_mem X (W j).subspace)
    (k : ℤ) (c : ∀ j, CycleGroup D ((W j).subspace.ι ≫ sX) k) : CycleGroup D sX k
```

**`AlgebraicGeometry.Space.IsRationallyEquivalentToZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L261). The attribute's comment: “part (2): rationally equivalent to zero. The sum is part (1), AlgebraicGeometry.Space.cycleFamilySum; the index type ranges over the universe v”.

> **Stacks 0EQ6, part (2).** A `k`-cycle on a good algebraic space `X/B` is *rationally
> equivalent to zero* when it is the cycle `∑ (i_j)_* div(f_j)` of part (1): there is a locally
> finite family `{W_j ⊆ X}` of integral closed subspaces with `dim_δ(W_j) = k + 1`, and on each a
> principal divisor `div(f_j)`, `f_j ∈ R(W_j)^*`, whose pushforwards sum to the cycle.
>
> The sum is `AlgebraicGeometry.Space.cycleFamilySum`, which is part (1) of the source.

```lean
def IsRationallyEquivalentToZero (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    (α : CycleGroup D sX k) : Prop
```

**`AlgebraicGeometry.Space.rationalEquivalences`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L336). The attribute's comment: “part (2): the cycles rationally equivalent to zero, as a subgroup of Z\_k(X); the carrier is exactly the set of sums of part (1)”.

> **Stacks 0EQ6, part (2).** The subgroup of `k`-cycles rationally equivalent to zero. Its
> carrier is exactly the set of cycles of the form `∑ (i_j)_* div(f_j)` of part (1); that this set
> is a subgroup is the content of the three closure proofs.

```lean
def rationalEquivalences (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    AddSubgroup (CycleGroup D sX k)
```

**`AlgebraicGeometry.Space.RationallyEquivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L354). The attribute's comment: “part (3): α ∼\_rat β, defined as α - β being rationally equivalent to zero”.

> **Stacks 0EQ6, part (3).** Two `k`-cycles are *rationally equivalent* when their difference
> is rationally equivalent to zero.

```lean
def RationallyEquivalent (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    (α β : CycleGroup D sX k) : Prop
```

**`AlgebraicGeometry.Space.rationallyEquivalent_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L364). The attribute's comment: “part (3): ∼\_rat is an equivalence relation, from the subgroup property of the cycles rationally equivalent to zero”.

> **Stacks 0EQ6, part (3).** Rational equivalence is an equivalence relation on `Z_k(X)`:
> reflexivity, symmetry and transitivity are the three closure properties of the subgroup of
> cycles rationally equivalent to zero, applied to `α - α = 0`, `β - α = -(α - β)` and
> `α - γ = (α - β) + (β - γ)`.

```lean
theorem rationallyEquivalent_equivalence (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    Equivalence (RationallyEquivalent.{v} D sX hX k)
```

**`AlgebraicGeometry.Space.chowGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L394). The attribute's comment: “part (4): CH\_k(X) = Z\_k(X)/∼\_rat, the quotient of Z\_k(X) by the subgroup of cycles rationally equivalent to zero”.

> **Stacks 0EQ6, part (4).** The *Chow group of `k`-cycles on `X`*, that is the Chow group of
> `k`-cycles modulo rational equivalence,
>
> `CH_k(X) = Z_k(X)/∼_rat`,
>
> the quotient of the group of `k`-cycles of a good algebraic space `X/B` by the subgroup of
> cycles rationally equivalent to zero.

```lean
abbrev chowGroup (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
```

**`AlgebraicGeometry.Space.chowClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L399). The attribute's comment: “part (4): the class map Z\_k(X) → CH\_k(X) of the quotient by ∼\_rat”.

> **Stacks 0EQ6, part (4).** The class map `Z_k(X) → CH_k(X)`, the quotient homomorphism.

```lean
def chowClass (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    CycleGroup D sX k →+ chowGroup.{v} D sX hX k
```

**`AlgebraicGeometry.Space.chowClass_cycleFamilySum_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalence.lean#L426). The attribute's comment: “parts (2) and (4): the class map kills ∑ (i\_j)\_* div(f\_j), the cycle of part (1); proved for the constructed CH\_k(X), not assumed”.

> **Stacks 0EQ6, parts (2) and (4).** The class in `CH_k(X)` of the cycle
> `∑ (i_j)_* div(f_j)` of part (1) is zero: a sum of principal divisors on a locally finite family
> of integral closed subspaces of δ-dimension `k + 1` is rationally equivalent to zero, hence dies
> in the quotient.

```lean
theorem chowClass_cycleFamilySum_eq_zero (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    {J : Type v} (W : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hWfin : LocallyFinite fun j : J =>
      subspacePointSet D.site D.base D.base_mem X (W j).subspace)
    (c : ∀ j, CycleGroup D ((W j).subspace.ι ≫ sX) k)
    (hWdim : ∀ j, deltaDimension D sX (W j) = k + 1)
    (hWprin : ∀ j, IsPrincipalDivisorCycle D ((W j).subspace.ι ≫ sX) k (c j)) :
    chowClass.{v} D sX hX k (cycleFamilySum D sX hX W hWfin k c) = 0
```

**`AlgebraicGeometry.Space.IsRationallyEquivalentToZeroCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L137). The attribute's comment: “part (2): rationally equivalent to zero, the summands being principal divisors at the canonical embeddings of Stacks 0ENK. The sum is part (1), AlgebraicGeometry.Space.cycleFamilySum; the index type ranges over the universe v”.

> A `k`-cycle on a good algebraic space `X/B` is *rationally equivalent to zero* when it is
> the cycle `∑ (i_j)_* div(f_j)` of part (1): there is a locally finite family `{W_j ⊆ X}` of
> integral closed subspaces with `dim_δ(W_j) = k + 1`, and on each a rational function
> `f_j ∈ R(W_j)^*` whose principal divisor `div(f_j)` is the `j`-th summand, the pushforwards
> summing to the cycle.
>
> Each `W_j` is good over `B` by `AlgebraicGeometry.Space.isGood_integralClosedSubspace` and
> integral by definition, so `div(f_j)` is read at the canonical embeddings
> `R(W_j) → Q(𝒪^h_{W_j,ξ})` of Stacks 0ENK and depends on nothing but `f_j`: the summand condition
> is `AlgebraicGeometry.Space.IsPrincipalDivisorCycleOfGood`. The sum is
> `AlgebraicGeometry.Space.cycleFamilySum`.

```lean
def IsRationallyEquivalentToZeroCanonical (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    (α : CycleGroup D sX k) : Prop
```

**`AlgebraicGeometry.Space.rationalEquivalencesCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L211). The attribute's comment: “part (2): the cycles rationally equivalent to zero, as a subgroup of Z\_k(X); the carrier is exactly the set of sums of part (1) with div(f) at the canonical embeddings”.

> The subgroup of `k`-cycles rationally equivalent to zero. Its carrier is exactly the set of
> cycles of the form `∑ (i_j)_* div(f_j)`, the principal divisors being read at the canonical
> embeddings of Stacks 0ENK.

```lean
def rationalEquivalencesCanonical (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    AddSubgroup (CycleGroup D sX k)
```

**`AlgebraicGeometry.Space.RationallyEquivalentCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L231). The attribute's comment: “part (3): α ∼\_rat β, defined as α - β being rationally equivalent to zero, for the reading of part (2) at the canonical embeddings”.

> Two `k`-cycles are *rationally equivalent* when their difference is rationally equivalent to
> zero.

```lean
def RationallyEquivalentCanonical (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    (α β : CycleGroup D sX k) : Prop
```

**`AlgebraicGeometry.Space.rationallyEquivalentCanonical_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L238). The attribute's comment: “part (3): ∼\_rat is an equivalence relation, from the subgroup property of the cycles rationally equivalent to zero”.

> Rational equivalence is an equivalence relation on `Z_k(X)`.

```lean
theorem rationallyEquivalentCanonical_equivalence (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    Equivalence (RationallyEquivalentCanonical.{v} D sX hX k)
```

**`AlgebraicGeometry.Space.chowGroupCanonical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L268). The attribute's comment: “part (4): CH\_k(X) = Z\_k(X)/∼\_rat, the quotient of Z\_k(X) by the subgroup of cycles rationally equivalent to zero”.

> The *Chow group of `k`-cycles on `X`*, that is the group of `k`-cycles modulo rational
> equivalence,
>
> `CH_k(X) = Z_k(X)/∼_rat`,
>
> the quotient of the group of `k`-cycles of a good algebraic space `X/B` by the subgroup of
> cycles rationally equivalent to zero.

```lean
abbrev chowGroupCanonical (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
```

**`AlgebraicGeometry.Space.chowClassCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L273). The attribute's comment: “part (4): the class map Z\_k(X) → CH\_k(X) of the quotient by ∼\_rat”.

> The class map `Z_k(X) → CH_k(X)`, the quotient homomorphism.

```lean
def chowClassCanonical (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ) :
    CycleGroup D sX k →+ chowGroupCanonical.{v} D sX hX k
```

**`AlgebraicGeometry.Space.chowClassCanonical_cycleFamilySum_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RationalEquivalenceCanonical.lean#L297). The attribute's comment: “parts (2) and (4): the class map kills ∑ (i\_j)\_* div(f\_j), the cycle of part (1); proved for the constructed CH\_k(X), not assumed”.

> The class in `CH_k(X)` of the cycle `∑ (i_j)_* div(f_j)`, a sum of principal divisors on a
> locally finite family of integral closed subspaces of δ-dimension `k + 1`, is zero.

```lean
theorem chowClassCanonical_cycleFamilySum_eq_zero (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    {J : Type v} (W : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hWfin : LocallyFinite fun j : J =>
      subspacePointSet D.site D.base D.base_mem X (W j).subspace)
    (c : ∀ j, CycleGroup D ((W j).subspace.ι ≫ sX) k)
    (hWdim : ∀ j, deltaDimension D sX (W j) = k + 1)
    (hWprin : ∀ j, IsPrincipalDivisorCycleOfGood D ((W j).subspace.ι ≫ sX)
      (isGood_integralClosedSubspace D sX hX (W j)) (W j).isIntegralSpace k (c j)) :
    chowClassCanonical.{v} D sX hX k (cycleFamilySum D sX hX W hWfin k c) = 0
```

## Tag 0EQ7, a lemma

[Tag 0EQ7](https://stacks.math.columbia.edu/tag/0EQ7) in the Stacks Project.

**`AlgebraicGeometry.Space.chowGroup_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowLocalizationSequence.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowLocalizationSequence.lean#L542).

> In Situation 0EDT let `X/B` be good, let `U ⊆ X` be an open subspace, let `Y ⊆ X` be a closed
> subspace with `|Y| = |X| \ |U|` and let `i : Y → X`, `j : U → X` be the inclusions. Let `k ∈ ℤ`.
>
> 1. If `α, β ∈ Z_k(X)` satisfy `α|_U ∼_rat β|_U`, then `α ∼_rat β + i_*γ` for some `γ ∈ Z_k(Y)`.
> 2. In other words, `CH_k(Y) →[i_*] CH_k(X) →[j^*] CH_k(U) → 0` is an exact complex of abelian
>    groups: the kernel of `j^*` is the image of `i_*`, and `j^*` is surjective.

```lean
theorem chowGroup_localization
    (hcomplement : Set.range (pointsMap D.site D.base D.base_mem Y.toFunctor Y.ι) =
      (Set.range (pointsMap D.site D.base D.base_mem U.toFunctor U.ι))ᶜ) (k : ℤ) :
    (∀ α β : CycleGroup D sX k,
      RationallyEquivalent.{v} D (U.ι ≫ sX) (isGood_ι_of_isOpenSubspace D sX hX U hU) k
        (cycleGroupRestrict D sX hX (U.ι ≫ sX) (isGood_ι_of_isOpenSubspace D sX hX U hU) hU.2
          rfl k α)
        (cycleGroupRestrict D sX hX (U.ι ≫ sX) (isGood_ι_of_isOpenSubspace D sX hX U hU) hU.2
          rfl k β) →
      ∃ γ : CycleGroup D (Y.ι ≫ sX) k,
        RationallyEquivalent.{v} D sX hX k α
          (β + cycleGroupClosedPushforward D hX.1 hY.1 (D.isDecentSpace_of_isGood sX hX) hY.2
            sX hX.2.2 (Y.ι ≫ sX) rfl k γ)) ∧
      Function.Exact (chowGroupClosedPushforward.{v} D sX hX Y hY k)
        (chowGroupRestrict.{v} D sX hX U hU k) ∧
      Function.Surjective (chowGroupRestrict.{v} D sX hX U hU k)
```

## Tag 0EQ8, a remark

[Tag 0EQ8](https://stacks.math.columbia.edu/tag/0EQ8) in the Stacks Project.

**`AlgebraicGeometry.Space.rationallyEquivalent_locallyFiniteCycleSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/InfiniteSumsRationalEquivalence.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/InfiniteSumsRationalEquivalence.lean#L182). The attribute's comment: “the remark in full: for alpha\_i, beta\_i supported on a locally finite family T\_i with alpha\_i ~rat beta\_i on T\_i, the sums are k-cycles and are rationally equivalent, the combined witnessing family being locally finite”.

> **Stacks 0EQ8.** Let `{T_i}_{i ∈ I}` be a locally finite collection of subsets of `|X|` and
> let `α_i, β_i ∈ Z_k(X)` be supported on `T_i`. If `α_i ∼_rat β_i` on `T_i` for every `i`, then
> `∑ α_i ∼_rat ∑ β_i`: the combined family `{W_{i, j}}_{i ∈ I, j ∈ J_i}` of witnessing subspaces
> is locally finite, so it is a single rational equivalence between the two sums.

```lean
theorem rationallyEquivalent_locallyFiniteCycleSum (sX : X ⟶ D.space) (hX : D.IsGood sX) (k : ℤ)
    (T : I → Set (points D.site D.base D.base_mem X)) (hT : LocallyFinite T)
    (α β : I → CycleGroup D sX k)
    (hαT : ∀ (i : I) (Z : IntegralClosedSubspace D.site D.base D.base_mem X),
      (α i).1 Z ≠ 0 → subspacePointSet D.site D.base D.base_mem X Z.subspace ⊆ T i)
    (hβT : ∀ (i : I) (Z : IntegralClosedSubspace D.site D.base D.base_mem X),
      (β i).1 Z ≠ 0 → subspacePointSet D.site D.base D.base_mem X Z.subspace ⊆ T i)
    (hαβ : ∀ i, RationallyEquivalentOn.{v} D sX hX k (T i) (α i) (β i)) :
    RationallyEquivalent.{v} D sX hX k (locallyFiniteCycleSum D sX k T hT α hαT)
      (locallyFiniteCycleSum D sX k T hT β hβT)
```

**`locallyFinite_sigma_of_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/LocallyFinite/Sigma.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/LocallyFinite/Sigma.lean#L42). The attribute's comment: “local finiteness of the combined family”.

> Let `T : I → Set Y` be a locally finite collection of subsets of a topological space and,
> for each `i`, let `W i : J i → Set Y` be a locally finite collection with `W i j ⊆ T i` for all
> `j`. Then the combined collection `fun ij : Σ i, J i ↦ W ij.1 ij.2` is locally finite.

```lean
theorem locallyFinite_sigma_of_subset {Y : Type u} [TopologicalSpace Y] {I : Type v}
    {J : I → Type w} {T : I → Set Y} (hT : LocallyFinite T) {W : ∀ i, J i → Set Y}
    (hW : ∀ i, LocallyFinite (W i)) (hWT : ∀ i j, W i j ⊆ T i) :
    LocallyFinite fun ij : Σ i, J i ↦ W ij.1 ij.2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.15, Tag 0EQ5](https://stacks.math.columbia.edu/tag/0EQ5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
