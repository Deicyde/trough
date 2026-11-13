---
declaration: section
origin: cited
lean: charP_prime_of_not_separable, Irreducible.eq_expand_of_derivative_eq_zero, Irreducible.isCoprime_derivative_or_eq_expand, Polynomial.separable_iff_derivative_ne_zero, Polynomial.card_toFinset_aroots_expand, Polynomial.natSepDegree_eq_of_isAlgClosed, Polynomial.natSepDegree, IntermediateField.bijOn_algHom_apply_of_adjoin_eq_top
statement: formalized
proof: formalized
---

# 9.12 Separable algebraic extensions

Section 9.12 of the Stacks Project, [Tag 09GZ](https://stacks.math.columbia.edu/tag/09GZ). 6 tags here are carried by 10 declarations of the repository (4 in StacksCore and 6 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09H0, a lemma

[Tag 09H0](https://stacks.math.columbia.edu/tag/09H0) in the Stacks Project.

**`charP_prime_of_not_separable`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Separable.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Separable.lean#L80). The attribute's comment: “second part”.

> **Stacks 09H0** (second part).
> If a field `K` admits an irreducible polynomial that is not separable, then `K` has prime
> characteristic: there is a prime `p` with `CharP K p`.

```lean
theorem charP_prime_of_not_separable
    {K : Type*} [Field K] {f : K[X]} (hfi : Irreducible f) (hfs : ¬f.Separable) :
    ∃ p, p.Prime ∧ CharP K p
```

**`Irreducible.eq_expand_of_derivative_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/IrreducibleSeparableContraction.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/IrreducibleSeparableContraction.lean#L33). The attribute's comment: “third part”.

> **Stacks 09H0** (third part). If `P ∈ F[x]` is irreducible with `P' = 0`, then `F` has
> prime characteristic `p` and `P(x) = Q(x ^ (p ^ m))` for some `m ≥ 1` and some irreducible
> `Q ∈ F[x]` relatively prime to its derivative `Q'`.

```lean
theorem eq_expand_of_derivative_eq_zero (hP : Irreducible P) (hd : derivative P = 0) :
    ∃ p, p.Prime ∧ CharP F p ∧ ∃ m, 1 ≤ m ∧ ∃ Q : F[X],
      Irreducible Q ∧ IsCoprime Q (derivative Q) ∧ expand F (p ^ m) Q = P
```

**`Irreducible.isCoprime_derivative_or_eq_expand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/IrreducibleSeparableContraction.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/IrreducibleSeparableContraction.lean#L52).

> **Stacks 09H0**. Let `P ∈ F[x]` be irreducible. Then either `P` and `P'` are relatively
> prime, or `P' = 0`; and in the second case `F` has prime characteristic `p` and
> `P(x) = Q(x ^ (p ^ m))` for some `m ≥ 1` and some irreducible `Q ∈ F[x]` relatively prime to
> its derivative `Q'`.

```lean
theorem isCoprime_derivative_or_eq_expand (hP : Irreducible P) :
    (IsCoprime P (derivative P) ∨ derivative P = 0) ∧
      (derivative P = 0 → ∃ p, p.Prime ∧ CharP F p ∧ ∃ m, 1 ≤ m ∧ ∃ Q : F[X],
        Irreducible Q ∧ IsCoprime Q (derivative Q) ∧ expand F (p ^ m) Q = P)
```

Declarations registered for the tag:

- [`Polynomial.separable_iff_derivative_ne_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.separable_iff_derivative_ne_zero#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Separable.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Separable.lean#L12) (StacksCore): “first part”.

## Tag 09H4, a lemma

[Tag 09H4](https://stacks.math.columbia.edu/tag/09H4) in the Stacks Project.

**`Polynomial.card_toFinset_aroots_expand`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Perfect.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Perfect.lean#L16).

> **Stacks 09H4**.
> Over a perfect ring `S` of exponential characteristic `p`, the polynomial `f.expand R p`
> and `f` have the same number of distinct roots in `S`: the Frobenius bijection on `S`
> identifies the root sets.

```lean
theorem Polynomial.card_toFinset_aroots_expand
    {R : Type*} [CommRing R]
    (S : Type*) [CommRing S] [IsDomain S] [DecidableEq S] [Algebra R S]
    {p : ℕ} [ExpChar S p] [PerfectRing S p] {f : R[X]} :
    ((f.expand R p).aroots S).toFinset.card = (f.aroots S).toFinset.card
```

## Tag 09H5, a definition

[Tag 09H5](https://stacks.math.columbia.edu/tag/09H5) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.natSepDegree_eq_of_isAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.natSepDegree_eq_of_isAlgClosed#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SeparableDegree.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableDegree.lean#L13) (StacksCore).
- [`Polynomial.natSepDegree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.natSepDegree#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks09H5.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks09H5.lean#L10) (StacksFrontier).

## Tag 09H7, a lemma

[Tag 09H7](https://stacks.math.columbia.edu/tag/09H7) in the Stacks Project.

**`IntermediateField.bijOn_algHom_apply_of_adjoin_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableDegree.lean#L53).

> **Stacks 09H7**.
> Let `E = F(α₀, …, α_{n-1})` and let `L` be a field extension of `F`. Write
> `Kᵢ = F(α₀, …, α_{i-1})` and `Pᵢ` for the minimal polynomial of `αᵢ` over `Kᵢ`. Then
> `φ ↦ (φ(α₀), …, φ(α_{n-1}))` is a bijection from the `F`-embeddings `E → L` onto the tuples
> `(β₀, …, β_{n-1})` for which there are `F`-embeddings `ψᵢ : Kᵢ → L` (`i ≤ n`) such that `βᵢ` is
> a root of `Pᵢ` twisted by `ψᵢ`, and `ψᵢ₊₁` extends `ψᵢ` and sends `αᵢ` to `βᵢ`.

```lean
theorem IntermediateField.bijOn_algHom_apply_of_adjoin_eq_top {L : Type*} [Field L] [Algebra F L]
    (α : ℕ → E) (n : ℕ) (hgen : adjoin F (α '' Set.Iio n) = ⊤) :
    Set.BijOn (fun (φ : E →ₐ[F] L) (i : Fin n) ↦ φ (α i)) Set.univ
      {β | ∃ ψ : ∀ i ≤ n, adjoin F (α '' Set.Iio i) →ₐ[F] L, ∀ (i : ℕ) (hi : i < n),
        ((minpoly (adjoin F (α '' Set.Iio i)) (α i)).map (ψ i hi.le : _ →+* L)).IsRoot
          (β ⟨i, hi⟩) ∧
        (ψ (i + 1) (Order.add_one_le_of_lt hi)).comp (inclusion <| adjoin.mono _ _ _ <|
          Set.image_mono <| Set.Iio_subset_Iio (Nat.le_add_right i 1)) = ψ i hi.le ∧
        ψ (i + 1) (Order.add_one_le_of_lt hi)
          ⟨α i, Set.mem_of_subset_of_mem (subset_adjoin _ _) <|
            Set.mem_image_of_mem α <| Set.mem_Iio.2 (Nat.lt_add_one i)⟩ =
          β ⟨i, hi⟩}
```

**`IntermediateField.bijOn_algHom_apply_rootTowerAlgHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/SeparableDegreeRootTower.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/SeparableDegreeRootTower.lean#L192). The attribute's comment: “for an arbitrary field extension `L` of `F` in place of an algebraic closure”.

> **Stacks 09H7**.
> Let `E = F(α₀, …, α_{n-1})` be an algebraic extension of `F` and `L` a field extension of `F`.
> Write `Kᵢ = F(α₀, …, α_{i-1})` and `Pᵢ` for the minimal polynomial of `αᵢ` over `Kᵢ`. Then
> `φ ↦ (φ(α₀), …, φ(α_{n-1}))` is a bijection from the `F`-embeddings `E → L` onto the tuples
> `(β₀, …, β_{n-1})` such that, for each `i < n`, `βᵢ` is a root of `Pᵢ` twisted by the embedding
> `φᵢ : Kᵢ → L` determined by `β₀, …, β_{i-1}`; here `φ₀` is the structure map and `φᵢ₊₁` is the
> unique extension of `φᵢ` sending `αᵢ` to `βᵢ`, which exists because `Kᵢ₊₁ = Kᵢ[x]/(Pᵢ)`
> (`IntermediateField.rootTowerAlgHom`).

```lean
theorem IntermediateField.bijOn_algHom_apply_rootTowerAlgHom [Algebra.IsAlgebraic F E]
    {L : Type*} [Field L] [Algebra F L]
    (α : ℕ → E) (n : ℕ) (hgen : adjoin F (α '' Set.Iio n) = ⊤) :
    Set.BijOn (fun (φ : E →ₐ[F] L) (i : Fin n) ↦ φ (α i)) Set.univ
      {β | ∀ (i : ℕ) (hi : i < n), ∃ ψ, rootTowerAlgHom F α β i hi.le = some ψ ∧
        ((minpoly (adjoin F (α '' Set.Iio i)) (α i)).map (ψ : _ →+* L)).IsRoot (β ⟨i, hi⟩)}
```

## Tag 09H8, a lemma

[Tag 09H8](https://stacks.math.columbia.edu/tag/09H8) in the Stacks Project.

**`Field.card_algHom_eq_prod_natSepDegree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableDegree.lean#L98).

> **Stacks 09H8**.
> Let `E = F(α₀, …, α_{n-1})` be an algebraic extension and `L` an algebraically closed field
> extension of `F`. Then the number of `F`-embeddings `E → L` is the product over `i < n` of the
> separable degrees of the minimal polynomials of `αᵢ` over `F(α₀, …, α_{i-1})`.

```lean
theorem Field.card_algHom_eq_prod_natSepDegree (L : Type*) [Field L] [Algebra F L] [IsAlgClosed L]
    [Algebra.IsAlgebraic F E] (α : ℕ → E) (n : ℕ) (hgen : adjoin F (α '' Set.Iio n) = ⊤) :
    Nat.card (E →ₐ[F] L) =
      ∏ i ∈ Finset.range n, (minpoly (adjoin F (α '' Set.Iio i)) (α i)).natSepDegree
```

## Tag 09H9, a lemma

[Tag 09H9](https://stacks.math.columbia.edu/tag/09H9) in the Stacks Project.

**`Algebra.isSeparable_of_isSeparable_adjoin_image_Iio`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/SeparableDegreeTower.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/SeparableDegreeTower.lean#L58). The attribute's comment: “Separability of `K/F` when each `αᵢ` is separable over `K_{i-1}`.”.

> **Stacks 09H9**, separability.
> Let `E = F(α₀, …, α_{n-1})`. If each `αᵢ` is separable over `F(α₀, …, α_{i-1})`, then `E / F` is
> separable.

```lean
theorem Algebra.isSeparable_of_isSeparable_adjoin_image_Iio (α : ℕ → E) (n : ℕ)
    (hgen : IntermediateField.adjoin F (α '' Set.Iio n) = ⊤)
    (hsep : ∀ i < n, IsSeparable (IntermediateField.adjoin F (α '' Set.Iio i)) (α i)) :
    Algebra.IsSeparable F E
```

**`Field.card_algHom_eq_finrank_of_isSeparable_adjoin_image_Iio`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/SeparableDegreeTower.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/SeparableDegreeTower.lean#L74). The attribute's comment: “Equality `|Mor_F(K, F̄)| = [K : F]` when each `αᵢ` is separable over `K_{i-1}`.”.

> **Stacks 09H9**, the count.
> Let `E = F(α₀, …, α_{n-1})` and `L` an algebraically closed extension of `F`. If each `αᵢ` is
> separable over `F(α₀, …, α_{i-1})`, then the number of `F`-embeddings `E → L` is `[E : F]`.
> Finiteness of `E / F` is not assumed: it follows from the hypotheses.

```lean
theorem Field.card_algHom_eq_finrank_of_isSeparable_adjoin_image_Iio (L : Type*) [Field L]
    [Algebra F L] [IsAlgClosed L] (α : ℕ → E) (n : ℕ)
    (hgen : adjoin F (α '' Set.Iio n) = ⊤)
    (hsep : ∀ i < n, IsSeparable (adjoin F (α '' Set.Iio i)) (α i)) :
    Nat.card (E →ₐ[F] L) = finrank F E
```

**`Field.card_algHom_lt_finrank_of_not_isSeparable_adjoin_image_Iio`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/SeparableDegreeTower.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/SeparableDegreeTower.lean#L89). The attribute's comment: “Strict inequality `|Mor_F(K, F̄)| < [K : F]` when some `αᵢ` is not separable over `K_{i-1}`.”.

> **Stacks 09H9**, the strict inequality.
> Let `E / F` be a finite extension, `L` an algebraically closed extension of `F` and
> `α₀, …, α_{n-1} ∈ E`. If some `αᵢ` is not separable over `F(α₀, …, α_{i-1})`, then the number of
> `F`-embeddings `E → L` is strictly smaller than `[E : F]`. That the `αᵢ` generate `E` is not
> needed.

```lean
theorem Field.card_algHom_lt_finrank_of_not_isSeparable_adjoin_image_Iio (L : Type*) [Field L]
    [Algebra F L] [IsAlgClosed L] [FiniteDimensional F E] (α : ℕ → E) (n : ℕ)
    (hns : ∃ i < n, ¬ IsSeparable (adjoin F (α '' Set.Iio i)) (α i)) :
    Nat.card (E →ₐ[F] L) < finrank F E
```

Declarations registered for the tag:

- [`IntermediateField.isSeparable_adjoin_iff_isSeparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.isSeparable_adjoin_iff_isSeparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SeparableClosure.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableClosure.lean#L12) (StacksCore): “Combine with 09HA, which is covered by `Field.finSepDegree_eq_finrank_iff` and `Field.finSepDegree_le_finrank`. Also use `Algebra.IsSeparable.trans` to transfer the separability conditions.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.12, Tag 09GZ](https://stacks.math.columbia.edu/tag/09GZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
