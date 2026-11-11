---
declaration: section
origin: cited
lean: MetaMathlibExt.brousseauA, MetaMathlibExt.brousseauA_zero, MetaMathlibExt.brousseauA_one, MetaMathlibExt.brousseauA_two, MetaMathlibExt.brousseauCoeff, MetaMathlibExt.brousseauCoeff_zero, MetaMathlibExt.brousseauCoeff_one, MetaMathlibExt.kFibonacci_eq_pow_add_convolution
statement: formalized
---

# Brousseau sums of k-Fibonacci numbers

13 results, 7 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html).

## The numbers $A_k^{(p)}$ for $k$-Fibonacci Brousseau sums

For a rational number $k$, the
rational numbers $A_k^{(p)}$, $p \ge 0$, are defined by $A_k^{(0)} = 1$ and, for $p \ge 1$,

$$
A_k^{(p)} = \frac{2}{k} \sum_{j=1}^{\lceil p/2 \rceil} \binom{p}{2j-1} A_k^{(p-2j+1)},
$$

where $2/k$ is read as $0$ when $k = 0$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 1.

Formalized by `MetaMathlibExt.brousseauA`, a definition declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-a).

## The initial value $A_k^{(0)} = 1$

For every rational number $k$, the number $A_k^{(0)}$
for $k$-Fibonacci Brousseau sums equals $1$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 1.

Formalized by `MetaMathlibExt.brousseauA_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-a-zero).

## The value $A_k^{(1)} = 2/k$

For every rational number $k$, the number $A_k^{(1)}$ for
$k$-Fibonacci Brousseau sums equals $2/k$, where $2/0$ is read as $0$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 1.

Formalized by `MetaMathlibExt.brousseauA_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-a-one).

## The value $A_k^{(2)} = 8/k^2$

For every rational number $k$, the number $A_k^{(2)}$ for
$k$-Fibonacci Brousseau sums equals $8/k^2$, where $8/0$ is read as $0$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 1.

Formalized by `MetaMathlibExt.brousseauA_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-a-two).

## The coefficient polynomials $C_k^{(p)}$ for $k$-Fibonacci Brousseau sums

For a rational
number $k$, let $A_k^{(r)}$ be the numbers for $k$-Fibonacci Brousseau sums. For a natural number
$p$ and a rational number $n$,

$$
C_k^{(p)}(n) = \sum_{r=0}^{p} (-1)^r A_k^{(r)} \binom{p}{r} n^{p-r},
$$

where $0^0 = 1$; in particular $C_k^{(p)}(0) = (-1)^p A_k^{(p)}$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 5.

Formalized by `MetaMathlibExt.brousseauCoeff`, a definition declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-coeff).

## The polynomial $C_k^{(0)}$ is constant $1$

For all rational numbers $k$ and $n$, the
coefficient polynomial $C_k^{(0)}$ for $k$-Fibonacci Brousseau sums satisfies $C_k^{(0)}(n) = 1$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 5.

Formalized by `MetaMathlibExt.brousseauCoeff_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-coeff-zero).

## The polynomial $C_k^{(1)}(n) = n - 2/k$

For all rational numbers $k$ and $n$, the
coefficient polynomial $C_k^{(1)}$ for $k$-Fibonacci Brousseau sums satisfies
$C_k^{(1)}(n) = n - 2/k$, where $2/0$ is read as $0$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Definition 5.

Formalized by `MetaMathlibExt.brousseauCoeff_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#brousseau-coeff-one).

## $k$-Fibonacci numbers as a power-weighted convolution

For an integer $k$, let $F_{k,n}$
be the $k$-Fibonacci numbers, the Lucas sequence $U(k, -1)$: $F_{k,0} = 0$, $F_{k,1} = 1$ and
$F_{k,n+2} = k F_{k,n+1} + F_{k,n}$. For every integer $k$, every $n \ge 0$ and every $p \ge 1$,

$$
F_{k,n} = n^p + \sum_{i=1}^{n} \Bigl(k i^p -
2 \sum_{j=1}^{\lceil p/2 \rceil} \binom{p}{2j-1} i^{p-2j+1}\Bigr) F_{k,n-i}.
$$

The paper assumes $k \ge 1$ and $n \ge 1$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Theorem 1 (`jis-2024-24.6.4-thm-1`).

Stated but not proved: `MetaMathlibExt.kFibonacci_eq_pow_add_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#k-fibonacci-eq-pow-add-convolution).

## Power-weighted convolution of k-Fibonacci numbers

Let $k$ be a nonzero integer and let
$F_{k,n}$ be the $k$-Fibonacci numbers, the Lucas sequence $U(k, -1)$: $F_{k,0} = 0$,
$F_{k,1} = 1$ and $F_{k,n+2} = k F_{k,n+1} + F_{k,n}$. Let $A_k^{(0)} = 1$ and
$A_k^{(p)} = \frac{2}{k} \sum_{j=1}^{\lceil p/2 \rceil} \binom{p}{2j-1} A_k^{(p-2j+1)}$ for
$p \ge 1$. Then for all natural numbers $n$ and $p$, with $0^0 = 1$,

$$
k \sum_{i=0}^{n} i^p F_{k,n-i} = A_k^{(p)} F_{k,n+1} +
\sum_{r=0}^{p} A_k^{(r)} \binom{p}{r} \left((-1)^{p-r} F_{k,n} - n^{p-r}\right).
$$

The source takes $k$ to be a positive integer.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Theorem 4 (`jis-2024-24.6.4-thm-4`).

Stated but not proved: `MetaMathlibExt.kFibonacci_power_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#k-fibonacci-power-convolution).

## Brousseau sums of $k$-Fibonacci numbers

For an integer $k$, let $F_{k,n}$ be the
$k$-Fibonacci numbers, the Lucas sequence $U(k, -1)$ ($F_{k,0} = 0$, $F_{k,1} = 1$,
$F_{k,n+2} = k F_{k,n+1} + F_{k,n}$), and let $C_k^{(p)}$ be the coefficient polynomials. For
every nonzero integer $k$ and all $n, p \ge 0$,

$$
k \sum_{i=0}^{n} i^p F_{k,i} = C_k^{(p)}(n) F_{k,n+1} + C_k^{(p)}(n+1) F_{k,n} - C_k^{(p)}(0),
$$

where $0^0 = 1$.

The paper assumes $k \ge 1$.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Theorem 6 (`jis-2024-24.6.4-thm-6`).

Stated but not proved: `MetaMathlibExt.kFibonacci_brousseau_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#k-fibonacci-brousseau-sum).

## Brousseau sums of Fibonacci numbers along an odd step

Let $F_n$ be the Fibonacci
numbers, $L_n$ the Lucas numbers and $C_k^{(p)}$ the coefficient polynomials. For every odd
natural number $m$ and all $n, p \ge 0$,

$$
L_m \sum_{i=1}^{n} i^p F_{mi} = C_{L_m}^{(p)}(n) F_{m(n+1)} + C_{L_m}^{(p)}(n+1) F_{mn} -
C_{L_m}^{(p)}(0) F_m.
$$

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Corollary 9 (`jis-2024-24.6.4-cor-9`).

Stated but not proved: `MetaMathlibExt.fibonacci_brousseau_sum_mul_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#fibonacci-brousseau-sum-mul-odd).

## Power-weighted Pell sums along odd multiples

Let $P_n$ be the Pell numbers and $Q_n$ the
Pell–Lucas numbers, the Lucas sequence $V(2, -1)$: $Q_0 = Q_1 = 2$ and
$Q_{n+2} = 2 Q_{n+1} + Q_n$. Let $m$ be an odd natural number and write $k = Q_m$. Let
$A_k^{(0)} = 1$ and
$A_k^{(p)} = \frac{2}{k} \sum_{j=1}^{\lceil p/2 \rceil} \binom{p}{2j-1} A_k^{(p-2j+1)}$ for
$p \ge 1$, and let $C_k^{(p)}(x) = \sum_{r=0}^{p} (-1)^r A_k^{(r)} \binom{p}{r} x^{p-r}$, with
$0^0 = 1$. Then for all natural numbers $n$ and $p$,

$$
Q_m \sum_{i=1}^{n} i^p P_{mi} = C_k^{(p)}(n) P_{m(n+1)} + C_k^{(p)}(n+1) P_{mn} -
C_k^{(p)}(0) P_m.
$$

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Corollary 10 (`jis-2024-24.6.4-cor-10`).

Stated but not proved: `MetaMathlibExt.pell_brousseau_sum_mul_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#pell-brousseau-sum-mul-odd).

## Shifted power-weighted sums of k-Fibonacci numbers

Let $k$ be a nonzero integer and let
$F_{k,n}$ be the $k$-Fibonacci numbers, the Lucas sequence $U(k, -1)$: $F_{k,0} = 0$,
$F_{k,1} = 1$ and $F_{k,n+2} = k F_{k,n+1} + F_{k,n}$. Let $A_k^{(0)} = 1$ and
$A_k^{(p)} = \frac{2}{k} \sum_{j=1}^{\lceil p/2 \rceil} \binom{p}{2j-1} A_k^{(p-2j+1)}$ for
$p \ge 1$, and let $C_k^{(p)}(x) = \sum_{r=0}^{p} (-1)^r A_k^{(r)} \binom{p}{r} x^{p-r}$, with
$0^0 = 1$. Then for all natural numbers $m$, $n$ and $p$,

$$
k \sum_{i=1}^{n} i^p F_{k,m+i} = C_k^{(p)}(n) F_{k,m+n+1} + C_k^{(p)}(n+1) F_{k,m+n} -
C_k^{(p)}(0) F_{k,m+1} - C_k^{(p)}(1) F_{k,m}.
$$

The source takes $k$ to be a positive integer.

## Sources

- Prabha Sivaraman Nair and Rejikumar Karunakaran, *On k-Fibonacci Brousseau Sums*, Journal of Integer Sequences 27 (2024), Article 24.6.4, Theorem 11 (`jis-2024-24.6.4-thm-11`).

Stated but not proved: `MetaMathlibExt.kFibonacci_shifted_brousseau_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KFibonacciBrousseauSumsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html#k-fibonacci-shifted-brousseau-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brousseau sums of k-Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/brousseau-sums-of-k-fibonacci-numbers)
