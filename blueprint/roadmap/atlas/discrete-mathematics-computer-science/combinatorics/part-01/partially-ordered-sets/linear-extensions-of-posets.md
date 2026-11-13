---
declaration: section
origin: cited
lean: FinPoset.linearExtensions, FinPoset.mem_linearExtensions, FinPoset.linExtOrderIso, FinPoset.someLinearExtension, FinPoset.bijective_someLinearExtension, FinPoset.monotone_someLinearExtension, FinPoset.nonempty_linearExtensions, FinPoset.card_linearExtensions_pos
statement: formalized
proof: formalized
---

# Linear extensions of posets

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html).

## Linear extensions of a finite poset

Let $\alpha$ be a finite poset with $n$
elements. Its linear extensions are represented as rank functions: the set of linear
extensions of $\alpha$ is the finite set of all maps $\sigma : \alpha \to \{0, 1, \dots, n-1\}$
that are bijective and monotone, meaning that $x \le y$ implies $\sigma(x) \le \sigma(y)$.

Formalized by `FinPoset.linearExtensions`, a definition declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#linear-extensions).

## Membership in the linear extensions

Let $\alpha$ be a finite poset with $n$
elements. A map $\sigma : \alpha \to \{0, 1, \dots, n-1\}$ belongs to the set of linear
extensions of $\alpha$ if and only if $\sigma$ is bijective and monotone.

Formalized by `FinPoset.mem_linearExtensions`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#mem-linear-extensions).

## Ranking a Szpilrajn linear extension

Let $\alpha$ be a finite poset with $n$
elements, and fix a linear order on $\alpha$ extending its partial order (one exists by
Szpilrajn's extension theorem; it is chosen once and for all). This is the order
isomorphism from $\alpha$ with that linear order onto $\{0, 1, \dots, n-1\}$ with its usual
order.

Formalized by `FinPoset.linExtOrderIso`, a definition declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#lin-ext-order-iso).

## A chosen linear extension

Let $\alpha$ be a finite poset with $n$ elements, and
fix a linear order on $\alpha$ extending its partial order (one exists by Szpilrajn's
extension theorem; it is chosen once and for all). The chosen linear extension of
$\alpha$ is the rank function $\alpha \to \{0, 1, \dots, n-1\}$ sending each element to its
position in that linear order, counted from $0$.

Formalized by `FinPoset.someLinearExtension`, a definition declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#some-linear-extension).

## The chosen linear extension is bijective

For every finite poset $\alpha$ with
$n$ elements, the chosen linear extension of $\alpha$, viewed as a rank function
$\alpha \to \{0, 1, \dots, n-1\}$, is a bijection.

Formalized by `FinPoset.bijective_someLinearExtension`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#bijective-some-linear-extension).

## The chosen linear extension is monotone

For every finite poset $\alpha$ with
$n$ elements, the chosen linear extension of $\alpha$, viewed as a rank function
$\sigma : \alpha \to \{0, 1, \dots, n-1\}$, is monotone: $x \le y$ implies
$\sigma(x) \le \sigma(y)$.

Formalized by `FinPoset.monotone_someLinearExtension`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#monotone-some-linear-extension).

## Existence of linear extensions

Every finite poset has a linear extension.

Formalized by `FinPoset.nonempty_linearExtensions`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#nonempty-linear-extensions).

## The number of linear extensions is positive

For every finite poset $\alpha$,
the number of linear extensions of $\alpha$ is positive.

So this count is a valid denominator for probabilities over linear extensions.

Formalized by `FinPoset.card_linearExtensions_pos`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#card-linear-extensions-pos).

## Maximal elements of a finite set

For a finite subset $A$ of a partially ordered
set $P$, the maximal elements of $A$ form the subset of those $x \in A$ such that every
$y \in A$ with $x \le y$ equals $x$.

Formalized by `FinPoset.maximalElements`, a definition declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#maximal-elements).

## Membership in the maximal elements

Let $A$ be a finite subset of a partially
ordered set $P$ and let $x \in P$. Then $x$ belongs to the set of maximal elements of $A$
if and only if $x \in A$ and every $y \in A$ with $x \le y$ equals $x$.

Formalized by `FinPoset.mem_maximalElements`, a theorem declared in [MathlibExt/Combinatorics/Poset/LinearExtension.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Poset/LinearExtension.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html#mem-maximal-elements).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear extensions of posets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/partially-ordered-sets/linear-extensions-of-posets)
