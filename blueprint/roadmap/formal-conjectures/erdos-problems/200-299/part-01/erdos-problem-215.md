---
declaration: theorem
origin: cited
lean: Erdos215.erdos_215
statement: formalized
---

# Erdős Problem 215

> *References:*
> - [erdosproblems.com/215](https://www.erdosproblems.com/215)
> - [Er83c] Erdős, Paul, *Combinatorial problems in geometry*. Math. Chronicle (1983), 35-54.
> - [JaMa02] Jackson, Steve and Mauldin, R. Daniel, *Sets meeting isometric copies of the lattice
>   $\mathbb{Z}^2$ in exactly one point*. Proc. Natl. Acad. Sci. USA (2002), 15883-15887.

*Quoted from [FormalConjectures/ErdosProblems/215.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/215.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/215](https://www.erdosproblems.com/215).

The file states 1 research or textbook statement: 1 solved.

## `Erdos215.erdos_215`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos215.lean#L55](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos215.lean#L55).

> Does there exist $S\subseteq \mathbb{R}^2$ such that every set congruent to $S$ (that is, $S$
> after some translation and rotation) contains exactly one point from $\mathbb{Z}^2$?
>
> An old question of Steinhaus. Erdős was 'almost certain that such a set does not exist'.
>
> In fact, such a set does exist, as proved by Jackson and Mauldin [JaMa02]. Their construction
> depends on the axiom of choice.
>
> The plane is identified with $\mathbb{C}$: the sets congruent to $S$ are the sets $uS + t$ with
> $\lvert u\rvert = 1$ and $t \in \mathbb{C}$, and $\mathbb{Z}^2$ is the set of Gaussian integers.

```lean
theorem erdos_215 : ∃ S : Set ℂ, ∀ u t : ℂ, ‖u‖ = 1 →
    ∃! z : ℂ, z ∈ (fun w => u * w + t) '' S ∧ ∃ a b : ℤ, z = a + b * Complex.I
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/215.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/215.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/215.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/215.lean)
- [erdosproblems.com/215](https://www.erdosproblems.com/215)
