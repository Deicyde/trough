---
declaration: theorem
origin: cited
lean: OeisA2426.conjecture
statement: formalized
---

# Central trinomial coefficients

> Central trinomial coefficients: largest coefficient of $(1 + x + x^2)^n$, which is the coefficient
> of $x^n$ in the expansion of $(1 + x + x^2)^n$.
>
> *References:*
> - [A002426](https://oeis.org/A002426)

*Quoted from [FormalConjectures/OEIS/2426.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2426.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA2426.conjecture`

Open: stated without proof.

> An integer $n > 3$ is prime if and only if $a(n) \equiv 1 \pmod{n^2}$.
> We have verified this for $n$ up to $8 \cdot 10^5$, and proved that $a(p) \equiv 1 \pmod{p^2}$
> for any prime $p > 3$ (cf. A277640).
> - Zhi-Wei Sun, Nov 30 2016

```lean
theorem conjecture (n : ℕ) (hn : 3 < n) :
    n.Prime ↔ a n ≡ 1 [MOD n ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/2426.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2426.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2426.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2426.lean)
- [A002426](https://oeis.org/A002426)
