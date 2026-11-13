---
declaration: theorem
origin: cited
lean: OeisA303656.conjecture
statement: formalized
---

# Sum of two squares, a power of 3, and a power of 5

> Any integer $n > 1$ can be written as $a^2 + b^2 + 3^c + 5^d$ where $a, b, c, d$ are
> nonnegative integers.
>
> Zhi-Wei Sun has offered a \$3,500 prize for the first proof.
>
> *References:*
> - [A303656](https://oeis.org/A303656)
> - Z.-W. Sun, "Restricted sums of four squares," arXiv preprint:
>   https://arxiv.org/abs/1701.05868v10
> - Z.-W. Sun, "Refining Lagrange's four-square theorem," Journal of Number Theory:
>   http://maths.nju.edu.cn/~zwsun/RefineFourSquareTh.pdf
> - Z.-W. Sun, "Restricted sums of three or four squares":
>   http://maths.nju.edu.cn/~zwsun/Square-sum.pdf
> - Zhi-Wei Sun's 1-3-5 conjecture and variations:
>   https://www.aimspress.com/aimspress-data/era/2020/2/PDF/1935-9179_2020_2_589.pdf

*Quoted from [FormalConjectures/OEIS/303656.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303656.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA303656.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's Conjecture (A303656)**: Any integer $n > 1$ can be written as the sum of two
> squares, a power of 3, and a power of 5.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/303656.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303656.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/303656.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/303656.lean)
- [A303656](https://oeis.org/A303656)
