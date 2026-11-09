---
declaration: theorem
origin: cited
lean: Erdos590.erdos_590, Erdos590.erdos_590.variants.two, Erdos590.erdos_590.variants.ge_three_false, Erdos590.erdos_590.variants.finite_cardinal
statement: formalized
---

# Erdős Problem 590

> *References:*
>  - [erdosproblems.com/590](https://www.erdosproblems.com/590)
>  - [Ch72] Chang, C. C., A partition theorem for the complete graph on {$\omega\sp{\omega }$}. J. Combinatorial Theory Ser. A (1972), 396-452.
>  - [Sp57] Specker, Ernst, Teilmengen von Mengen mit Relationen. Comment. Math. Helv. (1957), 302-314.
>  - [La73] Larson, Jean A., A short proof of a partition theorem for the ordinal {$\omega \sp{\omega }$}. Ann. Math. Logic (1973/74), 129-145.

*Quoted from [FormalConjectures/ErdosProblems/590.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/590](https://www.erdosproblems.com/590).

The file states 4 research or textbook statements: 4 solved.

## `Erdos590.erdos_590`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos590.lean#L7928](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos590.lean#L7928).

> Let $α$ be the infinite ordinal $\omega^{\omega}$. It was proved by Chang [Ch72] that any red/blue
> colouring of the edges of $K_α$ there is either a red $K_α$ or a blue $K_3$.

```lean
theorem erdos_590 : OrdinalCardinalRamsey (ω ^ ω) (ω ^ ω) 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/590.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean#L44).

## `Erdos590.erdos_590.variants.two`

Solved: stated here without proof.

> Specker [Sp57] proved that when $α=ω^2$ any red/blue
> colouring of the edges of $K_α$ there is either a red $K_α$ or a blue $K_3$.

```lean
theorem erdos_590.variants.two : OrdinalCardinalRamsey (ω ^ 2) (ω ^ 2) 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/590.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean#L52).

## `Erdos590.erdos_590.variants.ge_three_false`

Solved: stated here without proof.

> Specker [Sp57] proved that when $α=ω^n$ for $3≤ n < \omega$ then it is not the case that any
> red/blue colouring of the edges of $K_α$ there is either a red $K_α$ or a blue $K_3$.

```lean
theorem erdos_590.variants.ge_three_false {n : ℕ} (h : 3 ≤ n) :
    ¬ OrdinalCardinalRamsey (ω ^ n) (ω ^ n) 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/590.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean#L60).

## `Erdos590.erdos_590.variants.finite_cardinal`

Solved: stated here without proof.

> Let m be a finite cardinal $< \omega$. Let $α$ be the infinite ordinal $\omega^{\omega}$.
> It was proved by Milnor that any red/blue colouring of the edges of $K_α$ there is either a
> red $K_α$ or a blue $K_3$. A shorter proof was found by Larson [La73]

```lean
theorem erdos_590.variants.finite_cardinal (m : ℕ) : OrdinalCardinalRamsey (ω ^ ω) (ω ^ ω) m
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/590.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/590.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/590.lean)
- [erdosproblems.com/590](https://www.erdosproblems.com/590)
