---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.orderPolynomial, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.IsEulerianFunction, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.IsPSolvable, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSplitsSolvable, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSeparatesPSolvable, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSplitsSolvable_holds, MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSeparatesPSolvable_holds
statement: formalized
---

# Eulerian polynomials of groups

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html).

## Order polynomial of a subgroup

For a subgroup $H$ of a group, the order polynomial of $H$
is $f(H) = \prod_p x_p^{v_p(|H|)}$ in the integer polynomial ring $\mathbb{Z}[x_0, x_1, \dots]$,
where $p$ runs over the primes, $x_p$ is the variable indexed by $p$, and $v_p(|H|)$ is the
exponent of $p$ in the order $|H|$ of $H$. If $H$ is infinite, $f(H) = 1$.

Formalized by `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.orderPolynomial`, a definition declared in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#order-polynomial).

## Eulerian function of a group (G. E. Wall)

Let $G$ be a group and let $f$ be the order
polynomial. A function $\varphi$ from the subgroups of $G$ to the integer polynomial ring
$\mathbb{Z}[x_0, x_1, \dots]$ is an Eulerian function of $G$ if $\sum_{K \le H} \varphi(K) = f(H)$
for every subgroup $H$ of $G$, the sum running over the subgroups $K$ of $H$. The value
$\varphi(G)$ is the Eulerian polynomial of $G$.

For finite $G$ this relation determines $\varphi$ uniquely, by induction on $H$. If infinitely many
subgroups $K \le H$ have $\varphi(K) \ne 0$, the sum is read as $0$.

Formalized by `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.IsEulerianFunction`, a definition declared in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#is-eulerian-function).

## $p$-solvable group

For a natural number $p$, a group $G$ is $p$-solvable if it has a chain
of subgroups $1 = N_0 \le N_1 \le \dots \le N_n = G$ in which each $N_i$ is normal in $N_{i+1}$ and
each index $[N_{i+1} : N_i]$, taken to be $0$ when it is infinite, is a power $p^k$ with $k \ge 0$
or is coprime to $p$. For finite $G$ and prime $p$ this says that every factor $N_{i+1}/N_i$ is a
$p$-group or has order prime to $p$.

Formalized by `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.IsPSolvable`, a definition declared in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#is-psolvable).

## Kourovka Problem 11.104(a) (Eulerian polynomials and solvability, G. E. Wall)

This is the
statement that for every finite group $G$ and every Eulerian function $\varphi$ of $G$, with values
in the integer polynomial ring $\mathbb{Z}[x_0, x_1, \dots]$: if there are a finite set $S$ of
primes and, for each $q \in S$, an integer polynomial $P_q$ involving no variable other than $x_q$,
such that the Eulerian polynomial $\varphi(G)$ equals $\prod_{q \in S} P_q$, then $G$ is
solvable.

Formalized by `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSplitsSolvable`, a definition declared in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#eulerian-polynomial-splits-solvable).

## Kourovka Problem 11.104(b) (Eulerian polynomials and $p$-solvability)

This is the
statement that for every finite group $G$, every prime $p$ and every Eulerian function $\varphi$ of
$G$, with values in the integer polynomial ring $\mathbb{Z}[x_0, x_1, \dots]$: if the Eulerian
polynomial $\varphi(G)$ is a product $PQ$ of integer polynomials where $P$ involves no variable
other than $x_p$ and $x_p$ does not occur in $Q$, then $G$ is $p$-solvable.

Formalized by `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSeparatesPSolvable`, a definition declared in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#eulerian-polynomial-separates-psolvable).

## Solvability from one-variable factorizations of the Eulerian polynomial

Let $G$ be a finite
group and let $\varphi$ be an Eulerian function of $G$, with values in the integer polynomial ring
$\mathbb{Z}[x_0, x_1, \dots]$. If there are a finite set $S$ of primes and, for each $q \in S$, an
integer polynomial $P_q$ involving no variable other than $x_q$, such that the Eulerian polynomial
$\varphi(G)$ equals $\prod_{q \in S} P_q$, then $G$ is solvable.

Resolved true: the Kourovka Archive answers 11.104(a) Yes, citing Detomi and Lucchini (2004).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.104 (G. E. Wall); resolution: E. Detomi and A. Lucchini, J. London Math. Soc. (2) 70 (2004), 165-181 (a); E. Damian and A. Lucchini, Commun. Algebra 35 (2007), 3451-3472 (b), Kourovka Archive, Problem 11.104 ("Yes, the converses are true").

Stated but not proved: `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSplitsSolvable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#eulerian-polynomial-splits-solvable-hold).

## Eulerian polynomial factorization implies $p$-solvability

Let $G$ be a finite group, let $p$
be a prime, and let $\varphi$ be an Eulerian function of $G$, with values in the integer polynomial
ring $\mathbb{Z}[x_0, x_1, \dots]$. If the Eulerian polynomial $\varphi(G)$ is a product $PQ$ of
integer polynomials where $P$ involves no variable other than $x_p$ and $x_p$ does not occur in
$Q$, then $G$ is $p$-solvable.

Resolved true: the Kourovka Archive answers 11.104(b) Yes, citing Damian and Lucchini (2007).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.104 (G. E. Wall); resolution: E. Detomi and A. Lucchini, J. London Math. Soc. (2) 70 (2004), 165-181 (a); E. Damian and A. Lucchini, Commun. Algebra 35 (2007), 3451-3472 (b), Kourovka Archive, Problem 11.104 ("Yes, the converses are true").

Stated but not proved: `MathlibExt.GroupTheory.EulerianPolynomialFactorizationKourovka11Problem104Wanted.eulerianPolynomialSeparatesPSolvable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EulerianPolynomialFactorizationKourovka11Problem104Wanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html#eulerian-polynomial-separates-psolvable-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eulerian polynomials of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/generation/eulerian-polynomials-of-groups)
