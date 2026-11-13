---
declaration: theorem
origin: cited
lean: Erdos1138.erdos_1138
statement: formalized
---

# Erdős Problem 1138

> *References:*
> - [erdosproblems.com/1138](https://www.erdosproblems.com/1138)
> - [Va99] Vardi, I., Prime census. (1999).
> - [Kum26] Kumrawat, S., [Disproof of Erdős Problem 1138](https://sourish-kumrawat.github.io/papers/Erdos_1138.pdf).
>
> Note that the conjecture has a claimed disproof found at:
> https://sourish-kumrawat.github.io/papers/Erdos_1138.pdf,
> see the discussion section on the Erdos problems website for more information.

*Quoted from [FormalConjectures/ErdosProblems/1138.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1138.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1138](https://www.erdosproblems.com/1138).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1138.erdos_1138`

Solved: stated here; a Lean proof is at [https://github.com/YanYablonovskiy/formal-conjectures/blob/7c134317104d3b98ecc751afbb79ec0adddf8e7c/FormalConjectures/ErdosProblems/1138a.lean#L496](https://github.com/YanYablonovskiy/formal-conjectures/blob/7c134317104d3b98ecc751afbb79ec0adddf8e7c/FormalConjectures/ErdosProblems/1138a.lean#L496).

> **Erdős Problem 1138.**
> Let $x/2 < y < x$ and $C > 1$. If $d = \max_{p_n < x}(p_{n+1} - p_n)$,
> where $p_n$ denotes the $n$-th prime, then is it true that
>
> $$\pi(y + Cd) - \pi(y) \sim \frac{Cd}{\log y}$$
>
> ?

```lean
theorem erdos_1138 : ¬ ∀C > 1,
    primeCount_Ioc_mul_const C ~[snd_gt_half_fst] fun (x, y) ↦
      C * (sup_primeGap x) / Real.log y
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1138.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1138.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1138.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1138.lean)
- [erdosproblems.com/1138](https://www.erdosproblems.com/1138)
