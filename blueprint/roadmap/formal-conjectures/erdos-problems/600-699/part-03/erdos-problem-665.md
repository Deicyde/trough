---
declaration: theorem
origin: cited
lean: Erdos665.erdos_665
statement: formalized
---

# Erdős Problem 665

> *References:*
> - [erdosproblems.com/665](https://www.erdosproblems.com/665)
> - [Er97f] Erdős, Paul, Some unsolved problems. Combinatorics, geometry and probability (Cambridge,
>   1993) (1997), 1-10.
> - [ErLa82] Erdős, P. and Larson, J., On pairwise balanced block designs with the sizes of blocks as
>   uniform as possible. Annals of Discrete Mathematics (1982), 129-134.
> - [ShSi85] S. S. Shrikhande and N. M. Singhi, On a problem of Erdős and Larson. Combinatorica
>   (1985), 351-358.

*Quoted from [FormalConjectures/ErdosProblems/665.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/665.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/665](https://www.erdosproblems.com/665).

The file states 1 research or textbook statement: 1 open.

## `Erdos665.erdos_665`

Open: stated without proof.

> A pairwise balanced design for $\{1,\ldots,n\}$ is a collection of sets $A_1,\ldots,A_m\subseteq
> \{1,\ldots,n\}$ such that $2\leq \lvert A_i\rvert \lt n$ and every pair of distinct elements $x,y\in
> \{1,\ldots,n\}$ is contained in exactly one $A_i$. Is there a constant $C>0$ and, for all large $n$,
> a pairwise balanced design such that
>
> $$\lvert A_i\rvert > n^{1/2}-C$$
>
> for all $1\leq i\leq m$?

```lean
theorem erdos_665 :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop,
    ∃ H : Finset (Finset (Fin n)), H.IsPairwiseBalancedDesign ∧
      ∀ e ∈ H, e.card < n ∧ Real.sqrt n - C < e.card
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/665.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/665.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/665.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/665.lean)
- [erdosproblems.com/665](https://www.erdosproblems.com/665)
