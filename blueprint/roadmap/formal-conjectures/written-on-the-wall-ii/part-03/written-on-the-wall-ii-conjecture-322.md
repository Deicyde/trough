---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture322.conjecture322
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 322

> *Reference:*
> [E. DeLaViña, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.uhd.edu/faculty/delavinae/research/wowII/)
>
> The source applies the local-independence hypothesis to the complement graph. Its conclusion
> also follows from the characterization of minimal total dominating sets of complete multipartite
> graphs in [M. Subramanian and A. Selvakumar, *Total Domination and Minimal Total Domination
> Polynomial of H-Join Graphs*](https://doi.org/10.2298/FIL2501267S).

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture322.conjecture322`

Proved here.

> WOWII [Conjecture 322](http://cms.uhd.edu/faculty/delavinae/research/wowII/open.html)
>
> Let `G` be a simple connected graph on `n ≥ 5` vertices. If the maximum over all
> vertices `v` of `l(v)` in the complement graph `Gᶜ` — the independence number of
> the neighborhood `N(v)` of `v` — is at most 1, then `G` is well totally dominated.
>
> Here `l(v) = α(Gᶜ[N(v)])` is the independence number of the subgraph induced by the
> open neighborhood of `v` in `Gᶜ`.
>
> This proof was provided by Samuel Schlesinger.

```lean
theorem conjecture322 (G : SimpleGraph α) [DecidableRel G.Adj] (_hG : G.Connected)
    (hn : 5 ≤ Fintype.card α)
    (h : ∀ v : α, indepNeighborsCard Gᶜ v ≤ 1) :
    IsWellTotallyDominated G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean)
- [E. DeLaViña, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.uhd.edu/faculty/delavinae/research/wowII/)
