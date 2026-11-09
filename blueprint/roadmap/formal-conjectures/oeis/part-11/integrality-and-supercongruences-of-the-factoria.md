---
declaration: theorem
origin: cited
lean: OeisA211417.thirty_mul_sub_one_dvd_a, OeisA211417.seven_mul_a_dvd_two_mul_add_one, OeisA211417.a_dvd_three_mul_add_one, OeisA211417.a_dvd_five_mul_add_one, OeisA211417.forty_two_mul_a_dvd_product, OeisA211417.general_divisibility, OeisA211417.supercongruence
statement: formalized
---

# Integrality and supercongruences of the factorial ratio $\frac{(6n)! n!}{(3n)! (2n)!^2}$

> Integral factorial ratio sequence:
>
> $$a(n) = \frac{(30n)! n!}{(15n)! (10n)! (6n)!}$$
>
> *References:*
> - [A211417](https://oeis.org/A211417)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [Me11] R. Meštrović, *Wolstenholme's theorem: Its Generalizations and Extensions in the last
>   hundred and fifty years (1862-2012)*, [arXiv:1111.3057](https://arxiv.org/abs/1111.3057) (2011).

*Quoted from [FormalConjectures/OEIS/211417.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 7 solved. It also has 5 test statements, counted here but not shown.

## `OeisA211417.thirty_mul_sub_one_dvd_a`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/211417.wip.lean#L243](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/211417.wip.lean#L243).

> It appears that $a(n)/(30n - 1)$ is integral for all $n$ (checked up to $n = 1000$). - _Peter Bala_, Aug 28 2025
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem thirty_mul_sub_one_dvd_a (n : ℕ) : (30 * (n : ℤ) - 1) ∣ (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L85).

## `OeisA211417.seven_mul_a_dvd_two_mul_add_one`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L866-L868](https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L866-L868).

> Conjecture: "7*a(n)/(2*n + 1) ... [is an] integer for all n (checked up to n = 1000)."
> - _Peter Bala_, Aug 28 2025

```lean
theorem seven_mul_a_dvd_two_mul_add_one (n : ℕ) :
    (2 * (n : ℤ) + 1) ∣ 7 * (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L96).

## `OeisA211417.a_dvd_three_mul_add_one`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1173-L1175](https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1173-L1175).

> Conjecture: "a(n)/(3*n + 1) ... [is an] integer for all n (checked up to n = 1000)."
> - _Peter Bala_, Aug 28 2025

```lean
theorem a_dvd_three_mul_add_one (n : ℕ) :
    (3 * (n : ℤ) + 1) ∣ (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L108).

## `OeisA211417.a_dvd_five_mul_add_one`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1446-L1448](https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1446-L1448).

> Conjecture: "a(n)/(5*n + 1) ... [is an] integer for all n (checked up to n = 1000)."
> - _Peter Bala_, Aug 28 2025

```lean
theorem a_dvd_five_mul_add_one (n : ℕ) :
    (5 * (n : ℤ) + 1) ∣ (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L120).

## `OeisA211417.forty_two_mul_a_dvd_product`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1514-L1524](https://github.com/KitaKen1/oeis-a211417/blob/cad1fb228b5b80573cab3eeb92c8be57fd73c506/lean/OeisA211417FC.lean#L1514-L1524).

> Conjecture: "42*a(n)/((2*n + 1)*(3*n + 1)*(5*n + 1)) [is an] integer for all n
> (checked up to n = 1000)." - _Peter Bala_, Aug 28 2025

```lean
theorem forty_two_mul_a_dvd_product (n : ℕ) :
    ((2 * (n : ℤ) + 1) * (3 * (n : ℤ) + 1) * (5 * (n : ℤ) + 1)) ∣
      42 * (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L132).

## `OeisA211417.general_divisibility`

Solved: stated here; a Lean proof is at [https://github.com/chy4pro/formal-conjectures/blob/fbc6706451b0e80787580d91ee6c252c121e0165/FormalConjectures/OEIS/211417.lean#L555](https://github.com/chy4pro/formal-conjectures/blob/fbc6706451b0e80787580d91ee6c252c121e0165/FormalConjectures/OEIS/211417.lean#L555).

> Conjecture: "More generally, for r >= 1, we conjecture that there exists a constant D(r) such that
> D(r)*a(n)/Product_{i = 1..r, i coprime to 30} (30*n - i) is integral for all n."
> - _Peter Bala_, Aug 28 2025
>
> This generalizes `thirty_mul_sub_one_dvd_a` (the $r = 1$ case where $D(1) = 1$).
>
> **Proof sketch** (kernel-checked development at the `formal_proof` permalink below, which
> proves the non-vacuous form with the explicit positive witness $D = (r!)^{r^2}$):
> Legendre-valuation analysis of the Landau step function
> $\Delta(x) = \lfloor 30x \rfloor + \lfloor x \rfloor - \lfloor 15x \rfloor -
> \lfloor 10x \rfloor - \lfloor 6x \rfloor$, whose values lie in $\{0, 1\}$. Three
> ingredients: a unit-class rigidity lemma ($\Delta_c = 1$ for every unit class $c$ modulo
> $30$), a witness-uniqueness bound for prime powers $p^k > r$ (at most one factor of the
> divisor product is divisible by $p^k$), and a uniform low-layer budget for $p^k \le r$
> absorbed by the witness constant.

```lean
theorem general_divisibility (r : ℕ) (hr : 1 ≤ r) :
    ∃ D : ℤ, 0 < D ∧ ∀ n : ℕ, (divisorProduct n r) ∣ (D * (a n : ℤ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L157).

## `OeisA211417.supercongruence`

Solved: stated here; a Lean proof is at [https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/OeisA211417.lean#L848](https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/OeisA211417.lean#L848).

> Supercongruence: "a(p^k) == a(p^(k-1)) ( mod p^(3*k) ) for any prime p >= 5 and any positive
> integer k." - _Peter Bala_, Jan 24 2020
>
> More generally, "the congruences a(n*p^k) == a(n*p^(k-1)) ( mod p^(3*k) ) may hold for any
> prime p >= 5 and any positive integers n and k."
>
> The same OEIS comment (Peter Bala, Jan 24 2020) already sketches an informal proof of the
> supercongruence: write
> $a(n) = \binom{30n}{15n}\binom{15n}{5n} / \binom{6n}{n}$ and apply [Me11, eq. (39), p. 12].
>
> Solved: a Lean 4 proof, derived from the Atlas proofs in
> [facebookresearch/atlas-lean](https://github.com/facebookresearch/atlas-lean), is linked in
> `formal_proof`.

```lean
theorem supercongruence (p k : ℕ) (hp : p.Prime) (hp5 : 5 ≤ p) (hk : 0 < k) :
    (p : ℤ) ^ (3 * k) ∣ ((a (p ^ k) : ℤ) - (a (p ^ (k - 1)) : ℤ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211417.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean#L180).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/211417.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/211417.lean)
- [A211417](https://oeis.org/A211417)
