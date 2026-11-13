---
declaration: theorem
origin: cited
lean: BranchingVAS.reachability_decidable
statement: formalized
---

# Decidability of reachability for branching vector addition systems

> A *branching vector addition system* (BVAS) of dimension `d` is given by a finite
> list of *axioms*, a finite list of *unary rules*, and a finite list of *binary
> rules*, each of which is a vector in `ℤ^d`. A *configuration* is a vector in `ℕ^d`,
> which here is represented as a vector `v ∈ ℤ^d` subject to `0 ≤ v`. The set of
> *reachable* configurations is defined inductively:
>
> * every axiom that is a valid configuration (i.e. lies in `ℕ^d`) is reachable;
> * if `v` is a reachable configuration, `r` is a unary rule and `v + r ∈ ℕ^d`, then
>   `v + r` is reachable;
> * if `v₁, v₂` are both reachable configurations, `r` is a binary rule and
>   `v₁ + v₂ + r ∈ ℕ^d`, then `v₁ + v₂ + r` is reachable.
>
> Modelling axioms as vectors in `ℤ^d` and only counting the non-negative ones as
> reachable yields the same set of reachable configurations as the usual definition
> in which axioms are required to lie in `ℕ^d`.
>
> Branching vector addition systems are distinguished from ordinary vector addition systems (VAS) by allowing binary rules. VAS reachability is known to be decidable.
>
> *References:*
> - [The covering and boundedness problems for branching vector addition systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2009.2317)
>   (*Stéphane Demri, Marcin Jurdziński, Oded Lachish, Ranko Lazić*, FSTTCS 2009)
>   Gives a similar definition of BVAS, and compares it to related equivalent definitions.
> - [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.22)
>   by *Clotilde Bizière, Thibault Hilaire, Jérôme Leroux, Grégoire Sutre*, MFCS 2025, which
>   settles the two-dimensional case and states that "the decidability status of the reachability
>   problem for BVASS remains open in higher dimensions".
> - [The General Vector Addition System Reachability Problem by Presburger Inductive
>   Invariants](https://arxiv.org/abs/1009.1076) by *Jérôme Leroux* (2010), for the decidability
>   of reachability for ordinary VAS.
> - [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear
>   Inductive Invariants](https://arxiv.org/abs/2607.09558) by *Clotilde Bizière, Jérôme Leroux,
>   Grégoire Sutre* (2026), a recent preprint claiming a positive resolution to the conjecture:
>   reachability for branching vector addition systems is decidable.

*Quoted from [FormalConjectures/Paper/BranchingVAS.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/BranchingVAS.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 4 test statements and 3 API statements, counted here but not shown.

## `BranchingVAS.reachability_decidable`

Solved: stated here without proof.

> The reachability problem for branching vector addition systems is decidable.
>
> That is, the predicate taking a dimension `d`, a branching vector addition system `b` of
> dimension `d` and a target vector `t ∈ ℤ^d`, and returning whether `t` is reachable in `b`, is
> a computable predicate. Note that the dimension is part of the input: a single algorithm must
> work for all dimensions.
>
> As of August 2026, the solution is quite recently announced and is not
> yet peer-reviewed.

```lean
theorem reachability_decidable :
    ComputablePred fun p : Σ d : ℕ, Bvas d × (Fin d → ℤ) => p.2.1.Reachable p.2.2
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/BranchingVAS.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/BranchingVAS.lean#L143).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/BranchingVAS.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/BranchingVAS.lean)
- [The covering and boundedness problems for branching vector addition systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2009.2317)
