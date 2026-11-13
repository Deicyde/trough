---
declaration: theorem
origin: cited
lean: OeisA309132.carmichael_iff_squarefree_a
statement: formalized
---

# Characterization of Carmichael numbers via squarefree denominators $a(n)$

> $a(n)$ is the denominator of $F(n) = \operatorname{num}(B_{n-1})/n + \operatorname{den}(B_{n-1})/n^2$.
>
> A composite number $n$ has squarefree $a(n)$ if and only if $n$ is a Carmichael number.
>
> *References:*
> - [A309132](https://oeis.org/A309132)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A027641](https://oeis.org/A027641)
> - [A027642](https://oeis.org/A027642)

*Quoted from [FormalConjectures/OEIS/309132.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/309132.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA309132.carmichael_iff_squarefree_a`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/309132.wip.lean#L353](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/309132.wip.lean#L353).

> Conjecture: composite numbers $n$ such that $a(n)$ is squarefree are only the Carmichael numbers (A002997). - _Thomas Ordowski_, Jul 15 2019
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem carmichael_iff_squarefree_a :
    ∀ (n : ℕ), (IsComposite n ∧ Squarefree (a n)) ↔ IsCarmichaelNumber n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/309132.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/309132.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/309132.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/309132.lean)
- [A309132](https://oeis.org/A309132)
