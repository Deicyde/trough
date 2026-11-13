---
declaration: theorem
origin: cited
lean: IrvingLeather.irving_leather_pow_two, IrvingLeather.irving_leather_growth_rate
statement: formalized
---

# The Irving–Leather conjecture on stable matchings

> *References:*
> - [Concerning the maximum number of stable matchings in the stable marriage problem](https://core.ac.uk/download/pdf/82220141.pdf)
>   by E. G. Thurber, §2 and Appendix A.
> - [A recurrence giving a lower bound for stable matchings](https://oeis.org/A005154/a005154.pdf)
>   by Clay Thomas, Proposition 1.
>
> Let $M(n)$ be the maximum number of stable matchings with $n$ participants per side and complete,
> strict preferences. The Irving–Leather construction has $a_k$ stable matchings at size $2^k$.

*Quoted from [FormalConjectures/Paper/IrvingLeatherStableMatchings.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/IrvingLeatherStableMatchings.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `IrvingLeather.irving_leather_pow_two`

Open: stated without proof.

> Thurber's §2 attributes to Irving and Leather the conjecture that their construction attains
> the maximum number of stable matchings at every power-of-two size.

```lean
theorem irving_leather_pow_two (k : ℕ) :
    maxStableMatchings (2 ^ k) = irvingLeatherCount k
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/IrvingLeatherStableMatchings.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/IrvingLeatherStableMatchings.lean#L56).

## `IrvingLeather.irving_leather_growth_rate`

Open: stated without proof.

> A proposed weaker variant states that $M(n)^{1/n}$ and $a_k^{1/2^k}$ converge to the same real
> number. Thomas's recurrence analysis gives approximately $2.280142$ for the second limit.
> The first sequence is indexed by $n+1$ to start at positive sizes.

```lean
theorem irving_leather_growth_rate :
    ∃ c : ℝ,
      Tendsto (fun n : ℕ ↦ Real.rpow (maxStableMatchings (n + 1) : ℝ)
        (1 / ((n : ℝ) + 1))) atTop (𝓝 c) ∧
      Tendsto (fun k : ℕ ↦ Real.rpow (irvingLeatherCount k : ℝ)
        (1 / (2 : ℝ) ^ k)) atTop (𝓝 c)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/IrvingLeatherStableMatchings.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/IrvingLeatherStableMatchings.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/IrvingLeatherStableMatchings.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/IrvingLeatherStableMatchings.lean)
- [Concerning the maximum number of stable matchings in the stable marriage problem](https://core.ac.uk/download/pdf/82220141.pdf)
