---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook176Wanted.ScottishBookProblem176Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook176Wanted.eidelheit176_refuted
statement: formalized
---

# Inverses as limits of polynomials in Banach algebras

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/inverses-as-limits-of-polynomials-in-banach-alge/index.html).

## Scottish Book Problem 176 (Eidelheit's claim)

The claim that in every complete normed
ring $A$ (so $\|xy\| \le \|x\| \, \|y\|$, and $A$ has a unit) that is a normed algebra over
$\mathbb{R}$, the inverse of every invertible element is a limit of real polynomials in that
element: whenever $a, b \in A$ satisfy $ab = 1$ and $ba = 1$, there is a sequence
$(p_n)_{n \ge 0}$ of real polynomials with $p_n(a) \to b$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook176Wanted.ScottishBookProblem176Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook176Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook176Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/inverses-as-limits-of-polynomials-in-banach-alge/index.html#scottish-book-problem176-claim).

## Eidelheit's Problem 176 has a negative answer

The claim of Scottish Book Problem 176 is
false: there are a complete normed ring $A$ that is a normed algebra over $\mathbb{R}$ and
elements $a, b \in A$ with $ab = 1$ and $ba = 1$ such that $b$ is not the limit of any sequence
$(p_n(a))_{n \ge 0}$ with $p_n$ real polynomials.

The counterexample recorded in the typescript is the ring of linear operations on the space
$C[0, 1]$, with $a$ the operation $U$ given by $U(x)(t) = x(t^2)$ for $0 \le t \le 1$.

## Sources

- M. Eidelheit, Problem 176 of the Scottish Book, with the negative answer recorded in Ad 176 of the typescript (November 11, 1938). See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook176Wanted.eidelheit176_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook176Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook176Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/inverses-as-limits-of-polynomials-in-banach-alge/index.html#eidelheit176-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inverses as limits of polynomials in Banach algebras](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/inverses-as-limits-of-polynomials-in-banach-alge/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras/inverses-as-limits-of-polynomials-in-banach-alge)
