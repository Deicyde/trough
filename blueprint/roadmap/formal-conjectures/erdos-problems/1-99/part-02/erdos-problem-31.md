---
declaration: theorem
origin: cited
lean: Erdos31.erdos_31
statement: formalized
---

# Erdős Problem 31

> *References:*
> - [erdosproblems.com/31](https://www.erdosproblems.com/31)
> - [Er56] Erdős, P., *Problems and results in additive number theory*. Colloque sur la Théorie des
>   Nombres, Bruxelles, 1955 (1956), 127-137.
> - [Er59] Erdős, P., *Über einige Probleme der additiven Zahlentheorie*. Sammelband zu Ehren des 250.
>   Geburtstages Leonhard Eulers (1959), 116-119.
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of combinatorial
>   theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.
> - [Lo54] Lorentz, G. G., *On a problem of additive number theory*. Proc. Amer. Math. Soc.
>   (1954), 838-841.

*Quoted from [FormalConjectures/ErdosProblems/31.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/31.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/31](https://www.erdosproblems.com/31).

The file states 1 research or textbook statement: 1 solved.

## `Erdos31.erdos_31`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos31.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos31.lean).

> Given any infinite set $A\subset \mathbb{N}$ there is a set $B$ of density $0$ such that $A+B$ contains all except finitely many integers.
>
> Conjectured by Erdős and Straus. Proved by Lorentz [Lo54].

```lean
theorem erdos_31 : ∀ A : Set ℕ, A.Infinite →
    ∃ B : Set ℕ, B.HasDensity 0 ∧ ∀ᶠ n in atTop, n ∈ A + B
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/31.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/31.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/31.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/31.lean)
- [erdosproblems.com/31](https://www.erdosproblems.com/31)
