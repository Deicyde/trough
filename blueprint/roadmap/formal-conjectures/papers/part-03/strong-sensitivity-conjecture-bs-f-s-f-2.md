---
declaration: theorem
origin: cited
lean: StrongSensitivityConjecture.strong_sensitivity_conjecture
statement: formalized
---

# Strong Sensitivity Conjecture (\`bs(f) ≤ s(f)^2\`)

> This file formalizes the *strong* sensitivity conjecture, asserting:
>
> For every Boolean function `f : {0,1}^n → {0,1}`,
> `bs(f) ≤ s(f)^2`,
> where bs(f) denotes block sensitivity and s(f) denotes sensitivity.
>
> Huang's theorem proves a *quartic* upper bound, `bs(f) ≤ s(f)^4`, thereby
> resolving the most widely known form of the sensitivity conjecture.
>
> We now ask whether a stronger upper bound holds. Interestingly, the original
> paper of Nisan and Szegedy, where the sensitivity conjecture first appeared,
> already speculated that a *quadratic* upper bound might be the correct
> relation. On the lower bound side, Rubinstein
> (https://link.springer.com/article/10.1007/BF01200762) constructed Boolean functions
> exhibiting the first quadratic separation. The best gap known before [OAI26],
> due to Ambainis and Sun (https://arxiv.org/abs/1108.3494), was
> `bs(f) ≥ (2/3)⋅s(f)^2`.
>
> In September 2026 an internal OpenAI model disproved the quadratic bound [OAI26]: it
> constructs total Boolean functions with `bs(f) / s(f)^2` arbitrarily large.
>
> *References:*
> * [OAI26] [A superquadratic separation between sensitivity and block sensitivity](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf)
>   by OpenAI, OpenAI Math Release preprint (2026)
> * [Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture](https://arxiv.org/abs/1907.00847)
>   by Hao Huang (see Section 3, Concluding Remarks)
> * [Variations on the Sensitivity Conjecture](https://arxiv.org/abs/1011.0354)
>   by Pooya Hatami, Raghav Kulkarni, and Denis Pankratov (see Question 3.1)
> * [On the Degree of Boolean Functions as Real Polynomials](https://link.springer.com/article/10.1007/BF01263419)
>   by Noam Nisan, and Mario Szegedy (see Section 4, Open Problems)

*Quoted from [FormalConjectures/Paper/StrongSensitivityConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/StrongSensitivityConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 3 test statements, counted here but not shown.

## `StrongSensitivityConjecture.strong_sensitivity_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Sensitivity/Separation.lean#L12](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Sensitivity/Separation.lean#L12).

> Strong Sensitivity Conjecture,
> for every Boolean function `f : {0,1}^n → {0,1}`,
> `bs(f) ≤ s(f)^2`.
>
> We call this the *strong* sensitivity conjecture because the original sensitivity
> conjecture only asked for a polynomial bound in terms of `s(f)`. Huang's
> celebrated result (often called the sensitivity theorem) gives a quartic bound,
> `bs(f) ≤ s(f)^4`, thereby settling the original conjecture.
>
> The quadratic bound is false. This was disproved by an internal OpenAI model in September 2026
> [OAI26]; see the linked Lean proof.

```lean
theorem strong_sensitivity_conjecture :
    ¬ ∀ (n : ℕ) (f : (Fin n → Bool) → Bool), blockSensitivity f ≤ sensitivity f ^ 2
```

Category `research solved`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Paper/StrongSensitivityConjecture.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/StrongSensitivityConjecture.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/StrongSensitivityConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/StrongSensitivityConjecture.lean)
- [A superquadratic separation between sensitivity and block sensitivity](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf)
