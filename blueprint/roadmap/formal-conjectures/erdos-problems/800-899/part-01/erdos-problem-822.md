---
declaration: theorem
origin: cited
lean: Erdos822.erdos_822
statement: formalized
---

# Erdős Problem 822

> *References:*
> - [erdosproblems.com/822](https://www.erdosproblems.com/822)
> - [GIL24] Gabdullin, Mikhail R. and Iudelevich, Vitalii V. and Luca,
>   Florian, Numbers of the form {$k+f(k)$}. J. Number Theory (2024), 58--85.

*Quoted from [FormalConjectures/ErdosProblems/822.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/822.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/822](https://www.erdosproblems.com/822).

The file states 1 research or textbook statement: 1 solved.

## `Erdos822.erdos_822`

Solved: stated here without proof.

> Does the set of integers of the form $n + \varphi(n)$ have positive (lower) density?
>
> [GIL24] proved this was true.

```lean
theorem erdos_822 :
    0 < (Set.range fun n => n + Nat.totient n).lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/822.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/822.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/822.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/822.lean)
- [erdosproblems.com/822](https://www.erdosproblems.com/822)
