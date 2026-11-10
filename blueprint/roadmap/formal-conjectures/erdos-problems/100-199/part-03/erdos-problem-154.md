---
declaration: theorem
origin: cited
lean: Erdos154.erdos_154, Erdos154.erdos_154.variants.lindstrom
statement: formalized
---

# Erdős Problem 154

> *References:*
> - [erdosproblems.com/154](https://www.erdosproblems.com/154)
> - [Li98] Lindström, Bernt, *Well distribution of Sidon sets in residue classes*.
>   J. Number Theory (1998), 197-200.
> - [Ko99] Kolountzakis, Mihail N., *On the uniform distribution in residue classes of dense sets
>   of integers with distinct sums*. J. Number Theory (1999), 147-153.
> - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., *On Sum Sets of Sidon Sets, I*.
>   Journal of Number Theory (1994), 329-347.

*Quoted from [FormalConjectures/ErdosProblems/154.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/154.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/154](https://www.erdosproblems.com/154).

The file states 2 research or textbook statements: 2 solved.

## `Erdos154.erdos_154`

Solved: stated here; a Lean proof is at [https://github.com/willblair0708/lean-proofs/blob/f297d710018270c66b296082766334974260bcbc/ErdosProblems/Erdos154/Sumset.lean#L555](https://github.com/willblair0708/lean-proofs/blob/f297d710018270c66b296082766334974260bcbc/ErdosProblems/Erdos154/Sumset.lean#L555).

> Let $A\subset \{1,\ldots,N\}$ be a Sidon set with $\lvert A\rvert\sim N^{1/2}$. Must $A+A$ be
> well-distributed over all small moduli? In particular, must about half the elements of $A+A$ be
> even and half odd?
>
> The answer is yes. Lindström [Li98] proved the analogous statement for $A$ itself (see
> `erdos_154.variants.lindstrom`), later strengthened by Kolountzakis [Ko99]; well-distribution of
> $A+A$ then follows using the Sidon property.
>
> We state the question for the sumset: for any sequence of Sidon sets
> $A_k\subseteq\{0,\ldots,N_k\}$ with $N_k\to\infty$ and $\lvert A_k\rvert\sim N_k^{1/2}$, and any
> modulus $m\geq 2$, the proportion of elements of $A_k+A_k$ congruent to $i\pmod m$ (i.e. the count
> divided by $\lvert A_k+A_k\rvert$) tends to $1/m$ for every residue $i\lt m$.

```lean
theorem erdos_154 :
    ∀ (m : ℕ) (hm : 2 ≤ m) (N : ℕ → ℕ) (A : ℕ → Finset ℕ),
      Tendsto (fun k => (N k : ℝ)) atTop atTop →
      (∀ k, ∀ x ∈ A k, x ≤ N k) →
      (∀ k, IsSidon (A k : Set ℕ)) →
      Tendsto (fun k => ((A k).card : ℝ) / Real.sqrt (N k)) atTop (nhds 1) →
      ∀ i < m, Tendsto
        (fun k => (((A k + A k).filter (fun s => s % m = i)).card : ℝ) / ((A k + A k).card : ℝ))
        atTop (nhds (1 / m))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/154.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/154.lean#L58).

## `Erdos154.erdos_154.variants.lindstrom`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem154.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem154.lean).

> Lindström's result for $A$ itself [Li98], later strengthened by Kolountzakis [Ko99]: for any
> sequence of Sidon sets $A_k\subseteq\{0,\ldots,N_k\}$ with $N_k\to\infty$ and
> $\lvert A_k\rvert\sim N_k^{1/2}$, and any modulus $m\geq 2$, the number of elements of $A_k$
> congruent to $i\pmod m$, divided by $N_k^{1/2}$, tends to $1/m$ for every residue $i\lt m$.
>
> Well-distribution of $A+A$ (the actual question, `erdos_154`) follows from this using the Sidon
> property.

```lean
theorem erdos_154.variants.lindstrom :
    ∀ (m : ℕ) (hm : 2 ≤ m) (N : ℕ → ℕ) (A : ℕ → Finset ℕ),
      Tendsto (fun k => (N k : ℝ)) atTop atTop →
      (∀ k, ∀ x ∈ A k, x ≤ N k) →
      (∀ k, IsSidon (A k : Set ℕ)) →
      Tendsto (fun k => ((A k).card : ℝ) / Real.sqrt (N k)) atTop (nhds 1) →
      ∀ i < m, Tendsto
        (fun k => (((A k).filter (fun a => a % m = i)).card : ℝ) / Real.sqrt (N k))
        atTop (nhds (1 / m))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/154.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/154.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/154.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/154.lean)
- [erdosproblems.com/154](https://www.erdosproblems.com/154)
