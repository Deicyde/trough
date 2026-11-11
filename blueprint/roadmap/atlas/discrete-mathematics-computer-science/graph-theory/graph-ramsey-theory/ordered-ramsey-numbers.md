---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.IsOrderedEmbedding, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.HasRedOrderedCopy, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.HasBlueOrderedCopy, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.OrderedRamseyProp, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.orderedRamseyNumber, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.conjecture, MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.conjecture_holds
statement: formalized
---

# Ordered Ramsey numbers

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html).

## Ordered embedding

Let $\lt _H$ be a strict total order on $\{0, \dots, n - 1\}$. A map
$f \colon \{0, \dots, n - 1\} \to \{0, \dots, N - 1\}$ is an ordered embedding when it is
injective and $a \lt _H b$ implies $f(a) < f(b)$ for all $a$ and $b$, where $\{0, \dots, N - 1\}$
carries its natural order.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.IsOrderedEmbedding`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#is-ordered-embedding).

## Red ordered copy

Let $H$ be a simple graph on $\{0, \dots, n - 1\}$ with a strict total
order $\lt _H$ on its vertices, and let $G$ be a simple graph on $\{0, \dots, N - 1\}$, the red
graph. Then $G$ contains a red ordered copy of $(H, \lt _H)$ when there is an ordered embedding $f$
of $(\{0, \dots, n - 1\}, \lt _H)$ into $\{0, \dots, N - 1\}$ such that $f(a)$ and $f(b)$ are
adjacent in $G$ whenever $a$ and $b$ are adjacent in $H$. The copy need not be induced.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.HasRedOrderedCopy`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#has-red-ordered-copy).

## Blue ordered copy

Let $H$ be a simple graph on $\{0, \dots, n - 1\}$ with a strict total
order $\lt _H$ on its vertices, and let $G$ be a simple graph on $\{0, \dots, N - 1\}$, the red
graph. Then $G$ admits a blue ordered copy of $(H, \lt _H)$ when there is an ordered embedding $f$
of $(\{0, \dots, n - 1\}, \lt _H)$ into $\{0, \dots, N - 1\}$ such that $f(a)$ and $f(b)$ are not
adjacent in $G$ whenever $a$ and $b$ are adjacent in $H$. Since $f$ is injective, these pairs are
edges of the blue graph, the complement of $G$. The copy need not be induced.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.HasBlueOrderedCopy`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#has-blue-ordered-copy).

## Ordered Ramsey property

Let $H$ be a simple graph on $\{0, \dots, n - 1\}$ with a strict
total order $\lt _H$ on its vertices. A natural number $N$ has the ordered Ramsey property for
$(H, \lt _H)$ when every simple graph $G$ on $\{0, \dots, N - 1\}$ contains a red ordered copy of
$(H, \lt _H)$ or admits a blue ordered copy of $(H, \lt _H)$. Equivalently, every red/blue colouring of
the edges of the complete graph on $\{0, \dots, N - 1\}$ with its natural order, with red edges
those of $G$, contains a monochromatic ordered copy of $(H, \lt _H)$.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.OrderedRamseyProp`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#ordered-ramsey-prop).

## Ordered Ramsey number

For a simple graph $H$ on $\{0, \dots, n - 1\}$ with a strict total
order $\lt _H$ on its vertices, the ordered Ramsey number $r_<(H, \lt _H)$ is the least natural number
$N$ with the ordered Ramsey property for $(H, \lt _H)$, that is, such that every red/blue colouring
of the edges of the complete graph on $\{0, \dots, N - 1\}$ with its natural order contains a
monochromatic ordered copy of $(H, \lt _H)$. It is $0$ if no such $N$ exists.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.orderedRamseyNumber`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#ordered-ramsey-number).

## Order-robust ordered Ramsey conjecture for 100-regular graphs

There are a real number
$c > 0$ and a natural number $N_0$ such that for every $n \ge N_0$ there is a $100$-regular simple
graph $H$ on $\{0, \dots, n - 1\}$ such that $r_<(H, \lt _H) \ge n^{1+c}$ for every strict total
order $\lt _H$ on its vertices, where $r_<(H, \lt _H)$ is the ordered Ramsey number of $H$ with the
order $\lt _H$.

This is the AIM question asking whether such a $c$ exists, stated as a claim.

## Sources

- [AIM-COMBINATORICS-0079] Order-robust ordered Ramsey numbers of regular graphs (aim-combinatorics-notes.json notes[78], Source item 32, Section: Ordered Ramsey numbers, Workshop: Graph Ramsey theory, https://www.overleaf.com/read/mnvcscjjysvg).

Formalized by `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#conjecture).

## The order-robust ordered Ramsey conjecture holds

There are a real number $c > 0$ and a
natural number $N_0$ such that for every $n \ge N_0$ there is a $100$-regular simple graph $H$ on
$\{0, \dots, n - 1\}$ such that $r_<(H, \lt _H) \ge n^{1+c}$ for every strict total order $\lt _H$ on
its vertices. Here $r_<(H, \lt _H)$ is the least $N$ such that every red/blue colouring of the edges
of the complete graph on $\{0, \dots, N - 1\}$ with its natural order contains a monochromatic
copy of $H$ (not necessarily induced) under an injective map sending $\lt _H$ into the natural
order, and $0$ if there is no such $N$.

Balko, Jelínek and Valtr prove that for every $d \ge 3$ almost every $d$-regular $n$-vertex
graph has ordered Ramsey number at least $n^{3/2-1/d}/(4 \log n \log \log n)$ under every vertex
ordering; for $d = 100$ this exceeds $n^{1+c}$ for any $c < 49/100$ and all large $n$.

## Sources

- M. Balko, V. Jelínek and P. Valtr, On ordered Ramsey numbers of bounded-degree graphs, arXiv:1606.05628, https://arxiv.org/abs/1606.05628.

Stated but not proved: `MathlibExt.Combinatorics.OrderRobustOrderedRamseyWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/OrderRobustOrderedRamseyWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordered Ramsey numbers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-ramsey-theory/ordered-ramsey-numbers)
