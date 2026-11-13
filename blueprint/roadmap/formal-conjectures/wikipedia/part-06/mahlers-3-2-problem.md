---
declaration: theorem
origin: cited
lean: Mahler32.mahler_conjecture, Mahler32.mahler_conjecture.variants.consequence, Mahler32.mahler_conjecture.variants.flatto_lagarias_pollington
statement: formalized
---

# Mahler's 3/2 Problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Mahler%27s_3/2_problem)

*Quoted from [FormalConjectures/Wikipedia/Mahler32.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Mahler32.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result.

## `Mahler32.mahler_conjecture`

Open: stated without proof.

> The **Mahler Conjecture** states that there are no Z-numbers.

```lean
theorem mahler_conjecture (x : ℝ) (hx : IsZNumber x) : False
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mahler32.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Mahler32.lean#L42).

## `Mahler32.mahler_conjecture.variants.consequence`

Textbook result, stated without proof.

> Mahler's conjecture would follow if `Ω(3/2)` exceeded `1/2`: a Z-number `x` has all
> fractional parts `{x (3/2)^n}` below `1/2`, so `Ω(3/2) ≤ 1/2`.

```lean
theorem mahler_conjecture.variants.consequence (H : 1 / 2 < Ω (3 / 2)) :
    type_of% mahler_conjecture
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mahler32.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Mahler32.lean#L48).

## `Mahler32.mahler_conjecture.variants.flatto_lagarias_pollington`

Solved: stated here without proof.

> Flatto, Lagarias and Pollington proved that for all rational `p/q > 1` in lowest terms with
> `q ≥ 2`, we have `Ω(p/q) ≥ 1/p`: for every `θ > 0`, the limit points of `{θ (p/q)^n}` are not
> contained in any interval of length less than `1/p`.

```lean
theorem mahler_conjecture.variants.flatto_lagarias_pollington (p q : ℕ) (hq : 1 < q)
    (hpq : p.Coprime q) (hpq' : q < p) : 1 / p ≤ Ω (p / q)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mahler32.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Mahler32.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Mahler32.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Mahler32.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Mahler%27s_3/2_problem)
