---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.self_le_four_pow_div_one_twenty_eight_add_one, Nat.SylvesterSchur.Internal.two_pow_nineteen_mul_div_twelve_le_three_pow, Nat.SylvesterSchur.Internal.four_pow_mul_two_pow_mul_four_pow_lt_three_pow_mul_four_pow
statement: formalized
proof: formalized
---

# Power bounds for large residual Sylvester-Schur estimates

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur/index.html).

## A linear bound by a power of four

For every natural number $n \ge 512$,
$n \le 4^{\lfloor n/128 \rfloor + 1}$.

Formalized by `Nat.SylvesterSchur.Internal.self_le_four_pow_div_one_twenty_eight_add_one`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur/index.html#self-le-four-pow-div-one-twenty-eight-ad).

## Powers of two against powers of three

For every natural number $n$,
$2^{19 \lfloor n/12 \rfloor} \le 3^{n}$.

Formalized by `Nat.SylvesterSchur.Internal.two_pow_nineteen_mul_div_twelve_le_three_pow`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur/index.html#two-pow-nineteen-mul-div-twelve-le-three).

## A power comparison for the central-offset estimate

Let $D$, $E$, $i$, $n$ be natural
numbers with $2D + i + 2E < 19 \lfloor i/12 \rfloor + 2n$. Then
$4^{D} \cdot 2^{i} \cdot 4^{E} < 3^{i} \cdot 4^{n}$.

Formalized by `Nat.SylvesterSchur.Internal.four_pow_mul_two_pow_mul_four_pow_lt_three_pow_mul_four_pow`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/PowerBounds.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur/index.html#four-pow-mul-two-pow-mul-four-pow-lt-thr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power bounds for large residual Sylvester-Schur estimates](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/power-bounds-for-large-residual-sylvester-schur)
