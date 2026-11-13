---
declaration: theorem
origin: cited
lean: Erdos429.erdos_429
statement: formalized
---

# Erdős Problem 429

> *References:*
> - [erdosproblems.com/429](https://www.erdosproblems.com/429)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*.
>   Ann. Discrete Math. (1980), 89-115.
> - [We24] D. Weisenberg, *Sparse Admissible Sets and a Problem of Erdős and Graham*.
>   Integers (2024).

*Quoted from [FormalConjectures/ErdosProblems/429.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/429.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/429](https://www.erdosproblems.com/429).

The file states 1 research or textbook statement: 1 solved.

## `Erdos429.erdos_429`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos429.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos429.lean).

> Is it true that, if $A\subseteq \mathbb{N}$ is sparse enough and does not cover all residue
> classes modulo $p$ for any prime $p$, then there exists some $n\in \mathbb{Z}$ such that $n+a$ is
> prime for all $a\in A$?
>
> Weisenberg [We24] has shown the answer is no: $A$ can be arbitrarily sparse and missing at
> least one residue class modulo every prime $p$, and yet $A+n$ is not contained in the primes
> for any $n\in \mathbb{Z}$. (Weisenberg gives several constructions of such an $A$.)

```lean
theorem erdos_429 :
    ¬ ∃ f : ℕ → ℕ, Tendsto f atTop atTop ∧
      ∀ A : Set ℕ, A.Infinite → (∀ N, (A ∩ Set.Icc 1 N).ncard ≤ f N) →
        (∀ p : ℕ, p.Prime → ∃ b : ZMod p, ∀ a ∈ A, (a : ZMod p) ≠ b) →
        ∃ n : ℤ, ∀ a ∈ A, (n + a).toNat.Prime
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/429.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/429.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/429.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/429.lean)
- [erdosproblems.com/429](https://www.erdosproblems.com/429)
