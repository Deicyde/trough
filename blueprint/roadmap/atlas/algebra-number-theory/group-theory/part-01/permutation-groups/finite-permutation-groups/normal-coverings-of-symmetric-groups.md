---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumber, MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.conjecturedValue, MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumberEventuallyConjectured, MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumberEventuallyConjectured_refuted
statement: formalized
---

# Normal coverings of symmetric groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html).

## Normal covering number of the symmetric group

For a natural number $n$, the normal
covering number $\gamma(S_n)$ is the least $k$ for which there are proper subgroups
$H_1, \dots, H_k$ of the symmetric group $S_n$ such that every element of $S_n$ is conjugate to an
element of some $H_i$. When no such subgroups exist, as for $n \le 2$, it is $0$.

Formalized by `MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumber`, a definition declared in [WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html#normal-covering-number).

## Bubboloni–Praeger–Spiga conjectured value

For a natural number $n \ge 2$, write
$n = p_1^{\alpha_1} \cdots p_r^{\alpha_r}$ with primes $p_1 < \cdots < p_r$ and exponents
$\alpha_i \ge 1$, and let $p_2$ be the least prime factor of $n / p_1^{\alpha_1}$. The conjectured
value of $n$ is the rational number $\frac{n}{2}(1 - \frac{1}{p_1})$ if $r = 1$ and $\alpha_1 = 1$;
$\frac{n}{2}(1 - \frac{1}{p_1}) + 1$ if $r = 1$ and $\alpha_1 \ge 2$;
$\frac{n}{2}(1 - \frac{1}{p_1})(1 - \frac{1}{p_2}) + 1$ if $r = 2$ and $\alpha_1 = \alpha_2 = 1$;
and $\frac{n}{2}(1 - \frac{1}{p_1})(1 - \frac{1}{p_2}) + 2$ if $r \ge 2$ and
$\alpha_1 + \cdots + \alpha_r \ge 3$. For $n = 0$ and $n = 1$ the value is $2$.

Formalized by `MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.conjecturedValue`, a definition declared in [WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html#conjectured-value).

## Bubboloni–Praeger–Spiga normal covering conjecture (eventual form)

There is a natural
number $N$ such that, for every $n \ge N$, the normal covering number $\gamma(S_n)$ of the
symmetric group $S_n$ equals the Bubboloni–Praeger–Spiga conjectured value of $n$.

This is Kourovka Problem 18.23 (D. Bubboloni, C. E. Praeger, P. Spiga) in the form "for all
sufficiently large $n$" that the proposers single out.

Formalized by `MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumberEventuallyConjectured`, a definition declared in [WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html#normal-covering-number-eventually-conjec).

## Refutation of the Bubboloni–Praeger–Spiga normal covering conjecture

It is not the case
that there is a natural number $N$ such that, for every $n \ge N$, the normal covering number
$\gamma(S_n)$ of the symmetric group $S_n$ equals the Bubboloni–Praeger–Spiga conjectured value
of $n$. In other words, the conjecture fails for arbitrarily large $n$.

The Kourovka Archive records that A. Maróti showed the conjecture incorrect for odd $n$. His
covering, given in Section 2 of Bubboloni–Praeger–Spiga (2020), yields
$\gamma(S_n) \le n/3 + \varphi(n)/2 + \omega(n)$, where $\varphi$ is Euler's function and
$\omega(n)$ the number of distinct prime factors of $n$. This is below the conjectured value when
$n$ is the product of $r$ consecutive primes starting at a prime $p \ge 43$ and $r$ is large.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.23 (D. Bubboloni, C. E. Praeger, P. Spiga); resolution: D. Bubboloni, C. E. Praeger and P. Spiga, Linear bounds for the normal covering number of the symmetric and alternating groups, Monatsh. Math. 191 (2020), 229-247, Section 2, A. Maróti's construction: for n = N(r, p), the product of r consecutive primes starting at p ≥ 43, and r ≥ r*, γ(Sym(n)) < (n/2)(1 - 1/p₁)(1 - 1/p₂) + 2, contradicting the conjecture for infinitely many p and r; Kourovka Archive, Problem 18.23, https://api.research-repository.uwa.edu.au/ws/files/49055019/Bubboloni_et_al_2019_Linear_bounds_for_the_normal_covering.pdf.

Stated but not proved: `MathlibExt.GroupTheory.NormalCoveringSymmetricKourovka18Problem23Wanted.normalCoveringNumberEventuallyConjectured_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NormalCoveringSymmetricKourovka18Problem23Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html#normal-covering-number-eventually-conjec-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal coverings of symmetric groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/normal-coverings-of-symmetric-groups)
