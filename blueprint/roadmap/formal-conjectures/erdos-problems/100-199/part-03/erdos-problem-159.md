---
declaration: theorem
origin: cited
lean: Erdos159.erdos_159
statement: formalized
---

# Erdős Problem 159

> *References:*
> - [erdosproblems.com/159](https://www.erdosproblems.com/159)
> - [Er78] Erdős, P., Problems and results in combinatorial analysis and combinatorial number
>   theory. Proc. Ninth Southeastern Conf. Combinatorics, Graph Theory and Computing (1978), 29-40.
> - [Sp77] Spencer, J., Asymptotic lower bounds for Ramsey functions. Discrete Math. (1977), 69-76.

*Quoted from [FormalConjectures/ErdosProblems/159.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/159.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/159](https://www.erdosproblems.com/159).

The file states 1 research or textbook statement: 1 open.

## `Erdos159.erdos_159`

Open: stated without proof.

> There exists some constant $c>0$ such that
>
> $$R(C_4,K_n) \ll n^{2-c}.$$
>
> The prize of $100 is offered in [Er78] for a proof or disproof.
>
> This problem is #17 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_159 :
    ∃ (c : ℝ) (_ : 0 < c) (C : ℝ),
      ∀ (n : ℕ), 1 ≤ n →
        (SimpleGraph.graphRamsey (SimpleGraph.cycleGraph 4)
          (SimpleGraph.completeGraph (Fin n)) : ℝ) ≤ C * (n : ℝ) ^ (2 - c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/159.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/159.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/159.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/159.lean)
- [erdosproblems.com/159](https://www.erdosproblems.com/159)
