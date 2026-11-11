---
declaration: section
origin: cited
lean: MetaMathlibExt.replaceDigit, MetaMathlibExt.deleteDigit, MetaMathlibExt.insertDigit, MetaMathlibExt.IsDigitallyRobustComposite, MetaMathlibExt.infinitelyMany_digitallyRobustComposites, MetaMathlibExt.cyclotomicPrimeDivisor_order_and_largestPrime, MetaMathlibExt.replaceDigit_25011_units, MetaMathlibExt.deleteDigit_25011_tenThousands
statement: formalized
---

# Digitally robust composite numbers

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html).

## Replacing a base-ten digit

For natural numbers $N$, $i$ and $d$, the result of replacing the
digit of $N$ at position $i$ by $d$ is the natural number

$$\lfloor N / 10^{i+1} \rfloor \cdot 10^{i+1} + d \cdot 10^i + (N \bmod 10^i).$$

Positions are counted from the units digit, which is position $0$, and positions beyond the
written numeral are leading zeros. When $d < 10$, this keeps every digit of $N$ other than the
one at position $i$ and puts $d$ there.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.replaceDigit`, a definition declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#replace-digit).

## Deleting a digit

For natural numbers $N$ and $i$, deleting the base-ten digit of $N$ in
position $i$, where positions are counted from $0$ at the units digit, gives the number

$$\lfloor N / 10^{i+1} \rfloor \cdot 10^{i} + (N \bmod 10^{i}),$$

so the digits above position $i$ move down one place and the digits below position $i$ stay
where they are.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.deleteDigit`, a definition declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#delete-digit).

## Inserting a digit

For natural numbers $N$, $i$ and $d$, inserting $d$ into the base-ten
expansion of $N$ in position $i$, where positions are counted from $0$ at the units digit, gives
the number

$$\lfloor N / 10^{i} \rfloor \cdot 10^{i+1} + d \cdot 10^{i} + (N \bmod 10^{i}),$$

so the digits in positions $i$ and above move up one place, $d$ takes position $i$, and the
digits below position $i$ stay where they are. For $i = 0$ this appends $d$ on the right, and
for $i$ at least the number of digits of $N$ it inserts $d$ among the leading zeros.

When $i$ equals the number of digits of $N$, inserting $d$ gives the same number as replacing
the first leading zero by $d$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.insertDigit`, a definition declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#insert-digit).

## Digitally robust composite numbers

A natural number $N$ is a digitally robust composite if
it is composite (greater than $1$ and not prime), coprime to $10$, and each of the following
numbers is greater than $1$ and not prime: the result of replacing the base-ten digit of $N$ in
any position $i$ by any digit $d < 10$ other than $\lfloor N / 10^{i} \rfloor \bmod 10$; the
result of deleting the single digit in any position $i$ smaller than the number of base-ten
digits of $N$; and the result of inserting any digit $d < 10$ in any position $i$. Positions are
counted from $0$ at the units digit, and positions beyond the written digits of $N$ refer to its
leading zeros.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.IsDigitallyRobustComposite`, a definition declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#is-digitally-robust-composite).

## Infinitely many digitally robust composites

There are infinitely many natural numbers that
are digitally robust composites: composite numbers coprime to $10$ that stay composite after
replacing any one base-ten digit (including a leading zero) by a different digit, after deleting
any one of their digits, and after inserting any digit in any position.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Stated but not proved: `MetaMathlibExt.infinitelyMany_digitallyRobustComposites` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#infinitely-many-digitally-robust-composi).

## Prime divisors of cyclotomic values at 10

Let $b$ be a positive integer, let $\Phi_b$ be
the $b$-th cyclotomic polynomial with integer coefficients, and let $p$ be a prime that divides
the integer $\Phi_b(10)$. If $b < p$, then the multiplicative order of $10$ modulo $p$ is $b$.
If $p \le b$ and $b > 2$, then $p$ divides $b$, every prime divisor $q$ of $b$ satisfies
$q \le p$ (so $p$ is the largest prime divisor of $b$), and $p^2$ does not divide $\Phi_b(10)$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Lemma 1.

Stated but not proved: `MetaMathlibExt.cyclotomicPrimeDivisor_order_and_largestPrime` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#cyclotomic-prime-divisor-order-and-large).

## Replacing the units digit of 25011 by 3

Replacing the base-ten digit of $25011$ at
position $0$, its units digit, by $3$ gives $25013$.

This is a sample computation illustrating the replacement operation of Theorem 1, not a claim
from the theorem.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.replaceDigit_25011_units`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#replace-digit-25011-units).

## Deleting the ten-thousands digit of 25011

Deleting the base-ten digit in position $4$ of
$25011$, where positions are counted from $0$ at the units digit (so position $4$ is the
ten-thousands digit $2$), gives $5011$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.deleteDigit_25011_tenThousands`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#delete-digit-25011-ten-thousands).

## Inserting a digit among the leading zeros of 25011

Inserting the digit $1$ in position $7$
of $25011$, where positions are counted from $0$ at the units digit (so the new digit goes
between the second and third leading zeros), gives $10025011$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.insertDigit_25011_leadingZeros`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#insert-digit-25011-leading-zeros).

## Replacing a leading zero of 25011 by zero

Replacing the base-ten digit in position $6$ of
$25011$, where positions are counted from $0$ at the units digit (so this digit is a leading
zero), by $0$ gives $25011$ again.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.replaceDigit_25011_leadingZero`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#replace-digit-25011-leading-zero).

## Base-ten digits are less than ten

For all natural numbers $N$ and $i$, the base-ten digit
of $N$ in position $i$ (counted from $0$ at the units digit), namely
$\lfloor N / 10^{i} \rfloor \bmod 10$, is less than $10$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.digitValue_lt_ten`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#digit-value-lt-ten).

## 25011 is not a digitally robust composite

The number $25011$ is not a digitally robust
composite: replacing its units digit $1$ by $3$ gives the prime $25013$.

## Sources

- Ian Fultz, Jacob Juillerat, and Aidan Kuster, *Composite Numbers That Remain Composite When Inserting, Replacing, or Deleting a Digit*, INTEGERS 26 (2026), Article A119, Theorem 1.

Formalized by `MetaMathlibExt.not_isDigitallyRobustComposite_25011`, a theorem declared in [WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DigitallyRobustCompositesWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html#not-is-digitally-robust-composite-25011).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Digitally robust composite numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/digitally-robust-composite-numbers)
