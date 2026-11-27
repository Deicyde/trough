---
declaration: theorem
origin: cited
lean: Erdos349.erdos_349, Erdos349.complete_for_alpha_in_Ioo_one_to_goldenRatio, Erdos349.exists_t_for_k_disjoint_segments, Erdos349.erdos_349.variants.floor_3_halves_odd, Erdos349.erdos_349.variants.floor_3_halves_even, Erdos349.alpha_gt_two_not_isGoodPair, Erdos349.alpha_le_one_not_isGoodPair, Erdos349.exists_finsetSum_two_pow, Erdos349.one_two_isGoodPair, Erdos349.dyadic_two_isGoodPair, Erdos349.int_coeff_ge_two_not_isGoodPair, Erdos349.integer_isGoodPair_iff, Erdos349.three_halves_two_not_isGoodPair
statement: formalized
---

# Erdős Problem 349

> *References:*
> - [erdosproblems.com/349](https://www.erdosproblems.com/349)
> - [Ge26] Geneson, J., *Deletion thresholds and exponential examples for complete sequences*.
>   [arXiv:2609.25107](https://arxiv.org/abs/2609.25107) (2026).

*Quoted from [FormalConjectures/ErdosProblems/349.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/349](https://www.erdosproblems.com/349).

The file states 13 research or textbook statements: 3 open, 9 solved and 1 textbook result.

## `Erdos349.erdos_349`

Open: stated without proof.

> For what values of $t,\alpha \in (0,\infty)$ is the sequence $\lfloor t\alpha^n\rfloor$ complete
> (that is, all sufficiently large integers are the sum of distinct integers of the form $\lfloor t\alpha^n\rfloor$)?

```lean
theorem erdos_349 :
    {(t, α) | 0 < t ∧ 0 < α ∧ IsGoodPair t α} = erdos_349.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L49).

## `Erdos349.complete_for_alpha_in_Ioo_one_to_goldenRatio`

Solved: stated here without proof.

> Graham suggested that the sequence is complete for all $t>0$ and all
> $1 < \alpha < \frac{1+\sqrt{5}}{2}$. Geneson [Ge26, Theorem 9] disproved this: for the Salem number
> $\alpha$ with minimal polynomial $x^{18} - x^{12} - x^{11} - x^{10} - x^9 - x^8 - x^7 - x^6 + 1$,
> which satisfies $6/5 < \alpha < 13/10$, there are arbitrarily large $t > 0$ such that
> $\lfloor t\alpha^n\rfloor$ is even for every $n \geq 0$, so no odd integer is a sum of terms.

```lean
theorem complete_for_alpha_in_Ioo_one_to_goldenRatio :
    ¬ ∀ t α : ℝ, 0 < t → α ∈ Set.Ioo 1 ((1 + √5) / 2) → IsGoodPair t α
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L61).

## `Erdos349.exists_t_for_k_disjoint_segments`

Solved: stated here without proof.

> For any $k$ there exists some $t_k\in (0,1)$ such that the set of $\alpha > 0$
> such that the sequence $\lfloor t_k\alpha^n\rfloor$ is complete consists of at least $k$
> disjoint line segments, that is, it has at least $k$ connected components.

```lean
theorem exists_t_for_k_disjoint_segments (k : ℕ) :
    ∃ t ∈ Ioo 0 1,
      let S := {α | 0 < α ∧ IsGoodPair t α}
      k ≤ (connectedComponentIn S '' S).encard
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L71).

## `Erdos349.erdos_349.variants.floor_3_halves_odd`

Open: stated without proof.

> Is it true that the terms of the sequence $\lfloor (3/2)^n\rfloor$ are odd infinitely
> often and even infinitely often?

```lean
theorem erdos_349.variants.floor_3_halves_odd :
    {n | Odd ⌊(3/2 : ℝ) ^ n⌋}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L82).

## `Erdos349.erdos_349.variants.floor_3_halves_even`

Open: stated without proof.

> Is it true that the terms of the sequence $\lfloor (3/2)^n\rfloor$ are even infinitely often?

```lean
theorem erdos_349.variants.floor_3_halves_even :
    {n | Even ⌊(3/2 : ℝ) ^ n⌋}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L90).

## `Erdos349.alpha_gt_two_not_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/23c629bc2347864782ce88f957a64d6567b978a1/FormalConjectures/ErdosProblems/349.lean#L87](https://github.com/cepadugato/formal-conjectures/blob/23c629bc2347864782ce88f957a64d6567b978a1/FormalConjectures/ErdosProblems/349.lean#L87).

> For $\alpha > 2$ and any $t > 0$, the sequence $\lfloor t\alpha^n\rfloor$ is not additively
> complete; equivalently $(t, \alpha)$ is not a "good pair". A partial result on the open Erdős
> Problem 349: it complements `complete_for_alpha_in_Ioo_one_to_goldenRatio`.
>
> The proof is recorded via the `formal_proof` mechanism rather than written inline, as it exceeds
> the repository's proof-length guideline.

```lean
theorem alpha_gt_two_not_isGoodPair (t α : ℝ) (ht : 0 < t) (hα : 2 < α) : ¬ IsGoodPair t α
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L104).

## `Erdos349.alpha_le_one_not_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean).

> For $0 < \alpha \le 1$ and any $t > 0$, $(t, \alpha)$ is not a good pair: every term
> $\lfloor t\alpha^n\rfloor$ lies in the finite interval $[0, \lfloor t\rfloor]$ (since
> $\alpha^n \le 1$), so every subset sum is bounded by the constant $\sum_{i \in [0,\lfloor t\rfloor]} i$,
> and no large integer can be a subset sum. A partial result on the open Erdős Problem 349,
> complementing the $2 < \alpha$ and integer-coefficient cases.

```lean
theorem alpha_le_one_not_isGoodPair (t α : ℝ) (ht : 0 < t) (hα0 : 0 < α) (hα1 : α ≤ 1) :
    ¬ IsGoodPair t α
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L116).

## `Erdos349.exists_finsetSum_two_pow`

Textbook result, stated without proof. A Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean#L319](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean#L319).

> **Binary expansion.** Every natural number $k$ is a sum of distinct powers of two: there is
> a finite set $E$ of exponents with $k = \sum_{i \in E} 2^i$. Proved by strong induction:
> subtract the largest power $2^m \le k$, recurse on the remainder. A textbook-level building
> block for `one_two_isGoodPair` below; it says nothing about `IsGoodPair` itself.

```lean
theorem exists_finsetSum_two_pow (k : ℕ) :
    ∃ E : Finset ℕ, k = ∑ i ∈ E, 2 ^ i
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L127).

## `Erdos349.one_two_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean).

> **The pair $(1, 2)$ is good.** The powers of two $\lfloor 1\cdot 2^n\rfloor = 2^n$ form an
> additively complete set: every $k \ge 1$ is a finite sum of distinct powers of two.

```lean
theorem one_two_isGoodPair : IsGoodPair 1 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L137).

## `Erdos349.dyadic_two_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean).

> **The dyadic fiber at $\alpha = 2$.** For every $k$, the pair $(1/2^k, 2)$ is good: the
> sequence $\lfloor 2^n / 2^k\rfloor$ is additively complete because at index $n = m + k$ it equals
> the exact power $2^m$, so its range contains all powers of two, which already form an additively
> complete set. Uses monotonicity `IsAddComplete.mono`.

```lean
theorem dyadic_two_isGoodPair (k : ℕ) : IsGoodPair (1 / 2 ^ k) 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L148).

## `Erdos349.int_coeff_ge_two_not_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean).

> **Integer leading coefficient $t \ge 2$ blocks completeness.** For every integer base
> $\alpha$, the pair $(t, \alpha)$ with integer $t \ge 2$ is not good: $\lfloor t\alpha^n\rfloor =
> t\alpha^n$ is a multiple of $t$, so every subset sum is too, but two consecutive large integers
> cannot both be multiples of $t$. Generalizes the parity obstruction ($t = 2$). A partial result
> on Erdős Problem 349.

```lean
theorem int_coeff_ge_two_not_isGoodPair (t : ℤ) (ht : 2 ≤ t) (α : ℤ) :
    ¬ IsGoodPair (t : ℝ) (α : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L160).

## `Erdos349.integer_isGoodPair_iff`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/19e39e33be27d46713a423263d38312fe40c9e78/FormalConjectures/ErdosProblems/349.lean).

> **Erdős Problem 349, complete characterization on positive integer pairs.** For integers
> $t \ge 1$, $\alpha \ge 1$, the pair $(t, \alpha)$ is good (i.e. $\lfloor t\alpha^n\rfloor$ is
> additively complete) iff $(t, \alpha) = (1, 2)$. Assembles the four partial results: $(1,2)$ is
> good, $\alpha \le 1$ fails, $2 < \alpha$ fails (`alpha_gt_two_not_isGoodPair`), and integer
> $t \ge 2$ fails.

```lean
theorem integer_isGoodPair_iff (t α : ℤ) (ht : 1 ≤ t) (hα : 1 ≤ α) :
    IsGoodPair (t : ℝ) (α : ℝ) ↔ t = 1 ∧ α = 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L173).

## `Erdos349.three_halves_two_not_isGoodPair`

Solved: stated here; a Lean proof is at [https://github.com/cepadugato/formal-conjectures/blob/erdos-349-three-halves-fiber-proof/FormalConjectures/ErdosProblems/349.lean](https://github.com/cepadugato/formal-conjectures/blob/erdos-349-three-halves-fiber-proof/FormalConjectures/ErdosProblems/349.lean).

> **The pair $(3/2, 2)$ is NOT good.** The negative companion of `dyadic_two_isGoodPair`:
> while every dyadic coefficient $1/2^k$ gives a good pair at $\alpha = 2$, the non-dyadic rational
> $t = 3/2$ does not. The sequence $\lfloor (3/2)\cdot 2^n\rfloor = 1, 3, 6, 12, 24, \ldots$ is not
> additively complete because every term but the first $\lfloor 3/2\rfloor = 1$ is a multiple of
> $3$ (namely $\lfloor (3/2)\cdot 2^{n+1}\rfloor = 3\cdot 2^n$), so every subset sum is
> $\equiv 0$ or $1 \pmod 3$; the infinitely many integers $\equiv 2 \pmod 3$ are never reached.
> A partial result on Erdős Problem 349 in the same divisibility family as
> `int_coeff_ge_two_not_isGoodPair` (here the modulus is $3$).

```lean
theorem three_halves_two_not_isGoodPair : ¬ IsGoodPair (3 / 2) 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/349.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean#L189).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/349.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/349.lean)
- [erdosproblems.com/349](https://www.erdosproblems.com/349)
