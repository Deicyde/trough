---
declaration: theorem
origin: cited
lean: Erdos1050.erdos_1050, Erdos1050.erdos_1050.variants.two_pow_sub_one, Erdos1050.erdos_1050.variants.borwein, Erdos1050.erdos_1050.variants.transcendental
statement: formalized
---

# Erdős Problem 1050

> *References:*
> - [erdosproblems.com/1050](https://www.erdosproblems.com/1050)
> - [Bo91] Borwein, Peter B., On the irrationality of {$\sum(1/(q^n+r))$}. J. Number Theory (1991), 253--259.
> - [Bo92] Borwein, Peter B., On the irrationality of certain series. Math. Proc. Camb. Phil. Soc. (1992), 141--146.
> - [Er48] Erdős, P., On arithmetical properties of Lambert series. J. Indian Math. Soc. (N.S.) (1948), 63-66.
> - [Er88c] Erdős, P., On the irrationality of certain series: problems and results. New advances in transcendence theory (Durham, 1986) (1988), 102-109.
>
> Is $\sum_{n=1}^\infty \frac{1}{2^n - 3}$ irrational?
>
> The answer is **yes**, proved by P. B. Borwein [Bo91] (with a cleaner self-contained proof in [Bo92]),
> specialized to $q = 2$, $r = -3$.
>
> A formal Lean proof is given in an external repository,
> [`gotrevor/lean-gallery`](https://github.com/gotrevor/lean-gallery), formalized by Trevor Morris with
> Claude Code and Harmonic's Aristotle.

*Quoted from [FormalConjectures/ErdosProblems/1050.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1050](https://www.erdosproblems.com/1050).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos1050.erdos_1050`

Solved: stated here; a Lean proof is at [https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Statement.lean](https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Statement.lean).

> **Erdős Problem 1050.** The series $\sum_{n=1}^\infty \frac{1}{2^n - 3}$ is irrational.
>
> The source sum runs over $n \ge 1$; as a `tsum` over `ℕ` (which starts at $0$) it is reindexed
> $n \mapsto n + 1$, i.e. $\sum_{n=0}^\infty 1/(2^{n+1} - 3)$.

```lean
theorem erdos_1050 : Irrational (∑' n : ℕ, (1 : ℝ) / ((2 : ℝ) ^ (n + 1) - 3))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1050.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean#L52).

## `Erdos1050.erdos_1050.variants.two_pow_sub_one`

Solved: stated here; a Lean proof is at [https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Variants.lean](https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Variants.lean).

> **Erdős Problem 1050, variant [Er48].** Erdős proved that the related series
> $\sum_{n=1}^\infty \frac{1}{2^n - 1}$ (which equals the Lambert series $\sum_n \frac{\tau(n)}{2^n}$,
> where $\tau$ is the divisor function) is irrational. This is the $q = 2$, $r = -1$ case of Borwein's
> general theorem `Erdos1050.erdos_1050.variants.borwein` below.

```lean
theorem erdos_1050.variants.two_pow_sub_one :
    Irrational (∑' n : ℕ, (1 : ℝ) / ((2 : ℝ) ^ (n + 1) - 1))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1050.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean#L63).

## `Erdos1050.erdos_1050.variants.borwein`

Solved: stated here; a Lean proof is at [https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Variants.lean](https://github.com/gotrevor/lean-gallery/blob/main/LeanGallery/NumberTheory/Erdos1050/Variants.lean).

> **Erdős Problem 1050, variant [Bo91].** Borwein's general theorem: for every integer $q \ge 2$
> and rational $r \ne 0$ with $r \ne -q^n$ for all $n \ge 1$, the series $\sum_{n=1}^\infty \frac{1}{q^n + r}$
> is irrational. Problem 1050 is the case $q = 2$, $r = -3$; the [Er48] variant is $q = 2$, $r = -1$.

```lean
theorem erdos_1050.variants.borwein (q : ℤ) (hq : 2 ≤ q) (r : ℚ) (hr : r ≠ 0)
    (hne : ∀ n : ℕ, 1 ≤ n → r ≠ -((q : ℚ) ^ n)) :
    Irrational (∑' n : ℕ, (1 : ℝ) / ((q : ℝ) ^ (n + 1) + (r : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1050.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean#L74).

## `Erdos1050.erdos_1050.variants.transcendental`

Open: stated without proof.

> **Erdős Problem 1050, variant [Er88c] (open).** Erdős conjectured that
> $\sum_{n=1}^\infty \frac{1}{2^n + t}$ is *transcendental* for every integer $t \ne 0$ — strictly
> stronger than the irrationality established by Borwein [Bo91]. This remains open.
>
> Two exclusions make the series well-posed and the claim non-vacuous, exactly as in Borwein's theorem:
> $t \ne -2^n$ for all $n \ge 1$ (so no denominator vanishes), and $t \ne 0$ (at $t = 0$ the series is
> the rational $\sum_{n \ge 1} 2^{-n} = 1$, hence not transcendental).

```lean
theorem erdos_1050.variants.transcendental :
    ∀ t : ℤ, t ≠ 0 → (∀ n : ℕ, 1 ≤ n → t ≠ -(2 : ℤ) ^ n) →
      Transcendental ℚ (∑' n : ℕ, (1 : ℝ) / ((2 : ℝ) ^ (n + 1) + (t : ℝ)))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1050.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1050.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1050.lean)
- [erdosproblems.com/1050](https://www.erdosproblems.com/1050)
