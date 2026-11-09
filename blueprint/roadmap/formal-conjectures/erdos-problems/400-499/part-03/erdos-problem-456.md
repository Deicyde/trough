---
declaration: theorem
origin: cited
lean: Erdos456.erdos_456.parts.i, Erdos456.erdos_456.parts.ii, Erdos456.erdos_456.parts.iii, Erdos456.erdos_456.variants.linniks_theorem, Erdos456.erdos_456.variants.mn_leq_pn, Erdos456.erdos_456.variants.infinitely_many_n, Erdos456.erdos_456.variants.m_div_n
statement: formalized
---

# Erdős Problem 456

> *References:*
> - [erdosproblems.com/456](https://www.erdosproblems.com/456)
> - [Er79e] Erdős, Paul, Some unconventional problems in number theory. Astérisque (1979), 73--82.

*Quoted from [FormalConjectures/ErdosProblems/456.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/456](https://www.erdosproblems.com/456).

The file states 7 research or textbook statements: 3 open, 3 solved and 1 textbook result.

## `Erdos456.erdos_456.parts.i`

Open: stated without proof.

> Is it true that $m_n\lt p_n$ for almost all $n$?

```lean
theorem erdos_456.parts.i :
    Tendsto (fun N ↦ (count (fun n ↦ m n < p n) N : ℝ) / (N : ℝ)) atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L52).

## `Erdos456.erdos_456.parts.ii`

Open: stated without proof.

> Does $p_n/m_n \to \infty$ for almost all $n$?

```lean
theorem erdos_456.parts.ii :
    ∃ A : Set ℕ, Tendsto (fun N ↦ (count (· ∈ A) N : ℝ) / (N : ℝ)) atTop (𝓝 1) ∧
      Tendsto (fun n ↦ (p n : ℝ) / (m n : ℝ)) (atTop ⊓ 𝓟 A) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L61).

## `Erdos456.erdos_456.parts.iii`

Open: stated without proof.

> Are there infinitely many primes $p$ such that $p-1$ is the only $n$ for which $m_n=p$?

```lean
theorem erdos_456.parts.iii :
    { q | q.Prime ∧ ∀ n, m n = q ↔ n = q - 1 }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L70).

## `Erdos456.erdos_456.variants.linniks_theorem`

Solved: stated here without proof.

> Linnik's theorem implies that $p_n\leq n^{O(1)}$.

```lean
theorem erdos_456.variants.linniks_theorem :
    ∃ L : ℝ, (fun n ↦ (p n : ℝ)) =O[atTop] (fun n ↦ (n : ℝ) ^ L)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L78).

## `Erdos456.erdos_456.variants.mn_leq_pn`

Textbook result, proved here.

> It is trivial that $m_n \leq p_n$ always.

```lean
theorem erdos_456.variants.mn_leq_pn (n : ℕ) :
    m n ≤ p n
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L86).

## `Erdos456.erdos_456.variants.infinitely_many_n`

Proved here.

> Erdős [Er79e] writes it is 'easy to show' that for infinitely many $n$ we have $m_n < p_n$.

```lean
theorem erdos_456.variants.infinitely_many_n :
    { n | m n < p n }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L114).

## `Erdos456.erdos_456.variants.m_div_n`

Solved: stated here without proof.

> Erdős [Er79e] writes it is 'easy to show' that $m_n/n \to \infty$ for almost all $n$.

```lean
theorem erdos_456.variants.m_div_n :
    ∃ A : Set ℕ, Tendsto (fun N ↦ (count (· ∈ A) N : ℝ) / N) atTop (𝓝 1) ∧
      Tendsto (fun n ↦ (m n : ℝ) / (n : ℝ)) (atTop ⊓ 𝓟 A) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/456.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean#L161).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/456.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/456.lean)
- [erdosproblems.com/456](https://www.erdosproblems.com/456)
