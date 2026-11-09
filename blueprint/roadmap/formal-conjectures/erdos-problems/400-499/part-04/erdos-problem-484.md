---
declaration: theorem
origin: cited
lean: Erdos484.erdos_484
statement: formalized
---

# Erdős Problem 484

> *References:*
> - [erdosproblems.com/484](https://www.erdosproblems.com/484)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [ESS89] Erdős, P., Sárközy, A., and Sós, V. T., *On a conjecture of Roth and some related
>   problems. I*. (1989), 47-59.

*Quoted from [FormalConjectures/ErdosProblems/484.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/484.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/484](https://www.erdosproblems.com/484).

The file states 1 research or textbook statement: 1 solved.

## `Erdos484.erdos_484`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos484.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos484.lean).

> Prove that there exists an absolute constant $c>0$ such that, whenever $\{1,\ldots,N\}$ is
> $k$-coloured (and $N$ is large enough depending on $k$) then there are at least $cN$ many
> integers in $\{1,\ldots,N\}$ which are representable as a monochromatic sum (that is, $a+b$
> where $a,b\in \{1,\ldots,N\}$ are in the same colour class and $a\neq b$).
>
> A conjecture of Roth. Solved by Erdős, Sárközy, and Sós [ESS89], who in fact prove that
> there are at least $\frac{N}{2}-O(N^{1-1/2^{k+1}})$ many even numbers which are of this form.

```lean
theorem erdos_484 :
    ∃ c : ℝ, 0 < c ∧ ∀ k : ℕ, 0 < k → ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N → ∀ f : ℕ → Fin k,
      c * N ≤ (((Finset.Icc 1 N).filter fun n =>
        ∃ a ∈ Finset.Icc 1 N, ∃ b ∈ Finset.Icc 1 N,
          a ≠ b ∧ f a = f b ∧ a + b = n).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/484.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/484.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/484.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/484.lean)
- [erdosproblems.com/484](https://www.erdosproblems.com/484)
