---
declaration: section
origin: cited
lean: MetaMathlibExt.euler_characterization_of_even_perfect_numbers, MetaMathlibExt.IsExtremelyAbundantNumber, MetaMathlibExt.IsGiugaNumber, MetaMathlibExt.IsPracticalNumber, MetaMathlibExt.thabit_ibn_qurra
statement: formalized
proof: formalized
---

# Perfect numbers and their relatives: its own results

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html).

Perfect, multiperfect, odd perfect, abundant, practical, Zumkeller, Giuga, amicable numbers, spoof factorizations, Lehmer's totient problem.

## Euler's theorem on even perfect numbers

Every even perfect number $N$ is of the form
$N = 2^{p-1}(2^p - 1)$ for some natural number $p$ such that $p$ and $2^p - 1$ are both prime.

## Sources

- Paulo J. Almeida and Gabriel Cardoso, "An Extension of the Euclid-Euler Theorem to Certain α-Perfect Numbers," Journal of Integer Sequences 25 (2022), Article 22.8.4, Theorem [Euler] (unlabeled), lines 164–166, https://cs.uwaterloo.ca/journals/JIS/VOL25/Almeida/almeida9.tex

Formalized by `MetaMathlibExt.euler_characterization_of_even_perfect_numbers`, a theorem declared in [MathlibExt/NumberTheory/EvenPerfectNumbers.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPerfectNumbers.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html#euler-characterization-of-even-perfect-n).

## Extremely abundant number

Let $\sigma(n)$ denote the sum of the positive divisors of $n$.
A natural number $n$ is extremely abundant if either $n = 10080$, or $n > 10080$ and
$\sigma(n) / (n \log \log n) > \sigma(m) / (m \log \log m)$ for every natural number $m$ with
$10080 \le m < n$, where $\log$ is the natural logarithm.

Formalized by `MetaMathlibExt.IsExtremelyAbundantNumber`, a definition declared in [MathlibExt/NumberTheory/ExtremelyAbundantNumber.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ExtremelyAbundantNumber.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html#is-extremely-abundant-number).

## Giuga number

A natural number $n$ is a Giuga number if it is composite (that is,
$n \ge 2$ and $n$ is not prime) and $p$ divides $n/p - 1$ for every prime divisor $p$ of $n$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL15/Oller/oller5.tex> and <https://cs.uwaterloo.ca/journals/JIS/VOL17/Mestrovic/mes4.tex>.

Formalized by `MetaMathlibExt.IsGiugaNumber`, a definition declared in [MathlibExt/NumberTheory/GiugaNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GiugaNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html#is-giuga-number).

## Practical number

A natural number $n$ is practical if $n > 0$ and every integer $m$ with
$1 \le m \le n$ is the sum of a set of distinct positive divisors of $n$.

Formalized by `MetaMathlibExt.IsPracticalNumber`, a definition declared in [MathlibExt/NumberTheory/PracticalNumber.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PracticalNumber.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html#is-practical-number).

## Thābit ibn Qurra's theorem

Let $n \ge 2$ be a natural number and put $p = 3 \cdot 2^n - 1$,
$q = 3 \cdot 2^{n-1} - 1$ and $r = 9 \cdot 2^{2n-1} - 1$. If $p$, $q$ and $r$ are all prime, then
$2^n p q < 2^n r$, the sum of the proper divisors of $2^n p q$ equals $2^n r$, and the sum of the
proper divisors of $2^n r$ equals $2^n p q$; that is, $2^n p q$ and $2^n r$ are distinct amicable
numbers.

Proof: Following Thabit ibn Qurra's construction as recorded in Dickson, *History of the Theory
of Numbers*, Vol. I, Ch. I, p. 39, and the cited Wikipedia account, compute full divisor sums by
multiplicativity and recover the proper-divisor sums by subtracting each number.

## Sources

- https://en.wikipedia.org/wiki/Amicable_numbers#Th%C4%81bit_ibn_Qurra_theorem

Formalized by `MetaMathlibExt.thabit_ibn_qurra`, a theorem declared in [MathlibExt/NumberTheory/ThabitIbnQurra.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ThabitIbnQurra.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html#thabit-ibn-qurra).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect numbers and their relatives](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers)
