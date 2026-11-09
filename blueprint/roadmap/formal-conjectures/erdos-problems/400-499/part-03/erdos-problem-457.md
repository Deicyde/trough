---
declaration: theorem
origin: cited
lean: Erdos457.erdos_457, Erdos457.erdos_457.variants.qnk, Erdos457.erdos_457.variants.one_sub
statement: formalized
---

# Erdős Problem 457

> *Reference:* [erdosproblems.com/457](https://www.erdosproblems.com/457)

*Quoted from [FormalConjectures/ErdosProblems/457.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/457.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/457](https://www.erdosproblems.com/457).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos457.erdos_457`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem457.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem457.lean).

> Is there some $\epsilon > 0$ such that there are infinitely
> many $n$ where all primes $p \le (2 + \epsilon) \log n$ divide
>
> $$
>   \prod_{1 \le i \le \log n} (n + i)?
> $$
>
> This was formalized in Lean by Baretto and van Doorn using Aristotle.

```lean
theorem erdos_457 : ∃ ε > (0 : ℝ),
    { (n : ℕ) | ∀ (p : ℕ), p ≤ (2 + ε) * Real.log n → p.Prime →
      p ∣ ∏ i ∈ Finset.Icc 1 ⌊Real.log n⌋₊, (n + i) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/457.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/457.lean#L41).

## `Erdos457.erdos_457.variants.qnk`

Proved here.

> More generally, let $q(n, k)$ denote the least prime which
> does not divide $\prod_{1 \le i \le k}(n + i)$. This
> problem asks whether $q(n, \log n) \ge (2 + \epsilon) \log n$
> infinitely often.
>
> This follows from `erdos_457`: if every prime $p \le (2 + \epsilon) \log n$
> divides $\prod_{1 \le i \le \log n} (n + i)$, then $q(n, \log n)$, the least
> prime not dividing this product, must exceed $(2 + \epsilon) \log n$.

```lean
theorem erdos_457.variants.qnk : ∃ ε > (0 : ℝ),
    { (n : ℕ) | (2 + ε) * Real.log n ≤ q n (Real.log n) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/457.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/457.lean#L63).

## `Erdos457.erdos_457.variants.one_sub`

Open: stated without proof.

> Taking $n$ to be the product of primes
> between $\log n$ and $(2 + o(1)) \log n$ gives an example where
>
> $$
>   q(n, \log n) \ge (2 + o(1)) \log n.
> $$
>
> Can one prove that $q(n, \log n) < (1 - \epsilon) (\log n)^2$
> for all large $n$ and some $\epsilon > 0$?

```lean
theorem erdos_457.variants.one_sub : ∃ ε > (0 : ℝ),
    ∀ᶠ n in Filter.atTop, q n (Real.log n) < (1 - ε) * Real.log n ^ 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/457.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/457.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/457.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/457.lean)
- [erdosproblems.com/457](https://www.erdosproblems.com/457)
