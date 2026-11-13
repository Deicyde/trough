---
declaration: section
origin: cited
lean: MetaMathlibExt.alfred_consecutive_fibonacci_powers_determinant, MetaMathlibExt.brousseau_fibonacci_reciprocal_sum
statement: formalized
proof: formalized
---

# Fibonacci and Lucas numbers: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/index.html).

Identities, sums, reciprocal series, determinants and generating functions specifically for Fibonacci and Lucas numbers.

## Alfred's determinant of consecutive Fibonacci powers

Let $F_n$ denote the Fibonacci numbers
extended to all integers $n$ by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$, so that
$F_{-n} = (-1)^{n+1} F_n$. For every natural number $r$ and all integers $s$ and $k$, the
$(r+1) \times (r+1)$ integer matrix whose entry in row $i$ and column $j$, for
$0 \le i, j \le r$, is $F_{s+ik}^{\,r-j} \, F_{s+(i+1)k}^{\,j}$ has determinant
$(-1)^{|e|} \, F_k^{\binom{r+1}{2}} \prod_{\ell=1}^{r} F_{k\ell}^{\,r+1-\ell}$, where
$e = (s+1)\binom{r+1}{2} + k\binom{r+1}{3}$.

This is a slight variation of a result of Brother U. Alfred, "Some determinants involving
powers of Fibonacci numbers," Fibonacci Quarterly 2 (1964), 81–92.

## Sources

- Aram Tangboonduangjit and Thotsaporn Thanatipanonda, "Determinants Containing Powers of Generalized Fibonacci Numbers," Journal of Integer Sequences 19 (2016), Article 16.7.1, Corollary, lines 406–418, https://cs.uwaterloo.ca/journals/JIS/VOL19/Tangboonduangjit/aram5.tex

Formalized by `MetaMathlibExt.alfred_consecutive_fibonacci_powers_determinant`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/AlfredFibonacciDeterminant.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/AlfredFibonacciDeterminant.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/index.html#alfred-consecutive-fibonacci-powers-dete).

## Brousseau's alternating series of reciprocal Fibonacci squares

Let $F_n$ denote the
Fibonacci numbers, with $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. For every positive
integer $q$, the real series
$\sum_{k \ge 1} (-1)^{k-1} \frac{F_{2k+q}}{F_k^2 \, F_{k+q}^2}$ is unconditionally summable,
with sum $\frac{1}{F_q} \sum_{k=1}^{q} \frac{(-1)^{k-1}}{F_k^2}$.

Adegoke's generalization has a further integer parameter $n$ and assumes that $q$ is even or
$nq$ is odd; this is its case $n = 1$, in which that assumption holds for every positive $q$.

## Sources

- Kunle Adegoke, "Generalizations of the Reciprocal Fibonacci-Lucas Sums of Brousseau," Journal of Integer Sequences 21 (2018), <https://cs.uwaterloo.ca/journals/JIS/VOL21/Adegoke/ade3.tex>; controlling theorem, equation, and specialization at lines 1135–1148; original reference: Brother Alfred Brousseau, "Fibonacci-Lucas Infinite Series — Research Topic," Fibonacci Quarterly 7 (1969), 211–217, Formula (6), cited at source line 1414.

Formalized by `MetaMathlibExt.brousseau_fibonacci_reciprocal_sum`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/BrousseauFibonacciReciprocal.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/BrousseauFibonacciReciprocal.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/index.html#brousseau-fibonacci-reciprocal-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci and Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers)
