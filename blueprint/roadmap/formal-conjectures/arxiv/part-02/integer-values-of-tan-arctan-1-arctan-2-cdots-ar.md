---
declaration: theorem
origin: cited
lean: Arxiv.«2607.05739».tan_arctan_sum_not_integer, Arxiv.«2607.05739».x_succ, Arxiv.«2607.05739».x_eq_tan_sum_arctan, Arxiv.«2607.05739».kernel_dvd_of_eq_intCast, Arxiv.«2607.05739».exists_near_half_pi, Arxiv.«2607.05739».exceptional_ncard_le
statement: formalized
---

# Integer values of $\tan(\arctan 1 + \arctan 2 + \cdots + \arctan n)$

> *References:*
> - [arxiv/2607.05739](https://arxiv.org/abs/2607.05739)
>   **Integer values of $\tan(\arctan 1+\arctan 2+\cdots+\arctan n)$ are rare** by *Ken Ono*
> - [AMM08] T. Amdeberhan, L. A. Medina, and V. H. Moll, *Arithmetical properties of a sequence
>   arising from an arctangent sum*, J. Number Theory 128 (2008), no. 6, 1807-1846.
> - [TanArctan](https://github.com/AxiomMath/TanArctan), a Lean formalisation of the three
>   results of [Ono26], MIT licensed. Its `P`, `A`, `B` and `x` are the definitions used
>   here.

*Quoted from [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open, 3 solved and 2 textbook results. It also has 3 test statements, counted here but not shown.

## `Arxiv.«2607.05739».tan_arctan_sum_not_integer`

Open: stated without proof.

> **Conjecture (Amdeberhan-Medina-Moll, 2008).** For every integer $n \geq 5$, the value
>
> $$x_n = \tan(\arctan 1 + \arctan 2 + \cdots + \arctan n)$$
>
> is not an integer.

```lean
theorem tan_arctan_sum_not_integer :
    ∀ n : ℕ, 5 ≤ n → ¬ IsIntegerValue n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L67).

## `Arxiv.«2607.05739».x_succ`

Textbook result, stated without proof.

> $x_n$ satisfies $x_1 = 1$ and $x_n = \dfrac{x_{n-1} + n}{1 - n x_{n-1}}$, which is the
> tangent addition formula.

```lean
theorem x_succ (n : ℕ) (hn : 1 ≤ n) :
    x (n + 1) = (x n + (n + 1)) / (1 - (n + 1) * x n)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L74).

## `Arxiv.«2607.05739».x_eq_tan_sum_arctan`

Textbook result, stated without proof.

> $x_n$ is the tangent of the partial sum of arctangents it is named for.

```lean
theorem x_eq_tan_sum_arctan (n : ℕ) (hn : 1 ≤ n) :
    (x n : ℝ) = Real.tan (∑ k ∈ Finset.Icc 1 n, Real.arctan k)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L80).

## `Arxiv.«2607.05739».kernel_dvd_of_eq_intCast`

Solved: stated here; a Lean proof is at [https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L176](https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L176).

> An integer value is divisible in a way that forces it to be large: if $x_n = m$ then
> $K_n \mid 1 + m^2$, and $|m| \geq \sqrt{K_n - 1}$ once $K_n > 1$.

```lean
theorem kernel_dvd_of_eq_intCast {n : ℕ} (hn : 1 ≤ n) (hA : A n ≠ 0) {m : ℤ}
    (hx : x n = (m : ℚ)) :
    ((kernel n : ℤ) ∣ (1 + m ^ 2)) ∧
      (1 < kernel n → Real.sqrt ((kernel n : ℝ) - 1) ≤ |(m : ℝ)|)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L106).

## `Arxiv.«2607.05739».exists_near_half_pi`

Solved: stated here; a Lean proof is at [https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L453](https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L453).

> Every exceptional index sits close to a multiple of $\pi/2$ in angle.

```lean
theorem exists_near_half_pi {n : ℕ} (hn : n ∈ exceptional) :
    ∃ j : ℤ, |angleSum n - (j : ℝ) * (Real.pi / 2)| < 2 / (n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L116).

## `Arxiv.«2607.05739».exceptional_ncard_le`

Solved: stated here; a Lean proof is at [https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L975](https://github.com/AxiomMath/TanArctan/blob/5382d3c20ee3f30e2cbd84362eb07a7e93250348/output/solution.lean#L975).

> The exceptional indices are sparse: $\#(E \cap [1,N]) = O(\log N)$. This is the sense in
> which integer values are rare, and it is what [Ono26] proves.

```lean
theorem exceptional_ncard_le : ∃ (C : ℝ) (N₀ : ℕ), 0 < C ∧ ∀ N : ℕ, N₀ ≤ N →
    ((exceptional ∩ Set.Icc 1 N).ncard : ℝ) ≤ C * Real.log N
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean#L125).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.05739/TanArctanSum.lean)
- [arxiv/2607.05739](https://arxiv.org/abs/2607.05739)
