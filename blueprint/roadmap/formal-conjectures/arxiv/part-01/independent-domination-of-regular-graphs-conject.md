---
declaration: theorem
origin: cited
lean: Arxiv.«2107.00295».independentDominationEven, Arxiv.«2107.00295».independentDominationOdd
statement: formalized
---

# Independent Domination of Regular Graphs, Conjecture 1.6

> *Reference:* [arxiv/2107.00295](https://arxiv.org/abs/2107.00295)
> **On independent domination of regular graphs**
> by *Eun-Kyung Cho, Ilkyoo Choi, Boram Park*
>
> The conjecture was subsequently proved by Cho, Kim, Kim and Oum, as
> Corollary 1.3 of:
>
> *Reference:* [arxiv/2202.09594](https://arxiv.org/abs/2202.09594)
> **Independent domination of graphs with bounded maximum degree**
> by *Eun-Kyung Cho, Jinha Kim, Minki Kim, Sang-il Oum*,
> J. Combin. Theory Ser. B 158 (2023), 341-352.
>
> Corollary 1.3 states that every graph $G$ with maximum degree at most $\Delta$
> and no isolated vertices has an independent dominating set of size at most
> $\left(1 - \frac{\Delta}{\lfloor (\Delta+2)^2/4 \rfloor}\right)\lvert V(G)\rvert$.
> Expanding the floor for even and odd $\Delta$ gives exactly the two
> statements below.

*Quoted from [FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Arxiv.«2107.00295».independentDominationEven`

Solved: stated here without proof.

> **Conjecture 1.6 (Even case).**
> For a nonempty isolate-free graph $G$ on $n$ vertices,
> if $D$ is even, then $(D + 2)^2 \cdot i(G) \leq (D^2 + 4) \cdot n$.
>
> Proved by Cho, Kim, Kim and Oum ([arxiv/2202.09594](https://arxiv.org/abs/2202.09594),
> Corollary 1.3).

```lean
theorem independentDominationEven (hIso : 0 < G.minDegree) (hEven : Even G.maxDegree) :
    let D := G.maxDegree
    let i := G.indepDominationNumber
    let n := Fintype.card V
    (D + 2)^2 * i ≤ (D^2 + 4) * n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean#L55).

## `Arxiv.«2107.00295».independentDominationOdd`

Solved: stated here without proof.

> **Conjecture 1.6 (Odd case).**
> For a nonempty isolate-free graph $G$ on $n$ vertices,
> if $D$ is odd, then $(D + 1)(D + 3) \cdot i(G) \leq (D^2 + 3) \cdot n$.
>
> Proved by Cho, Kim, Kim and Oum ([arxiv/2202.09594](https://arxiv.org/abs/2202.09594),
> Corollary 1.3).

```lean
theorem independentDominationOdd (hIso : 0 < G.minDegree) (hOdd : Odd G.maxDegree) :
    let D := G.maxDegree
    let i := G.indepDominationNumber
    let n := Fintype.card V
    (D + 1) * (D + 3) * i ≤ (D^2 + 3) * n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2107.00295/IndependentDomination.lean)
- [arxiv/2107.00295](https://arxiv.org/abs/2107.00295)
