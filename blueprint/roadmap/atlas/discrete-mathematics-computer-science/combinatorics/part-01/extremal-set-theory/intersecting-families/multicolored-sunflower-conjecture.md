---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.TernaryVec, MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.HasMulticoloredSunflower, MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.multicoloredSunflowerConjecture, MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.multicoloredSunflowerConjecture_holds
statement: formalized
---

# Multicolored sunflower conjecture

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html).

## Ternary vectors

For a natural number $n$, the vectors of length $n$ over $\mathbb{Z}/3$,
that is, the functions from $\{0, 1, \dots, n - 1\}$ to $\mathbb{Z}/3$.

Formalized by `MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.TernaryVec`, an abbreviation declared in [WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html#ternary-vec).

## Multicolored sunflower

Let $n$ be a natural number and let $S$ be a finite set of triples
$(x, y, z)$ of vectors in $(\mathbb{Z}/3)^n$. Then $S$ contains a multicolored sunflower if there
are triples $(x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3) \in S$, not all three equal, with
$x_1 + y_2 + z_3 = 0$.

Formalized by `MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.HasMulticoloredSunflower`, a definition declared in [WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html#has-multicolored-sunflower).

## Multicolored sunflower conjecture

There are a real number $\varepsilon > 0$ and a natural
number $n_0$ such that for every $n > n_0$, every finite set $S$ of triples $(x, y, z)$ of vectors
in $(\mathbb{Z}/3)^n$ with $x + y + z = 0$ for every $(x, y, z) \in S$ and with
$|S| \ge 3^{(1 - \varepsilon) n}$ contains a multicolored sunflower: triples
$(x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3) \in S$, not all three equal, with
$x_1 + y_2 + z_3 = 0$.

The conjecture is due to Alon, Shpilka and Umans (Oberwolfach Report 54/2012, Conjecture 7).

Formalized by `MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.multicoloredSunflowerConjecture`, a definition declared in [WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html#multicolored-sunflower-conjecture).

## The multicolored sunflower conjecture holds

There are a real number $\varepsilon > 0$ and a
natural number $n_0$ such that for every $n > n_0$, every finite set $S$ of triples $(x, y, z)$ of
vectors in $(\mathbb{Z}/3)^n$ with $x + y + z = 0$ for every $(x, y, z) \in S$ and with
$|S| \ge 3^{(1 - \varepsilon) n}$ contains a multicolored sunflower: triples
$(x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3) \in S$, not all three equal, with
$x_1 + y_2 + z_3 = 0$.

This was resolved in the affirmative: a set $S$ as above with no multicolored sunflower is a
tricolored sum-free set ($x_a + y_b + z_c = 0$ only for $a = b = c$), and Blasiak, Church, Cohn,
Grochow, Naslund, Sawin and Umans proved (Theorem A′) that such sets in $(\mathbb{Z}/3)^n$ have at
most $3 \cdot 3^{(1 - \delta/\log 3) n}$ elements, $\delta = 0.0566\ldots$; Alon, Shpilka and Umans
had shown that this tricolored version of the cap set bound disproves the strong USP conjecture.

## Sources

- C. Umans, in Complexity Theory, Oberwolfach Reports 9 (2012), no. 54, p. 3292, Conjecture 7, DOI 10.4171/OWR/2012/54; resolution: J. Blasiak, T. Church, H. Cohn, J. A. Grochow, E. Naslund, W. F. Sawin and C. Umans, On cap sets and the group-theoretic approach to matrix multiplication, Discrete Anal. 2017:3, arXiv:1605.06702, Theorem A′: for H ≅ (ℤ/q)ⁿ, q a prime power, every tricolored sum-free set in H (Definition 3.1) has at most 3 |H|^{1 - δ/log q} elements, δ = 0.0566...; Section 1: Alon, Shpilka and Umans showed that a tricolored version of the cap set bounds would disprove the strong USP conjecture (the source's Theorem 8), and Theorem A disproves it via their result; Kleinberg, Sawin and Speyer, arXiv:1607.00047, abstract, restate the bound as 3 θⁿ, θ ≈ 2.755, https://arxiv.org/abs/1605.06702.

Stated but not proved: `MathlibExt.Combinatorics.MulticoloredSunflowerTernaryOWR12177Problem010Wanted.multicoloredSunflowerConjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MulticoloredSunflowerTernaryOWR12177Problem010Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html#multicolored-sunflower-conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multicolored sunflower conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/multicolored-sunflower-conjecture)
