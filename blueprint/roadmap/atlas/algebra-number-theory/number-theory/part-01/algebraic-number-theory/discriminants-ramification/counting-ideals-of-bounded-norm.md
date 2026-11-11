---
declaration: section
origin: cited
lean: NumberField.Ideal.card_nonzero_absNorm_le, NumberField.Ideal.card_nonzero_absNorm_le_real, NumberField.Ideal.card_nonzero_absNorm_le_real_rpow
statement: formalized
proof: formalized
---

# Counting ideals of bounded norm

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm/index.html).

## Bound on the number of ideals of bounded norm, integer threshold

Let $K$ be a number
field of degree $n = [K : \mathbb{Q}]$ with ring of integers $\mathcal{O}_K$, let $M$ be a natural
number, and let $k$ be the largest natural number with $2^k \le M$, with $k = 0$ if $M = 0$.
Then the number of nonzero ideals $I$ of $\mathcal{O}_K$ whose absolute norm
$N(I) = |\mathcal{O}_K / I|$ satisfies $N(I) \le M$ is at most $(nM)^k$.

## Sources

- ATLAS `NumberTheoryI:295`, *Number Theory I*, Section 14.5, Lemma 14.21; this is a discrete strengthening with an integer threshold, valid also at $M = 0$ and $M = 1$, not the source's literal positive-real statement.

Formalized by `NumberField.Ideal.card_nonzero_absNorm_le`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm/index.html#card-nonzero-abs-norm-le).

## Bound on the number of ideals of bounded norm, floor form

Let $K$ be a number field of
degree $n = [K : \mathbb{Q}]$ with ring of integers $\mathcal{O}_K$, let $M$ be any real number,
and let $m = \max(0, \lfloor M \rfloor)$. Let $k$ be the largest natural number with
$2^k \le m$, and $k = 0$ if $m = 0$. Then the number of nonzero ideals $I$ of $\mathcal{O}_K$
whose absolute norm $N(I) = |\mathcal{O}_K / I|$ satisfies $N(I) \le M$ is at most $(nm)^k$.

For $M < 1$ there are no such ideals, since every nonzero ideal has norm at least $1$; for
$M \ge 1$ the condition $N(I) \le M$ is equivalent to $N(I) \le m$.

Formalized by `NumberField.Ideal.card_nonzero_absNorm_le_real`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm/index.html#card-nonzero-abs-norm-le-real).

## Bound on the number of ideals of bounded norm

Let $K$ be a number field of degree
$n = [K : \mathbb{Q}]$ with ring of integers $\mathcal{O}_K$, and let $M > 0$ be a real number.
The number of nonzero ideals $I$ of $\mathcal{O}_K$ whose absolute norm
$N(I) = |\mathcal{O}_K / I|$ satisfies $N(I) \le M$ is at most $(nM)^{\log_2 M}$, where the
exponent $\log_2 M$ is a real number.

## Sources

- ATLAS `NumberTheoryI:295`, *Number Theory I*, Section 14.5, Lemma 14.21. The proof derives this bound from the integer-threshold and floor variants.

Formalized by `NumberField.Ideal.card_nonzero_absNorm_le_real_rpow`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Ideal/Counting.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm/index.html#card-nonzero-abs-norm-le-real-rpow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting ideals of bounded norm](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/counting-ideals-of-bounded-norm)
