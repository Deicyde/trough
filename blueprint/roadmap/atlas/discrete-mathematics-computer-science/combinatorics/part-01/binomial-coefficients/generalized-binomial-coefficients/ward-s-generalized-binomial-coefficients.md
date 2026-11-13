---
declaration: section
origin: cited
lean: MetaMathlibExt.wardUnitsCarry, MetaMathlibExt.wardGeneralizedBinomialCoefficient, MetaMathlibExt.wardUnitsCarry_eq_div, MetaMathlibExt.wardGeneralizedBinomialCoefficient_eq_prod_Icc, MetaMathlibExt.ward_sbinomial_carry_product_general, MetaMathlibExt.ward_sbinomial_carry_product
statement: formalized
proof: formalized
---

# Ward's generalized binomial coefficients

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html).

## Units-place carry

For natural numbers $b$, $n$ and $m$, the units-place carry
$\varepsilon_0^{b,n,m}$ of $n + m$ in base $b$ is $1$ if $b > 1$ and
$(n \bmod b) + (m \bmod b) \ge b$, and $0$ otherwise; in particular it is $0$ for the invalid
bases $b \le 1$.

Formalized by `MetaMathlibExt.wardUnitsCarry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-units-carry).

## Ward generalized binomial coefficient

Let $R$ be a commutative monoid and
$s = (s_b)_{b \in \mathbb{N}}$ a sequence in $R$. For natural numbers $n$ and $m$, the Ward
generalized binomial coefficient is

$$\binom{n+m}{n}_s = \prod_{b=2}^{n+m} s_b^{\varepsilon_0^{b,n,m}},$$

where $\varepsilon_0^{b,n,m} \in \{0, 1\}$ is the carry in the units place when $n$ and $m$ are
added in base $b$.

This is Ward's product $\prod_{b > 1} s_b^{\varepsilon_0^{b,n,m}}$: no base larger than $n + m$
carries in the units place, so the product is finite. The source uses the product as a
definition for arbitrary coefficient sequences, including sequences with zero terms.

Formalized by `MetaMathlibExt.wardGeneralizedBinomialCoefficient`, a definition declared in [MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-generalized-binomial-coefficient).

## Units-place carry as a quotient

For all natural numbers $b$, $n$ and $m$, the units-place
carry of $n + m$ in base $b$ (taken to be $0$ when $b \le 1$) equals
$\lfloor ((n \bmod b) + (m \bmod b)) / b \rfloor$, where $n \bmod 0 = n$ and division by $0$
gives $0$.

Formalized by `MetaMathlibExt.wardUnitsCarry_eq_div`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-units-carry-eq-div).

## Ward's generalized binomial coefficient as a finite product

Let $R$ be a commutative
monoid and $s = (s_b)_{b \in \mathbb{N}}$ a sequence in $R$. For all natural numbers $n$ and $m$,
the Ward generalized binomial coefficient $\binom{n+m}{n}_s$ equals

$$\prod_{b=2}^{n+m} s_b^{\lfloor ((n \bmod b) + (m \bmod b)) / b \rfloor}.$$

Formalized by `MetaMathlibExt.wardGeneralizedBinomialCoefficient_eq_prod_Icc`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WardGeneralizedBinomial.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-generalized-binomial-coefficient-eq).

## Ward's identity with hypotheses at positive indices

Let
$s, f : \mathbb{N} \to \mathbb{Z}$ satisfy $s(b) \ne 0$ for every $b \ge 1$ and
$f(k) = \prod_{d \mid k} s(d)$ for every $k \ge 1$, the product running over the positive
divisors of $k$. Write $f!(t) = \prod_{i=1}^{t} f(i)$. Let $n$ and $m$ be natural numbers, and
let $\binom{n+m}{n}_s$ be the Ward generalized binomial coefficient of $s$ at $n$ and $m$. Then
the identity

$$\frac{f!(n+m)}{f!(n) \, f!(m)} = \binom{n+m}{n}_s$$

holds in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.ward_sbinomial_carry_product_general`, a theorem declared in [MathlibExt/NumberTheory/WardSBinomialCarryProduct.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WardSBinomialCarryProduct.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-sbinomial-carry-product-general).

## Ward's identity for generalized binomial coefficients

Let
$s, f : \mathbb{N} \to \mathbb{Z}$ satisfy $s(b) \ne 0$ for every natural number $b$ and
$f(k) = \prod_{d \mid k} s(d)$ for every natural number $k$, the product running over the
positive divisors of $k$ (empty for $k = 0$). Write $f!(t) = \prod_{i=1}^{t} f(i)$. Then for all
natural numbers $n$ and $m$, the identity

$$\frac{f!(n+m)}{f!(n) \, f!(m)} =
\prod_{b=2}^{n+m} s(b)^{\lfloor ((n \bmod b) + (m \bmod b)) / b \rfloor}$$

holds in $\mathbb{Q}$.

The exponent $\lfloor ((n \bmod b) + (m \bmod b)) / b \rfloor$ is the carry in the ones position
when adding $n$ and $m$ in base $b$; for the classical case this recovers Kummer's carry-count
theorem.

## Sources

- Tom Edgar and Michael Z. Spivey, "Multiplicative Functions, Generalized Binomial Coefficients, and Generalized Catalan Numbers," Journal of Integer Sequences 19 (2016), Article 16.1.6, Theorem [Ward] `thmward` (equation `wardeqn`), lines 475–482, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Edgar/edgar3.tex>; attributed there to M. Ward.

Formalized by `MetaMathlibExt.ward_sbinomial_carry_product`, a theorem declared in [MathlibExt/NumberTheory/WardSBinomialCarryProduct.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WardSBinomialCarryProduct.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html#ward-sbinomial-carry-product).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ward's generalized binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/ward-s-generalized-binomial-coefficients)
