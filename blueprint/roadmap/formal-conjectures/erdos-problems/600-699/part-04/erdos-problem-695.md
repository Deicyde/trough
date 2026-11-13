---
declaration: theorem
origin: cited
lean: Erdos695.erdos_695, Erdos695.erdos_695.variants.upperBound
statement: formalized
---

# Erdős Problem 695

> *Reference:* [erdosproblems.com/695](https://www.erdosproblems.com/695)

*Quoted from [FormalConjectures/ErdosProblems/695.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/695.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/695](https://www.erdosproblems.com/695).

The file states 2 research or textbook statements: 2 open.

## `Erdos695.erdos_695`

Open: stated without proof.

> Let $q_1 < q_2 < \cdots$ be a sequence of primes such that $q_{i + 1} \equiv 1 \pmod{q_i}$. Is it
> true that
>
> $$
> \lim_{k \to \infty} q_k^{1/k} = \infty?
> $$

```lean
theorem erdos_695 :
    ∀ {q : ℕ → ℕ},
      StrictMono q →
      (∀ i, (q i).Prime) →
      (∀ i, q (i + 1) % q i = 1) →
      Tendsto (fun k => (q k : ℝ) ^ (1 / k : ℝ)) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/695.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/695.lean#L39).

## `Erdos695.erdos_695.variants.upperBound`

Open: stated without proof.

> Is there a sequence of primes $q_1 < q_2 < \cdots$ such that $q_{i + 1} \equiv 1 \pmod{q_i}$ and
>
> $$
> q(k) \leq \exp(k (\log k)^{1 + o(1)})?
> $$

```lean
theorem erdos_695.variants.upperBound :
    ∃ q : ℕ → ℕ,
      StrictMono q ∧
      (∀ i, (q i).Prime) ∧
      (∀ i, q (i + 1) % q i = 1) ∧
      ∃ o : ℕ → ℝ,
        (o =o[atTop] (1 : ℕ → ℝ)) ∧
        -- We use `(k + 1)` here as the informal statement is 1-indexed.
        ∀ k, q k ≤ exp ((k + 1) * log (k + 1) ^ (1 + o k))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/695.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/695.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/695.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/695.lean)
- [erdosproblems.com/695](https://www.erdosproblems.com/695)
