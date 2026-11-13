---
declaration: theorem
origin: cited
lean: Kourovka.«21.149».kourovka_21_149, Kourovka.«21.149».kourovka_21_149.variants.not_inner
statement: formalized
---

# Conjecture 21.149

> by A. V. Zenkov
>
> The problem is due to V. M. Kopytov and N. Ya. Medvedev. Its original form asked for an order
> automorphism of a Dlab group that is not inner (`kourovka_21_149.variants.not_inner`). After that
> form was solved, the problem was revised to the stronger question below [vDJMM, Appendix A].
> [GYZ] answered the revised question for order-preserving embeddings and rank-one slope groups.
>
> The Notebook does not define Dlab groups. We follow [Dl] and [GYZ]: the Dlab groups with slope
> group $H$ are four groups of order automorphisms of $I = [0, 1]$ and two groups of order
> automorphisms of the extended real line $\overline{\mathbb{R}}$. All six are viewed as subgroups
> of the order automorphisms of $\mathbb{R}$ (`IsDlabGroup`).
>
> *References:*
> - [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46), Problem 21.149. The original
>   wording is in [arXiv:1401.0300v43](https://arxiv.org/abs/1401.0300v43).
> - [GYZ] T. Gong, Y. Yang and M. R. Zeng, *An order automorphism of a Dlab group not induced by
>   conjugation*, [arXiv:2609.18630](https://arxiv.org/abs/2609.18630).
> - [vDJMM] W. van Doorn, E. Judin, P. Monticone and D. Morrison,
>   [arXiv:2607.17477](https://arxiv.org/abs/2607.17477).
> - [Dl] V. Dlab, *On a family of simple ordered groups*, J. Austral. Math. Soc. 8 (1968), 591–608.

*Quoted from [FormalConjectures/Kourovka/21_149.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/21_149.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Kourovka.«21.149».kourovka_21_149`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/kourovka-21-149-lean/blob/5c34c22661071d412f66a42009a1fe68db473b31/lean/Kourovka21149FC.lean#L5740-L5775](https://github.com/KitaKen1/kourovka-21-149-lean/blob/5c34c22661071d412f66a42009a1fe68db473b31/lean/Kourovka21149FC.lean#L5740-L5775).

> Are there order automorphisms of Dlab groups that are not induced by conjugation by elements of
> a (possibly bigger) Dlab group?
>
> A Dlab group $G$ (on $I$ or on $\overline{\mathbb{R}}$) carries Dlab's order, and $\alpha$ is an
> automorphism of $G$ that preserves it. The automorphism $\alpha$ is induced by conjugation in a
> bigger Dlab group $A$ if $G$ embeds into $A$ by an injective homomorphism $e$ and some $u \in A$
> satisfies $e(\alpha(f)) = u^{-1} e(f) u$ for all $f \in G$. This includes the inclusions and the
> order-preserving embeddings of [GYZ]. The slope groups are arbitrary.

```lean
theorem kourovka_21_149 :
    ∃ (K : Subgroup NNRealˣ) (G : Subgroup (ℝ ≃o ℝ)), IsDlabGroup K G ∧
      ∃ α : G ≃* G, (∀ f g : G, DlabLt (α f) (α g) ↔ DlabLt f g) ∧
        ¬ ∃ (H : Subgroup NNRealˣ) (A : Subgroup (ℝ ≃o ℝ)), IsDlabGroup H A ∧
          ∃ e : G →* A, Function.Injective e ∧ ∃ u : A, ∀ f : G, e (α f) = u⁻¹ * e f * u
```

Category `research solved`; AMS [06 Order, lattices, ordered algebraic structures](../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md), [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/21_149.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/21_149.lean#L105).

## `Kourovka.«21.149».kourovka_21_149.variants.not_inner`

Solved: stated here; a Lean proof is at [https://github.com/pitmonticone/Kourovka/blob/dcfdbdad8c434e30f6151fb3b4343364d70eeed4/Kourovka/Problem_21_149.lean#L770-L775](https://github.com/pitmonticone/Kourovka/blob/dcfdbdad8c434e30f6151fb3b4343364d70eeed4/Kourovka/Problem_21_149.lean#L770-L775); a Lean proof is at [https://github.com/KitaKen1/kourovka-21-149-lean/blob/5c34c22661071d412f66a42009a1fe68db473b31/lean/Kourovka21149FC.lean#L5777-L5786](https://github.com/KitaKen1/kourovka-21-149-lean/blob/5c34c22661071d412f66a42009a1fe68db473b31/lean/Kourovka21149FC.lean#L5777-L5786).

> The original form of the problem: are there order automorphisms of Dlab groups that are not inner
> automorphisms?
>
> This was answered affirmatively by the formal reasoning agent Aristotle (Harmonic), as reported
> in [vDJMM, Appendix A].

```lean
theorem kourovka_21_149.variants.not_inner :
    ∃ (K : Subgroup NNRealˣ) (G : Subgroup (ℝ ≃o ℝ)), IsDlabGroup K G ∧
      ∃ α : G ≃* G, (∀ f g : G, DlabLt (α f) (α g) ↔ DlabLt f g) ∧
        ¬ ∃ u : G, ∀ f : G, α f = u⁻¹ * f * u
```

Category `research solved`; AMS [06 Order, lattices, ordered algebraic structures](../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md), [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/21_149.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/21_149.lean#L125).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/21_149.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/21_149.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)
