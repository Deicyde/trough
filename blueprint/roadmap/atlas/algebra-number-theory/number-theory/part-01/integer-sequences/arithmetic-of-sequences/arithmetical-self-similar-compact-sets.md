---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSelfSimilarCompactSet, MetaMathlibExt.IsSelfSimilarCompactSet.smul_derivedSet_iterate, MetaMathlibExt.selfSimilarLayer, MetaMathlibExt.selfSimilarLayer_zero, MetaMathlibExt.selfSimilarLayer_succ, MetaMathlibExt.isSelfSimilarCompactSet_enumeration, MetaMathlibExt.isSelfSimilarCompactSet_eq_union_layers, MetaMathlibExt.isSelfSimilarCompactSet_derivedSet_enum
statement: formalized
---

# Arithmetical self-similar compact sets

28 results, 17 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html).

## Self-similar compact set

Let $\mu$ be a natural number and $\rho$ a real number. A set
$K \subseteq \mathbb{R}$ is a self-similar compact set of module $\mu$ and ratio $\rho$ when
$\rho > 1$, $K$ is nonempty and compact, $K \subseteq [0, \infty)$, $K$ is well ordered by the
reverse order $x \preceq y \iff x \ge y$ (every nonempty subset of $K$ has a largest element),
and $\rho K^{(\mu)} = K$, where $K^{(\mu)}$ is the $\mu$-th derived set of $K$ (the operation
$A \mapsto A'$ taking a set to its set of accumulation points, applied $\mu$ times) and
$\rho K^{(\mu)} = \{\rho x : x \in K^{(\mu)}\}$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 1.

Formalized by `MetaMathlibExt.IsSelfSimilarCompactSet`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set).

## Self-similarity equation

If $K \subseteq \mathbb{R}$ is a self-similar compact set of
module $\mu$ and ratio $\rho$, then $\rho K^{(\mu)} = K$, where $K^{(\mu)}$ is the $\mu$-th derived
set of $K$ (the set of accumulation points, iterated $\mu$ times) and $\rho K^{(\mu)}$ is its
image under multiplication by $\rho$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 1, equation (1).

Formalized by `MetaMathlibExt.IsSelfSimilarCompactSet.smul_derivedSet_iterate`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#smul-derived-set-iterate).

## Layers of the iterated derived sets

For a set $K \subseteq \mathbb{R}$ and a natural
number $u$, let $K^{(u)}$ be the $u$-th derived set of $K$ (the derived set, i.e. the set of
accumulation points, iterated $u$ times, with $K^{(0)} = K$). The layer of $K$ of index $u$ is
$T_u = K^{(u)} \setminus K^{(u+1)}$, the set of points of $K^{(u)}$ that are isolated in
$K^{(u)}$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 2.

Formalized by `MetaMathlibExt.selfSimilarLayer`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#self-similar-layer).

## The zeroth layer is the set of isolated points

For every set
$K \subseteq \mathbb{R}$, the layer $T_0$ of $K$ equals $K \setminus K'$, where $K'$ is the derived
set of $K$ (its set of accumulation points); that is, $T_0$ is the set of isolated points of $K$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 2.

Formalized by `MetaMathlibExt.selfSimilarLayer_zero`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#self-similar-layer-zero).

## Layers of the derived set

For a set $A \subseteq \mathbb{R}$ and $u \ge 0$, write
$T_u(A) = A^{(u)} \setminus A^{(u+1)}$ for the $u$-th layer of $A$, where $A^{(u)}$ is the $u$-th
derived set of $A$. Then for every set $K \subseteq \mathbb{R}$ and every $u \ge 0$,
$T_{u+1}(K) = T_u(K')$, where $K'$ is the derived set of $K$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, proof of Proposition 7.

Formalized by `MetaMathlibExt.selfSimilarLayer_succ`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#self-similar-layer-succ).

## Order type of a self-similar compact set

Let $K$ be a self-similar compact set of module
$\mu \ge 1$ and ratio $\rho$. Then there is a strictly decreasing map $\alpha \mapsto K[\alpha]$
from the ordinals $\alpha \le \omega^\omega$ onto $K$ (so $K$ has order type $\omega^\omega + 1$
under the reverse order) with $K[\omega^\omega] = 0$, $K[0] > 0$ and $K \subseteq [0, K[0]]$.

The hypothesis $\mu \ge 1$ is the paper's convention that $\mu$ is a natural number; for
$\mu = 0$ the set $\{0\}$ would satisfy the definition.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 1.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_enumeration` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-enumeration).

## Decomposition of a self-similar compact set into layers

Let $K$ be a self-similar
compact set of module $\mu$ and ratio $\rho$, and for $u \ge 0$ let
$T_u = K^{(u)} \setminus K^{(u+1)}$, where $K^{(u)}$ is the $u$-th derived set of $K$. Then

$$K = \{0\} \cup \bigcup_{n \ge 0} \bigcup_{0 \le u < \mu} \rho^{-n} T_u,$$

where $\rho^{-n} T_u = \{\rho^{-n} x : x \in T_u\}$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 2, equation (2).

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_eq_union_layers` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-eq-union-lay).

## Enumerating the derived sets of a self-similar compact set

Let $K$ be a self-similar
compact set of module $\mu$ and ratio $\rho$, let $n \ge 1$, and write $K^{(n)}$ for the $n$-th
derived set of $K$. Let $\alpha \mapsto K[\alpha]$ and $\alpha \mapsto K^{(n)}[\alpha]$ be
strictly decreasing maps from the ordinals $\alpha \le \omega^\omega$ onto $K$ and onto
$K^{(n)}$, respectively. Then $K^{(n)}[\alpha] = K[\omega^n (1 + \alpha)]$ (ordinal
arithmetic) for every ordinal $\alpha \le \omega^\omega$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 3.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_derivedSet_enum` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-derived-set).

## Enumerating the isolated points of a self-similar compact set

Let $K$ be a self-similar
compact set of module $\mu$ and ratio $\rho$, and let $T_0 = K \setminus K'$ be the set of
isolated points of $K$, where $K'$ is the derived set of $K$. Let $\alpha \mapsto K[\alpha]$ be a
strictly decreasing map from the ordinals $\alpha \le \omega^\omega$ onto $K$, and
$\alpha \mapsto T_0[\alpha]$ a strictly decreasing map from the ordinals $\alpha < \omega^\omega$
onto $T_0$. Then for every ordinal $\alpha < \omega^\omega$, $T_0[\alpha] = K[\alpha]$ if
$\alpha < \omega$, and $T_0[\alpha] = K[\alpha + 1]$ if $\omega \le \alpha$.

The paper writes $0 \le \alpha \le \omega^\omega$; the layer has order type $\omega^\omega$ (its
indices in $K$ are $0$ and the successor ordinals below $\omega^\omega$), so $T_0[\omega^\omega]$
is undefined and the range here is $\alpha < \omega^\omega$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 3.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_layer_zero_enum` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-layer-zero-e).

## Enumerating the higher layers of a self-similar compact set

Let $K$ be a self-similar
compact set of module $\mu$ and ratio $\rho$, let $u \ge 1$, and let
$T_u = K^{(u)} \setminus K^{(u+1)}$, where $K^{(u)}$ is the $u$-th derived set of $K$. Let
$\alpha \mapsto K[\alpha]$ be a strictly decreasing map from the ordinals $\alpha \le \omega^\omega$
onto $K$, and $\alpha \mapsto T_u[\alpha]$ a strictly decreasing map from the ordinals
$\alpha < \omega^\omega$ onto $T_u$. Then $T_u[\alpha] = K[\omega^u (\alpha + 1)]$ (ordinal
arithmetic) for every ordinal $\alpha < \omega^\omega$.

The paper writes $0 \le \alpha \le \omega^\omega$; the layer has order type $\omega^\omega$, so the
range here is $\alpha < \omega^\omega$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 3.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_layer_enum` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-layer-enum).

## Limits between consecutive layers of a self-similar compact set

Let $K$ be a
self-similar compact set of module $\mu$ and ratio $\rho$, with layers
$T_u = K^{(u)} \setminus K^{(u+1)}$ for $u \ge 0$, where $K^{(u)}$ is the $u$-th derived set of
$K$. Suppose that for every $u$, $\alpha \mapsto T_u[\alpha]$ is a strictly decreasing map from
the ordinals $\alpha < \omega^\omega$ onto $T_u$. Then for every $u \ge 0$ and every ordinal
$\alpha < \omega^\omega$, $T_u[\omega \alpha + n] \to T_{u+1}[\alpha]$ as $n \to \infty$ through
the natural numbers (ordinal arithmetic in the index).

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 4.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_layer_enum_tendsto` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-layer-enum-t).

## Limits across the last layer of a self-similar compact set

Let $K$ be a self-similar
compact set of module $\mu$ and ratio $\rho$, with layers $T_u = K^{(u)} \setminus K^{(u+1)}$
for $u \ge 0$, where $K^{(u)}$ is the $u$-th derived set of $K$. Suppose that for every $u$,
$\alpha \mapsto T_u[\alpha]$ is a strictly decreasing map from the ordinals $\alpha < \omega^\omega$
onto $T_u$. Then for every ordinal $\alpha < \omega^\omega$,
$T_{\mu-1}[\omega \alpha + n] \to T_0[\alpha] / \rho$ as $n \to \infty$ through the natural numbers
(ordinal arithmetic in the index).

These hypotheses force $\mu \ge 1$, so $\mu - 1$ is a genuine index.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 4.

Stated but not proved: `MetaMathlibExt.isSelfSimilarCompactSet_layer_enum_tendsto_last` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-layer-enum-t-2).

## Quasi-arithmetical compact sets

Let $K \subseteq \mathbb{R}$ and let $\mu$ and $\rho$ be
natural numbers. Then $K$ is a quasi-arithmetical compact set of module $\mu$ and ratio $\rho$
when $\rho \ge 2$, $K$ is a self-similar compact set of module $\mu$ and ratio $\rho$, and there
is a function $\kappa : \mathbb{N} \to \mathbb{N}$ such that
$K \setminus \{0\} = \{n / \rho^k : n, k \in \mathbb{N},\ \rho \nmid n,\ k \ge \kappa(n)\}$.

The paper's $\kappa$ is defined only on $\mathbb{N} \setminus \rho\mathbb{N}$; here its values at
multiples of $\rho$ are irrelevant.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 2.

Formalized by `MetaMathlibExt.IsQuasiArithmeticalCompactSet`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-quasi-arithmetical-compact-set).

## Quasi-arithmetical compact sets are self-similar

If $K$ is a quasi-arithmetical compact
set of module $\mu$ and natural-number ratio $\rho$, then $K$ is a self-similar compact set of
module $\mu$ and ratio $\rho$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 2.

Formalized by `MetaMathlibExt.IsQuasiArithmeticalCompactSet.isSelfSimilarCompactSet`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-self-similar-compact-set-2).

## The layer index of a quasi-arithmetical compact set is well defined (Proposition 5)

Let
$K \subseteq \mathbb{R}$ be a quasi-arithmetical compact set of module $\mu$ and ratio $\rho$. For
each natural number $j$ let $K^{(j)}$ be the $j$-th iterated derived set of $K$ and
$T_j = K^{(j)} \setminus K^{(j+1)}$ its $j$-th layer. If $n, p, q, v, w$ are natural numbers with
$n / \rho^p \in T_v$ and $n / \rho^q \in T_w$, then $p \mu - v = q \mu - w$ as integers.

The paper takes $n$ positive; $n = 0$ is allowed here, and then the claim is vacuous because $0$
lies in no layer.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 5.

Stated but not proved: `MetaMathlibExt.isQuasiArithmeticalCompactSet_layer_index` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-quasi-arithmetical-compact-set-layer).

## Multiplying by the ratio raises the gauge index by the module (Proposition 6)

Let
$K \subseteq \mathbb{R}$ be a quasi-arithmetical compact set of module $\mu$ and ratio $\rho$. For
each natural number $j$ let $K^{(j)}$ be the $j$-th iterated derived set of $K$ and
$T_j = K^{(j)} \setminus K^{(j+1)}$ its $j$-th layer. If $n, \ell, u, \ell', u'$ are natural
numbers with $n / \rho^\ell \in T_u$ and $\rho n / \rho^{\ell'} \in T_{u'}$, then
$\ell' \mu - u' = \ell \mu - u + \mu$ as integers.

The stability gauge of Definition 3 is $\lVert m \rVert_K = \ell \mu + d - u$ whenever
$m / \rho^\ell \in T_u$, with a displacement $d$ independent of $m$; so this is the identity
$\lVert \rho n \rVert_K = \lVert n \rVert_K + \mu$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 6.

Stated but not proved: `MetaMathlibExt.isQuasiArithmeticalCompactSet_gauge_ratio_mul` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-quasi-arithmetical-compact-set-gauge).

## Un-normalized stability gauge

Let $K \subseteq \mathbb{R}$, let $\mu$, $\rho$ and $n$ be
natural numbers, and let $T_u$ denote the layer of $K$ of index $u$. Let $\ell$ be the least
natural number such that $n / \rho^\ell$ lies in some layer $T_u$ (division by $0$ gives $0$), and
let $u$ be the least index with $n / \rho^\ell \in T_u$. The un-normalized stability gauge of $n$
is the integer $\ell \mu - u$. If $n / \rho^\ell$ lies in no layer for any $\ell$, its value is $0$.

When $K$ is a quasi-arithmetical compact set of module $\mu$ and ratio $\rho$, Proposition 5 of the
source says that $\ell \mu - u$ is the same for every $\ell$ and $u$ with $n / \rho^\ell \in T_u$;
taking the least $\ell$ only fixes a choice.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 3.

Formalized by `MetaMathlibExt.stabilityGaugeIndex`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#stability-gauge-index).

## Stability gauge

Let $K \subseteq \mathbb{R}$, let $\mu$ and $\rho$ be natural numbers, and
for a natural number $n$ let $g(n)$ be the un-normalized stability gauge of $n$ for $K$, $\mu$
and $\rho$: the integer $\ell \mu - u$, where $\ell$ is least such that $n / \rho^\ell$ lies in
some layer $T_u$ of $K$ and $u$ is the least such index (and $g(n) = 0$ if there is no such
$\ell$). The stability gauge of $n$ is the integer $\lVert n \rVert_K = g(n) - g(1)$. When such
an $\ell$ exists, this is $\ell \mu + d - u$ with the displacement $d = -g(1)$, chosen so that
$\lVert 1 \rVert_K = 0$.

The source defines the gauge only for quasi-arithmetical compact sets of module $\mu$ and ratio
$\rho$; this definition applies to every set $K$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 3.

Formalized by `MetaMathlibExt.stabilityGauge`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#stability-gauge).

## The stability gauge vanishes at one

For every set $K \subseteq \mathbb{R}$ and all
natural numbers $\mu$ and $\rho$, the stability gauge $n \mapsto \lVert n \rVert_K$ of $K$ with
module $\mu$ and ratio $\rho$ takes the value $0$ at $n = 1$, that is, $\lVert 1 \rVert_K = 0$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 3.

Formalized by `MetaMathlibExt.stabilityGauge_one`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#stability-gauge-one).

## Arithmetical compact sets

Let $K \subseteq \mathbb{R}$ and let $\mu$ and $\rho$ be natural
numbers. For each natural number $j$ let $K^{(j)}$ be the $j$-th iterated derived set (the set of
accumulation points, iterated $j$ times) of $K$ and $T_j = K^{(j)} \setminus K^{(j+1)}$ its $j$-th
layer, and for a natural number $m$ let $\lVert m \rVert_K$ be the stability gauge of $K$ with
module $\mu$ and ratio $\rho$ at $m$. Then $K$ is an arithmetical compact set of module $\mu$ and
ratio $\rho$ when $K$ is a quasi-arithmetical compact set of module $\mu$ and ratio $\rho$ and the
following holds for every family of maps $\alpha \mapsto T_j[\alpha]$ ($j \in \mathbb{N}$), each
strictly decreasing on the ordinals $\alpha < \omega^\omega$ and mapping them onto $T_j$: for every
$j \in \mathbb{N}$, every ordinal $\alpha < \omega^\omega$ and all natural numbers $n$ and $k$ with
$\rho \nmid n$ and $T_{j+1}[\alpha] = n / \rho^k$, the sets
$\{T_j[\omega \alpha + r] : r \in \mathbb{N}\}$ and
$\{b (a \rho^r + 1) / \rho^{r+k} : a, b, r \in \mathbb{N},\ n = ab,\
\lVert n \rVert_K = \lVert a \rVert_K + \lVert b \rVert_K\}$ have finite symmetric difference.

Such an enumeration of a layer is unique when it exists; by Proposition 3 each layer has order
type $\omega^\omega$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 4, displays (4) and (5).

Formalized by `MetaMathlibExt.IsArithmeticalCompactSet`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-arithmetical-compact-set).

## Arithmetical compact sets are quasi-arithmetical

If $K \subseteq \mathbb{R}$ is an
arithmetical compact set of module $\mu$ and ratio $\rho$, then $K$ is a quasi-arithmetical
compact set of module $\mu$ and ratio $\rho$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Definition 4.

Formalized by `MetaMathlibExt.IsArithmeticalCompactSet.isQuasiArithmeticalCompactSet`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-quasi-arithmetical-compact-set-2).

## Derived sets of an arithmetical compact set are arithmetical (Proposition 7)

Let $K$ be
an arithmetical compact set of module $\mu$ and ratio $\rho$. For every natural number $n$, the
$n$-th derived set $K^{(n)}$ of $K$ (the set of accumulation points, iterated $n$ times, so that
$K^{(0)} = K$) is an arithmetical compact set of module $\mu$ and ratio $\rho$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Proposition 7.

Stated but not proved: `MetaMathlibExt.isArithmeticalCompactSet_derivedSet_iterate` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-arithmetical-compact-set-derived-set).

## Stable numbers for integer complexity

A natural number $n$ is stable when $n > 0$ and
$\lVert 3^k n \rVert = \lVert n \rVert + 3k$ for every natural number $k$, where $\lVert m \rVert$
is the integer complexity of $m$.

The paper quantifies over $k \ge 1$; the case $k = 0$ holds trivially.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Section 1.

Formalized by `MetaMathlibExt.IsComplexityStable`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-complexity-stable).

## Stable complexity

For a natural number $n$, let $\lVert m \rVert$ denote the integer
complexity of a positive integer $m$, with $\lVert 0 \rVert = 0$, and let $a$ be the least natural
number such that $3^a n$ is stable, with $a = 0$ if there is none. The stable complexity of $n$
is the integer $\lVert n \rVert_{\mathrm{st}} = \lVert 3^a n \rVert - 3a$.

Altman and Zelinsky show that such an $a$ exists for $n \ge 1$, and any larger $a$ gives the
same value. For $n = 0$ there is none, so $\lVert 0 \rVert_{\mathrm{st}} = \lVert 0 \rVert = 0$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Section 1.

Formalized by `MetaMathlibExt.stableComplexity`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#stable-complexity).

## Stable complexity of a stable number

If $n$ is a stable natural number, then its
stable complexity equals its integer complexity: $\lVert n \rVert_{\mathrm{st}} = \lVert n \rVert$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Section 1.

Formalized by `MetaMathlibExt.stableComplexity_of_isComplexityStable`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#stable-complexity-of-is-complexity-stabl).

## The set $T_0$ built from stable numbers

Write $\lVert n \rVert$ for the integer complexity
of a natural number $n$, and call $n$ stable when $n > 0$ and
$\lVert 3^k n \rVert = \lVert n \rVert + 3k$ for every natural number $k$. The set
$T_0 \subseteq \mathbb{R}$ consists of the reals $n / 3^k$, where $n$ and $k$ are natural numbers,
$n$ is stable and $\lVert n \rVert = 3k + 2$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Section 3, equation (7).

Formalized by `MetaMathlibExt.complexityLayerZero`, a definition declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#complexity-layer-zero).

## The set $T_0$ is nonnegative

Every element of the set $T_0$ of reals $n / 3^k$, where
$n$ and $k$ are natural numbers, $n$ is stable and $\lVert n \rVert = 3k + 2$ (with
$\lVert n \rVert$ the integer complexity of $n$), is a nonnegative real number.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Section 3, equation (7).

Formalized by `MetaMathlibExt.complexityLayerZero_subset_Ici`, a theorem declared in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#complexity-layer-zero-subset-ici).

## The closure of $T_0$ is an arithmetical compact set (Theorem 2)

Let $T_0$ be the set of
reals $n / 3^k$, where $n$ and $k$ are natural numbers, $n$ is stable and
$\lVert n \rVert = 3k + 2$ (with $\lVert n \rVert$ the integer complexity of $n$), and let $K$ be
the closure of $T_0$ in $\mathbb{R}$. Then $K$ is an arithmetical compact set of module $3$ and
ratio $3$, and for every natural number $n \ge 1$ the stability gauge $\lVert n \rVert_K$ of $K$
with module $3$ and ratio $3$ equals the stable complexity $\lVert n \rVert_{\mathrm{st}}$.

## Sources

- J. Arias de Reyna, *Arithmetical Self-Similar Compact Sets*, INTEGERS 24 (2024), Article A21, Theorem 2.

Stated but not proved: `MetaMathlibExt.isArithmeticalCompactSet_closure_complexityLayerZero` is written with `theorem_wanted` in [WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ArithmeticalSelfSimilarCompactSetWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html#is-arithmetical-compact-set-closure-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetical self-similar compact sets](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetical-self-similar-compact-sets)
