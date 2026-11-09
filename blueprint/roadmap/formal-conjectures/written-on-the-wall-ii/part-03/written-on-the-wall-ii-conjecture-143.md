---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture143.conjecture143
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 143

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture143.conjecture143`

Proved here.

> WOWII [Conjecture 143](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj143):
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge (\mathrm{girth}(G) + 1) / \sigma(G)$,
> where $\mathrm{tree}(G)$ is the largest induced tree size, $\mathrm{girth}(G)$
> is the length of the shortest cycle, and
> $\sigma(G) = G.\mathrm{secondSmallestDegree}$ is the **second-smallest degree**
> of $G$'s degree sequence (per WOWII defEntry 65). We state the inequality in
> denominator-free form to avoid the $\sigma = 0$ corner case ($n \le 1$).
>
> The proof splits into the acyclic case and two cyclic cases. For an acyclic
> graph the girth is zero. If $\sigma \ge 2$, deleting two consecutive edges from
> a shortest cycle leaves an induced tree on $\mathrm{girth}(G)-1$ vertices, and
> the factor $\sigma \ge 2$ yields the required inequality. If $\sigma = 1$,
> there are two degree-one vertices. A maximal induced tree containing them must
> have an external vertex with two attachments; those attachments create a cycle
> whose length forces the tree to contain at least $\mathrm{girth}(G)+1$ vertices.

```lean
theorem conjecture143 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hσ : 0 < secondSmallestDegree G) :
    (G.girth : ℝ) + 1 ≤ (largestInducedTreeSize G : ℝ) * (secondSmallestDegree G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture143.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
