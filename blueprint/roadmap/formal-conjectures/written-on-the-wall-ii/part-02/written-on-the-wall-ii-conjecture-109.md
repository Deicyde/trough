---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture109.conjecture109
statement: formalized
---

# Written on the Wall II - Conjecture 109

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture109.conjecture109`

Solved: stated here; a Lean proof is at [https://github.com/DomTheDeveloper/formal-conjectures/blob/cf59008ef1cd432bf9803275dcf5d62ab1f094a3/FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean](https://github.com/DomTheDeveloper/formal-conjectures/blob/cf59008ef1cd432bf9803275dcf5d62ab1f094a3/FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean); a Lean proof is at [https://github.com/chelokot/wowii-109-counterexample/blob/543a66ee78565b553f4ba6dc7fd32b5610557913/lean/GraphConjecture109.lean#L29-L139](https://github.com/chelokot/wowii-109-counterexample/blob/543a66ee78565b553f4ba6dc7fd32b5610557913/lean/GraphConjecture109.lean#L29-L139).

> WOWII [Conjecture 109](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$, the independence number $\alpha(G)$ was
> conjectured to satisfy
> $\alpha(G) \le \lfloor (\mathrm{residue}(G) + 2 \cdot b(G)) / 3 \rfloor$, where
> $\mathrm{residue}(G)$ is the Havel--Hakimi residue and $b(G)$ is the size of a
> largest induced bipartite subgraph.
>
> This is false. A connected graph on 21 vertices has an independent set of size
> 15, residue 8, and no induced bipartite subgraph with more than 18 vertices, so
> the conjectured right-hand side is at most 14.
>
> A smaller counterexample is the connected 13-vertex graph
> $\overline K_7 \vee (K_3 \sqcup K_3)$. It has independence number $7$, residue
> $2$, and largest induced bipartite subgraph size $9$, so its conjectured
> right-hand side is $6$.

```lean
theorem conjecture109 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_h : G.Connected),
      (G.indepNum : ℝ) ≤ ⌊((residue G : ℝ) + 2 * b G) / 3⌋
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture109.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
