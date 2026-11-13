---
declaration: theorem
origin: cited
lean: OeisA1818.conjecture1, OeisA1818.conjecture2
statement: formalized
---

# Squares of double factorials

> Squares of double factorials: $a(n) = ((2n-1)!!)^2 = (1 \cdot 3 \cdot 5 \cdots (2n-1))^2$.
>
> *References:*
> - [A001818](https://oeis.org/A001818)
> - [She, Sun, Xia, *A novel permanent identity with applications*, Theorem 1.3(ii)](https://arxiv.org/abs/2208.12167)
> - [Yang, Zhang, *Sun-type determinant and permanent congruences*, Proposition 17](https://arxiv.org/abs/2605.19502)

*Quoted from [FormalConjectures/OEIS/1818.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1818.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA1818.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A001818.lean#L7753](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A001818.lean#L7753).

> Conjecture 1: For any primitive $2n$-th root $\zeta$ of unity, the permanent of the $2n \times 2n$
> matrix $[m(j,k)]_{j,k=1..2n}$ coincides with $a(n) = ((2n-1)!!)^2$, where $m(j,k)$ is
> $(1+\zeta^{j-k})/(1-\zeta^{j-k})$ if $j \neq k$, and $1$ otherwise.
> - Zhi-Wei Sun, Dec 21 2021
>
> Proved by She, Sun and Xia, Theorem 1.3(ii) in the reference above.
> Lean formalization by Wentao Li, with AI assistance.

```lean
theorem conjecture1 (n : ℕ) (hn : 1 ≤ n) :
    ∀ (ζ : ℂ), IsPrimitiveRoot ζ (2 * n) →
      Matrix.permanent (fun (i j : Fin (2 * n)) =>
        if i = j then
          (1 : ℂ)
        else
          (1 + ζ ^ (i.val - j.val : ℤ)) / (1 - ζ ^ (i.val - j.val : ℤ))
      ) = (a n : ℂ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/1818.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1818.lean#L83).

## `OeisA1818.conjecture2`

Solved: stated here without proof.

> Conjecture 2: Let $p$ be an odd prime. Then the permanent of the $(p-1) \times (p-1)$ matrix
> $[f(j,k)]_{j,k=1..p-1}$ is congruent to $a((p-1)/2) = ((p-2)!!)^2 \pmod{p^2}$,
> where $f(j,k)$ is $(j+k)/(j-k)$ if $j \neq k$, and $f(j,k) = 1$ otherwise.
> - Zhi-Wei Sun, Dec 22 2021

```lean
theorem conjecture2 {p : ℕ} (hp : p.Prime) (h_odd : p ≠ 2) :
    let N : ℕ := p - 1
    let R := ZMod (p ^ 2)
    let Idx := Fin N
    let M : Matrix Idx Idx R := fun i j => fEntry (i.val + 1) (j.val + 1)
    (M.permanent : R) = (a ((p - 1) / 2) : R)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/1818.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1818.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1818.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1818.lean)
- [A001818](https://oeis.org/A001818)
