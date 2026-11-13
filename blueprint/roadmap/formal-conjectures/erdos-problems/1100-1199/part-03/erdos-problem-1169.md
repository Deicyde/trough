---
declaration: theorem
origin: cited
lean: Erdos1169.erdos_1169, Erdos1169.erdos_1169.variants.finite_blue_target, Erdos1169.erdos_1169.variants.hajnal_under_ch
statement: formalized
---

# Erdős Problem 1169

> *Reference:* [erdosproblems.com/1169](https://www.erdosproblems.com/1169)
>
> *References:*
> - [Ha71] Hajnal, A. *A negative partition relation.* Proc. Nat. Acad. Sci. U.S.A. 68 (1971),
>   pp. 142–144.

*Quoted from [FormalConjectures/ErdosProblems/1169.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1169.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1169](https://www.erdosproblems.com/1169).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1169.erdos_1169`

Open: stated without proof.

> Is it true that $\omega_1^2 \not\to (\omega_1^2, 3)^2$?
>
> A problem of Erdős and Hajnal. Hajnal [Ha71] proved this assuming the continuum hypothesis.
> The source's displayed relation has blue target $3$; its introductory $k$ does not occur
> in that relation. See also [erdosproblems.com/592](https://www.erdosproblems.com/592).

```lean
theorem erdos_1169 :
    ¬ OrdinalRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) ^ (2 : ℕ)) (3 : Ordinal)
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1169.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1169.lean#L50).

## `Erdos1169.erdos_1169.variants.finite_blue_target`

Open: stated without proof.

> The finite-blue-target form asks whether $\omega_1^2 \not\to (\omega_1^2, k)^2$
> for every $k \ge 3$. The restriction excludes $k \le 2$, where the positive relation holds.
> A colouring witnessing the negative relation with blue target $3$ also witnesses this form.

```lean
theorem finite_blue_target :
    ∀ k : ℕ, 3 ≤ k →
      ¬ OrdinalRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) ^ (2 : ℕ)) (k : Ordinal)
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1169.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1169.lean#L64).

## `Erdos1169.erdos_1169.variants.hajnal_under_ch`

Solved: stated here without proof.

> **Hajnal (1971), assuming CH.** Under the Continuum Hypothesis,
> $\omega_1^2 \not\to (\omega_1^2, k)^2$ holds for every finite $k \ge 3$.

```lean
theorem hajnal_under_ch (hCH : 𝔠 = ℵ_ 1) :
    ∀ k : ℕ, 3 ≤ k → ¬ OrdinalRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) ^ (2 : ℕ)) (k : Ordinal)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1169.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1169.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1169.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1169.lean)
- [erdosproblems.com/1169](https://www.erdosproblems.com/1169)
