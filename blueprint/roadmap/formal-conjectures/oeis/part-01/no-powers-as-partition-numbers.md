---
declaration: theorem
origin: cited
lean: OeisA41.noPowerPartitionNumber
statement: formalized
---

# No powers as partition numbers

> There are no partition numbers $a(k)$ of the form $x^m$, with $x,m$ integers $>1$.
>
> *Reference:* [A41](https://oeis.org/A41)

*Quoted from [FormalConjectures/OEIS/41.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/41.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `OeisA41.noPowerPartitionNumber`

Open: stated without proof.

> There are no partition numbers $a(k)$ of the form $x^m$, with $x,m$ integers $>1$.
> See comment by Zhi-Wei Sun (Dec 02 2013).

```lean
theorem noPowerPartitionNumber : ∀ k, ¬IsPerfectPower (partitionNumber k)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/41.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/41.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/41.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/41.lean)
- [A41](https://oeis.org/A41)
