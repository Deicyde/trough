---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture101.conjecture101
statement: formalized
---

# Written on the Wall II - Conjecture 101

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [LM11] V. E. Levit and E. Mandrescu, [A Set and Collection Lemma](https://arxiv.org/abs/1101.4564), 2011, Corollaries 2.3–2.4.
> - [Li26] Wentao Li, [Lean proof of WOWII 101](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/proofs/WOWII101/PROOF.md), 2026.
>
> ## Definitions
>
> The **$\alpha$-core** of a graph $G$, written `alphaCore G`, is the set of vertices
> $v$ such that removing $v$ strictly decreases the independence number:
>
> $$\mathrm{alphaCore}(G) = \{v \mid \alpha(G - v) < \alpha(G)\}$$
>
> where $G - v$ is the subgraph of $G$ induced on $V(G) \setminus \{v\}$.
>
> These vertices are also called "critical vertices for independence."

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture101.conjecture101`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII101.lean#L318](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII101.lean#L318).

> WOWII [Conjecture 101](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\alpha(G) \le \lfloor (n + |\mathrm{alphaCore}(G)|) / 2 \rfloor$
> where $\alpha(G) = G.\mathrm{indepNum}$ is the independence number, $n$ is the
> number of vertices, and $\mathrm{alphaCore}(G)$ is the set of vertices whose
> removal decreases the independence number.
>
> This is Hajnal's inequality in its independent-set form; see [LM11].
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture101 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    G.indepNum ≤ (Fintype.card α + (alphaCore G).card) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture101.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
