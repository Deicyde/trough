---
declaration: theorem
origin: cited
lean: OeisA51293.tendsto_aReal_asymptotic
statement: formalized
---

# Asymptotics of subsets of $\{1, 2, \dots, n\}$ with integer average

> Number of nonempty subsets of $\{1, 2, 3, \dots, n\}$ whose elements have an integer average.
>
> Benoit Cloitre conjectured the asymptotic expansion:
> $$a(n) = \frac{2^{n+1}}{n} \left(1 + \frac{1}{n} + \frac{3}{n^2} + \frac{13}{n^3} + \frac{75}{n^4} + \frac{541}{n^5} + o\left(\frac{1}{n^5}\right)\right)$$
> where the coefficients $1, 1, 3, 13, 75, 541, \dots$ are the Fubini numbers (preferential arrangements, A000670).
>
> *References:*
> - [A051293](https://oeis.org/A051293)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A000670](https://oeis.org/A000670)

*Quoted from [FormalConjectures/OEIS/51293.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/51293.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA51293.tendsto_aReal_asymptotic`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/51293.wip.lean#L503](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/51293.wip.lean#L503).

> Conjecture: $a(n) = 2^{n+1}/n \cdot (1 + 1/n + 3/n^2 + 13/n^3 + 75/n^4 + 541/n^5 + o(1/n^5))$. - _Benoit Cloitre_, Oct 20 2002
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem tendsto_aReal_asymptotic :
    Tendsto (fun n : ℕ =>
      (aReal n - (2 ^ (n + 1) / (n : ℝ)) *
        (1 + 1 / (n : ℝ) + 3 / (n : ℝ) ^ 2 + 13 / (n : ℝ) ^ 3 + 75 / (n : ℝ) ^ 4 + 541 / (n : ℝ) ^ 5)) /
      (2 ^ (n + 1) / (n : ℝ) ^ 6)) atTop (nhds 0)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/51293.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/51293.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/51293.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/51293.lean)
- [A051293](https://oeis.org/A051293)
