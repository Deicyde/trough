---
declaration: theorem
origin: cited
lean: OeisA69004.conjecture1, OeisA69004.conjecture2, OeisA69004.conjecture2.variants.upper_bound_false, OeisA69004.conjecture2.variants.without_upper_bound
statement: formalized
---

# Number of times $n^2 + s^2$ is prime for positive integers $s < n$

> The sequence $a(n)$ counts the number of integers $s \in \{1, \dots, n-1\}$ such that
> $n^2 + s^2$ is prime:
>
> $$a(n) = \sum_{s=1}^{n-1} [\text{Prime}(n^2 + s^2)]$$
>
> *References:*
> - [A069004](https://oeis.org/A069004)
> - [CE26] j2d9w5xtjn-png, [Counterexample to the upper bound](https://github.com/google-deepmind/formal-conjectures/pull/5453), 2026.
> - [Li26] Wentao Li, [Lean certificate for the A069004 counterexample](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/a16a2711b082ccab4ba941330148e7b7c78b11c1/proofs/new-formalization/A069004/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/69004.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA69004.conjecture1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture1 (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69004.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean#L71).

## `OeisA69004.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/a16a2711b082ccab4ba941330148e7b7c78b11c1/LeanOeisProofs/NewFormalization/A069004.lean#L58](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/a16a2711b082ccab4ba941330148e7b7c78b11c1/LeanOeisProofs/NewFormalization/A069004.lean#L58).

> Stronger conjecture: Let pi(n) be the prime counting function (A000720). Then
> pi(n) >= a(n) >= pi(n)/5 for n>1, with the following equalities: pi(2)=a(2),
> pi(10)=a(10) and a(12)=pi(12)/5.
> - T. D. Noe, Feb 26 2007
>
> This conjunction is false. The upper bound fails at $n = 512720$:
> a Lean certificate proves $a(512720) \ge 42494 > 42493 = \pi(512720)$.
> The counterexample was recorded by j2d9w5xtjn-png [CE26].
>
> Lean formalization by Wentao Li, with AI assistance, adapting Epoch Research's
> certificate attempt; see [Li26].

```lean
theorem conjecture2 : ¬ (
    (∀ n : ℕ, 1 < n → Nat.primeCounting n ≥ a n) ∧
    (∀ n : ℕ, 1 < n → 5 * a n ≥ Nat.primeCounting n) ∧
    Nat.primeCounting 2 = a 2 ∧
    Nat.primeCounting 10 = a 10 ∧
    5 * a 12 = Nat.primeCounting 12)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69004.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean#L90).

## `OeisA69004.conjecture2.variants.upper_bound_false`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/a16a2711b082ccab4ba941330148e7b7c78b11c1/LeanOeisProofs/NewFormalization/A069004.lean#L49](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/a16a2711b082ccab4ba941330148e7b7c78b11c1/LeanOeisProofs/NewFormalization/A069004.lean#L49).

> The upper bound from T. D. Noe's stronger conjecture: "pi(n) >= a(n)" for "n>1".
> It is false at $n = 512720$: $a(512720) \ge 42494 > 42493 = \pi(512720)$.
> The counterexample was recorded by j2d9w5xtjn-png [CE26].
>
> Lean formalization by Wentao Li, with AI assistance, adapting Epoch Research's
> certificate attempt; see [Li26].

```lean
theorem conjecture2.variants.upper_bound_false :
    ¬ ∀ n : ℕ, 1 < n → Nat.primeCounting n ≥ a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69004.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean#L109).

## `OeisA69004.conjecture2.variants.without_upper_bound`

Open: stated without proof.

> The part of the stronger conjecture that survives the counterexample to its upper bound:
> $5 a(n) \ge \pi(n)$ for $n > 1$, together with the three claimed equalities
> $\pi(2) = a(2)$, $\pi(10) = a(10)$ and $a(12) = \pi(12)/5$.

```lean
theorem conjecture2.variants.without_upper_bound :
    (∀ n : ℕ, 1 < n → 5 * a n ≥ Nat.primeCounting n) ∧
    Nat.primeCounting 2 = a 2 ∧
    Nat.primeCounting 10 = a 10 ∧
    5 * a 12 = Nat.primeCounting 12
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69004.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/69004.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69004.lean)
- [A069004](https://oeis.org/A069004)
