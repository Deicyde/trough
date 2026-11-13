---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidOf, MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidPolynomialConjugatorLength, MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidPolynomialConjugatorLength_holds
statement: formalized
---

# Conjugators in braid groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups/index.html).

## The braid represented by a braid word

For $n \in \mathbb{N}$, let $B_{n+1}$ be the braid
group on $n + 1$ strands, realized as the Artin group of the Coxeter matrix of type $A_n$, with
standard generators $\sigma_1, \dots, \sigma_n$. A braid word is an element of the free group on
$\sigma_1, \dots, \sigma_n$; the braid it represents is its image under the group homomorphism from
this free group to $B_{n+1}$ that sends each $\sigma_i$ to the generator $\sigma_i$ of $B_{n+1}$.

Formalized by `MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidOf`, a definition declared in [WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups/index.html#braid-of).

## Polynomially short conjugators in braid groups

The proposition (the stronger question of
Kourovka Problem 19.81, V. Shpilrain) that for every $n \in \mathbb{N}$ there are natural numbers
$C$ and $d$ with the following property. Let $B_{n+1}$ be the braid group on $n + 1$ strands,
realized as the Artin group of the Coxeter matrix of type $A_n$, with standard generators
$\sigma_1, \dots, \sigma_n$; a braid word is an element of the free group on
$\sigma_1, \dots, \sigma_n$, and its length $|u|$ is the length of its freely reduced form. For all
braid words $u$ and $v$ whose braids are conjugate in $B_{n+1}$ there is a braid word $w$ with
$|w| \le C (\max(|u|, |v|) + 1)^d$ such that $w u w^{-1}$ and $v$ represent the same braid.

Formalized by `MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidPolynomialConjugatorLength`, a definition declared in [WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups/index.html#braid-polynomial-conjugator-length).

## Braid groups have polynomially short conjugators

For $n \in \mathbb{N}$, let $B_{n+1}$ be
the braid group on $n + 1$ strands, realized as the Artin group of the Coxeter matrix of type
$A_n$, with standard generators $\sigma_1, \dots, \sigma_n$. A braid word is an element of the
free group on $\sigma_1, \dots, \sigma_n$, and its length $|u|$ is the length of its freely reduced
form. For every $n$ there are natural numbers $C$ and $d$ such that for all braid words $u$ and $v$
whose braids are conjugate in $B_{n+1}$ there is a braid word $w$ with
$|w| \le C (\max(|u|, |v|) + 1)^d$ such that $w u w^{-1}$ and $v$ represent the same braid.

This answers the stronger question of Kourovka Problem 19.81 positively: the Kourovka Archive
answers "Yes, there is such a conjugator, even for any mapping class groups", citing Tao's
linearly bounded conjugator property for mapping class groups (Theorem B: a conjugator of length
at most $K(|f| + |g|)$).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.81 (V. Shpilrain); resolution: J. Tao, Linearly bounded conjugator property for mapping class groups, Geom. Funct. Anal. 23 (2013), no. 1, 415-466 (arXiv:1106.2341), Theorem B: for a finite generating set of the mapping class group of a surface of finite type there is K such that conjugate f, g have a conjugator ω with |ω| ≤ K(|f| + |g|); Kourovka Archive, Problem 19.81: Yes, there is such a conjugator, even for any mapping class groups, https://arxiv.org/abs/1106.2341.

Stated but not proved: `MathlibExt.GroupTheory.BraidConjugatorLengthKourovka19Problem81Wanted.braidPolynomialConjugatorLength_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BraidConjugatorLengthKourovka19Problem81Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups/index.html#braid-polynomial-conjugator-length-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugators in braid groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/conjugators-in-braid-groups)
