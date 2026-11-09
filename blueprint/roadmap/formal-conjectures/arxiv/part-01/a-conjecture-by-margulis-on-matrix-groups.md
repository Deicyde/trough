---
declaration: theorem
origin: cited
lean: Margulis.conjecture_1_1, Margulis.huang_shi_theorem_1_2
statement: formalized
---

# A conjecture by Margulis on matrix groups

> *Reference:* [arxiv/2504.17644v3](https://arxiv.org/abs/2504.17644v3)
> **Bounded diagonal orbits in homogeneous spaces over function fields**
> by *Qianlin Huang, Ronggang Shi*

*Quoted from [FormalConjectures/Arxiv/2504.17644/Margulis.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2504.17644/Margulis.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Margulis.conjecture_1_1`

Open: stated without proof.

> Let `D` be the diagonal group of `SL_n(ℝ)` where n ≥ 3.
> Then any relatively compact `D`-orbit in `SL_n(ℝ) / SL_n(ℤ)` is closed.

```lean
theorem conjecture_1_1 {n : ℕ} (hn : 3 ≤ n)
    (g : SL(n, ℝ) ⧸ Subgroup.map (map (Int.castRingHom ℝ)) ⊤)
    (hg : IsCompact <| closure (MulAction.orbit (diagonalSubgroup (Fin n) ℝ) g)) :
    IsClosed <| MulAction.orbit (diagonalSubgroup (Fin n) ℝ) g
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [22 Topological groups, Lie groups](../../by-subject/part-01/22-topological-groups-lie-groups/README.md). Declared in [FormalConjectures/Arxiv/2504.17644/Margulis.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2504.17644/Margulis.lean#L42).

## `Margulis.huang_shi_theorem_1_2`

Solved: stated here without proof.

> **Huang–Shi, Theorem 1.2**
>
> Let `F` be a finite field of characteristic `p ∈ {3, 5, 7, 11}`, and set
> `K = F((t⁻¹))`, `A = F[t]`. Here `K` is modelled by the Laurent series field `F⸨X⸩` with
> `X = t⁻¹`, so that `A` is embedded via `t ↦ X⁻¹`. Let
>
> * `D` be the diagonal subgroup of `SL₄(K)`,
> * `Γ = SL₄(A)` the lattice subgroup embedded into `SL₄(K)` via the natural inclusion `A →+* K`.
>
> Then there exists `z : SL₄(K)/Γ` such that the `D`-orbit of `z` has compact
> closure but is not closed.

```lean
theorem huang_shi_theorem_1_2
    (hchar : ringChar F ∈ ({3, 5, 7, 11} : Finset ℕ)) :
    ∃ z : SL(4, F⸨X⸩) ⧸ (  Matrix.SpecialLinearGroup.map
    (polyToLaurent F)).range,
      IsCompact (closure (MulAction.orbit (diagonalSubgroup (Fin 4) (F⸨X⸩)) z)) ∧
      ¬ IsClosed (MulAction.orbit (diagonalSubgroup (Fin 4) (F⸨X⸩)) z)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [22 Topological groups, Lie groups](../../by-subject/part-01/22-topological-groups-lie-groups/README.md). Declared in [FormalConjectures/Arxiv/2504.17644/Margulis.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2504.17644/Margulis.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2504.17644/Margulis.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2504.17644/Margulis.lean)
- [arxiv/2504.17644v3](https://arxiv.org/abs/2504.17644v3)
