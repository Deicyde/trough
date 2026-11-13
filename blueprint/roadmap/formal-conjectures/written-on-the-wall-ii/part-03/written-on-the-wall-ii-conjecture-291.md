---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture291.conjecture291
statement: formalized
---

# Written on the Wall II - Conjecture 291

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definitions
>
> For a vertex $v$ in a graph $G$, **$T(v)$** is the number of triangles (3-cliques)
> incident to $v$, i.e., the number of 3-element cliques in $G$ that contain $v$.
>
> The **triangle-frequency of the minimum** is the number of vertices that achieve the
> minimum value of $T(v)$.
>
> **$k$** is the **first step in the Havel–Hakimi process at which a zero appears**.
> Concretely, starting from the descending degree sequence $s_0$ of $G$, we set
> $s_{i+1} = \mathrm{havelHakimiStep}\, s_i$ and let $k$ be the least $i \ge 0$ such
> that $s_i$ contains a zero entry (or, vacuously, has been emptied entirely). Since
> each step is sorted descending and never increases entries, this is equivalent
> to the last (smallest) entry of $s_i$ being $0$, or $s_i$ being $[]$.
>
> This is **strictly weaker** than $n - \mathrm{residue}(G)$: $n - \mathrm{residue}(G)$
> is the *total* number of reduction steps until *every* entry is zero, whereas $k$
> only requires that *some* entry has hit zero — and a $0$ typically appears well
> before the all-zero state is reached.
>
> **Conjecture 291:** For a simple connected graph $G$ with $n > 2$,
> $\gamma_t(G) \le k + \mathrm{frequency}(t_{\min}(v))$
> where $\gamma_t(G)$ is the total domination number, $k$ is the Havel-Hakimi zero
> step, and $\mathrm{frequency}(t_{\min}(v))$ is the number of vertices achieving
> the minimum triangle count.
>
> The conjecture is **false**: on July 23, 2026, Zyad Tamimi sent a 12-vertex
> counterexample with $\gamma_t(G) = 4$, $\mathrm{frequency}(t_{\min}(v)) = 1$ and $k = 2$,
> and the source now lists Conjecture 291 as refuted.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture291.conjecture291`

Solved: stated here without proof.

> WOWII [Conjecture 291](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$ with $n > 2$,
> $\gamma_t(G) \le k + \mathrm{frequency}(t_{\min}(v))$
> where:
>
> - $\gamma_t(G)$ is the total domination number,
> - $k$ is the first step in which a zero appears in the Havel-Hakimi process,
> - $\mathrm{frequency}(t_{\min}(v))$ is the number of vertices achieving the
>   minimum triangle count.
>
> This is false: the source records a 12-vertex counterexample by Zyad Tamimi (July 23, 2026)
> with $\gamma_t(G) = 4 > 2 + 1 = k + \mathrm{frequency}(t_{\min}(v))$.
>
> The hypothesis $n > 2$ is stated in the source's full list of conjectures (as for the
> neighbouring Conjectures 290, 292 and 293) but omitted on its list of open conjectures;
> the counterexample has $12$ vertices, so it refutes both readings.

```lean
theorem conjecture291 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_h : G.Connected) (_hn : 2 < Fintype.card α),
      G.totalDominationNumber ≤ havelHakimiZeroStep G + freqMinTriangles G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture291.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
