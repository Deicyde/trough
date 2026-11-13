---
declaration: section
origin: cited
lean: MetaMathlibExt.minimumRestrictedAdditiveBasisCard, MetaMathlibExt.minimumRestrictedAdditiveBasisCard_eq_none_iff, MetaMathlibExt.minimumRestrictedAdditiveBasisCard_isSome_iff
statement: formalized
proof: formalized
---

# Restricted additive bases

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases/index.html).

## Minimum size of a restricted additive basis

Let $s$ be a natural number. A restricted
additive basis of $\{0, 1, \dots, s\}$ is a finite set $A$ of natural numbers with $2a \le s$ for
every $a \in A$ such that every natural number $x \le s$ can be written as $x = a + b$ with
$a, b \in A$, where $a = b$ is allowed. The minimum restricted additive basis size $k^*(s)$ is
the smallest cardinality of a restricted additive basis of $\{0, 1, \dots, s\}$; it is undefined
when no restricted additive basis of $\{0, 1, \dots, s\}$ exists.

The restriction $2a \le s$ is imposed for odd $s$ as well as for even $s$.

## Sources

- Jukka Kohonen, Visa Koivunen, and Robin Rajamäki, *Planar Additive Bases for Rectangles*, Journal of Integer Sequences 21 (2018), Article 18.9.8: additive-basis notion (`A + A ⊇ [0, n]`), lines 126–128; one-dimensional restricted basis (`A ⊆ [0, n/2]`), lines 170–171; minimum restricted-basis notation `k^*`, lines 200–203, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Rajamaki/raj.tex>. The one-dimensional `k^*(s, 0)` notion supports G. Yu's restricted 2-basis bound (`s_x / k^*(s_x, 0)^2 ≤ 0.41983`, equation `eq:yu_restr`, lines 897–901), quoting G. Yu, *Upper bounds for finite additive 2-bases*, Proc. Amer. Math. Soc. 137 (2009), 11–18, Theorem 1.2.

Formalized by `MetaMathlibExt.minimumRestrictedAdditiveBasisCard`, a definition declared in [MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases/index.html#minimum-restricted-additive-basis-card).

## The minimum restricted additive basis size is undefined exactly in the odd case

For
every natural number $s$, the minimum size $k^*(s)$ of a restricted additive basis of
$\{0, 1, \dots, s\}$, that is, of a finite set $A$ of natural numbers with $2a \le s$ for every
$a \in A$ such that every natural number $x \le s$ equals $a + b$ for some $a, b \in A$, is
undefined if and only if $s$ is odd.

Formalized by `MetaMathlibExt.minimumRestrictedAdditiveBasisCard_eq_none_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases/index.html#minimum-restricted-additive-basis-card-e).

## The minimum restricted additive basis size is defined exactly in the even case

For
every natural number $s$, the minimum size $k^*(s)$ of a restricted additive basis of
$\{0, 1, \dots, s\}$, that is, of a finite set $A$ of natural numbers with $2a \le s$ for every
$a \in A$ such that every natural number $x \le s$ equals $a + b$ for some $a, b \in A$, is
defined if and only if $s$ is even.

Formalized by `MetaMathlibExt.minimumRestrictedAdditiveBasisCard_isSome_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/MinimumRestrictedAdditiveBasis.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases/index.html#minimum-restricted-additive-basis-card-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted additive bases](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/restricted-additive-bases)
