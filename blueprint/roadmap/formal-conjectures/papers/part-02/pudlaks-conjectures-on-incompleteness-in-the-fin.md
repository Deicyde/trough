---
declaration: theorem
origin: cited
lean: PudlakFiniteDomain.sat_no_p_optimal_proof_system, PudlakFiniteDomain.tfnp_no_complete_problem, PudlakFiniteDomain.up_no_complete_language, PudlakFiniteDomain.np_inter_conp_no_complete_language, PudlakFiniteDomain.tfnp_no_complete_problem.variants.exists_of_NP_eq_coNP, PudlakFiniteDomain.tfnp_no_complete_problem.variants.NP_ne_coNP, PudlakFiniteDomain.sat_no_p_optimal_proof_system.variants.exists_of_P_eq_NP
statement: formalized
---

# Pudlák's conjectures on incompleteness in the finite domain

> *References:*
> * [CR79] Cook, S. A. and Reckhow, R. A. (1979). "The relative efficiency of propositional proof
>   systems." *J. Symbolic Logic* 44, pp. 36--50.
> * [HH88] Hartmanis, J. and Hemachandra, L. A. (1988). "Complexity classes without machines: on
>   complete languages for UP." *Theoret. Comput. Sci.* 58, pp. 129--142.
> * [KP89] Krajíček, J. and Pudlák, P. (1989). "Propositional proof systems, the consistency of
>   first order theories and the complexity of computations." *J. Symbolic Logic* 54,
>   pp. 1063--1079.
> * [MP91] Megiddo, N. and Papadimitriou, C. H. (1991). "On total functions, existence theorems
>   and computational complexity." *Theoret. Comput. Sci.* 81, pp. 317--324.
> * [Pa94] Papadimitriou, C. H. (1994). "On the complexity of the parity argument and other
>   inefficient proofs of existence." *J. Comput. System Sci.* 48, pp. 498--532.
> * [KMT03] Köbler, J., Messner, J., and Torán, J. (2003). "Optimal proof systems imply complete
>   sets for promise classes." *Inform. and Comput.* 184, pp. 71--92.
> * [Pu17] Pudlák, P. (2017). "Incompleteness in the finite domain." *Bull. Symbolic Logic* 23,
>   pp. 405--441. [arXiv:1601.01487](https://arxiv.org/abs/1601.01487)
> * [Kh22] Khaniki, E. (2022). "New relations and separations of conjectures about incompleteness
>   in the finite domain." *J. Symbolic Logic* 87, pp. 912--937.
>   [arXiv:1904.01362](https://arxiv.org/abs/1904.01362)

*Quoted from [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 4 open, 2 solved and 1 textbook result. It also has 4 API statements, counted here but not shown.

## `PudlakFiniteDomain.sat_no_p_optimal_proof_system`

Open: stated without proof.

> **SAT has no p-optimal proof system** (Pudlák's conjecture `SAT` [Pu17]).
>
> No proof system for `SAT` p-simulates every other proof system for `SAT`. Since the existence of
> a p-optimal proof system depends only on the polynomial-time many-one degree of the language
> [KMT03], the conjecture is stated here for an arbitrary NP-complete language. Equivalently
> [Pu17], for every consistent polynomial-time axiomatized theory `T ⊇ S¹₂` there is a proof
> system for `SAT` whose soundness `T` cannot prove.

```lean
theorem sat_no_p_optimal_proof_system (L : DecisionProblem) (hL : IsCompleteFor NP L) :
    ¬∃ P : List Bool → List Bool, IsPOptimalProofSystem L P
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L137).

## `PudlakFiniteDomain.tfnp_no_complete_problem`

Open: stated without proof.

> **TFNP has no complete problem** (Megiddo–Papadimitriou [MP91]; Pudlák's conjecture `TFNP`
> [Pu17]).
>
> No total NP search problem is complete under polynomial-time many-one reductions of search
> problems. Equivalently [Pu17], for every consistent polynomial-time axiomatized theory
> `T ⊇ S¹₂` some total NP search problem is not polynomially reducible to any total NP
> search problem provably total in `T`.

```lean
theorem tfnp_no_complete_problem : ¬∃ T : TFNPProblem, T.IsComplete
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L151).

## `PudlakFiniteDomain.up_no_complete_language`

Open: stated without proof.

> **UP has no complete language** (Hartmanis–Hemachandra [HH88]; Pudlák's conjecture `UP`
> [Pu17]).
>
> No language accepted by an unambiguous polynomial-time verifier is complete for `UP` under
> polynomial-time many-one reductions.

```lean
theorem up_no_complete_language : ¬∃ L : DecisionProblem, IsCompleteFor UP L
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L162).

## `PudlakFiniteDomain.np_inter_conp_no_complete_language`

Open: stated without proof.

> **NP ∩ coNP has no complete language** (Pudlák's conjecture `NP ∩ coNP` [Pu17]).
>
> No language in `NP ∩ coNP` is complete for that class under polynomial-time many-one
> reductions.

```lean
theorem np_inter_conp_no_complete_language :
    ¬∃ L : DecisionProblem, IsCompleteFor (NP ∩ coNP) L
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L172).

## `PudlakFiniteDomain.tfnp_no_complete_problem.variants.exists_of_NP_eq_coNP`

Solved: stated here without proof.

> **If `NP = coNP` then TFNP has a complete problem** [MP91, Pu17].
>
> Under `NP = coNP` the search problem "given a CNF, find a satisfying assignment or a short
> proof of unsatisfiability" is total and complete.

```lean
theorem tfnp_no_complete_problem.variants.exists_of_NP_eq_coNP (h : NP = coNP) :
    ∃ T : TFNPProblem, T.IsComplete
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L183).

## `PudlakFiniteDomain.tfnp_no_complete_problem.variants.NP_ne_coNP`

Proved here.

> **The conjecture implies `NP ≠ coNP`** [Pu17].

```lean
theorem tfnp_no_complete_problem.variants.NP_ne_coNP
    (h : ¬∃ T : TFNPProblem, T.IsComplete) : NP ≠ coNP
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 191](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L191).

## `PudlakFiniteDomain.sat_no_p_optimal_proof_system.variants.exists_of_P_eq_NP`

Textbook result, stated without proof.

> **If `P = NP` then every NP-complete language has a p-optimal proof system.**
>
> The map sending `π` to itself when `π ∈ L` and to a fixed element of `L` otherwise is then
> polynomial-time, and every proof system `Q` for `L` is p-simulated by it via `Q` itself.

```lean
theorem sat_no_p_optimal_proof_system.variants.exists_of_P_eq_NP (h : P = NP)
    (L : DecisionProblem) (hL : IsCompleteFor NP L) (hne : ∃ y, L y = true) :
    ∃ P : List Bool → List Bool, IsPOptimalProofSystem L P
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean#L202).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PudlakFiniteDomainConjectures.lean)
- [arXiv:1601.01487](https://arxiv.org/abs/1601.01487)
