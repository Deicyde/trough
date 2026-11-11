---
declaration: section
origin: cited
lean: MetaMathlibExt.staver_sign_mul, MetaMathlibExt.staver_sign_sq, MetaMathlibExt.staver_sign_odd, MetaMathlibExt.staver_sign_even, MetaMathlibExt.staver_reflect_zero, MetaMathlibExt.staver_reflect_one, MetaMathlibExt.staver_identity, MetaMathlibExt.staver_reciprocal_binomial_sum
statement: formalized
proof: formalized
---

# Staver's identity

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html).

## Splitting a power of minus one

For natural numbers $k \le n$, we have
$(-1)^{n-k} \cdot (-1)^k = (-1)^n$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_sign_mul`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-sign-mul).

## Squares of powers of minus one

For every natural number $k$, we have
$(-1)^k \cdot (-1)^k = 1$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_sign_sq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-sign-sq).

## Reflecting a power of minus one, odd case

If $n$ is an odd natural number and
$k \le n$ is a natural number, then $(-1)^{n-k} = -(-1)^k$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_sign_odd`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-sign-odd).

## Reflecting a power of minus one, even case

If $n$ is an even natural number and
$k \le n$ is a natural number, then $(-1)^{n-k} = (-1)^k$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_sign_even`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-sign-even).

## Reflection of the alternating reciprocal binomial sum

For every natural number $n$,
$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k}^{-1} = \sum_{k=0}^{n} (-1)^{k} \binom{n}{k}^{-1}$
in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_reflect_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-reflect-zero).

## Reflection of the weighted alternating reciprocal binomial sum

For every natural
number $n$,
$\sum_{k=0}^{n} (-1)^{n-k} \, k \binom{n}{k}^{-1} =
\sum_{k=0}^{n} (-1)^{k} (n-k) \binom{n}{k}^{-1}$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.staver_reflect_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-reflect-one).

## Staver's identity for alternating reciprocal binomial sums

For a natural number $n$,
let $S_0(n) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k}^{-1}$ and
$S_1(n) = \sum_{k=0}^{n} (-1)^{n-k} \, k \binom{n}{k}^{-1}$, computed in $\mathbb{Q}$.
If $n$ is even, then $S_1(n) = \frac{n}{2} S_0(n)$; if $n$ is odd, then $S_0(n) = 0$.

## Sources

- Renzo Sprugnoli, "Alternating Weighted Sums of Inverses of Binomial Coefficients," Journal of Integer Sequences 15 (2012), Article 12.6.3 (Staver's identity), <https://cs.uwaterloo.ca/journals/JIS/VOL15/Sprugnoli/sprugnoli6.tex>. Both parts follow by pairing `k ↔ n - k`: for odd `n` the pairs cancel, for even `n` they average to `n/2`.

Formalized by `MetaMathlibExt.staver_identity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StaverIdentity.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-identity).

## Staver's identity for reciprocal binomial sums

For every natural number $n$, the
following identity between rational numbers holds:

$$\sum_{k=0}^{n} \binom{n}{k}^{-1} = \frac{n+1}{2^{n+1}} \sum_{k=1}^{n+1} \frac{2^k}{k}.$$

Both sides satisfy the recurrence $F(n+1) = 1 + \frac{n+2}{2(n+1)} F(n)$ and both equal $1$ at
$n = 0$, so the identity follows by induction on $n$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Sprugnoli/sprugnoli4.tex>. Definition lines 115-125. Formula lines 231-236. The left side expands `S_n^(0)`, the sum of reciprocal binomial coefficients. All arithmetic is rational (`Rat` division and inverses); the statement holds for all `n : Nat`, so the edge case `n = 0` is included.

Formalized by `MetaMathlibExt.staver_reciprocal_binomial_sum`, a theorem declared in [MathlibExt/Combinatorics/StaverReciprocalBinomialSum.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/StaverReciprocalBinomialSum.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html#staver-reciprocal-binomial-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Staver's identity](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/staver-s-identity)
