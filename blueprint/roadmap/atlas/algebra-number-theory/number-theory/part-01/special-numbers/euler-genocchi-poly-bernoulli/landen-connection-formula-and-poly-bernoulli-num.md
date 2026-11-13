---
declaration: section
origin: cited
lean: MetaMathlibExt.linearFractionalPoleSeries, MetaMathlibExt.linearFractionalPoleSeries_spec, MetaMathlibExt.landenFormSeries, MetaMathlibExt.landenFormSeries_identity, MetaMathlibExt.integralDivX, MetaMathlibExt.integralDivX_spec, MetaMathlibExt.LandenData, MetaMathlibExt.LandenData.tilde
statement: formalized
---

# Landen connection formula and poly-Bernoulli numbers

37 results, 29 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html).

## Pole series and Landen data

## Linear fractional pole series

For real numbers $a$ and $c$, this is the power series
$F_{a,c}(u)$ of $\frac{cu}{a - cu}$: it is $\sum_{n \ge 1} (c/a)^n u^n$ if $a \neq 0$, the
constant $-1$ if $a = 0$ and $c \neq 0$, and $0$ (a junk value) if $a = c = 0$. It is $u$
times the summand $\frac{c}{a - cu}$ of $G_g(u) = \frac{c}{a - cu} - \frac{d}{b - du}$ for
the matrix $g$ with rows $(a, b)$ and $(c, d)$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, the function `G_g(t)` before Table 1.

Formalized by `MetaMathlibExt.linearFractionalPoleSeries`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#linear-fractional-pole-series).

## The linear fractional pole series solves its defining equation

For all real numbers
$a$ and $c$, the linear fractional pole series $F_{a,c}(u)$, the power series of
$\frac{cu}{a - cu}$, satisfies $(a - cu) \cdot F_{a,c}(u) = cu$ in $\mathbb{R}[[u]]$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, the function `G_g(t)` before Table 1.

Formalized by `MetaMathlibExt.linearFractionalPoleSeries_spec`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#linear-fractional-pole-series-spec).

## Landen form series

For real numbers $a, b, c, d$, viewed as the matrix $g$ with rows
$(a, b)$ and $(c, d)$, this is the power series
$u \cdot G_g(u) = \frac{cu}{a - cu} - \frac{du}{b - du} \in \mathbb{R}[[u]]$, where
$G_g(t) = \frac{c}{a - ct} - \frac{d}{b - dt}$. Here the power series of $\frac{cu}{a - cu}$ is
$\sum_{n \ge 1} (c/a)^n u^n$ if $a \neq 0$, the constant $-1$ if $a = 0$ and $c \neq 0$, and
$0$ if $a = c = 0$; likewise for $\frac{du}{b - du}$ with $b, d$ in place of $a, c$. For
$g \in GL_2(\mathbb{R})$ the last case does not occur.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, the function `G_g(t)` before Table 1.

Formalized by `MetaMathlibExt.landenFormSeries`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#landen-form-series).

## Landen form series of the identity matrix

For the identity matrix $g$, with rows $(1, 0)$
and $(0, 1)$, the Landen form series $u \cdot G_g(u)$ is the constant power series $1$ in
$\mathbb{R}[[u]]$; that is, $G_g(t) = 1/t$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Table 1.

Formalized by `MetaMathlibExt.landenFormSeries_identity`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#landen-form-series-identity).

## Formal integral against $du/u$

For a real power series $h$, this is the power series
$\int_0^z h(u)\,du/u$ computed coefficientwise: for $n \ge 1$ its coefficient of $z^n$ is the
coefficient of $u^n$ in $h$ divided by $n$, and its constant coefficient is $0$. The constant
coefficient of $h$ is ignored, so this is the termwise integral only when $h$ has zero constant
term.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, the integrals defining `Li_k(g; (β, γ); z)`.

Formalized by `MetaMathlibExt.integralDivX`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#integral-div-x).

## The formal integral against $du/u$ is a right inverse of $z \, d/dz$

Let
$h \in \mathbb{R}[[z]]$ be a power series with zero constant term, and let
$I(h) = \sum_{n \ge 1} \frac{[z^n] h}{n} z^n$ be its formal integral $\int_0^z h(u) \, du / u$,
where $[z^n] h$ is the coefficient of $z^n$ in $h$. Then $I(h)$ has zero constant term and
$z \, \frac{d}{dz} I(h) = h$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, the integrals defining `Li_k(g; (β, γ); z)`.

Formalized by `MetaMathlibExt.integralDivX_spec`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#integral-div-x-spec).

## Landen data

Landen data $g = (g_0, g_1, \dots, g_s)$ consist of a natural number $s$,
real numbers $c_0, d_0$, and real numbers $a_i, b_i, c_i, d_i$ for $1 \le i \le s$. They
encode the real $2 \times 2$ matrix $g_0$ with rows $(1, -1)$ and $(c_0, d_0)$ and, for
$1 \le i \le s$, the matrix $g_i$ with rows $(a_i, b_i)$ and $(c_i, d_i)$. No invertibility is
required.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2.

Formalized by `MetaMathlibExt.LandenData`, a structure declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#landen-data).

## Transformed Landen data

For Landen data $g = (g_0, g_1, \dots, g_s)$ with
$g_0 = \begin{pmatrix} 1 & -1 \\ c_0 & d_0 \end{pmatrix}$ and
$g_i = \begin{pmatrix} a_i & b_i \\ c_i & d_i \end{pmatrix}$ for $1 \le i \le s$, the transformed
data $\tilde g = (\tilde g_0, \tilde g_1, \dots, \tilde g_s)$ has the same $s$, with
$\tilde g_0 = \begin{pmatrix} 1 & -1 \\ -d_0 & -c_0 \end{pmatrix}$ and, for $1 \le i \le s$, the
matrix $\tilde g_i$ has first row $(a_i, b_i)$ and second row
$((c_0 - d_0) a_i - c_i, (c_0 - d_0) b_i - d_i)$. Equivalently,
$\tilde g_i = \begin{pmatrix} 1 & 0 \\ c_0 - d_0 & -1 \end{pmatrix} g_i$ for $0 \le i \le s$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, display before Theorem 2.

Formalized by `MetaMathlibExt.LandenData.tilde`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#tilde).

## The transformation of Landen data is an involution

For Landen data
$g = (g_0, g_1, \dots, g_s)$ with $g_0 = \begin{pmatrix} 1 & -1 \\ c_0 & d_0 \end{pmatrix}$, let
$\tilde g$ be the transformed data, given by
$\tilde g_i = \begin{pmatrix} 1 & 0 \\ c_0 - d_0 & -1 \end{pmatrix} g_i$ for $0 \le i \le s$.
Then the transformed data of $\tilde g$ is $g$ itself: $\tilde{\tilde g} = g$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, remark before Theorem 2.

Formalized by `MetaMathlibExt.LandenData.tilde_tilde`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#tilde-tilde).

## Weighted form series

Let $g = (g_0, g_1, \dots, g_s)$ be Landen data, where $g_i$ has
rows $(a_i, b_i)$ and $(c_i, d_i)$ for $1 \le i \le s$, and let $w_1, \dots, w_s$ be real
numbers. The weighted form series of $g$ with weights $w$ is the formal power series
$u \sum_{i=1}^{s} w_i G_{g_i}(u) \in \mathbb{R}[[u]]$, where $u\,G_{g_i}(u)$ is the Landen form
series of $g_i$: the expansion of $\frac{c_i u}{a_i - c_i u} - \frac{d_i u}{b_i - d_i u}$, a
fraction with zero numerator and zero denominator being read as $0$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, definition of `Li_k(g; (β, γ); z)`.

Formalized by `MetaMathlibExt.LandenData.formSeries`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#form-series).

## Reversed recursion for Kamano's generalized multiple polylogarithm

Fix Landen data $g$,
with $g_0 = \begin{pmatrix} 1 & -1 \\ c_0 & d_0 \end{pmatrix}$ and
$g_i = \begin{pmatrix} a_i & b_i \\ c_i & d_i \end{pmatrix}$ for $1 \le i \le s$, and weights
$\beta, \gamma \in \mathbb{R}^s$. For a real matrix
$h = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ let $z\,G_h(z) \in \mathbb{R}[[z]]$ be the
power series of $\frac{cz}{a - cz} - \frac{dz}{b - dz}$, where a term whose numerator and
denominator are both $0$ is read as $0$; for $w \in \mathbb{R}^s$ let
$\Phi_w = \sum_{i=1}^s w_i \, z\,G_{g_i}(z) \in \mathbb{R}[[z]]$; and for
$f = \sum_n f_n z^n \in \mathbb{R}[[z]]$ let $I(f) = \sum_{n \ge 1} (f_n / n) z^n$, which is the
formal integral $\int_0^z f(u) \, du / u$ when $f_0 = 0$. For a finite list $\ell$ of natural
numbers, the series $L(\ell) \in \mathbb{R}[[z]]$ is defined recursively: $L(\ell) = 0$ if $\ell$
is empty or its first entry is $0$; $L((1)) = I(z\,G_{g_0}(z))$;
$L((1, r, \ell')) = I(\Phi_\gamma \cdot L((r, \ell')))$ for every natural number $r$ and list
$\ell'$; and $L((n + 2, \ell')) = I(\Phi_\beta \cdot L((n + 1, \ell')))$ for every natural
number $n$ and list $\ell'$.

Applied to the reversed list $(k_r, \dots, k_1)$ of an index $k = (k_1, \dots, k_r)$, $L$ gives
Kamano's generalized multiple polylogarithm $\mathrm{Li}_k(g; (\beta, \gamma); z)$. A list with a
zero entry anywhere gives $0$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, display (6) and the two inductive integrals before it.

Formalized by `MetaMathlibExt.LandenData.polylogRev`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#polylog-rev).

## Kamano's generalized multiple polylogarithm

Let $g = (g_0, g_1, \dots, g_s)$ be Landen
data, where $g_0$ has rows $(1, -1)$ and $(c_0, d_0)$ and $g_i$ has rows $(a_i, b_i)$ and
$(c_i, d_i)$, and let $\beta, \gamma \in \mathbb{R}^s$. For a matrix $h$ with rows $(a, b)$ and
$(c, d)$ put $G_h(u) = \frac{c}{a - c u} - \frac{d}{b - d u}$, a fraction with zero numerator and
zero denominator being read as $0$. For an index $\mathbf{k} = (k_1, \dots, k_r)$ of positive
integers put $\mathbf{k}{\uparrow} = (k_1, \dots, k_r + 1)$ and
$\mathbf{k}{\rightarrow} = (k_1, \dots, k_r, 1)$. The generalized multiple polylogarithm
$\mathrm{Li}_{\mathbf{k}} = \mathrm{Li}_{\mathbf{k}}(g; (\beta, \gamma); z) \in \mathbb{R}[[z]]$
is defined recursively by
$\mathrm{Li}_{(1)} = \int_0^z \left(\frac{c_0}{1 - c_0 u} + \frac{d_0}{1 + d_0 u}\right) du$,
$\mathrm{Li}_{\mathbf{k}{\uparrow}} =
\int_0^z \sum_{i=1}^{s} \beta_i G_{g_i}(u) \, \mathrm{Li}_{\mathbf{k}}(u)\,du$ and
$\mathrm{Li}_{\mathbf{k}{\rightarrow}} =
\int_0^z \sum_{i=1}^{s} \gamma_i G_{g_i}(u) \, \mathrm{Li}_{\mathbf{k}}(u)\,du$, where
integrals of power series are taken term by term. A list of natural numbers that is empty or has
a zero entry gives $0$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, display (6).

Formalized by `MetaMathlibExt.generalizedMultiplePolylog`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog).

## Initial value of the generalized multiple polylogarithm

Let
$g = (g_0, g_1, \dots, g_s)$ be Landen data, where $g_0$ has rows $(1, -1)$ and $(c_0, d_0)$,
and let $\beta, \gamma \in \mathbb{R}^s$. Then
$\mathrm{Li}_{(1)}(g; (\beta, \gamma); z) = \int_0^z G_{g_0}(u)\,du$, where
$u\,G_{g_0}(u) = \frac{c_0 u}{1 - c_0 u} + \frac{d_0 u}{1 + d_0 u}$ is the Landen form series of
$g_0$ and the integral of a power series is taken term by term.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, display (6).

Formalized by `MetaMathlibExt.generalizedMultiplePolylog_one`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-one).

## Recurrence for raising the last entry

Let $g = (g_0, g_1, \dots, g_s)$ be Landen data and
let $\beta, \gamma \in \mathbb{R}^s$. For every list $(k_1, \dots, k_{r-1})$ of natural numbers
(possibly empty) and every natural number $m$, writing $\mathbf{k} = (k_1, \dots, k_{r-1}, m + 1)$,
$\mathrm{Li}_{(k_1, \dots, k_{r-1}, m + 2)}(g; (\beta, \gamma); z) =
\int_0^z \sum_{i=1}^{s} \beta_i G_{g_i}(u) \, \mathrm{Li}_{\mathbf{k}}(g; (\beta, \gamma); u)\,du$,
where $u \sum_{i} \beta_i G_{g_i}(u)$ is the weighted form series of $g$ with weights $\beta$
and the integral of a power series is taken term by term.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2.

Formalized by `MetaMathlibExt.generalizedMultiplePolylog_up`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-up).

## Recurrence for appending the entry 1

Let $g = (g_0, g_1, \dots, g_s)$ be Landen data and
let $\beta, \gamma \in \mathbb{R}^s$. For every nonempty list $\mathbf{k} = (k_1, \dots, k_r)$ of
natural numbers,
$\mathrm{Li}_{(k_1, \dots, k_r, 1)}(g; (\beta, \gamma); z) =
\int_0^z \sum_{i=1}^{s} \gamma_i G_{g_i}(u) \, \mathrm{Li}_{\mathbf{k}}(g; (\beta, \gamma); u)\,du$,
where $u \sum_{i} \gamma_i G_{g_i}(u)$ is the weighted form series of $g$ with weights $\gamma$
and the integral of a power series is taken term by term.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2.

Formalized by `MetaMathlibExt.generalizedMultiplePolylog_right`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-right).

## Coefficient recursion for multiple polylogarithms

For a finite list $\ell$ of natural
numbers and $m \in \mathbb{N}$, the real number $c_\ell(m)$ is defined by recursion on $\ell$:
for the empty list, $c_{()}(m)$ is $1$ if $m = 0$ and $0$ otherwise; for the list $(a, \ell')$
with first entry $a$ followed by the list $\ell'$,
$c_{(a, \ell')}(m) = \big(\sum_{m' < m} c_{\ell'}(m')\big) / m^a$.

The multiple polylogarithm $\mathrm{Li}_{(k_1, \dots, k_r)}(z)$ is defined as the power series
whose coefficient of $z^m$ is $c_{(k_r, \dots, k_1)}(m)$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1, definition of `Li_k(z)`.

Formalized by `MetaMathlibExt.multiplePolylogCoeffRev`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multiple-polylog-coeff-rev).

## Multiple polylogarithm

For a finite sequence $k = (k_1, \dots, k_r)$ of natural numbers
with $r \ge 1$, the multiple polylogarithm is the formal power series

$$\mathrm{Li}_k(z) = \sum_{0 < m_1 < \cdots < m_r} \frac{z^{m_r}}{m_1^{k_1} \cdots m_r^{k_r}}$$

in $\mathbb{R}[[z]]$; for the empty sequence it is the constant series $1$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1.

Formalized by `MetaMathlibExt.multiplePolylog`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multiple-polylog).

## Depth-one multiple polylogarithm

For every natural number $a$ and every integer
$m \ge 1$, the coefficient of $z^m$ in the multiple polylogarithm $\mathrm{Li}_{(a)}(z)$ is
$1/m^a$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1.

Formalized by `MetaMathlibExt.coeff_multiplePolylog_singleton`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#coeff-multiple-polylog-singleton).

## Coefficient recursion for the non-strict multiple polylogarithm

For a finite list $\ell$
of natural numbers and $m \in \mathbb{N}$, the real number $c_\ell(m)$ is defined by recursion on
$\ell$: for the empty list, $c_\ell(m) = 1$ if $m = 0$ and $c_\ell(m) = 0$ otherwise; for a list
$\ell = (a, \ell')$ with first entry $a$ followed by the list $\ell'$,

$$c_{(a, \ell')}(m) = \frac{1}{m^a} \sum_{m' = 0}^{m} c_{\ell'}(m'),$$

where $0^0 = 1$ and $1/0 = 0$.

Applied to the reversed list $(k_r, \dots, k_1)$ of positive integers $k_1, \dots, k_r$ with
$r \ge 1$, it gives the coefficient of $z^m$ in
$\sum_{0 < m_1 \le \cdots \le m_r} z^{m_r} / (m_1^{k_1} \cdots m_r^{k_r})$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1, definition of `Li⋆_k(z)`.

Formalized by `MetaMathlibExt.multiplePolylogStarCoeffRev`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multiple-polylog-star-coeff-rev).

## Non-strict multiple polylogarithm

For an index $k = (k_1, \dots, k_r)$ of positive
integers with $r \ge 1$, the non-strict multiple polylogarithm is the formal power series

$$\mathrm{Li}^\star_k(z) = \sum_{0\lt m_1\le\cdots\le m_r} \frac{z^{m_r}}{m_1^{k_1} \cdots m_r^{k_r}}$$

in $\mathbb{R}[[z]]$.

The definition accepts every finite list $k$ of natural numbers: for $r \ge 1$ the coefficient
of $z^m$ is the sum of $1/(m_1^{k_1} \cdots m_r^{k_r})$ over $0 \le m_1 \le \cdots \le m_r = m$,
where $0^0 = 1$ and $1/0 = 0$ (so for an index the terms with some $m_i = 0$ vanish), and the
empty list gives the constant series $1$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1.

Formalized by `MetaMathlibExt.multiplePolylogStar`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multiple-polylog-star).

## Depth-one non-strict multiple polylogarithm

For all natural numbers $a$ and $m$, the
coefficient of $z^m$ in the non-strict multiple polylogarithm $\mathrm{Li}^{\star}_{(a)}(z)$ is
$1/m^a$, with the conventions $0^0 = 1$ and $1/0 = 0$. In particular
$\mathrm{Li}^{\star}_{(a)}(z) = \sum_{m \ge 1} z^m / m^a$ for $a \ge 1$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 1.

Formalized by `MetaMathlibExt.coeff_multiplePolylogStar_singleton`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#coeff-multiple-polylog-star-singleton).

## Hoffman dual on reversed lists

The auxiliary map $R$ on finite lists
$l = (l_1, \dots, l_m)$ of natural numbers is defined recursively by: $R(()) = ()$; $R(l) = ()$
if $l_1 = 0$; $R((1)) = (1)$; if $l_1 = 1$ and $m \ge 2$, then $R(l)$ is $R((l_2, \dots, l_m))$
with its first entry increased by $1$ (unchanged if that list is empty); and if $l_1 \ge 2$, then
$R(l) = (1, r_1, \dots, r_p)$ where $(r_1, \dots, r_p) = R((l_1 - 1, l_2, \dots, l_m))$.

Reading an index from its last entry, these are the rules $(1)^\vee = (1)$,
$(k\rightarrow)^\vee = (k^\vee)\uparrow$ and $(k\uparrow)^\vee = (k^\vee)\rightarrow$ of Hoffman's
dual index, where $k\uparrow$ increases the last entry of $k$ by $1$ and $k\rightarrow$ appends an
entry $1$: the Hoffman dual of an index $k$ is the reverse of $R$ applied to the reverse of $k$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2, definition of Hoffman's dual index.

Formalized by `MetaMathlibExt.hoffmanDualRev`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#hoffman-dual-rev).

## Hoffman dual index

For an index $k = (k_1, \dots, k_r)$ of positive integers write
$k\uparrow = (k_1, \dots, k_r + 1)$ and $k\rightarrow = (k_1, \dots, k_r, 1)$. The Hoffman dual
index $k^\vee$ is defined recursively by $(1)^\vee = (1)$, $(k\uparrow)^\vee = (k^\vee)\rightarrow$
and $(k\rightarrow)^\vee = (k^\vee)\uparrow$. On other finite lists of natural numbers, the empty
list is sent to the empty list and a list with an entry $0$ is sent to an unspecified junk value.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2.

Formalized by `MetaMathlibExt.hoffmanDual`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#hoffman-dual).

## Small values of the Hoffman dual

The Hoffman dual index satisfies $(1)^\vee = (1)$,
$(3)^\vee = (1, 1, 1)$ and $(1, 2)^\vee = (2, 1)$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 2.

Formalized by `MetaMathlibExt.hoffmanDual_small_values`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#hoffman-dual-small-values).

## Landen exponential variable

For Landen data $g$ whose matrix $g_0$ has rows $(1, -1)$
and $(c_0, d_0)$, this is the formal power series $z(t) = (e^t - 1)(c_0 e^t + d_0)^{-1}$ in
$\mathbb{R}[[t]]$. The inverse is the power series inverse, which exists exactly when
$c_0 + d_0 \neq 0$; when $c_0 + d_0 = 0$ the inverse is taken to be $0$, so $z(t) = 0$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 4, definition of `C_n^{(k, g, (β, γ))}`.

Formalized by `MetaMathlibExt.landenExpVariable`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#landen-exp-variable).

## Defining relation of the Landen exponential variable

Let $g$ be Landen data whose
matrix $g_0$ has rows $(1, -1)$ and $(c_0, d_0)$ with $c_0 + d_0 \neq 0$, and let
$z(t) = (e^t - 1)(c_0 e^t + d_0)^{-1} \in \mathbb{R}[[t]]$ be its Landen exponential variable.
Then $(c_0 e^t + d_0)\, z(t) = e^t - 1$ in $\mathbb{R}[[t]]$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 4.

Formalized by `MetaMathlibExt.landenExpVariable_spec`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#landen-exp-variable-spec).

## Generalized poly-Bernoulli numbers of the first kind

Let $g = (g_0, g_1, \dots, g_s)$ be
Landen data, where $(c_0, d_0)$ is the bottom row of the matrix $g_0$, let
$\beta, \gamma \in \mathbb{R}^s$, and let $k = (k_1, \dots, k_r)$ be a list of natural numbers;
write $k\uparrow = (k_1, \dots, k_r + 1)$, with $k\uparrow = ()$ when $k$ is empty. Let
$z(t) \in \mathbb{R}[[t]]$ be the power series of $(e^t - 1)/(c_0 e^t + d_0)$ (the zero series
when $c_0 + d_0 = 0$). The numbers $C_n^{(k, g, (\beta, \gamma))} \in \mathbb{R}$, $n \ge 0$, are
defined by

$$\frac{d}{dt} \mathrm{Li}_{k\uparrow}(g; (\beta, \gamma); z(t)) =
\sum_{n \ge 0} C_n^{(k, g, (\beta, \gamma))} \frac{t^n}{n!},$$

where $\mathrm{Li}_{k\uparrow}(g; (\beta, \gamma); z)$ is Kamano's generalized multiple
polylogarithm, into which the series $z(t)$ is substituted.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 4.

Formalized by `MetaMathlibExt.generalizedPolyBernoulliC`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-c).

## Generalized poly-Bernoulli numbers of the second kind

Let $g = (g_0, g_1, \dots, g_s)$ be
Landen data, where $(c_0, d_0)$ is the bottom row of the matrix $g_0$, let
$\beta, \gamma \in \mathbb{R}^s$, and let $k = (k_1, \dots, k_r)$ be a list of natural numbers;
write $k\rightarrow = (k_1, \dots, k_r, 1)$, with $k\rightarrow = (1)$ when $k$ is empty. Let
$z(t) \in \mathbb{R}[[t]]$ be the power series of $(e^t - 1)/(c_0 e^t + d_0)$ (the zero series
when $c_0 + d_0 = 0$). The numbers $B_n^{(k, g, (\beta, \gamma))} \in \mathbb{R}$, $n \ge 0$, are
defined by

$$\frac{d}{dt} \mathrm{Li}_{k\rightarrow}(g; (\beta, \gamma); z(t)) =
\sum_{n \ge 0} B_n^{(k, g, (\beta, \gamma))} \frac{t^n}{n!},$$

where $\mathrm{Li}_{k\rightarrow}(g; (\beta, \gamma); z)$ is Kamano's generalized multiple
polylogarithm, into which the series $z(t)$ is substituted.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 4.

Formalized by `MetaMathlibExt.generalizedPolyBernoulliB`, a definition declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-b).

## Generalized poly-Bernoulli numbers $C_n$ as Taylor coefficients

Let
$g = (g_0, g_1, \dots, g_s)$ be Landen data, where $(c_0, d_0)$ is the bottom row of the matrix
$g_0$, let $\beta, \gamma \in \mathbb{R}^s$, let $k = (k_1, \dots, k_r)$ be a list of natural
numbers, and write $k\uparrow = (k_1, \dots, k_r + 1)$, with $k\uparrow = ()$ when $k$ is empty.
Let $z(t) \in \mathbb{R}[[t]]$ be the power series of $(e^t - 1)/(c_0 e^t + d_0)$ (the zero
series when $c_0 + d_0 = 0$). Then for every $n \ge 0$ the generalized poly-Bernoulli number of
the first kind satisfies

$$C_n^{(k, g, (\beta, \gamma))} =
(n + 1)! \, [t^{n+1}] \, \mathrm{Li}_{k\uparrow}(g; (\beta, \gamma); z(t)),$$

where $[t^m] F$ is the coefficient of $t^m$ in a power series $F$ and $\mathrm{Li}$ is Kamano's
generalized multiple polylogarithm.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Section 4.

Formalized by `MetaMathlibExt.generalizedPolyBernoulliC_eq_coeff`, a theorem declared in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-c-eq-coeff).

## Landen connection formula

**Landen connection formula** (Okuda–Ueno). Let $n \ge 0$ and let $k = (k_1, \dots, k_r)$ be
an index of weight $n$, that is, a finite sequence of positive integers with sum $n$. Then the
multiple polylogarithms satisfy the identity

$$\mathrm{Li}_k\left(\frac{z}{z - 1}\right) = (-1)^r \sum_{k'} \mathrm{Li}_{k'}(z)$$

in $\mathbb{R}[[z]]$, where $\mathrm{Li}_k(z) \in \mathbb{R}[[z]]$ is the multiple polylogarithm,
$\frac{z}{z - 1}$ stands for the series $-\sum_{m \ge 1} z^m$ substituted into $\mathrm{Li}_k$, and
the sum runs over all indices $k'$ of weight $n$ from which $k$ is obtained by adding up blocks of
consecutive entries; equivalently, every partial sum $k_1 + \cdots + k_j$ of $k$ is also a partial
sum of $k'$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Theorem 1 (quoting Okuda and Ueno, Prop. 9).

Stated but not proved: `MetaMathlibExt.multiplePolylog_landen_connection` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multiple-polylog-landen-connection).

## Sum formula

Let $g = (g_0, g_1, \dots, g_s)$ be Landen data, let
$\beta, \gamma, \delta \in \mathbb{R}^s$, let $\mu$ be a real number and let $k \ge 1$ be an
integer. Then
$\sum_{\mathbf{k}} \mu^{d(\mathbf{k}) - 1} \mathrm{Li}_{\mathbf{k}}(g; (\beta, \gamma); z) =
\mathrm{Li}_{(k)}(g; (\beta + \mu \gamma, \delta); z)$, where the sum runs over all compositions
$\mathbf{k} = (k_1, \dots, k_r)$ of $k$ (sequences of positive integers with
$k_1 + \dots + k_r = k$) and $d(\mathbf{k}) = r$ is the depth of $\mathbf{k}$.

The paper takes $\mu$ an indeterminate; both sides are polynomials in $\mu$, so this
is equivalent.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Proposition 1, Identity (7).

Stated but not proved: `MetaMathlibExt.generalizedMultiplePolylog_sum_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-sum-formula).

## Generalized Landen connection formula

Let $g = (g_0, g_1, \dots, g_s)$ be Landen data,
where $g_0$ has rows $(1, -1)$ and $(c_0, d_0)$ and each $g_i$ ($1 \le i \le s$) has rows
$(a_i, b_i)$ and $(c_i, d_i)$ with $a_i d_i - b_i c_i \ne 0$. Let $\tilde g$ be the transformed
data: $\tilde g_0$ has rows $(1, -1)$ and $(-d_0, -c_0)$, and $\tilde g_i = M g_i$, where $M$ is
the matrix with rows $(1, 0)$ and $(c_0 - d_0, -1)$. For all $\beta, \gamma \in \mathbb{R}^s$ and
every finite (possibly empty) sequence $\mathbf{k}$ of positive integers,
$\mathrm{Li}_{\mathbf{k}}(g; (\beta, \gamma); \frac{z}{(c_0 - d_0) z - 1}) =
\mathrm{Li}_{\mathbf{k}}(\tilde g; (\beta, \gamma); z)$ in $\mathbb{R}[[z]]$, where
$\frac{z}{(c_0 - d_0) z - 1} = -\sum_{n \ge 0} (c_0 - d_0)^n z^{n+1}$ is substituted for $z$.

The paper also assumes $g_0 \in \mathrm{GL}_2(\mathbb{R})$, that is $c_0 + d_0 \ne 0$; this is not
needed. The invertibility of the $g_i$ is needed: with $a_i = c_i = 0$ the identity fails.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Theorem 2, Identity (8).

Stated but not proved: `MetaMathlibExt.generalizedMultiplePolylog_landen_connection` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-landen-conn).

## Landen formula in the classical case

Let $g = (g_0, g_1, g_2)$ be the Landen data in
which $g_0 = g_2$ has rows $(1, -1)$ and $(1, 0)$ and $g_1$ is the identity matrix, so that
$G_{g_1}(t) = 1/t$ and $G_{g_2}(t) = 1/(1 - t)$. For all real numbers $\beta_1$, $\beta_2$,
$\gamma_1$, $\gamma_2$ and every finite (possibly empty) sequence $\mathbf{k}$ of positive
integers,
$\mathrm{Li}_{\mathbf{k}}(g; ((\beta_1, \beta_2), (\gamma_1, \gamma_2)); \frac{z}{z - 1}) =
-\mathrm{Li}_{\mathbf{k}}(g; ((\beta_1, \beta_1 - \beta_2), (\gamma_1, \gamma_1 - \gamma_2)); z)$
in $\mathbb{R}[[z]]$, where $\frac{z}{z - 1} = -\sum_{n \ge 1} z^n$ is substituted for $z$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Theorem 3, Identity (10).

Stated but not proved: `MetaMathlibExt.generalizedMultiplePolylog_landen_connection_classical` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-multiple-polylog-landen-conn-2).

## Duality of multi-poly-Bernoulli-star numbers

This duality is due to Imatomi. Let $k$
be an index (a composition of a natural number $m$), let $k^\vee$ be its Hoffman dual, and let
$\mathrm{Li}^\star_k$ be the non-strict multiple polylogarithm. Let $F, G \in \mathbb{R}[[t]]$
satisfy $(e^t - 1) F = \mathrm{Li}^\star_k(1 - e^{-t})$ and
$(1 - e^{-t}) G = \mathrm{Li}^\star_{k^\vee}(1 - e^{-t})$, and write
$F = \sum_{n \ge 0} C_{n,\star}^{(k)} t^n / n!$ and
$G = \sum_{n \ge 0} B_{n,\star}^{(k^\vee)} t^n / n!$. Then
$C_{n,\star}^{(k)} = (-1)^n B_{n,\star}^{(k^\vee)}$ for every $n \ge 0$.

Since $e^t - 1$ and $1 - e^{-t}$ are non-zero-divisors in $\mathbb{R}[[t]]$, these equations
determine $F$ and $G$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Theorem 4 (quoting Imatomi, Theorem 3.2), with generating functions (13) and (14).

Stated but not proved: `MetaMathlibExt.multiPolyBernoulliStar_duality` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#multi-poly-bernoulli-star-duality).

## Sum formula for generalized poly-Bernoulli numbers $C_n$

Let $g = (g_0, g_1, \dots, g_s)$
be Landen data, let $\beta, \gamma \in \mathbb{R}^s$, let $\mu$ be a real number, and let $k \ge 1$
and $n \ge 0$ be integers. Write $B_n$ and $C_n$ for Kamano's generalized poly-Bernoulli numbers of
the second and first kind, $d(\mathbf{k})$ for the number of entries of an index $\mathbf{k}$, and
$\{1\}^k = (1, \dots, 1)$ for the index of $k$ ones. Then

$$\sum_{|\mathbf{k}| = k} \mu^{d(\mathbf{k}) - 1} C_n^{(\mathbf{k}, g, (\beta, \gamma))} =
B_n^{((k), g, (\beta + \mu\gamma, \beta))} =
C_n^{(\{1\}^k, g, (\beta, \beta + \mu\gamma))},$$

where the sum runs over all compositions $\mathbf{k}$ of $k$, that is, all tuples of positive
integers with sum $k$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Proposition 2, Identity (16).

Stated but not proved: `MetaMathlibExt.generalizedPolyBernoulliC_sum_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-c-sum-formula).

## Sum formula for generalized poly-Bernoulli numbers $B_n$

Let $g = (g_0, g_1, \dots, g_s)$
be Landen data, let $\beta, \gamma \in \mathbb{R}^s$, let $\mu$ be a real number, and let $k \ge 1$
and $n \ge 0$ be integers. Write $B_n$ and $C_n$ for Kamano's generalized poly-Bernoulli numbers of
the second and first kind, $d(\mathbf{k})$ for the number of entries of an index $\mathbf{k}$, and
$\{1\}^k = (1, \dots, 1)$ for the index of $k$ ones. Then

$$\sum_{|\mathbf{k}| = k} \mu^{d(\mathbf{k}) - 1} B_n^{(\mathbf{k}, g, (\beta, \gamma))} =
B_n^{((k), g, (\beta + \mu\gamma, \gamma))} =
C_n^{(\{1\}^k, g, (\gamma, \beta + \mu\gamma))},$$

where the sum runs over all compositions $\mathbf{k}$ of $k$, that is, all tuples of positive
integers with sum $k$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Proposition 2, Identity (17).

Stated but not proved: `MetaMathlibExt.generalizedPolyBernoulliB_sum_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-b-sum-formula).

## Landen formula for generalized poly-Bernoulli numbers $C_n$

Let
$g = (g_0, g_1, \dots, g_s)$ be Landen data whose matrices $g_1, \dots, g_s$ are invertible, where
$(c_0, d_0)$ is the bottom row of $g_0$. Let $\tilde g$ be the transformed data: $\tilde g_0$ has
rows $(1, -1)$ and $(-d_0, -c_0)$, and $\tilde g_i = h g_i$ for $1 \le i \le s$, where $h$ is the
matrix with rows $(1, 0)$ and $(c_0 - d_0, -1)$. Let $\beta, \gamma \in \mathbb{R}^s$, let $k$ be a
composition of a natural number $m$ (the empty index when $m = 0$), and write $k\uparrow$ for $k$
with its last entry increased by $1$ ($k\uparrow$ is empty when $k$ is). Let
$z(t) \in \mathbb{R}[[t]]$, the variable of $g$, be the power series of
$(e^t - 1)/(c_0 e^t + d_0)$ (the zero series when $c_0 + d_0 = 0$). Then for every $n \ge 0$,

$$C_n^{(k, g, (\beta, \gamma))} =
(-1)^{n+1} \, n! \, [t^n] \, \frac{d}{dt}
\mathrm{Li}_{k\uparrow}(\tilde g; (\beta, \gamma); z(t)),$$

where $C_n$ is the generalized poly-Bernoulli number of the first kind, $\mathrm{Li}$ is Kamano's
generalized multiple polylogarithm and $[t^n] F$ is the coefficient of $t^n$ in $F$. Here
$\tilde g$ is evaluated at the variable $z(t)$ of $g$, not at its own variable.

This is Theorem 5 in the reading its proof establishes: the proof differentiates
$\mathrm{Li}_{k\uparrow}(g; z(t)) = \mathrm{Li}_{k\uparrow}(\tilde g; z(-t))$. The paper's sign
$(-1)^{n-1}$ equals $(-1)^{n+1}$ for all $n \ge 0$.

As printed, with $C_n^{(k, \tilde g, (\beta, \gamma))}$ formed from the variable
$(e^t - 1)/(-d_0 e^t - c_0) = z(-t)$ of $\tilde g$, the theorem is false: then
$C_n^{(k, \tilde g, (\beta, \gamma))} = C_n^{(k, g, (\beta, \gamma))}$ for all $n$. For instance,
$s = 1$, $g_0$ with rows $(1, -1)$ and $(1, 0)$, $g_1$ the identity matrix, $\beta = \gamma = (1)$,
$k = (1)$ and $n = 0$ give
$C_0^{(k, g, (\beta, \gamma))} = C_0^{(k, \tilde g, (\beta, \gamma))} = 1$, while the printed
identity asks for $1 = -1$.

## Sources

- Ken Kamano, *A Generalization of the Landen Connection Formula and Generalized Poly-Bernoulli Numbers*, INTEGERS 24 (2024), Article A77, Theorem 5.

Stated but not proved: `MetaMathlibExt.generalizedPolyBernoulliC_landen` is written with `theorem_wanted` in [WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KamanoLandenPolyBernoulliWanted.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html#generalized-poly-bernoulli-c-landen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Landen connection formula and poly-Bernoulli numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/landen-connection-formula-and-poly-bernoulli-num)
