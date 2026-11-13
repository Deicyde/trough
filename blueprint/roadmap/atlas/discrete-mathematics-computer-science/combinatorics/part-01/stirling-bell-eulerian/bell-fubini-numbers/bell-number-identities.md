---
declaration: section
origin: cited
lean: MetaMathlibExt.bell_eq_signed_stirlingFirst_convolution, MetaMathlibExt.bell_eq_sum_stirlingSecond
statement: formalized
proof: formalized
---

# Bell number identities

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/bell-number-identities/index.html).

## Gould–Quaintance double-sum formula for Bell numbers

Write $B_n$ for the $n$-th Bell
number and $s(p, m) = (-1)^{p-m} {p \brack m}$ for the signed Stirling number of the first kind,
where ${p \brack m}$ is the number of permutations of $p$ elements with exactly $m$ cycles. For all
natural numbers $n$ and $p$, with the convention $0^0 = 1$,

$$B_n = \sum_{k=0}^{n} (-p)^{n-k} \binom{n}{k} \sum_{m=0}^{p} B_{k+m}\, s(p, m).$$

The source states the formula for $p \ge 1$; with $0^0 = 1$ it also holds for $p = 0$.

## Sources

- H. W. Gould and Jocelyn Quaintance, "Implications of Spivey's Bell Number Formula," Journal of Integer Sequences 11 (2008), Article 08.3.7, Theorem, equation (E:4), lines 177–182, https://cs.uwaterloo.ca/journals/JIS/VOL11/Gould/gould35.tex

Formalized by `MetaMathlibExt.bell_eq_signed_stirlingFirst_convolution`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellConvolution.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BellConvolution.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/bell-number-identities/index.html#bell-eq-signed-stirling-first-convolutio).

## Bell numbers are row sums of Stirling numbers of the second kind

For every
natural number $n$, the Bell number $B_n$ equals $\sum_{k=0}^{n} S(n, k)$, where $S(n, k)$ is the
Stirling number of the second kind.

## Sources

- Michael Z. Spivey, *A Generalized Recurrence for Bell Numbers*, Journal of Integer Sequences 11 (2008), Article 08.2.5, equation `Stir`, lines 107–108 (quoting the classical formula), <https://cs.uwaterloo.ca/journals/JIS/VOL11/Spivey/spivey25.tex>.

Formalized by `MetaMathlibExt.bell_eq_sum_stirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellStirlingSum.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BellStirlingSum.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/bell-number-identities/index.html#bell-eq-sum-stirling-second).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bell number identities](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/bell-number-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/bell-number-identities)
