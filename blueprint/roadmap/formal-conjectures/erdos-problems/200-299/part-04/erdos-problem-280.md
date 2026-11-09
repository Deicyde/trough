---
declaration: theorem
origin: cited
lean: Erdos280.erdos_280
statement: formalized
---

# Erdős Problem 280

> *References:*
> - [erdosproblems.com/280](https://www.erdosproblems.com/280)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*. Monographies de L'Enseignement Mathematique (1980).

*Quoted from [FormalConjectures/ErdosProblems/280.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/280.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/280](https://www.erdosproblems.com/280).

The file states 1 research or textbook statement: 1 solved.

## `Erdos280.erdos_280`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos280.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos280.lean).

> Let $n_1\lt n_2\lt \cdots $ be an infinite sequence of integers with associated $a_k\pmod{n_k}$, such that for some $\epsilon>0$ we have $n_k>(1+\epsilon)k\log k$ for all $k$. Then
>
> $$
> \#\{ m\lt n_k : m\not\equiv a_i\pmod{n_i} \textrm{ for }1\leq i\leq k\}\neq o(k).
> $$
>
> Cambie observed that this is false.

```lean
theorem erdos_280 :
    ¬ ∀ (n a : ℕ → ℕ), StrictMono n → (∀ i, 1 ≤ i → a i < n i) →
      (∃ ε : ℝ, 0 < ε ∧
        ∀ k, 1 ≤ k → (n k : ℝ) > (1 + ε) * (k : ℝ) * Real.log (k : ℝ)) →
      ¬ Tendsto
        (fun k : ℕ => (uncoveredCount n a k : ℝ) / (k : ℝ))
        atTop (nhds 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/280.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/280.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/280.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/280.lean)
- [erdosproblems.com/280](https://www.erdosproblems.com/280)
