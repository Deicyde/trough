---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook27Wanted.IsPolynomialOn, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook27Wanted.bezout_identity_for_polynomials_without_common_zero, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook55Wanted.ScottishBookProblem55Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook55Wanted.mazur55_refuted, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook75Wanted.ScottishBookProblem75Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook75Wanted.mazur75_refuted
statement: formalized
---

# Polynomials on Banach spaces

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html).

## Continuous polynomial functions on a complex normed space

Let $E$ be a complex normed
space. A function $F : E \to \mathbb{C}$ is a continuous polynomial function if there are a
natural number $n$, natural numbers $m_1, \dots, m_n$ and continuous $\mathbb{C}$-multilinear
maps $A_i : E^{m_i} \to \mathbb{C}$, with $A_i$ taking $m_i$ arguments, such that
$F(x) = \sum_{i=1}^{n} A_i(x, \dots, x)$ for every $x \in E$.

A $0$-multilinear map is a constant, so constant functions are polynomial functions.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook27Wanted.IsPolynomialOn`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook27Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook27Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#is-polynomial-on).

## Bezout identity for polynomials without a common zero

Let $E$ be a complex Banach space
and let $F, G : E \to \mathbb{C}$ be continuous polynomial functions with no common zero, that
is, $G(x) \neq 0$ whenever $F(x) = 0$. Then there are continuous polynomial functions
$\varphi, \psi : E \to \mathbb{C}$ such that $F(x) \varphi(x) + G(x) \psi(x) = 1$ for every
$x \in E$.

This is the identity recorded in the addendum to Problem 27 of the Scottish Book (Mazur-Orlicz,
4 April 1939). The problem asks whether two complex polynomials on a complex Banach space that
both tend to $0$ along a sequence $(x_n)$ in the unit ball must have a common zero. The answer
is positive and follows from the identity by contradiction: continuous polynomials are bounded
on the unit ball, so $F(x_n) \varphi(x_n) + G(x_n) \psi(x_n)$ would tend to $0$, yet it equals
$1$.

## Sources

- S. Mazur and W. Orlicz, Problem 27 of the Scottish Book, with the positive answer via the Bezout identity in the addendum; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook27Wanted.bezout_identity_for_polynomials_without_common_zero` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook27Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook27Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#bezout-identity-for-polynomials-without).

## Mazur's factorisation claim (Scottish Book Problem 55)

The claim that for every real
Banach space $E$, every unbounded set $R \subseteq E$ and every continuous bilinear form
$B : E \times E \to \mathbb{R}$, if the quadratic form $W(x) = B(x, x)$ is bounded on the set
of points at distance less than $\varepsilon$ from $R$ for some $\varepsilon > 0$, then there
are a continuous linear functional $L : E \to \mathbb{R}$, a constant $c \in \mathbb{R}$ and a
real polynomial $V$ such that $W(x) = V(L(x) + c)$ for all $x \in E$ and $|L(r) + c|$ is
bounded for $r \in R$.

This is Mazur's question in the general Banach-space form for scalar-valued 2-polynomials: $W$
factors as $V \circ \varphi$ through the first-degree polynomial $\varphi(x) = L(x) + c$, which
maps $R$ to a bounded set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook55Wanted.ScottishBookProblem55Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook55Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook55Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#scottish-book-problem55-claim).

## Mazur's Problem 55 has a negative answer

The factorisation claim of Scottish Book
Problem 55 is false: there are a real Banach space $E$, an unbounded set $R \subseteq E$ and a
continuous bilinear form $B : E \times E \to \mathbb{R}$ such that for some $\varepsilon > 0$
the quadratic form $W(x) = B(x, x)$ is bounded on the set of points at distance less than
$\varepsilon$ from $R$, yet there are no continuous linear functional $L : E \to \mathbb{R}$,
constant $c \in \mathbb{R}$ and real polynomial $V$ with $W(x) = V(L(x) + c)$ for all $x \in E$
and $|L(r) + c|$ bounded for $r \in R$.

## Sources

- S. Mazur, Problem 55 of the Scottish Book; refuted by V. Pestov, who constructs a continuous scalar-valued 2-polynomial `W` on the separable Hilbert space `ℓ²` and an unbounded set `R` such that `W` is bounded on an `ε`-neighbourhood of `R` but does not factor through any bounded first-degree polynomial sending `R` to a bounded set ("Two 1935 questions of Mazur about polynomials in Banach spaces: a counter-example", 1997, arXiv:funct-an/9705002). The same counterexample refutes Problem 75. In finite dimensions the answer is positive (Auerbach), so the infinite-dimensional Banach setting is essential.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook55Wanted.mazur55_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook55Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook55Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#mazur55-refuted).

## Scottish Book Problem 75 (Mazur), general Banach-space form

The claim that for every real
Banach space $E$, every set $R \subseteq E$, every continuous bilinear form $B$ on $E$ and every
real $\alpha \ne 0$ the following holds: if for some $\varepsilon > 0$ the values $|B(x, x)|$ are
bounded on the open $\varepsilon$-neighbourhood of $R$, that is, for the $x \in E$ with
$\operatorname{dist}(x, r) < \varepsilon$ for some $r \in R$, then for some $\delta > 0$ the values
$|B(x, x)|$ are bounded on the open $\delta$-neighbourhood of the scaled set
$\alpha R = \{\alpha r : r \in R\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook75Wanted.ScottishBookProblem75Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook75Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook75Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#scottish-book-problem75-claim).

## Mazur's Scottish Book Problem 75 fails in general Banach spaces

The Scottish Book Problem 75
claim is false: there are a real Banach space $E$, a set $R \subseteq E$, a continuous bilinear
form $B$ on $E$ and a real $\alpha \ne 0$ such that $|B(x, x)|$ is bounded on some open
$\varepsilon$-neighbourhood of $R$ with $\varepsilon > 0$, but is unbounded on every open
$\delta$-neighbourhood of $\alpha R = \{\alpha r : r \in R\}$ with $\delta > 0$.

## Sources

- S. Mazur, Problem 75 of the Scottish Book; refuted by V. Pestov, whose counterexample to Problem 55 is a continuous scalar-valued 2-polynomial `W` on `ℓ²`, bounded on an `ε`-neighbourhood of an unbounded set `R`, but unbounded on `(1 / 2) R`, hence unbounded on every neighbourhood of `(1 / 2) R` ("Two 1935 questions of Mazur about polynomials in Banach spaces: a counter-example", 1997, arXiv:funct-an/9705002). Plichko and Zagorodnyuk gave an independent negative solution ("On automatic continuity and three problems of 'The Scottish Book' concerning the boundedness of polynomial functionals", J. Math. Anal. Appl. 220 (1998), 477–494). In the Euclidean case the statement is true, per typescript Ad 75.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook75Wanted.mazur75_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook75Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook75Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html#mazur75-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomials on Banach spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/polynomials-on-banach-spaces)
