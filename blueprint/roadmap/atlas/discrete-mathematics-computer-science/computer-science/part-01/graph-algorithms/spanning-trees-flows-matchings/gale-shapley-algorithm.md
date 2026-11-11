---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Matching.GaleShapley.toOrder, Cslib.Algorithms.Lean.Matching.GaleShapley.mprefs, Cslib.Algorithms.Lean.Matching.GaleShapley.wprefs, Cslib.Algorithms.Lean.Matching.GaleShapley.State, Cslib.Algorithms.Lean.Matching.GaleShapley.init, Cslib.Algorithms.Lean.Matching.GaleShapley.Free, Cslib.Algorithms.Lean.Matching.GaleShapley.newHolder, Cslib.Algorithms.Lean.Matching.GaleShapley.propose
statement: formalized
proof: formalized
---

# Gale–Shapley algorithm

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html).

## Preferences

## Preference order of a ranking

A permutation $\sigma$ of $\{0, \dots, n-1\}$, read as a
ranking ($\sigma(k)$ is the $k$-th choice, $\sigma(0)$ the best), gives the strict total order on
$\{0, \dots, n-1\}$ in which $a$ is preferred to $b$ when $\sigma^{-1}(a) < \sigma^{-1}(b)$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.toOrder`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#to-order).

## Proposers' preferences from rankings

Given for each proposer $m$ a ranking $\sigma_m$ of
the $n$ receivers ($\sigma_m(k)$ is the choice of $m$ of rank $k$, rank $0$ the best), the
proposers' preference profile assigns to $m$ the strict total order in which $m$ prefers $w$ to
$w'$ when $\sigma_m^{-1}(w) < \sigma_m^{-1}(w')$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.mprefs`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#mprefs).

## Receivers' preference profile from rankings

Given for each receiver $w$ a ranking
$\sigma_w$ of the $n$ proposers (a permutation of $\{0, \dots, n-1\}$, with $\sigma_w(0)$ her first
choice), the receivers' preference profile assigns to $w$ the preference order of $\sigma_w$: $w$
prefers $a$ to $b$ when $\sigma_w^{-1}(a) < \sigma_w^{-1}(b)$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.wprefs`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#wprefs).

## Deferred-acceptance state

A state of deferred acceptance with $n$ proposers and $n$
receivers, both numbered $0, \dots, n-1$, records for each proposer a natural number, the number of
proposals he has made (his next proposal goes to his choice of that rank), and for each receiver
either the proposer she currently holds or that she holds nobody.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.State`, a structure declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#state).

## Initial state of deferred acceptance

The initial state with $n$ proposers and
$n$ receivers: every proposer has made $0$ proposals and no receiver holds anyone.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.init`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#init).

## Free proposer

A proposer $m$ is free in a state $s$ of deferred acceptance when no
receiver holds $m$ in $s$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.Free`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#free).

## Receiver's holder after a proposal

In a state $s$ of deferred acceptance, the proposer
whom receiver $w$ holds after proposer $m$ proposes to her is $m$ if she holds nobody in $s$ or
ranks $m$ strictly better than her current holder $m'$ in her ranking, and $m'$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.newHolder`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#new-holder).

## A proposal

Fix, for each proposer, a ranking of the $n$ receivers and, for each receiver,
a ranking of the $n$ proposers (rank $0$ is the first choice). Let $s$ be a state of deferred
acceptance in which proposer $m$ has made $k$ proposals. If $k < n$, then $m$ proposes to the
receiver $w$ of rank $k$ in his ranking: his number of proposals becomes $k + 1$, and $w$ now
holds $m$ if she held nobody or ranks $m$ strictly above the proposer she held, and keeps her old
holder otherwise; all other counts and holders are unchanged. If $k \ge n$, the state is
unchanged.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.propose`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#propose).

## Choosing the next proposer

In a state $s$ of deferred acceptance with proposers
$0, 1, \dots, n-1$, the chooser returns the least proposer $m$ who is free in $s$ and has made
fewer than $n$ proposals in $s$, or no proposer if there is none.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.chooser`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#chooser).

## Running deferred acceptance

Fix rankings for $n$ proposers and $n$ receivers, both
numbered $0, \dots, n-1$. Starting from a state $s$ with a budget of $f$ proposals: if $f = 0$, or
if no proposer is both free (held by no receiver) and has made fewer than $n$ proposals, the run
returns $s$; otherwise the lowest-numbered such proposer makes a proposal, and the run continues
from the resulting state with budget $f - 1$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.run`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#run).

## Deferred acceptance

Let each of $n$ proposers rank the $n$ receivers, and each receiver
rank the $n$ proposers, with rank $0$ the best. Deferred acceptance is the state reached from the
initial state, in which no one has proposed and no receiver holds anyone, by repeating the
following step at most $n^2$ times, stopping early once no proposer is both free and has made
fewer than $n$ proposals: the least such proposer, having made $p$ proposals so far, proposes to
the receiver of rank $p$ in his ranking, and she then holds whichever of him and her current
holder she ranks better, or him if she held no one.

These $n^2$ steps always suffice: in the resulting state no proposer is both free and has made
fewer than $n$ proposals.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.galeShapley`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#gale-shapley).

## Invariant of deferred acceptance

Let each proposer $m$ have a ranking $\sigma_m$ of the
$n$ receivers and each receiver $w$ a ranking $\tau_w$ of the $n$ proposers, where $\sigma_m(k)$
is the choice of $m$ of rank $k$ (rank $0$ is the best) and $\tau_w^{-1}(x)$ is the rank of $x$
for $w$. A state $s$ of deferred acceptance satisfies the invariant when: every proposer has made
at most $n$ proposals; if $w$ holds $m$, then $m$ has made $k + 1$ proposals for some rank $k$
with $\sigma_m(k) = w$; no proposer is held by two different receivers; for every proposer $m$
and every rank $k$ less than the number of proposals of $m$, the receiver $w = \sigma_m(k)$ holds
some $m'$ with $\tau_w^{-1}(m') \le \tau_w^{-1}(m)$; and for such $m$ and $k$, if $\sigma_m(k)$
does not hold $m$, then no perfect matching that is stable for the preferences given by the
rankings matches $m$ with $\sigma_m(k)$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.Inv`, a structure declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#inv).

## A stable matching has no blocking pair

Let each proposer $m$ have a ranking $\sigma_m$ of
the $n$ receivers and each receiver $w$ a ranking $\tau_w$ of the $n$ proposers, where
$\sigma_m^{-1}(x)$ and $\tau_w^{-1}(x)$ are ranks ($0$ the best). If $\nu$ is a perfect matching
that is stable for the preferences given by these rankings, there are no proposer $m$ and
receiver $w$ with $\sigma_m^{-1}(w) < \sigma_m^{-1}(\nu(m))$ and
$\tau_w^{-1}(m) < \tau_w^{-1}(\nu^{-1}(w))$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.not_blocking`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#not-blocking).

## Rejected proposals bound stable partners

Let each proposer $m$ have a ranking
$\sigma_m$ of the $n$ receivers ($\sigma_m(k)$ is the choice of $m$ of rank $k$, rank $0$ the
best), and each receiver a ranking of the $n$ proposers. Let $s$ be a state of deferred
acceptance satisfying the invariant, let $\nu$ be a perfect matching that is stable for the
preferences given by the rankings, let $m$ be a proposer, and let $b$ be a natural number at most
the number of proposals $m$ has made in $s$. If for every rank $k < b$ the receiver $\sigma_m(k)$
does not hold $m$ in $s$, then $\sigma_m^{-1}(\nu(m)) \ge b$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.le_rank_of_rejected`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#le-rank-of-rejected).

## Cases of the receiver's new holder

Let $s$ be a state of deferred acceptance, $m$ a
proposer and $w$ a receiver with ranking $\tau_w$ of the proposers ($\tau_w^{-1}(x)$ is the rank
of $x$, rank $0$ the best). Then one of the following holds: $w$ holds nobody in $s$ and holds $m$
after $m$ proposes to her; or $w$ holds some $y$ in $s$ with $\tau_w^{-1}(m) < \tau_w^{-1}(y)$
and holds $m$ after $m$ proposes to her; or $w$ holds some $y$ in $s$ with
$\tau_w^{-1}(m) \ge \tau_w^{-1}(y)$ and holds $y$ after $m$ proposes to her.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.newHolder_cases`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#new-holder-cases).

## Remaining proposals

For a state $s$ of deferred acceptance with $n$ proposers and $n$
receivers, in which each proposer $m$ has made $k_m$ proposals, the number of proposals still
available is $\sum_{m} \max(n - k_m, 0)$, the sum running over all $n$ proposers.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.remaining`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#remaining).

## A proposal adds one to the proposal count

Fix rankings for $n$ proposers and $n$
receivers. If proposer $m$ has made fewer than $n$ proposals in a state $s$ of deferred
acceptance, then after $m$ proposes, the total number of proposals made by all proposers is one
more than in $s$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.sum_next_propose`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#sum-next-propose).

## Deferred acceptance makes at most n² proposals

For any rankings of the $n$ receivers by
each of the $n$ proposers and of the proposers by each receiver, in the final state of deferred
acceptance the numbers of proposals made by the proposers sum to at most $n \cdot n$.

No proposer proposes more than $n$ times.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.sum_next_galeShapley_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#sum-next-gale-shapley-le).

## When deferred acceptance stops, every proposer is held

Fix rankings of the $n$ receivers
by each of $n$ proposers and of the proposers by each receiver. Let $s$ be a state of deferred
acceptance that satisfies the invariant of deferred acceptance for these rankings, and suppose
that no proposer is both free in $s$ and has made fewer than $n$ proposals in $s$. Then every
proposer is held by some receiver in $s$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.held_of_done`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#held-of-done).

## Every receiver holds someone once every proposer is held

Let $s$ be a state of deferred
acceptance with $n$ proposers and $n$ receivers. If every proposer is held by some receiver in
$s$, then every receiver holds some proposer in $s$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.holds_of_held`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#holds-of-held).

## Receiver's partner

In a state $s$ of deferred acceptance with $n$ proposers and $n$
receivers, both numbered $0, \dots, n-1$, the partner of a receiver $w$ is the proposer she holds
in $s$; if she holds nobody, it is the proposer numbered $w$ (a default value).

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.partnerW`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#partner-w).

## Proposer's partner

In a state $s$ of deferred acceptance with $n$ proposers and $n$
receivers, both numbered $0, \dots, n-1$, the partner of a proposer $m$ is the lowest-numbered
receiver that holds $m$ in $s$; if no receiver holds $m$, it is the receiver numbered $m$
(a default value).

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.partnerM`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#partner-m).

## The Gale-Shapley matching

Each proposer with the receiver who holds him at the end.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.gsMatching`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#gs-matching).

## A proposer's final partner is his last proposal

Let each proposer $m$ rank the $n$
receivers by a permutation $\sigma_m$ of $\{0, \dots, n-1\}$, where $\sigma_m(k)$ is his choice
of rank $k$, let each receiver rank the $n$ proposers, and let $p_m$ be the number of proposals
$m$ has made in the final state of deferred acceptance. Then $p_m \ge 1$, and the Gale-Shapley
partner $\mu(m)$ of $m$ has rank $p_m - 1$ in his ranking, that is,
$\sigma_m^{-1}(\mu(m)) = p_m - 1$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.exists_rank_gsMatching`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#exists-rank-gs-matching).

## The Gale-Shapley matching is stable

For $n$ proposers and $n$ receivers, each with a
ranking of the other side, the perfect matching computed by deferred acceptance is stable for the
strict preferences given by these rankings.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.isStable_gsMatching`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#is-stable-gs-matching).

## Proposer-optimality

No stable matching gives a proposer a partner he prefers to his
Gale-Shapley partner.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.gsMatching_proposer_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#gs-matching-proposer-optimal).

## Receiver-pessimality

No stable matching gives a receiver a partner she likes less than
her Gale-Shapley partner.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.gsMatching_receiver_pessimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#gs-matching-receiver-pessimal).

## Rank under a strict total order

For a strict total order $<$ on $\{0, \dots, n-1\}$, the
rank of an element $a$ is the number of elements $b$ with $b < a$ (the elements preferred to $a$),
as an element of $\{0, \dots, n-1\}$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.orderRank`, a definition declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#order-rank).

## Every strict total order on $\{0, \dots, n-1\}$ is given by a ranking

For every strict
total order $\prec$ on $\{0, \dots, n-1\}$ there is a permutation $\sigma$ of $\{0, \dots, n-1\}$
such that, for all $a$ and $b$, $a \prec b$ holds exactly when $\sigma^{-1}(a) < \sigma^{-1}(b)$.

Hence the Gale-Shapley algorithm on rankings applies to every preference on $\{0, \dots, n-1\}$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.exists_toOrder_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#exists-to-order-eq).

## Gale-Shapley serves every preference profile with $n$ proposers and $n$ receivers

Let
the $n$ proposers and the $n$ receivers both be numbered $0, \dots, n-1$. Let each proposer $m$
have a strict total order $\lt _m$ of preference on the receivers and each receiver $w$ a strict
total order $\lt _w$ of preference on the proposers, where $x \lt _m y$ means that $m$ prefers $x$ to
$y$, and likewise for $\lt _w$. Then there are permutations $\sigma_m$ (one for each proposer $m$)
and $\tau_w$ (one for each receiver $w$) of $\{0, \dots, n-1\}$, read as rankings, such that
$w \lt _m w'$ exactly when $\sigma_m^{-1}(w) < \sigma_m^{-1}(w')$ and $a \lt _w b$ exactly when
$\tau_w^{-1}(a) < \tau_w^{-1}(b)$, and the Gale-Shapley matching $\mu$ of the rankings $\sigma$
and $\tau$ is stable for these preferences and proposer-optimal: for every perfect matching $\nu$
that is stable for these preferences and every proposer $m$, it is not the case that
$\nu(m) \lt _m \mu(m)$.

Formalized by `Cslib.Algorithms.Lean.Matching.GaleShapley.exists_rankings_gsMatching`, a theorem declared in [CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matching/GaleShapley.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html#exists-rankings-gs-matching).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gale–Shapley algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/gale-shapley-algorithm)
