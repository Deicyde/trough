---
declaration: section
origin: cited
lean: MetaMathlibExt.mahlerSubst, MetaMathlibExt.IsKMahlerFunction, MetaMathlibExt.nishioka_algebraic_kMahler_is_rational
statement: formalized
---

# Mahler functions

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions/index.html).

## Mahler substitution

For a formal power series $F \in \mathbb{C}[[z]]$ and natural numbers
$k$ and $i$, let $m = k^i$; the power series $F(z^{k^i})$ is defined coefficientwise. When
$m \ge 1$, its coefficient of $z^n$ is the coefficient of $z^{n/m}$ in $F$ if $m$ divides $n$, and
$0$ otherwise; this is the substitution $z \mapsto z^m$ in $F$. When $m = 0$ (that is, $k = 0$ and
$i \ge 1$), it is the constant series equal to the constant term of $F$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL16/Bell/bell2.tex.

Formalized by `MetaMathlibExt.mahlerSubst`, a definition declared in [MathlibExt/NumberTheory/KMahlerFunction.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KMahlerFunction.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions/index.html#mahler-subst).

## $k$-Mahler functions

Let $k$ be a natural number. A formal power series
$F \in \mathbb{C}[[z]]$ is a $k$-Mahler function when $k \ge 2$ and there exist a natural number
$d$ and polynomials $a_0(z), \dots, a_d(z) \in \mathbb{C}[z]$ with $a_0 \ne 0$ and $a_d \ne 0$
such that the following identity holds in $\mathbb{C}[[z]]$:

$$\sum_{i=0}^{d} a_i(z)\, F\bigl(z^{k^i}\bigr) = 0.$$

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL16/Bell/bell2.tex.

Formalized by `MetaMathlibExt.IsKMahlerFunction`, a definition declared in [MathlibExt/NumberTheory/KMahlerFunction.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KMahlerFunction.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions/index.html#is-kmahler-function).

## Nishioka's theorem: algebraic Mahler functions are rational

Let $k$ be a natural number
and let $F \in \mathbb{C}[[z]]$ be a $k$-Mahler function. If $F$ is algebraic over
$\mathbb{C}[z]$, that is, $P(F) = 0$ for some nonzero polynomial $P$ with coefficients in
$\mathbb{C}[z]$, then $F$ is rational: there are polynomials $p, q \in \mathbb{C}[z]$ with $q \ne 0$
and $qF = p$ in $\mathbb{C}[[z]]$.

## Sources

- Jason P. Bell, Michael Coons, and Eric Rowland, "The Rational-Transcendental Dichotomy of Mahler Functions", Journal of Integer Sequences 16 (2013), Article 13.2.10, Nishioka corollary lines 238–241, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Bell/bell2.tex>. The corollary is attributed to Ku. Nishioka, "Mahler Functions and Transcendence", Lecture Notes in Mathematics 1294, Theorem 5.1.7.

Stated but not proved: `MetaMathlibExt.nishioka_algebraic_kMahler_is_rational` is written with `theorem_wanted` in [WantedExt/NumberTheory/NishiokaMahlerRationalityWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NishiokaMahlerRationalityWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions/index.html#nishioka-algebraic-k-mahler-is-rational).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mahler functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/mahler-functions)
