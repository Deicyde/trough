---
declaration: section
origin: cited
lean: MetaMathlibExt.meromorphicStirlingFirst, MetaMathlibExt.meromorphicStirlingSecond, MetaMathlibExt.besselNumberFirst, MetaMathlibExt.besselNumberSecond, MetaMathlibExt.meromorphicStirlingFirst_eq_besselNumberFirst, MetaMathlibExt.meromorphicStirlingSecond_eq_besselNumberSecond
statement: formalized
proof: formalized
---

# Meromorphic Stirling numbers and Bessel numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html).

## The meromorphic Stirling numbers $S_{2;-1}(n,k)$

For natural numbers $n$ and $k$ with
$1 \le k \le n$, the meromorphic Stirling number $S_{2;-1}(n,k)$ is the rational number

$$S_{2;-1}(n,k) = \frac{(-1)^{n-k}\,(n-1)!}{2^{n-k}\,(k-1)!}\binom{2n-k-1}{n-1}.$$

For other $n$ and $k$ the same expression is evaluated with natural-number subtraction truncated
at $0$.

## Sources

- Schork, On Generalized Stirling Numbers and Normal Ordering, StirW1 formula. Defined independently from the Bessel side.

Formalized by `MetaMathlibExt.meromorphicStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#meromorphic-stirling-first).

## The meromorphic Stirling numbers $S_{-1;1}(n,k)$

For natural numbers $n$ and $k$ with
$k \le n \le 2k$, the meromorphic Stirling number $S_{-1;1}(n,k)$ is the rational number

$$S_{-1;1}(n,k) = \frac{(2n-2k)!}{2^{n-k}\,(n-k)!}\binom{n}{2k-n}.$$

For other $n$ and $k$ the same expression is evaluated with natural-number subtraction truncated
at $0$.

## Sources

- Schork, On Generalized Stirling Numbers and Normal Ordering, StirW2 formula. Defined independently from the Bessel side.

Formalized by `MetaMathlibExt.meromorphicStirlingSecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#meromorphic-stirling-second).

## Bessel numbers of the first kind

For natural numbers $n$ and $k$ with $1 \le k \le n$, the
Bessel number of the first kind is the rational number

$$b(n,k) = \frac{(-1)^{n-k}\,(2n-k-1)!}{2^{n-k}\,(k-1)!\,(n-k)!}.$$

For other $n$ and $k$ the same expression is evaluated with natural-number subtraction truncated
at $0$.

## Sources

- Schork, On Generalized Stirling Numbers and Normal Ordering, Bessfirst formula. Defined independently from the meromorphic side.

Formalized by `MetaMathlibExt.besselNumberFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#bessel-number-first).

## Bessel numbers of the second kind

For natural numbers $n$ and $k$ with $k \le n \le 2k$,
the Bessel number of the second kind is the rational number

$$B(n,k) = \frac{n!}{2^{n-k}\,(2k-n)!\,(n-k)!}.$$

For other $n$ and $k$ the same expression is evaluated with natural-number subtraction truncated
at $0$.

## Sources

- Schork, On Generalized Stirling Numbers and Normal Ordering, Besssecond formula. Defined independently from the meromorphic side.

Formalized by `MetaMathlibExt.besselNumberSecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#bessel-number-second).

## First identification of meromorphic Stirling and Bessel numbers

For all natural numbers
$n$ and $k$ with $1 \le k \le n$, the meromorphic Stirling number $S_{2;-1}(n,k)$ equals the
Bessel number of the first kind $b(n,k)$.

Formalized by `MetaMathlibExt.meromorphicStirlingFirst_eq_besselNumberFirst`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#meromorphic-stirling-first-eq-bessel-num).

## Second identification of meromorphic Stirling and Bessel numbers

For all natural numbers
$n$ and $k$ with $k \le n \le 2k$, the meromorphic Stirling number $S_{-1;1}(n,k)$ equals the
Bessel number of the second kind $B(n,k)$.

Formalized by `MetaMathlibExt.meromorphicStirlingSecond_eq_besselNumberSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeromorphicStirlingNumber.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html#meromorphic-stirling-second-eq-bessel-nu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Meromorphic Stirling numbers and Bessel numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/meromorphic-stirling-numbers-and-bessel-numbers)
