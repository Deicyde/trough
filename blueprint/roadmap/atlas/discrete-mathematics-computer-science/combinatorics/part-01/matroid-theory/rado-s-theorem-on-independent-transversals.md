---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Matroid.RadoWanted.rado_matroidal_marriage', MathlibExt.Combinatorics.Matroid.RadoWanted.rado_matroidal_marriage
statement: formalized
proof: formalized
---

# Rado's theorem on independent transversals

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/rado-s-theorem-on-independent-transversals/index.html).

## Rado's theorem on independent transversals, arbitrary ground set

Let $I$ and $E$ be finite
sets, let $M$ be a matroid with ground set $E(M) \subseteq E$, and let $(A_i)_{i \in I}$ be a
family of subsets of $E$. Then there is an injective map $f : I \to E$ such that $f(i) \in A_i$
for every $i \in I$ and the image $f(I)$ is independent in $M$, if and only if
$|J| \le r_M\bigl(\bigcup_{i \in J} A_i\bigr)$ for every $J \subseteq I$, where $r_M(X)$ denotes
the rank in $M$ of $X \cap E(M)$.

Formalized by `MathlibExt.Combinatorics.Matroid.RadoWanted.rado_matroidal_marriage'`, a theorem declared in [MathlibExt/Combinatorics/Matroid/Rado.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matroid/Rado.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/rado-s-theorem-on-independent-transversals/index.html#rado-matroidal-marriage).

## Rado's theorem on independent transversals

Let $I$ and $E$ be finite sets, let $M$ be a
matroid whose ground set is all of $E$, and let $(A_i)_{i \in I}$ be a family of subsets of $E$.
Then there is an injective map $f : I \to E$ such that $f(i) \in A_i$ for every $i \in I$ and
the image $f(I)$ is independent in $M$, if and only if
$|J| \le r_M\bigl(\bigcup_{i \in J} A_i\bigr)$ for every $J \subseteq I$, where $r_M$ is the rank
function of $M$.

The hypothesis that the ground set of $M$ is all of $E$ is not needed.

## Sources

- R. Rado, Quart. J. Math. os-13 (1942), DOI 10.1093/qmath/os-13.1.83.

Formalized by `MathlibExt.Combinatorics.Matroid.RadoWanted.rado_matroidal_marriage`, a theorem declared in [MathlibExt/Combinatorics/Matroid/Rado.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matroid/Rado.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/rado-s-theorem-on-independent-transversals/index.html#rado-matroidal-marriage-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rado's theorem on independent transversals](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/rado-s-theorem-on-independent-transversals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/matroid-theory/rado-s-theorem-on-independent-transversals)
