---
declaration: theorem
origin: cited
lean: OeisA102722.conjecture
statement: formalized
---

# Floor of sum of $\{n/k\}$

> Given $n$, sum all division remainders $\{n/k\}$, with $k=1,\dots,n$.
> The value $a(n)$ is given by the floor of that sum. Note that $\{x\}:=x-[x]$.
> Conjecture: a(n) ~ (1-EulerGamma)n.
>
> *References:*
> - [A102722](https://oeis.org/A102722)

*Quoted from [FormalConjectures/OEIS/102722.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102722.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 5 API statements, counted here but not shown.

## `OeisA102722.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-102722-asymptotic/blob/0e3bf1bc6dfd04627f926b07fb8d25f4395a5072/lean/OEIS102722FC.lean#L18-L24](https://github.com/KitaKen1/oeis-102722-asymptotic/blob/0e3bf1bc6dfd04627f926b07fb8d25f4395a5072/lean/OEIS102722FC.lean#L18-L24).

> A102722 Conjecture: $a(n) \sim (1-\gamma)n$.

```lean
theorem conjecture :
    (fun n : ℕ => (a n : ℝ)) ~[atTop]
      (fun n : ℕ => (1 - Real.eulerMascheroniConstant) * (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/102722.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102722.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/102722.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102722.lean)
- [A102722](https://oeis.org/A102722)
