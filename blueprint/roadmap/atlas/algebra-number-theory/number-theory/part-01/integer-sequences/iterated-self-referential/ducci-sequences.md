---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DucciWanted.ducciCoeff, MathlibExt.NumberTheory.DucciWanted.choose_prime_pow_sub_one_mod, MathlibExt.NumberTheory.DucciWanted.choose_prime_pow_sub_mod, MathlibExt.NumberTheory.DucciWanted.ducciCoeff_vanish_mod, MathlibExt.NumberTheory.DucciWanted.ducciCoeff_reduce_mod, MathlibExt.NumberTheory.DucciWanted.ducci_pred_iff
statement: formalized
---

# Ducci sequences

6 results, 1 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html).

## Ducci coefficients

For natural numbers $n$, $r$ and $s$, the Ducci coefficient is
$a_{r,s} = \sum_{0 \le j \le r,\ j \equiv s - 1 \ (\mathrm{mod}\ n)} \binom{r}{j}$, where $s - 1$
is read as $0$ when $s = 0$ and congruence modulo $0$ is equality.

For $1 \le s \le n$, $a_{r,s}$ is the coefficient of $x_s$ in the first entry of $D^r(x)$, where
the Ducci map $D$ on $\mathbb{Z}_m^n$ sends $(x_1, \dots, x_n)$ to
$(x_1 + x_2, x_2 + x_3, \dots, x_n + x_1)$.

Formalized by `MathlibExt.NumberTheory.DucciWanted.ducciCoeff`, a definition declared in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#ducci-coeff).

## Binomial coefficients $\binom{p^k - 1}{j}$ modulo $p$

Let $p$ be a prime, let $k \ge 1$,
and let $j$ be an integer with $0 \le j \le p^k - 1$. Then
$\binom{p^k - 1}{j} \equiv (-1)^j \pmod{p}$.

## Sources

- Mark L. Lewis and Shannon M. Tefft, "The Maximum Length for Ducci Sequences on `ℤ_m^n` when `n` is Even", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.DucciWanted.choose_prime_pow_sub_one_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#choose-prime-pow-sub-one-mod).

## Binomial coefficients $\binom{p^k - p^{k-1}}{j}$ modulo $p$

Let $p$ be an odd prime,
let $k \ge 2$, and let $j$ be an integer with $0 \le j \le p^k - p^{k-1}$. If $j = c\,p^{k-1}$
for an integer $c$, then $\binom{p^k - p^{k-1}}{j} \equiv (-1)^c \pmod{p}$; otherwise
$\binom{p^k - p^{k-1}}{j} \equiv 0 \pmod{p}$.

## Sources

- Mark L. Lewis and Shannon M. Tefft, "The Maximum Length for Ducci Sequences on `ℤ_m^n` when `n` is Even", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.DucciWanted.choose_prime_pow_sub_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#choose-prime-pow-sub-mod).

## Vanishing of Ducci coefficients modulo $p$

For integers $N \ge 1$, $r \ge 0$ and $s \ge 1$
write $a^{(N)}_{r,s} = \sum_{0 \le j \le r,\ j \equiv s - 1 \ (\mathrm{mod}\ N)} \binom{r}{j}$ for
the Ducci coefficients of length $N$. Let $p$ be a prime, let $k \ge 0$ and $n_1 \ge 2$ be
integers, and let $n = p^k n_1$. Let $c \ge 1$, and let $s$ be an integer with $1 \le s \le n$
that is not of the form $b\,p^k + 1$ with $0 \le b < n_1$. Then
$a^{(n)}_{c p^k, s} \equiv 0 \pmod{p}$.

## Sources

- Mark L. Lewis and Shannon M. Tefft, "The Maximum Length for Ducci Sequences on `ℤ_m^n` when `n` is Even", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.DucciWanted.ducciCoeff_vanish_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#ducci-coeff-vanish-mod).

## Reduction of Ducci coefficients modulo $p$

For integers $N \ge 1$, $r \ge 0$ and $s \ge 1$
write $a^{(N)}_{r,s} = \sum_{0 \le j \le r,\ j \equiv s - 1 \ (\mathrm{mod}\ N)} \binom{r}{j}$ for
the Ducci coefficients of length $N$. Let $p$ be a prime, let $k \ge 0$ and $n_1 \ge 2$ be
integers, and let $n = p^k n_1$. Then for every integer $c \ge 1$ and every integer $b$ with
$0 \le b < n_1$,
$a^{(n)}_{c p^k,\, b p^k + 1} \equiv a^{(n_1)}_{c,\, b + 1} \pmod{p}$.

## Sources

- Mark L. Lewis and Shannon M. Tefft, "The Maximum Length for Ducci Sequences on `ℤ_m^n` when `n` is Even", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.DucciWanted.ducciCoeff_reduce_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#ducci-coeff-reduce-mod).

## Ducci predecessor criterion for even length

Let $m \ge 0$ be an integer, let $n \ge 2$ be
even, and write $\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$ (so $\mathbb{Z}_0 = \mathbb{Z}$). A tuple
$x = (x_1, \dots, x_n) \in \mathbb{Z}_m^n$ has a Ducci predecessor, that is, a tuple
$y \in \mathbb{Z}_m^n$ with $y_i + y_{i+1} = x_i$ for all $i$ (indices taken cyclically, so
$y_{n+1} = y_1$), if and only if $x_1 - x_2 + x_3 - \cdots + x_{n-1} - x_n = 0$ in $\mathbb{Z}_m$.

## Sources

- Mark L. Lewis and Shannon M. Tefft, "The Maximum Length for Ducci Sequences on `ℤ_m^n` when `n` is Even", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.DucciWanted.ducci_pred_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/DucciSequenceWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DucciSequenceWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html#ducci-pred-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ducci sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/ducci-sequences)
