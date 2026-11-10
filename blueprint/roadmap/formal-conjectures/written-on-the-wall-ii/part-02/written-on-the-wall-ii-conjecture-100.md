---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture100.conjecture100
statement: formalized
---

# Written on the Wall II - Conjecture 100

> **Verbatim statement (WOWII #100, status O):**
> > If G is a simple connected graph, then α(G) ≤ CEIL[(maximum of λ(v) + 0.5*length(Ḡ))/2]
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj100
>
> The WOWII HTML uses `length(Ḡ)` (the bar denotes graph complement); the
> extracted JSON in our private repo previously dropped the overline. The
> formal statement below uses the Euclidean norm of the degree sequence of `Gᶜ`.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definition of graph length
>
> The WOWII definitions popup defines `length(H)` as the square root of the sum
> of the squares of the vertex degrees. This is `degreeL2Norm H` in Lean.
> Combined with the overline above, the inequality reads:
>   `α(G) ≤ ⌈(max_v l(v) + 0.5 · degreeL2Norm(Gᶜ)) / 2⌉`
> where `l(v) = indepNeighbors G v`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture100.conjecture100`

Solved: stated here; a Lean proof is at [https://github.com/DomTheDeveloper/formal-conjectures/blob/0a0d23bdfcea605892146b039dfbdd4896229b32/FormalConjectures/WrittenOnTheWallII/100.lean](https://github.com/DomTheDeveloper/formal-conjectures/blob/0a0d23bdfcea605892146b039dfbdd4896229b32/FormalConjectures/WrittenOnTheWallII/100.lean).

> WOWII [Conjecture 100](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj100)
> (status O):
>
> For a simple connected graph `G`,
> `α(G) ≤ ⌈(max_v l(v) + 0.5 · degreeL2Norm(Gᶜ)) / 2⌉`
> where `α(G) = G.indepNum` is the independence number,
> `max_v l(v)` is the maximum over all vertices of the independence number of
> the neighbourhood (in `G`), and `degreeL2Norm(Gᶜ)` is the square root of the
> sum of the squares of the degrees in the complement `Gᶜ`.
>
> **Proof outline.** Choose a maximum independent set `S`, write `A = |S|`, let
> `T` be its complement, and let `L` be the maximum neighbourhood independence
> number. Connectedness gives at least one edge from every vertex of `S` into
> `T`, while each vertex of `T` has at most `L` neighbours in `S`; double
> counting therefore gives `A ≤ |T|L`. In the complement graph, `S` is a clique.
> The missing cross-edges force explicit lower bounds on the complement degrees
> of vertices in both `S` and `T`. Summing their squares gives a lower bound for
> `degreeL2Norm(Gᶜ)²`, and the resulting quadratic inequality rearranges to the
> stated ceiling bound.
>
> **Provenance.** Solved by Dominic Dabish.
>
> ProofOrchestrator, using OpenAI GPT-5.6 Thinking, assisted with the mathematical
> argument and Lean formalization; all formal claims were checked by the pinned
> Lean compiler.

```lean
theorem conjecture100 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let maxL := (Finset.univ.image (indepNeighborsCard G)).max' (by simp)
    (G.indepNum : ℝ) ≤ ⌈((maxL : ℝ) + (1 / 2) * (degreeL2Norm Gᶜ : ℝ)) / 2⌉
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture100.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
