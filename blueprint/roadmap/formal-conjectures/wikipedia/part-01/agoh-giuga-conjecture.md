---
declaration: theorem
origin: cited
lean: AgohGiuga.agoh_giuga, AgohGiuga.agoh_giuga.variants.giuga, AgohGiuga.agoh_giuga.variants.equivalence, AgohGiuga.isWeakGiuga_iff_prime_dvd, AgohGiuga.isWeakGiuga_iff_sum_primeFactors, AgohGiuga.squarefree_of_isCarmichael, AgohGiuga.korselts_criterion, AgohGiuga.isStrongGiuga_iff, AgohGiuga.agoh_giuga.variants.isStrongGiuga_implies_isCarmichael, AgohGiuga.agoh_giuga.variants.le_primeFactors_card_of_isStrongGiuga, AgohGiuga.agoh_giuga.variants._1000_le_digits_length_of_isStrongGiuga, AgohGiuga.agoh_giuga.variants._1700_le_digits_length_of_isStrongGiuga, AgohGiuga.agoh_giuga.variants._13000_le_digits_length_of_isStrongGiuga, AgohGiuga.agoh_giuga.variants.isStrongGiuga_growth
statement: formalized
---

# Agoh-Giuga conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Agoh-Giuga_conjecture)

*Quoted from [FormalConjectures/Wikipedia/AgohGiuga.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 14 research or textbook statements: 2 open, 10 solved and 2 textbook results. It also has 1 test statement, counted here but not shown.

## `AgohGiuga.agoh_giuga`

Open: stated without proof.

> The **Agoh-Giuga Conjecture**, Agoh's formulation

```lean
theorem agoh_giuga : AgohGiugaCongr
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L65).

## `AgohGiuga.agoh_giuga.variants.giuga`

Open: stated without proof.

> The **Agoh-Giuga Conjecture**, Giuga's formulation

```lean
theorem agoh_giuga.variants.giuga : AgohGiugaSum
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L70).

## `AgohGiuga.agoh_giuga.variants.equivalence`

Solved: stated here without proof.

> The two statements of the conjecture are equivalent.

```lean
theorem agoh_giuga.variants.equivalence : AgohGiugaCongr ↔ AgohGiugaSum
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L75).

## `AgohGiuga.isWeakGiuga_iff_prime_dvd`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/Wikipedia/AgohGiuga.lean#L97](https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/Wikipedia/AgohGiuga.lean#L97).

> A composite number $n$ is weak Giuga if and only if $p \mid (\frac{n}{p} - 1)$ for all
> prime divisors $p$ of $n$.

```lean
theorem isWeakGiuga_iff_prime_dvd {n : ℕ} (hn : n.Composite) :
    IsWeakGiuga n ↔ ∀ p ∈ n.primeFactors, p ∣ (n / p - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L102).

## `AgohGiuga.isWeakGiuga_iff_sum_primeFactors`

Solved: stated here without proof.

> A composite number $n$ is weak Giuga if and only if
>
> $$
> \sum_{p\mid n} \frac{1}{p} - \frac{1}{n} \in\mathbb{N}.
> $$

```lean
theorem isWeakGiuga_iff_sum_primeFactors {n : ℕ} (hn : n.Composite) :
    IsWeakGiuga n ↔ ∃ m : ℕ, ∑ p ∈ n.primeFactors, (1 / p : ℚ) - 1 / n = m
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L113).

## `AgohGiuga.squarefree_of_isCarmichael`

Textbook result, proved here.

> A composite Carmichael number is squarefree.

```lean
theorem squarefree_of_isCarmichael {a : ℕ} (ha₁ : a.Composite) (ha₂ : IsCarmichael a) :
    Squarefree a
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L119).

## `AgohGiuga.korselts_criterion`

Textbook result, proved here.

> A composite number `a` is Carmichael if and only if it is squarefree
> and, for all prime `p` dividing `a`, we have `p - 1 ∣ a - 1`.

```lean
theorem korselts_criterion (a : ℕ) (ha₁ : a.Composite) :
    IsCarmichael a ↔ Squarefree a ∧
      ∀ p, p.Prime → p ∣ a → (p - 1 : ℕ) ∣ (a - 1 : ℕ)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L135).

## `AgohGiuga.isStrongGiuga_iff`

Solved: stated here without proof.

> Giuga showed that a number `n` is strong Giuga if and only if it is
> Carmichael and `∑_{p|n} 1/p - 1/n ∈ ℕ` (i.e., if and only if it is Carmichael
> and weak Giuga).
> Ref: G. Giuga, _Su una presumibile proprieta caratteristica dei numeri primi_

```lean
theorem isStrongGiuga_iff {a : ℕ} (ha : a.Composite) :
    IsStrongGiuga a ↔ IsCarmichael a ∧ ∃ n : ℕ, ∑ p ∈ a.primeFactors, (1 / p : ℚ) - 1 / a = n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L207).

## `AgohGiuga.agoh_giuga.variants.isStrongGiuga_implies_isCarmichael`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_AgohGiuga_agoh_giuga_variants_isStrongGiuga_implies_isCarmichael.lean#L283](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_AgohGiuga_agoh_giuga_variants_isStrongGiuga_implies_isCarmichael.lean#L283).

> Every strong Giuga number is a Carmichael number.

```lean
theorem agoh_giuga.variants.isStrongGiuga_implies_isCarmichael
    (a : ℕ) (ha : IsStrongGiuga a) : IsCarmichael a
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 216](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L216).

## `AgohGiuga.agoh_giuga.variants.le_primeFactors_card_of_isStrongGiuga`

Solved: stated here without proof.

> Giuga showed that a Giuga number has at least 9 prime factors.
> Ref: G. Giuga, _Su una presumibile proprieta caratteristica dei numeri primi_

```lean
theorem agoh_giuga.variants.le_primeFactors_card_of_isStrongGiuga
    (a : ℕ) (ha : IsStrongGiuga a) : 9 ≤ a.primeFactors.card
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 225](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L225).

## `AgohGiuga.agoh_giuga.variants._1000_le_digits_length_of_isStrongGiuga`

Solved: stated here without proof.

> Giuga showed that a counterexample Giuga number has at least 1000 digits.
> Ref: G. Giuga, _Su una presumibile proprieta caratteristica dei numeri primi_

```lean
theorem agoh_giuga.variants._1000_le_digits_length_of_isStrongGiuga
    (a : ℕ) (ha : IsStrongGiuga a) : 1000 ≤ (Nat.digits 10 a).length
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 234](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L234).

## `AgohGiuga.agoh_giuga.variants._1700_le_digits_length_of_isStrongGiuga`

Solved: stated here without proof.

> Bedocchi showed that any Giuga number has at least 1700 digits.
> Ref: E. Bedocchi, _Note on a conjecture about prime numbers_

```lean
theorem agoh_giuga.variants._1700_le_digits_length_of_isStrongGiuga
    (a : ℕ) (ha : IsStrongGiuga a) :
    (Nat.digits 10 a).length > 1700
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 243](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L243).

## `AgohGiuga.agoh_giuga.variants._13000_le_digits_length_of_isStrongGiuga`

Solved: stated here without proof.

> Borwein, Borwein, Borwein and Girgensohn showed that any strong Giuga
> number has at least 13000 digits.
> Ref: D. Borwein, J. M. Borwein, P. B. Borwein, and R. Girgensohn, _Giuga’s conjecture on primality_

```lean
theorem agoh_giuga.variants._13000_le_digits_length_of_isStrongGiuga
    (a : ℕ) (ha : IsStrongGiuga a) : 13000 ≤ (Nat.digits 10 a).length
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 254](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L254).

## `AgohGiuga.agoh_giuga.variants.isStrongGiuga_growth`

Solved: stated here without proof.

> Let `G(X)` denote the number of exceptions `n ≤ X` to Giuga’s conjecture.
> Then for `X` larger than an absolute constant which can be made
> explicit, `G(X) ≪ X^{1/2} log X`.
> Ref: Vicentiu Tipu, _A Note on Giuga’s Conjecture_

```lean
theorem agoh_giuga.variants.isStrongGiuga_growth
    (G : ℕ → ℕ) (hG : G = fun x => Finset.Icc 1 x |>.filter IsStrongGiuga |>.card) :
    ∃ N O, ∀ n ≥ N, G n ≤ O * (n : ℝ).sqrt * (n : ℝ).log
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AgohGiuga.lean, line 266](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean#L266).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AgohGiuga.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AgohGiuga.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Agoh-Giuga_conjecture)
