---
declaration: theorem
origin: cited
lean: Erdos308.erdos_308.parts.i, Erdos308.erdos_308.parts.ii, Erdos308.erdos_308.variants.shape, Erdos308.erdos_308.variants.croot, Erdos308.erdos_308.variants.all_N
statement: formalized
---

# Erdős Problem 308

> *References:*
> - [erdosproblems.com/308](https://www.erdosproblems.com/308)
> - [ErGr80] Erdős, P. and Graham, R., _Old and new problems and results in combinatorial number
>   theory_. Monographies de L'Enseignement Mathematique (1980).
> - [Cr99] Croot, III, Ernest S., _On some questions of Erdős and Graham about Egyptian
>   fractions_. Mathematika (1999), 359-372.

*Quoted from [FormalConjectures/ErdosProblems/308.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/308](https://www.erdosproblems.com/308).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos308.erdos_308.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458).

> Let $N\geq 1$. What is the smallest integer not representable as the sum of distinct unit
> fractions with denominators from $\{1,\ldots,N\}$?
>
> This was essentially solved by Croot [Cr99] (see `erdos_308.variants.croot`); in particular,
> for all sufficiently large $N$, the smallest such integer is either $m_N$ or $m_N+1$, where
> $m_N=\lfloor \sum_{n\leq N}\frac{1}{n}\rfloor$.

```lean
theorem erdos_308.parts.i : ∀ᶠ N : ℕ in atTop, f N = m N ∨ f N = m N + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/308.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean#L64).

## `Erdos308.erdos_308.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458).

> Let $N\geq 1$. Is it true that the set of integers representable as the sum of distinct unit
> fractions with denominators from $\{1,\ldots,N\}$ has the shape $\{1,\ldots,m\}$ for some $m$?
>
> It follows from Croot's bounds [Cr99] that this holds for all sufficiently large $N$.

```lean
theorem erdos_308.parts.ii :
    ∀ᶠ N : ℕ in atTop, ∃ m, representable N = Set.Icc 1 m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/308.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean#L76).

## `Erdos308.erdos_308.variants.shape`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos308.lean#L458).

> If $m_N=\lfloor \sum_{n\leq N}\frac{1}{n}\rfloor$, then the set of integers representable is, for
> all $N$ sufficiently large, either $\{1,\ldots,m_N-1\}$ or $\{1,\ldots,m_N\}$.

```lean
theorem erdos_308.variants.shape : ∀ᶠ N : ℕ in atTop,
    representable N = Set.Icc 1 (m N - 1) ∨ representable N = Set.Icc 1 (m N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/308.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean#L87).

## `Erdos308.erdos_308.variants.croot`

Solved: stated here without proof.

> Croot [Cr99] bounded $\eta(N)$, the largest integer such that every integer in
> $\{1,\ldots,\eta(N)\}$ is representable; this is $f(N)-1$, so his bounds read
> $$\left\lfloor\sum_{n\leq N}\frac{1}{n}-\frac{9}{2}(1+o(1))\frac{(\log\log N)^2}{\log N}
> \right\rfloor + 1 \leq f(N)$$
> and
> $$f(N)\leq \left\lfloor\sum_{n\leq N}\frac{1}{n}-\frac{1}{2}(1+o(1))
> \frac{(\log\log N)^2}{\log N}\right\rfloor + 1.$$

```lean
theorem erdos_308.variants.croot :
    ∃ o₁ o₂ : ℕ → ℝ, Tendsto o₁ atTop (nhds 0) ∧ Tendsto o₂ atTop (nhds 0) ∧
      ∀ᶠ N : ℕ in atTop,
        ⌊(harmonic N : ℝ) - 9 / 2 * (1 + o₁ N) * (log (log N)) ^ 2 / log N⌋₊ + 1 ≤ f N ∧
        f N ≤ ⌊(harmonic N : ℝ) - 1 / 2 * (1 + o₂ N) * (log (log N)) ^ 2 / log N⌋₊ + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/308.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean#L101).

## `Erdos308.erdos_308.variants.all_N`

Open: stated without proof.

> Is it true that, for every $N\geq 1$, the set of integers representable as the sum of distinct
> unit fractions with denominators from $\{1,\ldots,N\}$ has the shape $\{1,\ldots,m\}$ for some
> $m$?

```lean
theorem erdos_308.variants.all_N :
    ∀ N ≥ 1, ∃ m, representable N = Set.Icc 1 m
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/308.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/308.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/308.lean)
- [erdosproblems.com/308](https://www.erdosproblems.com/308)
