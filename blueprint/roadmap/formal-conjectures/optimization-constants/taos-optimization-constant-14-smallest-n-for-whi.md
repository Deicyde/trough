---
declaration: theorem
origin: cited
lean: Constant14.c14_ge_4, Constant14.c14_ge_5, Constant14.c14_lower_bound, Constant14.c14_lower_bound_improved, Constant14.c14_le_7910, Constant14.c14_le_748, Constant14.c14_le_432, Constant14.c14_upper_bound, Constant14.c14_upper_bound_improved, Constant14.c14_le_20
statement: formalized
---

# Tao's Optimization Constant 14 / Smallest $n$ for which the value of $BB(n)$ is undecidable

> *References:*
> - [Tao's Optimization Constant 14](https://teorth.github.io/optimizationproblems/constants/14a.html)
> - [LS1965] Lin, S. and Radó, T., [*Computer studies of Turing machine
>   problems*](https://doi.org/10.1145/321264.321270). J. ACM **12** (1965), 196–212.
> - [B1983] Brady, A. H., [*The determination of Radó's noncomputable function $\Sigma(k)$ for
>   four-state Turing machines*](https://docs.bbchallenge.org/papers/Brady1983.pdf).
>   Math. Comp. 40 (1983), 647–665.
> - [BB2025] Blanchard, J. et al., *Determination of the fifth Busy Beaver value* (2025).
>   [arXiv:2509.12337](https://arxiv.org/abs/2509.12337)
> - [YS2016] Yedidia, A. and Aaronson, S., *A relatively small Turing machine whose behavior is
>   independent of set theory* (2016). [arXiv:1605.04343](https://arxiv.org/abs/1605.04343)
> - [O2016] O'Rear, S.,
>   [*metamath-turing-machines*](https://github.com/sorear/metamath-turing-machines) (2016).
> - [W2025] Wade, A. J.,
>   [*turing_machine_explorer*](https://codeberg.org/ajwade/turing_machine_explorer) (2025).
> - [G2026] Glazer, E., [*K230: a 230-state Turing machine for the consistency of
>   ZFC*](https://github.com/elliotglazer/k230-rocq) (2026).
>   [Announcement](https://x.com/ElliotGlazer/status/2112179703687856497)
> - [A2020] Aaronson, S., [*The Busy Beaver
>   Frontier*](https://doi.org/10.1145/3427361.3427369). ACM SIGACT News **51** (2020), 32–54.
>
> This file defines the smallest $n$ for which the value of $BB(n)$ is undecidable. More precisely,
> it formalizes the least number of states for which ZFC can neither prove nor disprove that a
> specific Turing machine halts. Its existence and known upper bounds follow from Gödel's second
> incompleteness theorem.
>
> We do this by modeling a version of first order logic, ZFC and Turing machines within Lean.
> The implementation of FOL and ZFC is taken from the
> [FormalizedLogicLean](https://github.com/FormalizedFormalLogic/Foundation) project.
> The implementation is copied and minimized from that project. It is not necessary to read it to
> understand the definition of `C14`. The copied definitions span the section
> `FormalizedFormalLogic`. Confidence in that implementation partly comes from the large body of
> proofs developed with it, including formalizations of independence theorems.
>
> This is followed by a model of Turing machines within the first-order logic framework, developed
> for Formal Conjectures in the section `BackgroundDefs`. The file then defines `C14` and states its
> known bounds and related conjectures. The known bounds use `sorry`; formalizing one would be a
> substantial achievement.

*Quoted from [FormalConjectures/OptimizationConstants/14.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 3 open and 7 solved.

## `Constant14.c14_ge_4`

Solved: stated here without proof.

> Proven by Lin and Radó in [LS1965] by computing $BB(3) = 21$.

```lean
theorem c14_ge_4 : 4 ≤ C14
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1729](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1729).

## `Constant14.c14_ge_5`

Solved: stated here without proof.

> An intermediate lower bound, proved by Brady in [B1983] by explicitly computing
> $BB(4) = 107$.

```lean
theorem c14_ge_5 : 5 ≤ C14
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1734](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1734).

## `Constant14.c14_lower_bound`

Solved: stated here without proof.

> The current best known lower bound, proved by Blanchard et al. in [BB2025] by explcitily computing
> $BB(5) = 47176870$.
>
> Note $BB(5) = 47176870$ (as well as the values below) has been formally proven in Rocq as part of
> [BB2025], a formal proof of the declaration below would likely be much more difficult on a technical
> level than the proof in Rocq, which is based on dependent type theory.

```lean
theorem c14_lower_bound : 6 ≤ C14
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1743](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1743).

## `Constant14.c14_lower_bound_improved`

Open: stated without proof.

> Can the current best lower bound be improved?

```lean
theorem c14_lower_bound_improved : 6 < C14
```

Category `research open`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1747](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1747).

## `Constant14.c14_le_7910`

Solved: stated here without proof.

> The first known upper bound, proved by Yedidia and Aaronson in [YS2016]. Their construction
> reduces the independence problem to a graph-theoretic setting.

```lean
theorem c14_le_7910 : C14 ≤ 7910
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1752](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1752).

## `Constant14.c14_le_748`

Solved: stated here without proof.

> An intermediate upper bound, proved by O'Rear in [O2016]. It uses a Turing machine that
> enumerates proofs in ZF.

```lean
theorem c14_le_748 : C14 ≤ 748
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1757](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1757).

## `Constant14.c14_le_432`

Solved: stated here without proof.

> An intermediate upper bound, proved by Wade in [W2025]. It refines the proof-enumerating
> machine construction from [O2016].

```lean
theorem c14_le_432 : C14 ≤ 432
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1762](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1762).

## `Constant14.c14_upper_bound`

Solved: stated here without proof.

> The current best known upper bound, from [G2026]. Glazer proved in Rocq, without axioms, that
> a certain 230-state Turing machine halts if and only if ZFC is inconsistent.

```lean
theorem c14_upper_bound : C14 ≤ 230
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1767](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1767).

## `Constant14.c14_upper_bound_improved`

Open: stated without proof.

> Can the current best upper bound be improved?

```lean
theorem c14_upper_bound_improved : C14 < 230
```

Category `research open`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1771](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1771).

## `Constant14.c14_le_20`

Open: stated without proof.

> Conjecture 11 in [A2020] by Scott Aaronson

```lean
theorem c14_le_20 : C14 ≤ 20
```

Category `research open`; AMS [03 Mathematical logic and foundations](../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/OptimizationConstants/14.lean, line 1775](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean#L1775).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OptimizationConstants/14.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/14.lean)
- [Tao's Optimization Constant 14](https://teorth.github.io/optimizationproblems/constants/14a.html)
