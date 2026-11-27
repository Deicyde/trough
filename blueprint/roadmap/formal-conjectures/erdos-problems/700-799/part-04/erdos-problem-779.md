---
declaration: theorem
origin: cited
lean: Erdos779.erdos_779
statement: formalized
---

# Erdős Problem 779

> *Reference:* [erdosproblems.com/779](https://www.erdosproblems.com/779)

*Quoted from [FormalConjectures/ErdosProblems/779.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/779.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/779](https://www.erdosproblems.com/779).

The file states 1 research or textbook statement: 1 open.

## `Erdos779.erdos_779`

Open: stated without proof.

> A Conjecture of Marian Deaconescu, see p.120 in https://doi.org/10.2307/2975810
>
> [Needed to index shift in order to avoid trivial case $n = 0$,
> where the conjecture is trivially false.]

```lean
theorem erdos_779 (n : ℕ) (hn : n ≥ 1): let P := ∏ i ∈ range (n + 1), nth Nat.Prime i
    ∃ p, p.Prime ∧ (P + p).Prime ∧ nth Nat.Prime n < p ∧ p < P
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/779.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/779.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/779.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/779.lean)
- [erdosproblems.com/779](https://www.erdosproblems.com/779)
