---
declaration: theorem
origin: cited
lean: UntouchableNumber.chen_zhao_untouchable_lower_density, UntouchableNumber.unique_odd_untouchable_conjecture
statement: formalized
---

# Untouchable Numbers

> A natural number $m$ is *untouchable* (or *nonaliquot*, OEIS A005114) when it lies outside the
> range of the proper-divisor sum $s(n) = \sigma(n) - n = \sum_{d \mid n,\, d < n} d$; examples begin
> at $2, 5$, and $52$.
>
> Erdős (1973) proved that untouchable integers have positive lower asymptotic density (see also
> `Erdos418.erdos_418.variants.sigma` in `FormalConjectures.ErdosProblems.«418»`), and Chen and Zhao
> (2011) proved that at least $0.06 x + o(x)$ even integers below $x$ are untouchable, giving lower
> asymptotic density at least $0.06$. Meanwhile, $5$ is conjectured to be the sole odd untouchable
> integer: writing an even integer $2k > 6$ as $p + q$ for distinct primes $p \ne q$ gives
> $s(p q) = 1 + p + q = 2k + 1$, ruling out every odd integer above $7$.
>
> *References:*
> - [Wikipedia: Untouchable number](https://en.wikipedia.org/wiki/Untouchable_number)
> - [OEIS A005114](https://oeis.org/A005114)
> - P. Erdős (1973), *Elem. Math.* **28**, 83–86.
> - Y.-G. Chen and Q.-Q. Zhao (2011), *Publ. Math. Debrecen*, vol. 78, 439–442.
> - R. K. Guy (2004), Section B10.

*Quoted from [FormalConjectures/Wikipedia/UntouchableNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/UntouchableNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements and 1 API statement, counted here but not shown.

## `UntouchableNumber.chen_zhao_untouchable_lower_density`

Solved: stated here without proof.

> **Erdős (1973); Chen–Zhao (2011):** Untouchable integers have lower asymptotic density at least
> $0.06$ (Chen and Zhao prove that at least $0.06 x + o(x)$ even integers below $x$ are nonaliquot;
> compare `Erdos418.erdos_418.variants.sigma`).

```lean
theorem chen_zhao_untouchable_lower_density :
    (6 / 100 : ℝ) ≤ Set.lowerDensity {m : ℕ | m.IsUntouchable}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/UntouchableNumber.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/UntouchableNumber.lean#L103).

## `UntouchableNumber.unique_odd_untouchable_conjecture`

Open: stated without proof.

> **Unique Odd Untouchable Conjecture:** Among odd integers, $5$ is the unique untouchable
> value.

```lean
theorem unique_odd_untouchable_conjecture {m : ℕ} (hodd : Odd m) :
    m.IsUntouchable ↔ m = 5
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/UntouchableNumber.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/UntouchableNumber.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/UntouchableNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/UntouchableNumber.lean)
- [Wikipedia: Untouchable number](https://en.wikipedia.org/wiki/Untouchable_number)
