---
declaration: lemma
origin: cited
lean: Erdos124.erdos124.zero, Erdos124.erdos124.ne_zero, Erdos124.erdos124.ne_zero_three_four_seven, Erdos124.erdos124.converse, Erdos124.erdos124.melfi_construction
statement: formalized
---

# Erdős Problem 124

> *References:*
> - [erdosproblems.com/124](https://www.erdosproblems.com/124)
> - [BEGL96] Burr, S. A. and Erdős, P. and Graham, R. L. and Li, W. Wen-Ching, Complete sequences of sets of integer powers. Acta Arith. (1996), 133-138.

*Quoted from [FormalConjectures/ErdosProblems/124.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/124](https://www.erdosproblems.com/124).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos124.erdos124.zero`

Solved: stated here without proof.

> Let  $3 \le d_1 < d_2 < \dots < d_r$ be integers such that
>
> $$\sum_{1 \le i \le r}\frac 1{d_i - 1} \ge 1.$$
>
> Can all sufficiently large integers be written as a sum of the shape $\sum_i c_ia_i$
> where $c_i \in \{0, 1\}$ and $a_i$ has only the digits $0, 1$ when written in base $d_i$?
>
> Conjectured by Erdős [Er97], solved by Boris Alexeev using Aristotle.

```lean
lemma erdos124.zero :
    ∀ D : Finset ℕ, (∀ d ∈ D, 3 ≤ d) → 1 ≤ ∑ d ∈ D, (d - 1 : ℚ)⁻¹ →
      ∀ᶠ n in atTop, n ∈ ∑ d ∈ D, sumsOfDistinctPowers d 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/124.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean#L48).

## `Erdos124.erdos124.ne_zero`

Open: stated without proof.

> Let $k \ne 0$ and $3\leq d_1 < d_2 < \cdots < d_r$ be integers of gcd equal to $1$ such that
>
> $$\sum_{1 \le i \le r}\frac 1{d_i - 1} \ge 1.$$
>
> Can all sufficiently large integers be written as a sum of the shape $\sum_i c_ia_i$
> where $c_i \in \{0, 1\}$ and $a_i$ is divisible by $d_i ^ k$ and has only the digits $0, 1$ when
> written in base $d_i$?
>
> Conjectured by Burr, Erdős, Graham, and Li [BEGL96]

```lean
lemma erdos124.ne_zero :
    ∀ k ≠ 0, ∀ D : Finset ℕ, (∀ d ∈ D, 3 ≤ d) → 1 ≤ ∑ d ∈ D, (d - 1 : ℚ)⁻¹ → D.gcd id = 1 →
      ∀ᶠ n in atTop, n ∈ ∑ d ∈ D, sumsOfDistinctPowers d k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/124.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean#L62).

## `Erdos124.erdos124.ne_zero_three_four_seven`

Solved: stated here without proof.

> All sufficiently large integers can be written as $a + b + c$, where $a$, $b$, and $c$ are
> divisible by $3$, $4$, and $7$ respectively, and after division by that base have only the
> digits $0, 1$ in that base.
>
> Proved by Burr, Erdős, Graham, and Li [BEGL96]

```lean
lemma erdos124.ne_zero_three_four_seven :
    ∀ᶠ n in atTop,
      n ∈ sumsOfDistinctPowers 3 1 + sumsOfDistinctPowers 4 1 + sumsOfDistinctPowers 7 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/124.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean#L75).

## `Erdos124.erdos124.converse`

Solved: stated here; a Lean proof is at [https://github.com/arex1337/formal-conjectures-proofs/blob/3b7d581c75fd00e482deabfb20675cf3ccfaf49f/Erdos124/Converse.lean](https://github.com/arex1337/formal-conjectures-proofs/blob/3b7d581c75fd00e482deabfb20675cf3ccfaf49f/Erdos124/Converse.lean).

> Let $3\leq d_1 < d_2 < \cdots < d_r$ be integers such that all sufficiently large integers can be
> written as a sum of the shape $\sum_i c_ia_i$ where $c_i \in \{0, 1\}$ and $a_i$ has only the digits
> $0, 1$ when written in base $d_i$. Then
>
> $$\sum_{1 \le i \le r}\frac 1{d_i - 1} \ge 1.$$
>
> Reported by Burr, Erdős, Graham, and Li [BEGL96] as an observation of Pomerance

```lean
lemma erdos124.converse {D : Finset ℕ} (hD₃ : ∀ d ∈ D, 3 ≤ d)
    (h : ∀ᶠ n in atTop, n ∈ ∑ d ∈ D, sumsOfDistinctPowers d 0) : 1 ≤ ∑ d ∈ D, (d - 1 : ℚ)⁻¹
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/124.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean#L91).

## `Erdos124.erdos124.melfi_construction`

Solved: stated here without proof.

> For any $\varepsilon > 0$, there exists an infinite sequence $2 \le d_0 < d_1 < \dots$ such
> that the series $\sum_{i=0}^{\infty} \frac{1}{d_i - 1}$ converges to a value at most
> $\varepsilon$, and yet for every $k \ne 0$ all sufficiently large integers can be written as
> $\sum_{i \in I} a_i$ for some finite set $I$, where each $a_i$ is divisible by $d_i^k$ and has
> only the digits $0, 1$ when written in base $d_i$.
>
> The restriction $k \ne 0$ excludes the degenerate representation of $n$ as a sum of $n$ copies
> of $1 = d_i^0$ taken from $n$ distinct bases.
>
> Proved by Melfi [Me04, Proposition 1]

```lean
lemma erdos124.melfi_construction {ε : ℝ} (hε : 0 < ε) :
    ∃ d : ℕ → ℕ, StrictMono d ∧ 2 ≤ d 0 ∧
      Summable (fun i ↦ (d i - 1 : ℝ)⁻¹) ∧ ∑' i, (d i - 1 : ℝ)⁻¹ ≤ ε ∧ ∀ k ≠ 0, ∀ᶠ n in atTop,
      ∃ (I : Finset ℕ) (a : ℕ → ℕ), (∀ i ∈ I, a i ∈ sumsOfDistinctPowers (d i) k) ∧
        ∑ i ∈ I, a i = n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/124.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/124.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/124.lean)
- [erdosproblems.com/124](https://www.erdosproblems.com/124)
