---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PolysizeColoringListWanted.discrepancyOn, MathlibExt.Combinatorics.PolysizeColoringListWanted.hereditaryDisc, MathlibExt.Combinatorics.PolysizeColoringListWanted.conjecture, MathlibExt.Combinatorics.PolysizeColoringListWanted.conjecture_refuted
statement: formalized
---

# Colouring lists for hereditary discrepancy

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html).

## Discrepancy of a matrix on a set of columns

For a real $n \times m$ matrix $A$ and a set
$S$ of columns of $A$, the discrepancy of $A$ on $S$ is the minimum, over all sign vectors
$\varepsilon \in \{-1, 1\}^m$, of $\max_i \left|\sum_{j \in S} A_{ij} \varepsilon_j\right|$, the
largest absolute value of a row sum of $A$ restricted to $S$ and weighted by $\varepsilon$
(taken to be $0$ when $A$ has no rows).

Formalized by `MathlibExt.Combinatorics.PolysizeColoringListWanted.discrepancyOn`, a definition declared in [WantedExt/Combinatorics/PolysizeColoringListWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolysizeColoringListWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html#discrepancy-on).

## Hereditary discrepancy of a real matrix

The hereditary discrepancy
$\operatorname{herdisc}(A)$ of a real $n \times m$ matrix $A$ is the maximum, over all sets $S$
of columns of $A$, of the discrepancy of $A$ on $S$.

Formalized by `MathlibExt.Combinatorics.PolysizeColoringListWanted.hereditaryDisc`, a definition declared in [WantedExt/Combinatorics/PolysizeColoringListWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolysizeColoringListWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html#hereditary-disc).

## Polynomial-size colouring list conjecture

The statement that there exist a real number
$C > 0$ and a natural number $k$ such that for all positive integers $n$ and $m$ and every real
$n \times m$ matrix $A$ there is a set $L$ of at most $m^k$ sign vectors in $\{-1, 1\}^m$ with
the following property: for every set $S$ of columns of $A$ some $\varepsilon \in L$ satisfies
$\left|\sum_{j \in S} A_{ij} \varepsilon_j\right| \le C \operatorname{herdisc}(A)$ for every row
$i$, where $\operatorname{herdisc}(A)$ is the hereditary discrepancy of $A$.

## Sources

- AIM-COMBINATORICS-0047__20000922; AIM Hereditary discrepancy, item 1.85.

Formalized by `MathlibExt.Combinatorics.PolysizeColoringListWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PolysizeColoringListWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolysizeColoringListWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html#conjecture).

## The polynomial-size colouring list conjecture is false

There do not exist a real number
$C > 0$ and a natural number $k$ such that for all positive integers $n$ and $m$ and every real
$n \times m$ matrix $A$ there is a set $L$ of at most $m^k$ sign vectors in $\{-1, 1\}^m$ with
the following property: for every set $S$ of columns of $A$ some $\varepsilon \in L$ satisfies
$\left|\sum_{j \in S} A_{ij} \varepsilon_j\right| \le C \operatorname{herdisc}(A)$ for every row
$i$, where $\operatorname{herdisc}(A)$ is the hereditary discrepancy of $A$.

The AIM problem list records this negative answer: for the $0/1$ matrix with $m$ columns whose
$\sqrt{m}$ rows are the indicators of disjoint sets of $\sqrt{m}$ columns, the hereditary
discrepancy is $1$, yet for fixed $C$ and lists of polynomial size some set of columns has
discrepancy above $C$ under every listed colouring.

## Sources

- AIM Problem Lists, Hereditary discrepancy and factorization norms, Problem 1.85 (Polysize list of colorings), https://aimpl.org/hereddiscrep/1/.

Stated but not proved: `MathlibExt.Combinatorics.PolysizeColoringListWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolysizeColoringListWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolysizeColoringListWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colouring lists for hereditary discrepancy](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/discrepancy-theory/colouring-lists-for-hereditary-discrepancy)
