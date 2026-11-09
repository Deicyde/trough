---
declaration: theorem
origin: cited
lean: Erdos804.erdos_804.parts.i, Erdos804.erdos_804.parts.ii, Erdos804.erdos_804.variants.alon_sudakov
statement: formalized
---

# Erdős Problem 804

> *References:*
> - [erdosproblems.com/804](https://www.erdosproblems.com/804)
> - [Er91] Erdős, P., _Problems and results in combinatorial analysis and combinatorial number
>   theory_. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [AlSu07] Alon, Noga and Sudakov, Benny, _On graphs with subgraphs having large independence
>   numbers_. J. Graph Theory (2007), 149-157.

*Quoted from [FormalConjectures/ErdosProblems/804.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/804.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/804](https://www.erdosproblems.com/804).

The file states 3 research or textbook statements: 3 solved.

## `Erdos804.erdos_804.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532).

> Let $f(m,n)$ be maximal such that any graph on $n$ vertices in which every induced subgraph on
> $m$ vertices has an independent set of size at least $\log n$ must contain an independent set of
> size at least $f(n)$.
>
> Estimate $f(n)$. In particular, is it true that $f((\log n)^2,n) \geq n^{1/2-o(1)}$?
>
> The answer is no: Alon and Sudakov [AlSu07] proved that in fact
>
> $$\frac{(\log n)^2}{\log\log n}\ll f((\log n)^2,n) \ll (\log n)^2.$$

```lean
theorem erdos_804.parts.i :
    ¬ ∀ ε > 0, ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ (1 / 2 - ε : ℝ) ≤ f ⌊(log n) ^ 2⌋₊ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/804.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/804.lean#L62).

## `Erdos804.erdos_804.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532).

> Is it true that $f((\log n)^3,n)\gg (\log n)^3$?
>
> The answer is no: Alon and Sudakov [AlSu07] proved that in fact
>
> $$f((\log n)^3,n)\asymp \frac{(\log n)^2}{\log\log n}.$$

```lean
theorem erdos_804.parts.ii :
    ¬ ∃ c > 0, ∀ᶠ n : ℕ in atTop, c * (log n) ^ 3 ≤ f ⌊(log n) ^ 3⌋₊ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/804.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/804.lean#L76).

## `Erdos804.erdos_804.variants.alon_sudakov`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos804.lean#L3532).

> Alon and Sudakov [AlSu07] proved that
>
> $$\frac{(\log n)^2}{\log\log n}\ll f((\log n)^2,n) \ll (\log n)^2$$
>
> and
>
> $$f((\log n)^3,n)\asymp \frac{(\log n)^2}{\log\log n}.$$

```lean
theorem erdos_804.variants.alon_sudakov :
    ∃ c₂ C₂ c₃ C₃ : ℝ, 0 < c₂ ∧ 0 < C₂ ∧ 0 < c₃ ∧ 0 < C₃ ∧
    ∀ᶠ n : ℕ in atTop,
      c₂ * ((log n) ^ 2 / log (log n)) ≤ f ⌊(log n) ^ 2⌋₊ n ∧
      (f ⌊(log n) ^ 2⌋₊ n : ℝ) ≤ C₂ * (log n) ^ 2 ∧
      c₃ * ((log n) ^ 2 / log (log n)) ≤ f ⌊(log n) ^ 3⌋₊ n ∧
      (f ⌊(log n) ^ 3⌋₊ n : ℝ) ≤ C₃ * ((log n) ^ 2 / log (log n))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/804.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/804.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/804.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/804.lean)
- [erdosproblems.com/804](https://www.erdosproblems.com/804)
