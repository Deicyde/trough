---
declaration: theorem
origin: cited
lean: Erdos1167.erdos_1167, Erdos1167.erdos_1167.variants.finite_targets, Erdos1167.erdos_1167.variants.binary_colors, Erdos1167.erdos_1167.variants.infinite_targets, Erdos1167.erdos_1167.variants.r_eq_two
statement: formalized
---

# Erdős Problem 1167

> *References:*
> - [erdosproblems.com/1167](https://www.erdosproblems.com/1167)
> - [EHMR84] P. Erdős, A. Hajnal, A. Máté and R. Rado, *Combinatorial set theory: partition
>   relations for cardinals*. Studies in Logic and the Foundations of Mathematics 106,
>   North-Holland (1984).
>
> The original Erdős–Hajnal problem list gives the additional conditions $\gamma \geq 2$, $r < \omega$,
> and $\kappa_\alpha > r$. Without $\gamma \geq 2$, the statement is false: taking $\gamma = 1$ and
> $\kappa_0 = \aleph_1$ with $\lambda = \aleph_0$ gives a counterexample, since the partition relation
> with one color degenerates to a cardinality comparison (see `erdos_1167.unrestricted_is_false`).
> Without $\kappa_\alpha > r$ it is also false: with $r = 2$, $\lambda = \aleph_0$ and targets
> $(2, \aleph_1)$, the premise $2^{\aleph_0} \to (3, \aleph_1)^3$ holds, but a constant colouring
> of the pairs of $\aleph_0$ has neither a red pair nor a blue set of size $\aleph_1$.

*Quoted from [FormalConjectures/ErdosProblems/1167.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1167](https://www.erdosproblems.com/1167).

The file states 5 research or textbook statements: 4 open and 1 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `Erdos1167.erdos_1167`

Open: stated without proof.

> **Erdős Problem 1167.** Let $r \geq 2$ be finite, $\gamma \geq 2$, and $\lambda$ be an infinite
> cardinal. Let $\kappa_\alpha > r$ be cardinals for all $\alpha < \gamma$. Is it true
> that
>
> $$2^\lambda \to (\kappa_\alpha + 1)_{\alpha < \gamma}^{r+1}$$
>
> implies
>
> $$\lambda \to (\kappa_\alpha)_{\alpha < \gamma}^r?$$
>
> Here $+$ means cardinal addition, so that $\kappa_\alpha + 1 = \kappa_\alpha$
> if $\kappa_\alpha$ is infinite.
>
> A problem of Erdős, Hajnal, and Rado.

```lean
theorem erdos_1167 :
    ∀ (r : ℕ), 2 ≤ r →
    ∀ (lam : Cardinal.{u}), ℵ₀ ≤ lam →
    ∀ (γ : Ordinal.{u}), 2 ≤ γ →
    ∀ (κ : γ.ToType → Cardinal.{u}), (∀ α, (r : Cardinal.{u}) < κ α) →
      cardinalPartitionRel ((2 : Cardinal.{u}) ^ lam) (r + 1) γ (fun α => κ α + 1) →
      cardinalPartitionRel lam r γ κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1167.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean#L59).

## `Erdos1167.erdos_1167.variants.finite_targets`

Solved: stated here; a Lean proof is at [https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos1167.lean#L990](https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos1167.lean#L990).

> **Finite-target case.** When all $\kappa_\alpha$ are finite, $\kappa_\alpha + 1$
> is the ordinary natural-number successor. Special case of `erdos_1167`.
>
> This case was proved by Erdős, Hajnal, Máté and Rado [EHMR84], using the Erdős–Rado tree
> argument and the negative stepping-up lemma. The statement omits the condition $n_\alpha > r$.
> This is harmless, since a colouring that witnesses
> $\lambda \not\to (n_\alpha)^r_{\alpha < \gamma}$ can only use colours $\alpha$ with $n_\alpha > r$.

```lean
theorem finite_targets (r : ℕ) (hr : 2 ≤ r) (lam : Cardinal.{u}) (hlam : ℵ₀ ≤ lam)
    (γ : Ordinal.{u}) (hγ : 2 ≤ γ) (n : γ.ToType → ℕ) :
    cardinalPartitionRel ((2 : Cardinal.{u}) ^ lam) (r + 1) γ
        (fun α => (n α : Cardinal.{u}) + 1) →
    cardinalPartitionRel lam r γ (fun α => (n α : Cardinal.{u}))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1167.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean#L82).

## `Erdos1167.erdos_1167.variants.binary_colors`

Open: stated without proof.

> **Binary-color case.** The $\gamma = 2$ specialization (two color classes).

```lean
theorem binary_colors (r : ℕ) (hr : 2 ≤ r) (lam : Cardinal.{u}) (hlam : ℵ₀ ≤ lam)
    (κ : (2 : Ordinal.{u}).ToType → Cardinal.{u}) (hκ : ∀ α, (r : Cardinal.{u}) < κ α) :
    cardinalPartitionRel ((2 : Cardinal.{u}) ^ lam) (r + 1) 2 (fun α => κ α + 1) →
    cardinalPartitionRel lam r 2 κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1167.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean#L93).

## `Erdos1167.erdos_1167.variants.infinite_targets`

Open: stated without proof.

> **Infinite-target case.** When all $\kappa_\alpha \geq \aleph_0$ are infinite and bounded by
> $\lambda$, $\kappa_\alpha + 1 = \kappa_\alpha$, so the hypothesis simplifies to a "pure"
> stepping-down lemma:
>
> $$2^\lambda \to (\kappa_\alpha)_{\alpha\lt \gamma}^{r+1} \implies
>    \lambda \to (\kappa_\alpha)_{\alpha\lt \gamma}^r.$$
>
> The condition $\kappa_\alpha \leq \lambda$ is needed to avoid a size obstruction: without it, the
> conclusion would require a subset of $\lambda$ of size $\kappa_\alpha > \lambda$, which is impossible
> (see `infinite_targets_needs_bound`).

```lean
theorem infinite_targets (r : ℕ) (hr : 2 ≤ r) (lam : Cardinal.{u}) (hlam : ℵ₀ ≤ lam)
    (γ : Ordinal.{u}) (hγ : 2 ≤ γ) (κ : γ.ToType → Cardinal.{u}) (hκ : ∀ i, ℵ₀ ≤ κ i)
    (hκ_le : ∀ i, κ i ≤ lam) :
    cardinalPartitionRel ((2 : Cardinal.{u}) ^ lam) (r + 1) γ κ →
    cardinalPartitionRel lam r γ κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1167.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean#L110).

## `Erdos1167.erdos_1167.variants.r_eq_two`

Open: stated without proof.

> **$r = 2$ case.** The stepping-down from 3-uniform to 2-uniform partition
> relations: $2^\lambda \to (\kappa_\alpha + 1)_{\alpha\lt \gamma}^3$ implies
> $\lambda \to (\kappa_\alpha)_{\alpha\lt \gamma}^2$. Generalises the classical
> Erdős–Rado stepping-up/down theorem for pairs.

```lean
theorem r_eq_two (lam : Cardinal.{u}) (hlam : ℵ₀ ≤ lam)
    (γ : Ordinal.{u}) (hγ : 2 ≤ γ) (κ : γ.ToType → Cardinal.{u})
    (hκ : ∀ α, (2 : Cardinal.{u}) < κ α) :
    cardinalPartitionRel ((2 : Cardinal.{u}) ^ lam) 3 γ (fun α => κ α + 1) →
    cardinalPartitionRel lam 2 γ κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1167.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1167.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1167.lean)
- [erdosproblems.com/1167](https://www.erdosproblems.com/1167)
