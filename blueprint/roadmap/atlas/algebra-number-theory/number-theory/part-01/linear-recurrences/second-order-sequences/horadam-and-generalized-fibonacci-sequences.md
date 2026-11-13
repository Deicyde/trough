---
declaration: section
origin: cited
lean: MetaMathlibExt.horadam_generalized_catalan_identity, MetaMathlibExt.generalizedFibonacci_binet, MetaMathlibExt.generalizedFibonacci_mixed_identity, MetaMathlibExt.generalizedFibonacci_cassini, MetaMathlibExt.generalizedFibonacci_tendsto_ratio, MetaMathlibExt.generalizedFibonacci_binet_cassini_and_ratio_limit
statement: formalized
proof: formalized
---

# Horadam and generalized Fibonacci sequences

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html).

## Generalized Catalan identity for Horadam sequences

Let $R$ be a commutative ring, let
$c_1, c_2 \in R$, and let $W, Y, U : \mathbb{N} \to R$ be sequences that each satisfy
$x_{n+2} = c_1 x_{n+1} + c_2 x_n$ for every $n \in \mathbb{N}$, with $U_0 = 0$ and $U_1 = 1$.
Then for all $s, i, j \in \mathbb{N}$,

$$W_{s+i}\,Y_{s+j} - W_s\,Y_{s+i+j} = (-c_2)^s\,(W_1 Y_j - W_0 Y_{j+1})\,U_i.$$

The source states the identity over the integers, with integer coefficients, all integer
indices and $c_2 \ne 0$. This version restricts the indices to natural numbers and allows
coefficients in any commutative ring, so no invertibility of $c_2$ is needed; the bi-infinite
version is not claimed.

## Sources

- Aram Tangboonduangjit and Thotsaporn Thanatipanonda, "Determinants Containing Powers of Generalized Fibonacci Numbers," Journal of Integer Sequences 19 (2016), Article 16.7.1, Proposition "Generalized Catalan Identity," lines 111–126 of <https://cs.uwaterloo.ca/journals/JIS/VOL19/Tangboonduangjit/aram5.tex>.

Formalized by `MetaMathlibExt.horadam_generalized_catalan_identity`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HoradamGeneralizedCatalanIdentity.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/HoradamGeneralizedCatalanIdentity.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#horadam-generalized-catalan-identity).

## Binet formula for generalized Fibonacci sequences

Let $p$ be a real number and let
$(W_k)_{k \ge 0}$ be a real sequence with $W_{k+2} = p W_{k+1} + W_k$ for all $k \ge 0$. Put
$s = \sqrt{p^2 + 4}$, and let $\alpha = (p + s)/2$ and $\beta = (p - s)/2$, the roots of
$z^2 - pz - 1$. Then for every $n \ge 0$,
$W_n = \frac{W_1 - W_0 \beta}{s} \alpha^n + \frac{W_0 \alpha - W_1}{s} \beta^n$.

Formalized by `MetaMathlibExt.generalizedFibonacci_binet`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#generalized-fibonacci-binet).

## Mixed identity for generalized Fibonacci sequences

Let $p$ be a real number and let
$W, F : \mathbb{Z} \to \mathbb{R}$ satisfy $W_{k+2} = p W_{k+1} + W_k$ and
$F_{k+2} = p F_{k+1} + F_k$ for every integer $k$, with $F_0 = 0$ and $F_1 = 1$. Then for all
integers $m$ and $n$, $F_{m-2} W_{n-2} - F_{m-3} W_{n-1} = (-1)^{m-1} W_{n-m+1}$.

Formalized by `MetaMathlibExt.generalizedFibonacci_mixed_identity`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#generalized-fibonacci-mixed-identity).

## Cassini identity for generalized Fibonacci sequences

Let $R$ be a commutative ring, let
$p \in R$, and let $(W_k)_{k \ge 0}$ be a sequence in $R$ with $W_{k+2} = p W_{k+1} + W_k$ for
all $k \ge 0$. Then for every $n \ge 0$,
$W_n W_{n+2} - W_{n+1}^2 = (-1)^n (W_0^2 + p W_0 W_1 - W_1^2)$.

Formalized by `MetaMathlibExt.generalizedFibonacci_cassini`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#generalized-fibonacci-cassini).

## Ratio limit for generalized Fibonacci sequences

Let $p > 0$ be a real number and let
$(W_k)_{k \ge 0}$ be a real sequence with $W_0 \ge 0$, $W_1 > 0$ and
$W_{k+2} = p W_{k+1} + W_k$ for all $k \ge 0$. Then $W_{k+1}/W_k$ tends to
$(p + \sqrt{p^2 + 4})/2$ as $k \to \infty$.

Formalized by `MetaMathlibExt.generalizedFibonacci_tendsto_ratio`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#generalized-fibonacci-tendsto-ratio).

## Binet, Cassini, mixed identity and ratio limit for generalized Fibonacci sequences

Let $p \ge 1$, $a \ge 0$ and $b > 0$ be integers, and let $m \ge 0$ and $n \ge 0$ be integers.
Let $W, F : \mathbb{Z} \to \mathbb{R}$ satisfy $W_0 = a$, $W_1 = b$, $F_0 = 0$, $F_1 = 1$,
$W_{k+2} = p W_{k+1} + W_k$ and $F_{k+2} = p F_{k+1} + F_k$ for every integer $k$. Put
$s = \sqrt{p^2 + 4}$, $\alpha = (p + s)/2$ and $\beta = (p - s)/2$. Then
$W_n = \frac{b - a \beta}{s} \alpha^n + \frac{a \alpha - b}{s} \beta^n$,
$F_{m-2} W_{n-2} - F_{m-3} W_{n-1} = (-1)^{m-1} W_{n-m+1}$,
$W_n W_{n+2} - W_{n+1}^2 = (-1)^n (a^2 + p a b - b^2)$, and $W_{k+1}/W_k$ tends to $\alpha$ as
$k \to \infty$ through the natural numbers.

Here $a^2 + pab - b^2$ is the source's $\Delta$. The four parts also hold separately under weaker
hypotheses; in particular the mixed identity holds for all integers $m$ and $n$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas, and Mohammed Mekkaoui, "Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers," Journal of Integer Sequences 29 (2026), Article 26.2.5, preliminary-results lemma, lines 192–200, https://cs.uwaterloo.ca/journals/JIS/VOL29/Djellas/djellas7.tex

Formalized by `MetaMathlibExt.generalizedFibonacci_binet_cassini_and_ratio_limit`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GeneralizedFibonacciIdentities.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html#generalized-fibonacci-binet-cassini-and).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Horadam and generalized Fibonacci sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/horadam-and-generalized-fibonacci-sequences)
