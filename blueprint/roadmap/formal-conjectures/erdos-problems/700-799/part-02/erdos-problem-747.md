---
declaration: theorem
origin: cited
lean: Erdos747.erdos_747
statement: formalized
---

# Erdős Problem 747

> *References:*
> - [erdosproblems.com/747](https://www.erdosproblems.com/747)
> - [JKV08] Johansson, Anders and Kahn, Jeff and Vu, Van, Factors in random graphs. Random Structures
>   Algorithms (2008), 1-28.
> - [Ka23] Kahn, Jeff, Asymptotics for Shamir's problem. Adv. Math. (2023), Paper No. 109019, 39.

*Quoted from [FormalConjectures/ErdosProblems/747.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/747.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/747](https://www.erdosproblems.com/747).

The file states 1 research or textbook statement: 1 solved.

## `Erdos747.erdos_747`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos747.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos747.lean).

> How large should $\ell(n)$ be such that, almost surely, a random $3$-uniform hypergraph on $3n$
> vertices with $\ell(n)$ edges must contain $n$ vertex-disjoint edges?
>
> The precise asymptotic was given by Kahn [Ka23], proving that the threshold is $\sim n\log n$ (also
> for the general problem over $r$-uniform hypergraphs).

```lean
theorem erdos_747 :
    ∀ ε : ℝ, 0 < ε → ε < 1 →
    Tendsto (fun n ↦ Hypergraph.matchingProbability (3 * n) 3
      ⌊(1 + ε) * erdos_747.answer n⌋₊ n) atTop (𝓝 1) ∧
    Tendsto (fun n ↦ Hypergraph.matchingProbability (3 * n) 3
      ⌊(1 - ε) * erdos_747.answer n⌋₊ n) atTop (𝓝 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/747.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/747.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/747.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/747.lean)
- [erdosproblems.com/747](https://www.erdosproblems.com/747)
