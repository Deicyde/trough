---
declaration: section
origin: cited
lean: MetaMathlibExt.laurentCartier, MetaMathlibExt.coeff_laurentCartier, MetaMathlibExt.laurentDeg, MetaMathlibExt.laurentDeg_le_iff, MetaMathlibExt.SeqFactorOccursAt, MetaMathlibExt.IsRecurrentSeq, MetaMathlibExt.IsUniformlyRecurrentSeq, MetaMathlibExt.IsLinearlyRecurrentSeq
statement: formalized
---

# Constant terms of powers of Laurent polynomials

33 results, 11 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html).

## Cartier operator $\Lambda_k$ on Laurent polynomials

Let $R$ be a semiring and $f$ a
Laurent polynomial in $r$ variables with coefficients in $R$. For a natural number $k > 0$,
$\Lambda_k f$ keeps the terms of $f$ whose exponents are all multiples of $k$ and substitutes
$x_s^k \mapsto x_s$ for each variable, so that the coefficient of $x^j$ in $\Lambda_k f$ is the
coefficient of $x^{kj}$ in $f$ for every $j \in \mathbb{Z}^r$. For $k = 0$ it is set to
$\Lambda_0 f = 0$ (the paper uses only positive $k$).

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Section 2 (definition of `Λ_k`).

Formalized by `MetaMathlibExt.laurentCartier`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-cartier).

## Coefficients of Kohen's operator $\Lambda_k$

Let $R$ be a semiring and let $r$ and
$k \ne 0$ be natural numbers. For every Laurent polynomial $f$ in $r$ variables with coefficients
in $R$ and every $j \in \mathbb{Z}^r$, the coefficient of $x^j$ in $\Lambda_k f$ is the
coefficient of $x^{kj}$ in $f$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Section 2 (definition of `Λ_k`).

Formalized by `MetaMathlibExt.coeff_laurentCartier`, a theorem declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#coeff-laurent-cartier).

## Degree of a Laurent polynomial

Let $R$ be a semiring and let $f$ be a Laurent polynomial
in $r$ variables $x_1, \dots, x_r$ with coefficients in $R$. Kohen's degree $\deg f$ of $f$ is the
largest absolute value $|j_i|$ of a single exponent, taken over all $i$ and all exponent vectors
$j \in \mathbb{Z}^r$ whose monomial $x^j$ has nonzero coefficient in $f$, and is $0$ if there is
no such exponent (in particular for the zero polynomial). For example, over $\mathbb{Z}$ in two
variables $x, y$ one has $\deg(5x^{-3}y^{-2} + 2xy^{-1}) = 3$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Section 1.1.

Formalized by `MetaMathlibExt.laurentDeg`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-deg).

## Exponent criterion for the degree of a Laurent polynomial

Let $R$ be a semiring, let
$r$ and $m$ be natural numbers, and let $f$ be a Laurent polynomial in $r$ variables
$x_1, \dots, x_r$ with coefficients in $R$. Then Kohen's degree of $f$ (the largest absolute
value of a single exponent occurring in $f$, or $0$ if there is none) is at most $m$ if and only
if every exponent vector $j \in \mathbb{Z}^r$ whose monomial $x^j$ has nonzero coefficient in
$f$ satisfies $|j_i| \le m$ for every $i$, that is, lies in $[-m, m]^r$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Section 1.1.

Formalized by `MetaMathlibExt.laurentDeg_le_iff`, a theorem declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-deg-le-iff).

## Occurrence of a sequence factor at a position

Let $s = (s_n)_{n \ge 0}$ be a sequence and
let $i$, $\ell$ and $i'$ be natural numbers. The factor of $s$ of length $\ell$ starting at
position $i$ occurs at position $i'$ when $s_{i'+t} = s_{i+t}$ for every natural number $t < \ell$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.SeqFactorOccursAt`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#seq-factor-occurs-at).

## Recurrent sequence

A sequence $s : \mathbb{N} \to \alpha$ is recurrent if every
occurrence of a factor is followed by a later occurrence: for all $i, \ell \in \mathbb{N}$ there
is $j > 0$ such that $s(i + j + t) = s(i + t)$ for every $t < \ell$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, definition before Proposition 19.

Formalized by `MetaMathlibExt.IsRecurrentSeq`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-recurrent-seq).

## Uniformly recurrent sequence

A sequence $s : \mathbb{N} \to \alpha$ is uniformly
recurrent if for every factor $w$ there is a constant $C_w$ such that every occurrence of $w$ is
followed by another occurrence at distance at most $C_w$: for all $i, \ell \in \mathbb{N}$ there
is $C \in \mathbb{N}$ such that for every $i'$ with $s(i' + t) = s(i + t)$ for all $t < \ell$,
there is $j$ with $0 < j \le C$ and $s(i' + j + t) = s(i + t)$ for all $t < \ell$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.IsUniformlyRecurrentSeq`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-uniformly-recurrent-seq).

## Linearly recurrent sequence

A sequence $s = (s_n)_{n \in \mathbb{N}}$ with values in a
set $\alpha$ is linearly recurrent if there is $K \in \mathbb{N}$ such that for all
$i, i' \in \mathbb{N}$ and $\ell \ge 1$ with $s_{i'+t} = s_{i+t}$ for all $t < \ell$, there is $j$
with $0 < j \le K \ell$ and $s_{i'+j+t} = s_{i+t}$ for all $t < \ell$. That is, each occurrence
of a nonempty factor of length $\ell$ is followed by another occurrence starting at most
$K \ell$ positions later.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.IsLinearlyRecurrentSeq`, a definition declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq).

## Linearly recurrent sequences are uniformly recurrent

Every linearly recurrent sequence
$s : \mathbb{N} \to \alpha$, with values in any type $\alpha$, is uniformly recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.IsLinearlyRecurrentSeq.isUniformlyRecurrentSeq`, a theorem declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-uniformly-recurrent-seq-2).

## Uniformly recurrent sequences are recurrent

Every uniformly recurrent sequence
$s : \mathbb{N} \to \alpha$, with values in any type $\alpha$, is recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.IsUniformlyRecurrentSeq.isRecurrentSeq`, a theorem declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-recurrent-seq-2).

## Constant sequences are linearly recurrent

For every set $\alpha$ and every $c \in \alpha$,
the constant sequence $n \mapsto c$ on $\mathbb{N}$ is linearly recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Definition 1.

Formalized by `MetaMathlibExt.isLinearlyRecurrentSeq_const`, a theorem declared in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq-const).

## Rowland–Zeilberger congruence

Let $p$ be a prime and let $P$ and $Q$ be Laurent
polynomials in $r$ variables with integer coefficients. Write $\operatorname{ct}[F]$ for the
constant term of a Laurent polynomial $F$ and $\Lambda_p$ for Kohen's operator, which keeps the
terms whose exponents are all divisible by $p$ and replaces $x^{pj}$ by $x^j$. Then for all
natural numbers $n$ and $k$,
$\operatorname{ct}[P^{pn+k} Q] \equiv \operatorname{ct}[P^n \Lambda_p(P^k Q)] \pmod{p}$.

The exponents $n$ and $k$ are natural numbers; the paper writes "integers", but negative powers
of a general Laurent polynomial are undefined.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 3 (`jis-2026-26.4.2-lem-3`).

Stated but not proved: `MetaMathlibExt.constantTerm_pow_mul_modEq_laurentCartier` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#constant-term-pow-mul-mod-eq-laurent-car).

## Degree bound for the Rowland–Zeilberger states

Let $p$ be a prime and let $P$ and $Q$
be Laurent polynomials in $r$ variables with integer coefficients. Write $\deg F$ for the largest
absolute value of an exponent of a variable occurring in $F$, and $\Lambda_p$ for the operator
that keeps the terms whose exponents are all multiples of $p$ and substitutes $x_s^p \mapsto x_s$.
For every finite list $k_1, \dots, k_n$ of natural numbers with each $k_t < p$, starting from $Q$
and applying $R \mapsto \Lambda_p(P^{k_t} R)$ for $t = 1, \dots, n$ in turn gives a Laurent
polynomial of degree at most $\max(\deg P - 1, \deg Q)$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 4 (`jis-2026-26.4.2-lem-4`).

Stated but not proved: `MetaMathlibExt.laurentDeg_foldl_laurentCartier_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-deg-foldl-laurent-cartier-le).

## Cartier operator applied to a power times a monomial

Let $p$ be a prime and $P$ a
Laurent polynomial in $r$ variables with integer coefficients. Write $\mathrm{coef}_e[F]$ for the
coefficient of $x^e$ in a Laurent polynomial $F$, $\deg F$ for the largest absolute value of an
exponent of a variable occurring in $F$, and $\Lambda_p$ for the Cartier operator with
$\mathrm{coef}_j[\Lambda_p F] = \mathrm{coef}_{pj}[F]$. Let $m \in \mathbb{N}$ with
$\deg P \le m + 1$, put $T = [-m, m]^r \subset \mathbb{Z}^r$, and let $k < p$ be a natural
number and $i \in T$. Then
$\Lambda_p(P^k x^i) = \sum_{j \in T} \mathrm{coef}_{pj - i}[P^k] \, x^j$.

In Kohen's notation $\mathrm{coef}_{pj - i}[P^k]$ is $a^k_{i - pj}$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 6 (`jis-2026-26.4.2-prop-6`).

Stated but not proved: `MetaMathlibExt.laurentCartier_pow_mul_single_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-cartier-pow-mul-single-eq-sum).

## Kohen's linear representation step modulo $p$

Let $p$ be a prime, let $P$ be a Laurent
polynomial in $r$ variables with integer coefficients, and write $\deg P$ for the largest absolute
value of an exponent of a single variable in a monomial occurring in $P$ ($0$ if $P = 0$). Let $m$
be a natural number with $\deg P \le m + 1$. Write $T = [-m, m]^r \subseteq \mathbb{Z}^r$ and
$[x^e]F$ for the coefficient of $x^e$ in a Laurent polynomial $F$. Then for every natural number
$k < p$, every natural number $n$ and every $i \in T$,

$$[x^{-i}]P^{pn+k} \equiv \sum_{j \in T} [x^{pj - i}]P^k \cdot [x^{-j}]P^n \pmod{p}.$$

With Kohen's $a^n_i = [x^{-i}]P^n$, $\gamma(k) = (a^k_{i-pj})_{i,j \in T}$ and
$V(n) = (a^n_i)_{i \in T}$, this is the entrywise form of $\gamma(k) V(n) = V(pn + k)$ over
$\mathbb{F}_p$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 9 (`jis-2026-26.4.2-lem-9`).

Stated but not proved: `MetaMathlibExt.coeff_pow_modEq_sum_gamma_mul_V` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#coeff-pow-mod-eq-sum-gamma-mul-v).

## Powers of $\gamma(0)$ modulo $p$ stabilize at a matrix unit

Let $p$ be a prime, let
$r, m \ge 0$ be natural numbers, let $T = \{-m, \dots, m\}^r \subseteq \mathbb{Z}^r$, and let
$\gamma(0)$ be the $T \times T$ matrix over $\mathbb{Z}/p\mathbb{Z}$ whose $(i, j)$ entry is $1$
if $i = p j$ and $0$ otherwise. Then there is $s \in \mathbb{N}$ such that for every $s' \ge s$,
$\gamma(0)^{s'}$ is the matrix whose $(0, 0)$ entry is $1$ and whose other entries are $0$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 11 (`jis-2026-26.4.2-lem-11`).

Stated but not proved: `MetaMathlibExt.exists_gammaZero_pow_eq_single` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-gamma-zero-pow-eq-single).

## Divisibility of constant terms of powers is decided on a bounded prefix

Let $p$ be a
prime, let $r$ and $d$ be natural numbers, and write $\operatorname{ct}[F]$ for the constant term
of a Laurent polynomial $F$ and $\deg F$ for the largest absolute value of an exponent of a single
variable in a monomial occurring in $F$ ($0$ if $F = 0$). There is a natural number $B$ such that
for every Laurent polynomial $P$ in $r$ variables with integer coefficients and $\deg P \le d$, if
$p$ divides $\operatorname{ct}[P^n]$ for some natural number $n$, then $p$ divides
$\operatorname{ct}[P^{n_0}]$ for some natural number $n_0 < B$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 12 (`jis-2026-26.4.2-prop-12`).

Stated but not proved: `MetaMathlibExt.exists_bound_constantTerm_pow_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-bound-constant-term-pow-dvd).

## Density-one zeros of constant terms modulo $p$

Let $p$ be a prime, let $P$ be a Laurent
polynomial in $r$ variables with integer coefficients, write $\operatorname{ct}[F]$ for the
constant term of a Laurent polynomial $F$, and suppose that $p$ divides $\operatorname{ct}[P^n]$
for some natural number $n$. Then for every Laurent polynomial $Q$ in $r$ variables with integer
coefficients, the set of natural numbers $n$ with $p \mid \operatorname{ct}[P^n Q]$ has natural
density $1$; for every natural number $L$ there is a natural number $i$ such that
$p \mid \operatorname{ct}[P^{i+t} Q]$ for all $t < L$; and either
$p \mid \operatorname{ct}[P^n Q]$ for every $n$, or the sequence of residues
$\operatorname{ct}[P^n Q] \bmod p$ in $\mathbb{Z}/p\mathbb{Z}$ is not uniformly recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Theorem 14 (`jis-2026-26.4.2-thm-14`).

Stated but not proved: `MetaMathlibExt.constantTerm_zero_density_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#constant-term-zero-density-mod-prime).

## Return to the initial coefficient vector modulo $p$

Let $p$ be a prime, let
$m \in \mathbb{N}$, and let $P$ be a Laurent polynomial with integer coefficients in variables
$x_1, \dots, x_r$ with $\deg P \le m + 1$, where $\deg P$ is the largest absolute value of an
exponent of a single variable in a monomial occurring in $P$ (and $0$ if $P = 0$). Let
$T = \{-m, \dots, m\}^r$. Then there is $t_0 \in \mathbb{N}$ such that for every $n \in \mathbb{N}$
for which $p$ does not divide the constant term of $P^n$, there is $j < p^{t_0}$ such that for
every $i \in T$ the coefficient of $x^{-i}$ in $P^{p^{t_0} n + j}$ is congruent modulo $p$ to $1$
if $i = 0$ and to $0$ otherwise.

Equivalently, writing $V(n)$ for the vector of coefficients of $x^{-i}$ in $P^n$, $i \in T$,
reduced modulo $p$, the block $V(p^{t_0} n), \dots, V(p^{t_0} n + p^{t_0} - 1)$ contains $V(0)$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 15 (`jis-2026-26.4.2-prop-15`).

Stated but not proved: `MetaMathlibExt.exists_sigma_pow_V_contains_V_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-sigma-pow-v-contains-v-zero).

## Linear recurrence of constant terms modulo $p$

Let $p$ be a prime and let $P, Q$ be
Laurent polynomials with integer coefficients in $r$ variables; write $\operatorname{ct}[f]$ for
the constant term of $f$. Suppose $p \nmid \operatorname{ct}[P^n Q]$ for some $n \in \mathbb{N}$.
Then the sequence $u_n = \operatorname{ct}[P^n Q] \bmod p$ is linearly recurrent if and only if
$p \nmid \operatorname{ct}[P^n]$ for all $n \in \mathbb{N}$, and if $u$ is not linearly recurrent,
then the set of $n$ with $p \mid \operatorname{ct}[P^n Q]$ has natural density $1$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Theorem 16 (`jis-2026-26.4.2-thm-16`).

Stated but not proved: `MetaMathlibExt.isLinearlyRecurrentSeq_constantTerm_mod_prime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq-constant-term).

## Linear recurrence of combinations of constant terms modulo $p$

Let $p$ be a prime, let
$P, Q_1, \dots, Q_\ell$ be Laurent polynomials with integer coefficients in $r$ variables, let
$k_1, \dots, k_\ell \in \mathbb{N}$, and let $F \colon (\mathbb{Z}/p\mathbb{Z})^\ell \to X$ be a
map to a set $X$. Write $\operatorname{ct}[f]$ for the constant term of $f$ and, for
$n \in \mathbb{N}$, let
$b_n = F(\operatorname{ct}[P^{n+k_1} Q_1] \bmod p, \dots,
\operatorname{ct}[P^{n+k_\ell} Q_\ell] \bmod p)$.
Suppose $b_n \ne F(0, \dots, 0)$ for some $n$. Then $(b_n)$ is linearly recurrent if and only if
$p \nmid \operatorname{ct}[P^n]$ for all $n \in \mathbb{N}$, and if $p \mid \operatorname{ct}[P^n]$
for some $n$, then the set of $n$ with $b_n = F(0, \dots, 0)$ has natural density $1$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Corollary 17 (`jis-2026-26.4.2-cor-17`).

Stated but not proved: `MetaMathlibExt.isLinearlyRecurrentSeq_combination_mod_prime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq-combination-mo).

## Recurrence of constant-term sequences modulo a prime

Let $p$ be a prime and let $P$ and
$Q$ be Laurent polynomials in $r$ variables with integer coefficients; write $\mathrm{ct}[F]$ for
the constant term of a Laurent polynomial $F$. If $p \nmid \mathrm{ct}[P^{n_0}]$ for some
$n_0 > 0$, then the sequence of residues $(\mathrm{ct}[P^n Q] \bmod p)_{n \ge 0}$ in
$\mathbb{Z}/p\mathbb{Z}$ is recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 19 (`jis-2026-26.4.2-prop-19`).

Stated but not proved: `MetaMathlibExt.isRecurrentSeq_constantTerm_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-recurrent-seq-constant-term-mod-prime).

## Divisibility of constant terms of powers of $P$ and $\tilde P$

Let $p$ be a prime, let
$a \ge 1$ and $\ell$ be natural numbers, and let $P$ and $\tilde P$ be Laurent polynomials in $r$
variables with integer coefficients such that $P^{p^{a-1}} \equiv \tilde P(x^{p^\ell}) \pmod{p^a}$
coefficientwise, where $\tilde P(x^q)$ is obtained from $\tilde P$ by replacing each monomial
$x^e$ with $x^{qe}$. Write $\operatorname{ct}[F]$ for the constant term of a Laurent polynomial
$F$. Then $p$ divides $\operatorname{ct}[P^{n_0}]$ for some natural number $n_0$ if and only if
$p$ divides $\operatorname{ct}[\tilde P^{n_1}]$ for some natural number $n_1$; moreover, for every
natural number $n_0$ with $p \mid \operatorname{ct}[P^{n_0}]$, also
$p \mid \operatorname{ct}[\tilde P^{n_0}]$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 22 (`jis-2026-26.4.2-lem-22`).

Stated but not proved: `MetaMathlibExt.exists_constantTerm_pow_dvd_iff_tilde` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-constant-term-pow-dvd-iff-tilde).

## Passing from $P$ to $\tilde P$ modulo $p^a$

Let $p$ be a prime, let $a \ge 1$ and $\ell$
be natural numbers, and let $P$ and $\tilde P$ be Laurent polynomials in $r$ variables with
integer coefficients such that $P^{p^{a-1}} \equiv \tilde P(x^{p^\ell}) \pmod{p^a}$
coefficientwise, where $\tilde P(x^q)$ is obtained from $\tilde P$ by replacing each monomial
$x^e$ with $x^{qe}$. Write $\operatorname{ct}[F]$ for the constant term of a Laurent polynomial
$F$ and $\Lambda_q$ for Kohen's operator, which keeps the terms whose exponents are all divisible
by $q$ and replaces $x^{qj}$ by $x^j$. Then for every Laurent polynomial $Q$ in $r$ variables
with integer coefficients and all natural numbers $n$ and $k$,
$\operatorname{ct}[P^{p^{a-1} n + k} Q] \equiv
\operatorname{ct}[\tilde P^n \Lambda_{p^\ell}(P^k Q)] \pmod{p^a}$.

The statement holds for every natural number $k$; the paper restricts to $k < p^{a-1}$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 23 (`jis-2026-26.4.2-prop-23`).

Stated but not proved: `MetaMathlibExt.constantTerm_pow_mul_modEq_tilde` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#constant-term-pow-mul-mod-eq-tilde).

## Rowland–Zeilberger congruence modulo $p^a$

Let $p$ be a prime, let $a$ be a natural
number, and let $\tilde P$ be a Laurent polynomial in $r$ variables with integer coefficients
such that $\tilde P^p \equiv \tilde P(x^p) \pmod{p^a}$ coefficientwise, where $\tilde P(x^p)$
is obtained from $\tilde P$ by replacing each monomial $x^e$ with $x^{pe}$. Write
$\operatorname{ct}[F]$ for the constant term of a Laurent polynomial $F$ and $\Lambda_p$ for
Kohen's operator, which keeps the terms whose exponents are all divisible by $p$ and replaces
$x^{pj}$ by $x^j$. Then for every Laurent polynomial $Q$ in $r$ variables with integer
coefficients and all natural numbers $n$ and $k$,
$\operatorname{ct}[\tilde P^{pn+k} Q] \equiv
\operatorname{ct}[\tilde P^n \Lambda_p(\tilde P^k Q)] \pmod{p^a}$.

The statement holds for every natural number $k$; the paper states it for $k \in \mathbb{F}_p$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 24 (`jis-2026-26.4.2-lem-24`).

Stated but not proved: `MetaMathlibExt.constantTerm_tilde_pow_mul_modEq_laurentCartier` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#constant-term-tilde-pow-mul-mod-eq-laure).

## Degree bound for the Rowland–Zeilberger states mod $p^a$

Let $p$ be a prime, let $a$
be a natural number, and let $\tilde P$ and $Q_0$ be Laurent polynomials in $r$ variables with
coefficients in $\mathbb{Z}/p^a\mathbb{Z}$. Write $\deg F$ for the largest absolute value of an
exponent of a variable occurring in $F$, and $\Lambda_p$ for the operator that keeps the terms
whose exponents are all multiples of $p$ and substitutes $x_s^p \mapsto x_s$. For every finite
list $k_1, \dots, k_n$ of natural numbers with each $k_t < p$, starting from $Q_0$ and applying
$Q \mapsto \Lambda_p(\tilde P^{k_t} Q)$ for $t = 1, \dots, n$ in turn gives a Laurent polynomial
of degree at most $\max(\deg \tilde P - 1, \deg Q_0)$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 25 (`jis-2026-26.4.2-lem-25`).

Stated but not proved: `MetaMathlibExt.laurentDeg_foldl_laurentCartier_le_zmod` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#laurent-deg-foldl-laurent-cartier-le-zmo).

## Kohen's linear representation step modulo $p^a$

Let $p$ be a prime, let $a$ be a natural
number, and let $\tilde P$ be a Laurent polynomial in $r$ variables with integer coefficients such
that $\tilde P^p \equiv \tilde P(x^p) \pmod{p^a}$ coefficientwise, where $\tilde P(x^p)$ is
obtained from $\tilde P$ by replacing each monomial $x^e$ with $x^{pe}$. Write $\deg \tilde P$ for
the largest absolute value of an exponent of a single variable in a monomial occurring in
$\tilde P$ ($0$ if $\tilde P = 0$). Let $m$ be a natural number with $\deg \tilde P \le m + 1$,
and write $T = [-m, m]^r \subseteq \mathbb{Z}^r$ and $[x^e]F$ for the coefficient of $x^e$ in a
Laurent polynomial $F$. Then for every natural number $k < p$, every natural number $n$ and every
$i \in T$,

$$
[x^{-i}]\tilde P^{pn+k} \equiv
\sum_{j \in T} [x^{pj - i}]\tilde P^k \cdot [x^{-j}]\tilde P^n \pmod{p^a}.
$$

This is the entrywise form of Kohen's step $\tilde\gamma(k) \tilde V(n) = \tilde V(pn + k)$ over
$\mathbb{Z}/p^a\mathbb{Z}$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 28 (`jis-2026-26.4.2-lem-28`).

Stated but not proved: `MetaMathlibExt.coeff_tilde_pow_modEq_sum_gamma_mul_V` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#coeff-tilde-pow-mod-eq-sum-gamma-mul-v).

## Powers of $\tilde\gamma(0)$ modulo $p^a$ stabilize at a matrix unit

Let $p$ be a prime,
let $a \ge 1$, $r$ and $m$ be natural numbers, let $T = \{-m, \dots, m\}^r \subseteq \mathbb{Z}^r$,
and let $\tilde\gamma(0)$ be the $T \times T$ matrix over $\mathbb{Z}/p^a\mathbb{Z}$ whose
$(i, j)$ entry is $1$ if $i = p j$ and $0$ otherwise. Then there is $s \in \mathbb{N}$ such that for
every $s' \ge s$, $\tilde\gamma(0)^{s'}$ is the matrix whose $(0, 0)$ entry is $1$ and whose other
entries are $0$.

Kohen's Lemma 30 prints $\tilde\gamma(0)^s$; as in Lemma 11, it is read for every exponent
$s' \ge s$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 30 (`jis-2026-26.4.2-lem-30`).

Stated but not proved: `MetaMathlibExt.exists_gammaZero_pow_eq_single_zmod` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-gamma-zero-pow-eq-single-zmod).

## Density-one zeros of constant terms modulo $p^a$

Let $p$ be a prime, let $a$ be a natural
number, and let $\tilde P$ be a Laurent polynomial in $r$ variables with integer coefficients such
that $\tilde P^p \equiv \tilde P(x^p) \pmod{p^a}$ coefficientwise, where $\tilde P(x^p)$ is
obtained from $\tilde P$ by replacing each monomial $x^e$ with $x^{pe}$. Write
$\operatorname{ct}[F]$ for the constant term of a Laurent polynomial $F$, and suppose that $p$
divides $\operatorname{ct}[\tilde P^{n_0}]$ for some natural number $n_0$. Then for every
Laurent polynomial $Q$ in $r$ variables with integer coefficients, the set of natural numbers $n$
such that $p^a$ divides $\operatorname{ct}[\tilde P^n Q]$ has natural density $1$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Lemma 31 (`jis-2026-26.4.2-lem-31`).

Stated but not proved: `MetaMathlibExt.constantTerm_tilde_zero_density` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#constant-term-tilde-zero-density).

## Return to the initial coefficient vector modulo $p^a$

Let $p$ be a prime, let
$a, m \in \mathbb{N}$, and let $\tilde P$ be a Laurent polynomial with integer coefficients in
variables $x_1, \dots, x_r$ such that for every $j \in \mathbb{Z}^r$ the coefficients of $x^j$ in
$\tilde P(x_1, \dots, x_r)^p$ and in $\tilde P(x_1^p, \dots, x_r^p)$ are congruent modulo $p^a$.
Suppose $\deg \tilde P \le m + 1$, where $\deg \tilde P$ is the largest absolute value of an
exponent of a single variable in a monomial occurring in $\tilde P$ (and $0$ if $\tilde P = 0$),
and let $T = \{-m, \dots, m\}^r$. Then there is $t_0 \in \mathbb{N}$ such that for every
$n \in \mathbb{N}$ for which $p$ does not divide the constant term of $\tilde P^n$, there is
$j < p^{t_0}$ such that for every $i \in T$ the coefficient of $x^{-i}$ in
$\tilde P^{p^{t_0} n + j}$ is congruent modulo $p^a$ to $1$ if $i = 0$ and to $0$ otherwise.

Equivalently, writing $\tilde V(n)$ for the vector of coefficients of $x^{-i}$ in $\tilde P^n$,
$i \in T$, reduced modulo $p^a$, some $\tilde V(p^{t_0} n + j)$ with $j < p^{t_0}$ equals
$\tilde V(0)$. This is the analogue modulo $p^a$ of Proposition 15.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 32 (`jis-2026-26.4.2-prop-32`).

Stated but not proved: `MetaMathlibExt.exists_sigma_pow_V_contains_V_zero_tilde` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#exists-sigma-pow-v-contains-v-zero-tilde).

## Linear recurrence of constant terms modulo $p^a$

Let $p$ be a prime, let $a \ge 1$, and
let $P, Q$ be Laurent polynomials with integer coefficients in $r$ variables; write
$\operatorname{ct}[f]$ for the constant term of $f$. Suppose $p^a \nmid \operatorname{ct}[P^n Q]$
for some $n \in \mathbb{N}$. Then the sequence $u_n = \operatorname{ct}[P^n Q] \bmod p^a$ is
linearly recurrent if and only if $p \nmid \operatorname{ct}[P^n]$ for all $n \in \mathbb{N}$, and
if $u$ is not linearly recurrent, then the set of $n$ with $p^a \mid \operatorname{ct}[P^n Q]$ has
natural density $1$.

In particular, as long as $u$ is not identically $0$, whether it is linearly recurrent does not
depend on $Q$ or $a$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Theorem 33 (`jis-2026-26.4.2-thm-33`).

Stated but not proved: `MetaMathlibExt.isLinearlyRecurrentSeq_constantTerm_mod_primePow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq-constant-term-2).

## Linear recurrence of combinations of constant terms modulo $p^a$

Let $p$ be a prime,
let $a \ge 1$, let $P, Q_1, \dots, Q_\ell$ be Laurent polynomials with integer coefficients in
$r$ variables, let $k_1, \dots, k_\ell \in \mathbb{N}$, and let
$F \colon (\mathbb{Z}/p^a\mathbb{Z})^\ell \to X$ be a map to a set $X$. Write
$\operatorname{ct}[f]$ for the constant term of $f$ and, for $n \in \mathbb{N}$, let
$b_n = F(\operatorname{ct}[P^{n+k_1} Q_1] \bmod p^a, \dots,
\operatorname{ct}[P^{n+k_\ell} Q_\ell] \bmod p^a)$. Suppose $b_n \ne F(0, \dots, 0)$ for some $n$.
Then $(b_n)$ is linearly recurrent if and only if $p \nmid \operatorname{ct}[P^n]$ for all
$n \in \mathbb{N}$, and if $p \mid \operatorname{ct}[P^n]$ for some $n$, then the set of $n$ with
$b_n = F(0, \dots, 0)$ has natural density $1$.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Corollary 34 (`jis-2026-26.4.2-cor-34`).

Stated but not proved: `MetaMathlibExt.isLinearlyRecurrentSeq_combination_mod_primePow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-linearly-recurrent-seq-combination-mo-2).

## Recurrence of constant-term sequences modulo a prime power

Let $p$ be a prime, let
$a \ge 1$, and let $P$ and $Q$ be Laurent polynomials in $r$ variables with integer coefficients;
write $\mathrm{ct}[F]$ for the constant term of a Laurent polynomial $F$. If
$p \nmid \mathrm{ct}[P^{n_0}]$ for some $n_0 > 0$, then the sequence of residues
$(\mathrm{ct}[P^n Q] \bmod p^a)_{n \ge 0}$ in $\mathbb{Z}/p^a\mathbb{Z}$ is recurrent.

## Sources

- Nadav Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, Journal of Integer Sequences 29 (2026), Article 26.4.2, Proposition 35 (`jis-2026-26.4.2-prop-35`).

Stated but not proved: `MetaMathlibExt.isRecurrentSeq_constantTerm_mod_primePow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConstantTermLinearRepresentationWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html#is-recurrent-seq-constant-term-mod-prime-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Constant terms of powers of Laurent polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/constant-terms-of-powers-of-laurent-polynomials)
