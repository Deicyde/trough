---
declaration: theorem
origin: cited
lean: CourtadeKumar.courtade_kumar, CourtadeKumar.variants.courtade_kumar_random_variable
statement: formalized
---

# The Courtade–Kumar (most informative Boolean function) conjecture

> Let $X$ be uniform on the Boolean cube $\{0,1\}^n$. Independently of $X$, let the coordinates of $Z$
> be i.i.d. Bernoulli random variables with parameter $p \in [0, 1]$, and put $Y = X \oplus Z$,
> so that $Y$ is the output of $n$ independent binary symmetric channels with crossover
> probability $p$ on input $X$. The **Courtade–Kumar conjecture** asserts that for every
> Boolean function $f : \{0,1\}^n \to \{0,1\}$,
>
>   $I(f(X); Y) \le 1 - h(p)$,
>
> where mutual information and binary entropy are measured in bits.
>
> The usual restriction to $p \in [0, 1/2]$ is equivalent to the range used here. For $p > 1/2$,
> complementing every output bit replaces $Z$ by its bitwise complement, which is i.i.d.
> Bernoulli($1 - p$) noise still independent of $X$; this bijective relabelling of the output
> preserves $I(f(X); Y)$, and $h(1 - p) = h(p)$.
>
> This file contains two formulations:
>
> * `CourtadeKumar.courtade_kumar` is the elementary finite-sum statement used by the external
>   Lean proof and its comparator check. Its definitions and statement are retained unchanged.
> * `CourtadeKumar.variants.courtade_kumar_random_variable` is the random-variable formulation.
>   Its product-law hypothesis specifies a uniform input and independent i.i.d. Bernoulli channel
>   noise, and its conclusion is about the mutual information of the actual random variables.
>
> `CourtadeKumar.courtade_kumar_iff_random_variable` proves that the two formulations are
> equivalent, without using either research statement. Shannon entropy and mutual information of
> finite-valued random variables are defined in
> `FormalConjecturesForMathlib.InformationTheory.FiniteEntropy`.
>
> For $n \ge 1$, coordinate dictators attain the bound: $I(X_i; Y) = I(X_i; Y_i) = 1 - h(p)$, since
> the other output coordinates are independent of $(X_i, Y_i)$. The test `mutualInfo_dictator`
> checks $n = 1$.
>
> *References:*
> - [CK14] T. A. Courtade and G. R. Kumar, *Which Boolean functions maximize mutual information on
>   noisy inputs?*, IEEE Trans. Inf. Theory 60 (2014), no. 8, 4515–4525.
>
> Independent work on the conjecture from September 2026, in alphabetical order:
> - [CGJLMNW26] Z. Chen, A. Gohari, A. Javanmard, H. Lin, V. Mirrokni, C. Nair, D. P. Woodruff,
>   *A Proof of the Most Informative Boolean Function Conjecture*,
>   [arXiv:2609.24931](https://arxiv.org/abs/2609.24931). A Lean 4 formalisation of the proof is at
>   https://github.com/dpwoodru/general-courtade-kumar-lean.
> - [KS26] D. Kramer and M. Saglam, *On the most informative Boolean function under noise*,
>   manuscript, https://github.com/deepinfra/courtade-kumar.
> - [KT26] Vu Khac Ky and Tuan Tran, *Dictators are most informative*,
>   [arXiv:2609.24184](https://arxiv.org/abs/2609.24184). See also their follow-up *Stability of
>   the Courtade–Kumar inequality*, [arXiv:2609.31797](https://arxiv.org/abs/2609.31797).
> - [MB26] H. Mahdavifar and A. Beirami, *The Most Informative Bit and Beyond: A Proof of the
>   Courtade–Kumar Conjecture and Multibit Extensions*,
>   [arXiv:2609.26444](https://arxiv.org/abs/2609.26444).

*Quoted from [FormalConjectures/Paper/CourtadeKumar.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CourtadeKumar.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 2 test statements and 4 API statements, counted here but not shown.

## `CourtadeKumar.courtade_kumar`

Solved: stated here; a Lean proof is at [https://github.com/dpwoodru/general-courtade-kumar-lean/blob/c3599c05181ad357331b701edf8fd8ec75c88305/verification/comparator/CKChallenge/Solution.lean#L6](https://github.com/dpwoodru/general-courtade-kumar-lean/blob/c3599c05181ad357331b701edf8fd8ec75c88305/verification/comparator/CKChallenge/Solution.lean#L6).

> **The Courtade–Kumar conjecture.** For every $n$, every Boolean function $f$ on
> $\{0,1\}^n$ and every crossover probability $p \in [0, 1]$, $I(f(X); Y) \le 1 - h(p)$.

```lean
theorem courtade_kumar (n : ℕ) (f : Cube n → Bool) (p : ℝ) (hp₀ : 0 ≤ p) (hp₁ : p ≤ 1) :
    mutualInfo f p ≤ 1 - binEntropyBits p
```

Category `research solved`; AMS [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/Paper/CourtadeKumar.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CourtadeKumar.lean#L119).

## `CourtadeKumar.variants.courtade_kumar_random_variable`

Solved: stated here; a Lean proof is at [https://github.com/dpwoodru/general-courtade-kumar-lean/blob/c3599c05181ad357331b701edf8fd8ec75c88305/verification/comparator/CKChallenge/Solution.lean#L6](https://github.com/dpwoodru/general-courtade-kumar-lean/blob/c3599c05181ad357331b701edf8fd8ec75c88305/verification/comparator/CKChallenge/Solution.lean#L6).

> **The Courtade–Kumar conjecture, in random-variable form.**
>
> The pushforward in the hypothesis is the joint distribution of $(X, Z)$. The uniform measure on
> `Cube n` is the law of $n$ i.i.d. Bernoulli($1/2$) bits. The product law makes the coordinates of
> $Z$ i.i.d. Bernoulli($p$) and makes the whole noise vector independent of $X$. In
> `bernoulliMeasure true false p`, `true` has probability $p$ and denotes a flip.
>
> Conditional on $X$, $Y = X \oplus Z$ flips each input coordinate independently with probability
> $p$: this is the memoryless binary symmetric channel with crossover probability $p$ from $X$ to
> $Y$. Every Boolean function is allowed, including constants. All maps between these finite
> discrete types are measurable, so $f \circ X$ and $Y$ are measurable. The conclusion is
> $I(f(X); Y) \le 1 - h(p)$ in bits, for the entire output vector $Y$.
>
> The linked proof proves the elementary statement `CourtadeKumar.courtade_kumar`, and
> `CourtadeKumar.courtade_kumar_iff_random_variable` transfers it to this formulation.

```lean
theorem courtade_kumar_random_variable :
    ∀ (n : ℕ) (f : Cube n → Bool) (p : ℝ) (hp₀ : 0 ≤ p) (hp₁ : p ≤ 1)
      (Ω : Type) [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]
      (X Z : Ω → Cube n),
      Measurable X →
      Measurable Z →
      μ.map (fun ω => (X ω, Z ω)) =
        (PMF.uniformOfFintype (Cube n)).toMeasure.prod
          (Measure.pi fun _ : Fin n =>
            ProbabilityTheory.bernoulliMeasure true false
              (⟨p, hp₀, hp₁⟩ : unitInterval)) →
      let Y : Ω → Cube n := fun ω => cubeXor (X ω) (Z ω)
      InformationTheory.mutualInformationBits μ (f ∘ X) Y ≤ 1 - binEntropyBits p
```

Category `research solved`; AMS [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/Paper/CourtadeKumar.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CourtadeKumar.lean#L164).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/CourtadeKumar.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CourtadeKumar.lean)
- [arXiv:2609.24931](https://arxiv.org/abs/2609.24931)
