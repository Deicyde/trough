---
declaration: section
origin: cited
lean: TuranSystem.IsTuranSystem, TuranSystem.pos_of_isTuran, TuranSystem.lt_of_isTuran, TuranSystem.le_of_isTuran, TuranSystem.uniform_of_isTuran, TuranSystem.cover_of_isTuran, TuranSystem.completeGraph, TuranSystem.completeGraph_uniform
statement: formalized
proof: formalized
---

# Turán systems

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html).

## Turán system

Let $n$, $s$, $r$ be natural numbers. A family $H$ of subsets of
$\{0, 1, \dots, n-1\}$ is a Turán $(n, s, r)$-system when $0 < r < s \le n$, $H$ is
$r$-uniform (every member of $H$ has exactly $r$ elements), and every $s$-element subset of
$\{0, 1, \dots, n-1\}$ contains some member of $H$.

Formalized by `TuranSystem.IsTuranSystem`, a definition declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#is-turan-system).

## Turán systems have positive uniformity

Let $n$, $s$, $r$ be natural numbers and let $H$
be a Turán system with parameters $n$, $s$, $r$, whose definition includes $0 < r < s \le n$.
Then $0 < r$.

Formalized by `TuranSystem.pos_of_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#pos-of-is-turan).

## A Turán system has $r < s$

Let $n$, $s$, $r$ be natural numbers and let $H$ be a
Turán $(n, s, r)$-system. Then $r < s$.

Formalized by `TuranSystem.lt_of_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#lt-of-is-turan).

## A Turán system has $s \le n$

Let $n$, $s$, $r$ be natural numbers and let $H$ be a
Turán $(n, s, r)$-system. Then $s \le n$.

Formalized by `TuranSystem.le_of_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#le-of-is-turan).

## Turán systems are uniform

Let $n$, $s$, $r$ be natural numbers. If $H$ is a Turán system
with parameters $n$, $s$, $r$, then $H$ is $r$-uniform: every member of $H$ has exactly $r$
elements.

Formalized by `TuranSystem.uniform_of_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#uniform-of-is-turan).

## Turán systems cover every $s$-set

Let $n$, $s$, $r$ be natural numbers and let $H$ be a
Turán $(n, s, r)$-system. Then every $s$-element subset $T$ of $\{0, 1, \dots, n-1\}$ contains
some member $e$ of $H$.

Formalized by `TuranSystem.cover_of_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#cover-of-is-turan).

## The complete $r$-graph

For natural numbers $n$ and $r$, the complete $r$-graph on $n$
vertices is the family of all $r$-element subsets of $\{0, 1, \dots, n-1\}$.

Formalized by `TuranSystem.completeGraph`, a definition declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#complete-graph).

## The complete $r$-graph is $r$-uniform

For all natural numbers $n$ and $r$, every member
of the complete $r$-graph on $\{0, 1, \dots, n-1\}$ has exactly $r$ elements.

Formalized by `TuranSystem.completeGraph_uniform`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#complete-graph-uniform).

## The complete $r$-graph is a Turán system

Let $n$, $s$, $r$ be natural numbers with
$0 < r < s \le n$. Then the complete $r$-graph on $\{0, 1, \dots, n-1\}$ (the family of all its
$r$-element subsets) is a Turán $(n, s, r)$-system.

Formalized by `TuranSystem.completeGraph_isTuran`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#complete-graph-is-turan).

## Realized sizes of Turán systems

For natural numbers $n$, $s$, $r$, the set of realized
sizes is the set of natural numbers $k$ such that some Turán system with parameters $n$, $s$, $r$
on the vertex set $\{0, \dots, n-1\}$ has exactly $k$ members.

Formalized by `TuranSystem.realizedCounts`, a definition declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#realized-counts).

## Membership in the realized sizes

For natural numbers $n$, $s$, $r$, $k$, the number $k$
lies in the set of realized sizes for $(n, s, r)$ if and only if some Turán $(n, s, r)$-system
$H$ has exactly $k$ members.

Formalized by `TuranSystem.mem_realizedCounts`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#mem-realized-counts).

## Turán systems exist

For all natural numbers $n$, $s$, $r$ with $0 < r < s \le n$, there
is a Turán $(n, s, r)$-system.

Formalized by `TuranSystem.exists_system`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#exists-system).

## Some size of a Turán system is realized

For natural numbers $n$, $s$, $r$ with
$0 < r < s \le n$, the set of realized sizes for $n$, $s$, $r$ is nonempty: some natural number
$k$ is the number of members of a Turán system with parameters $n$, $s$, $r$.

Formalized by `TuranSystem.realizedCounts_nonempty`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#realized-counts-nonempty).

## Turán number

For natural numbers $n$, $s$, $r$, the Turán number $T(n, s, r)$ is the
least element of the set of realized sizes for $n$, $s$, $r$, that is, the least number of members
of a Turán system with parameters $n$, $s$, $r$, and $T(n, s, r) = 0$ if no such system exists.

Formalized by `TuranSystem.turanNumber`, a definition declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#turan-number).

## The Turán number is a realized size

Let $n$, $s$, $r$ be natural numbers with
$0 < r < s \le n$ and let $T(n, s, r)$ denote the Turán number. Then $T(n, s, r)$ belongs to the
set of realized sizes for $n$, $s$, $r$.

Formalized by `TuranSystem.turanNumber_mem`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#turan-number-mem).

## The Turán number is attained

Let $n$, $s$, $r$ be natural numbers with $0 < r < s \le n$
and let $T(n, s, r)$ denote the Turán number. Then some Turán system with parameters $n$, $s$,
$r$ has exactly $T(n, s, r)$ members.

Formalized by `TuranSystem.turanNumber_attains`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#turan-number-attains).

## Turán systems are at least as large as the Turán number

Let $n$, $s$, $r$ be natural
numbers and let $T(n, s, r)$ denote the Turán number. If $H$ is a Turán system with parameters
$n$, $s$, $r$, then $T(n, s, r) \le |H|$.

Formalized by `TuranSystem.turanNumber_le`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#turan-number-le).

## Lower bounds on the Turán number

Let $n$, $s$, $r$, $b$ be natural numbers with
$0 < r < s \le n$. If $b \le k$ for every $k$ in the set of realized sizes for $(n, s, r)$
(the sizes of Turán $(n, s, r)$-systems), then $b$ is at most the Turán number $T(n, s, r)$.

Formalized by `TuranSystem.le_turanNumber`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/TuranSystem.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/TuranSystem.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html#le-turan-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-systems)
