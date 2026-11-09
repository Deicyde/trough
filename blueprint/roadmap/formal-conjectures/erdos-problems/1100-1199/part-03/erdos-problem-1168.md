---
declaration: theorem
origin: cited
lean: Erdos1168.erdos_1168, Erdos1168.erdos_1168.variants.under_GCH
statement: formalized
---

# Erdős Problem 1168

> *References:*
> * [erdosproblems.com/1168](https://www.erdosproblems.com/1168)
> * [EHR65] Erdős, P., Hajnal, A. and Rado, R., *Partition relations for cardinal numbers*.
>   Acta Math. Acad. Sci. Hungar. (1965), pp. 93–196.

*Quoted from [FormalConjectures/ErdosProblems/1168.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1168.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1168](https://www.erdosproblems.com/1168).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos1168.erdos_1168`

Open: stated without proof.

> **Erdős Problem 1168.** Prove that
> $$\aleph_{\omega+1} \not\to (\aleph_{\omega+1}, \underbrace{3, 3, \ldots}_{\aleph_0})^2_{\aleph_0}$$
> without assuming the generalized continuum hypothesis.
>
> A problem of Erdős, Hajnal, and Rado [EHR65]: the negative arrow is known under GCH;
> the open problem asks for a ZFC proof. Here `ω = Ordinal.omega0`, so `ℵ_ (ω + 1)` is
> the successor cardinal of the singular `ℵ_ω`.

```lean
theorem erdos_1168 : ¬ CardinalCountableColorRamsey (ℵ_ (ω + 1))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1168.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1168.lean#L46).

## `Erdos1168.erdos_1168.variants.under_GCH`

Solved: stated here without proof.

> **Erdős–Hajnal–Rado theorem under GCH** [EHR65]: the negative partition relation
> $\aleph_{\omega+1} \not\to (\aleph_{\omega+1}, 3, 3, \ldots)^2_{\aleph_0}$ holds
> assuming GCH.

```lean
theorem under_GCH (hGCH : GCH) : ¬ CardinalCountableColorRamsey (ℵ_ (ω + 1))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1168.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1168.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1168.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1168.lean)
- [erdosproblems.com/1168](https://www.erdosproblems.com/1168)
