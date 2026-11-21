---
declaration: theorem
origin: cited
lean: OeisA70518.conjecture
statement: formalized
---

# Value of $n$-th cyclotomic polynomial at $n$

> The sequence $a(n) = \Phi_n(n)$ gives the value of the $n$-th cyclotomic polynomial evaluated
> at $n$:
>
> $$a(n) = |\Phi_n(n)|$$
>
> *References:*
> - [A070518](https://oeis.org/A070518)

*Quoted from [FormalConjectures/OEIS/70518.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/70518.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA70518.conjecture`

Open: stated without proof.

> $a(28341)$ is divisible by $283411^2$. What is the next $n$ such that $a(n)$ is not squarefree?

```lean
theorem conjecture :
    conjecture.answer =
      if h : ∃ n, 28341 < n ∧ ¬ Squarefree (a n) then
        some (sInf {n | 28341 < n ∧ ¬ Squarefree (a n)})
      else
        none
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/70518.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/70518.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/70518.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/70518.lean)
- [A070518](https://oeis.org/A070518)
