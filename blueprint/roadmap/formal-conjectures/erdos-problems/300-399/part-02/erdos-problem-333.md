---
declaration: theorem
origin: cited
lean: Erdos333.erdos_333
statement: formalized
---

# Erdős Problem 333

> *References:*
> - [erdosproblems.com/333](https://www.erdosproblems.com/333)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [ErNe77] Erdős, P. and Newman, D. J., *Bases for sets of integers*. J. Number Theory (1977),
>   420-425.

*Quoted from [FormalConjectures/ErdosProblems/333.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/333.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/333](https://www.erdosproblems.com/333).

The file states 1 research or textbook statement: 1 solved.

## `Erdos333.erdos_333`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos333.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos333.lean).

> Let $A\subseteq \mathbb{N}$ be a set of density zero. Does there exist a $B$ such that
> $A\subseteq B+B$ and
> $$\lvert B\cap \{1,\ldots,N\}\rvert =o(N^{1/2})$$
> for all large $N$?
>
> The answer is no. Erdős and Newman [ErNe77] have proved this is true when $A$ is the set of
> squares. In fact, Theorem 2 of [ErNe77] already implies a negative answer to this problem, but
> this seems to have been overlooked by Erdős and Graham.
>
> See also [806].

```lean
theorem erdos_333 :
    ¬ ∀ A : Set ℕ, A.HasDensity 0 →
      ∃ B : Set ℕ, A ⊆ B + B ∧
        (fun N => ((B ∩ Set.Icc 1 N).ncard : ℝ)) =o[atTop]
          fun N => Real.sqrt N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/333.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/333.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/333.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/333.lean)
- [erdosproblems.com/333](https://www.erdosproblems.com/333)
