---
declaration: theorem
origin: cited
lean: OeisA303639.conjecture, OeisA303639.conjecture.counterexample
statement: formalized
---

# Sum of two squares and two central-binomial-type terms

> A303639 counts the ways to write $n$ as $a^2 + b^2 + \binom{2c+1}{c} + \binom{2d+1}{d}$ with
> $a, b, c, d$ nonnegative integers, $a \le b$ and $c \le d$.
>
> *References:*
> - [A303639](https://oeis.org/A303639)
> - Z.-W. Sun, ["Restricted sums of four squares"](https://arxiv.org/abs/1701.05868),
>   arXiv:1701.05868 [math.NT], 2017-2018.
> - Z.-W. Sun, ["Refining Lagrange's four-square theorem"](https://doi.org/10.1016/j.jnt.2016.11.008),
>   *J. Number Theory* **175** (2017), 167-190.
> - S. Jeong, [A303639 Counterexample Project](https://github.com/DCLXAI/a303639-counterexample),
>   search, certificates and independent verifiers,
>   [DOI 10.5281/zenodo.21863025](https://doi.org/10.5281/zenodo.21863025). The counterexample is
>   recorded as an approved comment on the OEIS entry (Aug 10 2026).

*Quoted from [FormalConjectures/OEIS/303639.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303639.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 6 test statements, counted here but not shown.

## `OeisA303639.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/DCLXAI/a303639-counterexample/blob/8e21c57c622b05a1815bcf9927458ebb3973ef2e/lean/A303639/Counterexample.lean](https://github.com/DCLXAI/a303639-counterexample/blob/8e21c57c622b05a1815bcf9927458ebb3973ef2e/lean/A303639/Counterexample.lean).

> **Zhi-Wei Sun's Conjecture (A303639)**: any integer $n > 1$ can be written as
> $a^2 + b^2 + \binom{2c+1}{c} + \binom{2d+1}{d}$ with $a, b, c, d$ nonnegative integers.
> Sun checked this for $n$ up to $6 \cdot 10^8$.
>
> This is false: $n = 800322180$ admits no such representation, so $a(800322180) = 0$. Since
> $\binom{33}{16} > 800322180$, only $c, d \le 15$ are possible, and each of the resulting $136$
> remainders $800322180 - \binom{2c+1}{c} - \binom{2d+1}{d}$ is divisible by some prime
> $p \equiv 3 \pmod 4$ to an odd power, hence is not a sum of two squares by Fermat's two-square
> theorem.
>
> The counterexample is recorded as an approved comment on the OEIS entry; the Lean proof linked
> below formalises this argument, and was produced by Claude Opus 5 prompted by Sunsu Jeong
> ([DCLXAI](https://github.com/DCLXAI)).

```lean
theorem conjecture : ¬ ∀ n : ℕ, 1 < n → A n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/303639.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303639.lean#L96).

## `OeisA303639.conjecture.counterexample`

Solved: stated here; a Lean proof is at [https://github.com/DCLXAI/a303639-counterexample/blob/8e21c57c622b05a1815bcf9927458ebb3973ef2e/lean/A303639/Counterexample.lean](https://github.com/DCLXAI/a303639-counterexample/blob/8e21c57c622b05a1815bcf9927458ebb3973ef2e/lean/A303639/Counterexample.lean).

> The counterexample witnessing that A303639 vanishes: $a(800322180) = 0$.

```lean
theorem conjecture.counterexample : ¬ A 800322180
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/303639.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303639.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/303639.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303639.lean)
- [A303639](https://oeis.org/A303639)
