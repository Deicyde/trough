---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.finRank, MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.charPolyCoeff, MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.charPolyAbsCoeff, MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.characteristicPolynomialLogConcave, MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.characteristicPolynomialLogConcave_holds
statement: formalized
---

# Heron–Rota–Welsh conjecture

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html).

## Rank of a set in a matroid, as a natural number

For a matroid $M$ and a set $X$, this is
the rank $r(X)$ of $X$ in $M$, the size of a largest independent set of $M$ contained in $X$,
taken as a natural number; it is $0$ when this rank is infinite.

Formalized by `MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.finRank`, a definition declared in [WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html#fin-rank).

## Coefficients of the characteristic polynomial of a matroid

Let $M$ be a finite matroid on
the ground set $E$ with rank function $r$, and let
$\chi_M(\lambda) = \sum_{I \subseteq E} (-1)^{|I|} \lambda^{r(E) - r(I)}$ be its characteristic
polynomial. For a natural number $j$, this is the integer coefficient of $\lambda^j$ in
$\chi_M$, that is, the sum of $(-1)^{|I|}$ over the subsets $I \subseteq E$ with
$r(E) - r(I) = j$.

Formalized by `MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.charPolyCoeff`, a definition declared in [WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html#char-poly-coeff).

## Absolute coefficients of the characteristic polynomial of a matroid

Let $M$ be a finite
matroid on the ground set $E$ with rank function $r$ and characteristic polynomial
$\chi_M(\lambda) = \sum_{I \subseteq E} (-1)^{|I|} \lambda^{r(E) - r(I)}$. For a natural number
$k$, $w_k(M)$ is the absolute value of the coefficient of $\lambda^{r(E) - k}$ in $\chi_M$ when
$k \le r(E)$, and $w_k(M) = 0$ when $k > r(E)$.

Formalized by `MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.charPolyAbsCoeff`, a definition declared in [WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html#char-poly-abs-coeff).

## Log-concavity of the characteristic polynomial of a matroid, statement

For every finite
matroid $M$ on a ground set $E$ with rank function $r$, let $w_k(M)$ be the absolute value of the
coefficient of $\lambda^{r(E) - k}$ in the characteristic polynomial
$\chi_M(\lambda) = \sum_{I \subseteq E} (-1)^{|I|} \lambda^{r(E) - r(I)}$ when $k \le r(E)$, and
$w_k(M) = 0$ when $k > r(E)$. Then $w_{k-1}(M) \, w_{k+1}(M) \le w_k(M)^2$ for every natural
number $k \ge 1$.

This is part (a) of Stanley's Problem 25 (Read–Hoggar–Rota–Heron–Welsh).

Formalized by `MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.characteristicPolynomialLogConcave`, a definition declared in [WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html#characteristic-polynomial-log-concave).

## Adiprasito–Huh–Katz theorem (Heron–Rota–Welsh conjecture)

For every finite matroid $M$
on a ground set $E$ with rank function $r$, let $w_k(M)$ be the absolute value of the coefficient
of $\lambda^{r(E) - k}$ in the characteristic polynomial
$\chi_M(\lambda) = \sum_{I \subseteq E} (-1)^{|I|} \lambda^{r(E) - r(I)}$ when $k \le r(E)$, and
$w_k(M) = 0$ when $k > r(E)$. Then $w_{k-1}(M) \, w_{k+1}(M) \le w_k(M)^2$ for every natural
number $k \ge 1$.

Huh had proved the case of graphs and realizable matroids in characteristic $0$.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 25 (Read–Hoggar–Welsh–Mason conjectures); resolution: K. Adiprasito, J. Huh and E. Katz, Hodge theory for combinatorial geometries, Ann. of Math. 188 (2018), 381-452, arXiv:1511.02888; J. Huh, Milnor numbers of projective hypersurfaces and the chromatic polynomial of graphs, J. Amer. Math. Soc. 25 (2012), 907-927 (graphs), Theorem 9.9(2) (arXiv numbering): for every matroid M the coefficients of the characteristic polynomial form a log-concave sequence; §1, Conjecture 1.1 defines χ_M and w_k as above, https://arxiv.org/abs/1511.02888.

Stated but not proved: `MathlibExt.Combinatorics.MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.characteristicPolynomialLogConcave_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MatroidCharacteristicPolynomialLogConcaveAMR156Problem0026Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html#characteristic-polynomial-log-concave-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heron–Rota–Welsh conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/matroid-theory/heron-rota-welsh-conjecture)
