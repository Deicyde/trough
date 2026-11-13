---
declaration: theorem
origin: cited
lean: OeisA120424.conjecture1, OeisA120424.conjecture2
statement: formalized
---

# Half-Fibonacci sequence

> $a(0) = 1, a(1) = 3$; for $n \ge 2$, $a(n) = f(a(n-1)) + f(a(n-2))$ where $f(x) = x/2$ if $x$
> is even
> and $f(x) = x$ if $x$ is odd.
>
> *References:*
> - [A120424](https://oeis.org/A120424)

*Quoted from [FormalConjectures/OEIS/120424.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/120424.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA120424.conjecture1`

Open: stated without proof.

> Conjecture (1): The natural density of even terms in the sequence is $1/2$.

```lean
theorem conjecture1 :
    Filter.Tendsto (fun n : ℕ => ((Finset.filter (fun k => a k % 2 = 0) (Finset.range n)).card
        : ℝ) / (n : ℝ))
      Filter.atTop (nhds (1 / 2 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/120424.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/120424.lean#L66).

## `OeisA120424.conjecture2`

Open: stated without proof.

> Conjecture (2): There are infinitely many consecutive pairs that differ by 1.

```lean
theorem conjecture2 :
    Set.Infinite {n : ℕ | a (n + 1) = a n + 1 ∨ a n = a (n + 1) + 1}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/120424.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/120424.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/120424.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/120424.lean)
- [A120424](https://oeis.org/A120424)
