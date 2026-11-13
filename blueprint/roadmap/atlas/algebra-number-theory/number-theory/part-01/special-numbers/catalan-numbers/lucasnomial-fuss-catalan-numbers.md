---
declaration: section
origin: cited
lean: MetaMathlibExt.generalized_lucasnomial_fuss_catalan_integral_general, MetaMathlibExt.generalized_lucasnomial_fuss_catalan_integral, MetaMathlibExt.generalizedLucasnomialFussCatalan, MetaMathlibExt.generalizedLucasnomialFussCatalanRS, MetaMathlibExt.generalizedLucasnomialFussCatalan_vol24_eq
statement: formalized
proof: formalized
---

# Lucasnomial Fuss–Catalan numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html).

## Integrality of generalized Lucasnomial Fuss–Catalan numbers

Let $P$ and $Q$ be integers
with $\gcd(P, Q) = 1$, let $(U_m)_{m \ge 0}$ be the Lucas sequence of the first kind with
parameters $P$ and $Q$, and suppose $U_m \ne 0$ for every $m \ge 1$. Then for all natural numbers
$r \ge 1$, $a \ge 2$ and $n \ge 1$, the rational number

$$\frac{U_r}{U_{(a-1)n+r}} \cdot \frac{\prod_{j=0}^{n-1} U_{an+r-1-j}}{\prod_{j=0}^{n-1} U_{j+1}}$$

is an integer; its second factor is the Lucasnomial coefficient $\binom{an+r-1}{n}_U$.

Formalized by `MetaMathlibExt.generalized_lucasnomial_fuss_catalan_integral_general`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalan.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalan.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html#generalized-lucasnomial-fuss-catalan-int).

## Generalized Lucasnomial Fuss–Catalan numbers are integers (Ballot)

Let $P$ and $Q$ be
nonzero integers with $\gcd(P, Q) = 1$, and let $U : \mathbb{N} \to \mathbb{Z}$ satisfy $U_0 = 0$,
$U_1 = 1$, $U_{m+2} = P U_{m+1} - Q U_m$ for every natural number $m$, and $U_m \ne 0$ for every
$m \ge 1$. Then for all natural numbers $r \ge 1$, $a \ge 2$ and $n \ge 1$, the rational number

$$\frac{U_r}{U_{(a-1)n+r}} \cdot \frac{\prod_{j=0}^{n-1} U_{an+r-1-j}}{\prod_{j=0}^{n-1} U_{j+1}}$$

is an integer; its second factor is the Lucasnomial coefficient $\binom{an+r-1}{n}_U$.

## Sources

- Christian Ballot, "Lucasnomial Fuss-Catalan Numbers and Related Divisibility Questions," Journal of Integer Sequences 21 (2018), Article 18.6.5, Theorem `thm:2`, lines 553–558, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Ballot/ballot30.tex>. Fundamental Lucas sequences, nondegeneracy, and regularity at lines 185–207; Lucasnomial coefficients at lines 215–221. It follows from `generalized_lucasnomial_fuss_catalan_integral_general`; the hypotheses `hP` and `hQ` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.generalized_lucasnomial_fuss_catalan_integral`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalan.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalan.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html#generalized-lucasnomial-fuss-catalan-int-2).

## Generalized Lucasnomial Fuss–Catalan numbers

Let $P$ be Lucas parameters, that is, nonzero
reals $p$ and $q$ whose Lucas bracket sequence $U_0 = 0$, $U_1 = 1$, $U_{m+2} = pU_{m+1} + qU_m$
satisfies $U_m \ne 0$ for every $m \ge 1$. Write $U_m! = U_1 U_2 \cdots U_m$, and let the
Lucasnomial coefficient $\binom{m}{k}_U$ be $\frac{U_m!}{U_k! \, U_{m-k}!}$ for $k \le m$ and $0$
for $k > m$. For natural numbers $a$, $r$ and $n$, the generalized Lucasnomial Fuss–Catalan number
of $P$ is the real number

$$C_{U,a,r}(n) = \frac{U_r}{U_{(a-1)n+r}} \binom{an+r-1}{n}_U.$$

The source takes $a \ge 2$, $r \ge 1$ and $n \ge 1$. Here $a$, $r$ and $n$ range over all natural
numbers: $a - 1$ and $an + r - 1$ are truncated at $0$, and the quotient is $0$ when
$U_{(a-1)n+r} = 0$.

## Sources

- Ballot, JIS Vol. 21.

Formalized by `MetaMathlibExt.generalizedLucasnomialFussCatalan`, a definition declared in [MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html#generalized-lucasnomial-fuss-catalan).

## Generalized Lucasnomial Fuss–Catalan numbers in the r, s, t notation

Let $P$ be Lucas
parameters, that is, nonzero reals $p$ and $q$ whose Lucas bracket sequence $U_0 = 0$, $U_1 = 1$,
$U_{m+2} = pU_{m+1} + qU_m$ satisfies $U_m \ne 0$ for every $m \ge 1$. Write
$U_m! = U_1 U_2 \cdots U_m$, and let the Lucasnomial coefficient $\binom{m}{k}_U$ be
$\frac{U_m!}{U_k! \, U_{m-k}!}$ for $k \le m$ and $0$ for $k > m$. For natural numbers $r$, $s$
and $t$, define the real number

$$C_{U,r,s}(t) = \frac{U_s}{U_{(r-1)t+s}} \binom{rt+s-1}{t}_U.$$

The source takes $r \ge 2$, $s \ge 1$ and $t \ge 1$. Here $r$, $s$ and $t$ range over all natural
numbers: $r - 1$ and $rt + s - 1$ are truncated at $0$, and the quotient is $0$ when
$U_{(r-1)t+s} = 0$.

## Sources

- Ballot, JIS Vol. 24.

Formalized by `MetaMathlibExt.generalizedLucasnomialFussCatalanRS`, a definition declared in [MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html#generalized-lucasnomial-fuss-catalan-rs).

## The two indexings of the generalized Lucasnomial Fuss–Catalan numbers agree

For all Lucas
parameters $P$, with Lucas bracket sequence $U$, and all natural numbers $a$, $r$ and $n$, the
generalized Lucasnomial Fuss–Catalan number $C_{U,a,r}(n)$ equals $C'_{U,a,r}(n)$, where
$C'_{U,r,s}(t)$ denotes the generalized Lucasnomial Fuss–Catalan number in the r, s, t notation.
The two definitions are the same function.

## Sources

- Ballot, JIS Vol. 21 and Vol. 24.

Formalized by `MetaMathlibExt.generalizedLucasnomialFussCatalan_vol24_eq`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucasnomialFussCatalanNumber.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html#generalized-lucasnomial-fuss-catalan-vol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucasnomial Fuss–Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/catalan-numbers/lucasnomial-fuss-catalan-numbers)
