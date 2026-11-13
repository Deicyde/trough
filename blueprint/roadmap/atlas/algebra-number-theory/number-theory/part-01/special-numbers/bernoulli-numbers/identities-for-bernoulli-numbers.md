---
declaration: section
origin: cited
lean: MetaMathlibExt.abel_bernoulli_sum, MetaMathlibExt.abel_hurwitz_bernoulli_multinomial, MetaMathlibExt.carlitz_bernoulli_sum_symm, MetaMathlibExt.euler_bernoulli_convolution, MetaMathlibExt.gessel_bernoulli_number_identity, MetaMathlibExt.gould_bernoulli_identity, MetaMathlibExt.kaneko_bernoulli_stirling_sum, MetaMathlibExt.tuenter_bernoulli_power_sum_identity
statement: formalized
proof: formalized
---

# Identities for Bernoulli numbers

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html).

## Abel–Bernoulli sum

Let $B_k(t)$ denote the $k$-th Bernoulli polynomial. For every natural
number $n$ and all complex numbers $x$ and $y$ with $x \neq 0$,

$$\sum_{l=0}^{n} \binom{n}{l} (x + l)^{l-1} B_{n-l}(y + n - l) = \frac{1}{x} B_n(y + x + n),$$

where $(x + l)^{l-1}$ is an integer power, so the term $l = 0$ contains the factor $x^{-1}$.

This is the first of the source's two Abel–Bernoulli sums.

## Sources

- Claudio de J. Pita Ruiz V., "Carlitz-Type and Other Bernoulli Identities," Journal of Integer Sequences 19 (2016), Article 16.1.8, Proposition [Abel-Bernoulli sums], equation (5.11), lines 790–794, https://cs.uwaterloo.ca/journals/JIS/VOL19/Pita/pita23.tex

Formalized by `MetaMathlibExt.abel_bernoulli_sum`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/AbelBernoulliSums.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/AbelBernoulliSums.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#abel-bernoulli-sum).

## Abel–Hurwitz–Bernoulli multinomial identity

Let $B_k(t)$ denote the $k$-th Bernoulli
polynomial. Let $m \ge 2$ and $n$ be natural numbers, let $x_1, \dots, x_m$ be rational numbers,
and let $r$ be an index with $1 \le r \le m$. Then

$$\sum_{l} \binom{n}{l_1, \dots, l_m} B_{l_r}(x_r + l_r) \prod_{j \neq r} (x_j + l_j)^{l_j} =
\sum_{k=0}^{n} \binom{n}{k} \frac{(m + k - 2)!}{(m - 2)!} B_{n-k}(x_1 + \dots + x_m + n),$$

where the sum on the left runs over all $l = (l_1, \dots, l_m) \in \mathbb{N}^m$ with
$l_1 + \dots + l_m = n$, and $\binom{n}{l_1, \dots, l_m}$ is the multinomial coefficient.

The source states the identity for arbitrary real or complex parameters; this statement records
its specialization to rational $x_1, \dots, x_m$.

## Sources

- Claudio de J. Pita Ruiz V., "Carlitz-Type and Other Bernoulli Identities," Journal of Integer Sequences 19 (2016), Article 16.1.8, Proposition [Abel-Hurwitz-Bernoulli identity] (a), equation (5.16), lines 821–829, https://cs.uwaterloo.ca/journals/JIS/VOL19/Pita/pita23.tex

Formalized by `MetaMathlibExt.abel_hurwitz_bernoulli_multinomial`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/AbelHurwitzBernoulli.lean, line 957](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/AbelHurwitzBernoulli.lean#L957). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#abel-hurwitz-bernoulli-multinomial).

## Carlitz's Bernoulli identity

Let $B_j$ denote the $j$-th Bernoulli number, with
$B_1 = -1/2$. For all natural numbers $m$ and $n$,

$$(-1)^m \sum_{k=0}^{m} \binom{m}{k} B_{n+k} = (-1)^n \sum_{k=0}^{n} \binom{n}{k} B_{m+k}.$$

## Sources

- Pita Ruiz, “Carlitz-Type and Other Bernoulli Identities”; original L. Carlitz, Problem 795, Mathematics Magazine 44 (1971), p. 107.

Formalized by `MetaMathlibExt.carlitz_bernoulli_sum_symm`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/CarlitzIdentity.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/CarlitzIdentity.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#carlitz-bernoulli-sum-symm).

## Euler's convolution identity for Bernoulli numbers

Let $B_j$ denote the $j$-th
Bernoulli number, with $B_1 = -1/2$. For every natural number $n \ge 1$,

$$\sum_{i=0}^{n} \binom{n}{i} B_i B_{n-i} = -n B_{n-1} - (n-1) B_n.$$

## Sources

- Ken Kamano, "Sums of Products of Bernoulli Numbers, Including Poly-Bernoulli Numbers," Journal of Integer Sequences 13 (2010), <https://cs.uwaterloo.ca/journals/JIS/VOL13/Kamano/kamano2.tex>. Lines 98–104.

Formalized by `MetaMathlibExt.euler_bernoulli_convolution`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/EulerBernoulliConvolution.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/EulerBernoulliConvolution.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#euler-bernoulli-convolution).

## Gessel's Bernoulli-number identity

Let $B_j$ denote the $j$-th Bernoulli number, with
$B_1 = -1/2$. For all natural numbers $n$, $r$ and $m$ with $r$ odd and $m \ge 1$,

$$\sum_{k=0}^{n+r} m^{n+r-k} \binom{n+r}{k} \binom{n+k+r}{r} B_{n+k} =
\frac{r+1}{2} \sum_{k=1}^{m-1} \sum_{j=0}^{r+1} \binom{n+r}{j} \binom{n+r}{r+1-j}
k^{j+n-1} (k-m)^{n+r-j}.$$

The powers on the right have integer exponents and nonzero rational bases: for $n = 0$ the terms
$j = 0$ and $j = r + 1$ have exponent $-1$.

## Sources

- Redha Chellal and Farid Bencherif, *An Identity for Generalized Bernoulli Polynomials*, Journal of Integer Sequences 23 (2020), Article 20.11.2, formula `t5` (the special case `ℓ = n` with `r` odd), lines 142–149, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Chellal/chellal7.tex>. Quoted there from H. Belbachir and M. Rahmani, *On Gessel-Kaneko's identity for Bernoulli numbers*, Appl. Anal. Discrete Math. 7 (2013), 1–10. Original: I. M. Gessel, *Applications of the classical umbral calculus*, Algebra Universalis 49 (2003), 397–434.

Formalized by `MetaMathlibExt.gessel_bernoulli_number_identity`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/GesselIdentity.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/GesselIdentity.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#gessel-bernoulli-number-identity).

## Gould's alternating identity for Bernoulli polynomials

Let $B_i$ denote the $i$-th
Bernoulli number, with $B_1 = -1/2$, and let $B_j(x) = \sum_{i=0}^{j} \binom{j}{i} B_i x^{j-i}$
be the $j$-th Bernoulli polynomial. For every natural number $n$ and every rational number $x$,

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} B_{n+1}(x - k) = \frac{(n+1)!}{2} (2x - n - 1).$$

## Sources

- Claudio de J. Pita Ruiz V., "Carlitz-Type and Other Bernoulli Identities", Journal of Integer Sequences 19 (2016), Article 16.1.8, Proposition (Gould-Bernoulli identities), equation (5.3), lines 727-732, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Pita/pita23.tex>.

Formalized by `MetaMathlibExt.gould_bernoulli_identity`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/GouldBernoulliIdentity.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/GouldBernoulliIdentity.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#gould-bernoulli-identity).

## Kaneko's Stirling-number formula for the Bernoulli numbers

Let $B_n$ denote the $n$-th
Bernoulli number, with $B_1 = -1/2$, and let $S(n, j)$ denote the Stirling numbers of the second
kind. For every natural number $n$,

$$B_n = \sum_{m=1}^{n+1} \frac{(-1)^{m-1} (m-1)!\, S(n, m-1)}{m}.$$

This is Kaneko's explicit formula for the poly-Bernoulli numbers $B_n^{(k)}$ at $k = 1$. That
formula carries a factor $(-1)^n$, which cancels against $B_n^{(1)} = (-1)^n B_n$ (the numbers
$B_n^{(1)}$ come from the generating series $t/(1 - e^{-t})$).

## Sources

- Y. Hamahata and H. Masubuchi, "Special Multi-Poly-Bernoulli Numbers," Journal of Integer Sequences 10 (2007), Article 07.4.1, Theorem [Kaneko1], lines 144–152, https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata/hamahata3.tex citing M. Kaneko, "Poly-Bernoulli numbers," Journal de Théorie des Nombres de Bordeaux 9 (1997), 221–228.

Formalized by `MetaMathlibExt.kaneko_bernoulli_stirling_sum`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/KanekoBernoulliStirling.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/KanekoBernoulliStirling.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#kaneko-bernoulli-stirling-sum).

## Tuenter's power-sum identity for Bernoulli numbers

Let $a$ and $b$ be nonzero complex
numbers and let $n \ge 1$ be a natural number with $b^n \ne a^n$. Let $\sigma_x(i) \in \mathbb{C}$,
for $x \in \mathbb{C}$ and $i \in \mathbb{N}$, satisfy
$(i+1)\,\sigma_x(i) = B_{i+1}(x+1) - B_{i+1}$ for all $x$ and $i$, where $B_m(t)$ denotes the
Bernoulli polynomial and $B_m$ the Bernoulli number, with $B_1 = -\tfrac{1}{2}$. Then

$$B_n = \frac{1}{b^n - a^n} \sum_{i=1}^{n} \binom{n}{i} B_{n-i}
\left( a^{n-1-i} \, b^i \, \sigma_{a-1}(i) - a^i \, b^{n-1-i} \, \sigma_{b-1}(i) \right),$$

where the exponents $n - 1 - i$ are integers, equal to $-1$ when $i = n$.

For a natural number $x$ and $i \ge 1$ the relation gives $\sigma_x(i) = 1^i + 2^i + \dots + x^i$.

## Sources

- Jitender Singh, *On an Arithmetic Convolution*, Journal of Integer Sequences 17 (2014), Article 14.6.7, Corollary with equation `eq23`, lines 339–344, identified there as Tuenter's identity at `c = 0`, line 348, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Singh/singh8.tex>.

Formalized by `MetaMathlibExt.tuenter_bernoulli_power_sum_identity`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/TuenterBernoulliPowerSum.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/TuenterBernoulliPowerSum.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html#tuenter-bernoulli-power-sum-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Identities for Bernoulli numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/bernoulli-numbers/identities-for-bernoulli-numbers)
