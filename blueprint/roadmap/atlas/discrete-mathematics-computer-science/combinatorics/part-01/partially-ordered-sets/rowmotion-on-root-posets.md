---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsHomomesic, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.PosetAntichain, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsAntichainCardinality, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsAntichainRowmotion, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsTypeARootPoset, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.conjecture, MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.conjecture_holds
statement: formalized
---

# Rowmotion on root posets

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html).

## Homomesy

Let $X$ be a type, $\sigma \colon X \to X$ a map, $f \colon X \to \mathbb{Q}$ a
function and $c \in \mathbb{Q}$. Then $f$ is homomesic under $\sigma$ with average $c$ when $X$ is
finite, $\sigma$ is bijective, and for every $x \in X$ and every $k > 0$ with $\sigma^k(x) = x$
the average $\frac{1}{k} \sum_{i=0}^{k-1} f(\sigma^i(x))$ equals $c$.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsHomomesic`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#is-homomesic).

## Finite antichains of a poset

For a partially ordered set $P$, the finite antichains of
$P$ are the finite subsets $A \subseteq P$ in which no element is below a different element.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.PosetAntichain`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#poset-antichain).

## Antichain cardinality statistic

For a partially ordered set $P$, a function $f$ from the
finite antichains of $P$ to $\mathbb{Q}$ is the antichain cardinality statistic when
$f(A) = |A|$ for every finite antichain $A$ of $P$.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsAntichainCardinality`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#is-antichain-cardinality).

## Rowmotion on antichains

For a partially ordered set $P$, a map $\rho$ from the finite
antichains of $P$ to themselves is antichain rowmotion when $\rho$ is bijective and, for every
finite antichain $A$, $\rho(A)$ is the set of minimal elements of the complement of the down-set
of $A$: an element $x \in P$ lies in $\rho(A)$ exactly when $x \not\le a$ for all $a \in A$ and
every $y \le x$ with $y \not\le a$ for all $a \in A$ equals $x$.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsAntichainRowmotion`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#is-antichain-rowmotion).

## Type-A root poset

A partially ordered set $P$ is a type-A root poset of rank $n$, for a
natural number $n$, when there is a bijection $a \mapsto (i_a, j_a)$ from $P$ onto the set of
pairs $(i, j)$ of integers with $0 \le i \le j < n$ such that $a \le b$ holds exactly when the
interval $[i_a, j_a]$ is contained in $[i_b, j_b]$, that is, $i_b \le i_a$ and $j_a \le j_b$.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.IsTypeARootPoset`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#is-type-aroot-poset).

## Type-A rowmotion homomesy conjecture

The proposition that for every natural number $n$,
every finite partially ordered set $P$ that is a type-A root poset of rank $n$ (there is a
bijection $a \mapsto (i_a, j_a)$ from $P$ onto the set of pairs $(i, j)$ of integers with
$0 \le i \le j < n$ such that $a \le b$ holds exactly when $i_b \le i_a$ and $j_a \le j_b$), and
every bijection $\rho$ of the set of finite antichains of $P$ that sends each antichain $A$ to the
set of minimal elements of the complement of the down-set of $A$, the set of finite antichains of
$P$ is finite, $\rho$ is bijective, and for every antichain $A$ and every $k > 0$ with
$\rho^k(A) = A$ the average $\frac{1}{k} \sum_{i=0}^{k-1} |\rho^i(A)|$ equals $n/2$.

## Sources

- [AIM-OTHER-0019] Conjecture 3.3 (aim-other-notes.json notes[18]; http://aimath.org/pastworkshops/dac_preworkshop.pdf).

Formalized by `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#conjecture).

## Antichain size is homomesic under type-A rowmotion

Let $n$ be a natural number and let $P$
be a finite partially ordered set that is a type-A root poset of rank $n$: there is a bijection
$a \mapsto (i_a, j_a)$ from $P$ onto the set of pairs $(i, j)$ of integers with $0 \le i \le j < n$
such that $a \le b$ holds exactly when $[i_a, j_a] \subseteq [i_b, j_b]$, that is, $i_b \le i_a$
and $j_a \le j_b$. Let $\rho$ be a bijection of the set of finite antichains of $P$ such that,
for every antichain $A$, $\rho(A)$ is the set of minimal elements of the complement of the
down-set of $A$. Then the set of finite antichains of $P$ is finite, $\rho$ is bijective, and for
every antichain $A$ and every $k > 0$ with $\rho^k(A) = A$,

$$\frac{1}{k} \sum_{i=0}^{k-1} |\rho^i(A)| = \frac{n}{2}.$$

This is the type-A case of Panyushev's conjecture on antichain orbits in root posets, which
Armstrong, Stump, and Thomas proved for all crystallographic root systems.

## Sources

- D. Armstrong, C. Stump, and H. Thomas, A uniform bijection between nonnesting and noncrossing partitions, Transactions of the American Mathematical Society 365 (2013).

Stated but not proved: `MathlibExt.Combinatorics.RootPosetRowmotionHomomesyWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RootPosetRowmotionHomomesyWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rowmotion on root posets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/rowmotion-on-root-posets)
