---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PellLucasDiophantineWanted.pellLucasSequence_isSquare_iff, MathlibExt.NumberTheory.PellLucasDiophantineWanted.gcd_pellNumber_pellLucasSequence, MathlibExt.NumberTheory.PellLucasDiophantineWanted.gcd_pellLucasSequence_succ, MathlibExt.NumberTheory.PellLucasDiophantineWanted.pow_add_pow_ne_sq, MathlibExt.NumberTheory.PellLucasDiophantineWanted.pellLucasSequence_pow_add_pow_eq_sq
statement: formalized
---

# Squares among Pell–Lucas numbers

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html).

## Square Pell–Lucas numbers

For every natural number $n$, the Pell–Lucas number $Q_n$ is a
perfect square if and only if $n = 0$ or $n = 1$; thus the only square terms of the sequence are
$Q_0 = Q_1 = 1$.

## Sources

- Sérgio Mendes, "The Diophantine Equation `Q_n^x + Q_{n+1}^x = y^2`", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.PellLucasDiophantineWanted.pellLucasSequence_isSquare_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellLucasDiophantineWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellLucasDiophantineWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html#pell-lucas-sequence-is-square-iff).

## Pell and Pell–Lucas numbers are coprime

For every natural number $n$, the Pell number
$P_n$ and the Pell–Lucas number $Q_n$ satisfy $\gcd(P_n, Q_n) = 1$.

## Sources

- Sérgio Mendes, "The Diophantine Equation `Q_n^x + Q_{n+1}^x = y^2`", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.PellLucasDiophantineWanted.gcd_pellNumber_pellLucasSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellLucasDiophantineWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellLucasDiophantineWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html#gcd-pell-number-pell-lucas-sequence).

## Consecutive Pell–Lucas numbers are coprime

For every natural number $n$, the Pell–Lucas
numbers $Q_n$ and $Q_{n+1}$ satisfy $\gcd(Q_n, Q_{n+1}) = 1$.

## Sources

- Sérgio Mendes, "The Diophantine Equation `Q_n^x + Q_{n+1}^x = y^2`", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.PellLucasDiophantineWanted.gcd_pellLucasSequence_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellLucasDiophantineWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellLucasDiophantineWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html#gcd-pell-lucas-sequence-succ).

## Sums of two coprime positive $n$-th powers are not squares for $n \ge 4$

Let $n \ge 4$
be a natural number and let $x$ and $y$ be coprime positive integers. Then $x^n + y^n$ is not a
perfect square: there is no natural number $z$ with $x^n + y^n = z^2$.

## Sources

- Sérgio Mendes, "The Diophantine Equation `Q_n^x + Q_{n+1}^x = y^2`", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.PellLucasDiophantineWanted.pow_add_pow_ne_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellLucasDiophantineWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellLucasDiophantineWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html#pow-add-pow-ne-sq).

## Sums of powers of consecutive Pell–Lucas numbers that are squares

Let $Q_n$ denote the
Pell–Lucas numbers. For natural numbers $n$, $x$ and $y$, the equation $Q_n^x + Q_{n+1}^x = y^2$
holds if and only if $n = 1$, $x = 1$ and $y = 2$; that is, its only solution in natural numbers
is $Q_1 + Q_2 = 1 + 3 = 2^2$.

## Sources

- Sérgio Mendes, "The Diophantine Equation `Q_n^x + Q_{n+1}^x = y^2`", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.PellLucasDiophantineWanted.pellLucasSequence_pow_add_pow_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellLucasDiophantineWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellLucasDiophantineWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html#pell-lucas-sequence-pow-add-pow-eq-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares among Pell–Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-among-pell-lucas-numbers)
