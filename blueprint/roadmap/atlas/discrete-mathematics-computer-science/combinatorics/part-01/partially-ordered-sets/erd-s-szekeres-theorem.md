---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Order.ErdosSzekeres.sub_one_lt_of_pos, MathlibExt.Combinatorics.Order.ErdosSzekeres.IsIncrSubseq, MathlibExt.Combinatorics.Order.ErdosSzekeres.IsDecrSubseq, MathlibExt.Combinatorics.Order.ErdosSzekeres.IsIncrEnd, MathlibExt.Combinatorics.Order.ErdosSzekeres.IsDecrEnd, MathlibExt.Combinatorics.Order.ErdosSzekeres.fin1_false, MathlibExt.Combinatorics.Order.ErdosSzekeres.singleton_incr, MathlibExt.Combinatorics.Order.ErdosSzekeres.singleton_decr
statement: formalized
proof: formalized
---

# Erdős–Szekeres theorem

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html).

## A positive natural number exceeds its predecessor

For every natural number $k > 0$,
$k - 1 < k$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.sub_one_lt_of_pos`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#sub-one-lt-of-pos).

## Increasing subsequence

For $f : \{0, \dots, N-1\} \to \mathbb{R}$ and $k \in \mathbb{N}$,
a map $\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ is an increasing subsequence of $f$ of
length $k$ when $\varphi(i) < \varphi(j)$ and $f(\varphi(i)) < f(\varphi(j))$ for all $i < j$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.IsIncrSubseq`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#is-incr-subseq).

## Decreasing subsequence

For $f : \{0, \dots, N-1\} \to \mathbb{R}$ and $k \in \mathbb{N}$,
a map $\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ is a decreasing subsequence of $f$ of
length $k$ when $\varphi(i) < \varphi(j)$ and $f(\varphi(j)) < f(\varphi(i))$ for all $i < j$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.IsDecrSubseq`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#is-decr-subseq).

## Increasing subsequence ending at a position

For $f : \{0, \dots, N-1\} \to \mathbb{R}$,
a position $p$ and $k \in \mathbb{N}$, this is the statement that $k \ge 1$ and $f$ has an
increasing subsequence $\varphi$ of length $k$ (indices and values strictly increasing) ending at
$p$, that is, with $\varphi(k-1) = p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.IsIncrEnd`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#is-incr-end).

## Decreasing subsequence ending at a position

For $f : \{0, \dots, N-1\} \to \mathbb{R}$,
a position $p$ and $k \in \mathbb{N}$, this is the statement that $k \ge 1$ and $f$ has a
decreasing subsequence $\varphi$ of length $k$ (indices strictly increasing and values strictly
decreasing) ending at $p$, that is, with $\varphi(k-1) = p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.IsDecrEnd`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#is-decr-end).

## No strict pair in a one-element set

There are no $i, j \in \{0\}$ with $i < j$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.fin1_false`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#fin1-false).

## One-term subsequences are increasing

For every real sequence $f$ indexed by
$\{0, \dots, N-1\}$ and every position $p$, the subsequence of length $1$ consisting of the term
at position $p$ is a strictly increasing subsequence of $f$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.singleton_incr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#singleton-incr).

## One-term subsequences are decreasing

For every real sequence $f$ indexed by
$\{0, \dots, N-1\}$ and every position $p$, the subsequence of length $1$ consisting of the term
at position $p$ is a strictly decreasing subsequence of $f$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.singleton_decr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#singleton-decr).

## Length of the longest increasing subsequence ending at a position

For
$f : \{0, \dots, N-1\} \to \mathbb{R}$ and a position $p$, this is the largest $k \le N$ such that
$f$ has an increasing subsequence of length $k$ ending at $p$, where indices and values both
increase strictly.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.incrLen`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#incr-len).

## Length of the longest decreasing subsequence ending at a point

For a real sequence $f$
indexed by $\{0, \dots, N-1\}$ and an index $p$, this is the largest $k$ such that $f$ has a
strictly decreasing subsequence of length $k$ ending at $p$, that is, indices
$i_1 < \dots < i_k = p$ with $f(i_1) > \dots > f(i_k)$. The maximum exists: $k = 1$ qualifies, and
every such $k$ is at most $N$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.decrLen`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#decr-len).

## Subsequences are no longer than the sequence

If
$\varphi \colon \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ is strictly increasing, that is
$\varphi(i) < \varphi(j)$ whenever $i < j$, then $k \le N$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.subseqLen_le`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#subseq-len-le).

## The longest increasing subsequence ending at a position is attained

For every
$f : \{0, \dots, N-1\} \to \mathbb{R}$ and every position $p$, $f$ has an increasing subsequence
ending at $p$ whose length equals the length of the longest increasing subsequence of $f$ ending
at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.incrLen_isEnd`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#incr-len-is-end).

## The longest decreasing subsequence ending at a point is attained

For every real sequence
$f$ indexed by $\{0, \dots, N-1\}$ and every index $p$, $f$ has a strictly decreasing subsequence
ending at $p$ whose length equals the length of the longest strictly decreasing subsequence of $f$
ending at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.decrLen_isEnd`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#decr-len-is-end).

## Bound by the longest increasing subsequence ending at a position

Let $f$ be a real
sequence indexed by $\{0, \dots, N-1\}$ and let $p$ be a position. If $f$ has a strictly
increasing subsequence of length $k$ ending exactly at $p$, then $k$ is at most the length of the
longest strictly increasing subsequence of $f$ ending at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.le_incrLen`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#le-incr-len).

## Bound by the longest decreasing subsequence ending at a position

Let $f$ be a real
sequence indexed by $\{0, \dots, N-1\}$ and let $p$ be a position. If $f$ has a strictly
decreasing subsequence of length $k$ ending exactly at $p$, then $k$ is at most the length of the
longest strictly decreasing subsequence of $f$ ending at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.le_decrLen`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#le-decr-len).

## Longest increasing subsequences ending at a position have length at least one

For every
$f : \{0, \dots, N-1\} \to \mathbb{R}$ and every position $p$, the length of the longest
increasing subsequence of $f$ ending at $p$ is at least $1$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.incrLen_ge_one`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#incr-len-ge-one).

## The longest decreasing subsequence ending at a point has length at least one

For every
real sequence $f$ indexed by $\{0, \dots, N-1\}$ and every index $p$, the length of the longest
strictly decreasing subsequence of $f$ ending at $p$ is at least $1$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.decrLen_ge_one`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#decr-len-ge-one).

## Appending an entry to a map of indices

Given
$\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ and $p \in \{0, \dots, N-1\}$, the appended map
on $\{0, \dots, k\}$ sends each $i < k$ to $\varphi(i)$ and sends $k$ to $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.extendMap`, a definition declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#extend-map).

## Entries of a strictly increasing index map lie at or below its last entry

Let $k \ge 1$
and let $\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ be strictly increasing with
$\varphi(k-1) = q$. Then $\varphi(i) \le q$ for every $i < k$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.idx_le_last`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#idx-le-last).

## The last value is the largest along a strictly increasing selection

Let $f$ be a real
sequence indexed by $\{0, \dots, N-1\}$, let $k \ge 1$, and let $\varphi$ map
$\{0, \dots, k-1\}$ to $\{0, \dots, N-1\}$ so that $f(\varphi(i)) < f(\varphi(j))$ whenever
$i < j < k$. If $\varphi(k-1) = q$, then $f(\varphi(i)) \le f(q)$ for every $i < k$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.val_le_last_incr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#val-le-last-incr).

## The last value is the smallest along a strictly decreasing selection

Let $f$ be a real
sequence indexed by $\{0, \dots, N-1\}$, let $k \ge 1$, and let $\varphi$ map
$\{0, \dots, k-1\}$ to $\{0, \dots, N-1\}$ so that $f(\varphi(j)) < f(\varphi(i))$ whenever
$i < j < k$. If $\varphi(k-1) = q$, then $f(q) \le f(\varphi(i))$ for every $i < k$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.last_le_val_decr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#last-le-val-decr).

## Appending a later index keeps indices increasing

Let $k \ge 1$ and let
$\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ be strictly increasing with last value
$\varphi(k-1) = q$. If $p$ is an index with $q < p$, then the map on $\{0, \dots, k\}$ obtained by
appending $p$ to $\varphi$, which sends each $i < k$ to $\varphi(i)$ and sends $k$ to $p$, is
strictly increasing.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.extend_idx`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#extend-idx).

## The last entry of an appended map

For every map
$\varphi : \{0, \dots, k-1\} \to \{0, \dots, N-1\}$ and every $p \in \{0, \dots, N-1\}$, the map
obtained by appending $p$ to $\varphi$ takes the value $p$ at its last index $k$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.extend_last`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#extend-last).

## Extending an increasing subsequence

Let $f : \{0, \dots, N-1\} \to \mathbb{R}$, let
$k \ge 1$, and let $\varphi$ be an increasing subsequence of $f$ of length $k$ (indices and values
strictly increasing) with last index $\varphi(k-1) = q$. If $p \in \{0, \dots, N-1\}$ satisfies
$q < p$ and $f(q) < f(p)$, then $f$ has an increasing subsequence of length $k + 1$ ending at
$p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.incrExtend`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#incr-extend).

## Extending a decreasing subsequence

Let $f$ be a real sequence indexed by
$\{0, \dots, N-1\}$, let $k \ge 1$, and let $\varphi$ be a decreasing subsequence of $f$ of length
$k$, that is, indices $\varphi(0) < \dots < \varphi(k-1)$ with
$f(\varphi(0)) > \dots > f(\varphi(k-1))$, whose last index is $\varphi(k-1) = q$. If $p$ is an
index with $q < p$ and $f(p) < f(q)$, then $f$ has a decreasing subsequence of length $k + 1$ that
ends at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.decrExtend`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#decr-extend).

## Longest increasing subsequence lengths increase strictly along increasing pairs

Let
$f : \{0, \dots, N-1\} \to \mathbb{R}$ and let $q < p$ be positions with $f(q) < f(p)$. Then the
length of the longest increasing subsequence of $f$ ending at $q$ is strictly less than the
length of the longest increasing subsequence of $f$ ending at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.incrMono`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#incr-mono).

## Longest decreasing subsequence lengths grow along a descent

Let $f$ be a real sequence
indexed by $\{0, \dots, N-1\}$, and let $q < p$ be indices with $f(p) < f(q)$. Then the length of
the longest strictly decreasing subsequence of $f$ ending at $q$ is strictly less than the length
of the longest strictly decreasing subsequence of $f$ ending at $p$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.decrMono`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#decr-mono).

## Increasing subsequences of every smaller length

Let $f$ be a real sequence indexed by
$\{0, \dots, N-1\}$. If $f$ has a strictly increasing subsequence of length $k$, then for every
$r \le k$ it has a strictly increasing subsequence of length $r$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.truncIncr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#trunc-incr).

## Decreasing subsequences of every smaller length

Let $f$ be a real sequence indexed by
$\{0, \dots, N-1\}$. If $f$ has a strictly decreasing subsequence of length $k$, then for every
$s \le k$ it has a strictly decreasing subsequence of length $s$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.truncDecr`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#trunc-decr).

## Erdős–Szekeres theorem

Let $r, s \ge 1$ be natural numbers, let $N = (r - 1)(s - 1) + 1$,
and let $f$ be an injective real sequence indexed by $\{0, \dots, N-1\}$. Then $f$ has a strictly
increasing subsequence of length $r$, that is, indices $i_1 < \dots < i_r$ with
$f(i_1) < \dots < f(i_r)$, or a strictly decreasing subsequence of length $s$, that is, indices
$j_1 < \dots < j_s$ with $f(j_1) > \dots > f(j_s)$.

Formalized by `MathlibExt.Combinatorics.Order.ErdosSzekeres.erdos_szekeres`, a theorem declared in [MathlibExt/Combinatorics/Order/ErdosSzekeres.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Order/ErdosSzekeres.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html#erdos-szekeres).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Szekeres theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/partially-ordered-sets/erd-s-szekeres-theorem)
