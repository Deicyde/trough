---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.qInt, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.IsValid, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.degrees, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.coxeterNumber, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.coxeterFussCatalanPositive, MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.coxeterFussCatalanPositive_holds
statement: formalized
---

# q-Fuss–Catalan numbers of Coxeter groups

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html).

## Coxeter groups and q-integers

## q-integers

For a natural number $a$, the $q$-integer is the integer polynomial
$[a]_q = 1 + q + \dots + q^{a-1} = \sum_{i=0}^{a-1} q^i$; in particular $[0]_q = 0$.

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.qInt`, a definition declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#q-int).

## Types of irreducible finite Coxeter groups

The labels $A_n$, $B_n$, $D_n$ and $I_2(m)$
for natural numbers $n$ and $m$, together with $E_6$, $E_7$, $E_8$, $F_4$, $H_3$ and $H_4$. Every
natural number parameter is allowed here; the classification of irreducible finite Coxeter groups
uses $A_n$ ($n \ge 1$), $B_n$ ($n \ge 2$), $D_n$ ($n \ge 4$), the six exceptional labels and the
dihedral types $I_2(m)$ ($m \ge 3$).

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType`, an inductive type declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#coxeter-type).

## Valid Coxeter types

A Coxeter type is valid when it lies in the parameter range of the
classification of irreducible finite Coxeter groups: $A_n$ is valid when $n \ge 1$, $B_n$ when
$n \ge 2$, $D_n$ when $n \ge 4$ and $I_2(m)$ when $m \ge 3$, while $E_6$, $E_7$, $E_8$, $F_4$,
$H_3$ and $H_4$ are always valid.

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.IsValid`, a definition declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#is-valid).

## Degrees of the irreducible finite Coxeter groups

The list of degrees $d_1, \dots, d_r$ of
the basic invariants of a Coxeter type (so $d_i = e_i + 1$ for the exponents $e_i$) is:
$2, 3, \dots, n + 1$ for $A_n$; $2, 4, \dots, 2n$ for $B_n$; $n, 2, 4, \dots, 2n - 2$ for $D_n$;
$2, 5, 6, 8, 9, 12$ for $E_6$; $2, 6, 8, 10, 12, 14, 18$ for $E_7$;
$2, 8, 12, 14, 18, 20, 24, 30$ for $E_8$; $2, 6, 8, 12$ for $F_4$; $2, 6, 10$ for $H_3$;
$2, 12, 20, 30$ for $H_4$; and $2, m$ for $I_2(m)$.

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.degrees`, a definition declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#degrees).

## Coxeter number

The Coxeter number $h$ of a Coxeter type is the largest of its degrees,
and $0$ if its list of degrees is empty.

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.CoxeterType.coxeterNumber`, a definition declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#coxeter-number).

## AIM Problem 2.1: positivity of q-Fuss-Catalan numbers

The claim that for every type $T$
among $A_n$ ($n \ge 1$), $B_n$ ($n \ge 2$), $D_n$ ($n \ge 4$), $E_6$, $E_7$, $E_8$, $F_4$, $H_3$,
$H_4$ and $I_2(m)$ ($m \ge 3$) of irreducible finite Coxeter groups, with degrees
$d_1, \dots, d_r$ and Coxeter number $h$ (the largest degree), and every integer $k \ge 1$, there
is a polynomial $P(q)$ with nonnegative integer coefficients such that
$P(q) \prod_i [d_i]_q = \prod_i [kh + d_i]_q$, where $[a]_q = 1 + q + \dots + q^{a-1}$ is the
$q$-integer. Equivalently, $\prod_i [kh + d_i]_q / [d_i]_q$ is a polynomial in $q$ with
nonnegative integer coefficients.

Formalized by `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.coxeterFussCatalanPositive`, a definition declared in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#coxeter-fuss-catalan-positive).

## Positivity of q-Fuss-Catalan numbers of Coxeter groups

Let $T$ be one of the types $A_n$
($n \ge 1$), $B_n$ ($n \ge 2$), $D_n$ ($n \ge 4$), $E_6$, $E_7$, $E_8$, $F_4$, $H_3$, $H_4$ or
$I_2(m)$ ($m \ge 3$) of irreducible finite Coxeter groups, with degrees $d_1, \dots, d_r$ and
Coxeter number $h$ (the largest degree), and let $k \ge 1$ be an integer. With the $q$-integers
$[a]_q = 1 + q + \dots + q^{a-1}$, there is a polynomial $P(q)$ with nonnegative integer
coefficients such that $P(q) \prod_i [d_i]_q = \prod_i [kh + d_i]_q$; that is, the quotient
$\prod_i [kh + d_i]_q / [d_i]_q$ is a polynomial in $q$ with nonnegative integer coefficients.

Gordon and Griffeth proved this for every irreducible finite Coxeter group (a well-generated real
reflection group, for which their Hecke algebra hypothesis holds).

## Sources

- AIM workshop Braid groups, clusters and free probability (January 2005), outline by D. Armstrong, Problem 2.1 (C. Athanasiadis), https://aimath.org/WWN/braidgroups/braidgroups.pdf; resolution: I. Gordon and S. Griffeth, Catalan numbers for complex reflection groups, Amer. J. Math. 134 (2012), no. 6, 1491-1502, arXiv:0912.1578, Theorem in §1.6: the q-Fuss-Catalan number C_W^{(m)}(q) lies in ℕ[q] for every irreducible complex reflection group W under Hypothesis 2.4 (freeness of the Hecke algebra, which the paper notes is known for all real W); §1.9: for well-generated W, in particular every irreducible finite Coxeter group, C_W^{(m)}(q) = ∏ [mh + d_i]_q / [d_i]_q, https://doi.org/10.1353/ajm.2012.0047.

Stated but not proved: `MathlibExt.Combinatorics.CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.coxeterFussCatalanPositive_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CoxeterFussCatalanPositivityAIMProbabilityProblem148Wanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html#coxeter-fuss-catalan-positive-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: q-Fuss–Catalan numbers of Coxeter groups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/q-fuss-catalan-numbers-of-coxeter-groups)
