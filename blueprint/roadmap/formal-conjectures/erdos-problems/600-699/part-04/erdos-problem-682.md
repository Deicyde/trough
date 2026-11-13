---
declaration: theorem
origin: cited
lean: Erdos682.erdos_682, Erdos682.erdos_682.variants.exceptional_count, Erdos682.erdos_682.variants.dickson_counterexample
statement: formalized
---

# Erdős Problem 682

> *References:*
> - [erdosproblems.com/682](https://www.erdosproblems.com/682)
> - [Er79d] Erdős, P., Some unconventional problems in number theory. Acta Math. Acad. Sci. Hungar.
>   (1979), 71-80.
> - [GaTa25] A. Gafni and T. Tao, Rough numbers between consecutive primes. arXiv:2508.06463 (2025).

*Quoted from [FormalConjectures/ErdosProblems/682.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/682.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/682](https://www.erdosproblems.com/682).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos682.erdos_682`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos682.lean#L5018](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos682.lean#L5018).

> Is it true that for almost all $n$ there exists some $m\in (p_n,p_{n+1})$ such that
>
> $$p(m) \geq p_{n+1}-p_n,$$
>
> where $p(m)$ denotes the least prime factor of $m$?
>
> This was solved in the affirmative by Gafni and Tao [GaTa25].
>
> This was formalized in Lean by Codex and GPT-5.6 Sol.

```lean
theorem erdos_682 :
    {n | ∃ m ∈ Set.Ioo (p n) (p (n + 1)), p (n + 1) - p n ≤ m.minFac}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/682.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/682.lean#L50).

## `Erdos682.erdos_682.variants.exceptional_count`

Solved: stated here without proof.

> Gafni and Tao [GaTa25, Theorem 1.1] proved that the number of exceptional gaps
> $(p_n,p_{n+1})$ with $p_n\in [X,2X]$ is
>
> $$\ll \frac{X}{(\log X)^2}.$$

```lean
theorem erdos_682.variants.exceptional_count :
    (fun X : ℕ ↦ ({n | p n ∈ Set.Icc X (2 * X) ∧
        ∀ m ∈ Set.Ioo (p n) (p (n + 1)), m.minFac < p (n + 1) - p n}.ncard : ℝ)) =O[atTop]
      fun X : ℕ ↦ (X : ℝ) / Real.log X ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/682.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/682.lean#L60).

## `Erdos682.erdos_682.variants.dickson_counterexample`

Textbook result, stated without proof. A Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos682.lean#L5222](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos682.lean#L5222).

> Erdős first thought this should be true for all large $n$, but found a (conditional)
> counterexample: Dickson's conjecture says there are infinitely many $d$ such that
>
> $$2183+30030d\textrm{ and }2201+30030d$$
>
> are both prime, and then they must necessarily be consecutive primes. These give a counterexample
> since $30030=2\cdot 3 \cdot 5\cdot 7\cdot 11\cdot 13$ and every integer in $[2184,2200]$ is
> divisible by at least one of these primes.
>
> This was formalized in Lean by Codex and GPT-5.6 Sol.

```lean
theorem erdos_682.variants.dickson_counterexample (d : ℕ) (h₁ : (2183 + 30030 * d).Prime)
    (h₂ : (2201 + 30030 * d).Prime) : ∃ n, p n = 2183 + 30030 * d ∧ p (n + 1) = 2201 + 30030 * d ∧
      ∀ m ∈ Set.Ioo (p n) (p (n + 1)), m.minFac < p (n + 1) - p n
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/682.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/682.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/682.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/682.lean)
- [erdosproblems.com/682](https://www.erdosproblems.com/682)
