---
declaration: theorem
origin: cited
lean: Erdos470.erdos_470.parts.i, Erdos470.erdos_470.parts.ii, Erdos470.erdos_470.variants.weird_pos_density, Erdos470.erdos_470.variants.smallest_weird_eq_70, Erdos470.erdos_470.variants.prime_gap_imp_inf_prim_weird, Erdos470.erdos_470.variants.odd_weird_10_pow_21, Erdos470.erdos_470.variants.odd_weird_prime_div, Erdos470.erdos_470.variants.abundancy_index
statement: formalized
---

# Erdős Problem 470

> *Reference:* [erdosproblems.com/470](https://www.erdosproblems.com/470)

*Quoted from [FormalConjectures/ErdosProblems/470.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/470](https://www.erdosproblems.com/470).

The file states 8 research or textbook statements: 2 open, 5 solved and 1 textbook result.

## `Erdos470.erdos_470.parts.i`

Open: stated without proof.

> Are there any odd weird numbers?

```lean
theorem erdos_470.parts.i : ∃ n : ℕ, n.Weird ∧ Odd n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L44).

## `Erdos470.erdos_470.parts.ii`

Open: stated without proof.

> Are there infinitely many primitive weird numbers?

```lean
theorem erdos_470.parts.ii : Set.Infinite PrimitiveWeird
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L51).

## `Erdos470.erdos_470.variants.weird_pos_density`

Solved: stated here without proof.

> Benkoski and Erdős [BeEr74](https://mathscinet.ams.org/mathscinet/relay-station?mr=347726) proved
> that the set of weird numbers has positive density.
>
> `HasPosDensity` is the right reading here, rather than the positive *lower* density that Erdős'
> "positive density" usually abbreviates. Their Theorem 5 is stated as "the density of weird
> numbers is positive", and they first establish that the density exists at all: "It is clear that
> the weird numbers have a density since both the abundant numbers and the pseudoperfect numbers
> have a density. (A weird number is abundant and not pseudoperfect.)" The work in the paper goes
> into showing that density is not `0`.

```lean
theorem erdos_470.variants.weird_pos_density : {n : ℕ | n.Weird}.HasPosDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L66).

## `Erdos470.erdos_470.variants.smallest_weird_eq_70`

Textbook result, proved here.

> The smallest weird number is 70.

```lean
theorem erdos_470.variants.smallest_weird_eq_70 : (∀ n < 70, ¬n.Weird) ∧ (70).Weird
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L73).

## `Erdos470.erdos_470.variants.prime_gap_imp_inf_prim_weird`

Solved: stated here without proof.

> Melfi [Me15](https://mathscinet.ams.org/mathscinet/relay-station?mr=3276337) has proved that there
> are infinitely many primitive weird numbers, conditional on the fact that
> $p_{n+1} - p_n < \frac{1}{10} \sqrt{p_n}$ for all large $n$, which in turn would follow from
> well-known conjectures concerning prime gaps.

```lean
theorem erdos_470.variants.prime_gap_imp_inf_prim_weird :
    (∀ᶠ n in Filter.atTop, primeGap n < √ (n.nth Nat.Prime) / 10) →
      Set.Infinite PrimitiveWeird
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L104).

## `Erdos470.erdos_470.variants.odd_weird_10_pow_21`

Solved: stated here without proof.

> Fang [Fa22](https://arxiv.org/abs/2207.12906) has shown there are no odd weird numbers below $10^{21}$.

```lean
theorem erdos_470.variants.odd_weird_10_pow_21 : ∀ n < 10 ^ 21, Odd n → ¬n.Weird
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L113).

## `Erdos470.erdos_470.variants.odd_weird_prime_div`

Solved: stated here without proof.

> Liddy and Riedl [LiRi18](https://ideaexchange.uakron.edu/honors_research_projects/728/) have shown
> that an odd weird number must have at least 6 prime divisors.

```lean
theorem erdos_470.variants.odd_weird_prime_div :
    ∀ n : ℕ, Odd n → n.Weird → 6 ≤ {m | m ∈ n.divisors ∧ m.Prime}.ncard
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L121).

## `Erdos470.erdos_470.variants.abundancy_index`

Solved: stated here; a Lean proof is at [https://github.com/HowieHwong/lean-erdos-proofs/blob/40216cfee225ec5c9f122a48703e671a9f47db90/Erdos/P470.lean#L88](https://github.com/HowieHwong/lean-erdos-proofs/blob/40216cfee225ec5c9f122a48703e671a9f47db90/Erdos/P470.lean#L88).

> If there are no odd weird numbers then every weird number has abundancy index < 4.

```lean
theorem erdos_470.variants.abundancy_index :
    (∀ n : ℕ, n.Weird → ¬Odd n) → ∀ n, n.Weird → AbundancyIndex n < 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/470.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/470.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/470.lean)
- [erdosproblems.com/470](https://www.erdosproblems.com/470)
