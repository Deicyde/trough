---
declaration: theorem
origin: cited
lean: Erdos489.erdos_489, Erdos489.erdos_489.variants.squarefree
statement: formalized
---

# Erdős Problem 489

> *Reference:* [erdosproblems.com/489](https://www.erdosproblems.com/489)

*Quoted from [FormalConjectures/ErdosProblems/489.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/489.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/489](https://www.erdosproblems.com/489).

The file states 2 research or textbook statements: 2 solved.

## `Erdos489.erdos_489`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-489/F061/Erdos489.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-489/F061/Erdos489.lean).

> Let $A\subseteq \mathbb{N}$ be a set such that $\lvert A\cap [1,x]\rvert=o(x^{1/2})$. Let
> $B=\{ n\geq 1 : a\nmid n\textrm{ for all }a\in A\}$.
> If $B=\{b_1 < b_2 < \cdots\}$ then is it true that
>
> $$\lim_{x \to \infty} \frac{1}{x}\sum_{b_i < x}(b_{i+1}-b_i)^2$$
>
> exists (and is finite)?
>
> For example, when $A=\{p^2: p\textrm{ prime}\}$ then $B$ is the set of squarefree numbers,
> and the existence of this limit was proved by Erdős.
>
> See also [208].

```lean
theorem erdos_489 :
    ∀ (A : Set ℕ),
      (fun x : ℕ => (((Finset.Icc 1 x).filter (· ∈ A)).card : ℝ)) =o[atTop]
        (fun x : ℕ => (x : ℝ).sqrt) →
      (sievedSet A).Infinite →
      ∃ L : ℝ, Tendsto (fun x : ℕ => GapSumSq A x / (x : ℝ)) atTop (𝓝 L)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/489.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/489.lean#L59).

## `Erdos489.erdos_489.variants.squarefree`

Solved: stated here without proof.

> When $A = \{p^2 : p \textrm{ prime}\}$, $B$ is the set of squarefree numbers, and the
> existence of this limit was proved by Erdős. This is the $\alpha = 2$ case of Erdős Problem 145.

```lean
theorem erdos_489.variants.squarefree :
    ∃ L : ℝ, Tendsto
      (fun x : ℕ => GapSumSq {n | ∃ p, Nat.Prime p ∧ n = p ^ 2} x / (x : ℝ))
      atTop (𝓝 L)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/489.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/489.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/489.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/489.lean)
- [erdosproblems.com/489](https://www.erdosproblems.com/489)
