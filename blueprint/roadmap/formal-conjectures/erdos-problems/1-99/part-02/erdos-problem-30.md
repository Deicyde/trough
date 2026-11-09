---
declaration: theorem
origin: cited
lean: Erdos30.erdos_30, Erdos30.erdos_30.variants.O_one, Erdos30.erdos_30.variants.erdos_turan, Erdos30.erdos_30.variants.lindstrom, Erdos30.erdos_30.variants.balogh_furedi_roy, Erdos30.erdos_30.variants.obryant, Erdos30.erdos_30.variants.carter_hunter_obryant, Erdos30.erdos_30.variants.singer, Erdos30.erdos_30.variants.isEquivalent_sqrt, Erdos30.erdos_30.variants.elementary_difference_count, Erdos30.erdos_30.variants.distinct_sums_card, Erdos30.erdos_30.variants.distinct_sums_in_range, Erdos30.erdos_30.variants.erdos_turan_counting, Erdos30.erdos_30.variants.lindstrom_weak
statement: formalized
---

# Erdős Problem 30

> *References:*
> - [erdosproblems.com/30](https://www.erdosproblems.com/30)
> - [ErTu41] Erdős, P. and Turán, P., *On a problem of Sidon in additive number theory, and on
>   some related problems*. J. London Math. Soc. 16 (1941), 212-215.
> - [Li69] Lindström, B., *An inequality for $B_2$-sequences*. J. Combinatorial Theory 6 (1969),
>   211-212.
> - [Si38] Singer, J., *A theorem in finite projective geometry and some applications to number
>   theory*. Trans. Amer. Math. Soc. 43 (1938), 377-385.
> - [BFR23] Balogh, J., Füredi, Z. and Roy, S., *An upper bound on the size of Sidon sets*.
>   Amer. Math. Monthly 130 (2023), 437-445.
> - [OB22] O'Bryant, K., *On the size of finite Sidon sets*.
>   [arXiv:2207.07800](https://arxiv.org/abs/2207.07800) (2022).
> - [CHO25] Carter, D., Hunter, Z. and O'Bryant, K., *On the diameter of finite Sidon sets*.
>   Acta Math. Hungar. 175 (2025), 108-126.
>
> See also [Ben Green's Open Problem 31](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)
> (formalised in `FormalConjectures/GreensOpenProblems/31.lean`).

*Quoted from [FormalConjectures/ErdosProblems/30.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/30](https://www.erdosproblems.com/30).

The file states 14 research or textbook statements: 2 open, 7 solved and 5 textbook results.

## `Erdos30.erdos_30`

Open: stated without proof.

> Is it true that, for every $\varepsilon > 0$, $h(N) = \sqrt N + O_{\varepsilon}(N^\varepsilon)$

```lean
theorem erdos_30 :
    ∀ᵉ (ε > 0), (fun N => h N - (N : Real).sqrt) =O[atTop] fun N => (N : ℝ)^(ε : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L59).

## `Erdos30.erdos_30.variants.O_one`

Open: stated without proof.

> A stronger conjecture: is it true that $h(N) = \sqrt N + O(1)$?
> Erdős thought this was perhaps too optimistic.

```lean
theorem erdos_30.variants.O_one :
    (fun N => h N - (N : ℝ).sqrt) =O[atTop] fun _ => (1 : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L68).

## `Erdos30.erdos_30.variants.erdos_turan`

Solved: stated here without proof.

> Erdős and Turán [ErTu41] proved $h(N) \le \sqrt N + O(N^{1/4})$.
>
> This is an upper bound only. A statement with `=O` would also assert the lower bound
> $h(N) \ge \sqrt N - O(N^{1/4})$, which is not part of this result.

```lean
theorem erdos_30.variants.erdos_turan :
    ∃ C : ℝ, ∀ᶠ N in atTop, (h N : ℝ) ≤ (N : ℝ).sqrt + C * (N : ℝ) ^ (4⁻¹ : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L79).

## `Erdos30.erdos_30.variants.lindstrom`

Solved: stated here without proof.

> The proofs of Erdős–Turán [ErTu41] and Lindström [Li69] in fact give, for all $N$,
> $h(N) \le N^{1/2} + N^{1/4} + 1$.

```lean
theorem erdos_30.variants.lindstrom (N : ℕ) :
    (h N : ℝ) ≤ (N : ℝ).sqrt + (N : ℝ) ^ (4⁻¹ : ℝ) + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L88).

## `Erdos30.erdos_30.variants.balogh_furedi_roy`

Solved: stated here without proof.

> Balogh, Füredi and Roy [BFR23] proved $h(N) \le N^{1/2} + 0.998 N^{1/4}$ for all sufficiently
> large $N$.

```lean
theorem erdos_30.variants.balogh_furedi_roy :
    ∀ᶠ N in atTop, (h N : ℝ) ≤ (N : ℝ).sqrt + (0.998 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L97).

## `Erdos30.erdos_30.variants.obryant`

Solved: stated here without proof.

> O'Bryant [OB22] proved $h(N) \le N^{1/2} + 0.99703 N^{1/4}$ for all sufficiently large $N$.

```lean
theorem erdos_30.variants.obryant :
    ∀ᶠ N in atTop, (h N : ℝ) ≤ (N : ℝ).sqrt + (0.99703 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L105).

## `Erdos30.erdos_30.variants.carter_hunter_obryant`

Solved: stated here without proof.

> Carter, Hunter and O'Bryant [CHO25] proved $h(N) \le N^{1/2} + 0.98183 N^{1/4} + O(1)$.
> This is the current record upper bound.

```lean
theorem erdos_30.variants.carter_hunter_obryant :
    ∃ C : ℝ, ∀ᶠ N in atTop,
      (h N : ℝ) ≤ (N : ℝ).sqrt + (0.98183 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L114).

## `Erdos30.erdos_30.variants.singer`

Solved: stated here without proof.

> Singer's construction [Si38] shows $h(N) \ge (1 - o(1)) N^{1/2}$ for all $N$.

```lean
theorem erdos_30.variants.singer :
    ∀ ε > (0 : ℝ), ∀ᶠ N : ℕ in atTop, (1 - ε) * (N : ℝ).sqrt ≤ h N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L123).

## `Erdos30.erdos_30.variants.isEquivalent_sqrt`

Solved: stated here without proof.

> Combining Singer's lower bound [Si38] with the Erdős–Turán upper bound [ErTu41]:
> $h(N) \sim N^{1/2}$.

```lean
theorem erdos_30.variants.isEquivalent_sqrt :
    (fun N => (h N : ℝ)) ~[atTop] fun N => (N : ℝ).sqrt
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L132).

## `Erdos30.erdos_30.variants.elementary_difference_count`

Textbook result, proved here.

> The counting argument of Erdős and Turán [ErTu41]: a Sidon set $A \subseteq \{0, \dots, N\}$
> has $|A|(|A| - 1) \le 2N$, because the $|A|(|A|-1)/2$ positive differences of $A$ are distinct
> and lie in $\{1, \dots, N\}$.

```lean
theorem erdos_30.variants.elementary_difference_count (A : Finset ℕ) (N : ℕ)
    (hS : IsSidon (A : Set ℕ)) (hA : A ⊆ Finset.range (N + 1)) :
    A.card * (A.card - 1) ≤ 2 * N
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L142).

## `Erdos30.erdos_30.variants.distinct_sums_card`

Textbook result, proved here.

> For a Sidon set $A$, $|A + A| = |A|(|A|+1)/2$: the sums $a + b$ with $a \le b$ are pairwise
> distinct [ErTu41].

```lean
theorem erdos_30.variants.distinct_sums_card (A : Finset ℕ) (hS : IsSidon (A : Set ℕ)) :
    (A + A).card = A.card * (A.card + 1) / 2
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L165).

## `Erdos30.erdos_30.variants.distinct_sums_in_range`

Textbook result, proved here.

> If $A \subseteq \{0, \dots, N\}$ then $A + A \subseteq \{0, \dots, 2N\}$.

```lean
theorem erdos_30.variants.distinct_sums_in_range (A : Finset ℕ) (N : ℕ)
    (hA : A ⊆ Finset.range (N + 1)) :
    A + A ⊆ Finset.range (2 * N + 1)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 199](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L199).

## `Erdos30.erdos_30.variants.erdos_turan_counting`

Textbook result, proved here.

> The counting bound of Erdős and Turán [ErTu41] in its sum form: a Sidon set
> $A \subseteq \{0, \dots, N\}$ has $|A|(|A| + 1)/2 \le 2N + 1$.

```lean
theorem erdos_30.variants.erdos_turan_counting (A : Finset ℕ) (N : ℕ)
    (hS : IsSidon (A : Set ℕ)) (hA : A ⊆ Finset.range (N + 1)) :
    A.card * (A.card + 1) / 2 ≤ 2 * N + 1
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 210](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L210).

## `Erdos30.erdos_30.variants.lindstrom_weak`

Textbook result, proved here.

> A weak form of Lindström's bound [Li69], following from
> `erdos_30.variants.elementary_difference_count`: a Sidon set $A \subseteq \{0, \dots, N\}$
> has $|A| \le \lfloor \sqrt{2N} \rfloor + 1$.

```lean
theorem erdos_30.variants.lindstrom_weak (A : Finset ℕ) (N : ℕ)
    (hS : IsSidon (A : Set ℕ)) (hA : A ⊆ Finset.range (N + 1)) :
    A.card ≤ Nat.sqrt (2 * N) + 1
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/30.lean, line 222](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean#L222).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/30.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/30.lean)
- [erdosproblems.com/30](https://www.erdosproblems.com/30)
