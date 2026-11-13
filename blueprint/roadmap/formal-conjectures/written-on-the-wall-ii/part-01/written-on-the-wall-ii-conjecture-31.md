---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture31.conjecture31
statement: formalized
---

# Written on the Wall II - Conjecture 31

> The WOWII page records this as **Chung's theorem**. This radius bound is proved
> in Section 2 of P. Erdős, M. Saks, and V. T. Sós, *Maximum Induced Trees in
> Graphs*, J. Combin. Theory Ser. B **41** (1986), 61–79; the authors credit
> Fan Chung for the proof. We state it here as a theorem; the formal proof is left
> as `sorry` pending a Lean port of the argument.
>
> Here $\mathrm{path}(G)$ is the maximum number of vertices in an induced path,
> and $\mathrm{rad}(G)$ is the graph radius.
>
> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [P. Erdős, M. Saks, V. T. Sós, Maximum Induced Trees in Graphs](https://doi.org/10.1016/0095-8956(86)90028-6)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture31.conjecture31`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/wowii-graph-conjecture-31-lean/blob/a948e9fc07e11b786aee8dadb1376b4d938454d6/lean/GraphConjecture31.lean](https://github.com/KitaKen1/wowii-graph-conjecture-31-lean/blob/a948e9fc07e11b786aee8dadb1376b4d938454d6/lean/GraphConjecture31.lean).

> WOWII [Conjecture 31](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj31)
> (Chung):
>
> For every simple connected graph $G$,
> $\mathrm{path}(G) \ge 2 \cdot \mathrm{rad}(G) - 1$,
> where $\mathrm{path}(G)$ is the maximum number of vertices in an induced path
> and $\mathrm{rad}(G)$ is the graph radius.

```lean
theorem conjecture31 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    2 * (G.radius.toNat : ℤ) - 1 ≤ (path G : ℤ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture31.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
