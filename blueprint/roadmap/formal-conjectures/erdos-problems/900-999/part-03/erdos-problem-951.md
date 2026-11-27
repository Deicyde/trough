---
declaration: theorem
origin: cited
lean: Erdos951.erdos_951, Erdos951.erdos_951.variants.beurling
statement: formalized
---

# Erdős Problem 951

> *References:*
>  - [erdosproblems.com/951](https://www.erdosproblems.com/951)
>  - [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day (Proc. Conf., Rockefeller Univ.,
>     New York, 1976) (1977), 43-72.

*Quoted from [FormalConjectures/ErdosProblems/951.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/951.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/951](https://www.erdosproblems.com/951).

The file states 2 research or textbook statements: 2 open. It also has 1 API statement, counted here but not shown.

## `Erdos951.erdos_951`

Open: stated without proof.

> If `1 < a 0 < ...` has property `Erdos951Prop`, is it true that `#{a i ≤ x} ≤ π x` for all
> sufficiently large $x$?

```lean
theorem erdos_951 :
    ∀ a : ℕ → ℝ, 1 < a 0 → StrictMono a → Erdos951Prop a →
      ∀ᶠ (x : ℝ) in Filter.atTop, {i : ℕ | a i ≤ x}.ncard ≤ π ⌊x⌋₊
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/951.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/951.lean#L63).

## `Erdos951.erdos_951.variants.beurling`

Open: stated without proof.

> Beurling conjectured that if $1 < a_0 < a_1 < \cdots$ is a sequence of Beurling primes and
> the number of generalised integers $\prod_i a_i^{k_i} \le x$ (counted with multiplicity) is
> $x + o(\log x)$, then $a$ must be the sequence of primes. Counting with multiplicity is needed
> because without it $a_n = n + 2$ is a counterexample (its set of generalised integers is
> $\mathbb{N}_{\ge 1}$, giving count $\lfloor x \rfloor = x + O(1)$).

```lean
theorem erdos_951.variants.beurling :
    ∀ a : ℕ → ℝ, IsBeurlingPrimes a →
      ((fun x => ({k : ℕ →₀ ℕ | beurlingInteger a k ≤ x}.ncard : ℝ) - x) =o[atTop] Real.log) →
      a = Nat.cast ∘ Nat.nth Nat.Prime
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/951.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/951.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/951.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/951.lean)
- [erdosproblems.com/951](https://www.erdosproblems.com/951)
