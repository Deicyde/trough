---
declaration: section
origin: cited
lean: MetaMathlibExt.meteredOutcome, MetaMathlibExt.meteredOutcome_one_two_ones, MetaMathlibExt.meteredOutcome_one_two_fail, MetaMathlibExt.meteredOutcome_example_six, MetaMathlibExt.IsMeteredParkingFunction, MetaMathlibExt.meteredParkingCount, MetaMathlibExt.meteredParkingCount_one_two_two, MetaMathlibExt.meteredLuckyCount
statement: formalized
---

# Metered parking functions

37 results, 13 proved and 24 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html).

## Outcome of the metered parking scheme

Let $t, n \in \mathbb{N}$, number the $n$ spots
$0, \dots, n-1$, and let $a_0, a_1, \dots, a_{m-1}$ be a list of preferences in $\mathbb{N}$.
Cars arrive in order, and car $i$ parks in the least spot $s$ with $a_i \le s < n$ that is not
taken by one of the previous $t$ cars (cars $\max(0, i - t), \dots, i - 1$) that parked; if
there is no such spot, car $i$ fails. The outcome is the list whose $i$-th entry is the spot of
car $i$, or a failure marker if car $i$ fails. Thus after car $j$ arrives, car $j - t$ leaves,
and only the cars among the last $t$ entries of the outcome so far occupy spots.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 1 (definition of the `t`-metered scheme) and Section 2 (definition of the outcome).

Formalized by `MetaMathlibExt.meteredOutcome`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-outcome).

## A 1-metered example in which every car parks

In the $1$-metered parking scheme on two
spots $\{0, 1\}$, if three cars arrive all preferring spot $0$, then they park in spots $0$, $1$
and $0$, in that order.

In the source's one-based numbering: preferences $(1, 1, 1)$ give spots $1, 2, 1$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, example after the definition of `t`-metered parking functions (Section 1).

Formalized by `MetaMathlibExt.meteredOutcome_one_two_ones`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-outcome-one-two-ones).

## A 1-metered example in which the third car fails

In the $1$-metered parking scheme on
two spots $\{0, 1\}$, if three cars arrive with preferences $0$, $0$, $1$, then the first two
cars park in spots $0$ and $1$ and the third car fails to park.

In the source's one-based numbering: with preferences $(1, 1, 2)$, car $3$ fails.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, example after the definition of `t`-metered parking functions (Section 1).

Formalized by `MetaMathlibExt.meteredOutcome_one_two_fail`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-outcome-one-two-fail).

## Metered outcomes of a seven-car example on six spots

On the six spots
$\{0, \dots, 5\}$, for seven cars with preferences $(2, 2, 2, 2, 3, 4, 5)$, the $2$-metered
parking scheme parks the cars in spots $(2, 3, 4, 2, 3, 4, 5)$, while in the $1$-metered scheme
the first six cars park in spots $(2, 3, 2, 3, 4, 5)$ and the seventh car fails to park.

In the source's one-based notation, where $O^t_n$ is the outcome of the $t$-metered scheme on
$n$ spots and $X$ marks a car that fails to park, $O^2_6(3,3,3,3,4,5,6) = (3,4,5,3,4,5,6)$ and
$O^1_6(3,3,3,3,4,5,6) = (3,4,3,4,5,6,X)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, example after the definition of the outcome (Section 2).

Formalized by `MetaMathlibExt.meteredOutcome_example_six`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-outcome-example-six).

## Metered parking function

Let $m, n, t \in \mathbb{N}$, number the $n$ spots
$0, \dots, n-1$, and let $f : \{0, \dots, m-1\} \to \{0, \dots, n-1\}$ give the preferred spot of
each of $m$ cars. In the $t$-metered scheme the cars arrive in the order $0, 1, \dots, m-1$, and
car $i$ parks in the least spot $s$ with $f(i) \le s \le n - 1$ that is not occupied by any of the
(at most $t$) cars that arrived just before car $i$; it fails to park if there is no such spot.
Then $f$ is a $t$-metered parking function if every car parks.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 1 (definition of `t`-metered parking functions).

Formalized by `MetaMathlibExt.IsMeteredParkingFunction`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function).

## Number of metered parking functions

For natural numbers $t$, $m$ and $n$,
$\mathrm{mpf}_{m,n}(t)$ is the number of $t$-metered $(m, n)$-parking functions, that is, of maps
$f$ from the $m$ cars $\{0, \dots, m-1\}$ to the $n$ spots $\{0, \dots, n-1\}$ under which every
car parks in the $t$-metered parking scheme.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 1 (definition and the notation `mpf_{m,n}(t)`).

Formalized by `MetaMathlibExt.meteredParkingCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count).

## 1-metered parking functions with two cars and two spots

The number of $1$-metered
$(2, 2)$-parking functions is $\mathrm{mpf}_{2,2}(1) = 3$.

This is an entry of the source's Table 1.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Table 1.

Formalized by `MetaMathlibExt.meteredParkingCount_one_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-one-two-two).

## Lucky cars in the metered scheme

For natural numbers $t$, $m$, $n$ and a preference
function $f : \{0, \dots, m - 1\} \to \{0, \dots, n - 1\}$ (car $i$ prefers spot $f(i)$), the
lucky count of $f$ under the $t$-metered parking scheme on $n$ spots is the number of cars $i$
that park in their preferred spot $f(i)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 2 (`lucky(α)`).

Formalized by `MetaMathlibExt.meteredLuckyCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-lucky-count).

## One step of the lace decomposition

Given a list of blocks (each a list of natural
numbers) and a natural number $a$: if the last block is $(p)$ with $a = p$, or the last block has
at least two entries and ends with $e$ where $a = e + 1$, then $a$ is appended to the last block;
otherwise, including when there is no block, a new block $(a)$ is added at the end.

Applied to a list of laces, where a lace is $(p)$ or $(p, p, p+1, \dots, p+\ell-2)$ for some
natural number $p$ and some length $\ell \ge 2$, this extends the last lace exactly when the
result is again a lace.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 3 (definitions of a lace and of the lace decomposition).

Formalized by `MetaMathlibExt.laceStep`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#lace-step).

## Lace decomposition

A lace is a sequence of natural numbers of the form $(p)$ or
$(p, p, p+1, \dots, p+\ell-2)$ for some natural number $p$ and some length $\ell \ge 2$. The lace
decomposition of a finite sequence $(a_1, \dots, a_k)$ of natural numbers is its partition into
blocks of consecutive entries built greedily from left to right: starting with no blocks, each
entry $a_i$ in turn is appended to the last block if the result is again a lace, and otherwise
starts a new block $(a_i)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 3 (definitions of a lace and of the lace decomposition).

Formalized by `MetaMathlibExt.laceDecomposition`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#lace-decomposition).

## Examples of lace decompositions

The lace decomposition of $(3, 3, 3, 3, 4, 6)$ is
$((3, 3), (3, 3, 4), (6))$, and the lace decomposition of $(4, 1, 2, 2, 3, 4, 5, 5, 1, 2)$ is
$((4), (1), (2, 2, 3, 4, 5), (5), (1), (2))$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 3, example after the definition of the lace decomposition.

Formalized by `MetaMathlibExt.laceDecomposition_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#lace-decomposition-examples).

## Window condition for metered parking functions

Number the cars $1, \dots, m$ and the
spots $1, \dots, n$, and let $a_k$ be the preferred spot of car $k$. If $(a_1, \dots, a_m)$ is a
$t$-metered $(m, n)$-parking function, then for every $i$ with $1 \le i \le n$ and every $j$ with
$1 \le j \le m - t$ (truncated subtraction, so there is no such $j$ when $m \le t$),

$$t + 1 + i \le \#\{k : j \le k \le j + t,\ a_k \le i\} + n,$$

that is, at least $t + 1 - n + i$ of the cars $j, \dots, j + t$ prefer one of the spots
$1, \dots, i$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 1.

Stated but not proved: `MetaMathlibExt.metered_window_count_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-window-count-ge).

## Vanishing of metered parking counts

Let $m, n, t$ be natural numbers with $m > n$ and
$t \ge n$. Then there are no $t$-metered $(m, n)$-parking functions, that is,
$\mathrm{mpf}_{m,n}(t) = 0$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 2.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_eq_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-eq-zero).

## Metered parking functions with a long meter are classical

Let $m \le n$ and
$t \ge m - 1$. A map $f : \{0, \dots, m-1\} \to \{0, \dots, n-1\}$ is a $t$-metered parking
function if and only if it is a partial parking function with $m$ cars and $n$ spots.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 3.

Stated but not proved: `MetaMathlibExt.isMeteredParkingFunction_iff_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-iff-of-le).

## Classical parking functions are metered parking functions

Let $m \le n$. Every partial
parking function $f$ with $m$ cars and $n$ spots is a $t$-metered parking function for every
$t \in \mathbb{N}$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 4.

Stated but not proved: `MetaMathlibExt.IsPartialParkingFunction.isMeteredParkingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-2).

## Displacement bound in the metered scheme

Let $t$, $m$, $n$ be natural numbers, let
$f : \{0, \dots, m - 1\} \to \{0, \dots, n - 1\}$ be a preference function and let $i < m$ be a
car. Under the $t$-metered parking scheme on $n$ spots, if car $i$ parks in spot $s$ then
$s \le f(i) + t$, that is, its displacement is at most $t$; and if car $i$ fails to park then
$f(i) + t \ge n$.

In the source's one-based numbering, with preference $a_i = f(i) + 1$, a car that fails to park
has $a_i \ge n - t + 1$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 5.

Stated but not proved: `MetaMathlibExt.meteredOutcome_displacement_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-outcome-displacement-le).

## Lower bound for the number of metered parking functions

For all natural numbers $t$,
$m$ and $n$, $\mathrm{mpf}_{m,n}(t) \ge (n - t)^m$, where $n - t$ is truncated subtraction
(equal to $0$ when $t \ge n$).

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 1.

Stated but not proved: `MetaMathlibExt.pow_sub_le_meteredParkingCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#pow-sub-le-metered-parking-count).

## Metered parking functions with two cars

For every natural number $t \ge 1$ and every
natural number $n$, the number of $t$-metered $(2, n)$-parking functions is
$\mathrm{mpf}_{2,n}(t) = \max(n^2 - 1, 0)$, that is, $n^2 - 1$ for $n \ge 1$ and $0$ for $n = 0$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 2.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-two).

## Lucky cars of 1-metered parking are the lace starts

Let $0 < m \le n$ and let
$\alpha = (a_1, \dots, a_m)$, with each $a_i \in \{1, \dots, n\}$, be any sequence of preferred
spots of $m$ cars on $n$ spots. Under the $1$-metered parking scheme, car $i$ is lucky (it parks
in its preferred spot $a_i$) if and only if position $i$ is the first position of one of the
laces of the lace decomposition $\mathrm{lace}(\alpha)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Lemma 1.

Stated but not proved: `MetaMathlibExt.one_metered_lucky_iff_lace_start` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#one-metered-lucky-iff-lace-start).

## One-metered parking functions and laces

Let $0 < m \le n$ and
$f : \{0, \dots, m-1\} \to \{0, \dots, n-1\}$. Then $f$ is a $1$-metered parking function if and
only if, in the lace decomposition of $(f(0), \dots, f(m-1))$, the last spot $n - 1$ occurs in
no lace other than as its first entry.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 1.

Stated but not proved: `MetaMathlibExt.isMeteredParkingFunction_one_iff_lace` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-one-iff-lace).

## One-metered parking functions with two spots

Let $m \ge 1$ and
$f : \{0, \dots, m-1\} \to \{0, 1\}$. Then $f$ is a $1$-metered parking function with $m$ cars and
$2$ spots if and only if every lace of the lace decomposition of $(f(0), \dots, f(m-1))$ that
contains the value $1$ has length $1$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 3.

Stated but not proved: `MetaMathlibExt.isMeteredParkingFunction_one_two_iff_lace` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-one-two-iff).

## Equal last-spot counts for 1-metered parking functions

Let $1 \le m \le j < k \le n$
and number the spots $1, \dots, n$. The number of $1$-metered $(m, n)$-parking functions whose
last car parks in spot $j$ equals the number of those whose last car parks in spot $k$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Lemma 2.

Stated but not proved: `MetaMathlibExt.one_metered_last_spot_card_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#one-metered-last-spot-card-eq).

## 1-metered parking functions whose last car parks in the last spot

Let $1 \le m \le n$
and number the spots $1, \dots, n$. The number of $1$-metered $(m, n)$-parking functions whose
last car parks in spot $n$ equals $\mathrm{mpf}_{m-1,n}(1)$, the number of $1$-metered
$(m - 1, n)$-parking functions.

The source leaves $1 \le m$ implicit (there is a last car).

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Lemma 3.

Stated but not proved: `MetaMathlibExt.one_metered_last_spot_n_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#one-metered-last-spot-n-card).

## Lucas-type recursion for 1-metered parking functions

Write $\mathrm{mpf}_{m,n}(1)$ for
the number of $1$-metered $(m, n)$-parking functions. For every natural number $n$,
$\mathrm{mpf}_{1,n}(1) = n$ and $\mathrm{mpf}_{0,n}(1) = 1$, and for every natural number $m$
with $1 \le m \le n$,

$$\mathrm{mpf}_{m+1,n}(1) = n \cdot \mathrm{mpf}_{m,n}(1) - \mathrm{mpf}_{m-1,n}(1),$$

where the subtraction is taken in the integers.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 2.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_one_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-one-recursion).

## 1-metered parking functions with as many cars as spots

For every natural number
$n > 2$, the number of $1$-metered $(n, n)$-parking functions is

$$\mathrm{mpf}_{n,n}(1) = \sum_{k=0}^{n} (n-2)^{n-k} \binom{2n+1-k}{k}.$$

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 4.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_one_diag` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-one-diag).

## Binet formula for 1-metered parking functions

Let $m, n$ be natural numbers with
$m \le n + 1$ and $n > 2$. Then the number $\mathrm{mpf}_{m,n}(1)$ of $1$-metered
$(m, n)$-parking functions satisfies, as real numbers,

$$\mathrm{mpf}_{m,n}(1) = \frac{n(n + \sqrt{n^2-4}) - 2}{n(n + \sqrt{n^2-4}) - 4}
\left(\frac{n + \sqrt{n^2-4}}{2}\right)^m +
\frac{n(n - \sqrt{n^2-4}) - 2}{n(n - \sqrt{n^2-4}) - 4}
\left(\frac{n - \sqrt{n^2-4}}{2}\right)^m.$$

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 5.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_one_binet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-one-binet).

## 1-metered parking functions with three cars

For every natural number $n \ge 2$, the
number of $1$-metered $(3, n)$-parking functions is $\mathrm{mpf}_{3,n}(1) = n^3 - 2n$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 7.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_one_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-one-three).

## Metered parking functions in which every car is lucky

Let $m \ge 2$, $n \ge 2$ and
$t \le m - 1$. The number of $t$-metered $(m, n)$-parking functions in which every car parks in
its preferred spot is $n(n-1)\cdots(n-t+1) \cdot (n-t)^{m-t}$, where the falling factorial
$n(n-1)\cdots(n-t+1)$ has $t$ factors (it equals $1$ for $t = 0$ and $0$ for $t > n$).

The source's companion formula (12) for exactly one lucky car is not stated: it is false as
printed when $m > n + 1$ (for $n = 2$, $m = 4$, $t = 1$ the count is $0$, while the formula
$(t-1)!\,(n-m+1)\,t^{m-t}$ gives $-1$).

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Proposition 8, Equation (13).

Stated but not proved: `MetaMathlibExt.metered_all_lucky_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-all-lucky-card).

## Closed form for (m-2)-metered parking functions

Let $m, n$ be natural numbers with
$2 < m \le n + 1$. Then the number $\mathrm{mpf}_{m,n}(m-2)$ of $(m-2)$-metered
$(m, n)$-parking functions is

$$(n-m+2)^2 (m-1)^{m-3} + \sum_{k=n-m+3}^{n} \binom{m-2}{n-k} (n-k+1)^{n-k-1} S_k,$$

where

$$S_k = \binom{k+1}{2}(n-m+2)\, k^{m-n+k-3} +
\left(k(n-m+1) - \binom{n-m+2}{2}\right)(k-n+m-1)^{k-n+m-3} +
\sum_{j=n-m+2}^{k-1} \left(jk - \binom{j+1}{2}\right) \binom{m-2-n+k}{k-1-j} (n-m+1)\,
j^{j+m-2-n} (k-j)^{k-j-2}.$$

Every subtraction is nonnegative on the summation ranges except in the exponents of the bases
$n - k + 1$ (at $k = n$) and $k - j$ (at $j = k - 1$), which equal $1$ there, so the formula is
the same with exponents truncated at $0$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 5.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_sub_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-sub-two).

## Parking functions with a given first entry

Let $1 \le m \le n$ and $1 \le j \le n$, and
number the spots $1, \dots, n$. Write

$$S(i) = \binom{m-1}{n-i} (n-m+1)\, i^{i+m-n-2} (n-i+1)^{n-i-1}.$$

If $j > n - m + 1$, the number of partial parking functions with $m$ cars and $n$ spots
(classical $(m, n)$-parking functions) whose first entry is $a_1 = j$ is $\sum_{i=j}^{n} S(i)$;
if $j \le n - m + 1$, it is $m^{m-2} + \sum_{i=n-m+2}^{n} S(i)$. Exponents are natural numbers
with truncated subtraction; the only affected powers are $1^{-1}$, at $i = n$ and at $m = 1$,
which equal the truncated $1^0$.

The text prints the factor $n - m + 1$ as $n - m - 1$, which is false ($m = n = 2$, $j = 1$: two
parking functions, formula $0$); the factor $n - m + 1$ is the one in the source's Lemma 4
($|\mathrm{Sh}_m(k-1, n-k)|$), from which the source derives this corollary, and it matches
exact counts.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 6.

Stated but not proved: `MetaMathlibExt.parkingFunction_first_entry_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#parking-function-first-entry-card).

## Metered parking functions with one spot fewer than cars

Let $m \ge 2$ be a natural
number. The number $\mathrm{mpf}_{m,m-1}(m-2)$ of $(m-2)$-metered $(m, m-1)$-parking functions
equals the sum, over all parking functions $f$ of length $m - 1$, of $f(0) + 1$ (the preferred
spot of the first car, with spots numbered from $1$), and it also equals

$$\sum_{i=1}^{m-1} \sum_{s=0}^{m-1-i} \binom{m-2}{s}\, i\, (s+1)^{s-1} (m-s-1)^{m-s-3}.$$

The only negative exponents occur at $s = 0$ and $s = m - 2$, where the base is $1$, so the
formula is the same with exponents truncated at $0$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Corollary 7.

Stated but not proved: `MetaMathlibExt.meteredParkingCount_sub_two_pred` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#metered-parking-count-sub-two-pred).

## Parking-function shuffles

Let $m'$, $n$, $k$ be natural numbers and let
$\pi : \{0, \dots, m' - 1\} \to \{0, \dots, n - 1\}$, with one-based letters $w_i = \pi(i) + 1$.
Then $\pi$ is a parking-function shuffle with parameters $(m', n, k)$ when all of the following
hold: no letter $w_i$ equals $k$; exactly $\max(m' + k - n, 0)$ letters satisfy $w_i < k$;
exactly $\max(n - k, 0)$ letters satisfy $w_i > k$; for every $s$ with $1 \le s \le k - 1$, at
most $k - s$ letters satisfy $s \le w_i \le k - 1$; and for every $s$ with $k + 1 \le s \le n$, at
most $n + 1 - s$ letters satisfy $w_i \ge s$.

With $m = m' + 1$, the word $(w_0, \dots, w_{m'-1})$ plays the role of the source's
$(\pi_2, \dots, \pi_m)$, and the conditions express membership in the source's set
$\mathrm{Sh}_m(k - 1, n - k)$ of shuffles of a parking function of $m - n + k - 1$ cars on
$k - 1$ spots (the letters below $k$) with a parking function of length $n - k$ shifted up by
$k$ (the letters above $k$): parking-function membership does not depend on the order of the
letters, and the last two conditions are the usual counting criterion for every car to park.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 4, Definition of `(m, n)`-parking function shuffles (`Sh_m(k - 1, n - k)`).

Formalized by `MetaMathlibExt.IsParkingShuffle`, a definition declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-parking-shuffle).

## An example of a parking-function shuffle

The word $(2, 6, 1, 0, 6, 1)$ with entries
in $\{0, \dots, 7\}$, which is $(3, 7, 2, 1, 7, 2)$ in one-based values, is a
$(7, 8)$-parking-function shuffle with parameter $k = 6$, that is, it lies in
$\mathrm{Sh}_7(5, 2)$. In one-based values it is a shuffle of the parking function
$(3, 2, 1, 2)$ with $4$ cars and $5$ spots and of $(7, 7) = (1, 1) + (6, 6)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Section 4, Example 5.

Formalized by `MetaMathlibExt.isParkingShuffle_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-parking-shuffle-example).

## Parking-function shuffles and the first entry

Let $1 \le m \le n$ and $1 \le k \le n$,
and let $w = (w_1, \dots, w_{m-1})$ be a word with entries in $\{0, \dots, n-1\}$. Then the set
of spots $j \in \{0, \dots, n-1\}$ for which $(j, w_1, \dots, w_{m-1})$ is a partial parking
function with $m$ cars and $n$ spots equals $\{0, \dots, k-1\}$ if and only if $w$ lies in the
set $\mathrm{Sh}_m(k - 1, n - k)$ of $(m, n)$-parking-function shuffles with parameter $k$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 3, with Definition 6 (the sets `A^n`).

Stated but not proved: `MetaMathlibExt.firstEntrySet_eq_iff_isParkingShuffle` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#first-entry-set-eq-iff-is-parking-shuffl).

## Number of parking-function shuffles

Let $1 \le m \le n$ and $1 \le k \le n$, and write
$\mathrm{Sh}_m(k - 1, n - k)$ for the set of $(m, n)$-parking-function shuffles with parameter
$k$, words of length $m - 1$ with entries in $\{0, \dots, n-1\}$. Then
$|\mathrm{Sh}_m(k - 1, n - k)|$ equals $\binom{m-1}{n-k}(n-m+1)\,k^{m-n+k-2}(n-k+1)^{n-k-1}$
if $k > n - m + 1$, equals $m^{m-2}$ if $k = n - m + 1$, and equals $0$ if $k < n - m + 1$.
The exponent $-1$ occurs only on the base $1$ (at $k = n$, and at $m = 1$), and $1^{-1} = 1$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Lemma 4.

Stated but not proved: `MetaMathlibExt.isParkingShuffle_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-parking-shuffle-card).

## Characterization of $(m-2)$-metered parking functions

Let $2 < m \le n + 1$,
$f : \{0, \dots, m-1\} \to \{0, \dots, n-1\}$, $1 \le k \le n$ and $j \in \mathbb{N}$. Write
$\mathrm{Sh}_p(q - 1, N - q)$ for the set of $(p, N)$-parking-function shuffles with parameter
$q$, words of length $p - 1$ with entries in $\{0, \dots, N-1\}$. Suppose that the middle word
$w = (f(1), \dots, f(m-2))$ lies in $\mathrm{Sh}_{m-1}(k - 1, n - k)$, and that either
$m = n + 1$ and $j = 0$, or $m \le n$, $1 \le j \le k - 1$ and the subsequence $\sigma$ of the
entries of $w$ that are less than $k - 1$, a word of length $m + k - n - 2$ with entries in
$\{0, \dots, k-2\}$, lies in $\mathrm{Sh}_{m+k-n-1}(j - 1, k - 1 - j)$. Then $f$ is an
$(m-2)$-metered parking function if and only if either $f(0) < j$ and $f(m-1) < k$, or
$j \le f(0) < k$ and $f(m-1) \le f(0)$.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 4.

Stated but not proved: `MetaMathlibExt.isMeteredParkingFunction_sub_two_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-sub-two-iff).

## Metered parking functions with meter $n - 1$ and more cars than spots

Let $k > 0$ and
$f : \{0, \dots, n+k-1\} \to \{0, \dots, n-1\}$, and let $\pi_0, \dots, \pi_{n-1}$ be the
$(n-1)$-metered outcome of the first $n$ preferences $(f(0), \dots, f(n-1))$ on $n$ spots, where
$\pi_c$ is the spot in which car $c$ parks, if it parks. Then $f$ is an $(n-1)$-metered parking
function if and only if $(f(0), \dots, f(n-1))$ is a parking function and, for every
$i \in \{0, \dots, k-1\}$, car $i \bmod n$ parks in this outcome and $f(n + i) \le \pi_{i \bmod n}$.

The outcome is read periodically: the later preferences $f(n), f(n+1), \dots$ are compared with
$\pi_0, \dots, \pi_{n-1}, \pi_0, \dots$ in turn.

## Sources

- Spencer Daugherty, Pamela E. Harris, Ian Klein, and Matt McClinton, *Metered Parking Functions*, INTEGERS 25 (2025), Article A73, Theorem 6.

Stated but not proved: `MetaMathlibExt.isMeteredParkingFunction_pred_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MeteredParkingFunctionsWanted.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html#is-metered-parking-function-pred-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Metered parking functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/metered-parking-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/parking-functions/metered-parking-functions)
