---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture309.conjecture309
statement: formalized
---

# Written on the Wall II - Conjecture 309

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [J. J. Gebendorfer, An Infinite Family of Counterexamples to Written on the Wall II,
>   Conjecture 309](https://doi.org/10.5281/zenodo.21553295)
>
> The conjecture is false for the clique blow-ups $C_5[K_k]$ for every $k \geq 3$.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture309.conjecture309`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/c9daf0f594d6d5b264c6cd54dc9eec488cb64741/lean/GraphConjecture309.lean](https://github.com/Kuberwastaken/c5-k4/blob/c9daf0f594d6d5b264c6cd54dc9eec488cb64741/lean/GraphConjecture309.lean).

> Does every finite simple connected graph $G$ of order greater than two satisfy
>
> $$
> \gamma_t(G) \leq \frac{1}{2}\left(
> \max_v(\operatorname{distEven}(v)-\operatorname{evenHorizontal}(v))+
> \min_{e\in E(\overline G)}|N_{\overline G}(e)|\right)?
> $$
>
> Gebendorfer disproved the statement with the family $C_5[K_k]$, $k \geq 3$.

```lean
theorem conjecture309 : ¬ conjecture309Statement
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture309.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
