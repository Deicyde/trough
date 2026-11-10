---
declaration: theorem
origin: cited
lean: Erdos516.erdos_516, Erdos516.erdos_516.variants.limsup_ratio_eq_one, Erdos516.erdos_516.variants.limsup_ratio_eq_one_of_hasFejerGaps
statement: formalized
---

# Erdős Problem 516

> *References:*
>  - [erdosproblems.com/516](https://www.erdosproblems.com/516)
>  - [Fu63] Fuchs, W. H. J., Proof of a conjecture of G. Pólya concerning gap series. Illinois J.
>     Math. (1963), 661--667.
>  - [Ko65] Kövari, Thomas, A gap-theorem for entire functions of infinite order. Michigan Math. J.
>     (1965), 133--140.
>  - [Ki26] Kitamura, Kenta, A Lean counterexample to the Fejér-gap variant of Erdős Problem 516.
>     [GitHub](https://github.com/KitaKen1/erdos-516-fejer-counterexample) (2026).

*Quoted from [FormalConjectures/ErdosProblems/516.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/516.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/516](https://www.erdosproblems.com/516).

The file states 3 research or textbook statements: 3 solved.

## `Erdos516.erdos_516`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos516.lean#L4812](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos516.lean#L4812).

> Let `f = ∑ aₖzⁿₖ` be an entire function of finite order such that `nₖ / k → ∞`.
> Then `limsup (fun r => ratio r f) atTop = 1`. This is proved in [Fu63].

```lean
theorem erdos_516 {f : ℂ → ℂ} {n : ℕ → ℕ}
    (hn : HasFabryGaps n) {a : ℕ → ℂ} (ha : ∀ n, a n ≠ 0)
    (hfn : ∀ z, HasSum (fun k => a k * z ^ n k) (f z)) (hf : OfFiniteOrder f) :
    limsup (fun r => ratio r f) atTop = 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/516.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/516.lean#L53).

## `Erdos516.erdos_516.variants.limsup_ratio_eq_one`

Solved: stated here without proof.

> Let `f = ∑ aₖzⁿₖ` be an entire function with strictly increasing exponents such that
> `nₖ > k (log k) ^ (2 + c)`. Then `limsup (fun r => ratio r f) atTop = 1`. This is proved in [Ko65].
> Without `StrictMono n`, repeated exponents let nonzero coefficients cancel, and `f = 0` satisfies
> the other hypotheses.

```lean
theorem erdos_516.variants.limsup_ratio_eq_one {f : ℂ → ℂ} {n : ℕ → ℕ} (hmono : StrictMono n)
    (hn : ∃ c > (0 : ℝ), ∀ k, n k > k * log k ^ (2 + c)) {a : ℕ → ℂ} (ha : ∀ n, a n ≠ 0)
    (hfn : ∀ z, HasSum (fun k => a k * z ^ n k) (f z)) :
    limsup (fun r => ratio r f) atTop = 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/516.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/516.lean#L64).

## `Erdos516.erdos_516.variants.limsup_ratio_eq_one_of_hasFejerGaps`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-516-fejer-counterexample/blob/675d078d1c9fee4fcaa1c1a2eecde1c174853ff5/lean/Erdos516FejerFC.lean#L1304-L1314](https://github.com/KitaKen1/erdos-516-fejer-counterexample/blob/675d078d1c9fee4fcaa1c1a2eecde1c174853ff5/lean/Erdos516FejerFC.lean#L1304-L1314).

> Is it true that for all entire functions `f = ∑ aₖzⁿₖ` such that `∑' 1 / nₖ < ∞`,
> `limsup (fun r => ratio r f) atTop = 1`?
>
> The answer is no: [Ki26] gives an explicit counterexample whose `limsup` is not `1`.

```lean
theorem erdos_516.variants.limsup_ratio_eq_one_of_hasFejerGaps :
    ¬ ∀ {f : ℂ → ℂ} {n : ℕ → ℕ} (hn : HasFejerGaps n) {a : ℕ → ℂ} (ha : ∀ n, a n ≠ 0)
    (hfn : ∀ z, HasSum (fun k => a k * z ^ n k) (f z)),
    limsup (fun r => ratio r f) atTop = 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/516.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/516.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/516.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/516.lean)
- [erdosproblems.com/516](https://www.erdosproblems.com/516)
