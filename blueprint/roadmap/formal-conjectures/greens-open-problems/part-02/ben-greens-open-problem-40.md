---
declaration: theorem
origin: cited
lean: Green40.green_40, Green40.green_40.sanity_f_one, Green40.green_40.upper_bound, Green40.green_40.f_eq_one_for_all, Green40.green_40.f_two_eq_one, Green40.green_40.upper_bound_f_two, Green40.green_40.variants.arbitrary_subsets, Green40.green_40.variants.arbitrary_subsets_sanity_f_tilde_two, Green40.green_40.f_tilde_le_f, Green40.green_40.variants.all_n
statement: formalized
---

# Ben Green's Open Problem 40

> *References:*
> - [Gr24] [Ben Green's Open Problem 40](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.40)
> - [Da90] Davydov, Alexander Abramovich. "Construction of linear covering codes."
>   Problemy Peredachi Informatsii 26.4 (1990): 38-55.
> - [CHL97] Cohen, G., Honkala, I., Litsyn, S., & Lobstein, A. (1997). Covering codes (Vol. 54). Elsevier.
> - [St94] R. Struik, Covering codes, PhD Thesis, Eindhoven University of Technology, the Netherlands, 106 pp, 1994.

*Quoted from [FormalConjectures/GreensOpenProblems/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 5 open and 5 solved.

## `Green40.green_40`

Open: stated without proof.

> Does $f(r) \to \infty$? [Gr24]

```lean
theorem green_40 : Tendsto f atTop (𝓝 ⊤)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L64).

## `Green40.green_40.sanity_f_one`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green40_green_40_sanity_f_one.lean#L216](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green40_green_40_sanity_f_one.lean#L216).

> The only value known is $f(1) = 1$, which follows from the existence of the Hamming code [Gr24].

```lean
theorem green_40.sanity_f_one : f 1 = 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L70).

## `Green40.green_40.upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green40_green_40_upper_bound.lean#L245](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green40_green_40_upper_bound.lean#L245).

> $f(r) \le r^r / r! \sim e^r$ [Gr24].

```lean
theorem green_40.upper_bound (r : ℕ) : f r ≤ (r ^ r : ℝ≥0∞) / (r.factorial : ℝ≥0∞)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L76).

## `Green40.green_40.f_eq_one_for_all`

Open: stated without proof.

> The possibility that f(r) = 1 for all r has not been ruled out [Gr24]

```lean
theorem green_40.f_eq_one_for_all : ∀ r, f r = 1
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L81).

## `Green40.green_40.f_two_eq_one`

Open: stated without proof.

> It is not known whether f(2) = 1 [Gr24]

```lean
theorem green_40.f_two_eq_one : f 2 = 1
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L86).

## `Green40.green_40.upper_bound_f_two`

Solved: stated here without proof.

> The best-known upper bound for $f(2)$ is $1.4238$ [CHL97].

```lean
theorem green_40.upper_bound_f_two : f 2 ≤ (1.4238 : ℝ≥0∞)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L91).

## `Green40.green_40.variants.arbitrary_subsets`

Open: stated without proof.

> Does $\tilde{f}(r) \to \infty$? [Gr24]

```lean
theorem green_40.variants.arbitrary_subsets : Tendsto f_tilde atTop (𝓝 ⊤)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L113).

## `Green40.green_40.variants.arbitrary_subsets_sanity_f_tilde_two`

Solved: stated here without proof.

> It is known that $\tilde{f}(2) = 1$ [St94].

```lean
theorem green_40.variants.arbitrary_subsets_sanity_f_tilde_two : f_tilde 2 = 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L118).

## `Green40.green_40.f_tilde_le_f`

Proved here.

> We evidently have $\tilde{f}(r) \le f(r)$ [Gr24].

```lean
theorem green_40.f_tilde_le_f (r : ℕ) : f_tilde r ≤ f r
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L123).

## `Green40.green_40.variants.all_n`

Open: stated without proof.

> Does $f_{\text{all}}(r) \to \infty$? [Gr24]
>
> The target filter is `𝓝 ⊤`, as in `green_40` and `green_40.variants.arbitrary_subsets`. On
> `ℝ≥0∞`, `atTop` is the principal ultrafilter at `⊤`, so `Tendsto f_all atTop atTop` would say
> that `f_all r = ⊤` for all large `r` rather than that `f_all r → ∞`.

```lean
theorem green_40.variants.all_n : Tendsto f_all atTop (𝓝 ⊤)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/GreensOpenProblems/40.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean#L161).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/40.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/40.lean)
- [Ben Green's Open Problem 40](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.40)
