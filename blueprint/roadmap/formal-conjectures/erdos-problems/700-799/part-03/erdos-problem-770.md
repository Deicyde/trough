---
declaration: theorem
origin: cited
lean: Erdos770.Nat.Prime.h_eq_add_one, Erdos770.erdos_770.variants.odd_h_unbounded, Erdos770.erdos_770.parts.i, Erdos770.erdos_770.parts.ii, Erdos770.erdos_770.parts.iii, Erdos770.erdos_770.variants.three
statement: formalized
---

# Erdős Problem 770

> *References:*
>  - [erdosproblems.com/770](https://www.erdosproblems.com/770)
>  - [Er49d] Erdös, P. "On the strong law of large numbers." Transactions of the American Mathematical
>     Society 67.1 (1949): 51-56.
>  - [Ma66] Matsuyama, Noboru. "On the strong law of large numbers." Tohoku Mathematical Journal,
>     Second Series 18.3 (1966): 259-269.

*Quoted from [FormalConjectures/ErdosProblems/770.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/770](https://www.erdosproblems.com/770).

The file states 6 research or textbook statements: 4 open and 2 textbook results.

## `Erdos770.Nat.Prime.h_eq_add_one`

Textbook result, stated without proof.

> `n + 1` is prime iff `h n = n + 1`. This is described as 'easy to see' in [Er74b].

```lean
theorem Nat.Prime.h_eq_add_one {n : ℕ} (hn : 2 < n) : h n = n + 1 ↔ (n + 1).Prime
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L45).

## `Erdos770.erdos_770.variants.odd_h_unbounded`

Textbook result, stated without proof.

> For odd `n`, the values of `h n` form an unbounded set.
> This is described as 'easy to see' in [Er74b].

```lean
theorem erdos_770.variants.odd_h_unbounded : Unbounded (· ≤ ·) (ENat.toNat '' (h '' Odd))
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L51).

## `Erdos770.erdos_770.parts.i`

Open: stated without proof.

> For every prime `p`, does the density of integers with `h n = p` exist?

```lean
theorem erdos_770.parts.i : ∀ p : ℕ, p.Prime → ∃ a, HasDensity {n | h n = p} a
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L57).

## `Erdos770.erdos_770.parts.ii`

Open: stated without proof.

> Does `liminf h n = ∞`?

```lean
theorem erdos_770.parts.ii : liminf h atTop = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L62).

## `Erdos770.erdos_770.parts.iii`

Open: stated without proof.

> Is it true that if `p` is the greatest prime such that `p - 1 ∣ n` and `p > n ^ ε`, then
> `h n = p`?

```lean
theorem erdos_770.parts.iii : ∀ ε > 0, ∀ᶠ n in atTop,
    let p := sSup {m : ℕ | m.Prime ∧ m - 1 ∣ n}
    p > (n : ℝ) ^ (ε : ℝ) → h n = p
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L68).

## `Erdos770.erdos_770.variants.three`

Open: stated without proof.

> It is probably true that `h n = 3` for infinitely many `n`.

```lean
theorem erdos_770.variants.three : {n | h n = 3}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/770.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/770.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/770.lean)
- [erdosproblems.com/770](https://www.erdosproblems.com/770)
