---
declaration: section
origin: cited
lean: MetaMathlibExt.midy_theorem_general, MetaMathlibExt.midy_theorem
statement: formalized
proof: formalized
---

# Midy's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/midy-s-theorem/index.html).

## Midy's theorem, general form

Let $p$ be a prime and $n$ a natural number such that $p$
divides $10^{2n} - 1$ but does not divide $10^n - 1$. Let $Q = (10^{2n} - 1)/p$ and write
$Q = 10^n H + L$ with $0 \le L < 10^n$, so that $L$ is the number formed by the last $n$ decimal
digits of $Q$ and $H$ the number formed by the remaining digits. Then $H + L = 10^n - 1$.

Midy's theorem in its usual form, where the decimal period of $1/p$ is exactly $2n$, is the
special case in which $p$ does not divide $10^m - 1$ for any $0 < m < 2n$.

Formalized by `MetaMathlibExt.midy_theorem_general`, a theorem declared in [MathlibExt/NumberTheory/Digits/Midy.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Digits/Midy.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/midy-s-theorem/index.html#midy-theorem-general).

## Midy's theorem

Let $p \ne 2, 5$ be a prime and $n \ge 1$ an integer such that $p$ divides
$10^{2n} - 1$ and does not divide $10^m - 1$ for any $0 < m < 2n$, that is, the decimal period of
$1/p$ is $2n$. Let $Q = (10^{2n} - 1)/p$, whose decimal expansion padded with leading zeros to
$2n$ digits is the repetend of $1/p$, and write $Q = 10^n H + L$ with $0 \le L < 10^n$, so that
$H$ and $L$ are the two $n$-digit halves of the repetend. Then $H + L = 10^n - 1$.

The proof uses neither $p \ne 2, 5$ nor the minimality of the period beyond $p \nmid 10^n - 1$;
see Midy's theorem, general form.

## Sources

- https://en.wikipedia.org/wiki/Midy%27s_theorem.

Formalized by `MetaMathlibExt.midy_theorem`, a theorem declared in [MathlibExt/NumberTheory/Digits/Midy.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Digits/Midy.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/midy-s-theorem/index.html#midy-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Midy's theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/midy-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/midy-s-theorem)
