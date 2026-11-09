---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture7.conjecture7
statement: formalized
---

# Written on the Wall II - Conjecture 7

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [DFW03] E. DeLaVina, S. Fajtlowicz and B. Waller, [On Some Conjectures of Griggs and Graffiti](https://www.uhd.edu/documents/academics/sciences/griggsngraffiti.pdf), 2002, revised 2003.
> - [Li26] Wentao Li, [Lean proof of WOWII 7](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/proofs/WOWII7/PROOF.md), 2026.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture7.conjecture7`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII7.lean#L462](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII7.lean#L462).

> WOWII [Conjecture 7](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $L_s(G) \ge \max_v \lambda(v) - 1 + n - 2 \alpha(G)$,
> where $L_s(G)$ is the maximum number of leaves over all spanning trees of $G$,
> $n = |V(G)|$, $\alpha(G) = G.\mathrm{indepNum}$ is the independence number, and
> $\lambda(v) = \mathrm{indepNeighborsCard}\, G\, v$ is the independence number of the
> neighbourhood of $v$.
>
> Proved by DeLaVina, Fajtlowicz, Waller (2002); see [DFW03].
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture7 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let maxL := (Finset.univ.image (fun v => indepNeighborsCard G v)).max' (by simp)
    ((maxL : ℤ) - 1 + (Fintype.card α : ℤ) - 2 * (G.indepNum : ℤ) : ℝ) ≤ Ls G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture7.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
