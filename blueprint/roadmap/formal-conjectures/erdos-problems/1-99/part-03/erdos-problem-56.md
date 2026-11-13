---
declaration: theorem
origin: cited
lean: Erdos56.erdos_56
statement: formalized
---

# Erdős Problem 56

> *Reference:* [erdosproblems.com/56](https://www.erdosproblems.com/56)

*Quoted from [FormalConjectures/ErdosProblems/56.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/56.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/56](https://www.erdosproblems.com/56).

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 5 API statements, counted here but not shown.

## `Erdos56.erdos_56`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos56.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos56.lean).

> Suppose $A \subseteq \{1,\dots,N\}$ is such that there are no $k+1$ elements of $A$ which are
> relatively prime. An example is the set of all multiples of the first $k$ primes.
> Is this the largest such set?  To avoid trivial counterexamples, we must insist that $N$ be at
> least the $k$th prime.

```lean
theorem erdos_56 : ¬ ∀ᵉ (k > 0) (N ≥ (k-1).nth Nat.Prime),
    (MaxWeaklyDivisible N k = (FirstPrimesMultiples N k).card)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/56.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/56.lean#L153).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/56.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/56.lean)
- [erdosproblems.com/56](https://www.erdosproblems.com/56)
