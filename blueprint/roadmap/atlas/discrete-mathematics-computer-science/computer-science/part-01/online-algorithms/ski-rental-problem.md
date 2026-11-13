---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Online.SkiRental.Strategy, Cslib.Algorithms.Lean.Online.SkiRental.cost, Cslib.Algorithms.Lean.Online.SkiRental.opt, Cslib.Algorithms.Lean.Online.SkiRental.breakEven, Cslib.Algorithms.Lean.Online.SkiRental.opt_le_cost, Cslib.Algorithms.Lean.Online.SkiRental.cost_breakEven_le, Cslib.Algorithms.Lean.Online.SkiRental.cost_breakEven_le_two_mul, Cslib.Algorithms.Lean.Online.SkiRental.exists_cost_ge
statement: formalized
proof: formalized
---

# Ski rental problem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html).

## Deterministic ski-rental strategy

A deterministic strategy is either a day
$t \in \mathbb{N}$ on which to buy the skis, after renting on the days before it, or the choice to
rent forever. Days are numbered from $1$; the value $t = 0$ is also a strategy, and the cost
treats it as renting forever.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.Strategy`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#strategy).

## Cost of a ski-rental strategy

Renting skis costs $1$ per day and buying them costs a
natural number $B$. The cost $\mathrm{cost}_B(s, d) \in \mathbb{N}$ of a strategy $s$ for a season
of $d \in \mathbb{N}$ days is $(t - 1) + B$ if $s$ buys on a day $t$ with $1 \le t \le d$ (rent for
$t - 1$ days, then buy), and $d$ otherwise, that is, if $s$ rents forever or buys on a day $t$
with $t = 0$ or $t > d$ (rent every day).

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.cost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#cost).

## Offline optimum for ski rental

For a purchase price $B \in \mathbb{N}$ and a season of
$d \in \mathbb{N}$ days, the offline optimum is $\mathrm{opt}_B(d) = \min(d, B)$: rent every day
or buy on day one, whichever is cheaper.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.opt`, a definition declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#opt).

## Break-even strategy

For a purchase price $B$, the break-even strategy is the deterministic
strategy that buys on day $B$.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.breakEven`, a definition declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#break-even).

## The offline optimum bounds every strategy's cost

For every purchase price $B$, every
deterministic strategy $s$ and every season length $d$, the offline optimum $\mathrm{opt}_B(d)$ is
at most the cost $\mathrm{cost}_B(s, d)$ of $s$ for a season of $d$ days.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.opt_le_cost`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#opt-le-cost).

## Ski-rental upper bound for the break-even strategy

For every purchase price $B \ge 1$ and
every season length $d$, the break-even strategy $\mathrm{breakEven}_B$ pays at most $2 - 1/B$
times the offline optimum $\mathrm{opt}_B(d)$: its cost $\mathrm{cost}_B(\mathrm{breakEven}_B, d)$
for a season of $d$ days satisfies
$B \cdot \mathrm{cost}_B(\mathrm{breakEven}_B, d) \le (2B - 1) \cdot \mathrm{opt}_B(d)$.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.cost_breakEven_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#cost-break-even-le).

## The break-even strategy pays at most twice the optimum

For every purchase price $B \ge 1$
and every season length $d \in \mathbb{N}$, the cost $\mathrm{cost}_B(\mathrm{breakEven}_B, d)$ of
the break-even strategy for a season of $d$ days is at most $2 \cdot \mathrm{opt}_B(d)$, twice
the offline optimum $\mathrm{opt}_B(d)$. In particular, the break-even strategy is
$2$-competitive.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.cost_breakEven_le_two_mul`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#cost-break-even-le-two-mul).

## Lower bound

Every deterministic strategy pays at least `(2 - 1/B)` times the optimum on
some season, `(2 B - 1) * opt ≤ B * cost`.

Formalized by `Cslib.Algorithms.Lean.Online.SkiRental.exists_cost_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/SkiRental.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/SkiRental.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html#exists-cost-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ski rental problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/ski-rental-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/online-algorithms/ski-rental-problem)
