---
declaration: theorem
origin: cited
lean: KeithNumber.keith_numbers_base_two_infinite, KeithNumber.klazar_luca_keith_counting_bound, KeithNumber.keith_numbers_infinite
statement: formalized
---

# Keith numbers

> Defined by Mike Keith (1987) as *repfigit* numbers, an integer $N \ge b$ written in base $b \ge 2$
> using $k \ge 2$ digits $d_0, \dots, d_{k-1}$ (most-significant digit first) is a base-$b$ Keith
> integer when $N$ appears in the $k$-step Fibonacci-style recurrence initialized by $a_i = d_i$
> ($0 \le i < k$) and $a_m = \sum_{j=1}^k a_{m-j}$ ($m \ge k$). Base $2$ admits infinitely many Keith
> integers (including $2^r$ for every $r \ge 1$). In base $10$ (`OEIS A007629`), Martin Klazar and
> Florian Luca (2007, Theorem 1.2) proved the counting bound $\#\mathcal{K}(x) \ll x / \sqrt{\log x}$
> for $x \ge 2$ (which extends to every fixed base $b \ge 4$ and shows natural density zero, though it
> does not establish convergence of the reciprocal sum); whether infinitely many base-$10$ Keith
> integers exist remains open.
>
> *References:*
> - [Wikipedia: Keith number](https://en.wikipedia.org/wiki/Keith_number)
> - [OEIS A007629](https://oeis.org/A007629)
> - M. Keith (1987), J. Recreational Math. **19**, no. 1, 41–42.
> - M. Klazar and F. Luca (2007), J. Integer Seq. **10**, Article 07.2.2.

*Quoted from [FormalConjectures/Wikipedia/KeithNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KeithNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 9 test statements and 2 API statements, counted here but not shown.

## `KeithNumber.keith_numbers_base_two_infinite`

Textbook result, proved here.

> Infinitely many base-$2$ Keith integers exist (for example $2^r$ for every $r \ge 1$).

```lean
theorem keith_numbers_base_two_infinite :
    {N : ℕ | IsKeithNumberBase 2 N}.Infinite
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/KeithNumber.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KeithNumber.lean#L142).

## `KeithNumber.klazar_luca_keith_counting_bound`

Solved: stated here without proof.

> Klazar–Luca counting bound (2007, Theorem 1.2): there exists a constant $C > 0$ such that for every
> integer $x \ge 2$, the number of base-$10$ Keith integers at most $x$ satisfies
>
> $$\#\{N \le x : N \text{ is a Keith number}\} \le \frac{C x}{\sqrt{\log x}}.$$

```lean
theorem klazar_luca_keith_counting_bound :
    ∃ C : ℝ, 0 < C ∧ ∀ x : ℕ, 2 ≤ x →
      ({N : ℕ | N ≤ x ∧ IsKeithNumber N}.ncard : ℝ) ≤
        C * ((x : ℝ) / Real.sqrt (Real.log (x : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/KeithNumber.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KeithNumber.lean#L180).

## `KeithNumber.keith_numbers_infinite`

Open: stated without proof.

> Do infinitely many base-$10$ Keith integers exist ([OEIS A007629](https://oeis.org/A007629))?

```lean
theorem keith_numbers_infinite :
    {N : ℕ | IsKeithNumber N}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/KeithNumber.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KeithNumber.lean#L190).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/KeithNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KeithNumber.lean)
- [Wikipedia: Keith number](https://en.wikipedia.org/wiki/Keith_number)
