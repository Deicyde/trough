---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture217.conjecture217
statement: formalized
---

# Written on the Wall II - Conjecture 217

> Per the WOWII definitions popup linked from this conjecture:
>
> - $L(G)$ is the **maximum number of leaves of a spanning tree** of $G$
>   — i.e. `Ls G` in our invariant library.
> - $\chi_{\mathrm{residue}=2}(G)$ is the **characteristic function** for the
>   predicate $\mathrm{residue}\, G = 2$, i.e. $1$ when $\mathrm{residue}\, G = 2$
>   and $0$ otherwise. It is not a connected-component count of any 2-core.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture217.conjecture217`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/wowii-graph-conjecture-217-lean/blob/6a2fb82fcd17aa15ec734736740794bb8bd194c0/lean/GraphConjecture217Audit.lean](https://github.com/KitaKen1/wowii-graph-conjecture-217-lean/blob/6a2fb82fcd17aa15ec734736740794bb8bd194c0/lean/GraphConjecture217Audit.lean).

> WOWII [Conjecture 217](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj217):
>
> If $G$ is a finite simple connected graph on $n > 1$ vertices and
> $L_s(G) \le 4 \cdot \chi_{\mathrm{residue}=2}(G) + 2$,
> then $G$ has a Hamiltonian path. Here $L_s(G)$ is the maximum number of
> leaves over all spanning trees and $\chi_{\mathrm{residue}=2}(G)$ is the indicator
> of $\mathrm{residue}(G) = 2$.

```lean
theorem conjecture217 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hL : Ls G ≤ 4 * (residueEqTwoIndicator G : ℝ) + 2) :
    ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture217.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
