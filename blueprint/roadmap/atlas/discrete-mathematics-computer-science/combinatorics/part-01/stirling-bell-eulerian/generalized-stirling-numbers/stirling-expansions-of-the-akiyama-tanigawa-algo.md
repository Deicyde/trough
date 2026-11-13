---
declaration: section
origin: cited
lean: MetaMathlibExt.chen_stirlingSecond_expansion, MetaMathlibExt.poly_initial_expansion
statement: formalized
proof: formalized
---

# Stirling expansions of the Akiyama–Tanigawa algorithm

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-expansions-of-the-akiyama-tanigawa-algo/index.html).

## Chen's Stirling expansion

Let $a(m, s)$, for natural numbers $m$ and $s$, be real
numbers satisfying $a(m, s + 1) = m \, a(m, s) - (m + 1) \, a(m + 1, s)$ for all $m$ and $s$.
Then for every natural number $t$,

$$a(0, t) = \sum_{m=0}^{t} (-1)^m \, m! \, S(t, m) \, a(m, 0),$$

where $S(t, m)$ is the Stirling number of the second kind.

This recurrence is a variant of the Akiyama–Tanigawa algorithm.

## Sources

- K.-W. Chen, "Algorithms for Bernoulli numbers and Euler numbers," Journal of Integer Sequences 4 (2001), Article 01.1.6, as stated in Dil, Kurt, and Cenkci (2007), Proposition 4. It is the `x = 0` case of `poly_initial_expansion`.

Formalized by `MetaMathlibExt.chen_stirlingSecond_expansion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PolyInitialExpansion.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PolyInitialExpansion.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-expansions-of-the-akiyama-tanigawa-algo/index.html#chen-stirling-second-expansion).

## Expansion by generalized Stirling numbers of the second kind

For every natural number
$n$, every real number $x$ and all real numbers $a(m, t)$, indexed by natural numbers $m$ and $t$,
such that $a(m, t + 1) = m\,a(m, t) - (m + 1)\,a(m + 1, t)$ for all $m$ and $t$, writing
${n \brace m}_x$ for the generalized Stirling numbers of the second kind,

$$\sum_{k=0}^{n} \binom{n}{k} x^k a(0, n - k) = \sum_{m=0}^{n} (-1)^m m! {n \brace m}_x a(m, 0).$$

## Sources

- Ayhan Dil, Veli Kurt, and Mehmet Cenkci, "Algorithms for Bernoulli and Related Polynomials," Journal of Integer Sequences 10 (2007), Article 07.5.4, Proposition 5, lines 661–671, https://cs.uwaterloo.ca/journals/JIS/VOL10/Dil/dil11.tex

Formalized by `MetaMathlibExt.poly_initial_expansion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PolyInitialExpansion.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PolyInitialExpansion.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-expansions-of-the-akiyama-tanigawa-algo/index.html#poly-initial-expansion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stirling expansions of the Akiyama–Tanigawa algorithm](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-expansions-of-the-akiyama-tanigawa-algo/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-expansions-of-the-akiyama-tanigawa-algo)
