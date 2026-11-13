---
declaration: theorem
origin: cited
lean: DisjointNPPairs.no_complete_disjoint_NP_pair, DisjointNPPairs.no_complete_disjoint_coNP_pair, DisjointNPPairs.no_complete_disjoint_NP_pair.variants.exists_of_NP_eq_coNP, DisjointNPPairs.no_complete_disjoint_NP_pair.variants.NP_ne_coNP, DisjointNPPairs.no_complete_disjoint_NP_pair.variants.pSeparable_of_P_eq_NP
statement: formalized
---

# Complete disjoint NP pairs

> *References:*
> * [Ra94] Razborov, A. A. (1994). "On provably disjoint NP-pairs." *BRICS Report Series*
>   RS-94-36; ECCC TR94-006.
> * [KMT03] Köbler, J., Messner, J., and Torán, J. (2003). "Optimal proof systems imply complete
>   sets for promise classes." *Inform. and Comput.* 184, pp. 71--92.
> * [GSSZ04] Glaßer, C., Selman, A. L., Sengupta, S., and Zhang, L. (2004). "Disjoint NP-pairs."
>   *SIAM J. Comput.* 33, pp. 1369--1416.
> * [Pu17] Pudlák, P. (2017). "Incompleteness in the finite domain." *Bull. Symbolic Logic* 23,
>   pp. 405--441. [arXiv:1601.01487](https://arxiv.org/abs/1601.01487)
> * [Kh22] Khaniki, E. (2022). "New relations and separations of conjectures about incompleteness
>   in the finite domain." *J. Symbolic Logic* 87, pp. 912--937.
>   [arXiv:1904.01362](https://arxiv.org/abs/1904.01362)

*Quoted from [FormalConjectures/Paper/DisjointNPPairs.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result. It also has 4 API statements, counted here but not shown.

## `DisjointNPPairs.no_complete_disjoint_NP_pair`

Open: stated without proof.

> **There is no complete disjoint NP pair** (Razborov [Ra94]; Pudlák's conjecture `DisjNP` [Pu17]).
>
> No disjoint NP pair is complete under polynomial-time many-one reductions of pairs. This is the
> strongest of the "incompleteness in the finite domain" conjectures: it implies that no
> length-optimal propositional proof system exists [Ra94, KMT03], hence `NP ≠ coNP` and `P ≠ NP`.
> Equivalently [Pu17], for every consistent polynomial-time axiomatized theory `T ⊇ S¹₂` some
> disjoint NP pair is not provably disjoint in `T`.

```lean
theorem no_complete_disjoint_NP_pair : ¬∃ A B : DecisionProblem, IsCompleteNPPair A B
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/DisjointNPPairs.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean#L113).

## `DisjointNPPairs.no_complete_disjoint_coNP_pair`

Open: stated without proof.

> **There is no complete disjoint coNP pair** (Pudlák's conjecture `DisjCoNP` [Pu17]).
>
> No disjoint coNP pair is complete under polynomial-time many-one reductions of pairs. This
> implies that `TFNP` has no complete problem and that `SAT` has no p-optimal proof system
> [Pu17, Kh22].

```lean
theorem no_complete_disjoint_coNP_pair : ¬∃ A B : DecisionProblem, IsCompleteCoNPPair A B
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/DisjointNPPairs.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean#L124).

## `DisjointNPPairs.no_complete_disjoint_NP_pair.variants.exists_of_NP_eq_coNP`

Solved: stated here without proof.

> **If `NP = coNP` then a complete disjoint NP pair exists** [GSSZ04, Pu17].
>
> The pair `(SAT, ¬SAT)` is then a disjoint NP pair, and every disjoint NP pair `(A, B)` reduces
> to it via a Cook–Levin reduction of `A` to `SAT`, since `B` is disjoint from `A`.

```lean
theorem no_complete_disjoint_NP_pair.variants.exists_of_NP_eq_coNP (h : NP = coNP) :
    ∃ A B : DecisionProblem, IsCompleteNPPair A B
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/DisjointNPPairs.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean#L134).

## `DisjointNPPairs.no_complete_disjoint_NP_pair.variants.NP_ne_coNP`

Proved here.

> **The conjecture implies `NP ≠ coNP`** [Pu17].

```lean
theorem no_complete_disjoint_NP_pair.variants.NP_ne_coNP
    (h : ¬∃ A B : DecisionProblem, IsCompleteNPPair A B) : NP ≠ coNP
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/DisjointNPPairs.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean#L142).

## `DisjointNPPairs.no_complete_disjoint_NP_pair.variants.pSeparable_of_P_eq_NP`

Textbook result, proved here.

> **If `P = NP` then every disjoint NP pair is P-separable**, and hence a complete pair exists:
> each `A` is then in `P` and separates `(A, B)`.

```lean
theorem no_complete_disjoint_NP_pair.variants.pSeparable_of_P_eq_NP (h : P = NP)
    {A B : DecisionProblem} (hAB : IsDisjointNPPair A B) : IsPSeparable A B
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/DisjointNPPairs.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/DisjointNPPairs.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/DisjointNPPairs.lean)
- [arXiv:1601.01487](https://arxiv.org/abs/1601.01487)
