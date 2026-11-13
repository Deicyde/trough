---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.exists_common_indep_of_cut_le, MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.edmonds_matroid_intersection', MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.edmonds_matroid_intersection
statement: formalized
proof: formalized
---

# Matroid intersection theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem/index.html).

## Matroid intersection for abstract rank functions

Let $E$ be a finite subset of a type
$\alpha$, let $k$ be a natural number, and let $r_1, r_2$ be functions from the finite subsets of
$\alpha$ to $\mathbb{N}$ such that, for $i = 1, 2$ and all finite $X, Y \subseteq \alpha$, we have
$r_i(X) \le |X|$, $r_i(X) \le r_i(Y)$ whenever $X \subseteq Y$, and
$r_i(X \cap Y) + r_i(X \cup Y) \le r_i(X) + r_i(Y)$. If every $X \subseteq E$ satisfies
$k \le r_1(X) + r_2(E \setminus X)$, then there is a set $I \subseteq E$ with
$r_1(I) = r_2(I) = |I|$ and $|I| \ge k$.

Proved by induction on $E$, via deletion and contraction.

Formalized by `MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.exists_common_indep_of_cut_le`, a theorem declared in [MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem/index.html#exists-common-indep-of-cut-le).

## Edmonds' matroid intersection theorem

Let $M_1$ and $M_2$ be matroids on a finite type
$\alpha$, with arbitrary ground sets, and let $k$ be a natural number. There is a set
$I \subseteq \alpha$ independent in both $M_1$ and $M_2$ with $|I| \ge k$ if and only if every
$X \subseteq \alpha$ satisfies $k \le r_1(X) + r_2(\alpha \setminus X)$, where $r_i(Y)$ is the
largest size of a subset of $Y$ independent in $M_i$.

Formalized by `MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.edmonds_matroid_intersection'`, a theorem declared in [MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem/index.html#edmonds-matroid-intersection).

## Edmonds' matroid intersection theorem for matroids on the whole type

Let $M_1$ and $M_2$ be
matroids on a finite type $\alpha$, each with ground set all of $\alpha$, and let $k$ be a natural
number. There is a set $I \subseteq \alpha$ independent in both $M_1$ and $M_2$ with $|I| \ge k$
if and only if every $X \subseteq \alpha$ satisfies $k \le r_1(X) + r_2(\alpha \setminus X)$,
where $r_i$ is the rank function of $M_i$.

The hypotheses on the ground sets are not needed; the general version drops them.

## Sources

- J. Edmonds, Submodular Functions, Matroids, and Certain Polyhedra, Combinatorial Structures and Their Applications (1970), 69–87.

Formalized by `MathlibExt.Combinatorics.Matroid.MatroidIntersectionWanted.edmonds_matroid_intersection`, a theorem declared in [MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/MatroidIntersection.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem/index.html#edmonds-matroid-intersection-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matroid intersection theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/matroid-theory/matroid-intersection-theorem)
