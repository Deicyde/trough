---
declaration: theorem
origin: cited
lean: Green25.green_25, Green25.green_25.upper, Green25.green_25.lower, Green25.green_25.variants.lower_ess89, Green25.green_25.variants.upper_ess89, Green25.green_25.variants.upper_pow_23_40
statement: formalized
---

# Green's Open Problem 25

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.25)
> - [ESS89] Erdős, Pál, András Sárközy, and V. T. Sós. "On a conjecture of Roth and some related
>   problems I." Irregularities of partitions. Berlin, Heidelberg: Springer Berlin Heidelberg, 1989.
>   47-59.
> - [Ru04] Ruzsa, Imre Z. "A problem on restricted sumsets." CONTEMPORARY MATHEMATICS 342 (2004):
>   245-248.

*Quoted from [FormalConjectures/GreensOpenProblems/25.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 3 open and 3 solved.

## `Green25.green_25`

Open: stated without proof.

> For which values of $k$ is the following true: whenever we partition $[N] = A_1 \cup \dots \cup A_k$,
> $\left|\bigcup^k_{i=1} (A_i \hat{+} A_i)\right| \geq \frac{1}{10} N$?

```lean
theorem green_25 : {k : ℕ → ℕ | ∀ᶠ N in atTop, Property25 (k N) N} = green_25.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L60).

## `Green25.green_25.upper`

Open: stated without proof.

> We conjecture that the best-known upper bound can be lowered.

```lean
theorem green_25.upper :
    -- Ensure k is a valid partition size
    (∀ᶠ N in atTop, 1 ≤ green_25.upper.answer N ∧ green_25.upper.answer N ≤ N) ∧
    (fun N => (green_25.upper.answer N : ℝ)) =o[atTop] bestUpper ∧
    ¬ ∀ᶠ N in atTop, Property25 (green_25.upper.answer N) N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L67).

## `Green25.green_25.lower`

Open: stated without proof.

> We conjecture that the best-known lower bound can be raised.

```lean
theorem green_25.lower :
    (bestLower =o[atTop] green_25.lower.answer) ∧
    (∀ᶠ N in atTop, 1 ≤ green_25.lower.answer N ∧ green_25.lower.answer N ≤ N) ∧
    ∀ k : ℕ → ℕ,
      (∀ᶠ N in atTop, 1 ≤ k N ∧ k N ≤ N) ∧
      ((fun N => (k N : ℝ)) ≪ green_25.lower.answer) →
      ∀ᶠ N in atTop, Property25 (k N) N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L78).

## `Green25.green_25.variants.lower_ess89`

Solved: stated here without proof.

> For $k \ll \log \log N$, this is true [Gr24].
>
> NOTE: [ESS89] derive a precise constant for which this is true, but $\ll$ would imply that it works
> for any constant. We thus prefer a little-o statement.

```lean
theorem green_25.variants.lower_ess89 :
  ∀ k : ℕ → ℕ,
    (∀ᶠ N in atTop, 1 ≤ k N ∧ k N ≤ N) ∧ -- Ensure Property25 is not False due to non-existent partitions
    (fun N => (k N : ℝ)) =o[atTop] bestLower →
    ∀ᶠ N in atTop, Property25 (k N) N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L94).

## `Green25.green_25.variants.upper_ess89`

Solved: stated here without proof.

> For $k \gg N / \log N$, it need not be true [Gr24].
>
> We formalize by enforcing a $N / \log N$ growth rate on $k(N)$. This avoids cases like $k(N) = N$
> or $N-1$, which produce trivial counter examples with singletons and thus empty restricted sumsets.

```lean
theorem green_25.variants.upper_ess89 :
  ∃ k : ℕ → ℕ,
    (∀ᶠ N in atTop, 1 ≤ k N ∧ k N ≤ N) ∧
    (fun N => (k N : ℝ)) =Θ[atTop] bestUpper ∧
    ¬ ∀ᶠ N in atTop, Property25 (k N) N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L108).

## `Green25.green_25.variants.upper_pow_23_40`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/green-25-upper-bound/blob/3a54a688dfc4d7b9c8990bbaeb1a124c075454e4/lean/Green25UpperFC.lean#L3043-L3051](https://github.com/KitaKen1/green-25-upper-bound/blob/3a54a688dfc4d7b9c8990bbaeb1a124c075454e4/lean/Green25UpperFC.lean#L3043-L3051).

> For $k(N) = \lceil N^{23/40} \rceil$, it need not be true: for all sufficiently large $N$
> there is a partition of $[N]$ into $\lceil N^{23/40} \rceil$ parts with
> $\left|\bigcup^k_{i=1} (A_i \hat{+} A_i)\right| < \frac{1}{10} N$.
> In particular, the best-known upper bound $N / \log N$ can be lowered.

```lean
theorem green_25.variants.upper_pow_23_40 :
    let k : ℕ → ℕ := fun N => Nat.ceil ((N : ℝ) ^ (23 / 40 : ℝ))
    (∀ᶠ N in atTop, 1 ≤ k N ∧ k N ≤ N) ∧
    (fun N => (k N : ℝ)) =o[atTop] bestUpper ∧
    ∀ᶠ N in atTop, ¬ Property25 (k N) N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/25.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean#L125).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/25.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/25.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.25)
