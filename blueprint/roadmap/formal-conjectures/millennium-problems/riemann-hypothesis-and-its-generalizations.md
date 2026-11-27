---
declaration: theorem
origin: cited
lean: RiemannHypothesis.riemannHypothesis, GRH.generalized_riemann_hypothesis, ERH.extended_riemann_hypothesis
statement: formalized
---

# Riemann Hypothesis and its generalizations

> The Riemann Hypothesis asserts that all non-trivial zeros of the Riemann zeta function
> $\zeta(s)$ have real part $\frac{1}{2}$. The trivial zeros are the negative even integers
> $-2, -4, -6, \ldots$. The hypothesis is one of the seven Millennium Prize Problems
> posed by the Clay Mathematics Institute.
>
> The Generalized Riemann Hypothesis extends this to Dirichlet $L$-functions of primitive
> Dirichlet characters. The Extended Riemann Hypothesis extends it to Dedekind zeta functions of
> number fields.
>
> *References:*
> - [The Clay Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
> - L. Alpöge, [Note on the Riemann Hypothesis](https://alpo.ge/remark.pdf), 2026. Announces a
>   Lean proof of the Riemann Hypothesis and the Generalized Riemann Hypothesis.
> - [Wikipedia: Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis)
> - [Wikipedia: Generalized Riemann hypothesis](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
> - [Wikipedia: Dedekind zeta function](https://en.wikipedia.org/wiki/Dedekind_zeta_function)
> - J. Neukirch, *Algebraic Number Theory*, Springer (Grundlehren 322), 1999, Chapter VII, §5.
> - D. A. Marcus, *Number Fields*, Springer (GTM 81), 1977, Chapter VII.

*Quoted from [FormalConjectures/Millennium/RiemannHypothesis.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Millennium/RiemannHypothesis.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `RiemannHypothesis.riemannHypothesis`

Solved: stated here; a Lean proof is at [https://github.com/leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis).

> The **Riemann Hypothesis**: all non-trivial zeros of the Riemann zeta function have real
> part $\frac{1}{2}$. That is, if $\zeta(s) = 0$, $s \neq 1$, and $s$ is not a trivial zero
> $-2(n+1)$ for some $n \in \mathbb{N}$, then $\operatorname{Re}(s) = \frac{1}{2}$.
>
> This is the official Millennium Prize Problem as posed by the
> [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
>
> This uses the `RiemannHypothesis` type from Mathlib, which is defined as
> `∀ (s : ℂ), riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * (n + 1)) → s ≠ 1 → s.re = 1 / 2`.

```lean
theorem riemannHypothesis : RiemannHypothesis
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Millennium/RiemannHypothesis.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Millennium/RiemannHypothesis.lean#L59).

## `GRH.generalized_riemann_hypothesis`

Solved: stated here; a Lean proof is at [https://github.com/leanprover-community/riemann-hypothesis/blob/d27f71347abceb76cd37dc8a5fccbe556ec2be90/src/Main.lean#L54](https://github.com/leanprover-community/riemann-hypothesis/blob/d27f71347abceb76cd37dc8a5fccbe556ec2be90/src/Main.lean#L54).

> The **Generalized Riemann Hypothesis** asserts that all the non-trivial zeros of the
> Dirichlet $L$-function $L(\chi, s)$ of a primitive Dirichlet character $\chi$ have real part
> $\frac{1}{2}$.
>
> The linked proof states this for the zeros with $0 < \operatorname{Re}(s) < 1$. Our statement
> follows by combining it with the
> [bridge theorem](https://github.com/leanprover-community/riemann-hypothesis/blob/d27f71347abceb76cd37dc8a5fccbe556ec2be90/comparator/FormalConjecturesBridge.lean#L152).

```lean
theorem generalized_riemann_hypothesis (q : ℕ) [NeZero q] (χ : DirichletCharacter ℂ q)
    (hχ : χ.IsPrimitive) (s : ℂ) (hs : χ.LFunction s = 0)
    (hs_nontrivial : s ∉ Int.cast '' trivialZeros χ) :
    s.re = 1 / 2
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Millennium/RiemannHypothesis.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Millennium/RiemannHypothesis.lean#L87).

## `ERH.extended_riemann_hypothesis`

Open: stated without proof.

> The **Extended Riemann Hypothesis**: for every number field $K$, all zeros of the Dedekind
> zeta function $\zeta_K$ in the critical strip $0 < \operatorname{Re} s < 1$ have real part
> $\frac{1}{2}$.

```lean
theorem extended_riemann_hypothesis (K : Type*) [Field K] [NumberField K] :
    ExtendedRiemannHypothesis K
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Millennium/RiemannHypothesis.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Millennium/RiemannHypothesis.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/RiemannHypothesis.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Millennium/RiemannHypothesis.lean)
- [The Clay Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
