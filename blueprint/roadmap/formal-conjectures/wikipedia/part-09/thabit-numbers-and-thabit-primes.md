---
declaration: theorem
origin: cited
lean: ThabitNumber.thabit_amicable_rule, ThabitNumber.infinitely_many_thabit_primes, ThabitNumber.exists_thabit_amicable_exponent_gt_seven
statement: formalized
---

# Thabit numbers and Thabit primes

> For $n \ge 0$, the $n$-th *Thabit number* (of the first kind) is $K_n = 3 \cdot 2^n - 1$. In the
> ninth century, Thābit ibn Qurra proved that whenever $n \ge 2$ makes $p = K_{n-1}$, $q = K_n$, and
> $r = 9 \cdot 2^{2n - 1} - 1$ simultaneously prime, the integers $2^n p q$ and $2^n r$ form an
> amicable pair (`IsAmicable`). Whether infinitely many Thabit primes exist, and whether Thābit ibn
> Qurra's rule produces any amicable pair beyond the three known exponents $n = 2, 4, 7$ [Bo72, Gu04],
> remain open.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Thabit_number)
> - [OEIS A055010](https://oeis.org/A055010)
> - [OEIS A007505](https://oeis.org/A007505)
> - [OEIS A002235](https://oeis.org/A002235)
> - [Bo72] Borho, W. (1972). *On Thabit ibn Kurrah's formula for amicable numbers*, Math. Comp. 26
>   (118), 571--578.
> - [Gu04] Guy, R. K. (2004). *Unsolved Problems in Number Theory*, 3rd ed., Problem B4, Springer,
>   New York. https://doi.org/10.1007/978-0-387-26677-0

*Quoted from [FormalConjectures/Wikipedia/ThabitNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ThabitNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 2 test statements, counted here but not shown.

## `ThabitNumber.thabit_amicable_rule`

Textbook result, stated without proof.

> **Thābit ibn Qurra's amicable number theorem** [Bo72]: for $n \ge 2$, if $K_{n-1}$, $K_n$, and
> $9 \cdot 2^{2n - 1} - 1$ are all prime, then $2^n K_{n-1} K_n$ and $2^n (9 \cdot 2^{2n - 1} - 1)$
> form an amicable pair.
>
> The hypothesis $n \ge 2$ excludes $n = 1$, where $K_0 = 2$ is not coprime to $2^n$.

```lean
theorem thabit_amicable_rule {n : ℕ} (hn : 2 ≤ n) (hp : (thabitNumber (n - 1)).Prime)
    (hq : (thabitNumber n).Prime) (hr : (9 * 2 ^ (2 * n - 1) - 1).Prime) :
    IsAmicable (2 ^ n * thabitNumber (n - 1) * thabitNumber n)
      (2 ^ n * (9 * 2 ^ (2 * n - 1) - 1))
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ThabitNumber.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ThabitNumber.lean#L76).

## `ThabitNumber.infinitely_many_thabit_primes`

Open: stated without proof.

> There are infinitely many exponents $n \in \mathbb{N}$ ([OEIS A002235](https://oeis.org/A002235))
> for which the Thabit number $K_n = 3 \cdot 2^n - 1$ is prime
> ([OEIS A007505](https://oeis.org/A007505)); since `thabitNumber` is injective, this is equivalent to
> the infinitude of Thabit primes themselves.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Thabit_number)

```lean
theorem infinitely_many_thabit_primes : {n : ℕ | (thabitNumber n).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ThabitNumber.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ThabitNumber.lean#L91).

## `ThabitNumber.exists_thabit_amicable_exponent_gt_seven`

Open: stated without proof.

> Does there exist an integer $n > 7$ for which $K_{n-1}$, $K_n$, and $9 \cdot 2^{2n - 1} - 1$ are
> simultaneously prime, yielding an amicable pair via Thābit ibn Qurra's rule [Bo72, Gu04]? Only
> $n = 2, 4, 7$ are currently known.

```lean
theorem exists_thabit_amicable_exponent_gt_seven :
    ∃ n > 7, (thabitNumber (n - 1)).Prime ∧ (thabitNumber n).Prime ∧
      (9 * 2 ^ (2 * n - 1) - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ThabitNumber.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ThabitNumber.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ThabitNumber.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ThabitNumber.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Thabit_number)
