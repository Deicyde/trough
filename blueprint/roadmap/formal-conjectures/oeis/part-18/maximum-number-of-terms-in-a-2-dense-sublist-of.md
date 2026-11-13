---
declaration: theorem
origin: cited
lean: OeisA400194.conjecture
statement: formalized
---

# Maximum number of terms in a 2-dense sublist of divisors of $n$

> Write the divisors of $n$ in increasing order and split this list between consecutive divisors
> $d < d'$ with $d' > 2d$. The pieces are the 2-dense sublists of divisors of $n$. The sequence
> gives the maximum number of terms in such a sublist.
>
> *References:*
> - [A400194](https://oeis.org/A400194)
> - [A400195](https://oeis.org/A400195)
> - [A384222](https://oeis.org/A384222)

*Quoted from [FormalConjectures/OEIS/400194.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/400194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 7 test statements, counted here but not shown.

## `OeisA400194.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A400194.lean#L26-L27](https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A400194.lean#L26-L27).

> "Conjecture: a(n) is the product of the ruler function of n and the maximum number of odd terms
> in a 2-dense sublist of divisors of n."
>
> "Conjecture: a(n) = A001511(n) * A400195(n)."
>
> The ruler function is $A001511(n) = \nu_2(n) + 1$.
>
> Solved by Claude (Anthropic) prompted by otoinobuo. If $d$ and $2d$ divide $n$, then they lie
> in the same 2-dense sublist. So each sublist is a union of sets $\{o, 2o, \dots, 2^{\nu_2(n)} o\}$
> with $o$ odd.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : a n = (padicValNat 2 n + 1) * b n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/400194.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/400194.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/400194.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/400194.lean)
- [A400194](https://oeis.org/A400194)
