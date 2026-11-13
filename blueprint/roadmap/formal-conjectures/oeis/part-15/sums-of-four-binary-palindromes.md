---
declaration: theorem
origin: cited
lean: OeisA261680.conjecture
statement: formalized
---

# Sums of four binary palindromes

> Number of ordered quadruples $(u, v, w, x)$ of binary palindromes (see A006995) with
> $u + v + w + x = n$.
>
> *References:*
> - [A261680](https://oeis.org/A261680)
> - [Sums of Palindromes: an Approach via Nested-Word Automata](https://arxiv.org/abs/1706.10206)
>   by *Aayush Rajasekaran*, *Jeffrey Shallit*, and *Tim Smith*, arXiv:1706.10206 (2017)

*Quoted from [FormalConjectures/OEIS/261680.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261680.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA261680.conjecture`

Solved: stated here without proof.

> Every number is the sum of four binary palindromes, i.e., $a(n) > 0$ for all $n$.
> Originally stated as a conjecture on OEIS; proved by Rajasekaran, Shallit, and Smith (2017).

```lean
theorem conjecture (n : ℕ) : 0 < a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261680.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261680.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/261680.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261680.lean)
- [A261680](https://oeis.org/A261680)
