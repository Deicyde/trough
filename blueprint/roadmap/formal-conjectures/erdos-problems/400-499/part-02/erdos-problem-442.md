---
declaration: theorem
origin: cited
lean: Erdos442.erdos_442, Erdos442.erdos_442.variants.tao
statement: formalized
---

# Erdős Problem 442

> *Reference:* [erdosproblems.com/442](https://www.erdosproblems.com/442)

*Quoted from [FormalConjectures/ErdosProblems/442.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/442.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/442](https://www.erdosproblems.com/442).

The file states 2 research or textbook statements: 2 solved.

## `Erdos442.erdos_442`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos442.lean#L995](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos442.lean#L995).

> Let $\operatorname{Log} x := \max\{\log x, 1\}$,
> $\operatorname{Log}_2x = \operatorname{Log} (\operatorname{Log} x)$, and
> $\operatorname{Log}_3x = \operatorname{Log}(\operatorname{Log}(\operatorname{Log} x)).$
> Is it true that if $A\subseteq\mathbb{N}$ is such that
> $$
> \frac{1}{\operatorname{Log}_2 x} \sum_{n\in A: n\leq x} \frac{1}{n}\to\infty
> $$
> then
> $$
> \left(\sum_{n\in A: n\leq x} \frac{1}{n}\right)^2 \sum_{n, m \in A: n < m \leq x}
> \frac{1}{\operatorname{lcm}(n, m)}\to\infty
> $$
> as $x\to\infty$?
>
> Tao [Ta24b] has shown this is false.
>
> [Ta24b] Tao, T., _Dense sets of natural numbers with unusually large least common multiples_.
> arXiv:2407.04226 (2024).
>
> Note: the informal and formal statements follow the solution paper https://arxiv.org/pdf/2407.04226

```lean
theorem erdos_442 : ¬ ∀ (A : Set ℕ),
    Tendsto (fun (x : ℝ) =>
      1 / x.maxLogOne.maxLogOne * ∑ n ∈ (A ∩ Icc 1 ⌊x⌋₊ : Set ℕ), (1 : ℝ) / n) atTop atTop →
    Tendsto (fun (x : ℝ) => 1 / (∑ n ∈ (A ∩ Icc 1 ⌊x⌋₊ : Set ℕ), (1 : ℝ) / n) ^ 2 *
      ∑ nm ∈ A.bddProdUpper x, (1 : ℝ) / nm.1.lcm nm.2) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/442.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/442.lean#L89).

## `Erdos442.erdos_442.variants.tao`

Solved: stated here without proof.

> Tao resolved erdos_442 in the negative in Theorem 1 of https://arxiv.org/pdf/2407.04226.
> The following is a formalisation of that theorem with $C_0 = 1$.
>
> Let $\operatorname{Log} x := \max\{\log x, 1\}$,
> $\operatorname{Log}_2x = \operatorname{Log} (\operatorname{Log} x)$, and
> $\operatorname{Log}_3x = \operatorname{Log}(\operatorname{Log}(\operatorname{Log} x)).$
> There exists a set $A$ of natural numbers such that
> $$
> \sum_{n\in A: n\leq x} \frac{1}{n} =
>   \exp\left(\left(\left(\frac{1}{2} + o(1)\right)\operatorname{Log}_2^{1/2}x \operatorname{Log}_3x\right)\right)
> $$
> and
> $$
> \sum_{n, m\in A: n, m\leq x} \frac{1}{\operatorname{lcm}(n, m)}\ll\left(\sum_{n\in A: n\leq x} \frac{1}{n}\right)^2
> $$

```lean
theorem erdos_442.variants.tao :
    ∃ (A : Set ℕ) (f : ℝ → ℝ) (C: ℝ) (hC : 0 < C) (hf : f =o[atTop] (1 : ℝ → ℝ)),
      ∀ᶠ (x : ℝ) in atTop,
        ∑ n ∈ (A ∩ Icc 1 ⌊x⌋₊ : Set ℕ), (1 : ℝ) / n =
          Real.exp ((1 / 2 + f x) * √x.maxLogOne.maxLogOne * x.maxLogOne.maxLogOne.maxLogOne) ∧
        |∑ nm ∈ ((A ∩ Icc 1 ⌊x⌋₊) ×ˢ (A ∩ Icc 1 ⌊x⌋₊)).toFinset, (1 : ℝ) / nm.1.lcm nm.2| ≤
          C * (∑ n ∈ (A ∩ Icc 1 ⌊x⌋₊ : Set ℕ), (1 : ℝ) / n) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/442.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/442.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/442.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/442.lean)
- [erdosproblems.com/442](https://www.erdosproblems.com/442)
