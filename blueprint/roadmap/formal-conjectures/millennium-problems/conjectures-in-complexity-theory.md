---
declaration: theorem
origin: cited
lean: ComplexityTheory.P_ne_NP, ComplexityTheory.NP_ne_coNP, ComplexityTheory.P_eq_BPP, ComplexityTheory.coP_eq_P, ComplexityTheory.P_subset_NP, ComplexityTheory.P_subset_coNP, ComplexityTheory.P_subset_BPP
statement: formalized
---

# Conjectures in Complexity Theory

> This file contains formal statements of some of the main open conjectures
> in complexity theory, including
>
> - the P vs NP problem
> - the NP vs coNP problem
> - the P vs BPP problem
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/P_versus_NP_problem)
> - [The Clay Institute](https://www.claymath.org/millennium/p-vs-np/)

*Quoted from [FormalConjectures/Millennium/PvsNP.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 3 open and 4 textbook results.

## `ComplexityTheory.P_ne_NP`

Open: stated without proof.

> **P ≠ NP**:
>
> The conjecture that the complexity classes P and NP are not equal.

```lean
theorem P_ne_NP : P ≠ NP
```

Category `research open`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L45).

## `ComplexityTheory.NP_ne_coNP`

Open: stated without proof.

> **NP ≠ coNP**:
>
> The conjecture that the complexity classes NP and coNP are not equal.

```lean
theorem NP_ne_coNP : NP ≠ coNP
```

Category `research open`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L53).

## `ComplexityTheory.P_eq_BPP`

Open: stated without proof.

> **P = BPP**:
>
> The conjecture that the complexity classes P and BPP are equal.

```lean
theorem P_eq_BPP : P = BPP
```

Category `research open`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L61).

## `ComplexityTheory.coP_eq_P`

Textbook result, stated without proof.

> The theorem that the set of complements of languages in P is itself P.
>
> This can be proven by observing that the boolean negation function is computable in polynomial time,
> and that compositions of poly-time computable functions are also poly-time computable.

```lean
theorem coP_eq_P :
    { L | Lᶜ ∈ P } = P
```

Category `textbook`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L70).

## `ComplexityTheory.P_subset_NP`

Textbook result, stated without proof. A Lean proof is at [https://github.com/AItoBit/p-subset-np/blob/beaeee15c37af6efac518426e117861c00ff3acc/PSubsetNP.lean#L358](https://github.com/AItoBit/p-subset-np/blob/beaeee15c37af6efac518426e117861c00ff3acc/PSubsetNP.lean#L358).

> The theorem that P is a subset of NP.
>
> This can be proven by observing that for any language in P,
> we can construct a verifier that ignores the witness and simply runs the poly-time decider for the
> language.

```lean
theorem P_subset_NP :
    P ⊆ NP
```

Category `textbook`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L83).

## `ComplexityTheory.P_subset_coNP`

Textbook result, proved here.

> The theorem that P is a subset of coNP.

```lean
theorem P_subset_coNP :
    P ⊆ coNP
```

Category `textbook`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L91).

## `ComplexityTheory.P_subset_BPP`

Textbook result, stated without proof.

> The theorem that P is a subset of BPP.
>
> This can be proven by observing that for any language in P,
> we can construct a randomized decider that ignores the random bits
> and simply runs the poly-time decider for the language.

```lean
theorem P_subset_BPP :
    P ⊆ BPP
```

Category `textbook`; AMS [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Millennium/PvsNP.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/PvsNP.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/PvsNP.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/P_versus_NP_problem)
