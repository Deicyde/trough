---
declaration: theorem
origin: cited
lean: Erdos419.erdos_419
statement: formalized
---

# Erdős Problem 419

> *References:*
> - [erdosproblems.com/419](https://www.erdosproblems.com/419)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [EGIP96] Erdős, Paul and Graham, S. W. and Ivić, Aleksandar and Pomerance, Carl,
>   *On the number of divisors of $n!$*. (1996), 337--355.

*Quoted from [FormalConjectures/ErdosProblems/419.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/419.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/419](https://www.erdosproblems.com/419).

The file states 1 research or textbook statement: 1 solved.

## `Erdos419.erdos_419`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos419.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos419.lean).

> If $\tau(n)$ counts the number of divisors of $n$, then what is the set of limit points of
>
> $$
> \frac{\tau((n+1)!)}{\tau(n!)}?
> $$
>
> The limit points are exactly $\{1\} \cup \{1+1/k : k \geq 1\}$.

```lean
theorem erdos_419 :
    {x : ℝ | MapClusterPt x atTop factorialDivisorRatio} = limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/419.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/419.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/419.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/419.lean)
- [erdosproblems.com/419](https://www.erdosproblems.com/419)
