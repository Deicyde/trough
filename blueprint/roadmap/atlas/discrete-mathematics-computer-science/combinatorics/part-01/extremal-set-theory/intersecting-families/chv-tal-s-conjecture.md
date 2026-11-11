---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.IsHereditary, MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.conjecture, MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.conjecture_holds
statement: formalized
---

# Chvátal's conjecture

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture/index.html).

## Hereditary families

A finite family $F$ of finite subsets of $\alpha$ is hereditary (an
independence system) when it contains every subset of each of its members: if $A \in F$ and
$B \subseteq A$, then $B \in F$.

Formalized by `MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.IsHereditary`, a definition declared in [WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture/index.html#is-hereditary).

## Chvátal's conjecture

The statement that for every finite set $X$ and every hereditary
family $F$ of subsets of $X$ that contains a nonempty set, there is a point $x \in X$ such that
every intersecting subfamily $G \subseteq F$ has at most as many members as the star
$\{A \in F : x \in A\}$ of $x$. Here $F$ is hereditary when it contains every subset of each of
its members, and $G$ is intersecting when any two distinct members of $G$ meet.

The point $x$ is fixed for the whole family, and the competing subfamilies $G$ need not be
hereditary.

Formalized by `MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture/index.html#conjecture).

## Chvátal's conjecture holds

For every finite set $X$ and every hereditary family $F$ of
subsets of $X$ (one containing every subset of each of its members) that contains a nonempty set,
there is a point $x \in X$ such that every intersecting subfamily $G \subseteq F$ (one in which
any two distinct members meet) has at most as many members as the star $\{A \in F : x \in A\}$.

Resolved true: Chang, Liu, and Liu (arXiv:2609.19123, 2026) prove Chvátal's conjecture. Ellis,
Filmus, and Friedgut (arXiv:2609.28404) give an independent spectral proof, and Keevash
(arXiv:2609.23595) proves the stronger Kahn flow conjecture. erdosproblems.com/701 lists the
Chang–Liu–Liu proof claim with a Lean formalization by Boon Suan Ho.

## Sources

- Fan Chang, Hong Liu, and Miao Liu, A proof of Chvátal's conjecture via a sharp correlation inequality, arXiv:2609.19123 (2026), https://arxiv.org/abs/2609.19123; David Ellis, Yuval Filmus, and Ehud Friedgut, Chvátal's conjecture: a proof from The Book, arXiv:2609.28404v2 (2026), https://arxiv.org/abs/2609.28404; Peter Keevash, On Kahn's flow conjecture, arXiv:2609.23595 (2026), https://arxiv.org/abs/2609.23595.

Stated but not proved: `MathlibExt.Combinatorics.ChvatalHereditaryIntersectingWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ChvatalHereditaryIntersectingWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chvátal's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/chv-tal-s-conjecture)
