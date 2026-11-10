---
declaration: theorem
origin: cited
lean: PartitionParity.kolberg, PartitionParity.parkin_shanks, PartitionParity.subbarao.even, PartitionParity.subbarao.odd, PartitionParity.ahlgren.even, PartitionParity.ahlgren.odd, PartitionParity.bellaiche_nicolas.even, PartitionParity.bellaiche_nicolas.even_explicit, PartitionParity.bellaiche_nicolas.odd_explicit, PartitionParity.bellaiche_green_soundararajan.odd, PartitionParity.ono_swaminathan.quadratic, PartitionParity.ono_swaminathan.odd_bound, PartitionParity.classNumber_eq_ncard_reducedForms, PartitionParity.zheng.liminf, PartitionParity.zheng.odd, PartitionParity.ono.polynomial
statement: formalized
---

# Parities of partition numbers

> There are several conjectures on parities of partition numbers. The most famous conjecture is the
> Parkin-Shanks conjecture, which states that the natural density of `n` where the partition number
> `p(n)` is even (resp. odd) exists and equals `1/2`.
>
> There are several related (weaker) results toward the conjecture. Kolberg showed that `p(n)` takes
> each parity infinitely often. Subbarao conjectured that every arithmetic progression `r (mod t)`
> contains infinitely many `n` with `p(n)` even and infinitely many `n` with `p(n)` odd; the even
> case was proved by Ono and the odd case by Radu. Quantitative lower bounds for the number of
> `n ≤ X` with `p(n)` even (resp. odd) have also been studied. The best known bounds are
> `≫ √X log log X` for even values (Bellaïche–Nicolas) and `≫ √X` for odd values (Zheng, in an
> appendix to Ono–Swaminathan). Ono–Swaminathan also proved that both parities occur infinitely often
> along the quadratic progressions `(D m² + 1) / 24`, and Ono conjectured the same for every nonconstant
> integer-valued polynomial that is eventually positive.
>
> *References:*
> * [On the distribution of parity in the partition function](https://www.jstor.org/stable/2003251),
>   T. R. Parkin, D. Shanks, Math. Comp. 21 (1967), 466–480.
> * [Note on the parity of the partition function](https://doi.org/10.7146/math.scand.a-10584),
>   O. Kolberg, Math. Scand. 7 (1959), 377–378.
> * Some remarks on the partition function, M. V. Subbarao, Amer. Math. Monthly 73 (1966), 851–854.
> * [Parity of the partition function in arithmetic progressions](https://doi.org/10.1515/crll.1996.472.1),
>   K. Ono, J. Reine Angew. Math. 472 (1996), 1–16.
> * [Distribution of parity of the partition function in arithmetic progressions](https://doi.org/10.1016/S0019-3577(99)80014-7),
>   S. Ahlgren, Indag. Math. (N.S.) 10 (1999), 173–181.
> * [Parity of the partition function](https://doi.org/10.1016/j.aim.2010.02.023), K. Ono,
>   Adv. Math. 225 (2010), 349–366.
> * [A proof of Subbarao's conjecture](https://doi.org/10.1515/CRELLE.2011.165), C.-S. Radu,
>   J. Reine Angew. Math. 672 (2012), 161–175.
> * [Parité des coefficients de formes modulaires](https://doi.org/10.1007/s11139-014-9645-9),
>   J. Bellaïche, J.-L. Nicolas, Ramanujan J. 40 (2016), 1–44.
> * [Nonzero coefficients of half-integral weight modular forms mod ℓ](https://arxiv.org/abs/1704.07440),
>   J. Bellaïche, B. Green, K. Soundararajan, Res. Math. Sci. 5 (2018), Paper No. 6.
> * [Parity of the partition function in quadratic progressions](https://arxiv.org/abs/2509.09553)
>   (with an appendix by Q.-Y. Zheng), K. Ono, A. Swaminathan, arXiv:2509.09553.
> * [Cox] D. A. Cox, Primes of the Form $x^2 + ny^2$, 2nd ed., Wiley, 2013.

*Quoted from [FormalConjectures/Paper/PartitionParity.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 16 research or textbook statements: 2 open, 13 solved and 1 textbook result.

## `PartitionParity.kolberg`

Solved: stated here without proof.

> `p(n)` is even for infinitely many `n` and odd for infinitely many `n`. (Kolberg)

```lean
theorem kolberg :
    {n : ℕ | Even (partitionNumber n)}.Infinite ∧ {n : ℕ | Odd (partitionNumber n)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L68).

## `PartitionParity.parkin_shanks`

Open: stated without proof.

> The natural density of `n` where the partition number `p(n)` is even (resp. odd) exists and
> equals `1/2`.

```lean
theorem parkin_shanks :
    {n : ℕ | Even (partitionNumber n)}.HasDensity (1 / 2) ∧
    {n : ℕ | Odd (partitionNumber n)}.HasDensity (1 / 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L75).

## `PartitionParity.subbarao.even`

Solved: stated here without proof.

> Every arithmetic progression contains infinitely many `n` where `p(n)` is even.
> Conjectured by Subbarao and proved by Ono.

```lean
theorem subbarao.even : ∀ r t, 0 < t →
    {n : ℕ | n ≡ r [MOD t] ∧ Even (partitionNumber n)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L83).

## `PartitionParity.subbarao.odd`

Solved: stated here without proof.

> Every arithmetic progression contains infinitely many `n` where `p(n)` is odd.
> Conjectured by Subbarao; Ono proved it for every progression containing at least one `n` with
> `p(n)` odd, and Radu showed that every progression contains such an `n`.

```lean
theorem subbarao.odd : ∀ r t, 0 < t →
    {n : ℕ | n ≡ r [MOD t] ∧ Odd (partitionNumber n)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L91).

## `PartitionParity.ahlgren.even`

Solved: stated here without proof.

> For every arithmetic progression `r (mod t)`, the number of `n ≤ X` with `n ≡ r (mod t)` and
> `p(n)` even is `≫ √X`. (Ahlgren)

```lean
theorem ahlgren.even : ∀ r t, 0 < t →
    (fun X : ℝ ↦ √X) =O[atTop]
      fun X : ℝ ↦ ({n : ℕ | n ≤ X ∧ n ≡ r [MOD t] ∧ Even (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L98).

## `PartitionParity.ahlgren.odd`

Solved: stated here without proof.

> For every arithmetic progression `r (mod t)`, the number of `n ≤ X` with `n ≡ r (mod t)` and
> `p(n)` odd is `≫ √X / log X`. Ahlgren proved this for every progression containing at least one
> `n` with `p(n)` odd; by Radu's theorem every progression does.

```lean
theorem ahlgren.odd : ∀ r t, 0 < t →
    (fun X : ℝ ↦ √X / X.log) =O[atTop]
      fun X : ℝ ↦ ({n : ℕ | n ≤ X ∧ n ≡ r [MOD t] ∧ Odd (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L107).

## `PartitionParity.bellaiche_nicolas.even`

Solved: stated here without proof.

> The number of `n ≤ X` with `p(n)` even is `≫ √X log log X`. (Bellaïche–Nicolas)

```lean
theorem bellaiche_nicolas.even :
    (fun X : ℝ ↦ √X * X.log.log) =O[atTop]
      fun X : ℝ ↦ ({n : ℕ | n ≤ X ∧ Even (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L114).

## `PartitionParity.bellaiche_nicolas.even_explicit`

Solved: stated here without proof.

> The number of `n ≤ x` with `p(n)` even is at least `0.069 √x log log x` for every `x > 1`.
> (Bellaïche–Nicolas)

```lean
theorem bellaiche_nicolas.even_explicit : ∀ x : ℝ, 1 < x →
    0.069 * √x * x.log.log ≤ ({n : ℕ | n ≤ x ∧ Even (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L122).

## `PartitionParity.bellaiche_nicolas.odd_explicit`

Solved: stated here without proof.

> The number of `n ≤ x` with `p(n)` odd is at least `0.037 √x / (log x)^(7/8)` for every `x ≥ 2`.
> (Bellaïche–Nicolas)

```lean
theorem bellaiche_nicolas.odd_explicit : ∀ x : ℝ, 2 ≤ x →
    0.037 * √x / (x.log) ^ (7 / 8 : ℝ) ≤ ({n : ℕ | n ≤ x ∧ Odd (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L129).

## `PartitionParity.bellaiche_green_soundararajan.odd`

Solved: stated here without proof.

> The number of `n ≤ X` with `p(n)` odd is `≫ √X / log log X`.
> (Bellaïche–Green–Soundararajan)

```lean
theorem bellaiche_green_soundararajan.odd :
    (fun X : ℝ ↦ √X / X.log.log) =O[atTop]
      fun X : ℝ ↦ ({n : ℕ | n ≤ X ∧ Odd (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L136).

## `PartitionParity.ono_swaminathan.quadratic`

Solved: stated here without proof.

> For square-free `D > 1` with `D ≡ 23 (mod 24)`, both parities occur infinitely often among
> `p((D m² + 1) / 24)` as `m` ranges over the positive integers coprime to `6`. Note that
> `24 ∣ D m² + 1` for such `m`. Conjectured by Ono and proved by Ono–Swaminathan.

```lean
theorem ono_swaminathan.quadratic : ∀ D : ℕ, 1 < D → Squarefree D → D % 24 = 23 →
    {m : ℕ | m.Coprime 6 ∧ Even (partitionNumber ((D * m ^ 2 + 1) / 24))}.Infinite ∧
    {m : ℕ | m.Coprime 6 ∧ Odd (partitionNumber ((D * m ^ 2 + 1) / 24))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L145).

## `PartitionParity.ono_swaminathan.odd_bound`

Solved: stated here without proof.

> The odd half of Theorem 1 of Ono–Swaminathan, with its effective bound: for square-free `D > 1`
> with `D ≡ 23 (mod 24)` there is an `m` coprime to `6` with `m ≤ 12 h(-D) + 2` such that
> `p((D m² + 1) / 24)` is odd, where `h(-D)` is the class number of `ℚ(√-D)`. Here `ℚ(√-D)` is
> `AdjoinRoot (X ^ 2 + D)`, a number field since `X ^ 2 + D` is irreducible over `ℚ` for `D > 0`.

```lean
theorem ono_swaminathan.odd_bound (D : ℕ) (hD : 1 < D) (hsq : Squarefree D) (h23 : D % 24 = 23) :
    haveI : Fact (Irreducible (X ^ 2 + C (D : ℚ))) :=
      ⟨irreducible_X_sq_add_C_of_pos (Nat.cast_pos.2 (by lia))⟩
    ∃ m : ℕ, m.Coprime 6 ∧
      m ≤ 12 * NumberField.classNumber (AdjoinRoot (X ^ 2 + C (D : ℚ))) + 2 ∧
      Odd (partitionNumber ((D * m ^ 2 + 1) / 24))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L155).

## `PartitionParity.classNumber_eq_ncard_reducedForms`

Textbook result, stated without proof.

> For square-free `D ≡ 3 (mod 4)`, the discriminant `-D` is fundamental and the class number of
> `ℚ(√-D)` equals the number of reduced primitive positive-definite binary quadratic forms of
> discriminant `-D` [Cox, Theorem 2.8].
> This identification is used in Zheng's appendix to Ono–Swaminathan.

```lean
theorem classNumber_eq_ncard_reducedForms (D : ℕ) (hsq : Squarefree D) (h3 : D % 4 = 3) :
    haveI : Fact (Irreducible (X ^ 2 + C (D : ℚ))) :=
      ⟨irreducible_X_sq_add_C_of_pos (Nat.cast_pos.2 (by lia))⟩
    NumberField.classNumber (AdjoinRoot (X ^ 2 + C (D : ℚ))) =
      {⟨a, b, c⟩ : ℤ × ℤ × ℤ | IsReducedForm D a b c}.ncard
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L174).

## `PartitionParity.zheng.liminf`

Solved: stated here; a Lean proof assuming `ono_swaminathan.odd_bound`, `classNumber_eq_ncard_reducedForms` is at [https://github.com/AxiomMath/PartitionZheng/blob/9bfb4326c4ea1e00016a842d7cc145e5c4e0684a/Solution/Basic.lean#L17](https://github.com/AxiomMath/PartitionZheng/blob/9bfb4326c4ea1e00016a842d7cc145e5c4e0684a/Solution/Basic.lean#L17).

> Zheng's explicit lower bound: `liminf_{X → ∞} N_odd(X) / √X ≥ 243 / (64 √6 π⁵)`, where
> `N_odd(X)` is the number of `n ≤ X` with `p(n)` odd [Ono-Swaminathan, Appendix A, Corollary 2].

```lean
theorem zheng.liminf :
    ((243 / (64 * √6 * π ^ 5) : ℝ) : EReal) ≤
      liminf (fun X : ℝ ↦
        ((({n : ℕ | n ≤ X ∧ Odd (partitionNumber n)}.ncard : ℝ) / √X : ℝ) : EReal)) atTop
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 188](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L188).

## `PartitionParity.zheng.odd`

Solved: stated here without proof.

> The number of `n ≤ X` with `p(n)` odd is `≫ √X`.

```lean
theorem zheng.odd :
    (fun X : ℝ ↦ √X) =O[atTop]
      fun X : ℝ ↦ ({n : ℕ | n ≤ X ∧ Odd (partitionNumber n)}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 196](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L196).

## `PartitionParity.ono.polynomial`

Open: stated without proof.

> Ono's conjecture, as stated in Section 1 of Ono–Swaminathan: if `g` is a nonconstant
> integer-valued polynomial that is eventually positive, then `p(g(n))` is even for infinitely many
> `n` and odd for infinitely many `n`.

```lean
theorem ono.polynomial (g : ℚ[X]) (hg : 0 < g.natDegree)
    (hint : ∀ n : ℕ, ∃ k : ℤ, g.eval (n : ℚ) = k)
    (hpos : ∀ᶠ n : ℕ in atTop, 0 < g.eval (n : ℚ)) :
    {n : ℕ | Even (partitionNumber ⌊g.eval (n : ℚ)⌋₊)}.Infinite ∧
    {n : ℕ | Odd (partitionNumber ⌊g.eval (n : ℚ)⌋₊)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PartitionParity.lean, line 205](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean#L205).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/PartitionParity.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PartitionParity.lean)
- [On the distribution of parity in the partition function](https://www.jstor.org/stable/2003251)
