---
declaration: theorem
origin: cited
lean: Erdos494.erdos_494.variants.k_eq_2_card_not_pow_two, Erdos494.erdos_494.variants.k_eq_2_card_pow_two, Erdos494.erdos_494.variants.k_eq_3_card_gt_6, Erdos494.erdos_494.variants.k_eq_4_card_gt_12, Erdos494.erdos_494.variants.card_divisible_by_prime_gt_k, Erdos494.erdos_494.variants.k_eq_card, Erdos494.erdos_494.variants.card_eq_2k, Erdos494.erdos_494.variants.gordon_fraenkel_straus, Erdos494.erdos_494.variants.product
statement: formalized
---

# Erdős Problem 494

> *References:*
>   - [erdosproblems.com/494](https://www.erdosproblems.com/494)
>   - [SeSt58] Selfridge, J. L. and Straus, E., On the determination of numbers by their sums
>       of a fixed order. Pacific Journal of Math. (1958), 847-856.
>   - [Er61] Erdős, Paul, Some unsolved problems. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>       221-254.
>   - [GFS62] Gordon, B. and Fraenkel, A. S. and Straus, E. G., On the determination of sets
>       by the sets of sums of a certain order. Pacific J. Math. (1962), 187--196.
>   - [FoIz94] Fomin, D. V. and Izhboldin, O. T., Sets of multiple sums. Proc. St. Petersburg
>       Math. Soc. 3 (1994), 244-259.

*Quoted from [FormalConjectures/ErdosProblems/494.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/494](https://www.erdosproblems.com/494).

The file states 9 research or textbook statements: 9 solved.

## `Erdos494.erdos_494.variants.k_eq_2_card_not_pow_two`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/a2d6dcb99d4f11469cbb40c18959357031786c4c/erdos-494/Solution.lean#L26](https://github.com/linrock/math-proofs/blob/a2d6dcb99d4f11469cbb40c18959357031786c4c/erdos-494/Solution.lean#L26).

> Selfridge and Straus [SeSt58] showed that the conjecture is true when $k = 2$ and
> $|A| \ne 2^l$ for $l \ge 0$.
> They also gave counterexamples when $k = 2$ and $|A| = 2^l$.

```lean
theorem erdos_494.variants.k_eq_2_card_not_pow_two :
    ∀ card : ℕ, (∀ l : ℕ, card ≠ 2 ^ l) → Erdos494Unique 2 card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L59).

## `Erdos494.erdos_494.variants.k_eq_2_card_pow_two`

Solved: stated here; a Lean proof is at [https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L533](https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L533).

> Selfridge and Straus [SeSt58] gave counterexamples to the conjecture
> when $k = 2$ and $|A| = 2^l$.

```lean
theorem erdos_494.variants.k_eq_2_card_pow_two :
    ∀ card : ℕ, (∃ l : ℕ, card = 2 ^ l) → ¬Erdos494Unique 2 card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L71).

## `Erdos494.erdos_494.variants.k_eq_3_card_gt_6`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/a2d6dcb99d4f11469cbb40c18959357031786c4c/erdos-494/Solution.lean#L30](https://github.com/linrock/math-proofs/blob/a2d6dcb99d4f11469cbb40c18959357031786c4c/erdos-494/Solution.lean#L30).

> Selfridge and Straus [SeSt58] also showed that the conjecture is true when
> 1) $k = 3$ and $|A| > 6$, except possibly for $|A| = 27$ and $|A| = 486$, or
> 2) $k = 4$ and $|A| > 12$.
> More generally, they proved that $A$ is determined by $A_k$ (and $|A|$) if $|A|$ is divisible by
> a prime greater than $k$.
>
> The cases $|A| = 27$ and $|A| = 486$ were left open in [SeSt58]. Fomin and Izhboldin [FoIz94]
> later found two distinct sets of each of these sizes with the same multiset of $3$-sums, so
> these exceptions are genuine.

```lean
theorem erdos_494.variants.k_eq_3_card_gt_6 :
    ∀ card > 6, card ≠ 27 → card ≠ 486 → Erdos494Unique 3 card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L89).

## `Erdos494.erdos_494.variants.k_eq_4_card_gt_12`

Solved: stated here without proof.

> Selfridge and Straus [SeSt58] showed that the conjecture is true
> when $k = 4$ and $|A| > 12$.

```lean
theorem erdos_494.variants.k_eq_4_card_gt_12 :
    ∀ card > 12, Erdos494Unique 4 card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L98).

## `Erdos494.erdos_494.variants.card_divisible_by_prime_gt_k`

Solved: stated here without proof.

> Selfridge and Straus [SeSt58] proved that $A$ is determined by $A_k$
> if $|A|$ is divisible by a prime greater than $k$.

```lean
theorem erdos_494.variants.card_divisible_by_prime_gt_k :
    ∀ (k card p : ℕ), p.Prime → k ∈ Set.Ioo 0 p → p ∣ card → Erdos494Unique k card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L107).

## `Erdos494.erdos_494.variants.k_eq_card`

Solved: stated here; a Lean proof is at [https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L592](https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L592).

> Kruyt noted that the conjecture fails when $|A| = k$, by rotating $A$ around an appropriate point.

```lean
theorem erdos_494.variants.k_eq_card :
    ∀ k > 2, ¬Erdos494Unique k k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L118).

## `Erdos494.erdos_494.variants.card_eq_2k`

Solved: stated here; a Lean proof is at [https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L916](https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L916).

> Similarly, Tao noted that the conjecture fails when $|A| = 2k$, by taking $A$ to be a set of
> the total sum 0 and considering $-A$.

```lean
theorem erdos_494.variants.card_eq_2k :
    ∀ k > 2, ¬Erdos494Unique k (2 * k)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L130).

## `Erdos494.erdos_494.variants.gordon_fraenkel_straus`

Solved: stated here without proof.

> Gordon, Fraenkel, and Straus [GRS62] proved that the claim is true for all $k > 2$ when
> $|A|$ is sufficiently large.

```lean
theorem erdos_494.variants.gordon_fraenkel_straus :
    ∀ k > 2, ∀ᶠ card in atTop, Erdos494Unique k card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L139).

## `Erdos494.erdos_494.variants.product`

Solved: stated here; a Lean proof is at [https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L951](https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/494.lean#L951).

> A counterexample to the product version of the conjecture (by Steinerberger).

```lean
theorem erdos_494.variants.product :
    ∃ (A B : Finset ℂ), A.card = B.card ∧ prodMultiset A 3 = prodMultiset B 3 ∧
      A ≠ B
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/494.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/494.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/494.lean)
- [erdosproblems.com/494](https://www.erdosproblems.com/494)
