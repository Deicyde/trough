---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.pricingScan, Cslib.Algorithms.Lean.TimeM.pricingVertexCover, Cslib.Algorithms.Lean.TimeM.pricingScan_residual, Cslib.Algorithms.Lean.TimeM.pricingScan_covers, Cslib.Algorithms.Lean.TimeM.sum_drop_le_two_mul_price, Cslib.Algorithms.Lean.TimeM.price_le_sum_drop, Cslib.Algorithms.Lean.TimeM.pricingVertexCover_covers, Cslib.Algorithms.Lean.TimeM.pricingVertexCover_isVertexCover
statement: formalized
proof: formalized
---

# Weighted vertex cover by the pricing method

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html).

## Pricing scan

Given rational residual weights $r$ on the vertices, a rational total
price $P$ and a list of edges (ordered pairs of vertices), the pricing scan processes the
edges in order: an edge $(u, v)$ has price $\delta = \min(r(u), r(v))$, which is subtracted
from the residual weight of $u$ and of $v$ (once if $u = v$) and added to the total price.
The result is the final pair of residual weights and total price, and the scan costs one
time unit per edge.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingScan`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-scan).

## Pricing method for weighted vertex cover

Given rational weights $w$ on a finite vertex
set $V$ and a list of edges (ordered pairs of vertices), run the pricing scan on the list
starting from residual weights $w$ and total price $0$, then return the set of vertices whose
final residual weight is $0$. On top of the cost of the scan, the selection costs $|V|$ time
units.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingVertexCover`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-vertex-cover).

## Pricing scan: residual weights stay between $0$ and their start

Let $r$ be rational
residual weights with $r(v) \ge 0$ for every vertex $v$, let $P$ be a rational number and
let $L$ be a list of edges. If the pricing scan of $L$ from residual weights $r$ and total
price $P$ ends with residual weights $r'$, then $0 \le r'(v) \le r(v)$ for every vertex $v$.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingScan_residual`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-scan-residual).

## Pricing scan: every edge has an exhausted endpoint

Let $r$ be rational residual
weights with $r(v) \ge 0$ for every vertex $v$, let $P$ be a rational number and let $L$ be
a list of edges (ordered pairs of vertices). If the pricing scan of $L$ from residual
weights $r$ and total price $P$ ends with residual weights $r'$, then every pair $(u, v)$
in $L$ has $r'(u) = 0$ or $r'(v) = 0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingScan_covers`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-scan-covers).

## Pricing scan: the vertices pay at most twice the price

Let $V$ be a finite vertex set,
let $r$ be rational residual weights with $r(v) \ge 0$ for every vertex $v$, let $P$ be a
rational number and let $L$ be a list of edges. If the pricing scan of $L$ from residual
weights $r$ and total price $P$ ends with residual weights $r'$ and total price $P'$, then
$\sum_{v \in V} (r(v) - r'(v)) \le 2 (P' - P)$.

Each edge's price is paid by its two endpoints.

Formalized by `Cslib.Algorithms.Lean.TimeM.sum_drop_le_two_mul_price`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#sum-drop-le-two-mul-price).

## Pricing scan: the total price is at most what a cover pays

Let $C$ be a finite
set of vertices, let $r$ be rational residual weights with $r(v) \ge 0$ for every vertex
$v$, let $P$ be a rational number, and let $L$ be a list of edges (ordered pairs of
vertices) such that every pair $(u, v)$ in $L$ has $u \in C$ or $v \in C$. If the pricing
scan of $L$ from residual weights $r$ and total price $P$ ends with residual weights $r'$
and total price $P'$, then $P' - P \le \sum_{v \in C} (r(v) - r'(v))$.

Every edge has an endpoint in $C$, which pays that edge's price.

Formalized by `Cslib.Algorithms.Lean.TimeM.price_le_sum_drop`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#price-le-sum-drop).

## The pricing method covers every listed edge

Let $w$ be rational weights on a finite
vertex set with $w(v) \ge 0$ for every vertex $v$, and let $L$ be a list of edges (ordered
pairs of vertices). For every pair $(u, v)$ in $L$, $u$ or $v$ belongs to the set returned
by the pricing method on $w$ and $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingVertexCover_covers`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-vertex-cover-covers).

## The pricing method returns a vertex cover

Let $G$ be a simple graph on a finite
vertex set, let $w$ be rational vertex weights with $w(v) \ge 0$ for every vertex $v$, and
let $L$ be a list of ordered pairs of vertices such that for every edge $uv$ of $G$, the
pair $(u, v)$ or the pair $(v, u)$ is in $L$. Then the set returned by the pricing method on
$w$ and $L$ is a vertex cover of $G$.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingVertexCover_isVertexCover`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-vertex-cover-is-vertex-cover).

## The pricing method weighs at most twice any cover of the listed edges

Let $w$ be
rational weights on a finite vertex set with $w(v) \ge 0$ for every vertex $v$, let $L$ be a
list of edges (ordered pairs of vertices), and let $C$ be a set of vertices such that every
pair $(u, v)$ in $L$ has $u \in C$ or $v \in C$. Then the total weight of the set returned by
the pricing method on $w$ and $L$ is at most $2 \sum_{v \in C} w(v)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingVertexCover_weight_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-vertex-cover-weight-le).

## Running time of the pricing method

For all rational vertex weights $w$ on a finite
vertex set $V$ and every list $L$ of edges, the pricing method on $w$ and $L$ takes exactly
$|L| + |V|$ time units, where $|L|$ is the length of the list: one unit per listed edge and
one per vertex.

Formalized by `Cslib.Algorithms.Lean.TimeM.pricingVertexCover_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/WeightedVertexCover.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html#pricing-vertex-cover-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted vertex cover by the pricing method](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/approximation-algorithms/weighted-vertex-cover-by-the-pricing-method)
