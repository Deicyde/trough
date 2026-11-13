---
declaration: theorem
origin: cited
lean: OeisA2.density_one
statement: formalized
---

# Density of ones in the Kolakoski sequence

> The Kolakoski sequence is the self-describing sequence of ones and twos whose terms are the
> lengths of its successive runs. Its official indexing begins with $a(1) = 1$; here it is extended
> by $a(0) = 0$.
>
> *References:*
> - [A000002](https://oeis.org/A000002)
> - E. S. Kupin and E. S. Rowland,
>   ["Bounds on the frequency of 1 in the Kolakoski word"](https://arxiv.org/abs/0809.2776),
>   arXiv:0809.2776 [math.CO] (2008).

*Quoted from [FormalConjectures/OEIS/2.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 11 test statements and 4 API statements, counted here but not shown.

## `OeisA2.density_one`

Open: stated without proof.

> "It is an unsolved problem to show that the density of 1's is equal to 1/2."
> — [A000002](https://oeis.org/A000002)

```lean
theorem density_one : {n : ℕ | a n = 1}.HasDensity (1 / 2 : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OEIS/2.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2.lean#L137).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2.lean)
- [A000002](https://oeis.org/A000002)
