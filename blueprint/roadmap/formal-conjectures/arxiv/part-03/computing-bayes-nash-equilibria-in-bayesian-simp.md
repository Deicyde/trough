---
declaration: theorem
origin: cited
lean: Arxiv.«2610.08796».exists_isPolyTime_bayesNash
statement: formalized
---

# Computing Bayes–Nash equilibria in Bayesian simple security games

> The source lists the game data explicitly and leaves the numerical encoding implicit.
> We use rational payoffs and probabilities. `BitstringEncoding` encodes each rational by its
> reduced numerator and positive denominator. The time bound is polynomial in the bit length of
> the encoded input, which includes the resource count and all table entries.
>
> The defender chooses exactly $r$ distinct targets. We represent her mixed strategy by the
> coverage probability of each target, with entries in $[0,1]$ that sum to $r$. In this model,
> these marginals can be converted in polynomial time to a sparse mixture of legal allocations.
>
> *References:*
> - Vincent Conitzer, *Computing Bayes–Nash equilibrium in simple security games*,
>   [§1](https://arxiv.org/pdf/2610.08796#page=1).
> - Joshua Letchford and Vincent Conitzer, *Solving Security Games on Graphs via Marginal
>   Probabilities*. [Paper](https://cdn.aaai.org/ojs/8688/8688-13-12216-1-2-20201228.pdf).

*Quoted from [FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Arxiv.«2610.08796».exists_isPolyTime_bayesNash`

Open: stated without proof.

> Can one deterministic polynomial-time algorithm compute an exact Bayes–Nash equilibrium
> for every Bayesian simple security game?

```lean
theorem exists_isPolyTime_bayesNash :
    ∃ solve : GameInput → EquilibriumOutput,
      IsPolyTime solve ∧ ∀ (g : GameInput), g.Valid → g.IsBayesNash (solve g)
```

Category `research open`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2610.08796/BayesianSecurityGames.lean)
- [§1](https://arxiv.org/pdf/2610.08796#page=1)
