---
declaration: theorem
origin: cited
lean: LehmerTotient.lehmer_totient
statement: formalized
---

# Lehmer's totient problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_totient_problem)

*Quoted from [FormalConjectures/Wikipedia/LehmerTotient.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LehmerTotient.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `LehmerTotient.lehmer_totient`

Open: stated without proof.

> Does there exist a composite number $n > 1$ such that Euler’s totient function
> $\varphi(n)$ divides $n - 1$?

```lean
theorem lehmer_totient :
    ∃ n > 1, ¬Prime n ∧ Nat.totient n ∣ n - 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LehmerTotient.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LehmerTotient.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LehmerTotient.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LehmerTotient.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_totient_problem)
