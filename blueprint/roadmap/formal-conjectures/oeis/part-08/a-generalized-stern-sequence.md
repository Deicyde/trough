---
declaration: theorem
origin: cited
lean: OeisA112970.conjecture1, OeisA112970.conjecture1_value, OeisA112970.conjecture2, OeisA112970.conjecture3
statement: formalized
---

# A generalized Stern sequence

> A112970: A generalized Stern sequence, defined by the recurrence relations:
> $a(2n+1) = a(n)$ and $a(2n) = a(n) + a(n-2)$ with $a(0)=1$, $a(1)=1$ and $a(n)=0$ for $n \le -1$.
>
> *References:*
> - [A112970](https://oeis.org/A112970)

*Quoted from [FormalConjectures/OEIS/112970.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 solved. It also has 5 test statements, counted here but not shown.

## `OeisA112970.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L43-L46](https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L43-L46).

> Conjecture: $a(2^n)=a(2^(n+1)+1)=\textrm{A033638}(n)$.
> This formalizes the equality $a(2^n) = a(2^(n+1)+1)$.

```lean
theorem conjecture1 (n : ℕ) : a (2^n) = a (2^(n + 1) + 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/112970.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean#L77).

## `OeisA112970.conjecture1_value`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA112970_conjecture1_value.lean#L139](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA112970_conjecture1_value.lean#L139).

> Second part of the conjecture, $a(2^n)=\textrm{A033638}(n)=\lfloor n^2 / 4 \rfloor + 1$.
> It holds by induction on $n$, since $a(2^{n+1}) = a(2^n) + a(2^n - 2)$ for $n \ge 1$ and
> $a(2^m - 2) = \lfloor (m+1)/2 \rfloor$ for $m \ge 1$.

```lean
theorem conjecture1_value (n : ℕ) : a (2^n) = n ^ 2 / 4 + 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/112970.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean#L87).

## `OeisA112970.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L56-L64](https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L56-L64).

> Conjecture: $a(2^n-1)=a(3*2^n-1)=1$.
> This formalizes the equality part $a(2^n-1) = a(3*2^n-1)$.

```lean
theorem conjecture2 (n : ℕ) : a (2^n - 1) = a (3 * 2^n - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/112970.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean#L98).

## `OeisA112970.conjecture3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L48-L54](https://github.com/KitaKen1/oeis-a112970-formal-conjectures/blob/71ae72f443bd9bee7d958f0a19d9f9ec5ab82af5/lean/OeisA112970FC.lean#L48-L54).

> Conjecture: $a(2^n-1)=a(3*2^n-1)=1$. This formalizes the value part $a(2^n-1)=1$.

```lean
theorem conjecture3 (n : ℕ) : a (2^n - 1) = 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/112970.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/112970.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112970.lean)
- [A112970](https://oeis.org/A112970)
