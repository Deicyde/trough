---
declaration: theorem
origin: cited
lean: Erdos1.erdos_1, Erdos1.erdos_1.variants.weaker, Erdos1.erdos_1.variants.lb, Erdos1.erdos_1.variants.lb_strong, Erdos1.erdos_1.variants.real, Erdos1.erdos_1.variants.least_N_3, Erdos1.erdos_1.variants.least_N_4, Erdos1.erdos_1.variants.least_N_5, Erdos1.erdos_1.variants.least_N_9
statement: formalized
---

# Erdős Problem 1

> *Reference:* [erdosproblems.com/1](https://www.erdosproblems.com/1)

*Quoted from [FormalConjectures/ErdosProblems/1.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1](https://www.erdosproblems.com/1).

The file states 9 research or textbook statements: 6 solved and 3 textbook results.

## `Erdos1.erdos_1`

Solved: stated here; a Lean proof is at [https://github.com/tadamcz/erdos1/blob/0e395153306f34b3829d118b85bdd704136f2843/Erdos1/Resolutions/Erdos1_219usd_38h.lean#L2419](https://github.com/tadamcz/erdos1/blob/0e395153306f34b3829d118b85bdd704136f2843/Erdos1/Resolutions/Erdos1_219usd_38h.lean#L2419).

> If $A\subseteq\{1, ..., N\}$ with $|A| = n$ is such that the subset sums $\sum_{a\in S}a$ are
> distinct for all $S\subseteq A$ then
> $$
>   N \gg 2 ^ n.
> $$
>
> This conjecture is false. A machine-checked disproof constructs sum-distinct sets for which
> $N / 2^n$ tends to zero.

```lean
theorem erdos_1 : ¬ ∃ C > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℕ) (_ : IsSumDistinctSet A N),
    N ≠ 0 → C * 2 ^ A.card < N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L54).

## `Erdos1.erdos_1.variants.weaker`

Textbook result, proved here.

> The trivial lower bound is $N \gg 2^n / n$.

```lean
theorem erdos_1.variants.weaker : ∃ C > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℕ)
    (_ : IsSumDistinctSet A N), N ≠ 0 → C * 2 ^ A.card / A.card < N
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L62).

## `Erdos1.erdos_1.variants.lb`

Solved: stated here without proof.

> Erdős and Moser [Er56] proved
> $$
>   N \geq (\tfrac{1}{4} - o(1)) \frac{2^n}{\sqrt{n}}.
> $$
>
> [Er56] Erdős, P., _Problems and results in additive number theory_. Colloque sur la Th\'{E}orie des Nombres, Bruxelles, 1955 (1956), 127-137.

```lean
theorem erdos_1.variants.lb : ∃ (o : ℕ → ℝ) (_ : o =o[atTop] (1 : ℕ → ℝ)),
    ∀ (N : ℕ) (A : Finset ℕ) (h : IsSumDistinctSet A N),
      (1 / 4 - o A.card) * 2 ^ A.card / (A.card : ℝ).sqrt ≤ N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L91).

## `Erdos1.erdos_1.variants.lb_strong`

Solved: stated here; a Lean proof is at [https://github.com/MyTH-zyxeon/formal-conjectures/blob/362eed1a8864d142ae65f51af7981a7c7530956e/FormalConjectures/Scratch/HarperCompression.lean#L2174](https://github.com/MyTH-zyxeon/formal-conjectures/blob/362eed1a8864d142ae65f51af7981a7c7530956e/FormalConjectures/Scratch/HarperCompression.lean#L2174).

> A number of improvements of the constant $\frac{1}{4}$ have been given, with the current
> record $\sqrt{2 / \pi}$ first provided in unpublished work of Elkies and Gleason.

```lean
theorem erdos_1.variants.lb_strong : ∃ (o : ℕ → ℝ) (_ : o =o[atTop] (1 : ℕ → ℝ)),
    ∀ (N : ℕ) (A : Finset ℕ) (h : IsSumDistinctSet A N),
      (√(2 / π) - o A.card) * 2 ^ A.card / (A.card : ℝ).sqrt ≤ N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L104).

## `Erdos1.erdos_1.variants.real`

Proved here.

> A generalisation of the problem to sets $A \subseteq (0, N]$ of real numbers, such that the subset
> sums all differ by at least $1$ is proposed in [Er73] and [ErGr80].
>
> The positive statement is false: every natural-number counterexample to `erdos_1` embeds into
> $\mathbb{R}$, and distinct integer subset sums differ by at least one.
>
> [Er73] Erdős, P., _Problems and results on combinatorial number theory_. A survey of combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.
>
> [ErGr80] Erdős, P. and Graham, R., _Old and new problems and results in combinatorial number theory_. Monographies de L'Enseignement Mathematique (1980).

```lean
theorem erdos_1.variants.real : ¬ ∃ C > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℝ)
    (_ : IsSumDistinctRealSet A N), N ≠ 0 → C * 2 ^ A.card < N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L129).

## `Erdos1.erdos_1.variants.least_N_3`

Textbook result, proved here.

> The minimal value of $N$ such that there exists a sum-distinct set with three
> elements is $4$.
>
> https://oeis.org/A276661

```lean
theorem erdos_1.variants.least_N_3 :
    IsLeast { N | ∃ A, IsSumDistinctSet A N ∧ A.card = 3 } 4
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 230](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L230).

## `Erdos1.erdos_1.variants.least_N_4`

Textbook result, proved here.

> The minimal value of $N$ such that there exists a sum-distinct set with four
> elements is $7$.
>
> https://oeis.org/A276661

```lean
theorem erdos_1.variants.least_N_4 :
    IsLeast { N | ∃ A, IsSumDistinctSet A N ∧ A.card = 4 } 7
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 261](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L261).

## `Erdos1.erdos_1.variants.least_N_5`

Proved here.

> The minimal value of $N$ such that there exists a sum-distinct set with five
> elements is $13$.
>
> https://oeis.org/A276661

```lean
theorem erdos_1.variants.least_N_5 :
    IsLeast { N | ∃ A, IsSumDistinctSet A N ∧ A.card = 5 } 13
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 282](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L282).

## `Erdos1.erdos_1.variants.least_N_9`

Solved: stated here without proof.

> The minimal value of $N$ such that there exists a sum-distinct set with nine
> elements is $161$.
>
> https://oeis.org/A276661

```lean
theorem erdos_1.variants.least_N_9 :
    IsLeast { N | ∃ A, IsSumDistinctSet A N ∧ A.card = 9 } 161
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1.lean, line 303](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean#L303).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1.lean)
- [erdosproblems.com/1](https://www.erdosproblems.com/1)
