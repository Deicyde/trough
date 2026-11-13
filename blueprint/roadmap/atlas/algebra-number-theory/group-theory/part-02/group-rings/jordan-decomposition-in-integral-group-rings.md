---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasIntegralCoeffs, MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasAJD, MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasMJD, MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.finitelyManyTwoGroupsMJDNotAJD, MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.finitelyManyTwoGroupsMJDNotAJD_holds
statement: formalized
---

# Jordan decomposition in integral group rings

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html).

## Elements with integer coefficients

An element $x$ of the monoid algebra $\mathbb{Q}[G]$
lies in $\mathbb{Z}[G]$ when all its coefficients are integers: for every $g \in G$, the
coefficient of $x$ at $g$ is an integer.

Formalized by `MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasIntegralCoeffs`, a definition declared in [WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html#has-integral-coeffs).

## Additive Jordan decomposition property

For a group $G$, let $\mathbb{Z}[G]$ be the set
of elements of the rational group algebra $\mathbb{Q}[G]$ all of whose coefficients are integers.
Then $\mathbb{Z}[G]$ has the additive Jordan decomposition property (AJD) when, for all
$a, s, n \in \mathbb{Q}[G]$ such that $a \in \mathbb{Z}[G]$, $a = s + n$, $sn = ns$, $n$ is
nilpotent and the minimal polynomial of $s$ over $\mathbb{Q}$ is squarefree, both $s$ and $n$ lie
in $\mathbb{Z}[G]$.

For finite $G$ every $a \in \mathbb{Q}[G]$ has exactly one such decomposition $a = s + n$, its
Jordan decomposition, so AJD says that the semisimple and nilpotent parts of every
$a \in \mathbb{Z}[G]$ lie in $\mathbb{Z}[G]$.

Formalized by `MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasAJD`, a definition declared in [WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html#has-ajd).

## Multiplicative Jordan decomposition property

For a group $G$, let $\mathbb{Z}[G]$ be
the set of elements of the rational group algebra $\mathbb{Q}[G]$ all of whose coefficients are
integers. Then $\mathbb{Z}[G]$ has the multiplicative Jordan decomposition property (MJD) when,
for all $a, b, s, u \in \mathbb{Q}[G]$ such that $a, b \in \mathbb{Z}[G]$, $ab = ba = 1$,
$a = su$, $su = us$, $u - 1$ is nilpotent and the minimal polynomial of $s$ over $\mathbb{Q}$ is
squarefree, both $s$ and $u$ lie in $\mathbb{Z}[G]$.

Equivalently, for every unit $a$ of $\mathbb{Z}[G]$ and every factorization $a = su$ in
$\mathbb{Q}[G]$ into commuting factors with $s$ semisimple over $\mathbb{Q}$ and $u$ unipotent,
both factors lie in $\mathbb{Z}[G]$; for finite $G$ such a factorization exists and is unique.

Formalized by `MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.HasMJD`, a definition declared in [WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html#has-mjd).

## Kourovka Problem 16.104

The proposition that there is a natural number $B$ such that
every finite $2$-group $G$ whose integral group ring $\mathbb{Z}[G]$ has the multiplicative Jordan
decomposition property (MJD) but not the additive Jordan decomposition property (AJD) has order
at most $B$.

A. W. Hales and I. B. S. Passi asked whether only finitely many isomorphism classes of finite
$2$-groups $G$ have MJD but not AJD for $\mathbb{Z}[G]$; a bound on the orders is equivalent.

Formalized by `MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.finitelyManyTwoGroupsMJDNotAJD`, a definition declared in [WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html#finitely-many-two-groups-mjdnot-ajd).

## Finitely many $2$-groups have MJD but not AJD

There is a natural number $B$ such that every
finite $2$-group $G$ whose integral group ring $\mathbb{Z}[G]$ has the multiplicative Jordan
decomposition property (MJD) but not the additive Jordan decomposition property (AJD) has order
at most $B$. In particular, only finitely many isomorphism classes of finite $2$-groups have MJD
but not AJD, which answers Kourovka Problem 16.104 in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.104 (A. W. Hales, I. B. S. Passi); resolution: A. W. Hales, I. B. S. Passi and L. E. Wilson, The multiplicative Jordan decomposition in group rings, II, J. Algebra 316 (2007), no. 1, 109-132; corrigendum, J. Algebra 371 (2012), 665-666, Kourovka Archive, Problem 16.104 (answer: Yes, it is true).

Stated but not proved: `MathlibExt.GroupTheory.IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.finitelyManyTwoGroupsMJDNotAJD_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralGroupRingJordanDecompositionKourovka16Problem104Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html#finitely-many-two-groups-mjdnot-ajd-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jordan decomposition in integral group rings](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/group-rings/jordan-decomposition-in-integral-group-rings)
