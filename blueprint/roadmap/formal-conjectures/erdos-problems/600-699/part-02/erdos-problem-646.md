---
declaration: theorem
origin: cited
lean: Erdos646.erdos_646
statement: formalized
---

# Erdős Problem 646

> *References:*
> - [erdosproblems.com/646](https://www.erdosproblems.com/646)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Be97] Berend, Daniel, *On the parity of exponents in the factorization of $n!$*.
>   J. Number Theory (1997), 13-19.

*Quoted from [FormalConjectures/ErdosProblems/646.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/646.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/646](https://www.erdosproblems.com/646).

The file states 1 research or textbook statement: 1 solved.

## `Erdos646.erdos_646`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos646.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos646.lean).

> Let $p_1,\ldots,p_k$ be distinct primes. Are there infinitely many $n$ such that $n!$ is
> divisible by an even power of each of the $p_i$?
>
> The answer is yes, proved by Berend [Be97], who further proved that the sequence of such $n$
> has bounded gaps (where the bound depends on the initial set of primes).

```lean
theorem erdos_646 :
    ∀ S : Finset ℕ, (∀ p ∈ S, p.Prime) →
      {n : ℕ | ∀ p ∈ S, Even (padicValNat p (n !))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/646.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/646.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/646.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/646.lean)
- [erdosproblems.com/646](https://www.erdosproblems.com/646)
