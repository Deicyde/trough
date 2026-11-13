---
declaration: theorem
origin: cited
lean: RudinsConjecture.rudins_conjecture, RudinsConjecture.rudins_conjecture_strong, RudinsConjecture.rudins_conjecture_unique
statement: formalized
---

# Rudin's conjecture on squares in arithmetic progressions

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Rudin%27s_conjecture)
> - [Ru60] Rudin, W., *Trigonometric series with gaps*, J. Math. Mech. 9 (1960), 203–227.
> - González-Jiménez, E. and Xarles, X., *On a conjecture of Rudin on squares in arithmetic
>   progressions*, LMS J. Comput. Math. 17 (2014), 58–76.

*Quoted from [FormalConjectures/Wikipedia/RudinsConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RudinsConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 3 test statements, counted here but not shown.

## `RudinsConjecture.rudins_conjecture`

Open: stated without proof.

> **Rudin's conjecture.** The maximal number of squares among the first $N$ terms of a non-trivial
> arithmetic progression grows at most like $\sqrt{N}$:
>
> $$Q(N) = O(\sqrt{N}).$$

```lean
theorem rudins_conjecture :
    (fun N : ℕ => (Qmax N : ℝ)) =O[atTop] fun N : ℕ => Real.sqrt N
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RudinsConjecture.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RudinsConjecture.lean#L101).

## `RudinsConjecture.rudins_conjecture_strong`

Open: stated without proof.

> A stronger form of Rudin's conjecture: for every $N \ge 6$, the arithmetic progression
> $24 n + 1$ attains the maximum $Q(N)$.

```lean
theorem rudins_conjecture_strong (N : ℕ) (hN : 6 ≤ N) : Q N 24 1 = Qmax N
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RudinsConjecture.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RudinsConjecture.lean#L110).

## `RudinsConjecture.rudins_conjecture_unique`

Open: stated without proof.

> The strongest form of Rudin's conjecture also asserts *uniqueness*: for $N \ge 6$, any non-trivial
> arithmetic progression attaining the maximum $Q(N)$ has common difference $24$. (Its initial term
> is then forced by $\gcd(24, a) = 1$; the progression $24n + 1$ is the canonical representative.)

```lean
theorem rudins_conjecture_unique (N : ℕ) (hN : 6 ≤ N) (q a : ℕ)
    (hqa : IsNontrivial q a) (hmax : Q N q a = Qmax N) : q = 24
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RudinsConjecture.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RudinsConjecture.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RudinsConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RudinsConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Rudin%27s_conjecture)
