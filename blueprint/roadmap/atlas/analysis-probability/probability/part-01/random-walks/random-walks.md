---
declaration: section
origin: cited
lean: MetaMathlibExt.bertrand_ballot
statement: formalized
proof: formalized
---

# Random walks: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/index.html).

Sums of i.i.d. steps as processes: the drift/oscillation dichotomy, limsup and liminf of partial sums, tail measurability of asymptotic events, the strong Markov property of i.i.d. sequences at stopping times, and ballot theorems.

## Bertrand's ballot theorem

Let $p$ and $q$ be natural numbers with $1 \le q < p$. Call a
sequence of $p + q$ votes, each for A or for B, favourable if it contains exactly $p$ votes for A
and, for every $k$ with $1 \le k \le p + q$, strictly more of its first $k$ votes are for A than
for B. Then the number of favourable sequences, multiplied by $p + q$, equals
$(p - q)\binom{p+q}{q}$.

Equivalently, when the $p + q$ votes are counted in uniformly random order, the probability that
A is strictly ahead of B throughout the count is $\frac{p-q}{p+q}$, since there are
$\binom{p+q}{q}$ sequences with exactly $p$ votes for A.

## Sources

- *Bertrand's ballot theorem*, Wikipedia, https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem.

Formalized by `MetaMathlibExt.bertrand_ballot`, a theorem declared in [MathlibExt/Probability/BertrandBallot.lean, line 758](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BertrandBallot.lean#L758). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/index.html#bertrand-ballot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random walks](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/random-walks)
