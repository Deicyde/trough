---
declaration: theorem
origin: cited
lean: Erdos845.erdos_845
statement: formalized
---

# Erdős Problem 845

> *Reference:* [erdosproblems.com/845](https://www.erdosproblems.com/845)

*Quoted from [FormalConjectures/ErdosProblems/845.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/845.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/845](https://www.erdosproblems.com/845).

The file states 1 research or textbook statement: 1 solved.

## `Erdos845.erdos_845`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos845.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos845.lean).

> Let $C > 0$. Is it true that the set of integers of the form $n = b_1 + \cdots + b_t$,
> with $b_1 < \cdots < b_t$, where $b_i = 2^{k_i}3^{l_i}$ for $1 \leq i\leq t$ and
> $b_t \leq Cb_1$ has density $0$?
>
> van Doorn and Everts \cite{vDEv25} have disproved this with $C=6$ - in fact, they prove that all
> integers can be written as such a sum in which $b_t<6b_1$.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_845 :
    ¬ ∀ᵉ (C : ℝ) (hC : 0 < C),
      let f : ℕ × ℕ → ℕ := fun (k, l) ↦ 2 ^ k * 3 ^ l
      { ∑ x ∈ B, f x | (B : Finset (ℕ × ℕ)) (h : B.Nonempty)
        (hB : B.sup f ≤ C * B.inf' h f) }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/845.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/845.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/845.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/845.lean)
- [erdosproblems.com/845](https://www.erdosproblems.com/845)
