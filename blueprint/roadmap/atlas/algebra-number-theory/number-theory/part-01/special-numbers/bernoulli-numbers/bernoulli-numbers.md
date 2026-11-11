---
declaration: section
origin: cited
lean: MetaMathlibExt.IsApostolBernoulliSequence, MetaMathlibExt.IsAppellSequence, MetaMathlibExt.faulhaber_bernoulli_polynomial_sum, MetaMathlibExt.kummer_congruence
statement: formalized
proof: formalized
---

# Bernoulli numbers and polynomials: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html).

Bernoulli numbers and polynomials, identities, denominators, Kummer congruences, Faulhaber sums, Appell sequences, higher-order and Apostol variants.

## Apostol–Bernoulli numbers

Let $\alpha$ be a complex number and let $\log$ denote the
principal branch of the complex logarithm. A sequence $(\beta_k)_{k \ge 0}$ of complex numbers
is the sequence of Apostol–Bernoulli numbers $\beta_k(\alpha)$ when $\alpha \ne 0$,
$\alpha \ne 1$, and for every complex number $t$ with $|t| < |\log \alpha|$ the series
$\sum_{k \ge 0} \beta_k t^k / k!$ converges unconditionally to $t / (\alpha e^t - 1)$.

Formalized by `MetaMathlibExt.IsApostolBernoulliSequence`, a definition declared in [MathlibExt/NumberTheory/ApostolBernoulliNumber.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ApostolBernoulliNumber.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html#is-apostol-bernoulli-sequence).

## Appell sequence

Let $R$ be a field of characteristic zero. A sequence of polynomials
$(p_n)_{n \ge 0}$ over $R$ is an Appell sequence when, for every $n$, the polynomial $p_n$ has
degree exactly $n$ (in particular $p_n \ne 0$) and the formal derivative of $p_{n+1}$ equals
$(n + 1)\, p_n$.

Formalized by `MetaMathlibExt.IsAppellSequence`, a definition declared in [MathlibExt/NumberTheory/AppellSequence.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AppellSequence.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html#is-appell-sequence).

## Faulhaber-type summation formula for Bernoulli polynomials

Let $B_i$ denote the
$i$-th Bernoulli number, with $B_1 = -1/2$, and let
$B_j(X) = \sum_{i=0}^{j} \binom{j}{i} B_i X^{j-i} \in \mathbb{Q}[X]$ be the $j$-th Bernoulli
polynomial. For all natural numbers $k$ and $n$, the following identity holds in $\mathbb{Q}[X]$:

$$\sum_{j=1}^{n} B_k(X + j) = \frac{1}{k+1} \sum_{r=0}^{k} \binom{k+1}{r+1}
\left(B_{r+1}(n+1) + (-1)^r B_{r+1}\right) B_{k-r}(X).$$

## Sources

- Claudio de J. Pita Ruiz V., *Carlitz-Type and Other Bernoulli Identities*, Journal of Integer Sequences 19 (2016), Article 16.1.8, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Pita/pita23.tex>, Proposition [Faulhaber-type formula], equation (5.32), lines 1001-1007.

Formalized by `MetaMathlibExt.faulhaber_bernoulli_polynomial_sum`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/FaulhaberBernoulliPolynomialSummation.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Bernoulli/FaulhaberBernoulliPolynomialSummation.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html#faulhaber-bernoulli-polynomial-sum).

## Kummer's congruence

Let $p$ be a prime, let $B_j$ denote the $j$-th Bernoulli number,
with $B_1 = -1/2$, and let $t$ be a natural number. Let $m$ and $n$ be natural numbers, neither
divisible by $p - 1$, with $m \equiv n \pmod{(p-1)p^t}$. Then the rational numbers

$$\frac{(1 - p^{m-1}) B_m}{m} \quad \text{and} \quad \frac{(1 - p^{n-1}) B_n}{n}$$

are either equal, or their difference has $p$-adic valuation at least $t + 1$.

In other words, the two numbers agree modulo $p^{t+1}$; equality is listed as a separate case
because the $p$-adic valuation of $0$ is taken to be $0$.

Proof: We use Voronoi's finite-sum congruence in p-adic norm form, following
Ireland--Rosen, Ch. 15 §2, and Washington, Cor. 5.14, back to Kummer's 1851 paper.

## Sources

- Ernst Eduard Kummer, "Über eine allgemeine Eigenschaft der rationalen Entwickelungscoefficienten einer bestimmten Gattung analytischer Functionen," Journal für die reine und angewandte Mathematik 41 (1851), 368–372, DOI 10.1515/crll.1851.41.368, https://doi.org/10.1515/crll.1851.41.368.

Formalized by `MetaMathlibExt.kummer_congruence`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/KummerCongruence.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Bernoulli/KummerCongruence.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html#kummer-congruence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli numbers and polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/bernoulli-numbers)
