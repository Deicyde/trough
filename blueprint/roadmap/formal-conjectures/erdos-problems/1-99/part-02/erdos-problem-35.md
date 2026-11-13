---
declaration: theorem
origin: cited
lean: Erdos35.erdos_35, Erdos35.erdos_35.variants.plunnecke
statement: formalized
---

# Erdős Problem 35

> *References:*
> - [erdosproblems.com/35](https://www.erdosproblems.com/35)
> - [Er56] Erdős, P., *Problems and results in additive number theory*. Colloque sur la Théorie des
>   Nombres, Bruxelles, 1955 (1956), 127-137.
> - [Er36c] Erdős, P., *On the arithmetical density of the sum of two sequences, one of which forms
>   a basis for the integers*. Acta. Arith. (1936), 197-200.
> - [Pl70] Plünnecke, H., *Eine zahlentheoretische Anwendung der Graphentheorie*. J. Reine. Angew.
>   Math. (1970), 171-183.

*Quoted from [FormalConjectures/ErdosProblems/35.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/35.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/35](https://www.erdosproblems.com/35).

The file states 2 research or textbook statements: 2 solved.

## `Erdos35.erdos_35`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos35.lean#L1738](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos35.lean#L1738).

> Let $B\subseteq\mathbb{N}$ be an additive basis of order $k$ with $0\in B$. Is it true that for
> every $A\subseteq\mathbb{N}$ we have
>
> $$d_s(A+B)\geq \alpha+\frac{\alpha(1-\alpha)}{k},$$
>
> where $\alpha=d_s(A)$ and
>
> $$d_s(A) = \inf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N}$$
>
> is the Schnirelmann density?
>
> Erdős [Er36c] proved this is true with $k$ replaced by $2k$ in the denominator (in a stronger form
> that only considers $A\cup (A+b)$ for some $b\in B$, see [38](https://www.erdosproblems.com/38)).
>
> Ruzsa has observed that this follows immediately from the stronger fact proved by Plünnecke
> [Pl70] that (under the same assumptions, and for $\alpha>0$)
>
> $$d_S(A+B)\geq \alpha^{1-1/k}.$$

```lean
theorem erdos_35 : ∀ (B : Set ℕ) (k : ℕ), 0 ∈ B → B.IsAddBasisOfOrder k →
    ∀ A : Set ℕ, schnirelmannDensity A +
      schnirelmannDensity A * (1 - schnirelmannDensity A) / k ≤ schnirelmannDensity (A + B)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/35.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/35.lean#L58).

## `Erdos35.erdos_35.variants.plunnecke`

Solved: stated here without proof.

> Plünnecke [Pl70] proved that if $B\subseteq\mathbb{N}$ is an additive basis of order $k$ with
> $0\in B$ then $d_S(A+B)\geq d_s(A)^{1-1/k}$ for every $A\subseteq\mathbb{N}$ with $d_s(A)>0$.

```lean
theorem erdos_35.variants.plunnecke (B : Set ℕ) (k : ℕ) (h0 : 0 ∈ B) (hB : B.IsAddBasisOfOrder k)
    (A : Set ℕ) (hA : 0 < schnirelmannDensity A) :
    schnirelmannDensity A ^ (1 - (k : ℝ)⁻¹) ≤ schnirelmannDensity (A + B)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/35.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/35.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/35.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/35.lean)
- [erdosproblems.com/35](https://www.erdosproblems.com/35)
