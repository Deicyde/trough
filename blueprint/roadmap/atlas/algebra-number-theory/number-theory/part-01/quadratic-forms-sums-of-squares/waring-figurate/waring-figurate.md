---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.HilbertWaringWanted.hilbert_waring, MetaMathlibExt.four_triangular_numbers_eq_divisor_sum, MetaMathlibExt.hurwitz_quaternion_waring_bound
statement: formalized
proof: formalized
---

# Waring's problem and figurate numbers: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/index.html).

Hilbert–Waring, g(3)=9, Fermat polygonal theorem, polygonal, triangular and polytopic numbers and their sums.

## Hilbert–Waring theorem

For every integer $k \ge 1$ there is a natural number $g$ such that
every natural number $n$ is a sum of $g$ $k$-th powers of natural numbers, that is,
$n = x_1^k + \dots + x_g^k$ for some $x_1, \dots, x_g \in \mathbb{N}$.

Proof: We follow Linnik's elementary route as presented in Tim Jameson's notes: a mean-value
estimate gives positive Schnirelmann density for a bounded power sumset, which is then an additive
basis of finite order by Schnirelmann's inequality.

## Sources

- D. Hilbert, Beweis für die Darstellbarkeit der ganzen Zahlen durch eine feste Anzahl n-ter Potenzen (Waringsches Problem), Math. Ann. 67 (1909) 281–305; textbook in Vaughan, The Hardy-Littlewood Method; general includes minimal g(k).

Formalized by `MathlibExt.NumberTheory.HilbertWaringWanted.hilbert_waring`, a theorem declared in [MathlibExt/NumberTheory/HilbertWaring.lean, line 3445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HilbertWaring.lean#L3445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/index.html#hilbert-waring).

## Legendre's four-triangular-numbers theorem

For $k \ge 0$ let $T_k = k(k+1)/2$ be the
$k$-th triangular number. For every natural number $j$, the number of ordered quadruples
$(k_1, k_2, k_3, k_4)$ of integers with $0 \le k_i \le j$ and
$T_{k_1} + T_{k_2} + T_{k_3} + T_{k_4} = j$ equals $\sigma(2j+1)$, the sum of the positive
divisors of $2j+1$.

The bound $k_i \le j$ is automatic, since $T_k \ge k$. Representations using $T_0 = 0$ are
counted, and quadruples that differ only in the order of their entries are counted separately.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, "Glaisher's Divisors and Infinite Products," Journal of Integer Sequences 27 (2024), Article 24.1.6, Proposition [Legendre] (equation nttriangle-b), lines 738–740, https://cs.uwaterloo.ca/journals/JIS/VOL27/Bhatnagar/bhat4.tex

Formalized by `MetaMathlibExt.four_triangular_numbers_eq_divisor_sum`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/FourTriangularNumbers.lean, line 2781](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/FourTriangularNumbers.lean#L2781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/index.html#four-triangular-numbers-eq-divisor-sum).

## Waring's problem for Hurwitz quaternion integers

Call a rational quaternion a Hurwitz
integer if its four coordinates are either all integers or all of the form $a + \tfrac12$ with
$a$ an integer. For every positive integer $\ell$ with $\ell \equiv 1$ or $\ell \equiv 2 \pmod 3$
there is a natural number $g$ such that every Hurwitz integer is a sum of at most $g$ $\ell$-th
powers of Hurwitz integers.

## Sources

- Janyarak Tongsomporn, Nicola Oswald, and Jörn Steuding, "Waring's Problem for Hurwitz Quaternion Integers," Journal of Integer Sequences 22 (2019), Article 19.8.1, Theorem, lines 127–129, https://cs.uwaterloo.ca/journals/JIS/VOL22/Steuding/steuding6.tex

Formalized by `MetaMathlibExt.hurwitz_quaternion_waring_bound`, a theorem declared in [MathlibExt/NumberTheory/HurwitzQuaternionWaring.lean, line 1362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HurwitzQuaternionWaring.lean#L1362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/index.html#hurwitz-quaternion-waring-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Waring's problem and figurate numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate)
