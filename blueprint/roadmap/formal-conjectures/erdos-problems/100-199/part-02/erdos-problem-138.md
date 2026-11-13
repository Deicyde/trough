---
declaration: theorem
origin: cited
lean: Erdos138.monoAP_guarantee_set_nonempty, Erdos138.erdos_138, Erdos138.erdos_138.variants.prime, Erdos138.erdos_138.variants.upper, Erdos138.erdos_138.variants.quotient, Erdos138.erdos_138.variants.difference, Erdos138.erdos_138.variants.dvd_two_pow
statement: formalized
---

# Erdős Problem 138

> *References:*
> - [erdosproblems.com/138](https://www.erdosproblems.com/138)
> - [Be68] Berlekamp, E. R., A construction for partitions which avoid long arithmetic progressions. Canad. Math. Bull. (1968), 409-414.
> - [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann. Discrete Math. (1980), 89-115.
> - [Er81] Erdős, P., On the combinatorial problems which I would most like to see solved. Combinatorica (1981), 25-42.
> - [Go01] Gowers, W. T., A new proof of Szemerédi's theorem. Geom. Funct. Anal. (2001), 465-588.
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven
>   Formal Proof Search* by George Tsoukalas et al.
> - [CFS26] Campos, M., Fox, J. and Schildkraut, C., A new lower bound for two-color van der Waerden
>   numbers. [arXiv:2608.20824](https://arxiv.org/abs/2608.20824) (2026).
> - [OAI26] OpenAI, *Quantitative Superexponential Bounds for van der Waerden Numbers*. OpenAI Math
>   Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/138.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/138](https://www.erdosproblems.com/138).

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 2 test statements, counted here but not shown.

## `Erdos138.monoAP_guarantee_set_nonempty`

Solved: stated here without proof.

> Asserts that for any number of colors `r` and any progression length `k`, there
> always exists some number `N` large enough to guarantee a monochromatic arithmetic progression.
> In other words, the set `monoAP_guarantee_set` is non-empty. This is the fundamental existence
> result that allows for the definition of the van der Waerden numbers.

```lean
theorem monoAP_guarantee_set_nonempty (r k) : (monoAP_guarantee_set r k).Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L62).

## `Erdos138.erdos_138`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/ProgressionColoring/Main.lean#L12](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/ProgressionColoring/Main.lean#L12).

> In [Er80] Erdős asks whether
>
> $$ \lim_{k \to \infty} (W(k))^{1/k} = \infty $$
>
> Yes. This was proved by an internal OpenAI model in September 2026 [OAI26], which shows
> $W(k) > k^{k/100000}$ for all large $k$; see the linked Lean proof.

```lean
theorem erdos_138 : atTop.Tendsto (fun k => (W k : ℝ)^(1/(k : ℝ))) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L99).

## `Erdos138.erdos_138.variants.prime`

Solved: stated here without proof.

> When $p$ is prime Berlekamp [Be68] has proved $W(p+1) ≥ p^{2^p}$.

```lean
theorem erdos_138.variants.prime (p : ℕ) (hp : p.Prime) : p * (2 ^ p) ≤ W (p + 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L107).

## `Erdos138.erdos_138.variants.upper`

Solved: stated here without proof.

> Gowers [Go01] has proved
>
> $$W(k) \leq 2^{2^{2^{2^{2^{k+9}}}}.$$

```lean
theorem erdos_138.variants.upper (k : ℕ) : W k ≤ 2 ^ (2 ^ (2 ^ 2 ^ 2 ^ (k + 9)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L114).

## `Erdos138.erdos_138.variants.quotient`

Open: stated without proof.

> In [Er81] Erdős asks whether $\frac{W(k+1)}{W(k)} \to \infty$.

```lean
theorem erdos_138.variants.quotient :
    atTop.Tendsto (fun k => ((W (k + 1) : ℚ)/(W k))) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L121).

## `Erdos138.erdos_138.variants.difference`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/6ac8d0cbe1a85e71747c62c1391a84788015ebc1/FormalConjectures/ErdosProblems/138.lean#L844](https://github.com/mo271/formal-conjectures/blob/6ac8d0cbe1a85e71747c62c1391a84788015ebc1/FormalConjectures/ErdosProblems/138.lean#L844).

> In [Er81] Erdős asks whether $W(k+1) - W(k) \to \infty$.
>
> The DeepMind prover agent has found a formal proof of this statement.

```lean
theorem erdos_138.variants.difference :
    atTop.Tendsto (fun k => (W (k + 1) - W k)) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L133).

## `Erdos138.erdos_138.variants.dvd_two_pow`

Solved: stated here; a Lean proof is at [https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/Erdos138.lean#L1033](https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/Erdos138.lean#L1033).

> In [Er80] Erdős asks whether $W(k)/2^k\to \infty$.
>
> Campos, Fox and Schildkraut [CFS26] independently prove $W(k) \geq (1 - o(1)) k 2^{k-1}$, which
> implies this; they report that their proof was generated with ChatGPT. (The related variant
> `erdos_138.variants.difference`, $W(k+1) - W(k) \to \infty$, was solved separately in
> [arxiv/2605.22763].)
>
> Solved: a Lean 4 proof, derived from the Atlas proofs in
> [facebookresearch/atlas-lean](https://github.com/facebookresearch/atlas-lean), is linked in
> `formal_proof`.

```lean
theorem erdos_138.variants.dvd_two_pow :
    atTop.Tendsto (fun k => ((W k : ℚ)/ (2 ^ k))) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/138.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean#L153).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/138.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/138.lean)
- [erdosproblems.com/138](https://www.erdosproblems.com/138)
